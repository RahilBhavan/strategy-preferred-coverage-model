"""Set native Excel calculation metadata missing from Artifact Tool's exporter.

Does not author or evaluate financial formulas. Run after build.mjs.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as E
import os, tempfile

root=Path(__file__).resolve().parents[1]
p=root/'Strategy_Preferred_Coverage_Model.xlsx'
ns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
E.register_namespace('',ns)
with tempfile.NamedTemporaryFile(dir=p.parent,suffix='.xlsx',delete=False) as tmp: out=Path(tmp.name)
try:
 with ZipFile(p) as z,ZipFile(out,'w',ZIP_DEFLATED) as d:
  for name in z.namelist():
   data=z.read(name)
   if name=='xl/workbook.xml':
    t=E.fromstring(data);c=t.find('{'+ns+'}calcPr')
    if c is None:c=E.SubElement(t,'{'+ns+'}calcPr')
    c.attrib.update(calcId='0',calcMode='auto',fullCalcOnLoad='1',forceFullCalc='1')
    data=E.tostring(t,encoding='utf-8',xml_declaration=True)
   d.writestr(name,data)
 os.replace(out,p)
finally:
 if out.exists():out.unlink()
print('Set automatic full recalculation on open')
