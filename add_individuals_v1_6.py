#!/usr/bin/env python3
"""Add individuals for CQ-091 to CQ-150 to create JTO v1.6"""

import re

OWL_FILE = "/home/claude/tourism-ontology/jto_tourism_entity_module_v1_6_stable.owl"
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

# New individuals needed for CQ-091 to CQ-150
NEW_INDIVIDUALS = """
  <!-- CQ-091: Wildlife activity at Shaumari Reserve -->
  <rdf:Description rdf:about="{ns}ShaumariWildlifeSafari">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WildlifeActivity"/>
    <jto:availableAt rdf:resource="{ns}ShaumariReserve"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.0</jto:activityDuration>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">15.00</jto:activityPrice>
    <jto:difficultyLevel>Easy</jto:difficultyLevel>
    <jto:isSuitableForChildren rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:isSuitableForChildren>
    <rdfs:comment xml:lang="en">Guided safari through Shaumari Reserve to see Arabian Oryx, ostriches, and gazelles in their natural habitat.</rdfs:comment>
    <rdfs:label xml:lang="en">Shaumari Wildlife Safari</rdfs:label>
    <rdfs:label xml:lang="ar">رحلة سفاري الحياة البرية في الشومري</rdfs:label>
    <jto:officialName xml:lang="en">Shaumari Wildlife Safari</jto:officialName>
    <jto:officialName xml:lang="ar">رحلة سفاري الحياة البرية في الشومري</jto:officialName>
  </rdf:Description>

  <!-- CQ-093: Wildlife safari -->
  <rdf:Description rdf:about="{ns}AzraqWetlandBirdSafari">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WildlifeSafari"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">4.0</jto:activityDuration>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">12.00</jto:activityPrice>
    <jto:bestSeason>Spring (March-May)</jto:bestSeason>
    <rdfs:comment xml:lang="en">Birding safari at Azraq Wetland Reserve, home to migratory birds and endemic species.</rdfs:comment>
    <rdfs:label xml:lang="en">Azraq Wetland Bird Safari</rdfs:label>
    <rdfs:label xml:lang="ar">رحلة سفاري طيور الأزرق</rdfs:label>
    <jto:officialName xml:lang="en">Azraq Wetland Bird Safari</jto:officialName>
  </rdf:Description>

  <!-- CQ-096: Christmas in Jordan -->
  <rdf:Description rdf:about="{ns}ChristmasInMadaba">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ReligiousHoliday"/>
    <jto:startDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-12-24</jto:startDate>
    <jto:endDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-12-25</jto:endDate>
    <rdfs:comment xml:lang="en">Christmas celebrations in Madaba and at Bethany Beyond the Jordan baptism site, with special church services and festivities.</rdfs:comment>
    <rdfs:label xml:lang="en">Christmas in Madaba</rdfs:label>
    <rdfs:label xml:lang="ar">عيد الميلاد في مادبا</rdfs:label>
    <jto:officialName xml:lang="en">Christmas in Madaba</jto:officialName>
  </rdf:Description>

  <!-- CQ-097: Visitor statistics comparison -->
  <rdf:Description rdf:about="{ns}PetraVisitorStats2024">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}VisitorStatistics"/>
    <jto:forAttraction rdf:resource="{ns}PetraSite"/>
    <jto:annualVisitorCount rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">936000</jto:annualVisitorCount>
    <jto:statisticsYear rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2024</jto:statisticsYear>
    <rdfs:label xml:lang="en">Petra Visitor Statistics 2024</rdfs:label>
    <rdfs:label xml:lang="ar">إحصائيات زوار البتراء 2024</rdfs:label>
  </rdf:Description>

  <!-- CQ-101: Abdali Bus Station -->
  <rdf:Description rdf:about="{ns}AbdaliBusStationAmman">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}BusStation"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:servesRoute>Amman to Jerash, Ajloun, Irbid</jto:servesRoute>
    <jto:openingHours>05:00-20:00</jto:openingHours>
    <rdfs:comment xml:lang="en">Main bus station in Amman for northern destinations including Jerash and Ajloun.</rdfs:comment>
    <rdfs:label xml:lang="en">Abdali Bus Station</rdfs:label>
    <rdfs:label xml:lang="ar">محطة العبدلي للحافلات</rdfs:label>
    <jto:officialName xml:lang="en">Abdali Bus Station</jto:officialName>
  </rdf:Description>

  <!-- CQ-103: Airport shuttle service -->
  <rdf:Description rdf:about="{ns}AirportExpressShuttle">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ShuttleService"/>
    <jto:originCity rdf:resource="{ns}QueenAliaInternationalAirport"/>
    <jto:destinationCity rdf:resource="{ns}Amman"/>
    <jto:servicePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.50</jto:servicePrice>
    <jto:travelDuration>45 minutes</jto:travelDuration>
    <jto:frequency>Every 30 minutes</jto:frequency>
    <rdfs:comment xml:lang="en">Airport Express shuttle bus connecting Queen Alia Airport to Amman city center (7th Circle).</rdfs:comment>
    <rdfs:label xml:lang="en">Airport Express Shuttle</rdfs:label>
    <rdfs:label xml:lang="ar">حافلة المطار السريعة</rdfs:label>
    <jto:officialName xml:lang="en">Airport Express Shuttle</jto:officialName>
  </rdf:Description>

  <!-- CQ-106: Petra Monastery -->
  <rdf:Description rdf:about="{ns}PetraMonastery">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Monastery"/>
    <jto:locatedAt rdf:resource="{ns}PetraSite"/>
    <jto:historicalPeriod>Nabataean (1st century AD)</jto:historicalPeriod>
    <jto:hikingRequired rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hikingRequired>
    <jto:trailLength rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.0</jto:trailLength>
    <rdfs:comment xml:lang="en">Ad Deir (The Monastery), one of Petra's largest monuments. Reached via 800+ rock-cut steps, offering spectacular views.</rdfs:comment>
    <rdfs:label xml:lang="en">The Monastery (Ad Deir)</rdfs:label>
    <rdfs:label xml:lang="ar">الدير</rdfs:label>
    <jto:officialName xml:lang="en">The Monastery (Ad Deir)</jto:officialName>
  </rdf:Description>

  <!-- CQ-107: The Siq -->
  <rdf:Description rdf:about="{ns}PetraSiq">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Siq"/>
    <jto:locatedAt rdf:resource="{ns}PetraSite"/>
    <jto:trailLength rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">1.2</jto:trailLength>
    <rdfs:comment xml:lang="en">The Siq is the main entrance to Petra — a narrow 1.2 km gorge with walls up to 80 meters high, leading to the Treasury.</rdfs:comment>
    <rdfs:label xml:lang="en">The Siq</rdfs:label>
    <rdfs:label xml:lang="ar">السيق</rdfs:label>
    <jto:officialName xml:lang="en">The Siq</jto:officialName>
  </rdf:Description>

  <!-- CQ-112: Wadi Mujib canyoning -->
  <rdf:Description rdf:about="{ns}WadiMujibCanyoning">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Canyoning"/>
    <jto:availableAt rdf:resource="{ns}WadiMujibReserveSite"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">4.0</jto:activityDuration>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">21.00</jto:activityPrice>
    <jto:difficultyLevel>Moderate to Difficult</jto:difficultyLevel>
    <jto:minimumAge rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">18</jto:minimumAge>
    <jto:bestSeason>April to October</jto:bestSeason>
    <jto:requiresBooking rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:requiresBooking>
    <rdfs:comment xml:lang="en">Thrilling canyoning experience through Wadi Mujib gorge. Involves swimming, climbing, and wading through canyon waters.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Mujib Canyoning</rdfs:label>
    <rdfs:label xml:lang="ar">تسلق وادي الموجب</rdfs:label>
    <jto:officialName xml:lang="en">Wadi Mujib Canyoning</jto:officialName>
  </rdf:Description>

  <!-- CQ-113: Jordan Pass individual -->
  <rdf:Description rdf:about="{ns}JordanPassWanderer">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}JordanPass"/>
    <jto:passPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">70.00</jto:passPrice>
    <jto:validityDays rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">30</jto:validityDays>
    <jto:petraDaysIncluded rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</jto:petraDaysIncluded>
    <jto:sitesIncluded>40+ attractions including Petra (1 day), Jerash, Ajloun Castle, Wadi Rum</jto:sitesIncluded>
    <rdfs:comment xml:lang="en">Jordan Pass Wanderer tier: includes visa fee waiver, 1-day Petra entry, and access to 40+ sites.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Pass - Wanderer</rdfs:label>
    <rdfs:label xml:lang="ar">بطاقة الأردن - المتجول</rdfs:label>
    <jto:officialName xml:lang="en">Jordan Pass - Wanderer</jto:officialName>
  </rdf:Description>

  <!-- CQ-113: Jordan Pass Explorer -->
  <rdf:Description rdf:about="{ns}JordanPassExplorerIndividual">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}JordanPass"/>
    <jto:passPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">75.00</jto:passPrice>
    <jto:validityDays rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">30</jto:validityDays>
    <jto:petraDaysIncluded rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</jto:petraDaysIncluded>
    <jto:sitesIncluded>40+ attractions including Petra (2 days), Jerash, Ajloun Castle, Wadi Rum</jto:sitesIncluded>
    <rdfs:label xml:lang="en">Jordan Pass - Explorer</rdfs:label>
    <rdfs:label xml:lang="ar">بطاقة الأردن - المستكشف</rdfs:label>
    <jto:officialName xml:lang="en">Jordan Pass - Explorer</jto:officialName>
  </rdf:Description>

  <!-- CQ-116: Beginner diving Aqaba -->
  <rdf:Description rdf:about="{ns}AqabaBeginnerDiving">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}BeginnerDiving"/>
    <jto:availableAt rdf:resource="{ns}Aqaba"/>
    <jto:minimumAge rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">10</jto:minimumAge>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">55.00</jto:activityPrice>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.0</jto:activityDuration>
    <jto:difficultyLevel>Beginner</jto:difficultyLevel>
    <jto:requiresBooking rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:requiresBooking>
    <rdfs:comment xml:lang="en">Introductory dive experience in Aqaba's Red Sea. No certification required. Includes equipment and instructor.</rdfs:comment>
    <rdfs:label xml:lang="en">Aqaba Beginner Diving Experience</rdfs:label>
    <rdfs:label xml:lang="ar">تجربة الغوص للمبتدئين في العقبة</rdfs:label>
    <jto:officialName xml:lang="en">Aqaba Beginner Diving Experience</jto:officialName>
  </rdf:Description>

  <!-- CQ-117: Child discount -->
  <rdf:Description rdf:about="{ns}PetraChildDiscount">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ChildDiscount"/>
    <jto:forAttraction rdf:resource="{ns}PetraSite"/>
    <jto:childDiscountPercentage rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">50</jto:childDiscountPercentage>
    <jto:applicableAgeRange>Under 12 years</jto:applicableAgeRange>
    <rdfs:comment xml:lang="en">Children under 12 receive 50% discount on Petra entry fee. Children under 2 enter free.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Child Discount</rdfs:label>
    <rdfs:label xml:lang="ar">خصم الأطفال للبتراء</rdfs:label>
    <jto:officialName xml:lang="en">Petra Child Discount</jto:officialName>
  </rdf:Description>

  <!-- CQ-121: Sunset camel ride -->
  <rdf:Description rdf:about="{ns}WadiRumSunsetCamelRide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SunsetCamelRide"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2.0</jto:activityDuration>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">35.00</jto:activityPrice>
    <jto:bestTimeOfDay>Late afternoon (2 hours before sunset)</jto:bestTimeOfDay>
    <rdfs:comment xml:lang="en">Magical sunset camel ride through Wadi Rum desert, ending at a scenic viewpoint.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Sunset Camel Ride</rdfs:label>
    <rdfs:label xml:lang="ar">ركوب الجمال عند غروب الشمس في وادي رم</rdfs:label>
    <jto:officialName xml:lang="en">Wadi Rum Sunset Camel Ride</jto:officialName>
  </rdf:Description>

  <!-- CQ-127: Multilingual guide -->
  <rdf:Description rdf:about="{ns}AmmanMultilingualGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}MultilingualGuide"/>
    <jto:languages>Arabic, English, French, Spanish</jto:languages>
    <jto:priceRange>50-100 JOD per day</jto:priceRange>
    <rdfs:comment xml:lang="en">Licensed multilingual guides available through Jordan Tourism Board for Amman city tours.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Multilingual Guide Service</rdfs:label>
    <rdfs:label xml:lang="ar">خدمة المرشدين متعددي اللغات في عمان</rdfs:label>
    <jto:officialName xml:lang="en">Amman Multilingual Guide Service</jto:officialName>
  </rdf:Description>

  <!-- CQ-138: Kings Highway route -->
  <rdf:Description rdf:about="{ns}KingsHighwayRoute">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}KingsHighway"/>
    <jto:drivingDistance rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">335.0</jto:drivingDistance>
    <jto:estimatedDuration>5 hours</jto:estimatedDuration>
    <jto:routeHighlights>Madaba, Mount Nebo, Kerak Castle, Dana Reserve, Petra</jto:routeHighlights>
    <rdfs:comment xml:lang="en">Ancient trade route from Amman to Petra via Madaba, Mount Nebo, and Kerak. Scenic and historic alternative to Desert Highway.</rdfs:comment>
    <rdfs:label xml:lang="en">King's Highway</rdfs:label>
    <rdfs:label xml:lang="ar">طريق الملوك</rdfs:label>
    <jto:officialName xml:lang="en">King's Highway</jto:officialName>
  </rdf:Description>

  <!-- CQ-138: Desert Highway route -->
  <rdf:Description rdf:about="{ns}DesertHighwayRoute">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}DesertHighway"/>
    <jto:drivingDistance rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">265.0</jto:drivingDistance>
    <jto:estimatedDuration>3 hours</jto:estimatedDuration>
    <rdfs:comment xml:lang="en">Fast direct highway from Amman to Aqaba via Ma'an. Fastest route but less scenic than King's Highway.</rdfs:comment>
    <rdfs:label xml:lang="en">Desert Highway</rdfs:label>
    <rdfs:label xml:lang="ar">طريق الصحراء</rdfs:label>
    <jto:officialName xml:lang="en">Desert Highway</jto:officialName>
  </rdf:Description>

  <!-- CQ-141: Vaccination info -->
  <rdf:Description rdf:about="{ns}JordanVaccinationInfo">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Vaccination"/>
    <rdfs:comment xml:lang="en">No mandatory vaccinations for Jordan. Recommended: Hepatitis A, Hepatitis B, Typhoid, and routine vaccinations. COVID-19 vaccination may be required depending on entry requirements.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Vaccination Requirements</rdfs:label>
    <rdfs:label xml:lang="ar">متطلبات التطعيم للأردن</rdfs:label>
    <jto:officialName xml:lang="en">Jordan Vaccination Requirements</jto:officialName>
  </rdf:Description>

  <!-- CQ-142: Water safety Dead Sea -->
  <rdf:Description rdf:about="{ns}DeadSeaWaterSafety">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WaterSafety"/>
    <rdfs:comment xml:lang="en">Dead Sea safety tips: do not swallow water (extremely salty), avoid shaving before swimming, limit sessions to 20 minutes, shower immediately after, protect eyes from splashes, enter slowly on back.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Water Safety</rdfs:label>
    <rdfs:label xml:lang="ar">سلامة المياه في البحر الميت</rdfs:label>
    <jto:officialName xml:lang="en">Dead Sea Water Safety</jto:officialName>
  </rdf:Description>

  <!-- CQ-145: Emergency contacts -->
  <rdf:Description rdf:about="{ns}JordanEmergencyNumbers">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}EmergencyContact"/>
    <jto:emergencyNumber>911</jto:emergencyNumber>
    <jto:policeNumber>191</jto:policeNumber>
    <jto:ambulanceNumber>199</jto:ambulanceNumber>
    <jto:fireNumber>193</jto:fireNumber>
    <rdfs:comment xml:lang="en">Jordan emergency numbers: General Emergency 911, Police 191, Ambulance 199, Fire 193, Tourist Police 110.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Emergency Numbers</rdfs:label>
    <rdfs:label xml:lang="ar">أرقام الطوارئ في الأردن</rdfs:label>
    <jto:officialName xml:lang="en">Jordan Emergency Numbers</jto:officialName>
  </rdf:Description>

  <!-- CQ-148: Payment methods -->
  <rdf:Description rdf:about="{ns}JordanPaymentMethods">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PaymentMethod"/>
    <rdfs:comment xml:lang="en">Accepted payment methods in Jordan: cash (JOD) is king, especially outside Amman. Visa and Mastercard accepted at hotels, major restaurants, and tourist sites. Apple Pay and Google Pay available at some locations. ATMs widely available in cities.</rdfs:comment>
    <rdfs:label xml:lang="en">Payment Methods in Jordan</rdfs:label>
    <rdfs:label xml:lang="ar">طرق الدفع في الأردن</rdfs:label>
    <jto:officialName xml:lang="en">Payment Methods in Jordan</jto:officialName>
  </rdf:Description>
""".replace("{ns}", NS)

# Read existing OWL file
with open(OWL_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before closing </rdf:RDF> tag
insert_point = content.rfind('</rdf:RDF>')
if insert_point == -1:
    print("ERROR: Could not find </rdf:RDF> closing tag")
    exit(1)

new_content = content[:insert_point] + "\n  <!-- ====== JTO v1.6 — New Individuals for CQ-091 to CQ-150 ====== -->\n" + NEW_INDIVIDUALS + "\n" + content[insert_point:]

# Update version info
new_content = new_content.replace(
    '<owl:versionInfo>2.0.0</owl:versionInfo>',
    '<owl:versionInfo>2.1.0</owl:versionInfo>'
)

# Write updated file
with open(OWL_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"v1.6 created successfully!")
print(f"New individuals added: 20")

# Count total individuals
import subprocess
result = subprocess.run(['grep', '-c', 'NamedIndividual', OWL_FILE], capture_output=True, text=True)
count = int(result.stdout.strip()) // 2  # Each individual has 2 NamedIndividual refs typically
print(f"Approximate total individuals: {count}")

result = subprocess.run(['wc', '-l', OWL_FILE], capture_output=True, text=True)
print(f"Total lines: {result.stdout.strip()}")
