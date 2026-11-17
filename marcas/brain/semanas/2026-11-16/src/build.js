// BRAIN+ · semana 2026-11-16 · 3 carruseles 1080x1350
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const D = __dirname;
const F = p => 'file://' + path.join(D, p);
const FONT = 'file://' + path.join(D, 'node_modules/@fontsource');
const LEY = 'Producto para mayores de 18 años. No consumir más de 1 unidad al día. No recomendado para niños, mujeres embarazadas o en lactancia, ni personas sensibles a la cafeína. No mezclar con alcohol. Aviso COFEPRIS 2619025018B00067.';

const CSS = `
@font-face{font-family:'Titan One';src:url(${FONT}/titan-one/files/titan-one-latin-400-normal.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
@font-face{font-family:'Titan One';src:url(${FONT}/titan-one/files/titan-one-latin-ext-400-normal.woff2) format('woff2');unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;}
@font-face{font-family:'Rubik';font-weight:800;src:url(${FONT}/rubik/files/rubik-latin-800-normal.woff2) format('woff2');}
@font-face{font-family:'Rubik';font-weight:500;src:url(${FONT}/rubik/files/rubik-latin-500-normal.woff2) format('woff2');}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#111}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Rubik';font-weight:800;color:#fff}
.bg{position:absolute;inset:0;z-index:0}
.z{position:absolute;z-index:2}
.t{font-family:'Titan One';color:#fff;-webkit-text-stroke:12px #000;paint-order:stroke fill;text-shadow:9px 9px 0 #000;line-height:1.02;letter-spacing:1px}
.ty{color:#ffd400}.tp{color:#ff2d87}.tw{color:#fff}
.b{font-size:44px;line-height:1.2}
.chip{display:inline-block;background:#000;color:#ffd400;border-radius:60px;padding:14px 34px;font-size:40px;border:5px solid #fff}
.logo{position:absolute;z-index:3;width:150px;top:40px;right:44px;filter:drop-shadow(0 6px 10px rgba(0,0,0,.45))}
.foot{position:absolute;z-index:3;bottom:36px;left:56px;right:56px;display:flex;justify-content:space-between;font-size:30px;color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.6)}
.can{position:absolute;z-index:1;filter:drop-shadow(26px 34px 30px rgba(0,0,0,.6)) drop-shadow(0 0 40px rgba(255,255,255,.35))}
.shine{position:absolute;z-index:1;border-radius:50%;background:radial-gradient(circle,rgba(255,255,255,.95) 0,rgba(255,255,255,.35) 30%,rgba(255,255,255,0) 68%)}
.ley{position:absolute;z-index:3;left:56px;right:56px;bottom:84px;font-family:'Rubik';font-weight:500;font-size:22px;line-height:1.3;color:#fff;background:rgba(0,0,0,.72);padding:16px 22px;border-radius:16px}
.card{background:#fff;color:#000;border:7px solid #000;border-radius:34px;box-shadow:12px 12px 0 #000;padding:28px 34px}
.num{font-family:'Titan One';font-size:120px;color:#ffd400;-webkit-text-stroke:10px #000;paint-order:stroke fill;text-shadow:7px 7px 0 #000;line-height:1}
`;

// ---------- fondos psicodélicos ----------
const rays = (c1, c2, x = 50, y = 50, n = 10) =>
  `<div class="bg" style="background:repeating-conic-gradient(from 0deg at ${x}% ${y}%, ${c1} 0deg ${360 / n / 2}deg, ${c2} ${360 / n / 2}deg ${360 / n}deg)"></div>`;
const rings = (cs, x = 50, y = 50, w = 70) => {
  let stops = [], p = 0;
  cs.forEach(c => { stops.push(`${c} ${p}px ${p + w}px`); p += w; });
  return `<div class="bg" style="background:repeating-radial-gradient(circle at ${x}% ${y}%, ${stops.join(',')})"></div>`;
};
const halo = (x, y, r, c) => `<div class="bg" style="background:radial-gradient(circle at ${x}% ${y}%, ${c} 0, rgba(0,0,0,0) ${r}px)"></div>`;
const vignette = a => `<div class="bg" style="background:radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 40%, rgba(0,0,0,${a}) 100%)"></div>`;
// remolino SVG: espiral de bandas
const swirl = (cA, cB, cx = 540, cy = 675, turns = 5, bg = '#000') => {
  let paths = '';
  const arms = 8;
  for (let a = 0; a < arms; a++) {
    let d = '';
    for (let i = 0; i <= 220; i++) {
      const t = i / 220, ang = a * (2 * Math.PI / arms) + t * turns * Math.PI, r = 20 + t * 1200;
      d += (i ? 'L' : 'M') + (cx + r * Math.cos(ang)).toFixed(1) + ' ' + (cy + r * Math.sin(ang)).toFixed(1);
    }
    paths += `<path d="${d}" stroke="${a % 2 ? cA : cB}" stroke-width="${70}" fill="none" stroke-linecap="round"/>`;
  }
  return `<svg class="bg" width="1080" height="1350" viewBox="0 0 1080 1350"><rect width="1080" height="1350" fill="${bg}"/>${paths}</svg>`;
};

const can = (file, x, y, h, rot = 0) => {
  const ar = { 'lata-frente-creativity.png': 520 / 1368, 'lata-costado-formula.png': 510 / 1338, 'lata-trasera-nutrimental.png': 520 / 1368 }[file];
  const w = Math.round(h * ar);
  return `<div class="shine" style="left:${x - w * 0.6}px;top:${y + h * 0.1}px;width:${w * 2.2}px;height:${w * 2.2}px"></div>` +
    `<img class="can" src="${F(file)}" style="left:${x}px;top:${y}px;height:${h}px;width:${w}px;transform:rotate(${rot}deg)">`;
};
const logo = (pos = '') => `<img class="logo" src="${F('logo-tercer-ojo.png')}" style="${pos}">`;
const foot = (i, n, dark = false) => `<div class="foot" ${dark ? 'style="color:#000;text-shadow:none"' : ''}><span>@drinkbrainplus</span><span>${i}/${n}${i < n ? '  →' : ''}</span></div>`;
const ley = () => `<div class="ley">${LEY}</div>`;

// ================= A · Reto del tercer ojo (martes) =================
const A = [
  // A1 portada
  `${rays('#ff2d87', '#000', 50, 62, 16)}${halo(50, 62, 520, 'rgba(255,212,0,.85)')}${vignette(.55)}
   ${logo('left:50%;transform:translateX(-50%);width:170px;top:38px;right:auto')}
   <div class="z t" style="top:225px;left:40px;right:40px;text-align:center;font-size:118px">¿VES LO QUE<br><span class="ty">OTROS NO VEN?</span></div>
   ${can('lata-frente-creativity.png', 426, 510, 600, -6)}
   <div class="z" style="left:56px;bottom:120px"><span class="chip">El reto del tercer ojo</span></div>
   <div class="z" style="right:56px;bottom:120px"><span class="chip" style="background:#ff2d87;color:#fff">3 pasos →</span></div>
   ${foot(1, 5)}`,
  // A2 paso 1
  `${rings(['#ffd400', '#ff2d87', '#000', '#fff'], 72, 55, 64)}${vignette(.5)}${logo()}
   <div class="z" style="left:56px;top:70px"><div class="num">1</div></div>
   <div class="z t" style="left:56px;top:230px;width:600px;font-size:104px">ALINEA<br>LA LATA</div>
   <div class="z card b" style="left:56px;top:540px;width:500px">Ponla frente a tu cara, a la altura de tus ojos.</div>
   ${can('lata-frente-creativity.png', 650, 330, 900, 0)}
   ${foot(2, 5)}`,
  // A3 paso 2
  `${swirl('#ff2d87', '#ffd400', 300, 900, 4, '#000')}${vignette(.6)}${logo()}
   <div class="z" style="right:70px;top:230px"><div class="num">2</div></div>
   ${can('lata-costado-formula.png', 40, 260, 920, 8)}
   <div class="z t" style="right:56px;top:400px;width:620px;text-align:right;font-size:80px">ENFOCA TU<br><span class="tp">CREATIVIDAD</span></div>
   <div class="z card b" style="right:56px;top:700px;width:520px">Busca tu mejor ángulo. Luz, fondo y actitud: tú mandas.</div>
   ${foot(3, 5)}`,
  // A4 paso 3
  `${rays('#ffd400', '#fff', 50, 40, 22)}${halo(50, 40, 480, 'rgba(255,45,135,.75)')}${logo('left:56px;right:auto')}
   <div class="z" style="left:0;right:0;top:80px;text-align:center"><div class="num" style="color:#ff2d87">3</div></div>
   <div class="z t" style="left:40px;right:40px;top:230px;text-align:center;font-size:104px">MUÉSTRANOS<br><span class="ty">TU TERCER OJO</span></div>
   <div class="z card b" style="left:110px;right:110px;top:520px;text-align:center">Sube tu foto con la lata y etiqueta a <span style="color:#ff2d87">@drinkbrainplus</span></div>
   ${can('lata-frente-creativity.png', 445, 745, 500, 0)}
   ${foot(4, 5, true)}`,
  // A5 CTA
  `${swirl('#000', '#ff2d87', 540, 1350, 3, '#ffd400')}${vignette(.35)}${logo()}
   <div class="z t" style="left:56px;top:110px;width:980px;font-size:88px">¿QUIÉN DE TUS<br>AMIGOS<br><span class="ty">VE MÁS ALLÁ?</span></div>
   <div class="z card b" style="left:56px;top:480px;width:580px">Etiquétalos aquí abajo y rétalos a subir su foto.</div>
   <div class="z" style="left:56px;top:750px"><span class="chip" style="font-size:38px">drinkbrainplus.com/tienda</span></div>
   ${can('lata-costado-formula.png', 690, 430, 690, -8)}
   ${ley()}${foot(5, 5)}`,
];

// ================= B · Para negocios (jueves) =================
const B = [
  `${rings(['#ffd400', '#ffd400', '#000'], 50, 108, 58)}${halo(50, 100, 700, 'rgba(255,45,135,.9)')}${logo('left:56px;right:auto')}
   <div class="z" style="right:56px;top:70px"><span class="chip">Para dueños de negocio</span></div>
   <div class="z t" style="left:50px;right:50px;top:230px;font-size:112px">¿TIENES GYM,<br>BARBERÍA, CAFÉ<br><span class="tp">U OFICINA?</span></div>
   <div class="z card b" style="left:56px;top:700px;width:600px;font-size:48px">Esto es para ti<br>y para tus clientes.</div>
   ${can('lata-frente-creativity.png', 700, 560, 630, 7)}
   ${foot(1, 5)}`,
  `${rays('#000', '#1a1a1a', 50, 50, 24)}${halo(30, 70, 600, 'rgba(255,45,135,.65)')}${halo(85, 20, 420, 'rgba(255,212,0,.5)')}${logo()}
   <div class="z t" style="left:56px;top:150px;width:800px;font-size:100px">¿QUÉ ES UN<br><span class="ty">SMART POINT?</span></div>
   <div class="z card b" style="left:56px;top:470px;width:560px;font-size:48px">Un punto BRAIN+ dentro de tu negocio.</div>
   <div class="z card b" style="left:56px;top:740px;width:560px;font-size:48px;background:#ffd400">Tus clientes pagan con QR desde su celular.</div>
   ${can('lata-costado-formula.png', 700, 380, 820, -5)}
   ${foot(2, 5)}`,
  `${swirl('#ff2d87', '#fff', 1080, 0, 3, '#ffd400')}${vignette(.3)}${logo('left:56px;right:auto')}
   <div class="z t" style="left:56px;right:56px;top:230px;font-size:92px">YA HAY SMART<br>POINTS EN:</div>
   <div class="z" style="left:56px;right:56px;top:480px;display:flex;flex-direction:column;gap:22px">
     <div class="card b" style="font-size:44px">BROSFIT GYM <span style="color:#ff2d87">· Escobedo</span></div>
     <div class="card b" style="font-size:44px">Protein Shop Valle <span style="color:#ff2d87">· Del Valle</span></div>
     <div class="card b" style="font-size:44px">Hybrid GYM <span style="color:#ff2d87">· San Jerónimo</span></div>
     <div class="card b" style="font-size:44px">Ludivina Lugo <span style="color:#ff2d87">· Centro de MTY</span></div>
   </div>
   ${foot(3, 5, true)}`,
  `${rays('#ff2d87', '#ffd400', 50, 70, 14)}${halo(50, 70, 520, 'rgba(255,255,255,.9)')}${vignette(.4)}${logo()}
   <div class="z t" style="left:40px;right:40px;top:170px;text-align:center;font-size:150px">¿EL QUE<br>SIGUE?</div>
   ${can('lata-frente-creativity.png', 430, 520, 580, 0)}
   <div class="z t" style="left:40px;right:40px;top:1120px;text-align:center;font-size:104px"><span class="ty">EL TUYO.</span></div>
   ${foot(4, 5)}`,
  `${rings(['#000', '#111', '#ff2d87', '#111'], 0, 100, 60)}${vignette(.4)}${logo()}
   <div class="z t" style="left:56px;top:150px;width:800px;font-size:96px">PIDE TU<br><span class="ty">SMART POINT</span></div>
   <div class="z b" style="left:56px;top:420px;width:620px;font-size:46px">Escríbenos por WhatsApp:</div>
   <div class="z card" style="left:56px;top:510px;font-family:'Titan One';font-size:84px;background:#ffd400">81 2909 0049</div>
   <div class="z b" style="left:56px;top:720px;width:560px;font-size:42px">¿Conoces a un dueño de gym, barbería o café? Mándale este post.</div>
   ${can('lata-costado-formula.png', 730, 470, 640, -6)}
   ${ley()}${foot(5, 5)}`,
];

// ================= C · Tu momento BRAIN+ (sábado) =================
const opt = (L, txt, bg) => `<div class="card" style="display:flex;align-items:center;gap:30px;background:${bg}"><span class="num" style="font-size:110px;color:#ff2d87">${L}</span><span class="b" style="font-size:50px">${txt}</span></div>`;
const C = [
  `${swirl('#ffd400', '#000', 540, 760, 5, '#ff2d87')}${vignette(.5)}${logo('left:50%;transform:translateX(-50%);right:auto;width:160px;top:36px')}
   <div class="z t" style="left:40px;right:40px;top:215px;text-align:center;font-size:120px">¿CUÁL ES TU<br><span class="ty">MOMENTO</span><br>BRAIN+?</div>
   ${can('lata-frente-creativity.png', 420, 690, 560, -4)}
   <div class="z" style="left:0;right:0;bottom:110px;text-align:center"><span class="chip" style="font-size:44px">Elige A, B, C o D y coméntala</span></div>
   ${foot(1, 5)}`,
  `${rays('#ffd400', '#ffe766', 0, 100, 18)}${halo(0, 100, 700, 'rgba(255,45,135,.55)')}${logo()}
   <div class="z t" style="left:56px;top:110px;font-size:96px">¿A O B?</div>
   <div class="z" style="left:56px;top:330px;width:620px;display:flex;flex-direction:column;gap:46px">
     ${opt('A', 'El proyecto creativo de medianoche', '#fff')}
     ${opt('B', 'Antes de entrar al gym', '#fff')}
   </div>
   ${can('lata-costado-formula.png', 720, 330, 860, 6)}
   ${foot(2, 5, true)}`,
  `${rings(['#000', '#ff2d87', '#000', '#ffd400'], 100, 30, 56)}${vignette(.5)}${logo('left:56px;right:auto')}
   <div class="z t" style="right:56px;top:110px;font-size:96px;text-align:right">¿C O D?</div>
   ${can('lata-frente-creativity.png', 60, 330, 860, -6)}
   <div class="z" style="right:56px;top:330px;width:600px;display:flex;flex-direction:column;gap:46px">
     ${opt('C', 'La sesión de estudio del domingo', '#fff')}
     ${opt('D', 'La lluvia de ideas en la oficina', '#ffd400')}
   </div>
   ${foot(3, 5)}`,
  `${rays('#000', '#141414', 70, 50, 20)}${halo(70, 50, 560, 'rgba(255,212,0,.55)')}${logo()}
   <div class="z t" style="left:56px;top:110px;width:760px;font-size:84px">LA QUE TE<br>ACOMPAÑA <span class="tp">TRAE:</span></div>
   <div class="z" style="left:56px;top:400px;width:620px;display:flex;flex-direction:column;gap:18px">
     <div class="card b" style="font-size:42px">8 ingredientes activos</div>
     <div class="card b" style="font-size:42px;background:#ffd400">0 g de azúcares añadidos</div>
     <div class="card b" style="font-size:42px">200 mg de cafeína por lata</div>
     <div class="card b" style="font-size:42px;background:#ff2d87;color:#fff">Uva + té verde</div>
     <div class="card b" style="font-size:42px">Hecha en Monterrey, N.L.</div>
   </div>
   ${can('lata-trasera-nutrimental.png', 700, 400, 820, 0)}
   ${foot(4, 5)}`,
  `${swirl('#ff2d87', '#ffd400', 540, 1350, 4, '#000')}${vignette(.45)}${logo()}
   <div class="z t" style="left:56px;top:110px;width:780px;font-size:100px">ENERGÍA PARA<br><span class="ty">LA MENTE</span></div>
   <div class="z card b" style="left:56px;top:400px;width:580px">Pídela en paquetes de 6, 12 o 24 latas.</div>
   <div class="z" style="left:56px;top:640px"><span class="chip" style="font-size:40px">drinkbrainplus.com/tienda</span></div>
   <div class="z card b" style="left:56px;top:760px;width:580px;font-size:42px;background:#ffd400">O búscala en tu Smart Point.</div>
   ${can('lata-frente-creativity.png', 720, 380, 720, 5)}
   ${ley()}${foot(5, 5)}`,
];

(async () => {
  const sets = { A, B, C };
  fs.mkdirSync(path.join(D, 'out'), { recursive: true });
  fs.mkdirSync(path.join(D, 'src'), { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const [k, slides] of Object.entries(sets)) {
    const html = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${slides.map((s, i) => `<div class="slide" id="s${i + 1}">${s}</div>`).join('')}</body></html>`;
    const f = path.join(D, 'src', `${k}.html`);
    fs.writeFileSync(f, html);
    await page.goto('file://' + f);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    for (let i = 1; i <= slides.length; i++) {
      await page.locator('#s' + i).screenshot({ path: path.join(D, 'out', `${k}${i}.jpg`), type: 'jpeg', quality: 90 });
    }
  }
  await browser.close();
  console.log('ok');
})();
