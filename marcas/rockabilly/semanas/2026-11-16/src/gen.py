import os, asyncio
from playwright.async_api import async_playwright

R = '/home/claude/oficina-torres-media/marcas/rockabilly/assets'
F = 'file:///home/claude/redes-rockabilly/node_modules/@fontsource'
OUT = '/home/claude/redes-rockabilly/out'
SRC = '/home/claude/redes-rockabilly/src'
os.makedirs(OUT, exist_ok=True); os.makedirs(SRC, exist_ok=True)

def foto(n): return f'file://{R}/fotos/{n}'
LOGO_CREMA = f'file://{R}/rockandbilly-crema.png'
LOGO_ROJO = f'file://{R}/rockandbilly-rojo.png'
MASCOTA = f'file://{R}/malteada-feliz-1500.png'

GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")

CSS = f"""
@font-face{{font-family:'Yellowtail';src:url('{F}/yellowtail/files/yellowtail-latin-400-normal.woff2')}}
@font-face{{font-family:'League Gothic';src:url('{F}/league-gothic/files/league-gothic-latin-400-normal.woff2')}}
@font-face{{font-family:'Oswald';font-weight:400;src:url('{F}/oswald/files/oswald-latin-400-normal.woff2')}}
@font-face{{font-family:'Oswald';font-weight:600;src:url('{F}/oswald/files/oswald-latin-600-normal.woff2')}}
@font-face{{font-family:'Alfa Slab One';src:url('{F}/alfa-slab-one/files/alfa-slab-one-latin-400-normal.woff2')}}
:root{{--rojo:#A80E12;--rojo2:#C4161C;--crema:#F6ECD6;--negro:#151110;--menta:#7FD3C9}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:var(--negro)}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Oswald';color:var(--crema)}}
.grain{{position:absolute;inset:0;background:url("{GRAIN}");opacity:.16;mix-blend-mode:multiply;pointer-events:none;z-index:50}}
.lg{{font-family:'League Gothic';text-transform:uppercase;line-height:.92;letter-spacing:1px}}
.yt{{font-family:'Yellowtail'}}
.alfa{{font-family:'Alfa Slab One'}}
.frame{{position:absolute;inset:34px;border:6px solid var(--crema);border-radius:26px;z-index:40;pointer-events:none}}
.frame:after{{content:'';position:absolute;inset:10px;border:2px solid var(--crema);border-radius:18px}}
.frame.r,.frame.r:after{{border-color:var(--rojo)}}
.checker{{background-color:#f3efe6;background-image:conic-gradient(#151110 25%,transparent 0 50%,#151110 0 75%,transparent 0);background-size:90px 90px}}
.rays{{background:repeating-conic-gradient(from 0deg at 50% 46%,var(--rojo2) 0 7.5deg,#B5121A 7.5deg 15deg)}}
.rays-c{{background:repeating-conic-gradient(from 0deg at 50% 46%,#F6ECD6 0 7.5deg,#EADBB8 7.5deg 15deg)}}
.photo{{position:absolute;background-size:cover;background-position:center}}
.page{{position:absolute;bottom:62px;right:74px;font-family:'Oswald';font-weight:600;font-size:30px;letter-spacing:4px;z-index:45}}
"""

def page(html, extra=''):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{html}</body></html>"

CTA = """<div style='font-size:42px;line-height:1.3;font-weight:400'>Plaza Outlet Escobedo<br>Citadel San Nicolás</div>
<div class='alfa' style='font-size:52px;margin-top:22px'>WhatsApp 81 2418 8940</div>"""

slides = {}

# ---------------- A · En todo grupo de amigos ----------------
slides['A1'] = page(f"""
<div class='s rays'>
  <div style='position:absolute;top:120px;left:0;right:0;text-align:center'>
    <div class='lg' style='font-size:118px;color:var(--crema);text-shadow:6px 6px 0 var(--negro)'>En todo grupo<br>de amigos hay…</div>
    <div class='yt' style='font-size:96px;color:var(--crema);margin-top:6px;text-shadow:4px 4px 0 var(--negro)'>¿cuál eres tú?</div>
  </div>
  <div class='photo' style='left:70px;top:640px;width:340px;height:440px;background-image:url({foto('nachos-rockabilly.jpg')});transform:rotate(-7deg);border:16px solid var(--crema);border-bottom-width:60px;box-shadow:10px 14px 0 rgba(0,0,0,.45)'></div>
  <div class='photo' style='left:370px;top:600px;width:340px;height:440px;background-image:url({foto('hamburguesa-rockabilly.jpg')});transform:rotate(2deg);border:16px solid var(--crema);border-bottom-width:60px;box-shadow:10px 14px 0 rgba(0,0,0,.45);z-index:2'></div>
  <div class='photo' style='left:670px;top:650px;width:340px;height:440px;background-image:url({foto('malteada-fresa.jpg')});background-position:center 60%;transform:rotate(8deg);border:16px solid var(--crema);border-bottom-width:60px;box-shadow:10px 14px 0 rgba(0,0,0,.45)'></div>
  <img src='{LOGO_CREMA}' style='position:absolute;bottom:70px;left:50%;transform:translateX(-50%);width:380px'>
  <div class='frame'></div><div class='grain'></div>
</div>""")

def tipo(num, titulo, remate, img, pos='center'):
    return page(f"""
<div class='s' style='background:var(--crema)'>
  <div class='photo' style='left:0;top:0;width:1080px;height:800px;background-image:url({foto(img)});background-position:{pos}'></div>
  <div style='position:absolute;top:740px;left:80px;background:var(--rojo2);color:var(--crema);padding:14px 34px;border-radius:14px;transform:rotate(-3deg);box-shadow:6px 6px 0 var(--negro);z-index:3'>
    <span class='alfa' style='font-size:46px'>TIPO #{num}</span></div>
  <div style='position:absolute;top:870px;left:80px;right:80px;color:var(--negro)'>
    <div class='lg' style='font-size:116px'>{titulo}</div>
    <div class='yt' style='font-size:76px;color:var(--rojo);margin-top:14px'>{remate}</div>
  </div>
  <div class='page' style='color:var(--rojo)'>{num+1}/5</div>
  <div class='frame r'></div><div class='grain'></div>
</div>""")

slides['A2'] = tipo(1, 'El que «no tiene hambre»', '…y se acaba tus nachos.', 'nachos-rockabilly.jpg')
slides['A3'] = tipo(2, 'El que pide lo mismo<br>hace 9 años', 'Rock&amp;Billy Burguer. Siempre.', 'hamburguesa-rockabilly.jpg', 'center 62%')
slides['A4'] = tipo(3, 'El que empieza<br>por la malteada', 'La comida puede esperar.', 'malteada-fresa.jpg', 'center 58%')

slides['A5'] = page(f"""
<div class='s checker'>
  <div style='position:absolute;left:90px;right:90px;top:150px;bottom:150px;background:var(--crema);border-radius:30px;box-shadow:14px 14px 0 var(--rojo2);border:6px solid var(--negro);padding:70px 60px;text-align:center;color:var(--negro)'>
    <div class='lg' style='font-size:130px;color:var(--rojo)'>Etiqueta<br>a cada uno</div>
    <div class='yt' style='font-size:84px;margin-top:10px'>y armen la salida</div>
    <div style='width:120px;height:6px;background:var(--rojo);margin:40px auto'></div>
    {CTA}
    <img src='{LOGO_ROJO}' style='width:340px;margin-top:44px'>
  </div>
  <div class='grain'></div>
</div>""")

# ---------------- B · Reglas de la casa ----------------
slides['B1'] = page(f"""
<div class='s' style='background:var(--crema);color:var(--negro)'>
  <div style='position:absolute;top:150px;left:0;right:0;text-align:center'>
    <div class='alfa' style='font-size:44px;letter-spacing:10px;color:var(--negro)'>★ MENÚ OFICIAL ★</div>
    <div class='lg' style='font-size:250px;color:var(--rojo);margin-top:20px;text-shadow:7px 7px 0 var(--negro)'>Reglas<br>de la casa</div>
    <div class='yt' style='font-size:80px;margin-top:20px'>léelas antes de venir</div>
  </div>
  <img src='{MASCOTA}' style='position:absolute;bottom:70px;right:110px;height:380px;transform:rotate(6deg)'>
  <img src='{LOGO_ROJO}' style='position:absolute;bottom:120px;left:110px;width:400px'>
  <div class='frame r'></div><div class='grain'></div>
</div>""")

def regla(n, texto, img, pos='center'):
    return page(f"""
<div class='s' style='background:var(--negro)'>
  <div style='position:absolute;top:110px;left:100px;display:flex;align-items:center;gap:34px;right:100px'>
    <div class='alfa' style='flex:none;width:170px;height:170px;border-radius:50%;background:var(--rojo2);color:var(--crema);font-size:84px;display:flex;align-items:center;justify-content:center;border:6px solid var(--crema)'>{n:02d}</div>
    <div class='lg' style='font-size:92px;color:var(--crema)'>{texto}</div>
  </div>
  <div class='photo' style='left:100px;right:100px;top:440px;height:780px;background-image:url({foto(img)});background-position:{pos};border:10px solid var(--crema);border-radius:22px;outline:3px solid var(--crema);outline-offset:10px'></div>
  <div class='page' style='color:var(--crema);bottom:56px;right:110px'>{n+1}/5</div>
  <div class='grain' style='opacity:.10;mix-blend-mode:screen'></div>
</div>""")

slides['B2'] = regla(1, 'Una hamburguesa<br>jamás se niega.', 'hamburguesa-bacon-texas-burguer.jpg', '70% center')
slides['B3'] = regla(2, 'La malteada no se<br>comparte. Se pide otra.', 'malteada-chocolate.jpg', 'center 62%')
slides['B4'] = regla(3, '¿No sabes qué pedir?<br>Pizza Burguer.', 'hamburguesa-pizza.jpg', 'center 60%')

slides['B5'] = page(f"""
<div class='s rays-c' style='color:var(--negro)'>
  <div style='position:absolute;top:150px;left:0;right:0;text-align:center'>
    <div class='lg' style='font-size:150px;color:var(--rojo);text-shadow:6px 6px 0 var(--negro)'>¿Qué regla<br>le falta?</div>
    <div class='yt' style='font-size:80px;margin-top:16px'>Escríbela en los comentarios</div>
    <div style='font-size:44px;margin-top:26px;font-weight:600;letter-spacing:2px'>Y GUARDA ESTE MENÚ PARA EL FIN.</div>
  </div>
  <div style='position:absolute;left:120px;right:120px;bottom:120px;background:var(--rojo);color:var(--crema);border-radius:26px;padding:46px 40px;text-align:center;border:6px solid var(--negro);box-shadow:10px 10px 0 var(--negro)'>
    {CTA}
    <img src='{LOGO_CREMA}' style='width:300px;margin-top:26px'>
  </div>
  <div class='grain'></div>
</div>""")

# ---------------- C · Plan de domingo: ¿qué pides primero? ----------------
slides['C1'] = page(f"""
<div class='s checker'>
  <div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,17,16,.0) 0%,rgba(21,17,16,0) 100%)'></div>
  <div style='position:absolute;left:50%;top:640px;transform:translate(-50%,-50%);width:900px;height:900px;border-radius:50%;background:var(--rojo2);border:12px solid var(--crema);outline:6px solid var(--negro);box-shadow:0 0 0 22px var(--negro);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center'>
    <div class='yt' style='font-size:100px;color:var(--crema);text-shadow:4px 4px 0 var(--negro)'>Plan de domingo</div>
    <div class='lg' style='font-size:150px;color:var(--crema);margin-top:6px;text-shadow:6px 6px 0 var(--negro)'>¿Qué pides<br>primero?</div>
    <div class='alfa' style='font-size:92px;color:var(--negro);background:var(--crema);padding:6px 40px;border-radius:60px;margin-top:26px'>1 · 2 · 3</div>
  </div>
  <div style='position:absolute;bottom:60px;left:50%;transform:translateX(-50%);background:var(--negro);padding:18px 46px;border-radius:20px'>
    <img src='{LOGO_CREMA}' style='width:340px;display:block'></div>
  <div class='grain'></div>
</div>""")

def opcion(n, nombre, linea, img, pos='center'):
    return page(f"""
<div class='s'>
  <div class='photo' style='inset:0;background-image:url({foto(img)});background-position:{pos}'></div>
  <div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,17,16,0) 45%,rgba(21,17,16,.92) 78%)'></div>
  <div class='alfa' style='position:absolute;top:90px;left:90px;width:200px;height:200px;border-radius:50%;background:var(--crema);color:var(--rojo);font-size:130px;display:flex;align-items:center;justify-content:center;border:8px solid var(--rojo2);box-shadow:8px 8px 0 var(--negro)'>{n}</div>
  <div style='position:absolute;left:90px;right:90px;bottom:150px'>
    <div class='lg' style='font-size:150px;color:var(--crema)'>{nombre}</div>
    <div style='font-size:46px;margin-top:16px;line-height:1.25'>{linea}</div>
  </div>
  <div class='page' style='color:var(--crema)'>{n+1}/5</div>
  <div class='frame'></div><div class='grain'></div>
</div>""")

slides['C2'] = opcion(1, 'Hot dog pizza', 'Para el que no se decide entre las dos.', 'hotdog-pizza.jpg', '60% center')
slides['C3'] = opcion(2, 'Tacos de trompo', 'Para el que viene a un diner… y pide tacos.', 'tacos-trompo.jpg', '45% center')
slides['C4'] = opcion(3, 'Boneless buffalo', 'Para compartir. (Eso dice.)', 'bonneles-buffalo.jpg', 'center 45%')

slides['C5'] = page(f"""
<div class='s' style='background:var(--rojo)'>
  <div class='checker' style='position:absolute;left:0;right:0;top:0;height:110px'></div>
  <div class='checker' style='position:absolute;left:0;right:0;bottom:0;height:110px'></div>
  <div style='position:absolute;top:200px;left:80px;right:80px;text-align:center'>
    <div class='lg' style='font-size:160px;text-shadow:6px 6px 0 var(--negro)'>Comenta<br>tu número</div>
    <div class='yt' style='font-size:76px;margin-top:16px'>y etiqueta con quién vienes</div>
    <div style='width:120px;height:6px;background:var(--crema);margin:44px auto'></div>
    {CTA}
    <img src='{LOGO_CREMA}' style='width:360px;margin-top:40px'>
  </div>
  <div class='grain'></div>
</div>""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350})
        for k, html in slides.items():
            path = f'{SRC}/{k}.html'
            open(path,'w').write(html)
            await pg.goto('file://'+path)
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(250)
            await pg.screenshot(path=f'{OUT}/{k}.png')
        await b.close()
    from PIL import Image
    for k in slides:
        Image.open(f'{OUT}/{k}.png').convert('RGB').save(f'{OUT}/{k}.jpg', quality=90)
        os.remove(f'{OUT}/{k}.png')
    for c in 'ABC':
        ims=[Image.open(f'{OUT}/{c}{i}.jpg').resize((432,540)) for i in range(1,6)]
        st=Image.new('RGB',(432*5+40,540),'white')
        for i,im in enumerate(ims): st.paste(im,(i*442,0))
        st.save(f'/home/claude/redes-rockabilly/tira_{c}.jpg',quality=85)
asyncio.run(main())
