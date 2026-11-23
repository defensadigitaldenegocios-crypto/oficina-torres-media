# Genera las láminas HTML de BROSFIT (semana 2026-11-23)
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

