#!/bin/sh
# Archive material for "What Happened to Flint, Michigan?" — public domain or CC BY only (licences logged in SOURCES.jsonl).
cd "$(dirname "$0")/.." || exit 1
PY=${PY:-python -I}
F="$PY tools/footage.py fetch"
big() {   # name, commons file title, credit, licence, width
  ls raw/$1.* >/dev/null 2>&1 && return 0
  enc=$($PY -c "import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1].replace(' ','_')))" "$2")
  $F "https://commons.wikimedia.org/wiki/Special:FilePath/$enc?width=${5:-2600}" --name "$1" \
    --page "https://commons.wikimedia.org/wiki/File:$enc" --license "$4" --credit "$3"; sleep 2
}
SD="Sheldon Dick, Farm Security Administration, 1937 (Library of Congress)"
big strike_window "Flint Sit-Down Strike window.jpg" "$SD" "Public domain" 3600
big strike_entrance "Flint-Strike-1937.jpg" "$SD" "Public domain" 742
big strike_meal "Flint Sit-Down Strike meal.jpg" "$SD" "Public domain" 1024
big strike_sleeping "Flint Sit-Down Strike sleeping.jpg" "$SD" "Public domain" 951
big strike_sitdowners "Sitdown strikers in the Fisher body plant factory number three. Flint, Michigan.jpg" "$SD" "Public domain" 932
big guard_gun "Flint Sit-Down Strike National Guard.jpg" "$SD" "Public domain" 978
big guard_drill1 "Nation Guard drilling at Flint school during 1937 strike 1.jpg" "National Guard at a Flint school, 1937" "Public domain" 2344
big guard_drill3 "Nation Guard drilling at Flint school during 1937 strike 3.jpg" "National Guard at a Flint school, 1937" "Public domain" 2344
big women_flint "Women of Flint.jpg" "Joseph Vavak, 1937" "Public domain" 2000
big durant1916 "WilliamCDurant.jpg" "William C. Durant, c. 1916" "Public domain" 487
big durant_bain "W.C. Durant, motor magnate, & wife - photo by Bain News Service, New York. LCCN90711046.jpg" "Bain News Service, 1926 (Library of Congress)" "Public domain" 2600
big dort "Photo of Josiah Dallas Dort.png" "National Cyclopaedia of American Biography, 1920" "Public domain" 298
big buick1907 "Buick motor works flint 1907.jpg" "Buick Motor Works, Flint, 1907" "Public domain" 1500
big buick1906 "Buick motor co factory flint.jpg" "Buick factory, Flint, c. 1906" "Public domain" 896
big buick_postcard "Buick factory and offices flint.jpg" "Postcard, c. 1910s" "Public domain" 683
big buick_whistle "When the Whistle Blows at the Buick.jpg" "Postcard, 1912 (Burton Historical Collection, Detroit Public Library)" "Public domain" 1500
big buick_city1950 "Buick City (1950).jpg" "Buick works, aerial, c. 1950" "Public domain" 3000
big vehicle_city "Flint Vehicle City.jpg" "Postcard, 1906 (Burton Historical Collection, Detroit Public Library)" "Public domain" 1500
big saginaw1910 "RPPC Sagniaw Street Flint Mich.jpg" "Real-photo postcard, Saginaw Street, c. 1910" "Public domain" 3600
big kearsley1909 "Kearsley Street, Flint, Michigan postcard - DPLA - 0864bb59f3661a11c68e29566ade4351 (page 1).jpg" "Postcard, 1909 (DPLA)" "Public domain" 2236
big wagon_works "Flint Wagon Works.png" "Flint Wagon Works, 1912 (Detroit Public Library)" "Public domain" 508
big carriage_office "Durant Dort Carriage Co Office.jpg" "Ralph J. Christian, 1977" "Public domain" 1304
big map1955 "Flint, Michigan 1955 Yellow Book.jpg" "Public Roads Administration, 1955" "Public domain" 800
big map1947 "Flint MI 1947 (8395801128).jpg" "Fred Johnson Maps, 1947; scan davecito (CC BY 2.0)" "CC BY 2.0" 1144
big dompolski1980 "Dom Polski, Saginaw Street, Flint, Michigan LCCN2017706233.tif" "John Margolies, 1980 (Library of Congress)" "Public domain" 2600
big ac_women1942 "A woman's place is on the production line 8b07409v.jpg" "Ann Rosener, OWI, 1942 (Library of Congress)" "Public domain" 1024
big ac_women1942b "With swift, deft movements, this young worker 8b07408v.jpg" "Ann Rosener, OWI, 1942 (Library of Congress)" "Public domain" 1024
big ac_demolition "AC Spark Plug, Flint Michigan (3308627798).jpg" "abarndweller, 2009 (CC BY 2.0)" "CC BY 2.0" 1600
big epa_testing "EPA water quality testing in Flint.jpg" "U.S. EPA, 2016" "Public domain" 2560
big epa_tower "Flint-water-treatment-plant-tower.jpg" "U.S. EPA, 2016" "Public domain" 2560
big obama_water "President Obama sips filtered water from Flint.jpg" "Pete Souza, White House, 4 May 2016" "Public domain" 2600
big usda_water "Genesee County Community Action Resource Department (GCCARD) partners with USDA to help Flint, MI - TEFAP and CSFP (20161004-FNS-LSC-0039).jpg" "USDA, 4 Oct 2016" "Public domain" 2600
big chevy_commons_ground "Speaking at groundbreaking for Chevy Commons Community green space in Flint. (17057806178).jpg" "Office of Sen. Debbie Stabenow, 2015 (CC BY 2.0)" "CC BY 2.0" 1536
SB="Sanborn Map Company (Library of Congress)"
SBF="Sanborn Fire Insurance Map from Flint, Genesee County, Michigan. LOC sanborn04009"
big sanborn1886 "$SBF 001-1.jpg" "$SB, Feb 1886" "Public domain" 3400
big sanborn1909_index "$SBF 005-1.jpg" "$SB, Nov 1909" "Public domain" 3400
big sanborn1909_buick "$SBF 005-34.jpg" "$SB, Nov 1909" "Public domain" 3400
big sanborn1909_buick2 "$SBF 005-35.jpg" "$SB, Nov 1909" "Public domain" 3400
NG="The National Guard, Jan 2016 (CC BY 2.0)"
big guard2016_door "Michigan National Guard (23874993203).jpg" "$NG" "CC BY 2.0" 1632
big guard2016_site "Michigan National Guard (24372794412).jpg" "$NG" "CC BY 2.0" 2600
big guard2016_site2 "Michigan National Guard (24185515550).jpg" "$NG" "CC BY 2.0" 2600
