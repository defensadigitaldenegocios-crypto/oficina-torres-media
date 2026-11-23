exec(open('/home/claude/redes-brosfit/base.py').read())
INK='#151515'; BONE='#f1ece2'

# ---------- A · Elige tu personaje de diciembre ----------
def ico(kind, s=150):
    if kind=='pinata':
        pts=[];import math
        for i in range(10):
            r=70 if i%2==0 else 34; a=math.pi/2+i*math.pi/5
            pts.append(f"{75+r*math.cos(a):.1f},{80-r*math.sin(a):.1f}")
        return f'<svg width="{s}" height="{s}" viewBox="0 0 150 150"><path d="M75 4v8" stroke="#bdb6aa" stroke-width="4"/><polygon points="{" ".join(pts)}" fill="{RED}" stroke="{BONE}" stroke-width="5" stroke-linejoin="round"/><circle cx="75" cy="80" r="16" fill="{BONE}"/></svg>'
    if kind=='cal':
        return f'<svg width="{s}" height="{s}" viewBox="0 0 150 150"><rect x="14" y="26" width="122" height="112" rx="16" fill="{BONE}"/><rect x="14" y="26" width="122" height="34" rx="16" fill="{RED}"/><rect x="14" y="44" width="122" height="16" fill="{RED}"/><rect x="40" y="12" width="12" height="30" rx="6" fill="#bdb6aa"/><rect x="98" y="12" width="12" height="30" rx="6" fill="#bdb6aa"/><text x="75" y="126" text-anchor="middle" font-family="Anton" font-size="64" fill="{INK}">1</text></svg>'
    if kind=='ghost':
        return f'<svg width="{s}" height="{s}" viewBox="0 0 150 150"><path d="M25 140V70a50 50 0 0 1 100 0v70l-17-14-16 14-17-14-16 14-17-14z" fill="{BONE}" opacity=".9"/><ellipse cx="58" cy="72" rx="9" ry="13" fill="{INK}"/><ellipse cx="92" cy="72" rx="9" ry="13" fill="{INK}"/></svg>'
    if kind=='star':
        return f'<svg width="{s}" height="{s}" viewBox="0 0 150 150"><circle cx="75" cy="75" r="72" fill="{RED}"/><path d="M48 36h54v22a27 27 0 0 1-54 0z" fill="{BONE}"/><path d="M48 44H34v8a16 16 0 0 0 16 16M102 44h14v8a16 16 0 0 1-16 16" stroke="{BONE}" stroke-width="7" fill="none"/><rect x="69" y="84" width="12" height="18" fill="{BONE}"/><rect x="52" y="102" width="46" height="14" rx="4" fill="{BONE}"/></svg>'

def bar(lbl, v, hot=False):
    return f"""<div style="display:flex;align-items:center;gap:22px;margin-top:20px">
<div style="width:250px;font-size:40px;letter-spacing:2px">{lbl}</div>
<div style="flex:1;height:34px;background:#2c2c2c;border-radius:8px;overflow:hidden;border:2px solid #3a3a3a"><div style="width:{v}%;height:100%;background:{RED if hot else '#bdb6aa'};background-image:repeating-linear-gradient(90deg,transparent 0 46px,rgba(0,0,0,.35) 46px 50px)"></div></div>
<div class="h" style="width:96px;text-align:right;font-size:46px">{v}</div></div>"""

def ficha(num, nombre, ic, desc, stats, hab, n, gx='80%', gy='25%', win=False):
    page('A%d'%n, f"""<div class="wrap">
<div style="display:flex;align-items:center;gap:20px"><div class="pill" style="{'background:'+RED+';color:#fff' if win else ''}">JUGADOR {num} / 4</div><div class="kick" style="font-size:30px">{'Desbloqueado' if win else 'Modo diciembre'}</div></div>
<div class="card" style="margin-top:30px;{'border-color:'+RED+';border-width:4px' if win else ''}">
 <div style="display:flex;align-items:center;gap:36px">{ico(ic)}<div class="h" style="font-size:{92 if len(nombre)<16 else 76}px">{nombre}</div></div>
 <div class="body" style="margin-top:30px;font-size:50px;color:#e6dfd3">{desc}</div>
 <div style="margin-top:18px">{''.join(bar(a,b,h) for a,b,h in stats)}</div>
</div>
<div style="margin-top:34px;display:flex;gap:24px;align-items:baseline"><div class="kick" style="white-space:nowrap">Habilidad especial</div></div>
<div class="h" style="margin-top:14px;font-size:84px">{hab}</div>
</div>""", n, 5, gx=gx, gy=gy)

def lock(i):
    return f'<div style="flex:1;height:200px;border-radius:22px;background:#222;border:3px solid {"#d6453d" if i==4 else "#3a3a3a"};display:flex;align-items:center;justify-content:center;flex-direction:column"><div class="h" style="font-size:96px;color:{"#d6453d" if i==4 else "#6f6a62"}">{i}</div><div style="font-size:28px;letter-spacing:3px;color:#8d877d">???</div></div>'

page('A1', f"""<div class="wrap">
<div class="kick">Modo diciembre · Selecciona jugador</div>
<div class="h" style="font-size:176px;margin-top:24px">ELIGE TU<br><span class="red">PERSONAJE</span></div>
<div class="body" style="margin-top:34px;max-width:880px;font-size:52px">Cuatro personajes aparecen en diciembre. Solo uno <span class="hl">llega a enero.</span></div>
<div style="display:flex;gap:20px;margin-top:56px">{''.join(lock(i) for i in range(1,5))}</div>
<div style="margin-top:34px;font-size:40px;color:#bdb6aa">Desliza y comenta tu número →</div>
</div>""", 1, 5, gx='85%', gy='18%')

ficha(1,'EL POSADERO','pinata','Entrena cargando la mesa del intercambio.',[('EXCUSAS',99,True),('CONSTANCIA',12,False)],'Desaparece del 12 de diciembre al 6 de enero.',2,gy='60%')
ficha(2,'EL «EN ENERO SÍ»','cal','Ya compró tenis nuevos. Para estrenarlos en enero.',[('PLANES',100,True),('CONSTANCIA',8,False)],'Empezar el lunes. Todos los lunes.',3,gx='20%',gy='55%')
ficha(3,'EL FANTASMA','ghost','Va un día, se toma la foto y no lo vuelves a ver.',[('FOTOS',95,True),('CONSTANCIA',20,False)],'Invisible de martes a domingo.',4,gy='65%')

page('A5', f"""<div class="wrap">
<div style="display:flex;align-items:center;gap:20px"><div class="pill" style="background:{RED};color:#fff">JUGADOR 4 / 4</div><div class="kick" style="font-size:30px">Desbloqueado</div></div>
<div class="card" style="margin-top:26px;border:4px solid {RED};padding:36px 44px">
 <div style="display:flex;align-items:center;gap:30px">{ico('star',130)}<div class="h" style="font-size:72px">EL QUE LLEGA A<br><span class="red">ENERO ENTRENANDO</span></div></div>
 <div style="margin-top:6px">{bar('CONSTANCIA',100,True)}{bar('EXCUSAS',5,False)}</div>
 <div class="body" style="margin-top:22px;font-size:44px;color:#e6dfd3">No es el más fuerte. Es el que no se fue.</div>
</div>
<div class="h" style="font-size:64px;margin:36px 0 28px">¿CUÁL ERES? <span class="red">COMENTA 1, 2, 3 O 4</span></div>
<div class="cta" style="align-self:flex-start">{WA}<div><small>Para elegir al 4, escríbenos</small>81 2909 0049</div></div>
<div style="font-size:40px;color:#e6dfd3;margin-top:22px">o mándanos DM aquí en <span class="red" style="font-weight:800">@brosfitgym</span></div>
</div>""", 5, 5, gx='85%', gy='15%')

# ---------- B · Mensaje de tu yo de enero ----------
AV = f'<div style="width:96px;height:96px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;flex:none"><span class="h" style="font-size:44px;color:#fff">TÚ</span></div>'
def chathead(sub='en línea'):
    return f"""<div style="display:flex;align-items:center;gap:24px;padding-bottom:26px;border-bottom:2px solid #333">{AV}
<div><div style="font-size:46px;font-weight:800">Tú (1 de enero)</div><div style="font-size:32px;color:#8fd19e">{sub}</div></div>
<div style="margin-left:auto;font-size:32px;color:#8d877d;letter-spacing:2px">1 ENE 2027</div></div>"""
def bub(t, big=False, red=False):
    return f'<div style="align-self:flex-start;max-width:820px;margin-top:26px;background:{RED if red else "#2a2a2a"};color:{"#fff" if red else BONE};border-radius:8px 34px 34px 34px;padding:28px 38px;font-size:{68 if big else 56}px;line-height:1.15;font-weight:{800 if big else 700}">{t}</div>'
def mine(t):
    return f'<div style="align-self:flex-end;max-width:700px;margin-top:26px;background:{BONE};color:{INK};border-radius:34px 8px 34px 34px;padding:24px 36px;font-size:46px;font-weight:800">{t}</div>'
TYP='<div style="align-self:flex-start;margin-top:26px;background:#2a2a2a;border-radius:34px;padding:26px 34px;display:flex;gap:14px">'+''.join('<span style="width:22px;height:22px;border-radius:50%;background:#8d877d;display:inline-block"></span>' for _ in range(3))+'</div>'
def chat(n, bubbles, sub='en línea', gy='40%'):
    page('B%d'%n, f'<div class="wrap" style="justify-content:flex-start;top:110px">{chathead(sub)}<div style="display:flex;flex-direction:column;margin-top:14px">{bubbles}{TYP}</div></div>', n, 5, gx='15%', gy=gy)

page('B1', f"""<div class="wrap" style="align-items:center;text-align:center">
<div style="font-size:40px;letter-spacing:6px;color:#bdb6aa">VIERNES 1 DE ENERO</div>
<div class="h" style="font-size:250px;line-height:1;margin-top:6px">00:01</div>
<div class="card" style="margin-top:50px;text-align:left;width:100%;background:rgba(40,40,40,.92);padding:34px 40px">
 <div style="display:flex;align-items:center;gap:22px">{AV}<div style="font-size:42px;font-weight:800">Tú (1 de enero)</div><div style="margin-left:auto;font-size:32px;color:#8d877d">ahora</div></div>
 <div style="font-size:50px;margin-top:22px;line-height:1.15">Oye, ¿tienes un minuto? Es sobre diciembre…</div>
</div>
<div class="h" style="font-size:84px;margin-top:60px">TIENES 1 MENSAJE DE<br><span class="red">TU YO DEL FUTURO</span></div>
</div>""", 1, 5, gx='50%', gy='35%')
chat(2, bub('Te escribo desde el 1 de enero.')+bub('Todos están haciendo propósitos.')+bub('Yo no. <b style="color:#d6453d">Yo ya vengo entrenando.</b>', big=True), sub='escribiendo…')
chat(3, mine('¿Cómo?? 😳'.replace(' 😳',''))+bub('Porque no esperaste a enero.')+bub('Ni al lunes. Ni a la quincena.')+bub('Empezaste en noviembre. <br>Esa semana.', big=True, red=True), gy='70%')
chat(4, bub('Las posadas sí fueron.')+bub('Los tamales también.')+bub('Pero no soltaste el hábito: 2 o 3 días a la semana, <b style="color:#d6453d">aunque fuera poquito.</b>', big=True), gy='55%')
page('B5', f"""<div class="wrap">
<div class="card" style="padding:34px 40px"><div style="font-size:50px;line-height:1.15">Gracias por no dejármelo todo a mí.</div><div style="font-size:42px;color:#bdb6aa;margin-top:16px">— Atte: tú, el 1 de enero</div></div>
<div class="h" style="font-size:112px;margin:46px 0 22px">CONTÉSTALE<br><span class="red">HOY.</span></div>
<div class="body" style="margin-bottom:40px;font-size:46px">Mándaselo al compa que dice «en enero sí».</div>
{ctablock()}</div>""", 5, 5, gx='85%', gy='15%')

# ---------- C · Mito o verdad, edición diciembre ----------
def stamp(word, rot=-8, ok=False):
    c = '#8fd19e' if ok else RED
    return f'<div style="display:inline-block;transform:rotate({rot}deg);border:10px solid {c};color:{c};border-radius:18px;padding:6px 36px;font-family:Anton;font-size:140px;line-height:1.05;letter-spacing:4px">{word}</div>'
def mv(n, frase, word, ok, exp, gx, gy):
    page('C%d'%n, f"""<div class="wrap">
<div class="pill" style="align-self:flex-start">FRASE {n-1} DE 3</div>
<div class="h" style="font-size:{104 if len(frase)<40 else 92}px;margin-top:30px">«{frase}»</div>
<div style="margin:56px 0 50px">{stamp(word, -6 if ok else -8, ok)}</div>
<div class="card"><div class="body" style="font-size:50px">{exp}</div></div>
</div>""", n, 5, gx=gx, gy=gy)

page('C1', f"""<div class="wrap">
<div class="kick">Edición diciembre</div>
<div class="h" style="font-size:210px;margin-top:20px;line-height:.92;white-space:nowrap">¿MITO O</div>
<div class="h red" style="font-size:210px;line-height:.92">VERDAD?</div>
<div class="body" style="margin-top:46px;max-width:880px;font-size:54px">3 frases que vas a escuchar este mes. Adivina antes de deslizar.</div>
<div style="display:flex;gap:30px;margin-top:56px;align-items:center">{stamp('MITO',-8).replace('140px','84px').replace('10px solid','7px solid')}{stamp('VERDAD',5,True).replace('140px','84px').replace('10px solid','7px solid')}</div>
</div>""", 1, 5, gx='80%', gy='25%')
mv(2,'Si falté dos semanas, ya perdí todo.','MITO',False,'Faltar no borra lo que ya hiciste. Lo que cuenta es <span class="hl">volver.</span>','20%','60%')
mv(3,'En diciembre ya no vale la pena empezar.','MITO',False,'Empezar ahora es llegar a enero con el hábito hecho, no con el propósito.','80%','60%')
mv(4,'Volver después de faltar cuesta.','VERDAD',True,'Sí cuesta. Por eso el regreso va ligero, sin culpa y sin compararte con nadie.','25%','55%')
page('C5', f"""<div class="wrap">
<div class="kick">Resultado</div>
<div class="h" style="font-size:132px;margin-top:20px">¿CUÁNTAS<br><span class="red">LE ATINASTE?</span></div>
<div style="display:flex;gap:18px;margin:36px 0 48px">{''.join(f'<div style="flex:1;height:120px;border-radius:20px;background:{"#d6453d" if i==3 else "#262626"};border:2px solid #3a3a3a;display:flex;align-items:center;justify-content:center"><span class="h" style="font-size:72px">{i}/3</span></div>' for i in range(4))}</div>
<div class="body" style="margin-bottom:44px;font-size:48px">Comenta tu resultado y empieza diciembre entrenando.</div>
{ctablock()}</div>""", 5, 5, gx='85%', gy='15%')
