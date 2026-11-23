import os
S=os.path.dirname(os.path.abspath(__file__))
M='file:///home/claude/oficina-torres-media/marcas/sazonika/assets/'
F='file://'+S+'/node_modules/@fontsource/'
CSS=f"""
@font-face{{font-family:Oswald;font-weight:700;src:url({F}oswald/files/oswald-latin-700-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:400;src:url({F}barlow/files/barlow-latin-400-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:600;src:url({F}barlow/files/barlow-latin-600-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:800;src:url({F}barlow/files/barlow-latin-800-normal.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:Barlow,sans-serif;color:#F4EFE6}}
.s{{position:relative;width:1080px;height:1350px;padding:84px;display:flex;flex-direction:column;overflow:hidden}}
.dark{{background:radial-gradient(ellipse at 80% 85%,rgba(200,22,29,.45) 0%,rgba(200,22,29,0) 55%),radial-gradient(ellipse at 15% 0%,rgba(242,179,61,.16) 0%,rgba(242,179,61,0) 45%),#121110}}
.cream{{background:#F4EFE6;color:#121110}}
.red{{background:radial-gradient(ellipse at 50% 110%,#7d0c11 0%,#C8161D 60%)}}
.amber{{background:#F2B33D;color:#121110}}
.top{{display:flex;justify-content:space-between;align-items:center;height:96px;position:relative;z-index:3}}
.top img{{height:84px}}
.n{{font:600 30px Barlow;letter-spacing:.08em;opacity:.75}}
.h{{font-family:Oswald;font-weight:700;text-transform:uppercase;line-height:1.02}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:90px;position:relative;z-index:2}}
.k{{display:inline-block;font:800 26px Barlow;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px;border-radius:999px}}
.swipe{{position:absolute;left:84px;bottom:70px;font:600 30px Barlow;letter-spacing:.06em;opacity:.8;z-index:3}}
.p{{font:400 46px/1.3 Barlow}}
.b{{font-weight:800}}
.am{{color:#F2B33D}}.rd{{color:#C8161D}}
.btn{{display:inline-block;font:800 52px Barlow;padding:24px 44px;border-radius:18px}}
"""
def page(body,cls='dark',num='',logo='logo-color.png',swipe=True,style=''):
    lg=f'<img src="{M}{logo}">' if logo else '<span></span>'
    sw='<div class="swipe">Desliza &rarr;</div>' if swipe else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {cls}" style="{style}"><div class="top">{lg}<span class="n">{num}</span></div>{body}{sw}</div></body></html>'
slides={}

# ================= A · El quinto sabor (miércoles)
slides['A1']=page(f'''
<div style="position:absolute;inset:0;background:url({M}grill.png) center 70%/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.96) 0%,rgba(18,17,16,.86) 38%,rgba(18,17,16,.15) 70%,rgba(18,17,16,.6) 100%)"></div>
<div style="position:relative;z-index:2;margin-top:40px">
<div class="h" style="font-size:112px;line-height:1.04">Tu carne tiene<br>un sabor que<br><span class="am">casi nadie<br>aprovecha.</span></div>
<div class="k" style="margin-top:38px;background:#C8161D;color:#F4EFE6;font-size:30px">¿Sabes cuál?</div></div>''',num='1/5')

slides['A2']=page(f'''
<div class="mid">
<div class="p b" style="font-size:44px;opacity:.75">Todos conocemos cuatro:</div>
<div class="h" style="font-size:150px;line-height:1.08;margin-top:26px;color:#121110">Dulce<br>Salado<br>Ácido<br>Amargo</div>
<div class="h rd" style="font-size:92px;margin-top:40px">…pero hay un quinto.</div></div>''','cream',num='2/5')

slides['A3']=page(f'''
<div class="mid">
<span class="k" style="background:#121110;color:#F2B33D;align-self:flex-start">El quinto sabor</span>
<div class="h" style="font-size:250px;line-height:1;margin-top:30px">Umami</div>
<div style="width:160px;height:14px;background:#F2B33D;margin:46px 0 46px"></div>
<div class="p" style="font-size:54px;max-width:860px">Ese sabor <b>profundo, «a carne»</b>, que hace que alguien pregunte: <b>¿qué le pusiste?</b></div></div>''','red',num='3/5')

slides['A4']=page(f'''
<div style="position:relative;z-index:2;margin-top:44px">
<div class="h" style="font-size:96px;line-height:1.06">Por eso se llama<br><span class="am">Umami Blend.</span></div>
<div class="p" style="margin-top:34px;max-width:900px;font-size:48px">Sazonika Original no tapa la carne: es un <b>intensificador de sabores</b> que realza su sabor natural.</div></div>
<img src="{M}mockup.png" style="position:absolute;left:50%;transform:translateX(-50%);bottom:-30px;width:700px;filter:drop-shadow(0 30px 60px rgba(0,0,0,.6))">''',num='4/5',swipe=False)

slides['A5']=page(f'''
<div class="mid">
<div class="h" style="font-size:118px;line-height:1.06">Mándaselo<br>al que dice<br><span class="rd">«con sal basta».</span></div>
<div class="p b" style="margin-top:46px;font-size:48px">Sobre de 30 g · rinde aprox. 1 kg de carne<br>Hecho en Nuevo León</div>
<div><div class="btn" style="margin-top:50px;background:#121110;color:#F4EFE6">sazonika.mx</div></div></div>''','amber',num='5/5',swipe=False)

# ================= B · La cuenta de la asada (viernes)
slides['B1']=page(f'''
<div style="position:relative;z-index:2;margin-top:40px">
<div class="h" style="font-size:120px;line-height:1.04">La cuenta<br>que nadie<br>hace antes<br>de la asada</div></div>
<div style="position:absolute;left:84px;bottom:150px;z-index:3"><div class="h" style="font-size:300px;line-height:.8;color:#C8161D">?</div></div>
<img src="{M}mockup.png" style="position:absolute;right:-200px;bottom:-10px;width:680px;transform:rotate(-6deg);filter:drop-shadow(0 30px 50px rgba(0,0,0,.45))">''','amber',num='1/5')

slides['B2']=page(f'''
<div class="mid" style="align-items:center;text-align:center">
<div class="p b am" style="font-size:44px;letter-spacing:.06em;text-transform:uppercase">La regla</div>
<div style="display:flex;align-items:center;gap:40px;margin-top:40px">
<div><div class="h" style="font-size:260px;line-height:.9">1</div><div class="p b" style="font-size:46px">sobre de 30 g</div></div>
<div class="h rd" style="font-size:180px">=</div>
<div><div class="h am" style="font-size:260px;line-height:.9">1 kg</div><div class="p b" style="font-size:46px">de carne (aprox.)</div></div></div>
<div class="p" style="margin-top:70px;font-size:48px;max-width:820px">Así de fácil. Ahora haz la cuenta de tu asada.</div></div>''',num='2/5')

def row(kg,txt,sub,hl=False):
    bg='#C8161D' if hl else '#fff'
    col='#F4EFE6' if hl else '#121110'
    return f'''<div style="display:flex;align-items:center;gap:36px;background:{bg};color:{col};border-radius:26px;padding:26px 40px;box-shadow:0 12px 30px rgba(0,0,0,.08)">
<div class="h" style="font-size:96px;width:250px;flex:none">{kg}</div>
<div><div style="font:800 50px Barlow">{txt}</div><div style="font:400 36px Barlow;opacity:.8;margin-top:4px">{sub}</div></div></div>'''
slides['B3']=page(f'''
<div class="mid" style="padding-bottom:110px">
<div class="h" style="font-size:96px">¿Cuántos <span class="rd">kilos?</span></div>
<div style="display:flex;flex-direction:column;gap:22px;margin-top:44px">
{row('1 kg','1 sobre','La de entre semana')}
{row('3 kg','Paquete de 3','La de la familia')}
{row('6 kg','Paquete de 6','La del fin de semana largo')}
{row('10 kg','Ristra de 10','La de la posada · envío gratis',True)}
</div></div>''','cream',num='3/5')

icons=[('res','Res'),('hamburguesas','Hamburguesas'),('parrilla','Parrilla'),('steaks','Steaks'),('pollo','Pollo'),('harinas','Harinas')]
grid=''.join(f'''<div style="display:flex;flex-direction:column;align-items:center;gap:14px">
<img src="{M}ic-{i}.png" style="width:220px;height:220px;border-radius:50%;box-shadow:0 14px 30px rgba(0,0,0,.35)"><span style="font:800 40px Barlow">{t}</span></div>''' for i,t in icons)
slides['B4']=page(f'''
<div class="mid">
<div class="h" style="font-size:104px">Y no solo<br>para la res.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px 20px;margin-top:56px">{grid}</div>
<div class="p" style="margin-top:50px;font-size:46px">El mismo sobre, la misma regla: <b>30 g por kilo.</b></div></div>''','red',num='4/5')

slides['B5']=page(f'''
<div class="mid">
<div class="h" style="font-size:112px;line-height:1.06">¿Cuántos kilos<br>vas a asar<br><span class="am">este fin?</span></div>
<div class="p b" style="margin-top:40px;font-size:52px">Comenta el número.</div>
<div class="p" style="margin-top:44px;font-size:44px">Paquetes de 3, 6 y ristra de 10.<br>Envío a todo México, <b>gratis en la ristra.</b></div>
<div><div class="btn" style="margin-top:50px;background:#C8161D;color:#F4EFE6">sazonika.mx</div></div></div>
<img src="{M}s.png" style="position:absolute;right:-60px;bottom:-40px;width:360px;opacity:.10;filter:invert(1)">''',num='5/5',swipe=False)

# ================= C · ¿Qué le pusiste? (sábado)
slides['C1']=page(f'''
<div style="position:relative;z-index:2;margin-top:70px">
<div style="position:relative;background:#F4EFE6;color:#121110;border-radius:44px;padding:56px 60px;max-width:860px">
<div class="h" style="font-size:118px;line-height:1.04">¿Qué le<br>pusiste a<br>la carne?</div>
<div style="position:absolute;left:90px;bottom:-56px;width:0;height:0;border-left:30px solid transparent;border-right:50px solid transparent;border-top:60px solid #F4EFE6"></div></div>
<div class="p" style="margin-top:100px;font-size:50px;max-width:820px">La pregunta que <b class="am">vas a escuchar hoy</b> en la asada.</div></div>''','red',num='1/5')

def review(img,quote,who,cls,acc,num):
    return page(f'''
<div style="position:relative;z-index:2;margin-top:34px">
<div class="h" style="font-size:120px;line-height:.6;height:70px;color:{acc}">“</div>
<div style="font:800 54px/1.18 Barlow;max-width:900px">{quote}</div>
<div style="font:600 36px Barlow;margin-top:22px;opacity:.75">{who} · reseña real</div></div>
<img src="{M}{img}" style="position:absolute;left:50%;transform:translateX(-50%) rotate(-2deg);bottom:105px;width:620px;border-radius:24px;box-shadow:0 30px 60px rgba(0,0,0,.35)">''',cls,num=num)
slides['C2']=review('review-1.png','Realmente marca la diferencia… aporta un sabor intenso, equilibrado y muy profesional.','Chef Roberto G. · Monterrey, N.L.','dark','#F2B33D','2/5')
slides['C3']=review('review-3.png','Lo usé en una carne asada familiar y también en pollo… Lo volvería a comprar.','Andrea G. · San Nicolás, N.L.','cream','#C8161D','3/5')

slides['C4']=page(f'''
<div style="position:absolute;inset:0;background:url({M}grill.png) 85% 0%/150% auto no-repeat"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.15) 0%,rgba(18,17,16,.35) 45%,rgba(18,17,16,.95) 78%)"></div>
<div style="position:absolute;left:84px;right:84px;bottom:150px;z-index:2">
<div class="h" style="font-size:112px;line-height:1.04">Hoy te toca<br><span class="am">a ti</span> la pregunta.</div>
<div class="p" style="margin-top:28px;font-size:48px;max-width:860px">Un <b>intensificador de sabores</b>: realza lo que ya trae la carne.</div></div>''',num='4/5')

slides['C5']=page(f'''
<div class="mid">
<div class="h" style="font-size:124px;line-height:1.04">¿Ya lo<br>probaste?</div>
<div class="p" style="margin-top:40px;font-size:52px;max-width:880px">Comenta <b>con qué carne lo usaste:</b> res, pollo, hamburguesa…</div>
<div class="p b" style="margin-top:40px;font-size:46px">¿Aún no? Sobre de 30 g, rinde aprox. 1 kg.</div>
<div><div class="btn" style="margin-top:48px;background:#121110;color:#F4EFE6">sazonika.mx</div></div></div>''','amber',num='5/5',swipe=False)

os.makedirs(os.path.join(S,'html'),exist_ok=True)
for k,v in slides.items():
    open(os.path.join(S,'html',k+'.html'),'w').write(v)
print(len(slides))
