import { fileURLToPath } from 'node:url';
import fs from 'node:fs/promises';
import {FileBlob,SpreadsheetFile} from '@oai/artifact-tool';
const root=fileURLToPath(new URL('..',import.meta.url)).replace(/\/$/,'');
const w=await SpreadsheetFile.importXlsx(await FileBlob.load(root+'/model/template.xlsx'));
const old=JSON.parse(await fs.readFile(root+'/model/original-layout.json','utf8'));
const S=n=>w.worksheets.getItem(n);
const v=(s,c,x)=>S(s).getRange(c).values=[[x]];
const f=(s,c,x)=>S(s).getRange(c).formulas=[[x]];
const nm=k=>{const [s,c]=old.names[k].replaceAll("'",'').split('!');return [s,c.replaceAll('$','')];};
const nf=(k,x)=>f(...nm(k),x);
const nv=(k,x)=>v(...nm(k),x);
const add=n=>{const s=w.worksheets.add(n);s.showGridLines=false;s.getRange('A1:V75').format.font={name:'Arial',size:10,color:'#000000'};s.getRange('A1:A75').format.columnWidth=48;s.getRange('B1:V75').format.columnWidth=14;s.freezePanes.freezeRows(4);return s;};
const title=(s,t,n)=>{v(s,'A1',t);S(s).getRange('A1').format.font={size:16,bold:true};v(s,'A2',n);S(s).getRange('A2:H2').format.rowHeight=32;};
const head=(s,c,a)=>{S(s).getRange(c).values=[a];S(s).getRange(c).format={fill:'#1F2937',font:{bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:36};};
const input=(s,c,x,fmt)=>{v(s,c,x);S(s).getRange(c).format.font.color='#0000FF';if(fmt)S(s).getRange(c).setNumberFormat(fmt);};
const fmt=(s,c,x)=>S(s).getRange(c).setNumberFormat(x);
const notes='https://www.strategy.com/notes';
const q2='https://www.sec.gov/Archives/edgar/data/1050446/000105044626000044/mstr-20260630.htm';
add('Net NAV');add('Quarterly path');add('Native sensitivity');add('Excel review');
title('Net NAV','Net mNAV bridge','Current definition. Inputs in millions except per-share prices. Estimated basic shares and dated awards need Q3 refresh.');
head('Net NAV','A4:H4',['Note','Face ($m)','Conversion price','Put date','OTM claim ($m)','ITM shares (m)','Coupon','Source']);
const ds=[['2028',1010,183.19,'2027-09-15',.00625],['2029',1500,672.4,'2028-06-01',0],['2030A',800,149.77,'2028-09-15',.00625],['2030B',2000,433.43,'2028-03-01',0],['2031',603.659,232.72,'2028-09-15',.00875],['2032',800,204.33,'2029-06-15',.0225]];
for(let i=0;i<ds.length;i++){let r=i+5,[name,face,cp,d,rate]=ds[i];v('Net NAV','A'+r,name);input('Net NAV','B'+r,face);input('Net NAV','C'+r,cp);v('Net NAV','D'+r,new Date(d+'T00:00:00Z'));fmt('Net NAV','D'+r,'yyyy-mm-dd');f('Net NAV','E'+r,`=IF(MSTR_Price<C${r},B${r},0)`);f('Net NAV','F'+r,`=IF(MSTR_Price>=C${r},B${r}/C${r},0)`);input('Net NAV','G'+r,rate,'0.000%');v('Net NAV','H'+r,q2);}
const netRows={12:['Basic shares (m), rolled estimate','=MSTR_Shares'],13:['Awards (m), Q2 anchor',3.950554],14:['STRK conversion price',1000],15:['STRK in-money shares (m)','=IF(MSTR_Price>=B14,Notional_STRK_In/B14,0)'],16:['Fully diluted shares (m)','=SUM(B12:B13)+SUM(F5:F10)+B15'],17:['Out-of-money convertible claims ($m)','=SUM(E5:E10)'],18:['Preferred claims ($m)','=Pref_Notional_Spot-IF(MSTR_Price>=B14,Notional_STRK_In,0)'],19:['Net BTC value ($m)','=BTC_NAV_Now+USD_Reserve+USD_Cash-B17-B18'],20:['Net mNAV','=IF(B19>0,MSTR_Price*B16/B19,NA())'],21:['Enterprise-value mNAV (legacy)','=EV_Now/BTC_NAV_Now'],22:['Basic mNAV','=MSTR_MktCap_Now/BTC_NAV_Now'],23:['Net BTC per diluted share','=B19*1000000/BTC_Spot/(B16*1000000)']};
for(const [r,[label,x]] of Object.entries(netRows)){v('Net NAV','A'+r,label);typeof x==='string'?f('Net NAV','B'+r,x):input('Net NAV','B'+r,x);}
fmt('Net NAV','B12:F23','#,##0.000');fmt('Net NAV','B20:B22','0.000"x"');v('Net NAV','H13',q2+' (options + RSU + PSU anchor)');v('Net NAV','A25','Moneyness uses >= conversion price, matching current issuer notes. dat-accretion currently uses >; equality is the only boundary difference.');v('Net NAV','A26','Net definition excludes other secured debt, retained separately in cash interest and BTC gross-claim coverage.');v('Net NAV','A27','USD Assets use Reserve + USD Cash; STRE uses model FX, not a certified Friday BFIX. This is an estimated reconstruction.');v('Net NAV','A28',notes);v('Net NAV','A29','Snapshot sensitivities freeze observed moneyness. The path reclassifies on prior-quarter price, avoiding circular calculations.');
nf('mNAV_Now',"='Net NAV'!B20");v('Liquidity','A10','Net mNAV (estimated reconstruction)');v('Liquidity','D10','Price / net BTC value per fully diluted share. See Net NAV for claims and dilution.');
nf('EV_Live',"=L_mNAV*(BTC_NAV_Live+'Net NAV'!B19-BTC_NAV_Now)+Debt_Principal+Pref_Notional_Total-Cash_For_EV");
nf('MSTR_Price_Live',"=MktCap_Live/'Net NAV'!B16");
v('Liquidity','D13','Reconstructed from net equity value; observed moneyness held fixed in snapshot scenarios.');
v('Liquidity','D16','Market cap / fully diluted shares. Matches observed price in Base.');
const oldmc='MAX(0,{m}*BTC_Held*{P}/1000000-Debt_Principal-Pref_Notional_Total+Cash_For_EV)';
for(const [name,cells] of Object.entries(old.sheets))for(const x of cells){if(typeof x.v!=='string')continue;let z=x.v;
 if(z.startsWith('=')){
 z=z.replace(/MAX\(0,([^,]+)\*BTC_Held\*([^,]+)\/1000000-Debt_Principal-Pref_Notional_Total\+Cash_For_EV\)/g,"MAX(0,$1*(BTC_Held*$2/1000000+'Net NAV'!B19-BTC_NAV_Now))");
 // Snapshot scenario comparisons and sensitivities use the same observed net claims.
 z=z.replace(/=([A-Z]+\d+)\*([A-Z]+\d+)-Debt_Principal-Pref_Notional_Total\+Cash_For_EV/g,"=MAX(0,$1*($2+'Net NAV'!B19-BTC_NAV_Now))");
 if(name==='Stress')z=z.replaceAll('/MSTR_Shares',"/'Net NAV'!B16");
 if(z!==x.v)f(name,x.cell,z);
 }
}
nf('BE_BTC_Target',`=IF(Common_Needed=0,"Reserve alone covers it",IF((Reserve_Live+ATM_Cap)/Charges_Total<Target_Years,"Not reachable: ATM capacity",IF(Gate_Closed,"Not reachable: below mNAV floor",(Common_Needed*'Net NAV'!B16/(L_ADV*L_Part*Trading_Days*L_mNAV)-'Net NAV'!B19+BTC_NAV_Now)*1000000/BTC_Held)))`);
for(const c of ['B','C','D','E','F']){
 f('Dashboard',c+'38',`=MAX(0,${c}33*(BTC_Held*${c}32/1000000+Cash_For_EV-'Net NAV'!B17-${c}37+IF(MSTR_Price>='Net NAV'!B14,Notional_STRK_In,0)))`);
 f('Dashboard',c+'39',`=IF(AND(Gate_On="Yes",${c}33<mNAV_Floor),0,Scenarios!${c}12*${c}38/'Net NAV'!B16*Scenarios!${c}13*Trading_Days)`);
}
nv('Participation',.02); // Uncalibrated starting assumption, explicit in source note.
const part=nm('Participation')[1];v('Inputs',part.replace('B','F'),'Model assumption, 2% maximum. Path further scales demand by premium and BTC drawdown; no historical calibration claimed.');
title('Native sensitivity','Native Excel What-If Data Tables','Both tables replace actual input cells on this sheet. Snapshot runway excludes principal; see Quarterly path for puts.');
head('Native sensitivity','A4:C4',['Driver','Active input','Source / control']);
const levers=[[5,'BTC price',6],[6,'Net mNAV',7],[7,'STRC rate',8],[8,'EUR/USD',10]];
for(const [r,label,sr] of levers){v('Native sensitivity','A'+r,label);f('Native sensitivity','B'+r,`=INDEX(Scenarios!B${sr}:F${sr},MATCH(Scenario_Select,Scenarios!$B$4:$F$4,0))`);f('Scenarios','H'+sr,`='Native sensitivity'!B${r}`);}
v('Native sensitivity','A10','Years covered by Reserve + common');f('Native sensitivity','B10','=Cov_Years_Total');
v('Native sensitivity','A11','Reserve months');f('Native sensitivity','B11','=Cov_Reserve_Months');
f('Native sensitivity','D5','=B10');S('Native sensitivity').getRange('E5:K5').values=[[.6,.8,1,1.25,1.5,2,2.5]];
S('Native sensitivity').getRange('D6:D14').values=[30000,40000,50000,60000,75000,100000,125000,150000,200000].map(x=>[x]);
S('Native sensitivity').dataTables.add('D5:K14',{rowInput:'B6',columnInput:'B5'});fmt('Native sensitivity','E6:K14','0.0" yrs"');fmt('Native sensitivity','E5:K5','0.00"x"');
f('Native sensitivity','D19','=B11');S('Native sensitivity').getRange('E19:H19').values=[[1,1.1,1.2,1.3]];S('Native sensitivity').getRange('D20:D25').values=[.10,.11,.12,.13,.14,.15].map(x=>[x]);
S('Native sensitivity').dataTables.add('D19:H25',{rowInput:'B8',columnInput:'B7'});fmt('Native sensitivity','E20:H25','0.0" mo"');fmt('Native sensitivity','D20:D25','0.0%');
v('Native sensitivity','D16','Columns: net mNAV. Rows: BTC price. Observed conversion classification held fixed.');v('Native sensitivity','D27','Columns: EUR/USD. Rows: STRC rate. Native Excel recalculation remains to be checked on Mac.');
title('Quarterly path','Five-year liquidity path','Cash fixed charges plus full cash puts. All dollars in millions. Unfunded amounts remain visible; no automatic refinancing.');
v('Quarterly path','A3','Case selected');f('Quarterly path','B3','=Scenario_Select');
const settings=[[5,'BTC annual recovery after initial shock',0],[6,'Premium sensitivity to log BTC change',.6],[7,'Demand sensitivity to BTC drawdown',1],[8,'Premium cushion for demand factor',.25],[9,'Cash put election, 1 = all puts',1],[10,'Issuance transaction cost',.01],[11,'STRC monthly VWAP assumption',99.5],[12,'Use February rate framework? 1=yes',0],[13,'Rate increase below $95',.005],[14,'Rate increase $95 to <$99',.0025],[15,'Rate decrease at >=$101',-.0025],[16,'Illustrative rate floor',0],[17,'Illustrative rate ceiling',.20]];
head('Quarterly path','A4:C4',['Path assumption','Value','Basis']);
for(const [r,label,x] of settings){v('Quarterly path','A'+r,label);input('Quarterly path','B'+r,x);v('Quarterly path','C'+r,'Model assumption');}
fmt('Quarterly path','B5','0.0%');fmt('Quarterly path','B10','0.0%');fmt('Quarterly path','B13:B17','0.00%');
v('Quarterly path','A19','Rate rule is an optional illustration. Current announced rate is default; later hold-near-par policy supersedes February bands.');
v('Quarterly path','A20','Framework uses monthly VWAP, not the last trade. Three monthly steps per full quarter; no market-price feedback forecast.');
v('Quarterly path','A21','STRC rule sources: February results and June capital framework. Ceiling/floor and fixed VWAP are model assumptions.');
v('Quarterly path','C13','https://www.strategy.com/press/strategy-announces-fourth-quarter-2025-financial-results_02-05-2026');
v('Quarterly path','C12','https://www.strategy.com/press/strategy-announces-digital-credit-capital-framework_06-29-2026');
const labels={24:'Quarter end',25:'Quarter starts',26:'Year fraction',27:'BTC price',28:'Net mNAV assumption',29:'Demand factor',30:'Opening cash',31:'Opening ATM capacity',32:'Opening basic shares (m)',33:'Prior price for moneyness',34:'Remaining OTM note claims',35:'Remaining ITM note shares (m)',36:'Preferred claims for net NAV',37:'Fully diluted shares (m)',38:'Net BTC value ($m)',39:'Implied MSTR price',40:'STRC annual rate',41:'Preferred cash accrual',42:'Debt interest accrual',43:'Total cash charges',44:'Holder puts: full cash need',45:'Volume-limited gross common proceeds',46:'Gross common issued',47:'Issuance fees',48:'Net proceeds',49:'Ending cash',50:'Unfunded amount this quarter',51:'Cumulative unfunded amount',52:'Ending ATM capacity',53:'New common shares (m)',54:'Ending basic shares (m)',55:'Months of charges in cash',56:'Policy shortfall ($m)',57:'Cash equation residual',58:'Put risk: notes below conversion',59:'Debt remaining after puts'};
for(const [r,l] of Object.entries(labels))v('Quarterly path','A'+r,l);
const col=i=>String.fromCharCode(66+i);
for(let i=0;i<20;i++){
 const c=col(i),p=col(i-1);let end=new Date(Date.UTC(2026,12+i*3,0));v('Quarterly path',c+'24',end);
 const F=(r,z)=>f('Quarterly path',c+r,'='+z);
 F(25,i===0?'DATE(2026,10,16)':`${p}24+1`);F(26,`(${c}24-${c}25+1)/365.25`);
 F(27,i===0?'L_BTC':`${p}27*(1+$B$5)^${c}26`);F(28,`MAX(0.05,L_mNAV+$B$6*LN(${c}27/L_BTC))`);
 F(29,`MIN(1,MAX(0,(${c}28-mNAV_Floor+$B$8)/$B$8))*MIN(1,(${c}27/BTC_Spot)^$B$7)`);
 F(30,i===0?'Reserve_Live':`${p}49`);F(31,i===0?'ATM_Cap':`${p}52`);F(32,i===0?'MSTR_Shares':`${p}54`);F(33,i===0?'MSTR_Price_Live':`${p}39`);
 const rem=j=>`IF(${c}25>'Net NAV'!D${j},'Net NAV'!B${j}*(1-$B$9),'Net NAV'!B${j})`;
 F(34,ds.map((_,j)=>`IF(${c}33<'Net NAV'!C${j+5},${rem(j+5)},0)`).join('+'));
 F(35,ds.map((_,j)=>`IF(${c}33>='Net NAV'!C${j+5},${rem(j+5)}/'Net NAV'!C${j+5},0)`).join('+'));
 F(36,`Pref_Notional_Total-IF(${c}33>='Net NAV'!$B$14,Notional_STRK_In,0)`);
 F(37,`${c}32+'Net NAV'!$B$13+${c}35+IF(${c}33>='Net NAV'!$B$14,Notional_STRK_In/'Net NAV'!$B$14,0)`);
 F(38,`(BTC_Held-BTC_Topup*1000000/L_BTC)*${c}27/1000000+${c}30+IF(Include_USD_Cash="Yes",0,USD_Cash)-${c}34-${c}36`);
 F(39,`MAX(0,${c}28*${c}38/${c}37)`);
 F(40,`IF($B$12=0,L_STRC,MAX($B$16,MIN($B$17,${i===0?'L_STRC':p+'40'}+12*${c}26*IF($B$11<95,$B$13,IF($B$11<99,$B$14,IF($B$11<101,0,$B$15))))))`);
 F(41,`(Pref_Cash_Div_Total-Div_STRC_Cash+STRC_Notional_Now*${c}40)*${c}26`);
 F(42,`(${ds.map((_,j)=>`${rem(j+5)}*'Net NAV'!G${j+5}`).join('+')}+Other_Debt_Interest)*${c}26`);
 F(43,`SUM(${c}41:${c}42)`);
 F(44,`SUMIFS('Net NAV'!$B$5:$B$10,'Net NAV'!$D$5:$D$10,">="&${c}25,'Net NAV'!$D$5:$D$10,"<="&${c}24)*$B$9`);
 F(45,`IF(AND(Gate_On="Yes",${c}28<mNAV_Floor),0,L_ADV*L_Part*${c}29*Trading_Days*${c}26*${c}39)`);
 F(46,`MIN(${c}31,${c}45,MAX(0,(${c}43+${c}44+${c}43/${c}26*Reserve_Min_Months/12-${c}30)/(1-$B$10)))`);
 F(47,`${c}46*$B$10`);F(48,`${c}46-${c}47`);F(49,`MAX(0,${c}30+${c}48-${c}43-${c}44)`);F(50,`MAX(0,${c}43+${c}44-${c}30-${c}48)`);F(51,i===0?`${c}50`:`${p}51+${c}50`);F(52,`MAX(0,${c}31-${c}46)`);F(53,`IF(${c}39=0,0,(${c}46+IF(STRK_In_Stock="Yes",Div_STRK*${c}26,0))/${c}39)`);F(54,`SUM(${c}32,${c}53)`);F(55,`${c}49/(${c}43/${c}26)*12`);F(56,`MAX(0,${c}43/${c}26*Reserve_Min_Months/12-${c}49)`);F(57,`${c}30+${c}48+${c}50-${c}43-${c}44-${c}49`);
 F(58,ds.map((_,j)=>`IF(AND('Net NAV'!D${j+5}>=${c}25,'Net NAV'!D${j+5}<=${c}24,${c}39<'Net NAV'!C${j+5}),'Net NAV'!B${j+5},0)`).join('+'));
 F(59,`SUM('Net NAV'!$B$5:$B$10)-SUMIFS('Net NAV'!$B$5:$B$10,'Net NAV'!$D$5:$D$10,"<="&${c}24)*$B$9`);
}
fmt('Quarterly path','B24:U25','yyyy-mm-dd');fmt('Quarterly path','B26:U59','#,##0.0;(#,##0.0);"-"');fmt('Quarterly path','B28:U29','0.00"x"');fmt('Quarterly path','B40:U40','0.0%');
S('Quarterly path').getRange('B49:U49').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0.01,format:{fill:'#F4CCCC'}});
S('Quarterly path').getRange('B50:U51').conditionalFormats.add('cellIs',{operator:'greaterThan',formula:0.01,format:{fill:'#F4CCCC',font:{color:'#9C0006'}}});
for(const r of [24,43,49,51,57])S('Quarterly path').getRange(`A${r}:U${r}`).format.font.bold=true;
v('Quarterly path','A61','Accrual approximation, actual dates for puts. All puts paid in cash by default, even if in-money. Moneyness is a risk indicator, not a holder election forecast.');
v('Quarterly path','A62','No new preferreds, refinancing, BTC purchases or further BTC sales. Optional initial BTC top-up is removed from asset value.');
v('Quarterly path','A63','Unfunded amounts are financing needs, not payments. After first shortfall, this is a required-funding schedule, not a continuing solvency forecast.');
v('Quarterly path','A64','Rate bands are discretionary and superseded by the current hold policy. This optional rule omits SOFR and legal reduction-cap mechanics.');
v('Quarterly path','A65','20 quarters from Oct 16 2026 to Sep 30 2031. First period is a stub. Coupon cessation is next-quarter; within-quarter interest conservatively accrues a full period.');
head('Quarterly path','A68:B68',['Quarter','Ending cash']);for(let i=0;i<20;i++){f('Quarterly path','A'+(69+i),'=TEXT('+col(i)+'24,"mmm-yy")');f('Quarterly path','B'+(69+i),'='+col(i)+'49');}const chart=S('Quarterly path').charts.add('line',S('Quarterly path').getRange('A68:B88'));chart.title='Ending cash after charges and puts ($m)';chart.setPosition('D68','L85');chart.series.items[0].line={fill:'#333333',width:2};
title('Excel review','Excel and source review','Leave evidence fields blank until the actual check is performed. Linux export does not establish Excel behavior.');
head('Excel review','A4:D4',['Required check','Status','Evidence / result','Next action']);
[['Open in Microsoft Excel for Mac','Pending','','Recalculate All; test dropdown, formatting and charts'],['BTC x net mNAV Data Table','Pending','','Change B5/B6 on Native sensitivity; verify base and 0.8x gate'],['STRC x EUR/USD Data Table','Pending','','Change B7/B8; verify 12% x 1.10 vs manual input'],['Goal Seek native run','Pending','','Set Coverage G10 to 1 by changing Inputs BTC spot; record before / after'],['Q3 source refresh','Pending','','Replace counts and awards after Q3 10-Q is released'],['Human reader test','Pending','','Rahil volunteered; use docs/reader-test.md']].forEach((a,i)=>S('Excel review').getRange(`A${i+5}:D${i+5}`).values=[a]);
v('Excel review','A13','Goal Seek exercise (native execution pending)');v('Excel review','A14','Set cell');v('Excel review','B14',"Coverage!G10");v('Excel review','A15','Target');input('Excel review','B15',1);v('Excel review','A16','Changing cell');v('Excel review','B16',old.names.BTC_Spot);v('Excel review','A17','Analytical expected price');f('Excel review','B17','=BE_BTC_1x');v('Excel review','A18','Recorded Excel result');v('Excel review','A19','Date and Excel version');v('Excel review','A20','Restore original BTC spot after run. G10 is gross BTC value / senior claims, not liquidity coverage. Use Base and restore the original price. Verify address before execution.');
// Update source-facing text and remove stale implementation claims.
v('Dashboard','A9','Static coverage excludes principal repayments. Quarterly path includes puts, fees, demand and dilution. Excel verification and Q3 refresh pending.');
f('Dashboard','A10','="Five-year path: ending cash $"&TEXT(\'Quarterly path\'!U49,"#,##0")&"M; unmet funding $"&TEXT(\'Quarterly path\'!U51,"#,##0")&"M. Full cash puts assumed; no refinancing."');
v('Dashboard','D4','Workbook arithmetic');
f('Checks','B15','=IF(Gate_On="Yes",SUM('+['B','C','D','E','F','G','H'].map(c=>`IF(Stress!${c}5<mNAV_Floor,SUM(Stress!${c}6:${c}15),0)`).join(',')+'),0)');
for(const x of old.sheets.README){if(typeof x.v==='string'&&!x.v.startsWith('=')){
 let z=x.v.replace('uses an enterprise-value definition that may differ from Strategy\'s revised one','uses a reconstructed net definition with dated dilution inputs').replace('convertible conversion prices','early conversion elections and cash settlement choices').replace('The quarterly runway uses accrual timing.','The five-year path uses accrual timing and actual put dates.').replace('Stress grids are plain formulas, not What-If Data Tables, so they recalculate in Excel desktop, Excel for the web and Google Sheets. A note under Grid 5 shows how to rebuild one as a Data Table.','Stress retains portable formula grids. Native sensitivity adds two real What-If Data Tables tied to active model inputs; Microsoft Excel behavior awaits Mac verification.').replace('implied market cap = mNAV x bitcoin NAV - debt - preferred notional + cash','implied market cap = net mNAV x (bitcoin value - out-of-money senior claims + USD Assets)').replace('about three years of all cash charges','about three years of all cash charges before principal repayments');
 if(z!==x.v)v('README',x.cell,z);
}}
v('Stress','A2','Portable snapshot grids using net mNAV and observed moneyness. Principal excluded. Native What-If tables are on Native sensitivity.');
for(const n of ['Net NAV','Excel review']){S(n).getRange('A1:A75').format.columnWidth=56;S(n).getRange('C1:C75').format.columnWidth=32;S(n).getRange('H1:H30').format.columnWidth=65;}
S('Excel review').getRange('D1:D25').format.columnWidth=70;S('Excel review').getRange('A5:D10').format.wrapText=true;S('Excel review').getRange('A5:D10').format.rowHeight=44;
await fs.mkdir(root+'/verification-previews',{recursive:true});
w.recalculate();
console.log((await w.inspect({kind:'table',range:'Net NAV!A12:B23',include:'values,formulas',tableMaxRows:12,tableMaxCols:2,maxChars:3000})).ndjson);
console.log((await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!',options:{useRegex:true,maxResults:20},summary:'formula errors',maxChars:3000})).ndjson);
await (await SpreadsheetFile.exportXlsx(w)).save(root+'/Strategy_Preferred_Coverage_Model.xlsx');
for(const [s,r] of [['Dashboard','A1:F19'],['Net NAV','A4:G23'],['Quarterly path','A24:F59'],['Native sensitivity','D5:K14'],['Excel review','A4:D10']]){
try{const b=await w.render({sheetName:s,range:r,scale:1.4});await fs.writeFile(root+'/verification-previews/'+s.replaceAll(' ','-')+'.png',new Uint8Array(await b.arrayBuffer()));}catch(e){console.log('render',s,String(e).slice(0,200));}
}
await fs.writeFile(root+'/verification-previews/results.json',JSON.stringify({net:S('Net NAV').getRange('A12:B23').values,path:S('Quarterly path').getRange('B24:U59').values,sensitivity:S('Native sensitivity').getRange('D5:K14').values},null,2));
console.log('saved upgraded workbook');
