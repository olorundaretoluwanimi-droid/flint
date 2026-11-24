# One-off: turn the Newton page (copied to flint/index.html) into the Flint page — keeps the primitives and the photo /
# stat / card / quote scenes, replaces the rest with Flint's scene types (date cards, film clips, strike board, charts).
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(D, 'index.html'); s = open(p, encoding='utf-8').read()
head = s[:s.index("function sPano(t, s)")]
tail = s[s.index("function subs(t)"):]
head = head.replace("<title>What Happened to Newton, Iowa?</title>", "<title>What Happened to Flint, Michigan?</title>")
head = head.replace('// "What Happened to Newton, Iowa?"', '// "What Happened to Flint, Michigan?"')
head = head.replace("const PAPERY = img => /sanborn|patent|ad1|ad_|birdseye|ww1/.test(img.src || '');", "const PAPERY = img => /sanborn|map1955|buick_city1950/.test(img.src || '');")
a = "  const names = new Set(['hq2005', 'sanborn1918_maytag', 'pano1907', 'square2014_court', 'wringer', 'fl_maytag_1935', 'mural2017']);"
assert a in head
head = head.replace(a, "  const names = new Set(['strike_window', 'strike_sleeping', 'usda_water', 'vehicle_city', 'durant1916', 'saginaw1910', 'guard_gun']);")
a = "  await Promise.all(L);"
head = head.replace(a, "  for (const [c, n] of Object.entries(CLIPN)) { CLIP[c] = []; for (let i = 1; i <= n; i++) L.push(load(`assets/film/${c}/${String(i).padStart(3, '0')}.jpg`).then(im => CLIP[c][i - 1] = im)); }\n" + a, 1)
head = head.replace("const IM = {}; let GRAIN = [];", "const IM = {}, CLIP = {}; let GRAIN = [];\nconst CLIPN = { c0: 60, c1: 60, c2: 60, c3: 60, c4: 60, c5: 60, c6: 60 };")
new = open(os.path.join(D, 'tools', 'page_flint.js'), encoding='utf-8').read()
open(p, 'w', encoding='utf-8').write(head + new + tail); print('ok')
