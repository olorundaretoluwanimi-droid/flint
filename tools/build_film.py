#!/usr/bin/env python3
"""lines.json + narration durations + the shot list below → film.json (scenes, voice starts, subtitles) and audio/cues.json.
Each day opens on a big red date card (CARD s). Rings: [src_x, src_y, r, label, at]; at ≥ 0 = seconds after the line starts,
at < 0 = fraction of the line. Every scene lasts until the next one starts."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = json.load(open(os.path.join(D, 'audio/lines.json'), encoding='utf-8'))
DUR = json.load(open(os.environ.get('DURFILE') or os.path.join(D, 'audio/vo/dur.json')))
GAP, CARD, LEAD, END = 0.9, 4.6, 1.2, 16.0

CH = {'open': None,
      'd1': ('DAY 1', '16 SEPT 1908', 'The day General Motors was born', 'vehicle_city'),
      'd2': ('DAY 2', '30 DEC 1936', 'The night they sat down', 'strike_sitdowners'),
      'd3': ('DAY 3', '11 FEB 1937', 'The day they won', 'guard_drill1'),
      'd4': ('DAY 4', '1978', 'The year at the top', 'buick_city1950'),
      'd5': ('DAY 5', '29 JUNE 1999', 'The last Buick', 'ac_demolition'),
      'd6': ('DAY 6', 'OCT 2014', 'The day the water changed', 'epa_tower'),
      'today': ('', 'TODAY', '', 'usda_water')}
COLOUR = ('ac_demolition', 'chevy_commons', 'dompolski', 'epa_', 'guard2016', 'obama_', 'usda_', 'map1947', 'kearsley', 'buick_postcard')

P = lambda img, **k: dict(type='photo', img=img, **k)
SD = 'PHOTO · SHELDON DICK · FISHER BODY PLANT, FLINT · 1937'
MH = 'FILM · “MASTER HANDS” · CHEVROLET PLANTS, FLINT · 1936'
SB09 = 'SANBORN MAP · FLINT · NOV 1909'
EPA = 'U.S. EPA · FLINT · 2016'
NG16 = 'MICHIGAN NATIONAL GUARD · FLINT · JAN 2016 (CC BY 2.0)'
S = {
 # ── cold open ──
 'n01': dict(type='open'),
 'n02': P('strike_entrance', tag='STRIKERS GUARDING A WINDOW ENTRANCE · FISHER BODY, FLINT · SHELDON DICK · 1937', small=1),
 'n03': P('strike_window', tag=SD, z=(1.0, 1.15), fy=.4),
 'q01': dict(type='quote', img='strike_window', fx=.35, imgTag='SHELDON DICK · 1937', q=['“She’s ours!”'], who='A SIT-DOWNER · 30 DEC 1936 · HISTORY.COM', at=0.0),
 'n04': dict(type='stat', img='strike_sitdowners', num='44', label='days inside the plants', tag=SD, at=0.3),
 'n05': dict(type='stat', img='buick_city1950', num='≈ 80,000', label='GM jobs in Flint, 1978', tag='MAP OF THE BUICK WORKS, FLINT · c. 1950', at=-0.35),
 'n06': dict(type='stat', img='ac_demolition', num='−59%', label='Flint’s population, 1960 → 2020', tag='AC SPARK PLUG SITE, FLINT · 2009 (CC BY 2.0)', at=0.3),
 'n07': dict(type='title'),
 'n08': P('strike_sleeping', tag='A STRIKER OFF SENTRY DUTY, ASLEEP ON CAR SEATS · SHELDON DICK · 1937', small=1),
 'n09': P('saginaw1910', tag='SAGINAW STREET, FLINT · REAL-PHOTO POSTCARD · c. 1910', z=(1.0, 1.1), fy=.5),
 'n10': P('strike_meal', tag='STRIKERS EATING IN THE PLANT CAFETERIA · SHELDON DICK · 1937', small=1),
 # ── Day 1 ──
 'n11': P('durant_bain', tag='W. C. DURANT · BAIN NEWS SERVICE · LIBRARY OF CONGRESS', fy=.25, z=(1.0, 1.1)),
 'n12': dict(type='card', name='William C. Durant', sub='1861–1947 · “BILLY” · FOUNDER OF GENERAL MOTORS', img='durant1916', tag='W. C. DURANT · c. 1916', portrait=1),
 'n13': dict(type='card', name='J. Dallas Dort', sub='DURANT’S PARTNER · FLINT ROAD CART CO., 1886', img='dort', tag='J. D. DORT · 1920', date='1886', portrait=1),
 'n14': P('vehicle_city', tag='“FLINT VEHICLE CITY” · DETROIT & SAGINAW STREETS · POSTCARD · 1906', date='1900', z=(1.0, 1.12), fy=.3),
 'n15': P('buick1907', tag='BUICK MOTOR WORKS, FLINT · 1907', date='1904', z=(1.0, 1.1)),
 'n16': P('buick_postcard', tag='BUICK FACTORY AND OFFICES, FLINT · POSTCARD', date='1908', small=1),
 'n17': P('sanborn1909_buick2', tag=SB09 + ' · SHEET 35', fy=.78, z=(1.0, 1.06), rings=[[2295, 2338, 460, 'BUICK MOTOR CO.', -0.3]]),
 'n18': dict(type='seq', items=[['wagon_works', 'FLINT WAGON WORKS (CHEVROLET) · 1912', 0], ['buick_whistle', 'BUICK WORKERS · POSTCARD · 1912', 0], ['kearsley1909', 'KEARSLEY ST., FLINT · 1909', 1]]),
 'n19': dict(type='bars', title='FLINT · POPULATION · U.S. CENSUS', data=[['1900', 13103], ['1910', 38550], ['1920', 91599], ['1930', 156492]], max=200000, at=[-0.22, -0.4, -0.55, -0.7], red=3,
             img='buick_whistle', imgTag='BUICK WORKERS AT THE WHISTLE · 1912'),
 'n20': dict(type='film', clips=['c1', 'c2', 'c3', 'c5'], tag=MH),
 'n21': dict(type='film', clips=['c0', 'c4'], tag=MH),
 'n22': P('strike_window', tag=SD, z=(1.15, 1.25), fx=.3, fy=.45),
 # ── Day 2 ──
 'n23': P('strike_window', tag=SD, z=(1.0, 1.08)),
 'n24': dict(type='film', clips=['c6', 'c5'], tag=MH),
 'n25': P('strike_entrance', tag='GUARDING THE WINDOW ENTRANCE · FISHER BODY, FLINT · 1937', small=1),
 'n26': P('strike_sitdowners', tag=SD, z=(1.0, 1.12)),
 'n27': P('strike_sitdowners', tag=SD, z=(1.0, 1.08), name='Photographs: Sheldon Dick', role='FARM SECURITY ADMINISTRATION · LIBRARY OF CONGRESS'),
 'n28': dict(type='seq', items=[['strike_sleeping', 'ASLEEP ON CAR SEATS · 1937', 0], ['strike_meal', 'THE PLANT CAFETERIA · 1937', 0], ['strike_entrance', 'ON GUARD AT A WINDOW · 1937', 0]]),
 'n30': P('women_flint', tag='“WOMEN OF FLINT” · PAINTING · JOSEPH VAVAK · 1937', z=(1.0, 1.1), date='1937'),
 'n31': dict(type='board', upto=1, from_=1),
 'n32': dict(type='stat', img='strike_window', num='14', label='strikers hit by gunfire · 11 January 1937', tag=SD, at=0.3),
 'n33': P('guard_gun', tag='NATIONAL GUARD OVERLOOKING CHEVROLET PLANTS 9 AND 4 · SHELDON DICK · 1937', small=1, date='1937'),
 'n34': P('guard_drill1', tag='NATIONAL GUARD AT A FLINT SCHOOL · 1937', z=(1.0, 1.1)),
 'n35': dict(type='board', upto=3, from_=3),
 'n36': dict(type='bars', title='GENERAL MOTORS · CARS BUILT PER MONTH', data=[['DEC 1936', 50000], ['FEB 1937', 125, '125']], max=55000, at=[-0.1, -0.6], red=1,
             img='guard_gun', imgTag='NATIONAL GUARD, FLINT · 1937'),
 'n37': P('strike_sitdowners', tag=SD, z=(1.1, 1.2), fx=.6),
 # ── Day 3 ──
 'n38': dict(type='board', upto=4, from_=4),
 'n39': P('guard_drill3', tag='NATIONAL GUARD, FLINT · 1937', z=(1.0, 1.1)),
 'n40': P('strike_window', tag=SD, z=(1.05, 1.15), fy=.3),
 'n41': dict(type='stat', img='strike_sleeping', num='136,000', label='GM workers idled · 280,000 cars unbuilt', tag='SHELDON DICK · 1937', at=-0.2),
 'n42': dict(type='bars', title='UNITED AUTO WORKERS · MEMBERS', data=[['FEB 1937', 88000], ['OCT 1937', 400000]], max=420000, at=[-0.2, -0.6], red=1,
             img='strike_window', imgTag='SIT-DOWNERS · 1937'),
 'n43': dict(type='seq', items=[['ac_women1942', 'AC SPARK PLUG, FLINT · WAR WORK · ANN ROSENER, OWI · 1942', 0], ['ac_women1942b', 'AC SPARK PLUG, FLINT · ANN ROSENER, OWI · 1942', 0]]),
 'n44': P('map1947', tag='MAP OF FLINT · FRED JOHNSON MAPS · 1947 (CC BY 2.0)', z=(1.0, 1.15)),
 'n45': dict(type='pop', data=[[1900, 13103], [1910, 38550], [1920, 91599], [1930, 156492], [1940, 151543], [1950, 163143], [1960, 196940]], marks=[[1960, 196940, -0.6]], end=-0.6),
 'n46': P('map1955', tag='FLINT · MAP · 1955', small=1),
 # ── Day 4 ──
 'n47': P('buick_city1950', tag='MAP OF THE BUICK WORKS, FLINT · c. 1950', z=(1.0, 1.15), fy=.4),
 'n48': dict(type='stat', img='buick_city1950', num='≈ 80,000', label='GM jobs in and around Flint · 1978', tag='MAP OF THE BUICK WORKS · c. 1950', at=0.3),
 'n49': dict(type='stat', img='dompolski1980', num='618,365', label='GM workers in the U.S. at the peak · 1979', tag='SAGINAW STREET, FLINT · JOHN MARGOLIES · 1980 (LIBRARY OF CONGRESS)', at=-0.55),
 'n50': dict(type='bars', title='IMPORTED CARS · SHARE OF THE U.S. MARKET', data=[['1978', 18, '18%'], ['1980', 26.5, '26.5%']], max=30, at=[-0.4, -0.75], red=1,
             img='dompolski1980', imgTag='FLINT · JOHN MARGOLIES · 1980'),
 'n51': P('dompolski1980', tag='DOM POLSKI, SAGINAW STREET, FLINT · JOHN MARGOLIES · 1980 (LIBRARY OF CONGRESS)', z=(1.0, 1.1)),
 'n52': P('dompolski1980', tag='SAGINAW STREET, FLINT · JOHN MARGOLIES · 1980 (LIBRARY OF CONGRESS)', z=(1.1, 1.2), fx=.6, date='1989'),
 'n53': P('buick_whistle', tag='BUICK WORKERS AT THE WHISTLE · POSTCARD · 1912', z=(1.0, 1.1)),
 'n54': dict(type='pop', data=[[1900, 13103], [1910, 38550], [1920, 91599], [1930, 156492], [1940, 151543], [1950, 163143], [1960, 196940], [1970, 193317], [1980, 159611]],
             marks=[[1960, 196940, -0.2], [1980, 159611, -0.5]], end=-0.5),
 'n55': P('ac_demolition', tag='AC SPARK PLUG SITE, FLINT · 2009 (CC BY 2.0)', z=(1.0, 1.08)),
 # ── Day 5 ──
 'n56': P('sanborn1909_buick2', tag=SB09 + ' · THE BUICK WORKS, NORTH FLINT', z=(1.0, 1.1), fy=.5, fx=.7),
 'n57': P('buick1906', tag='THE FIRST BUICK FACTORY, NORTH FLINT · c. 1906', z=(1.0, 1.1)),
 'n58': P('buick_postcard', tag='BUICK FACTORY AND OFFICES, FLINT · POSTCARD', small=1),
 'n59': dict(type='stat', img='ac_demolition', num='≈ 1,200', label='workers left at Buick City in 1999', tag='AC SPARK PLUG SITE, FLINT · 2009 (CC BY 2.0)', at=-0.6),
 'n60': dict(type='stat', img='buick1907', num='1999', label='J.D. Power Platinum Award · plant quality', tag='BUICK MOTOR WORKS, FLINT · 1907', at=-0.55),
 'n61': P('buick1907', tag='BUICK MOTOR WORKS, FLINT · 1907', z=(1.1, 1.2)),
 'n62': P('ac_demolition', tag='AC SPARK PLUG SITE, FLINT · 2009 (CC BY 2.0)', z=(1.05, 1.12)),
 'n63': dict(type='bars', title='GENERAL MOTORS JOBS IN FLINT', data=[['1978', 80000, '≈ 80,000'], ['1999', 33000, '≈ 33,000'], ['2010', 8000, '< 8,000']], max=85000, at=[-0.1, -0.2, -0.75], red=2,
             img='ac_demolition', colour=1, imgTag='AC SPARK PLUG SITE · 2009 (CC BY 2.0)'),
 'n64': P('saginaw1910', tag='SAGINAW STREET, FLINT · c. 1910', z=(1.0, 1.08)),
 # ── Day 6 ──
 'n65': P('epa_tower', tag=EPA + ' · THE WATER PLANT', z=(1.0, 1.08)),
 'n66': P('epa_tower', tag=EPA, z=(1.1, 1.2), fx=.4),
 'n67': dict(type='stat', img='epa_tower', num='25 APR 2014', label='Flint switches to Flint River water', tag=EPA, at=-0.4),
 'n68': P('epa_testing', tag=EPA + ' · TESTING WATER AT A SINK', z=(1.0, 1.1)),
 'n69': dict(type='film', clips=['c3', 'c2'], tag=MH + ' · ENGINE WORK (ILLUSTRATIVE)'),
 'q02': dict(type='quote', img='epa_testing', imgTag=EPA, q=['“They told Flint…', 'you’re causing us', 'to lose engines.”'], who='RONALD JAMISON · 39 YEARS AT THE FLINT ENGINE PLANT · DEMOCRACY NOW! · 2016', at=-0.45),
 'q03': dict(type='quote', img='epa_testing', imgTag=EPA, q=['“They took all', 'the water fountains', 'out of the plant.”'], who='RONALD JAMISON · DEMOCRACY NOW! · 17 FEB 2016'),
 'n70': P('epa_testing', tag=EPA, z=(1.1, 1.2), fx=.6),
 'n71': dict(type='stat', img='epa_tower', num='16 OCT 2015', label='Flint switches back to Detroit water', tag=EPA, at=-0.75),
 'n72': dict(type='stat', img='epa_testing', num='12', label='deaths, at least, in a Legionnaires’ outbreak', tag=EPA, at=-0.7),
 'n73': dict(type='pair', a='guard_drill1', b='guard2016_door', ta='NATIONAL GUARD · FLINT · 1937', tb=NG16, cb=1, bat=-0.3),
 'n74': dict(type='stat', img='guard2016_site', num='$626M', label='settlement approved · 2021', tag=NG16, at=-0.45,
             note=['Charges later dropped or dismissed (2019–2023)', 'INCLUDING BOTH FORMER EMERGENCY MANAGERS']),
 'n75': P('guard2016_site2', tag=NG16, z=(1.0, 1.1)),
 # ── Today ──
 'n76': dict(type='pop', data=[[1900, 13103], [1910, 38550], [1920, 91599], [1930, 156492], [1940, 151543], [1950, 163143], [1960, 196940], [1970, 193317], [1980, 159611], [1990, 140761], [2000, 124943], [2010, 102434], [2020, 81252]],
             marks=[[1960, 196940, -0.4], [2020, 81252, -0.2]], end=-0.35),
 'n77': P('usda_water', tag='FLINT · USDA PHOTO · 2016', z=(1.0, 1.08)),
 'n78': P('chevy_commons_ground', tag='GROUNDBREAKING FOR CHEVY COMMONS, FLINT · 2015 (CC BY 2.0)', small=1),
 'n79': P('sanborn1909_buick2', tag=SB09 + ' · THE BUICK WORKS', z=(1.1, 1.2), fy=.4, fx=.75),
 'n80': P('strike_meal', tag='STRIKERS IN THE PLANT CAFETERIA · 1937', small=1),
 'n81': dict(type='pair', a='strike_window', b='guard2016_site2', ta='FLINT · 1937', tb='FLINT · 2016 (CC BY 2.0)', cb=1, bat=-0.45),
 'n82': dict(type='pair', a='vehicle_city', b='usda_water', ta='“FLINT VEHICLE CITY” · 1906', tb='THE FLINT ARCH · 2016 · ≈ SAME STREET (USDA)', cb=1, bat=-0.4),
 'q04': dict(type='quote', img='strike_window', imgTag=SD, q=['“She’s ours!”'], who='A SIT-DOWN STRIKER · 30 DECEMBER 1936', at=0.0),
 'n83': P('strike_sitdowners', tag=SD, z=(1.0, 1.08)),
 'n84': P('usda_water', tag='FLINT · 2016 (USDA)', z=(1.05, 1.12)),
}
missing = [l['id'] for l in L if l['id'] not in S]
if missing: raise SystemExit('no shot for ' + ', '.join(missing))
scenes, vo, subs, t, prev = [], {}, [], LEAD, None
for l in L:
    ch = l['chapter']
    if ch != prev and CH[ch]:
        num, date, sub, img = CH[ch]
        scenes.append(dict(type='chapter', t0=round(t, 2), num=num, title=date, sub=sub, img=img, colour=img.startswith(COLOUR))); t += CARD
    prev = ch; d = DUR[l['id']]
    sh = dict(S[l['id']]); sh['t0'] = round(t, 2); sh['line'] = l['id']; sh['vd'] = round(d, 2)
    if 'from_' in sh: sh['from'] = sh.pop('from_')
    if 'img' in sh and 'colour' not in sh and sh['img'].startswith(COLOUR): sh['colour'] = 1
    scenes.append(sh); vo[l['id']] = round(t, 3)
    parts = l['subs']; n = sum(len(p) for p in parts); tt = t
    for i, p in enumerate(parts):
        dd = d * len(p) / n; subs.append([round(tt - .1, 2), round(tt + dd + (.3 if i == len(parts) - 1 else .02), 2), p]); tt += dd
    t += d + GAP
for i in range(len(subs) - 1): subs[i][1] = round(min(subs[i][1], subs[i + 1][0] - .02), 2)
scenes.append(dict(type='end', t0=round(t + .6, 2)))
dur = round(t + .6 + END, 1)
for i, s in enumerate(scenes): s['t1'] = scenes[i + 1]['t0'] if i + 1 < len(scenes) else dur
F = dict(dur=dur, scenes=scenes, vo=vo, subs=subs)
json.dump(F, open(os.path.join(D, 'film.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump([{'t0': a, 't1': b, 'text': s} for a, b, s in subs], open(os.path.join(D, 'audio/cues.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('scenes', len(scenes), 'subs', len(subs), 'duration', dur, 's =', round(dur / 60, 1), 'min')
