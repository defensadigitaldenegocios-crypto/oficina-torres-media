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

// ---------- fondos nuevos semana 2026-11-23 ----------
const stripes = (c1, c2, ang = 45, w = 60) => `<div class="bg" style="background:repeating-linear-gradient(${ang}deg, ${c1} 0 ${w}px, ${c2} ${w}px ${w * 2}px)"></div>`;
// silueta tipo Cerro de la Silla
const cerro = (fill = '#000', y = 1100, op = 1) => `<svg class="bg" style="z-index:1;opacity:${op}" width="1080" height="1350" viewBox="0 0 1080 1350"><path d="M0 ${y + 120} L120 ${y + 60} L230 ${y - 40} L300 ${y - 150} L360 ${y - 60} L430 ${y - 20} L520 ${y - 10} L600 ${y - 40} L680 ${y - 120} L740 ${y - 260} L800 ${y - 140} L880 ${y - 50} L980 ${y + 20} L1080 ${y + 70} L1080 1350 L0 1350Z" fill="${fill}"/></svg>`;
const grid = (line = '#ff2d87', bg = '#000') => {
  let l = '';
  for (let i = -12; i <= 12; i++) l += `<line x1="540" y1="560" x2="${540 + i * 180}" y2="1350" stroke="${line}" stroke-width="5"/>`;
  for (let k = 0; k < 9; k++) { const y = 560 + Math.pow(k / 8, 1.9) * 790; l += `<line x1="0" y1="${y}" x2="1080" y2="${y}" stroke="${line}" stroke-width="5"/>`; }
  return `<svg class="bg" width="1080" height="1350" viewBox="0 0 1080 1350"><rect width="1080" height="1350" fill="${bg}"/>${l}</svg>`;
};
const waves = (cs, amp = 40, band = 70, bg = '#ffd400') => {
  let p = '';
  for (let j = -2, k = 0; j * band < 1500; j++, k++) {
    let d = '';
    for (let x = 0; x <= 1080; x += 20) d += (x ? 'L' : 'M') + x + ' ' + (j * band + amp * Math.sin(x / 90 + j * 0.5)).toFixed(1);
    p += `<path d="${d}" stroke="${cs[k % cs.length]}" stroke-width="${band * 0.55}" fill="none"/>`;
  }
  return `<svg class="bg" width="1080" height="1350" viewBox="0 0 1080 1350"><rect width="1080" height="1350" fill="${bg}"/>${p}</svg>`;
};
const pin = (txt, c = '#ff2d87') => `<span style="display:inline-flex;align-items:center;justify-content:center;width:96px;height:96px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:${c};border:6px solid #000;box-shadow:6px 6px 0 #000"><span style="transform:rotate(45deg);font-family:'Titan One';font-size:48px;color:#fff;-webkit-text-stroke:6px #000;paint-order:stroke fill">${txt}</span></span>`;
const item = (t, sub, n, c) => `<div class="card" style="display:flex;gap:30px;align-items:center;margin-bottom:34px">${pin(n, c)}<div><div style="font-size:50px;line-height:1.05">${t}</div><div style="font-size:40px;font-weight:500;font-family:Rubik;margin-top:8px">${sub}</div></div></div>`;

// ================= A · Hecha en Monterrey (martes 24) =================
const A = [
  `${stripes('#ff2d87', '#ffd400', 135, 70)}${halo(62, 58, 520, 'rgba(255,255,255,.75)')}${cerro('#000', 1180)}${vignette(.35)}${logo()}
   <div class="z t" style="top:150px;left:50px;font-size:112px">ESTA LATA ES<br><span class="tp">MÁS REGIA</span><br>DE LO QUE<br>CREES</div>
   ${can('lata-frente-creativity.png', 640, 470, 720, 7)}
   <div class="z" style="left:56px;top:880px"><span class="chip">Desliza y compruébalo →</span></div>
   ${foot(1, 5)}`,
  `${rays('#ff2d87', '#000', 30, 75, 18)}${halo(30, 75, 480, 'rgba(255,212,0,.8)')}${cerro('#000', 1220)}${vignette(.5)}${logo()}
   <div class="z t" style="top:140px;left:56px;font-size:104px">NACIÓ EN<br><span class="ty">MONTERREY</span></div>
   <div class="z card b" style="top:420px;right:56px;width:560px">Hecha en Monterrey, Nuevo León. Sí, aquí mismito. ¡Puro talento regio!</div>
   ${can('lata-costado-formula.png', 110, 470, 700, -5)}
   ${foot(2, 5)}`,
  `${rings(['#ffd400', '#ff2d87', '#000'], 70, 60, 64)}${halo(70, 60, 420, 'rgba(255,255,255,.85)')}${vignette(.4)}${logo()}
   <div class="z t" style="top:130px;left:56px;font-size:100px">UVA +<br><span style="color:#7ddc3a">TÉ VERDE</span></div>
   <div class="z card" style="top:430px;left:56px;width:470px;text-align:center"><div class="num" style="font-size:150px">0 g</div><div class="b" style="margin-top:8px">de azúcares añadidos</div></div>
   <div class="z" style="left:56px;top:900px"><span class="chip">Lata de 355 mL</span></div>
   ${can('lata-frente-creativity.png', 640, 400, 760, 4)}
   ${foot(3, 5)}`,
  `${swirl('#ff2d87', '#7ddc3a', 900, 1200, 5, '#000')}${vignette(.55)}${logo()}
   <div class="z t" style="top:110px;left:56px;font-size:96px">8 ACTIVOS<br><span class="ty">EN UNA LATA</span></div>
   <div class="z" style="top:400px;left:56px;width:600px;display:flex;flex-direction:column;gap:16px">
     ${['Alpha-GPC', 'Taurina', 'L-teanina', 'Ashwagandha', 'Electrolitos', 'Complejo B', 'Cafeína · 200 mg', 'Extracto de té verde'].map((x, i) => `<div style="background:${i % 2 ? '#ffd400' : '#fff'};color:#000;border:5px solid #000;border-radius:40px;box-shadow:7px 7px 0 #000;padding:8px 28px;font-size:42px">${x}</div>`).join('')}
   </div>
   ${can('lata-trasera-nutrimental.png', 690, 420, 760, 0)}
   ${foot(4, 5)}`,
  `${stripes('#ffd400', '#ff2d87', 45, 70)}${halo(70, 45, 520, 'rgba(255,255,255,.8)')}${vignette(.35)}${logo()}
   <div class="z t" style="top:120px;left:56px;font-size:96px">ENERGÍA PARA<br><span class="tp">LA MENTE</span></div>
   <div class="z card b" style="top:390px;left:56px;width:560px;background:#000;color:#fff;border-color:#fff">¡Etiqueta al más regio que conozcas!</div>
   <div class="z" style="left:56px;top:640px"><span class="chip">drinkbrainplus.com/tienda</span></div>
   <div class="z card b" style="left:56px;top:760px;width:560px;font-size:42px">O búscala en tu Smart Point.</div>
   ${can('lata-frente-creativity.png', 700, 330, 700, 5)}
   ${ley()}${foot(5, 5)}`,
];

// ================= B · Rincón vacío / negocios (jueves 26) =================
const B = [
  `${grid('#ff2d87', '#000')}${halo(50, 42, 560, 'rgba(255,212,0,.9)')}${vignette(.5)}${logo()}
   <div class="z t" style="top:130px;left:50px;right:50px;font-size:108px">ESE RINCÓN<br><span class="ty">VACÍO</span> DE TU<br>NEGOCIO...</div>
   ${can('lata-frente-creativity.png', 590, 560, 640, -4)}
   <div class="z card b" style="left:56px;top:720px;width:470px;background:#ffd400">...ya tiene otro plan. Desliza →</div>
   <div class="z" style="left:56px;bottom:110px"><span class="chip" style="font-size:36px">Gyms · barberías · cafés · oficinas</span></div>
   ${foot(1, 5)}`,
  `${rays('#ffd400', '#ff2d87', 70, 55, 14)}${halo(70, 55, 450, 'rgba(255,255,255,.85)')}${vignette(.4)}${logo()}
   <div class="z t" style="top:130px;left:56px;font-size:104px">PONLE UN<br><span class="tp">SMART</span><br><span class="tp">POINT</span></div>
   <div class="z card b" style="top:620px;left:56px;width:520px">Un punto BRAIN+ dentro de tu gym, barbería, café u oficina.</div>
   ${can('lata-frente-creativity.png', 640, 420, 760, 5)}
   ${foot(2, 5)}`,
  `${waves(['#000', '#ff2d87'], 36, 90, '#ffd400')}${vignette(.35)}${logo()}
   <div class="z t" style="top:110px;left:56px;font-size:90px">¿CÓMO PAGAN<br><span class="tp">TUS CLIENTES?</span></div>
   <div class="z" style="top:400px;left:56px;width:600px">
     ${[['1', 'Escanean el QR'], ['2', 'Pagan desde su celular'], ['3', '¡Listo! Su BRAIN+']].map(([n, t]) => `<div class="card" style="display:flex;align-items:center;gap:26px;margin-bottom:30px"><span class="num" style="font-size:96px">${n}</span><span style="font-size:48px;line-height:1.1">${t}</span></div>`).join('')}
   </div>
   ${can('lata-costado-formula.png', 700, 420, 760, 3)}
   ${foot(3, 5)}`,
  `${swirl('#ff2d87', '#ffd400', 1080, 0, 4, '#000')}${vignette(.6)}${logo()}
   <div class="z t" style="top:120px;left:56px;font-size:92px">YA HAY<br><span class="ty">SMART POINTS</span><br>EN...</div>
   <div class="z" style="top:470px;left:56px;width:620px;display:flex;flex-direction:column;gap:20px">
     ${['BROSFIT GYM · Escobedo', 'Protein Shop Valle · Del Valle', 'Hybrid GYM · San Jerónimo', 'Ludivina Lugo · centro de MTY'].map((x, i) => `<div style="background:${i % 2 ? '#ffd400' : '#fff'};color:#000;border:5px solid #000;border-radius:40px;box-shadow:7px 7px 0 #000;padding:14px 28px;font-size:40px">${x}</div>`).join('')}
   </div>
   <div class="z t" style="top:1000px;left:56px;font-size:70px">¿EL TUYO <span class="tp">SIGUE?</span></div>
   ${can('lata-frente-creativity.png', 730, 440, 680, 4)}
   ${foot(4, 5)}`,
  `${grid('#ffd400', '#ff2d87')}${halo(50, 40, 520, 'rgba(255,255,255,.8)')}${vignette(.35)}${logo()}
   <div class="z t" style="top:110px;left:56px;font-size:92px">ESCRÍBENOS<br><span class="ty">POR WHATSAPP</span></div>
   <div class="z" style="left:56px;top:350px"><span class="chip" style="font-size:58px;padding:18px 40px">81 2909 0049</span></div>
   <div class="z card b" style="left:56px;top:520px;width:580px">Comenta qué negocio de tu colonia debería tener uno.</div>
   ${can('lata-frente-creativity.png', 700, 370, 680, 6)}
   ${ley()}${foot(5, 5)}`,
];

// ================= C · Guarda este mapa (sábado 28) =================
const C = [
  `${waves(['#ff2d87', '#000', '#ffd400', '#fff'], 46, 80, '#ffd400')}${halo(50, 55, 520, 'rgba(255,255,255,.8)')}${vignette(.35)}${logo()}
   <div class="z t" style="top:120px;left:56px;font-size:118px">GUARDA<br>ESTE <span class="tp">MAPA</span></div>
   <div class="z card" style="top:470px;left:56px;width:520px;height:440px;background:#fff;overflow:hidden;padding:0">
     <svg width="520" height="440" viewBox="0 0 520 440" style="position:absolute;inset:0"><path d="M-10 300 Q140 220 260 260 T540 180" stroke="#ffd400" stroke-width="34" fill="none"/><path d="M120 -10 Q160 200 90 450" stroke="#ff2d87" stroke-width="22" fill="none"/><path d="M-10 120 L540 90" stroke="#000" stroke-width="12" fill="none" stroke-dasharray="26 18"/></svg>
     <div style="position:absolute;left:40px;top:40px">${pin('1')}</div><div style="position:absolute;left:330px;top:60px">${pin('2', '#ffd400')}</div><div style="position:absolute;left:200px;top:180px">${pin('3', '#7ddc3a')}</div><div style="position:absolute;left:360px;top:290px">${pin('4', '#000')}</div>
   </div>
   ${can('lata-frente-creativity.png', 640, 480, 700, 6)}
   <div class="z" style="left:56px;bottom:110px"><span class="chip" style="font-size:38px">¿Dónde hay BRAIN+ en Monterrey?</span></div>
   ${foot(1, 5)}`,
  `${rays('#000', '#ff2d87', 85, 80, 16)}${halo(85, 80, 460, 'rgba(255,212,0,.85)')}${vignette(.45)}${logo()}
   <div class="z t" style="top:120px;left:56px;font-size:100px">PARA LOS<br><span class="ty">DEL GYM</span></div>
   <div class="z" style="top:430px;left:56px;width:640px">
     ${item('BROSFIT GYM', 'Escobedo', '1', '#ff2d87')}
     ${item('Hybrid GYM', 'San Jerónimo', '2', '#ffd400')}
   </div>
   ${can('lata-costado-formula.png', 720, 560, 700, 4)}
   ${foot(2, 5)}`,
  `${rings(['#ff2d87', '#ffd400', '#fff'], 20, 85, 66)}${halo(20, 85, 380, 'rgba(255,255,255,.7)')}${vignette(.45)}${logo()}
   <div class="z t" style="top:120px;left:56px;font-size:100px">EN EL VALLE<br><span class="ty">Y EN EL CENTRO</span></div>
   <div class="z" style="top:430px;left:56px;width:660px">
     ${item('Protein Shop Valle', 'Plaza Los Ríos, Del Valle', '3', '#7ddc3a')}
     ${item('Ludivina Lugo', 'Centro de Monterrey', '4', '#000')}
   </div>
   ${can('lata-frente-creativity.png', 740, 560, 680, 5)}
   ${foot(3, 5)}`,
  `${grid('#ff2d87', '#000')}${halo(50, 45, 500, 'rgba(255,45,135,.85)')}${vignette(.5)}${logo()}
   <div class="z t" style="top:110px;left:56px;font-size:96px">¿NINGUNO TE<br><span class="ty">QUEDA CERCA?</span></div>
   <div class="z card b" style="top:420px;left:56px;width:560px">Pídela en línea en paquetes de 6, 12 o 24 latas.</div>
   <div class="z" style="left:56px;top:680px"><span class="chip">drinkbrainplus.com/tienda</span></div>
   ${can('lata-frente-creativity.png', 690, 430, 740, 4)}
   ${foot(4, 5)}`,
  `${swirl('#ffd400', '#ff2d87', 540, 1350, 4, '#000')}${vignette(.45)}${logo()}
   <div class="z t" style="top:110px;left:56px;font-size:86px">¿CUÁL TE QUEDA<br><span class="ty">MÁS CERCA?</span></div>
   <div class="z card b" style="top:390px;left:56px;width:580px">Comenta el número: 1, 2, 3 o 4.</div>
   <div class="z card b" style="top:580px;left:56px;width:580px;background:#ffd400">En el Smart Point pagas con QR desde tu celular.</div>
   ${can('lata-frente-creativity.png', 710, 360, 690, 5)}
   ${ley()}${foot(5, 5)}`,
];
(async () => {
  const sets = { A, B, C };
  fs.mkdirSync(path.join(D, 'out'), { recursive: true });
  fs.mkdirSync(path.join(D, 'src'), { recursive: true });
  const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
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
