#!/usr/bin/env python3
"""Add individuals for CQ-151 to CQ-200 to create JTO v1.7"""

OWL_FILE = "/home/claude/tourism-ontology/jto_tourism_entity_module_v1_7_stable.owl"
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

NEW_INDIVIDUALS = """
  <!-- ====== JTO v1.7 — New Individuals for CQ-151 to CQ-200 ====== -->

  <!-- CQ-154: Swimming season -->
  <rdf:Description rdf:about="{ns}AqabaSwimmingSeason">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SwimmingSeason"/>
    <jto:startMonth>March</jto:startMonth>
    <jto:endMonth>November</jto:endMonth>
    <jto:waterTemperatureMin rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">21.0</jto:waterTemperatureMin>
    <jto:waterTemperatureMax rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">28.0</jto:waterTemperatureMax>
    <rdfs:comment xml:lang="en">Aqaba Red Sea swimming season runs March through November with water temperatures between 21-28°C.</rdfs:comment>
    <rdfs:label xml:lang="en">Aqaba Swimming Season</rdfs:label>
    <rdfs:label xml:lang="ar">موسم السباحة في العقبة</rdfs:label>
  </rdf:Description>

  <!-- CQ-155: Snow conditions -->
  <rdf:Description rdf:about="{ns}AmmanSnowConditions">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SnowCondition"/>
    <jto:snowMonths>December to February</jto:snowMonths>
    <jto:frequency>Rare (1-3 times per winter)</jto:frequency>
    <rdfs:comment xml:lang="en">Amman occasionally receives snowfall between December and February. Roads may close temporarily. Higher elevations like Ajloun see more frequent snow.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Snow Conditions</rdfs:label>
    <rdfs:label xml:lang="ar">ظروف الثلوج في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-156: Mount Nebo biblical viewpoint -->
  <rdf:Description rdf:about="{ns}MountNeboViewpoint">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}BiblicalViewpoint"/>
    <jto:locatedAt rdf:resource="{ns}MountNeboSite"/>
    <jto:biblicalSignificance>Where Moses viewed the Promised Land before his death (Deuteronomy 34)</jto:biblicalSignificance>
    <rdfs:comment xml:lang="en">Mount Nebo offers panoramic views of the Dead Sea, Jordan Valley, and on clear days, Jerusalem. Sacred site where Moses is believed to have seen the Promised Land.</rdfs:comment>
    <rdfs:label xml:lang="en">Mount Nebo Biblical Viewpoint</rdfs:label>
    <rdfs:label xml:lang="ar">المنظر التوراتي من جبل نيبو</rdfs:label>
  </rdf:Description>

  <!-- CQ-158: Lot's Cave -->
  <rdf:Description rdf:about="{ns}LotsCaveMuseum">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}LotsCave"/>
    <jto:locatedIn rdf:resource="{ns}DeadSeaArea"/>
    <jto:entryFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.00</jto:entryFee>
    <jto:historicalPeriod>Early Bronze Age / Biblical</jto:historicalPeriod>
    <rdfs:comment xml:lang="en">Archaeological site and museum near the Dead Sea. Believed to be where Lot and his daughters took refuge. Contains Byzantine church ruins and Early Bronze Age artifacts.</rdfs:comment>
    <rdfs:label xml:lang="en">Lot's Cave and Museum</rdfs:label>
    <rdfs:label xml:lang="ar">كهف لوط والمتحف</rdfs:label>
  </rdf:Description>

  <!-- CQ-159: Pilgrimage route -->
  <rdf:Description rdf:about="{ns}JordanPilgrimageRoute">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PilgrimageRoute"/>
    <jto:routeStops>Bethany Beyond Jordan, Mount Nebo, Madaba (St George Church), Lot's Cave, Umm ar-Rasas</jto:routeStops>
    <jto:durationDays rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">3</jto:durationDays>
    <rdfs:comment xml:lang="en">A 3-day pilgrimage route covering Jordan's major biblical and holy sites, from Bethany to Madaba and beyond.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Pilgrimage Route</rdfs:label>
    <rdfs:label xml:lang="ar">مسار الحج في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-160: Holy Land sites -->
  <rdf:Description rdf:about="{ns}UmmArRasas">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}HolyLandSite"/>
    <jto:unescoInscriptionYear rdf:datatype="http://www.w3.org/2001/XMLSchema#gYear">2004</jto:unescoInscriptionYear>
    <jto:entryFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2.00</jto:entryFee>
    <rdfs:comment xml:lang="en">UNESCO World Heritage Site with remarkable Byzantine mosaic floors. Contains ruins of Roman, Byzantine and Early Muslim civilizations.</rdfs:comment>
    <rdfs:label xml:lang="en">Umm ar-Rasas</rdfs:label>
    <rdfs:label xml:lang="ar">أم الرصاص</rdfs:label>
  </rdf:Description>

  <!-- CQ-162: Adults-only resort -->
  <rdf:Description rdf:about="{ns}DeadSeaAdultsOnlyResort">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}AdultsOnlyResort"/>
    <jto:locatedIn rdf:resource="{ns}DeadSeaArea"/>
    <jto:pricePerNight rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">250.00</jto:pricePerNight>
    <jto:hasSpa rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasSpa>
    <jto:minimumAge rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">18</jto:minimumAge>
    <rdfs:comment xml:lang="en">Premium adults-only resort at the Dead Sea with full spa, private beach access, and infinity pool overlooking the Dead Sea.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Adults-Only Spa Resort</rdfs:label>
    <rdfs:label xml:lang="ar">منتجع البحر الميت للبالغين فقط</rdfs:label>
  </rdf:Description>

  <!-- CQ-163: Couples activities -->
  <rdf:Description rdf:about="{ns}PetraCandlelitDinnerActivity">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}RomanticActivity"/>
    <jto:availableAt rdf:resource="{ns}PetraSite"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">120.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Private candlelit dinner in the Petra Siq with traditional Jordanian cuisine and live music.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Candlelit Dinner for Couples</rdfs:label>
    <rdfs:label xml:lang="ar">عشاء على ضوء الشموع في البتراء للأزواج</rdfs:label>
  </rdf:Description>

  <!-- CQ-164: Honeymoon packages -->
  <rdf:Description rdf:about="{ns}JordanHoneymoonPackage">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}TourPackage"/>
    <jto:packagePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">1500.00</jto:packagePrice>
    <jto:packageDuration>7 days</jto:packageDuration>
    <jto:destinationsIncluded>Amman, Dead Sea, Petra, Wadi Rum, Aqaba</jto:destinationsIncluded>
    <jto:includesMeals rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:includesMeals>
    <jto:includesTransport rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:includesTransport>
    <rdfs:comment xml:lang="en">7-day luxury honeymoon package covering Amman, Dead Sea spa, Petra by Night, Wadi Rum glamping, and Aqaba beach.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Honeymoon Package</rdfs:label>
    <rdfs:label xml:lang="ar">باقة شهر العسل في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-165: Private beach -->
  <rdf:Description rdf:about="{ns}KempinskiPrivateBeach">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PrivateBeach"/>
    <jto:locatedAt rdf:resource="{ns}KempinskiDeadSea"/>
    <jto:guestsOnly rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:guestsOnly>
    <rdfs:comment xml:lang="en">Private Dead Sea beach exclusively for Kempinski Ishtar hotel guests with mud station and shower facilities.</rdfs:comment>
    <rdfs:label xml:lang="en">Kempinski Private Dead Sea Beach</rdfs:label>
    <rdfs:label xml:lang="ar">شاطئ كمبنسكي الخاص في البحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-169: Bargaining tips -->
  <rdf:Description rdf:about="{ns}JordanBargainingGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ShoppingEtiquette"/>
    <jto:hagglingExpected rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hagglingExpected>
    <jto:settingType>souks and markets</jto:settingType>
    <jto:notes>Start at 50-60% of asking price. Be friendly and patient. Walk away if price is too high — seller may call you back. Fixed prices in malls and supermarkets.</jto:notes>
    <rdfs:comment xml:lang="en">Bargaining tips for Jordan's markets and souks. Haggling is expected and part of the shopping culture.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Bargaining Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل المساومة في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-171: Spa and wellness Dead Sea -->
  <rdf:Description rdf:about="{ns}DeadSeaSpaExperience">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WellnessActivity"/>
    <jto:availableAt rdf:resource="{ns}DeadSeaArea"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">80.00</jto:activityPrice>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.0</jto:activityDuration>
    <rdfs:comment xml:lang="en">Full spa experience at the Dead Sea including mineral mud wrap, salt scrub, and mineral pool soak. Uses natural Dead Sea minerals.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Spa Experience</rdfs:label>
    <rdfs:label xml:lang="ar">تجربة سبا البحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-172: Hot springs Ma'in -->
  <rdf:Description rdf:about="{ns}MainHotSprings">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}HotSpring"/>
    <jto:waterTemperature rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">63.0</jto:waterTemperature>
    <jto:entryFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">20.00</jto:entryFee>
    <rdfs:comment xml:lang="en">Natural hot springs at Ma'in with therapeutic mineral-rich waters heated by underground lava. Water temperature reaches 63°C at source, cooled at bathing pools.</rdfs:comment>
    <rdfs:label xml:lang="en">Ma'in Hot Springs</rdfs:label>
    <rdfs:label xml:lang="ar">حمامات ماعين الساخنة</rdfs:label>
  </rdf:Description>

  <!-- CQ-173: Yoga retreat -->
  <rdf:Description rdf:about="{ns}DeadSeaYogaRetreat">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WellnessActivity"/>
    <jto:availableAt rdf:resource="{ns}DeadSeaArea"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">5.0</jto:activityDuration>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">45.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Yoga and meditation retreat at the Dead Sea. Sessions at sunrise overlooking the lowest point on Earth.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Yoga Retreat</rdfs:label>
    <rdfs:label xml:lang="ar">معتكف يوغا البحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-174: Mud treatment -->
  <rdf:Description rdf:about="{ns}DeadSeaMudTherapy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WellnessActivity"/>
    <jto:availableAt rdf:resource="{ns}DeadSeaArea"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">15.00</jto:activityPrice>
    <jto:healthBenefits>Skin conditions (psoriasis, eczema), joint pain, muscle relaxation, improved circulation</jto:healthBenefits>
    <rdfs:comment xml:lang="en">Natural Dead Sea mineral mud treatment. Applied to skin and left to dry for 15-20 minutes before rinsing. Rich in magnesium, calcium, and potassium.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Mud Therapy</rdfs:label>
    <rdfs:label xml:lang="ar">علاج طين البحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-175: Aqaba Ironman -->
  <rdf:Description rdf:about="{ns}AqabaIronman">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}IronmanEvent"/>
    <jto:locatedIn rdf:resource="{ns}Aqaba"/>
    <jto:eventMonth>November</jto:eventMonth>
    <rdfs:comment xml:lang="en">IRONMAN 70.3 Aqaba — annual triathlon event featuring a 1.9km swim in the Red Sea, 90km bike ride, and 21.1km run through the desert landscape.</rdfs:comment>
    <rdfs:label xml:lang="en">IRONMAN 70.3 Aqaba</rdfs:label>
    <rdfs:label xml:lang="ar">آيرونمان 70.3 العقبة</rdfs:label>
  </rdf:Description>

  <!-- CQ-176: Marathon / running events -->
  <rdf:Description rdf:about="{ns}DeadSeaUltraMarathon">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SportEvent"/>
    <jto:locatedIn rdf:resource="{ns}DeadSeaArea"/>
    <jto:eventMonth>April</jto:eventMonth>
    <rdfs:comment xml:lang="en">Dead Sea Ultra Marathon — annual running event at the lowest point on Earth. Distances from 10K to 50K along the Dead Sea shore.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Ultra Marathon</rdfs:label>
    <rdfs:label xml:lang="ar">ماراثون البحر الميت الفائق</rdfs:label>
  </rdf:Description>

  <!-- CQ-177: Outdoor sports -->
  <rdf:Description rdf:about="{ns}JordanRockClimbing">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}AdventureActivity"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <jto:difficultyLevel>Moderate to Advanced</jto:difficultyLevel>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">60.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Rock climbing in Wadi Rum's sandstone formations. Routes for all levels, guided by local Bedouin climbers.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Rock Climbing</rdfs:label>
    <rdfs:label xml:lang="ar">تسلق الصخور في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-178: Art gallery Amman -->
  <rdf:Description rdf:about="{ns}DaratAlFununGallery">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ArtGallery"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:entryFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.00</jto:entryFee>
    <rdfs:comment xml:lang="en">Darat al Funun — leading contemporary art gallery in Amman set in renovated 1920s houses on Jabal al-Weibdeh. Free entry, rotating exhibitions.</rdfs:comment>
    <rdfs:label xml:lang="en">Darat al Funun Art Gallery</rdfs:label>
    <rdfs:label xml:lang="ar">دارة الفنون</rdfs:label>
  </rdf:Description>

  <!-- CQ-179: Music and nightlife Amman -->
  <rdf:Description rdf:about="{ns}AmmanNightlife">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Nightlife"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <rdfs:comment xml:lang="en">Amman's nightlife centers around Abdoun, Jabal Amman (Rainbow Street), and Jabal al-Weibdeh. Live music venues, rooftop bars, and jazz clubs. Most venues open until 2 AM.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Nightlife Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل الحياة الليلية في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-180: Festivals and cultural events -->
  <rdf:Description rdf:about="{ns}JerashFestival">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}CulturalFestival"/>
    <jto:locatedIn rdf:resource="{ns}Jerash"/>
    <jto:eventMonth>July-August</jto:eventMonth>
    <jto:entryFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">10.00</jto:entryFee>
    <rdfs:comment xml:lang="en">Jerash Festival of Culture and Arts — annual summer festival held in the ancient Roman ruins featuring music, dance, theater, and poetry from Jordan and the Arab world.</rdfs:comment>
    <rdfs:label xml:lang="en">Jerash Festival of Culture and Arts</rdfs:label>
    <rdfs:label xml:lang="ar">مهرجان جرش للثقافة والفنون</rdfs:label>
  </rdf:Description>

  <!-- CQ-188: Google Maps / Waze -->
  <rdf:Description rdf:about="{ns}GoogleMapsJordan">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}NavigationApp"/>
    <jto:worksOffline rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:worksOffline>
    <jto:appName>Google Maps</jto:appName>
    <rdfs:comment xml:lang="en">Google Maps works well in Jordan's cities. Download offline maps for desert areas. Limited public transit data outside Amman.</rdfs:comment>
    <rdfs:label xml:lang="en">Google Maps in Jordan</rdfs:label>
    <rdfs:label xml:lang="ar">خرائط جوجل في الأردن</rdfs:label>
  </rdf:Description>

  <rdf:Description rdf:about="{ns}WazeJordan">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}NavigationApp"/>
    <jto:worksOffline rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">false</jto:worksOffline>
    <jto:appName>Waze</jto:appName>
    <rdfs:comment xml:lang="en">Waze is popular among Jordanians for real-time traffic and police checkpoint alerts. Best for driving in Amman traffic. Requires mobile data.</rdfs:comment>
    <rdfs:label xml:lang="en">Waze in Jordan</rdfs:label>
    <rdfs:label xml:lang="ar">ويز في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-190: Travel booking apps -->
  <rdf:Description rdf:about="{ns}JordanESimApp">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}TelecomService"/>
    <jto:appName>Airalo</jto:appName>
    <rdfs:comment xml:lang="en">eSIM service for Jordan via Airalo app. Provides mobile data without physical SIM card. Plans from 1GB to 20GB for 7-30 days.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan eSIM (Airalo)</rdfs:label>
    <rdfs:label xml:lang="ar">شريحة إلكترونية للأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-197: First-time visitor itinerary -->
  <rdf:Description rdf:about="{ns}FirstTimeVisitorItinerary">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FirstTimeVisitor"/>
    <jto:recommendedDays rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">7</jto:recommendedDays>
    <jto:mustSeeAttractions>Amman Citadel, Petra, Wadi Rum, Dead Sea, Jerash</jto:mustSeeAttractions>
    <rdfs:comment xml:lang="en">Recommended 7-day itinerary for first-time visitors: Day 1-2 Amman, Day 3 Jerash, Day 4-5 Petra, Day 6 Wadi Rum, Day 7 Dead Sea.</rdfs:comment>
    <rdfs:label xml:lang="en">First-Time Visitor 7-Day Itinerary</rdfs:label>
    <rdfs:label xml:lang="ar">خط سير 7 أيام للزائر لأول مرة</rdfs:label>
  </rdf:Description>
""".replace("{ns}", NS)

with open(OWL_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

insert_point = content.rfind('</rdf:RDF>')
new_content = content[:insert_point] + NEW_INDIVIDUALS + "\n" + content[insert_point:]

with open(OWL_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

import subprocess
result = subprocess.run(['wc', '-l', OWL_FILE], capture_output=True, text=True)
print(f"v1.7 created: {result.stdout.strip()}")

import xml.etree.ElementTree as ET
tree = ET.parse(OWL_FILE)
root = tree.getroot()
rdf_ns = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
ni_uri = 'http://www.w3.org/2002/07/owl#NamedIndividual'
count = sum(1 for d in root.findall(f'{rdf_ns}Description') for t in d.findall(f'{rdf_ns}type') if t.get(f'{rdf_ns}resource') == ni_uri)
print(f"XML valid ✅ · Named individuals: {count}")
