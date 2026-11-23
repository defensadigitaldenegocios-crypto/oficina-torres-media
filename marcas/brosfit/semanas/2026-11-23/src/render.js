const {chromium}=require('playwright');const fs=require('fs');
(async()=>{let b;try{b=await chromium.launch()}catch(e){b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'})}
const p=await b.newPage({viewport:{width:1080,height:1350}});fs.mkdirSync('out',{recursive:true});
for(const f of fs.readdirSync('html').filter(x=>x.endsWith('.html')).sort()){
await p.goto('file://'+__dirname+'/html/'+f);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
const ov=await p.evaluate(()=>{const r=[];document.querySelectorAll('.wrap *').forEach(e=>{const b=e.getBoundingClientRect();if(b.right>1000||b.bottom>1200||b.left<80)r.push(e.tagName+':'+(e.textContent||'').slice(0,20)+':'+Math.round(b.right)+','+Math.round(b.bottom))});return r.slice(0,4)});
if(ov.length)console.log(f,ov);
await p.screenshot({path:'out/'+f.replace('.html','.jpg'),type:'jpeg',quality:90});}
await b.close()})();
