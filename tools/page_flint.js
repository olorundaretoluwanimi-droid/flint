function sFilm(t, s) {   // 1936 film (Master Hands, Chevrolet, Flint): clips cut to 15 fps frame sequences, ping-pong
  const l = t - s.t0, per = (s.t1 - s.t0) / s.clips.length, ci = Math.min(s.clips.length - 1, Math.floor(l / per)), c = s.clips[ci], fr = CLIP[c], n = fr.length;
  const i = Math.floor(((l - ci * per) * 15) % (2 * n - 2)), j = i < n ? i : 2 * n - 2 - i, z = lerp(1, 1.05, (l - ci * per) / per);
  const X = (W - 1146) / 2; cover(fr[j], X, 60, 1146, 860, { flash: 1 - seg(l - ci * per, 0, .12) }, .5, .5, null, z); tag(s.tag, X, 46, { id: 'tg' });
  if (s.date) dateBox(s.date, X + 1146, 60, seg(t, s.t0 + .2, s.t0 + .3));
}
const BOARD = [['30 DEC', 'Sit-down', 'Fisher Body Plant No. 1'], ['11 JAN', 'Running Bulls', '14 strikers shot · Fisher No. 2'], ['12 JAN', 'National Guard', 'sent to keep the peace'],
  ['1 FEB', 'Chevy Plant 4', 'taken · Chevrolet engines stop'], ['11 FEB', 'Agreement', 'GM recognises the UAW']];
function sBoard(t, s) {
  cover(IM[s.img || 'strike_window'], 60, 60, 1800, 470, { flash: s.hold ? 0 : flashK(t, s) }, .5, s.fy ?? .35, null, lerp(1.0, 1.05, K(t, s))); tag(s.tag || 'SIT-DOWNERS AT THE WINDOWS · SHELDON DICK · 1937', 60, 46, { id: 'bt' });
  const X0 = 240, step = 360, Y = 660; hair(X0 - 120, Y, X0 + 4 * step + 120, Y, C.line, 2);
  BOARD.forEach(([d, a, b], i) => { if (i > s.upto) return; const a0 = (s.from ?? s.upto) <= i && !s.hold ? AT(s, -(.15 + (i - (s.from ?? s.upto)) * .2)) : 0, k = seg(t, a0, a0 + .1), X = X0 + i * step;
    x.save(); x.globalAlpha = k; x.fillStyle = i === 4 ? C.acc : C.text; x.beginPath(); x.arc(X, Y, 13, 0, 7); x.fill(); x.restore();
    txt(d, X, Y - 34, { s: 46, f: F.mono, w: 600, c: C.acc, al: 'center', a: k, id: 'bd' + i });
    txt(a, X, Y + 68, { s: 34, w: 700, al: 'center', a: k, id: 'ba' + i });
    b.split(' · ').forEach((p, j) => txt(p, X, Y + 108 + j * 34, { s: 23, c: C.dim, al: 'center', a: k, id: 'bb' + i + j })); });
  txt('THE 44 DAYS · 1936–37', 1860, 600, { s: 30, f: F.mono, w: 600, c: C.acc, al: 'right', id: 'by' });
}
function sBars(t, s) {
  cover(IM[s.img], 60, 60, 640, 860, { flash: flashK(t, s), colour: s.colour }, .5, .4, null, lerp(1.1, 1.2, K(t, s))); tag(s.imgTag, 60, 46, { id: 'tg' });
  txt(s.title, 780, 140, { s: 24, f: F.mono, w: 600, c: C.dim, ls: 2, id: 'bt' });
  const mx = s.max, n = s.data.length, gap = 60, BW = Math.min(220, (1060 - gap * (n - 1)) / n), X0 = 800, Yb = 840, Hm = 600;
  s.data.forEach(([y, v, lab], i) => { const a0 = AT(s, s.at[i]), k = eo(seg(t, a0, a0 + .7)); if (k <= 0) return; const h = Hm * v / mx * k, X = X0 + i * (BW + gap);
    fill(X, Yb - h, BW, h, i === (s.red ?? -1) ? C.acc : '#8c7a62'); txt(y, X + BW / 2, Yb + 48, { s: 34, f: F.mono, w: 600, c: C.dim, al: 'center', id: 'by' + i });
    txt(lab || v.toLocaleString('en-US'), X + BW / 2, Yb - h - 18, { s: 36, f: F.mono, w: 600, al: 'center', a: seg(k, .8, 1), id: 'bv' + i }); });
  hair(780, Yb, 1860, Yb, C.dim, 2);
}
function sPop(t, s) {
  cover(IM.saginaw1910, 60, 60, 1800, 860, { flash: flashK(t, s) }, .5, .5); shade(60, 60, 1800, 860, .82);
  txt('FLINT · POPULATION · U.S. CENSUS', 140, 150, { s: 26, f: F.mono, w: 600, c: C.dim, ls: 2, id: 'pt' });
  const X0 = 200, X1 = 1720, Y0 = 820, Y1 = 230, px = y => lerp(X0, X1, (y - 1900) / 120), py = v => lerp(Y0, Y1, v / 210000);
  hair(X0, Y0, X1, Y0, C.dim, 2); [1900, 1930, 1960, 1990, 2020].forEach((y, i) => txt(String(y), px(y), Y0 + 44, { s: 28, f: F.mono, w: 600, c: C.dim, al: 'center', id: 'px' + i }));
  const k = eo(seg(t, s.t0 + .3, AT(s, s.end ?? -.85))), d = s.data, last = d[d.length - 1][0], upto = 1900 + (last - 1900) * k;
  x.save(); x.strokeStyle = C.acc; x.lineWidth = 5; x.beginPath();
  for (let i = 0; i < d.length; i++) { const [y, v] = d[i]; if (y > upto) { const [y0, v0] = d[i - 1], f = (upto - y0) / (y - y0); x.lineTo(px(upto), py(lerp(v0, v, f))); break; } i ? x.lineTo(px(y), py(v)) : x.moveTo(px(y), py(v)); }
  x.stroke(); x.restore();
  s.marks.forEach(([y, v, f], i) => { const kk = seg(t, AT(s, f), AT(s, f) + .1); if (kk <= 0 || upto < y - .5) return;
    x.save(); x.globalAlpha = kk; x.fillStyle = C.acc; x.beginPath(); x.arc(px(y), py(v), 11, 0, 7); x.fill(); x.restore();
    txt(y + ' · ' + v.toLocaleString('en-US'), px(y) + (y > 2000 ? -20 : 0), py(v) - 30, { s: 34, f: F.mono, w: 600, al: y > 2000 ? 'right' : 'center', a: kk, id: 'pv' + i }); });
}
function sSeq(t, s) {
  const n = s.items.length, per = (s.t1 - s.t0) / n, i = Math.min(n - 1, Math.floor((t - s.t0) / per)), [img, tg, col] = s.items[i], l = t - s.t0 - i * per;
  cover(IM[img], 60, 60, 1800, 860, { flash: 1 - seg(l, 0, .14), colour: col }, .5, .45, null, lerp(1, 1.07, l / per)); tag(tg, 60, 46, { id: 'tg' + i });
}
function sPair(t, s) {
  cover(IM[s.a], 60, 60, 880, 860, { flash: flashK(t, s), colour: s.ca }, .5, s.fya ?? .45); tag(s.ta, 60, 46, { id: 'pa' });
  const b0 = AT(s, s.bat ?? 1.2), k = seg(t, b0, b0 + .1); if (k > 0) { cover(IM[s.b], 980, 60, 880, 860, { flash: 1 - seg(t, b0, b0 + .14), colour: s.cb }, .5, s.fyb ?? .45); tag(s.tb, 980, 46, { id: 'pb' }); }
}
function sChapter(t, s) {   // the big red date card that opens each day
  cover(IM[s.img], 60, 60, 1800, 860, { colour: s.colour }, .5, .45, null, lerp(1.0, 1.05, K(t, s))); shade(60, 60, 1800, 860, .74);
  const k = seg(t, s.t0 + .2, s.t0 + .32); txt(s.num, W / 2, 360, { s: 48, f: F.mono, w: 600, c: C.text, al: 'center', ls: 10, a: k, id: 'chn' });
  txt(s.title, W / 2, 560, { s: s.title.length > 10 ? 150 : 180, f: F.mono, w: 600, c: C.acc, al: 'center', a: seg(t, s.t0 + .45, s.t0 + .55), id: 'cht' });
  if (s.sub) txt(s.sub, W / 2, 660, { s: 34, c: C.dim, al: 'center', a: seg(t, s.t0 + .8, s.t0 + .9), id: 'chs' });
}
function sOpen(t, s) {
  const im = IM.strike_window, w = 1100, h = w * im.height / im.width; cover(im, 60, 60 + (860 - h) / 2, w, h, { flash: flashK(t, s, .3) }, .5, .5, null, lerp(1, 1.06, K(t, s)));
  tag('SIT-DOWN STRIKERS · FISHER BODY, FLINT · SHELDON DICK · 1937', 60, 46 + (860 - h) / 2, { id: 'tg' });
  const k = seg(t, s.t0 + .6, s.t0 + .7); txt('THE NIGHT OF', 1220, 400, { s: 40, f: F.mono, w: 600, c: C.dim, ls: 4, a: k, id: 'od1' });
  txt('30 DEC', 1220, 520, { s: 120, f: F.mono, w: 600, c: C.acc, a: k, id: 'od2' }); txt('1936', 1220, 650, { s: 120, f: F.mono, w: 600, c: C.acc, a: k, id: 'od3' });
  txt('FLINT, MICHIGAN', 1224, 720, { s: 30, f: F.mono, w: 600, c: C.text, ls: 3, a: k, id: 'od4' });
}
function sTitle(t, s) {
  cover(IM.vehicle_city, 60, 60, 1800, 860, { flash: flashK(t, s) }, .5, .35, null, lerp(1, 1.06, K(t, s))); tag('“FLINT VEHICLE CITY” · POSTCARD · 1906', 60, 46, { id: 'tt' }); shade(60, 520, 1800, 400, .86);
  const k = seg(t, s.t0 + .3, s.t0 + .45); txt('What Happened to Flint, Michigan?', 120, 680, { s: 92, w: 700, a: k, id: 'ti1' });
  txt('THE TOWN GM BUILT', 126, 750, { s: 30, f: F.mono, c: C.dim, ls: 3, a: seg(t, s.t0 + .9, s.t0 + 1.0), id: 'ti2' });
  x.save(); x.globalAlpha = seg(t, s.t0 + 1.4, s.t0 + 1.5); fill(126, 800, 6, 70, C.acc); x.restore();
  txt('Flint · Genesee County · Michigan', 150, 848, { s: 34, w: 700, a: seg(t, s.t0 + 1.4, s.t0 + 1.5), id: 'ti3' });
}
function sEnd(t, s) {
  const k = seg(t, s.t0, s.t0 + .2); txt('What Happened to Flint, Michigan?', 120, 250, { s: 72, w: 700, a: k, id: 'e1' });
  txt('THE TOWN GM BUILT', 124, 306, { s: 24, f: F.mono, c: C.dim, ls: 1, a: k, id: 'e2' });
  x.save(); x.globalAlpha = k; hair(124, 346, lerp(124, 1200, eo(seg(t, s.t0, s.t0 + .6))), 346, C.dim, 1); x.restore();
  const k3 = seg(t, s.t0 + .5, s.t0 + .6), cr = [
    'Photographs  Sheldon Dick, FSA, 1937; Ann Rosener, OWI, 1942; Bain News Service; John Margolies, 1980 (Library of Congress) · Pete Souza, White House; U.S. EPA; USDA',
    'Film  “Master Hands” (1936), Jam Handy Organization for Chevrolet, Flint (Prelinger Archives, public domain) · Maps  Sanborn Map Co., Flint, 1886 and 1909 (Library of Congress)',
    'Postcards: Burton Historical Collection, Detroit Public Library; DPLA · Painting: Joseph Vavak, “Women of Flint”, 1937 · Michigan National Guard, 2016 (CC BY 2.0)',
    'Office of Sen. Debbie Stabenow (CC BY 2.0); abarndweller (CC BY 2.0); Fred Johnson Maps, scan davecito (CC BY 2.0); via Wikimedia Commons',
    'Words  History.com; CBS News; Democracy Now! (Ronald Jamison, 2016); NPR; Michigan Public; Wikipedia; U.S. Census Bureau',
    'Music  original score; VSCO 2 CE (CC0), Salamander Grand Piano (CC BY 3.0, Alexander Holm)' ];
  cr.forEach((c, i) => txt(c, 124, 560 + i * 40, { s: 20, c: '#CDBFA6', a: k3 }));
  x.save(); x.globalAlpha = seg(t, s.t0 + .8, s.t0 + .9); cover(IM.strike_sleeping, 1360, 80, 440, 330, {}, .5, .5); x.restore();
}
const DRAW = { photo: sPhoto, stat: sStat, card: sCard, quote: sQuote, film: sFilm, board: sBoard, bars: sBars, pop: sPop, seq: sSeq, pair: sPair,
  chapter: sChapter, open: sOpen, title: sTitle, end: sEnd };
