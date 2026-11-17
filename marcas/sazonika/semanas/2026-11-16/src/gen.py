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
.p{{font:400 44px/1.3 Barlow}}
.b{{font-weight:800}}
.am{{color:#F2B33D}}.rd{{color:#C8161D}}
.btn{{display:inline-block;font:800 52px Barlow;padding:24px 44px;border-radius:18px}}
"""
def page(body,cls='dark',num='',logo='logo-color.png',swipe=True,style=''):
    lg=f'<img src="{M}{logo}">' if logo else '<span></span>'
    sw='<div class="swipe">Desliza &rarr;</div>' if swipe else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {cls}" style="{style}"><div class="top">{lg}<span class="n">{num}</span></div>{body}{sw}</div></body></html>'
slides={}

# ================= A · 3 errores (miércoles)
slides['A1']=page(f'''
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:url({M}grill.png) center 62%/cover"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(180deg,#121110 0%,rgba(18,17,16,.15) 45%,rgba(18,17,16,.55) 100%)"></div>
<div style="position:relative;z-index:2;margin-top:40px;display:flex;align-items:flex-start;gap:34px">
<div class="h rd" style="font-size:440px;line-height:.78">3</div>
<div class="h" style="font-size:96px;margin-top:6px">errores<br>que le<br>quitan sabor</div></div>
<div class="h am" style="position:relative;z-index:2;font-size:96px;margin-top:22px">a tu carne asada</div>
<div style="position:absolute;right:84px;bottom:66px;z-index:3"><span class="k" style="background:#F4EFE6;color:#121110;font-size:30px">¿Cuál cometes tú?</span></div>''',num='1/5')

def err(n,titulo,fix,cls,colnum):
    return page(f'''
<div class="mid"><div>
<span class="k" style="background:{'#121110' if cls!='dark' else '#C8161D'};color:#F4EFE6">Error {n}</span></div>
<div class="h" style="font-size:150px;margin-top:40px">{titulo}</div>
<div style="width:160px;height:14px;background:{colnum};margin:60px 0 54px"></div>
<div class="p" style="font-size:56px;max-width:780px">{fix}</div></div>
<div class="h" style="position:absolute;right:-10px;bottom:-150px;font-size:440px;line-height:1;color:{colnum};opacity:.12;z-index:1">{n}</div>''',cls,num=f'{n+1}/5')
slides['A2']=err(1,'Sazonar<br>a puro ojo','<b>Mídele.</b> Un sobre de 30 g de Sazonika rinde aprox. <b>1 kg</b> de carne.','cream','#C8161D')
slides['A3']=err(2,'Sazonar de<br>un solo lado','<b>Espolvorea por ambos lados</b>, antes de que la carne toque el fuego.','dark','#F2B33D')
slides['A4']=err(3,'Cortarla en<br>cuanto sale','<b>Déjala reposar</b> unos minutos antes de cortar. Tu paciencia también sazona.','amber','#C8161D')
slides['A5']=page(f'''
<div style="margin-top:56px;position:relative;z-index:2">
<div class="h" style="font-size:112px;line-height:1.14">¿Y el error<br>más común?</div>
<div class="p" style="margin-top:34px;max-width:640px;font-size:46px">Usar algo que <b>tapa</b> el sabor de la carne. Sazonika es un <b>intensificador de sabores</b>: lo realza.</div>
<div class="p b" style="margin-top:44px;font-size:46px">Comenta: 1, 2 o 3.<br>¿Cuál era el tuyo?</div>
<div class="btn" style="margin-top:44px;background:#121110;color:#F4EFE6">sazonika.mx</div></div>
<img src="{M}mockup.png" style="position:absolute;right:-300px;bottom:-60px;width:700px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5))">''','red',num='5/5',swipe=False)

# ================= B · Si solo pudieras usarlo en una cosa (viernes)
slides['B1']=page(f'''
<div style="position:relative;z-index:2;margin-top:34px">
<div class="h" style="font-size:112px">Si solo<br>pudieras<br>usarlo en<br><span class="rd">una cosa…</span></div>
<div class="p b" style="margin-top:30px;font-size:50px">¿Qué eliges?</div></div>
<img src="{M}nl.png" style="position:absolute;right:70px;bottom:120px;width:430px;border-radius:30px;transform:rotate(5deg);box-shadow:0 30px 70px rgba(0,0,0,.35);border:14px solid #fff">''','cream',num='1/4')
icons=[('res','Res'),('hamburguesas','Hamburguesas'),('parrilla','Parrilla'),('steaks','Steaks'),('pollo','Pollo'),('harinas','Harinas')]
grid=''.join(f'''<div style="position:relative;display:flex;flex-direction:column;align-items:center;gap:16px;background:rgba(244,239,230,.06);border:2px solid rgba(244,239,230,.14);border-radius:28px;padding:44px 10px 36px">
<span class="h" style="position:absolute;left:22px;top:14px;font-size:64px;color:#F2B33D">{k}</span>
<img src="{M}ic-{i}.png" style="width:200px;height:200px;border-radius:50%"><span style="font:600 38px Barlow">{t}</span></div>''' for k,(i,t) in enumerate(icons,1))
slides['B2']=page(f'''
<div class="mid">
<div class="h" style="font-size:110px">Elige <span class="am">un número</span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:56px">{grid}</div></div>''',num='2/4')
slides['B3']=page(f'''
<div style="margin-top:70px;position:relative;z-index:2">
<span class="k" style="background:#121110;color:#F2B33D">Plot twist</span>
<div class="h" style="font-size:140px;margin-top:36px">No tienes<br>que elegir.</div>
<div class="p" style="margin-top:44px;max-width:640px">Sazonika no es solo un sazonador: es un <b>intensificador de sabores</b>. Realza el sabor natural de las 6.</div></div>
<img src="{M}label-front.png" style="position:absolute;right:-250px;bottom:-330px;width:640px;transform:rotate(-10deg);filter:drop-shadow(0 30px 60px rgba(0,0,0,.6))">''','red',num='3/4')
slides['B4']=page(f'''
<div class="mid">
<div class="h" style="font-size:130px">Por eso<br>mejor <span class="rd">pide<br>la ristra.</span></div>
<div class="p" style="margin-top:44px;font-size:50px">10 sobres. <b>Envío gratis</b> a todo México.<br>También hay paquetes de 3 y de 6.</div>
<div class="p b" style="margin-top:34px;font-size:48px">$29 el sobre · 30 g rinde aprox. 1 kg</div>
<div><div class="btn" style="margin-top:50px;background:#C8161D;color:#F4EFE6">sazonika.mx</div></div>
<div class="p" style="margin-top:50px;font-size:48px">Pero dinos: <b>¿cuál número elegiste?</b></div></div>''','amber',num='4/4',swipe=False)

# ================= C · Tipos de parrillero (sábado)
slides['C1']=page(f'''
<div style="position:relative;z-index:2;margin-top:40px">
<div class="h" style="font-size:110px">En toda<br>carne asada<br>hay uno<br>de estos.</div>
<div class="k" style="margin-top:36px;background:#121110;color:#F4EFE6;font-size:30px">Etiquétalo</div></div>
<div style="position:absolute;right:50px;bottom:70px;width:430px;background:#fff;padding:18px 18px 70px;transform:rotate(-6deg);box-shadow:0 30px 60px rgba(0,0,0,.35)">
<div style="width:100%;height:450px;background:url({M}grill.png) 60% 70%/cover"></div>
<div style="position:absolute;left:0;right:0;bottom:16px;text-align:center;font:800 30px Barlow;color:#121110">sábado, 2 p.m.</div></div>''','amber',num='1/5')
def tipo(n,nombre,desc,cls,acc,fs=150):
    return page(f'''
<div class="mid">
<div class="h" style="font-size:52px;color:{acc}">Tipo {n}</div>
<div class="h" style="font-size:{fs}px;margin-top:22px;line-height:1.16">{nombre}</div>
<div style="width:160px;height:14px;background:{acc};margin:60px 0 54px"></div>
<div class="p" style="font-size:58px;max-width:880px">{desc}</div></div>''',cls,num=f'{n+1}/5')
slides['C2']=tipo(1,'El que no<br>suelta las<br>pinzas','Nadie más toca la parrilla. <b>Nadie.</b>','dark','#F2B33D')
slides['C3']=tipo(2,'El que llega<br>cuando ya<br>está la carne','Nunca ayudó, pero siempre come primero.','cream','#C8161D',fs=128)
slides['C4']=page(f'''
<div style="margin-top:60px;position:relative;z-index:2">
<div class="h am" style="font-size:44px">Tipo 3</div>
<div class="h" style="font-size:120px;margin-top:22px;line-height:1.1">El del<br>sazón<br>secreto</div>
<div class="p" style="margin-top:40px;max-width:520px">Todos le preguntan qué le pone. <b>Spoiler: Sazonika.</b></div></div>
<img src="{M}nl.png" style="position:absolute;right:64px;bottom:120px;width:400px;border-radius:26px;transform:rotate(5deg);box-shadow:0 30px 70px rgba(0,0,0,.55)">''',num='4/5')
slides['C5']=page(f'''
<div class="mid">
<div style="background:#fff;color:#121110;border-radius:30px;padding:56px 56px;box-shadow:0 30px 70px rgba(0,0,0,.4)">
<div class="h rd" style="font-size:120px;line-height:.6;height:60px">“</div>
<div style="font:600 60px/1.22 Barlow;margin-top:10px">Se nota la diferencia, muy recomendable.</div>
<div style="font:400 34px Barlow;margin-top:22px;opacity:.7">Luis R. · Escobedo, N.L. · cliente real</div></div>
<div class="h" style="font-size:130px;margin-top:80px">¿Cuál eres tú?</div>
<div class="p" style="margin-top:24px;font-size:50px">Etiqueta al parrillero de tu grupo.</div>
<div><div class="btn" style="margin-top:50px;background:#C8161D;color:#F4EFE6">sazonika.mx</div></div></div>''',num='5/5',swipe=False)

for k,v in slides.items():
    open(os.path.join(S,'html',k+'.html'),'w').write(v)
print(len(slides))
