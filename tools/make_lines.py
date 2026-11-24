#!/usr/bin/env python3
"""The script, line by line → audio/lines.json (for the AI33 narrator) and script.md (readable).
Each entry: id, chapter, text (spoken, numbers as words), subs (caption lines, digits). Present tense inside each day."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = 'elevenlabs_0dPqNXnhg2bmxQv1WKDp'   # Storyteller Oxley (AI33 Pro / ElevenLabs)
C = []
def L(ch, i, spoken, *subs): C.append((ch, i, spoken, list(subs)))

# ── cold open: 30 Dec 1936 ──
L('open', 'n01', "It's the night of December the thirtieth, nineteen thirty-six. Flint, Michigan.", "It's the night of 30 December 1936.", "Flint, Michigan.")
L('open', 'n02', "Inside General Motors' Fisher Body Plant Number One, the workers have seen something they don't like. Machinery is being loaded onto railroad cars, bound for other factories.",
  "Inside General Motors' Fisher Body Plant No. 1,", "the workers have seen something they don't like.", "Machinery is being loaded onto railroad cars, bound for other factories.")
L('open', 'n03', "So they stop working. They shut the doors. And they sit down.", "So they stop working. They shut the doors.", "And they sit down.")
L('open', 'q01', "One man shouts: She's ours!", "One man shouts: “She's ours!”")
L('open', 'n04', "They will stay for forty-four days. And when they walk out, the biggest carmaker in the world will have given in. Flint will be the town where American factory workers won.",
  "They will stay for 44 days.", "And when they walk out, the biggest carmaker in the world will have given in.", "Flint will be the town where American factory workers won.")
L('open', 'n05', "Four decades later, about eighty thousand people in Flint will work for General Motors.", "Four decades later, about 80,000 people in Flint", "will work for General Motors.")
L('open', 'n06', "Today, the city has lost more than half its people.", "Today, the city has lost more than half its people.")
L('open', 'n07', "So what did winning buy? And what couldn't it protect?", "So what did winning buy?", "And what couldn't it protect?")
L('open', 'n08', "This is the story of what happened to Flint. Every photograph you'll see is of the real Flint. Every number has a source. And we'll tell it in six days.",
  "This is the story of what happened to Flint.", "Every photograph you'll see is of the real Flint.", "Every number has a source. And we'll tell it in six days.")
L('open', 'n09', "The day General Motors was born. The night they sat down. The day they won. The year at the top. The day the last Buick was built. And the day the water changed.",
  "The day General Motors was born. The night they sat down.", "The day they won. The year at the top.", "The day the last Buick was built. And the day the water changed.")
L('open', 'n10', "If anyone in your family ever carried a union card, or built a car in Flint, this one is for them.", "If anyone in your family ever carried a union card,", "or built a car in Flint, this one is for them.")

# ── Day 1: 16 Sept 1908 ──
L('d1', 'n11', "It's the sixteenth of September, nineteen-oh-eight. And a man from Flint is about to create a car company that will become the biggest in the world.", "It's 16 September 1908.", "And a man from Flint is about to create a car company", "that will become the biggest in the world.")
L('d1', 'n12', "His name is William Crapo Durant. Everyone calls him Billy. He isn't an engineer. He's a salesman.", "His name is William Crapo Durant. Everyone calls him Billy.", "He isn't an engineer. He's a salesman.")
L('d1', 'n13', "Twenty-two years earlier, in eighteen eighty-six, he borrowed fifteen hundred dollars and bought the rights to a two-wheeled road cart. With a partner, Dallas Dort, he started building them in Flint.",
  "Twenty-two years earlier, in 1886,", "he borrowed $1,500 and bought the rights to a two-wheeled road cart.", "With a partner, Dallas Dort, he started building them in Flint.")
L('d1', 'n14', "By nineteen hundred, the Durant-Dort Carriage Company was the biggest carriage maker in America. Flint put up an arch over its main street. Vehicle City.",
  "By 1900, the Durant-Dort Carriage Company", "was the biggest carriage maker in America.", "Flint put up an arch over its main street: Vehicle City.")
L('d1', 'n15', "Then the vehicles changed. In nineteen-oh-four, Durant took over a small, struggling company called Buick. He sold Buicks the way he had sold carts, and Buick grew faster than anyone could build them.",
  "Then the vehicles changed. In 1904, Durant took over", "a small, struggling company called Buick.", "He sold Buicks the way he had sold carts,", "and Buick grew faster than anyone could build them.")
L('d1', 'n16', "Now, in September nineteen-oh-eight, he puts Buick inside a new company, with Oldsmobile beside it. He calls it General Motors.", "Now, in September 1908, he puts Buick inside a new company,", "with Oldsmobile beside it. He calls it General Motors.")
L('d1', 'n17', "The fire-insurance map of Flint the next year shows what Buick has become: a factory spread over block after block, on the north side of town.", "The fire-insurance map of Flint the next year shows what Buick has become:", "a factory spread over block after block, on the north side of town.")
L('d1', 'n18', "More would come. Chevrolet built cars in Flint's old wagon works. Fisher Body stamped the steel. AC made the spark plugs.", "More would come. Chevrolet built cars in Flint's old wagon works.", "Fisher Body stamped the steel. AC made the spark plugs.")
L('d1', 'n19', "And the people came. In nineteen hundred, Flint had thirteen thousand people. By nineteen thirty, it had more than a hundred and fifty thousand.", "And the people came.", "In 1900, Flint had 13,000 people.", "By 1930, it had more than 150,000.")
L('d1', 'n20', "This is what working there looked like, filmed inside Chevrolet's Flint plants in nineteen thirty-six. The foundry. The presses. The line. Fast, hot, and never stopping.",
  "This is what working there looked like,", "filmed inside Chevrolet's Flint plants in 1936.", "The foundry. The presses. The line. Fast, hot, and never stopping.")
L('d1', 'n21', "The pay was better than on any farm. But the men on the line had no say over how fast it ran, or who was laid off when it slowed.", "The pay was better than on any farm.", "But the men on the line had no say over how fast it ran,", "or who was laid off when it slowed.")
L('d1', 'n22', "So why would they risk everything?", "So why would they risk everything?")

# ── Day 2: 30 Dec 1936 ──
L('d2', 'n23', "It's the thirtieth of December, nineteen thirty-six, again. And now we're inside.", "It's 30 December 1936, again.", "And now we're inside.")
L('d2', 'n24', "The union has a plan. General Motors makes almost all its car bodies from steel dies, the giant moulds that stamp out the panels. And there are only two sets. One in Cleveland. One here, in Fisher Body Plant Number One.",
  "The union has a plan. General Motors makes almost all its car bodies", "from steel dies, the giant moulds that stamp out the panels.", "And there are only two sets. One in Cleveland.", "One here, in Fisher Body Plant No. 1.")
L('d2', 'n25', "When the workers see those dies being moved toward the railroad cars, they know. If the dies leave, the strike is lost before it starts.", "When the workers see those dies being moved toward the railroad cars,", "they know. If the dies leave,", "the strike is lost before it starts.")
L('d2', 'n26', "So they don't walk out. Walking out would let the company bring in other men. Instead, they stay inside, and they sit down.", "So they don't walk out.", "Walking out would let the company bring in other men.", "Instead, they stay inside, and they sit down.")
L('d2', 'n27', "These photographs were taken inside the Fisher Body plants by a government photographer, Sheldon Dick.", "These photographs were taken inside the Fisher Body plants", "by a government photographer, Sheldon Dick.")
L('d2', 'n28', "The strikers sleep on the car seats from the assembly line. They eat in the plant cafeteria. They guard the doors and windows in shifts.", "The strikers sleep on the car seats from the assembly line.", "They eat in the plant cafeteria.", "They guard the doors and windows in shifts.")
L('d2', 'n30', "Outside, the women of Flint organize. They call themselves the Women's Emergency Brigade, and they wear red berets. One of their organizers is Genora Johnson.",
  "Outside, the women of Flint organize.", "They call themselves the Women's Emergency Brigade,", "and they wear red berets.", "One of their organizers is Genora Johnson.")
L('d2', 'n31', "On the eleventh of January, the police try to cut off the food at Fisher Body Plant Number Two. The strikers fight back with fire hoses and heavy car-door hinges. The police fire tear gas, and then bullets.",
  "On 11 January, the police try to cut off the food", "at Fisher Body Plant No. 2.", "The strikers fight back with fire hoses and heavy car-door hinges.", "The police fire tear gas, and then bullets.")
L('d2', 'n32', "Fourteen strikers are hit by gunfire. The police pull back. The strikers call it the Battle of the Running Bulls.", "Fourteen strikers are hit by gunfire.", "The police pull back.", "The strikers call it the Battle of the Running Bulls.")
L('d2', 'n33', "Now the new governor of Michigan, Frank Murphy, sends in the National Guard. But not to throw the strikers out. To keep the peace, and to protect them.",
  "Now the new governor of Michigan, Frank Murphy, sends in the National Guard.", "But not to throw the strikers out.", "To keep the peace, and to protect them.")
L('d2', 'n34', "A court orders the strikers to leave. They don't. And the governor will not use the troops to make them.", "A court orders the strikers to leave. They don't.", "And the governor will not use the troops to make them.")
L('d2', 'n35', "On the first of February, the union pulls a trick. It starts a fight at Chevrolet Plant Number Nine, to draw the company guards away. Meanwhile, its men take Chevrolet Plant Number Four. That's where the engines for every Chevrolet are made.",
  "On 1 February, the union pulls a trick.", "It starts a fight at Chevrolet Plant No. 9, to draw the company guards away.", "Meanwhile, its men take Chevrolet Plant No. 4.", "That's where the engines for every Chevrolet are made.")
L('d2', 'n36', "In December, General Motors built fifty thousand cars. In February, it builds a hundred and twenty-five.", "In December, General Motors built 50,000 cars.", "In February, it builds 125.")
L('d2', 'n37', "Can they actually win?", "Can they actually win?")

# ── Day 3: 11 Feb 1937 ──
L('d3', 'n38', "It's the eleventh of February, nineteen thirty-seven. Day forty-four.", "It's 11 February 1937.", "Day 44.")
L('d3', 'n39', "With the governor carrying messages between the two sides, General Motors and the union sign an agreement. It is one page long. For the first time, General Motors recognizes the United Auto Workers as the bargaining agent for its members.",
  "With the governor carrying messages between the two sides,", "General Motors and the union sign an agreement. It is one page long.", "For the first time, General Motors recognizes the United Auto Workers", "as the bargaining agent for its members.")
L('d3', 'n40', "The strikers parade out of the plants, victorious. Some of them have not been home in six weeks.", "The strikers parade out of the plants, victorious.", "Some of them have not been home in six weeks.")
L('d3', 'n41', "The strike has idled a hundred and thirty-six thousand General Motors workers, and left two hundred and eighty thousand cars unbuilt. And it changes everything that comes after.",
  "The strike has idled 136,000 General Motors workers,", "and left 280,000 cars unbuilt.", "And it changes everything that comes after.")
L('d3', 'n42', "In February, the United Auto Workers has eighty-eight thousand members. By October, it has four hundred thousand.", "In February, the United Auto Workers has 88,000 members.", "By October, it has 400,000.")
L('d3', 'n43', "What follows are the good years. During the Second World War, Flint's plants build for the war. Women take their places on the lines.", "What follows are the good years.", "During the Second World War, Flint's plants build for the war.", "Women take their places on the lines.")
L('d3', 'n44', "After it, the cars come back bigger than ever. A factory job in Flint means a house, a car, and a pension.", "After it, the cars come back bigger than ever.", "A factory job in Flint means a house, a car, and a pension.")
L('d3', 'n45', "By nineteen sixty, Flint has almost a hundred and ninety-seven thousand people. More than it has ever had, or ever will.", "By 1960, Flint has almost 197,000 people.", "More than it has ever had, or ever will.")
L('d3', 'n46', "How long can it last?", "How long can it last?")

# ── Day 4: 1978 ──
L('d4', 'n47', "It's nineteen seventy-eight. The top.", "It's 1978. The top.")
L('d4', 'n48', "About eighty thousand people in and around Flint work for General Motors. Buick, Chevrolet, Fisher Body, AC.",
  "About 80,000 people in and around Flint work for General Motors.", "Buick, Chevrolet, Fisher Body, AC.")
L('d4', 'n49', "Across America, General Motors employs more people than any other private company. At its peak, in nineteen seventy-nine, more than six hundred and eighteen thousand.",
  "Across America, General Motors employs more people than any other private company.", "At its peak, in 1979, more than 618,000.")
L('d4', 'n50', "But the cracks are already there. Smaller, cheaper imported cars are selling. In nineteen seventy-eight, imports are eighteen percent of the American market. Two years later, more than a quarter.",
  "But the cracks are already there. Smaller, cheaper imported cars are selling.", "In 1978, imports are 18% of the American market.", "Two years later, more than a quarter.")
L('d4', 'n51', "General Motors builds new plants in other states, and in Mexico. Flint's old factories close, one after another.", "General Motors builds new plants in other states, and in Mexico.", "Flint's old factories close, one after another.")
L('d4', 'n52', "In nineteen eighty-nine, a filmmaker from Flint, Michael Moore, makes a film about it, Roger and Me, following his attempts to talk to the chairman of General Motors. Many people see Flint for the first time, as a place that has been left behind.",
  "In 1989, a filmmaker from Flint, Michael Moore, makes a film about it,", "“Roger & Me”, following his attempts to talk to the chairman of General Motors.", "Many people see Flint for the first time,", "as a place that has been left behind.")
L('d4', 'n53', "General Motors says it has to cut costs to survive the competition. The workers say they did everything that was asked of them. Both are telling the truth as they see it.",
  "General Motors says it has to cut costs to survive the competition.", "The workers say they did everything that was asked of them.", "Both are telling the truth as they see it.")
L('d4', 'n54', "By nineteen eighty, Flint is down to a hundred and sixty thousand people. And still falling.", "By 1980, Flint is down to 160,000 people.", "And still falling.")
L('d4', 'n55', "What happens when the jobs go?", "What happens when the jobs go?")

# ── Day 5: 29 June 1999 ──
L('d5', 'n56', "It's the twenty-ninth of June, nineteen ninety-nine. Buick City.", "It's 29 June 1999. Buick City.")
L('d5', 'n57', "This is the old Buick works, the same ground on the north side where Billy Durant built Buicks ninety years ago, rebuilt in the nineteen eighties as one giant modern plant.",
  "This is the old Buick works, the same ground on the north side", "where Billy Durant built Buicks ninety years ago,", "rebuilt in the 1980s as one giant modern plant.")
L('d5', 'n58', "The last Buick LeSabre is coming down the line. When it's done, Buick will no longer build cars in Flint, the city where it began.", "The last Buick LeSabre is coming down the line.", "When it's done, Buick will no longer build cars in Flint,", "the city where it began.")
L('d5', 'n59', "General Motors announced the closing two years ago. Sales of big sedans are falling. Only about twelve hundred workers are left.", "General Motors announced the closing two years ago.", "Sales of big sedans are falling. Only about 1,200 workers are left.")
L('d5', 'n60', "And here is the part that's hard to believe. This same year, Buick City wins J.D. Power's Platinum Award, for the quality of its plant.", "And here is the part that's hard to believe.", "This same year, Buick City wins J.D. Power's Platinum Award,", "for the quality of its plant.")
L('d5', 'n61', "Ten years earlier, a LeSabre built here was ranked the top car in J.D. Power's quality rankings. The first American-built car ever to make that list.", "Ten years earlier, a LeSabre built here was ranked the top car", "in J.D. Power's quality rankings.", "The first American-built car ever to make that list.")
L('d5', 'n62', "Being the best was not enough.", "Being the best was not enough.")
L('d5', 'n63', "By now, General Motors employs about thirty-three thousand people in Flint. Down from eighty thousand. And it will keep falling, to under eight thousand.", "By now, General Motors employs about 33,000 people in Flint.", "Down from 80,000.", "And it will keep falling, to under 8,000.")
L('d5', 'n64', "What is Flint, without its factories?", "What is Flint, without its factories?")

# ── Day 6: October 2014 ──
L('d6', 'n65', "It's October, two thousand and fourteen.", "It's October 2014.")
L('d6', 'n66', "Flint is short of money, and the state of Michigan has put it under an emergency manager, appointed by the governor, with power over the city's decisions.", "Flint is short of money, and the state of Michigan has put it under", "an emergency manager, appointed by the governor,", "with power over the city's decisions.")
L('d6', 'n67', "Six months ago, in April, to save money, the city stopped buying its water from Detroit, and started drawing it from the Flint River. It was meant to be temporary, until a new pipeline was built.",
  "Six months ago, in April, to save money,", "the city stopped buying its water from Detroit,", "and started drawing it from the Flint River.", "It was meant to be temporary, until a new pipeline was built.")
L('d6', 'n68', "The river water is not treated to control corrosion. And it is eating away at the old pipes.", "The river water is not treated to control corrosion.", "And it is eating away at the old pipes.")
L('d6', 'n69', "At General Motors' Flint engine plant, the company notices first. The water is corroding engine parts. So General Motors gets permission to stop using it, and switches to another supply.",
  "At General Motors' Flint engine plant, the company notices first.", "The water is corroding engine parts.", "So General Motors gets permission to stop using it,", "and switches to another supply.")
L('d6', 'q02', "Ronald Jamison had worked at that plant for thirty-nine years. They told Flint, he said, you're causing us to lose engines.", "Ronald Jamison had worked at that plant for 39 years.", "“They told Flint… you're causing us to lose engines.”")
L('d6', 'q03', "Matter of fact, they took all the water fountains out of the plant. We have all water coolers throughout the plant.", "“Matter of fact, they took all the water fountains out of the plant.", "We have all water coolers throughout the plant.”")
L('d6', 'n70', "The people of Flint stay on the river water for another year.", "The people of Flint stay on the river water for another year.")
L('d6', 'n71', "In September twenty fifteen, a local doctor, Mona Hanna-Attisha, shows that more of the city's children have lead in their blood. In October, Flint switches back to Detroit's water.",
  "In September 2015, a local doctor, Mona Hanna-Attisha,", "shows that more of the city's children have lead in their blood.", "In October, Flint switches back to Detroit's water.")
L('d6', 'n72', "By then, lead from the old pipes has reached the taps. An outbreak of Legionnaires' disease, linked to the water, kills at least twelve people.", "By then, lead from the old pipes has reached the taps.", "An outbreak of Legionnaires' disease, linked to the water,", "kills at least 12 people.")
L('d6', 'n73', "In January twenty sixteen, the National Guard comes to Flint again. Not to protect strikers, this time. To carry bottled water and filters, door to door.", "In January 2016, the National Guard comes to Flint again.", "Not to protect strikers, this time.", "To carry bottled water and filters, door to door.")
L('d6', 'n74', "Officials, including two former emergency managers, are charged with crimes. In twenty twenty-one, a judge approves a settlement of six hundred and twenty-six million dollars, most of it paid by the state, most of it for the children.",
  "Officials, including two former emergency managers, are charged with crimes.", "In 2021, a judge approves a settlement of $626 million,", "most of it paid by the state, most of it for the children.")
L('d6', 'n75', "Is anything left?", "Is anything left?")

# ── Today ──
L('today', 'n76', "Today, Flint has eighty-one thousand people. Fewer than half as many as in nineteen sixty.", "Today, Flint has 81,000 people.", "Fewer than half as many as in 1960.")
L('today', 'n77', "But General Motors still builds trucks here. Flint Assembly, its oldest working assembly plant in North America, makes heavy-duty pickups, with more than four thousand people on the line.",
  "But General Motors still builds trucks here.", "Flint Assembly, its oldest working assembly plant in North America,", "makes heavy-duty pickups, with more than 4,000 people on the line.")
L('today', 'n78', "Chevy in the Hole, where Chevrolet's plants stood, and where the strikers took Plant Number Four, is now a park by the river. Chevy Commons.", "Chevy in the Hole, where Chevrolet's plants stood,", "and where the strikers took Plant No. 4,", "is now a park by the river: Chevy Commons.")
L('today', 'n79', "And on the Buick City ground, where Billy Durant's first factory grew, new industrial buildings are going up. Ground was broken in twenty twenty-three.", "And on the Buick City ground, where Billy Durant's first factory grew,", "new industrial buildings are going up.", "Ground was broken in 2023.")
L('today', 'n80', "So what did winning buy? Decades of union wages, pensions and health care, for hundreds of thousands of families.", "So what did winning buy?", "Decades of union wages, pensions and health care,", "for hundreds of thousands of families.")
L('today', 'n81', "And what couldn't it protect? It couldn't keep the company in the city. It couldn't decide where the next plant would be built. And it couldn't stop a decision about the water.",
  "And what couldn't it protect?", "It couldn't keep the company in the city.", "It couldn't decide where the next plant would be built.", "And it couldn't stop a decision about the water.")
L('today', 'n82', "Ninety years ago, a group of workers sat down in a car-body plant in Flint, and refused to leave.", "Ninety years ago, a group of workers sat down", "in a car-body plant in Flint, and refused to leave.")
L('today', 'q04', "She's ours, one of them shouted. For forty-four days, it was.", "“She's ours,” one of them shouted.", "For 44 days, it was.")
L('today', 'n83', "Did your family build cars in Flint? Or carry a union card? Tell us in the comments. We read every one.", "Did your family build cars in Flint? Or carry a union card?", "Tell us in the comments. We read every one.")
L('today', 'n84', "Next Sunday: Sears.", "Next Sunday: Sears.")

MAXC = 64
def split(s):
    if len(s) <= MAXC: return [s]
    mid = len(s) // 2; best = None
    for j, ch in enumerate(s):
        if ch == ' ' and 12 < j < len(s) - 12:
            score = abs(j - mid) - (14 if s[j - 1] in ',.:;' else 0)
            if best is None or score < best[0]: best = (score, j)
    if best is None: return [s]
    return split(s[:best[1]]) + split(s[best[1] + 1:])
out = [{'id': i, 'chapter': ch, 'voice': V, 'speed': 0.95, 'text': sp, 'subs': [p for s in subs for p in split(s)]} for ch, i, sp, subs in C]
os.makedirs(os.path.join(D, 'audio'), exist_ok=True)
open(os.path.join(D, 'audio/lines.json'), 'w', encoding='utf-8').write('[\n' + ',\n'.join('  ' + json.dumps(l, ensure_ascii=False) for l in out) + '\n]\n')
TITLES = {'open': 'Cold open · 30 December 1936', 'd1': 'Day 1 · 16 September 1908', 'd2': 'Day 2 · 30 December 1936', 'd3': 'Day 3 · 11 February 1937',
          'd4': 'Day 4 · 1978', 'd5': 'Day 5 · 29 June 1999', 'd6': 'Day 6 · October 2014', 'today': 'Today'}
md, prev = ['# Script: What Happened to Flint, Michigan? The Town GM Built', '', 'Narration by Storyteller Oxley. Lines starting with q are read over a quote card. Every fact is in FACTS.md.', ''], None
for l in out:
    if l['chapter'] != prev: md += ['', '## ' + TITLES[l['chapter']], '']; prev = l['chapter']
    md.append(f"{l['id'].upper()}. " + ' '.join(l['subs']))
open(os.path.join(D, 'script.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
n = sum(len(l['text']) for l in out); w = sum(len(l['text'].split()) for l in out)
print(len(out), 'lines', w, 'words', n, 'characters; longest caption', max(len(s) for l in out for s in l['subs']))
