# Genera las láminas HTML de BROSFIT (semana 2026-11-16)
import os
A = '/home/claude/oficina-torres-media/marcas/brosfit/assets'
F = '/home/claude/redes-brosfit/node_modules/@fontsource'
OUT = '/home/claude/redes-brosfit/html'
os.makedirs(OUT, exist_ok=True)
RED = '#d6453d'

CSS = f"""
@font-face{{font-family:Anton;src:url(file://{F}/anton/files/anton-latin-400-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:500;src:url(file://{F}/barlow-condensed/files/barlow-condensed-latin-500-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:700;src:url(file://{F}/barlow-condensed/files/barlow-condensed-latin-700-normal.woff2)}}
@font-face{{font-family:Barlow;font-weight:800;src:url(file://{F}/barlow-condensed/files/barlow-condensed-latin-800-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:#151515;color:#f1ece2;font-family:Barlow;font-weight:700;position:relative}}
.glow{{position:absolute;inset:0;background:radial-gradient(circle at var(--gx,80%) var(--gy,30%),rgba(214,69,61,.38),transparent 55%)}}
.grain{{position:absolute;inset:0;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}}
.stripe{{position:absolute;top:0;left:0;right:0;height:22px;background:repeating-linear-gradient(-45deg,{RED} 0 18px,#151515 18px 36px)}}
.wm{{position:absolute;right:-90px;bottom:120px;width:520px;opacity:.06}}
.wrap{{position:absolute;left:84px;right:84px;top:80px;bottom:140px;display:flex;flex-direction:column;justify-content:center}}
.wrap>*{{flex:none}}
.foot{{position:absolute;left:84px;right:84px;bottom:56px;display:flex;align-items:center;gap:22px;font-size:26px;letter-spacing:4px;color:#bdb6aa}}
.foot img{{height:34px}}
.foot .n{{margin-left:auto;font-size:30px;letter-spacing:2px;color:#f1ece2}}
.kick{{font-size:34px;letter-spacing:7px;color:{RED};font-weight:800;text-transform:uppercase}}
.h{{font-family:Anton;text-transform:uppercase;line-height:.98;letter-spacing:.5px}}
.red{{color:{RED}}} .muted{{color:#a59e93}}
.body{{font-size:46px;line-height:1.18;font-weight:700}}
.hl{{background:{RED};color:#fff;padding:0 12px;white-space:nowrap}}
.badge{{position:absolute;right:70px;top:70px;width:170px;height:170px}}
.card{{background:#222;border-radius:28px;padding:44px 48px;border:2px solid #333}}
.cardr{{background:{RED};color:#fff;border-radius:28px;padding:44px 48px}}
.pill{{display:inline-block;font-size:30px;letter-spacing:4px;font-weight:800;padding:8px 22px;border-radius:40px;background:#333;color:#d9d2c6}}
.cta{{display:flex;align-items:center;gap:26px;background:{RED};color:#fff;border-radius:90px;padding:26px 44px;font-size:52px;font-weight:800}}
.cta small{{display:block;font-size:30px;font-weight:700;opacity:.9;letter-spacing:1px}}
.addr{{display:flex;align-items:center;gap:16px;font-size:38px;color:#e6dfd3}}
"""

def badge():
    return f"""<svg class="badge" viewBox="0 0 200 200"><defs><path id="c" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs>
<circle cx="100" cy="100" r="96" fill="#f1ece2"/><circle cx="100" cy="100" r="54" fill="{RED}"/>
<text font-family="Barlow" font-weight="800" font-size="19" letter-spacing="3" fill="#151515"><textPath href="#c">LLEGA A ENERO ENTRENANDO · NOV–DIC ·</textPath></text>
<text x="100" y="96" text-anchor="middle" font-family="Anton" font-size="26" fill="#fff">BROS</text><text x="100" y="124" text-anchor="middle" font-family="Anton" font-size="26" fill="#fff">FIT</text></svg>"""

PIN = f'<svg width="40" height="48" viewBox="0 0 24 30"><path d="M12 0C5.4 0 0 5.2 0 11.7 0 20 12 30 12 30s12-10 12-18.3C24 5.2 18.6 0 12 0z" fill="{RED}"/><circle cx="12" cy="11.5" r="4.5" fill="#151515"/></svg>'
WA = '<svg width="64" height="64" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="#fff"/><path d="M9 23l1.2-3.6A7.5 7.5 0 1 1 13 22z" fill="none" stroke="#d6453d" stroke-width="2.2" stroke-linejoin="round"/><path d="M13.2 12.6c.3 1.9 2.2 3.9 4.2 4.4l1.1-1.1 1.7.9-.4 1.6c-3.4.4-7.6-3.6-7.6-6.9l1.6-.5.9 1.7z" fill="#d6453d"/></svg>'
DUMB = f'<svg width="{{w}}" viewBox="0 0 220 80"><rect x="40" y="34" width="140" height="12" rx="4" fill="#bdb6aa"/><rect x="18" y="8" width="26" height="64" rx="6" fill="{RED}"/><rect x="176" y="8" width="26" height="64" rx="6" fill="{RED}"/><rect x="2" y="20" width="18" height="40" rx="5" fill="#f1ece2"/><rect x="200" y="20" width="18" height="40" rx="5" fill="#f1ece2"/></svg>'

def page(name, inner, n, N, gx='80%', gy='30%', bg=None):
    style = f"--gx:{gx};--gy:{gy};" + (f"background:{bg};" if bg else '')
    logo = 'BROSFITLETRAS-blanco.png'
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body style="{style}"><div class="glow"></div><div class="grain"></div><div class="stripe"></div>
<img class="wm" src="file://{A}/KERBELL-blanco.png">
{inner}
<div class="foot"><img src="file://{A}/{logo}"><span>ESCOBEDO, N.L.</span><span class="n">{n:02d} / {N:02d} &nbsp;→</span></div>
</body></html>"""
    open(f'{OUT}/{name}.html', 'w').write(html)

def ctablock(extra=''):
    return f"""<div style="display:flex;flex-direction:column;gap:30px;align-items:flex-start">
<div class="cta">{WA}<div><small>Escríbenos por WhatsApp</small>81 2909 0049</div></div>
<div style="font-size:40px;color:#e6dfd3">o mándanos DM aquí en <span class="red" style="font-weight:800">@brosfitgym</span></div>
<div class="addr">{PIN}Av. Raúl Salinas Lozano 1101, C.P. 66055, Escobedo, N.L.</div>{extra}</div>"""

# ---------- A · Traductor del «ya mero empiezo» ----------
def tr(src, dst, note=''):
    return f"""<div class="card" style="padding:38px 44px">
  <div class="pill">LO QUE DICES</div>
  <div class="h" style="font-size:108px;margin-top:22px">«{src}»</div>
</div>
<div style="display:flex;justify-content:center;margin:26px 0"><svg width="90" height="90" viewBox="0 0 90 90"><circle cx="45" cy="45" r="43" fill="{RED}"/><path d="M45 22v40M28 47l17 17 17-17" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<div class="cardr" style="padding:38px 44px">
  <div class="pill" style="background:rgba(0,0,0,.25);color:#fff">LO QUE SIGNIFICA</div>
  <div class="h" style="font-size:108px;margin-top:22px">{dst}</div>
</div>
<div class="body" style="margin-top:50px;font-size:52px">{note}</div>"""

page('A1', f"""<div class="wrap">
<div class="kick">Traductor de gym · edición puente</div>
<div class="h" style="font-size:200px;margin-top:26px">«YA MERO<br><span class="red">EMPIEZO»</span></div>
<div class="body" style="margin-top:40px;max-width:860px;font-size:54px">Lo has dicho. Lo hemos dicho. Aquí está la traducción oficial.</div>
<div class="card" style="margin-top:56px;display:flex;align-items:center;gap:30px;padding:34px 44px">
  <div class="pill">TRADUCIENDO</div>
  <div style="display:flex;gap:16px">{''.join(f'<span style="width:30px;height:30px;border-radius:50%;background:{c};display:inline-block"></span>' for c in [RED,'#8a3a35','#4a2c2a'])}</div>
  <div style="margin-left:auto;font-size:40px;color:#bdb6aa">Desliza →</div>
</div></div>""", 1, 5, gx='85%', gy='20%')

page('A2', f'<div class="wrap">{tr("Después del puente", "Después de la quincena.", "Porque con el puente se nos fue el lunes… y el impulso.")}</div>', 2, 5, gy='60%')
page('A3', f'<div class="wrap">{tr("Después de la quincena", "Después de las posadas.", "Ya en diciembre <span class=hl>nadie</span> empieza nada. Tú lo sabes.")}</div>', 3, 5, gx='20%', gy='55%')
page('A4', f'<div class="wrap">{tr("En enero, ahora sí", "Después de la cuesta de enero.", "Y así se nos van tres años. El que avisa no es traidor.")}</div>', 4, 5, gy='65%')

page('A5', f"""<div class="wrap">
<div class="kick">Traducción final</div>
<div class="h" style="font-size:150px;margin-top:22px">EMPIEZA<br><span class="red">ESTA SEMANA.</span></div>
<div class="body" style="margin:30px 0 60px;max-width:860px">Sin esperar el puente, la quincena ni enero. <span class="hl">Llega a enero entrenando.</span></div>
{ctablock()}</div>{badge().replace('top:70px','top:70px')}""", 5, 5, gx='85%', gy='15%')

# ---------- B · Faltan 6 semanas ----------
def weeks(active):
    cells = ''
    for i in range(1, 7):
        on = i in active
        cells += f"""<div style="flex:1;height:120px;border-radius:18px;background:{RED if on else '#262626'};border:2px solid {'#e2625a' if on else '#383838'};display:flex;flex-direction:column;align-items:center;justify-content:center">
<div style="font-size:26px;letter-spacing:3px;color:{'#fff' if on else '#8d877d'}">SEM</div><div class="h" style="font-size:58px;color:{'#fff' if on else '#6f6a62'}">{i}</div></div>"""
    return f'<div style="display:flex;gap:14px">{cells}</div>'

page('B1', f"""<div class="wrap">
<div class="kick">Llega a enero entrenando</div>
<div style="display:flex;align-items:flex-end;gap:30px;margin-top:10px">
  <div class="h red" style="font-size:520px;line-height:.86">6</div>
  <div class="h" style="font-size:118px;padding-bottom:40px">SEMANAS<br>PARA<br>ENERO</div>
</div>
<div style="margin-top:40px">{weeks([])}</div>
<div class="body" style="margin-top:50px;max-width:900px;font-size:52px">Y un plan sencillo que <span class="hl">sí cabe en diciembre</span>. Guárdalo antes de que se te olvide.</div>
</div>""", 1, 5, gx='25%', gy='30%')

def wk(sem, fechas, titulo, txt, active, icon):
    return f"""<div class="wrap">
<div class="kick">{sem} · {fechas}</div>
<div style="margin-top:34px">{weeks(active)}</div>
<div style="display:flex;align-items:center;gap:30px;margin-top:70px">{icon}<div class="h" style="font-size:122px">{titulo}</div></div>
<div class="body" style="margin-top:50px;font-size:56px;max-width:900px">{txt}</div>
</div>"""

CHECK = f'<svg width="120" height="120" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="{RED}"/><path d="M28 52l15 15 30-32" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
STAR = f'<svg width="120" height="120" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="{RED}"/><path d="M50 18l8.8 19.5 21.2 2.3-15.8 14.3 4.4 20.9L50 64.4 31.4 75l4.4-20.9L20 39.8l21.2-2.3z" fill="#fff"/></svg>'
FLAG = f'<svg width="120" height="120" viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="{RED}"/><path d="M34 78V22" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path d="M37 24h32l-8 12 8 12H37z" fill="#fff"/></svg>'
page('B2', wk('Semanas 1 y 2', '23 nov – 6 dic', 'Conocer<br><span class="red">y repetir</span>', '2 o 3 días por semana. Aprende dónde está todo. La meta es <span class="hl">no faltar</span>, no romper récords.', [1, 2], CHECK), 2, 5, gy='70%')
page('B3', wk('Semanas 3 y 4', '7 – 20 dic', 'Temporada<br><span class="red">de posadas</span>', '¿Posada en la noche? Entrena antes. Un día menos <span class="hl">no es un día perdido</span>.', [3, 4], STAR), 3, 5, gx='20%', gy='70%')
page('B4', wk('Semanas 5 y 6', '21 dic – 3 ene', 'Navidad y<br><span class="red">Año Nuevo</span>', 'Aunque sea 1 o 2 días. Llegar entrenando le gana a <span class="hl">empezar de cero</span>.', [5, 6], FLAG), 4, 5, gy='70%')

page('B5', f"""<div class="wrap">
<div class="kick">La semana 1 arranca el 23 de nov</div>
<div class="h" style="font-size:132px;margin-top:22px">TÚ NO ESPERES<br><span class="red">A ENERO.</span></div>
<div class="body" style="margin:30px 0 56px;max-width:880px">Guarda el plan y escríbenos para conocer BROSFIT esta misma semana.</div>
{ctablock()}</div>{badge()}""", 5, 5, gx='85%', gy='15%')

# ---------- C · Encuesta del domingo ----------
OPTS = [('0', 'días'), ('1–2', 'días'), ('3–4', 'días'), ('5+', 'días')]
def opt(v, on=False, big=False):
    s = 150 if big else 112
    return f"""<div style="flex:1;border-radius:24px;padding:26px 0;text-align:center;background:{RED if on else '#232323'};border:3px solid {RED if on else '#3a3a3a'}">
<div class="h" style="font-size:{s}px;color:{'#fff' if on else '#f1ece2'}">{v}</div><div style="font-size:32px;letter-spacing:4px;color:{'#fff' if on else '#a59e93'}">DÍAS</div></div>"""
def opts(on=None):
    return '<div style="display:flex;gap:18px">' + ''.join(opt(v, on == v) for v, _ in OPTS) + '</div>'

page('C1', f"""<div class="wrap">
<div class="kick">Encuesta de domingo · sé honesto</div>
<div class="h" style="font-size:150px;margin-top:26px">¿CUÁNTOS DÍAS<br><span class="red">ENTRENASTE</span><br>ESTA SEMANA?</div>
<div style="margin-top:64px">{opts()}</div>
<div class="body" style="margin-top:60px;max-width:900px;font-size:52px">Comenta tu número. Desliza para ver <span class="hl">qué dice de ti</span>.</div>
</div>""", 1, 5, gx='80%', gy='18%')

def res(v, titulo, txt):
    return f"""<div class="wrap">
<div class="kick">Si contestaste…</div>
<div style="margin-top:34px">{opts(v)}</div>
<div class="h red" style="font-size:250px;margin-top:56px;line-height:.9">{v}</div>
<div class="h" style="font-size:104px;margin-top:10px">{titulo}</div>
<div class="body" style="margin-top:40px;font-size:54px;max-width:900px">{txt}</div>
</div>"""

page('C2', res('0', 'Modo puente extendido', 'Sin culpa. Mañana es lunes y esta vez <span class="hl">sí cuenta</span>. Con un día ya arrancaste.'), 2, 5, gy='60%')
page('C3', res('1–2', 'Ya arrancaste', 'Lo difícil era empezar. La próxima semana, <span class="hl">repite lo mismo</span>. Así se hace costumbre.'), 3, 5, gx='20%', gy='60%')
page('C4', res('3–4', 'Ya es costumbre', 'Ya tienes máquina favorita y te saludan al entrar. <span class="hl">Eso es constancia.</span>'), 4, 5, gy='60%')

page('C5', f"""<div class="wrap">
<div style="display:flex;align-items:center;gap:36px">
 <div class="h red" style="font-size:220px;line-height:.9">5+</div>
 <div><div class="h" style="font-size:96px">Ya vives aquí</div><div class="body" style="margin-top:10px">Nomás te falta traer tu cobija.</div></div>
</div>
<div style="height:3px;background:#333;margin:50px 0 46px"></div>
<div class="h" style="font-size:84px">COMENTA TU NÚMERO.<br><span class="red">VOLVER TAMBIÉN CUENTA.</span></div>
<div style="margin-top:46px">{ctablock()}</div>
</div>""", 5, 5, gx='85%', gy='15%')
print('ok')
