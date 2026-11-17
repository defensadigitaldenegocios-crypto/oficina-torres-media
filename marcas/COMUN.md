# Redes de la Oficina Torres · proceso común

Este repo (público) guarda el material de marca y las publicaciones de cada semana. Las tareas programadas de los lunes leen de aquí, diseñan, suben aquí sus JPG (Metricool los toma de raw.githubusercontent.com) y programan en Metricool.

```
marcas/<marca>/GUIA.md          reglas, voz, datos y estilo de la marca (LÉELA COMPLETA)
marcas/<marca>/assets/          logos, latas, fotos oficiales
marcas/<marca>/semanas/AAAA-MM-DD/   JPG de la semana + src/ (HTML) + NOTAS.md
<raíz>/*.jpg|mp4                ejemplos de las tandas de octubre (referencia de estilo)
```

## Proceso de cada lunes (una marca por tarea)
1. **Contexto.** Lee `marcas/<marca>/GUIA.md` y los `NOTAS.md` de las 2 semanas más recientes de la marca. No repitas ganchos ni formatos de portada de la semana anterior.
2. **Qué ya hay.** En Metricool: `getScheduledPosts` del lunes al domingo de esta semana para el blogId de la marca. Si ya hay 2 o más publicaciones programadas esta semana, NO crees nada: solo manda el análisis del paso 3 y di qué hay programado.
3. **Qué funcionó.** `getAnalyticsDataByMetrics` de los últimos 14 días (Instagram: IGPO02 alcance, IGPO13 likes, IGPO08 comentarios, IGPO15 guardados, IGPO27 compartidos; Facebook y TikTok si están conectadas). Con pocos datos, no saques conclusiones fuertes; dilo.
4. **Ideas.** Si vidIQ está disponible, 1–2 búsquedas de outliers en español de México del tema de la marca (últimos 30 días). WebSearch (modo standard) de fechas relevantes en Monterrey/México esa semana (festivos, quincena, partidos, temporada). Elige 3 ganchos distintos con intriga o identificación y una mecánica de interacción (comenta, etiqueta, guarda, mándaselo a).
5. **Diseño.** 3 carruseles de 4–5 láminas, 1080×1350 (4:5), JPG calidad 90. HTML/CSS renderizado con Playwright:
   - Trabaja en `/home/claude/redes-<marca>` (fuera del repo). `npm i playwright@1.56.1 @fontsource/<fuente>...` (las fuentes de la guía; Google Fonts no carga en este entorno, usa Fontsource con `@font-face` y rutas `file://` absolutas). Chromium: `chromium.launch()` sin opciones; si falla, `executablePath:'/opt/pw-browsers/chromium'`.
   - Imágenes con `file://` absoluto desde `marcas/<marca>/assets/`. Usa SOLO material oficial de assets; no inventes productos ni platillos, no generes fotos falsas del producto.
   - Texto de cuerpo de 40 px o más, máximo ~25 palabras por lámina, contraste alto. Sin emojis dentro de las láminas.
   - Revisa CADA lámina con Read (arma tiras con Pillow): nada encimado, nada cortado, nada fuera de lámina, sin huecos enormes. Corrige y vuelve a renderizar hasta que se vea profesional.
6. **Calidad.** Califica cada carrusel con el checklist de la guía (10 puntos). Mínimo 8/10 y **ningún punto eliminatorio en No**. Si no pasa, corrige antes de programar. Anota la calificación en NOTAS.md.
7. **Subir.** Copia los JPG a `marcas/<marca>/semanas/<lunes AAAA-MM-DD>/` (nombres A1.jpg…C5.jpg), el HTML a `src/` y escribe `NOTAS.md` (tabla día/hora/gancho/formato, qué aprendiste de las métricas, calificación). `git add`, commit en español, `git pull --rebase origin main` y `git push origin main`. Si el push falla por conflicto, repite pull --rebase y push (hasta 3 veces). Verifica con curl que la URL raw de cada JPG responde 200: `https://raw.githubusercontent.com/defensadigitaldenegocios-crypto/oficina-torres-media/main/marcas/<marca>/semanas/<fecha>/A1.jpg`.
8. **Programar.** `createScheduledPost` con el blogId de la marca, en los días y horas de la guía (solo fechas futuras), en las redes de la guía. `autoPublish true`, `draft false`, `media` = URLs raw en orden, `mediaAltText` por lámina, `instagramData {"type":"POST","collaborators":[],"isAiGenerated":<según guía>}`. Pie de foto: primera línea = gancho; 2–4 líneas; 1–2 emojis; una instrucción de interacción concreta; CTA real de la guía; 4–5 hashtags.
9. **Aviso final (corto, en español):** «<Marca> · semana programada»: tabla con día, hora, gancho y plannerUrl de cada post; 2 líneas de lo que funcionó la semana pasada; cualquier falla clara.

## Reglas que nunca se rompen
- Nada de precios, promociones, descuentos, horarios ni datos que no estén en la guía. Ante la duda, no lo pongas.
- Nada de promesas de salud ni de resultados.
- Solo publicaciones en las redes de la guía. Nunca mensajes directos, nunca seguir cuentas, nunca comentar en cuentas ajenas.
- No toques las publicaciones de otras marcas ni las que ya estaban programadas.
