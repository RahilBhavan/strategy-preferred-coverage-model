"""Check arithmetic and navigation; does not execute Excel or assess a learner."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import math
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = ROOT / 'verification-previews/course'
checks = 0


def close(actual, expected):
    global checks
    assert math.isclose(actual, expected, abs_tol=.000002), (actual, expected)
    checks += 1


def cash_path(cash, uses, limit, capacity, planned=None):
    rows = []
    for i, use in enumerate(uses):
        issue = min(limit, capacity, max(use-cash, 0) if planned is None else planned[i])
        capacity -= issue
        shortage = max(use-cash-issue, 0)
        cash = max(cash+issue-use, 0)
        rows.append((cash, issue, capacity, shortage))
    return rows


def treasury(action, deploy, stress):
    cash, coins, debt, shares, pref = 100., 10000., 200., 100., 200.
    proceeds = {'none': 0, 'common': 198, 'preferred': 196}[action]
    if action == 'common':
        shares += 200/11
    if action == 'preferred':
        pref += 250
    if deploy:
        coins += proceeds*1e6/100000
    else:
        cash += proceeds
    rows = []
    for q in range(1, 9):
        price = (50000 if q <= 4 else 50000+(q-4)*12500) if stress else 100000
        rate = .18 if stress and q >= 5 else .12
        interest = debt*.02/4
        payout = 100*.10/4 + 100*rate/4
        payout += 250*.10/4 if action == 'preferred' else 0
        principal = 60 if q == 4 else 140 if q == 8 else 0
        use = interest+payout+principal
        sale_dollars = max(use-cash, 0)
        sold = sale_dollars*1e6/price
        assert sold <= coins
        coins -= sold
        cash += sale_dollars-use
        debt -= principal
        rows.append(dict(cash=cash, coins=coins, sold=sold, use=use, interest=interest))
    return rows, (coins*price/1e6+cash-debt-pref)/shares


def arithmetic():
    values = [
        (sum(c/1.08**t for t, c in enumerate([6, 6, 106], 1)), 94.845806),
        (6/94.8458060255*100, 6.326057),
        (math.sqrt(1.4*.7)-1, -.0100505063), (1.08/1.03-1, .0485436893),
        ((120+15-12)/66, 1.863636), ((200+30-2-60-40)/60, 2.133333),
        ((220-60-40)/60, 2), (340/106, 3.207547), (6/(340/106), 1.870588),
        ((120+30-1)/70, 2.128571), (110/84-1, .3095238095),
        (100/1.06**4, 79.209366), (5/1.1+6/1.1**2+82/1.1**3, 71.111946),
        (1.2+.5*math.log(.8), 1.088428), (1.2+.5*math.log(.3), .598014),
        (4/1.08+104/1.08**2, 92.866941), (88*1.2-110, -4.4),
        (998/(100+200/11), 8.444615)]
    for actual, expected in values:
        close(actual, expected)
    assert cash_path(30, [8, 28, 8, 8], 12, 20) == [
        (22, 0, 20, 0), (0, 6, 14, 0), (0, 8, 6, 0), (0, 6, 0, 2)]
    close(sum(r[3] for r in cash_path(10, [3, 3, 7, 3], 2, 6)), 2)
    close(sum(r[3] for r in cash_path(10, [3, 3, 7, 3], 2, 6, [0, 2, 2, 2])), 0)
    close(sum(r[3] for r in cash_path(15, [4, 14, 4, 4], 3, 10)), 2)
    close(sum(r[3] for r in cash_path(15, [4, 14, 4, 4], 3, 10, [3, 3, 1, 3])), 1)
    cases = [('none', False, False, 8492, 0), ('common', False, False, 10000, 47.2),
             ('preferred', False, False, 9952, 0), ('common', True, False, 10472, 0),
             ('preferred', True, False, 9952, 0), ('none', False, True, 8416.333333, 0),
             ('common', False, True, 10000, 41.2), ('preferred', False, True, 9892, 0),
             ('common', True, True, 10396.333333, 0),
             ('preferred', True, True, 9631.871429, 0)]
    for action, deploy, stress, coins, cash in cases:
        rows, residual = treasury(action, deploy, stress)
        close(rows[-1]['coins'], coins)
        close(rows[-1]['cash'], cash)
        close(sum(r['interest'] for r in rows), 6.8)
        assert residual > 0
    rows, _ = treasury('preferred', True, True)
    for row, sold in zip(rows[3:], [220, 223.2, 186, 159.428571, 1539.5]):
        close(row['sold'], sold)
    key = (HERE/'solutions-exams.md').read_text()
    for anchor in ['8.444615', '250.8', '47.2', '41.2', '2,328.128571', '9,631.871429']:
        assert anchor in key, anchor


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if 'id' in attrs:
            self.ids.add(attrs['id'])


def content():
    global checks
    assert len(re.findall(r'^\*\*\d+\.', (HERE/'README.md').read_text(), re.M)) == 16
    assert len(re.findall(r'^\*\*[ABCD]\d\.', (HERE/'problem-sets.md').read_text(), re.M)) == 24
    assert len(re.findall(r'^## \d+\.', (HERE/'excel-labs.md').read_text(), re.M)) == 16
    assert sum([10]*4+[20, 15, 20, 5]) == 100
    for source in HERE.glob('*.md'):
        assert source.stat().st_size < 20000, source
        for link in re.findall(r'\]\(([^)]+)\)', source.read_text()):
            if not urlsplit(link).scheme:
                assert (source.parent/link).exists(), (source, link)
    parsed = {}
    for file in OUTPUT.glob('*.html'):
        parser = Links()
        parser.feed(file.read_text())
        parsed[file.resolve()] = parser
    assert len(parsed) == 15, len(parsed)
    for file, page in parsed.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path and not url.fragment:
                continue
            dest = (file.parent/unquote(url.path)).resolve() if url.path else file
            assert dest.exists(), (file.name, link)
            if url.fragment and dest in parsed:
                assert unquote(url.fragment) in parsed[dest].ids, (file.name, link)
            checks += 1
    assert '8416.333333' not in (OUTPUT/'assessments.html').read_text()


if __name__ == '__main__':
    arithmetic()
    content()
    print(f'{checks} arithmetic and navigation checks passed; learner/Excel behavior not assessed.')
