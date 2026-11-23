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

def page(html, extra=''):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{html}</body></html>"

CTA = """<div style='font-size:42px;line-height:1.3;font-weight:400'>Plaza Outlet Escobedo<br>Citadel San Nicolás</div>
<div class='alfa' style='font-size:50px;margin-top:20px'>WhatsApp 81 2418 8940</div>"""

PAPER = "background:#F3E7CC;background-image:repeating-linear-gradient(0deg,transparent 0 62px,rgba(168,14,18,.13) 62px 64px)"
STAMP = ("position:absolute;border:9px solid var(--rojo2);color:var(--rojo2);border-radius:18px;padding:6px 34px;"
         "letter-spacing:4px;opacity:.88;mix-blend-mode:multiply")
slides = {}

# ================= A · Aviso de cobranza (compartible) =================
slides['A1'] = page(f"""
<div class='s' style='background:var(--negro)'>
  <div class='photo' style='left:0;right:0;bottom:0;height:560px;background-image:url({foto('hamburguesa-bacon-texas-burguer.jpg')});background-position:center 45%'></div>
  <div style='position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(180deg,var(--negro) 0%,rgba(21,17,16,0) 40%)'></div>
  <div style='position:absolute;left:90px;right:90px;top:100px;height:860px;{PAPER};transform:rotate(-2.5deg);box-shadow:16px 18px 0 rgba(0,0,0,.55);padding:60px 64px;color:var(--negro);z-index:3'>
    <div style='display:flex;justify-content:space-between;align-items:center;border-bottom:5px double var(--negro);padding-bottom:18px'>
      <div class='lg' style='font-size:84px;color:var(--rojo)'>Aviso de cobranza</div>
      <div class='alfa' style='font-size:34px'>Nº 1955</div>
    </div>
    <div class='lg' style='font-size:150px;margin-top:44px;line-height:.9'>Alguien te debe<br><span style='color:var(--rojo)'>una burguer</span></div>
    <div class='yt' style='font-size:84px;margin-top:26px'>y sabe perfecto quién es</div>
    <div class='alfa' style='{STAMP};font-size:70px;right:46px;bottom:44px;transform:rotate(-8deg)'>VENCIDO</div>
  </div>
  <img src='{LOGO_CREMA}' style='position:absolute;bottom:70px;right:80px;width:330px;z-index:4;filter:drop-shadow(3px 3px 0 #000)'>
  <div class='grain'></div>
</div>""")

def deudor(n, quien, debe, img, pos='center'):
    return page(f"""
<div class='s' style='background:var(--negro)'>
  <div class='photo' style='left:0;top:0;width:1080px;height:820px;background-image:url({foto(img)});background-position:{pos}'></div>
  <div style='position:absolute;left:70px;right:70px;top:720px;bottom:110px;{PAPER};box-shadow:12px 14px 0 rgba(0,0,0,.6);padding:46px 56px;color:var(--negro);transform:rotate({-1.5 if n%2 else 1.5}deg)'>
    <div class='alfa' style='font-size:40px;color:var(--rojo);letter-spacing:3px'>DEUDOR #{n}</div>
    <div class='lg' style='font-size:104px;margin-top:14px'>{quien}</div>
    <div style='border-top:4px dashed var(--negro);margin:26px 0 18px'></div>
    <div style='font-size:46px;font-weight:600'>DEBE: <span class='yt' style='font-size:74px;color:var(--rojo);font-weight:400'>{debe}</span></div>
    <div class='alfa' style='{STAMP};font-size:44px;right:44px;top:40px;transform:rotate(9deg)'>PENDIENTE</div>
  </div>
  <div class='page' style='color:var(--crema);bottom:42px'>{n+1}/5</div>
  <div class='grain'></div>
</div>""")

slides['A2'] = deudor(1, 'El que te dejó<br>en visto', 'una malteada de fresa', 'malteada-fresa.jpg', 'center 22%')
slides['A3'] = deudor(2, 'El de «ahorita<br>te lo pago»', 'unos nachos', 'nachos-rockabilly.jpg', 'center 55%')
slides['A4'] = deudor(3, 'El que se comió<br>tus papas', 'una Bacon Texas Burguer', 'hamburguesa-bacon-texas-burguer.jpg', 'center 45%')

slides['A5'] = page(f"""
<div class='s rays'>
  <div style='position:absolute;left:100px;right:100px;top:130px;bottom:130px;{PAPER};box-shadow:16px 16px 0 var(--negro);padding:70px 60px;text-align:center;color:var(--negro)'>
    <div class='lg' style='font-size:150px;color:var(--rojo)'>Cóbrasela</div>
    <div class='yt' style='font-size:80px;margin-top:6px'>etiquétalo en los comentarios</div>
    <div style='width:140px;height:6px;background:var(--rojo);margin:44px auto'></div>
    <div class='alfa' style='font-size:36px;letter-spacing:3px;margin-bottom:16px'>LUGAR DE COBRO</div>
    {CTA}
    <img src='{LOGO_ROJO}' style='width:330px;margin-top:40px'>
  </div>
  <div class='grain'></div>
</div>""")

# ================= B · Boleto a 1955 (antojo) =================
TICKET = ("background:var(--crema);color:var(--negro);border-radius:26px;"
          "-webkit-mask:radial-gradient(circle 34px at 0 50%,transparent 98%,#000) left/51% 100% no-repeat,"
          "radial-gradient(circle 34px at 100% 50%,transparent 98%,#000) right/51% 100% no-repeat")
slides['B1'] = page(f"""
<div class='s' style='background:var(--negro)'>
  <div class='photo' style='inset:0;background-image:url({foto('hamburguesa-rockabilly.jpg')});background-position:center 60%;filter:brightness(.55)'></div>
  <div style='position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(21,17,16,.1),rgba(21,17,16,.75))'></div>
  <div style='position:absolute;top:110px;left:0;right:0;text-align:center'>
    <div class='yt' style='font-size:120px;color:var(--crema);text-shadow:5px 5px 0 var(--rojo)'>Viaje en el tiempo</div>
  </div>
  <div style='position:absolute;left:90px;right:90px;top:330px;height:560px;{TICKET};transform:rotate(-3deg);box-shadow:0 20px 40px rgba(0,0,0,.6)'>
    <div style='position:absolute;inset:26px 70px;border:4px dashed var(--rojo);border-radius:14px'></div>
    <div style='position:absolute;top:70px;left:0;right:0;text-align:center'>
      <div class='alfa' style='font-size:40px;letter-spacing:8px;color:var(--rojo)'>BOLETO · SOLO IDA</div>
      <div class='lg' style='font-size:118px;margin-top:20px'>Destino</div>
      <div class='alfa' style='font-size:190px;color:var(--rojo);line-height:1;text-shadow:6px 6px 0 var(--negro)'>1955</div>
      <div style='font-size:42px;font-weight:600;letter-spacing:3px;margin-top:18px'>3 PARADAS · DESLIZA →</div>
    </div>
  </div>
  <img src='{LOGO_CREMA}' style='position:absolute;bottom:90px;left:50%;transform:translateX(-50%);width:400px;filter:drop-shadow(3px 3px 0 #000)'>
  <div class='frame'></div><div class='grain'></div>
</div>""")

def parada(n, platillo, frase, img, pos='center'):
    return page(f"""
<div class='s' style='background:var(--negro)'>
  <div class='photo' style='inset:0;background-image:url({foto(img)});background-position:{pos}'></div>
  <div style='position:absolute;left:0;right:0;bottom:0;height:640px;background:linear-gradient(0deg,rgba(21,17,16,.97) 30%,rgba(21,17,16,0))'></div>
  <div style='position:absolute;top:96px;left:90px;background:var(--rojo2);padding:16px 36px;border-radius:12px;border:5px solid var(--crema);transform:rotate(-3deg);box-shadow:6px 6px 0 var(--negro)'>
    <span class='alfa' style='font-size:48px;color:var(--crema);letter-spacing:3px'>PARADA {n}</span></div>
  <div style='position:absolute;left:90px;right:90px;bottom:150px'>
    <div class='lg' style='font-size:136px;color:var(--crema)'>{platillo}</div>
    <div class='yt' style='font-size:78px;color:#F2C14E;margin-top:16px'>{frase}</div>
  </div>
  <div class='page' style='color:var(--crema);bottom:70px;right:90px'>{n+1}/5</div>
  <div class='frame'></div><div class='grain'></div>
</div>""")

slides['B2'] = parada(1, 'Rock&amp;Billy Burguer', 'aquí arranca el viaje', 'hamburguesa-rockabilly.jpg', 'center 40%')
slides['B3'] = parada(2, 'Malteada de chocolate', 'combustible oficial de la máquina', 'malteada-chocolate.jpg', 'center 35%')
slides['B4'] = parada(3, 'Pizza Burguer', 'el futuro llegó al pasado', 'hamburguesa-pizza.jpg', '30% center')

slides['B5'] = page(f"""
<div class='s' style='background:var(--crema)'>
  <div class='photo checker' style='left:0;right:0;top:0;height:180px'></div>
  <div class='photo checker' style='left:0;right:0;bottom:0;height:180px'></div>
  <div style='position:absolute;top:230px;left:80px;right:80px;text-align:center;color:var(--negro)'>
    <div class='lg' style='font-size:140px;color:var(--rojo)'>¿Con quién<br>viajas?</div>
    <div class='yt' style='font-size:78px;margin-top:10px'>mándale este boleto a tu copiloto</div>
    <div style='width:140px;height:6px;background:var(--rojo);margin:40px auto'></div>
    {CTA}
  </div>
  <img src='{MASCOTA}' style='position:absolute;bottom:150px;right:70px;height:300px;transform:rotate(8deg)'>
  <img src='{LOGO_ROJO}' style='position:absolute;bottom:215px;left:90px;width:300px'>
  <div class='grain'></div>
</div>""")

# ================= C · Bingo del domingo (planes) =================
BALL = ("display:inline-flex;align-items:center;justify-content:center;width:150px;height:150px;border-radius:50%;"
        "background:radial-gradient(circle at 35% 30%,#fff 0 18%,var(--crema) 19% 100%);border:7px solid var(--negro);"
        "font-size:84px;color:var(--rojo);box-shadow:7px 7px 0 var(--negro)")
slides['C1'] = page(f"""
<div class='s checker'>
  <div style='position:absolute;left:70px;right:70px;top:90px;bottom:90px;background:var(--rojo2);border:7px solid var(--negro);border-radius:30px;box-shadow:14px 14px 0 var(--negro)'></div>
  <div style='position:absolute;top:150px;left:0;right:0;text-align:center;display:flex;justify-content:center;gap:18px'>
    {''.join(f"<span class='alfa' style='{BALL};transform:rotate({r}deg)'>{l}</span>" for l,r in zip('BINGO',[-8,5,-4,7,-6]))}
  </div>
  <div style='position:absolute;top:360px;left:0;right:0;text-align:center'>
    <div class='yt' style='font-size:120px;color:var(--crema);text-shadow:5px 5px 0 var(--negro)'>del domingo</div>
    <div class='lg' style='font-size:92px;color:var(--crema);margin-top:6px'>¿Cuántas casillas tachas hoy?</div>
  </div>
  <div class='photo' style='left:150px;right:150px;top:690px;height:390px;background-image:url({foto('buffet-pizza.jpg')});border:12px solid var(--crema);border-radius:20px;transform:rotate(2deg);box-shadow:10px 10px 0 var(--negro)'></div>
  <img src='{LOGO_CREMA}' style='position:absolute;bottom:120px;left:50%;transform:translateX(-50%);width:330px;filter:drop-shadow(3px 3px 0 #000)'>
  <div class='grain'></div>
</div>""")

def celda_foto(img, txt, pos='center'):
    return (f"<div class='cell' style='background-image:url({foto(img)});background-size:cover;background-position:{pos}'>"
            f"<div class='lab'>{txt}</div></div>")
def celda_txt(txt):
    return f"<div class='cell t'><div class='lg' style='font-size:58px'>{txt}</div></div>"
CARD_CSS = """
.grid{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:14px;position:absolute;left:96px;right:96px;top:300px;bottom:150px}
.cell{position:relative;border:6px solid var(--negro);border-radius:14px;overflow:hidden;background:var(--crema);display:flex;align-items:center;justify-content:center;text-align:center;color:var(--negro)}
.cell.t{padding:14px;background:#F3E7CC}
.lab{position:absolute;left:0;right:0;bottom:0;background:rgba(21,17,16,.86);color:var(--crema);font-family:'League Gothic';text-transform:uppercase;font-size:44px;line-height:1;padding:10px 8px 8px}
"""
slides['C2'] = page(f"""
<div class='s' style='background:var(--rojo2)'>
  <div style='position:absolute;inset:60px;background:var(--crema);border:7px solid var(--negro);border-radius:30px'></div>
  <div style='position:absolute;top:110px;left:0;right:0;text-align:center'>
    <div class='lg' style='font-size:120px;color:var(--rojo);letter-spacing:12px'>B · I · N · G · O</div>
    <div style='font-size:40px;font-weight:600;color:var(--negro);letter-spacing:2px'>TACHA LO QUE TE PASE HOY</div>
  </div>
  <div class='grid'>
    {celda_foto('malteada-vainilla.jpg','Malteada antes de comer','center 40%')}
    {celda_txt('Alguien dice «yo nomás pruebo»')}
    {celda_foto('tacos-trompo.jpg','Tacos de trompo')}
    {celda_txt('Robarle papas a alguien')}
    <div class='cell' style='background:var(--rojo2)'><img src='{MASCOTA}' style='height:200px;position:absolute;top:14px'><div class='alfa' style='position:absolute;bottom:14px;font-size:46px;color:var(--crema)'>LIBRE</div></div>
    {celda_foto('buffet-pizza2.jpg','Vuelta extra al buffet')}
    {celda_txt('La foto antes de comer')}
    {celda_foto('hotdog-polaco.jpg','Hot dog polaco')}
    {celda_txt('Postre «para compartir»')}
  </div>
  <div class='page' style='color:var(--negro);bottom:92px;right:110px'>2/5</div>
  <div class='grain'></div>
</div>""", CARD_CSS)

slides['C3'] = page(f"""
<div class='s' style='background:var(--negro)'>
  <div class='photo' style='left:0;right:0;top:0;height:760px;background-image:url({foto('buffet-postre-pastel.jpg')});background-position:center'></div>
  <div style='position:absolute;left:0;right:0;top:560px;height:200px;background:linear-gradient(0deg,var(--negro),rgba(21,17,16,0))'></div>
  <div style='position:absolute;left:90px;right:90px;top:740px'>
    <div class='alfa' style='font-size:42px;color:#F2C14E;letter-spacing:3px'>LA CASILLA MÁS DIFÍCIL</div>
    <div class='lg' style='font-size:150px;color:var(--crema);margin-top:16px'>No pedir postre</div>
    <div class='yt' style='font-size:80px;color:var(--crema);margin-top:14px'>nadie la ha tachado</div>
  </div>
  <div class='page' style='color:var(--crema)'>3/5</div>
  <div class='frame'></div><div class='grain'></div>
</div>""")

slides['C4'] = page(f"""
<div class='s rays-c'>
  <div style='position:absolute;top:130px;left:90px;right:90px;text-align:center;color:var(--negro)'>
    <div class='lg' style='font-size:118px;color:var(--rojo)'>Cómo se gana</div>
  </div>
  <div style='position:absolute;top:330px;left:110px;right:110px;display:flex;flex-direction:column;gap:40px'>
    {''.join(f"<div style='display:flex;align-items:center;gap:34px;background:var(--crema);border:6px solid var(--negro);border-radius:22px;padding:26px 34px;box-shadow:8px 8px 0 var(--rojo2)'><span class='alfa' style='{BALL};width:120px;height:120px;font-size:62px;flex:none;box-shadow:none'>{n}</span><span class='lg' style='font-size:76px;color:var(--negro)'>{t}</span></div>" for n,t in [(1,'Vienes con tu gente'),(2,'Tachas lo que pase'),(3,'Tres en línea: ganaste el domingo')])}
  </div>
  <div class='page' style='color:var(--rojo)'>4/5</div>
  <div class='frame r'></div><div class='grain'></div>
</div>""")

slides['C5'] = page(f"""
<div class='s' style='background:var(--negro)'>
  <div style='position:absolute;inset:0;background:repeating-linear-gradient(90deg,var(--rojo2) 0 90px,#B5121A 90px 180px);opacity:.9'></div>
  <div style='position:absolute;left:100px;right:100px;top:140px;bottom:140px;background:var(--crema);border:7px solid var(--negro);border-radius:30px;box-shadow:14px 14px 0 var(--negro);padding:70px 60px;text-align:center;color:var(--negro)'>
    <div class='lg' style='font-size:130px;color:var(--rojo)'>Comenta cuántas<br>tachaste</div>
    <div class='yt' style='font-size:76px;margin-top:10px'>y etiqueta a tu equipo</div>
    <div style='width:140px;height:6px;background:var(--rojo);margin:40px auto'></div>
    {CTA}
    <img src='{LOGO_ROJO}' style='width:320px;margin-top:40px'>
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
