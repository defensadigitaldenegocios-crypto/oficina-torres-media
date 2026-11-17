import os
S=os.path.dirname(os.path.abspath(__file__))
M='file:///home/claude/defensadigitaldenegocios-crypto/sazonika-web/media/'
F='file://'+S+'/node_modules/@fontsource/'
CSS=f"""
@font-face{{font-family:Oswald;font-weight:500;src:url({F}oswald/files/oswald-latin-500-normal.woff2)}}
@font-face{{font-family:Oswald;font-weight:700;src:url({F}oswald/files/oswald-latin-700-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:400;src:url({F}barlow/files/barlow-latin-400-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:600;src:url({F}barlow/files/barlow-latin-600-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:800;src:url({F}barlow/files/barlow-latin-800-normal.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:Barlow,sans-serif;color:#F4EFE6}}
.s{{position:relative;width:1080px;height:1350px;padding:84px;display:flex;flex-direction:column;overflow:hidden}}
.dark{{background:radial-gradient(ellipse at 80% 85%,rgba(200,22,29,.45) 0%,rgba(200,22,29,0) 55%),radial-gradient(ellipse at 15% 0%,rgba(242,179,61,.16) 0%,rgba(242,179,61,0) 45%),#121110}}
.cream{{background:#F4EFE6;color:#121110}}
.red{{background:radial-gradient(ellipse at 50% 110%,#7d0c11 0%,#C8161D 60%);}}
.amber{{background:#F2B33D;color:#121110}}
.top{{display:flex;justify-content:space-between;align-items:center;height:96px;position:relative;z-index:3}}
.top img{{height:84px}}
.n{{font:600 30px Barlow;letter-spacing:.08em;opacity:.75}}
.h{{font-family:Oswald;font-weight:700;text-transform:uppercase;line-height:.95;letter-spacing:-.005em}}
.k{{display:inline-block;font:800 26px Barlow;letter-spacing:.14em;text-transform:uppercase;padding:12px 22px;border-radius:999px}}
.swipe{{position:absolute;left:84px;bottom:70px;font:600 30px Barlow;letter-spacing:.06em;opacity:.8;z-index:3}}
.p{{font:400 42px/1.32 Barlow}}
.b{{font-weight:800}}
.am{{color:#F2B33D}}.rd{{color:#C8161D}}
"""
def page(body,cls='dark',num='',logo='logo-color.webp',swipe=True):
    lg=f'<img src="{M}{logo}">' if logo else '<span></span>'
    sw='<div class="swipe">Desliza &rarr;</div>' if swipe else ''
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {cls}"><div class="top">{lg}<span class="n">{num}</span></div>{body}{sw}</div></body></html>'
slides={}
# ---------- A: No es un sazonador
slides['A1']=page(f'''
<img src="{M}label-front.webp" style="position:absolute;right:-190px;bottom:-200px;width:640px;transform:rotate(-9deg);filter:drop-shadow(0 40px 60px rgba(0,0,0,.6))">
<div style="margin-top:90px;position:relative;z-index:2">
<span class="k" style="background:#C8161D;color:#F4EFE6">Hecho en Nuevo León</span>
<div class="h" style="font-size:156px;margin-top:40px">No es un<br>sazonador.</div>
<div class="p am b" style="margin-top:36px;font-size:46px">Es otra cosa.<br>Te explicamos.</div></div>''',num='1/4')
slides['A2']=page(f'''
<div style="margin-top:110px">
<div class="h" style="font-size:118px">Es un<br><span class="rd">intensificador</span><br>de sabores.</div>
<div style="width:120px;height:10px;background:#F2B33D;margin:56px 0"></div>
<div class="p" style="max-width:860px;font-size:48px">No tapa el sabor de la carne: <span class="b">lo realza.</span><br><br>Su fórmula <span class="b">Umami Blend</span> saca lo mejor de cada corte, para que la carne sepa más a carne.</div></div>''','cream',num='2/4',logo='logo-color.webp')
icons=[('res','Res'),('hamburguesas','Hamburguesas'),('parrilla','Parrilla'),('steaks','Steaks'),('pollo','Pollo'),('harinas','Harinas')]
grid=''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:18px"><img src="{M}ic-{i}.webp" style="width:190px;height:190px;border-radius:50%"><span style="font:600 34px Barlow">{t}</span></div>' for i,t in icons)
slides['A3']=page(f'''
<div style="margin-top:70px">
<div class="h" style="font-size:96px">1 sobre de 30 g<br><span class="am">rinde aprox. 1 kg</span></div>
<div class="p" style="margin-top:22px;opacity:.85">Para todo lo que va al fuego o al sartén:</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:46px 30px;margin-top:64px">{grid}</div></div>''',num='3/4')
slides['A4']=page(f'''
<div style="margin-top:80px;position:relative;z-index:2">
<div class="h" style="font-size:150px">Pruébalo<br>este fin.</div>
<div class="p b" style="margin-top:40px;font-size:52px">$29 el sobre</div>
<div class="p" style="margin-top:10px">Paquetes de 3, 6 y ristra de 10.<br>Envío a todo México. <span class="b">Gratis en la ristra.</span></div>
<div style="display:inline-block;margin-top:56px;background:#121110;color:#F4EFE6;font:800 52px Barlow;padding:26px 46px;border-radius:18px">sazonika.mx</div></div>
<img src="{M}mockup.webp" style="position:absolute;right:-210px;bottom:-60px;width:820px;opacity:.95">''','red',num='4/4',swipe=False)
# ---------- B: Reseñas
slides['B1']=page(f'''
<div style="margin-top:60px;position:relative;z-index:2">
<div class="h" style="font-size:132px">Lo dicen<br>ellos,<br><span class="am">no nosotros.</span></div>
<div class="p" style="margin-top:30px;max-width:560px">3 clientes reales de Monterrey, Escobedo y San Nicolás.</div></div>
<img src="{M}nl.webp" style="position:absolute;right:70px;bottom:110px;width:370px;border-radius:28px;transform:rotate(4deg);box-shadow:0 30px 70px rgba(0,0,0,.55)">''',num='1/5')
for i,(sl,lugar) in enumerate([('B2','Monterrey'),('B3','Escobedo'),('B4','San Nicolás')],1):
    slides[sl]=page(f'''
<div style="margin-top:40px"><span class="k" style="background:#F2B33D;color:#121110">Cliente real · {lugar}</span></div>
<div style="flex:1;display:flex;align-items:center;justify-content:center;padding-bottom:70px">
<img src="{M}review-{i}.webp" style="width:100%;border-radius:30px;box-shadow:0 30px 80px rgba(0,0,0,.55)"></div>''',num=f'{i+1}/5')
slides['B5']=page(f'''
<div style="margin-top:120px">
<div class="h" style="font-size:132px">¿Ya lo<br>probaste?</div>
<div class="p" style="margin-top:40px;max-width:860px">Cuéntanos en los comentarios en qué lo usaste: <span class="b">asada, hamburguesas, pollo…</span></div>
<div style="display:inline-block;margin-top:64px;background:#C8161D;color:#F4EFE6;font:800 52px Barlow;padding:26px 46px;border-radius:18px">sazonika.mx</div></div>''','cream',num='5/5',swipe=False)
# ---------- C: Checklist asada
slides['C1']=f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s" style="background:url({M}grill.webp) center/cover">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(18,17,16,.35) 0%,rgba(18,17,16,0) 30%,rgba(18,17,16,.65) 58%,#121110 88%)"></div>
<div class="top"><span></span><span class="n">1/4</span></div>
<div style="margin-top:auto;position:relative;z-index:2;padding-bottom:110px">
<span class="k" style="background:#F2B33D;color:#121110">Guárdalo</span>
<div class="h" style="font-size:124px;margin-top:30px">Checklist de la<br>carne asada<br><span class="am">del sábado</span></div></div>
<div class="swipe">Desliza &rarr;</div></div></body></html>'''
items=['Carbón y encendedor','La carne: arrachera, diezmillo o costilla','Tortillas de harina','Salsa, cebollitas y limones','Sazonika: 1 sobre por kilo']
lst=''.join(f'<div style="display:flex;gap:30px;align-items:center;padding:30px 0;border-bottom:3px dashed rgba(18,17,16,.18)"><span style="flex:none;width:62px;height:62px;border:6px solid #121110;border-radius:12px;display:grid;place-items:center;font:800 44px Barlow;color:#C8161D">{"✓" if k<4 else ""}</span><span style="font:600 46px Barlow;{"color:#C8161D" if k==4 else ""}">{t}</span></div>' for k,t in enumerate(items))
slides['C2']=page(f'''<div style="margin-top:50px"><div class="h" style="font-size:96px">Lo que no<br>puede faltar</div><div style="margin-top:40px">{lst}</div></div>''','cream',num='2/4')
steps=[('Saca la carne del refri un rato antes de asarla.'),('Espolvorea Sazonika por ambos lados. Un sobre alcanza para 1 kg.'),('A la parrilla. Voltéala una vez y déjala reposar antes de cortar.')]
st=''.join(f'<div style="display:flex;gap:36px;align-items:flex-start;margin-top:52px"><span class="h am" style="font-size:150px;line-height:.8;width:110px;flex:none">{i}</span><span class="p" style="font-size:44px">{t}</span></div>' for i,t in enumerate(steps,1))
slides['C3']=page(f'''<div style="margin-top:50px"><div class="h" style="font-size:100px">Sazona en<br><span class="am">3 pasos</span></div>{st}</div>''',num='3/4')
slides['C4']=page(f'''
<div style="margin-top:100px;position:relative;z-index:2">
<div class="h" style="font-size:124px">¿A quién le<br>toca la asada<br>este sábado?</div>
<div class="p" style="margin-top:36px">Etiquétalo para que no se le olvide <span class="b">el Sazonika.</span></div>
<div style="display:inline-block;margin-top:56px;background:#121110;color:#F4EFE6;font:800 52px Barlow;padding:26px 46px;border-radius:18px">sazonika.mx</div>
<div class="p b" style="margin-top:26px;font-size:38px">$29 el sobre · hecho en Nuevo León</div></div>''','red',num='4/4',swipe=False)
# ---------- D: Comercios
slides['D1']=page(f'''
<div style="margin-top:70px;position:relative;z-index:2">
<span class="k" style="background:#F2B33D;color:#121110">Para negocios</span>
<div class="h" style="font-size:118px;margin-top:36px">¿Tienes<br>carnicería,<br>tiendita o<br>minisúper?</div>
<div class="p am b" style="margin-top:34px;font-size:48px">Gana con cada sobre<br>sin invertir un peso.</div></div>
<img src="{M}pouch-back.webp" style="position:absolute;right:-170px;bottom:-170px;width:430px;transform:rotate(8deg);filter:drop-shadow(0 30px 60px rgba(0,0,0,.6))">''',num='1/4')
pasos=['Te dejamos ristras de 10 sobres <b>a consignación</b>.','Se venden a <b>$29</b> al público.','Te quedas con el <b>20%</b>: $5.80 por sobre.','Liquidamos <b>cada semana</b>: solo pagas lo vendido.']
ps=''.join(f'<div style="display:flex;gap:30px;align-items:center;margin-top:44px"><span style="flex:none;width:92px;height:92px;border-radius:50%;background:#C8161D;color:#F4EFE6;display:grid;place-items:center;font:700 52px Oswald">{i}</span><span class="p" style="font-size:44px">{t}</span></div>' for i,t in enumerate(pasos,1))
slides['D2']=page(f'''<div style="margin-top:50px"><div class="h" style="font-size:104px">Así funciona</div>{ps}</div>''','cream',num='2/4')
slides['D3']=page(f'''
<div style="margin-top:90px">
<div class="p" style="font-size:44px;opacity:.85">Ejemplo: si vendes</div>
<div class="h" style="font-size:150px;margin-top:10px">2 ristras<br>por semana</div>
<div class="p" style="font-size:44px;margin-top:40px;opacity:.85">tu negocio gana</div>
<div class="h am" style="font-size:230px;margin-top:6px">$464</div>
<div class="h" style="font-size:72px">al mes</div>
<div style="font:400 28px Barlow;opacity:.6;margin-top:40px">Ejemplo ilustrativo: 20 sobres × $5.80 × 4 semanas. No es una venta garantizada.</div></div>''',num='3/4')
slides['D4']=page(f'''
<div style="margin-top:110px">
<div class="h" style="font-size:132px">¿Lo<br>probamos en<br>tu negocio?</div>
<div class="p" style="margin-top:40px">Escríbele a <b>Valeria</b> por WhatsApp:</div>
<div class="h" style="font-size:104px;margin-top:16px">81 8113 9153</div>
<div class="p b" style="margin-top:40px">@sazonika.mty · sazonika.mx</div></div>''','amber',num='4/4',logo='logo-color.webp',swipe=False)
for k,v in slides.items():
    open(os.path.join(S,'html',k+'.html'),'w').write(v)
print(len(slides))
