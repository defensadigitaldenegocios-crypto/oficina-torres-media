const { chromium } = require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{const dir=process.argv[2]||__dirname;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync(path.join(dir,'html')).sort()){await p.goto('file://'+path.join(dir,'html',f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:path.join(dir,'out',f.replace('.html','.jpg')),type:'jpeg',quality:90});}
await b.close();})();
