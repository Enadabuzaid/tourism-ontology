#!/usr/bin/env python3
"""Add individuals for CQ-251 to CQ-300 to create JTO v1.9"""

OWL_FILE = "/home/claude/tourism-ontology/jto_tourism_entity_module_v1_9_stable.owl"
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

NEW_INDIVIDUALS = """
  <!-- ====== JTO v1.9 — New Individuals for CQ-251 to CQ-300 ====== -->

  <!-- CQ-251: Archaeological research permit -->
  <rdf:Description rdf:about="{ns}JordanResearchPermit">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ResearchPermit"/>
    <jto:issuedBy>Department of Antiquities of Jordan</jto:issuedBy>
    <jto:processingTime>2-4 weeks</jto:processingTime>
    <rdfs:comment xml:lang="en">Research permits for archaeological work in Jordan are issued by the Department of Antiquities. Foreign researchers must partner with a local institution. Permits cover excavation, survey, and conservation activities.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Archaeological Research Permit</rdfs:label>
    <rdfs:label xml:lang="ar">تصريح البحث الأثري في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-253: Academic conferences archaeology -->
  <rdf:Description rdf:about="{ns}JordanArchaeologyConference">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}AcademicConference"/>
    <jto:eventMonth>June</jto:eventMonth>
    <rdfs:comment xml:lang="en">Annual archaeological conference in Amman hosted by ACOR (American Center of Oriental Research). Covers Nabataean, Roman, Byzantine, and Islamic period research in Jordan.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Archaeology Conference</rdfs:label>
    <rdfs:label xml:lang="ar">مؤتمر الآثار الأردني</rdfs:label>
  </rdf:Description>

  <!-- CQ-254: Open archaeological digs -->
  <rdf:Description rdf:about="{ns}PetraOpenDigSite">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ArchaeologicalSite"/>
    <jto:isOpenForVisitors rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:isOpenForVisitors>
    <jto:availableAt rdf:resource="{ns}PetraSite"/>
    <rdfs:comment xml:lang="en">Active archaeological excavation sites at Petra occasionally open to public viewing. Check with Petra Visitor Centre for current dig schedules and viewing opportunities.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Open Dig Site</rdfs:label>
    <rdfs:label xml:lang="ar">موقع حفريات البتراء المفتوح</rdfs:label>
  </rdf:Description>

  <!-- CQ-258: Women's cooperative -->
  <rdf:Description rdf:about="{ns}IraqAlAmirWomenCooperative">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WomensCooperative"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:products>Paper, ceramics, weaving, food products</jto:products>
    <rdfs:comment xml:lang="en">Iraq al-Amir Women's Cooperative near Amman. Supports local women through handicraft production and tourism income. Visitors can tour workshops, buy products, and enjoy traditional meals.</rdfs:comment>
    <rdfs:label xml:lang="en">Iraq al-Amir Women's Cooperative</rdfs:label>
    <rdfs:label xml:lang="ar">جمعية عراق الأمير النسائية التعاونية</rdfs:label>
  </rdf:Description>

  <!-- CQ-259: Fair trade souvenirs -->
  <rdf:Description rdf:about="{ns}JordanFairTradeSouvenirs">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FairTrade"/>
    <rdfs:comment xml:lang="en">Fair trade souvenirs in Jordan: RSCN Nature Shops (Dana, Ajloun reserves), Jordan River Foundation stores (Queen Alia Airport), Iraq al-Amir Women's Cooperative, Bani Hamida weaving project.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Fair Trade Souvenirs</rdfs:label>
    <rdfs:label xml:lang="ar">هدايا التجارة العادلة في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-261: Bedouin homestay -->
  <rdf:Description rdf:about="{ns}WadiRumBedouinHomestay">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Homestay"/>
    <jto:locatedIn rdf:resource="{ns}WadiRum"/>
    <jto:pricePerNight rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">35.00</jto:pricePerNight>
    <rdfs:comment xml:lang="en">Authentic Bedouin homestay experience in Wadi Rum. Stay with a Bedouin family, share meals, learn desert navigation, and experience traditional tent living under the stars.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Bedouin Homestay</rdfs:label>
    <rdfs:label xml:lang="ar">إقامة مع البدو في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-264: Jordanian spices market -->
  <rdf:Description rdf:about="{ns}AmmanSpiceMarket">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}Market"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <rdfs:comment xml:lang="en">Downtown Amman spice souk near Al-Husseini Mosque. Sells za'atar, sumac, cardamom, saffron, and traditional spice blends. Best prices through bargaining.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Spice Market</rdfs:label>
    <rdfs:label xml:lang="ar">سوق التوابل في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-269: Dangerous wildlife -->
  <rdf:Description rdf:about="{ns}JordanWildlifeWarning">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WildlifeWarning"/>
    <rdfs:comment xml:lang="en">Wildlife hazards in Jordan: Palestine viper (Daboia palaestinae) in hills, Deathstalker scorpion in desert, camel spiders (harmless but startling). Shake shoes before wearing. Carry antivenom awareness card.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Wildlife Safety Warning</rdfs:label>
    <rdfs:label xml:lang="ar">تحذير الحياة البرية في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-271: Diving certification Aqaba -->
  <rdf:Description rdf:about="{ns}AqabaDivingCertification">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}DivingCertification"/>
    <jto:certifyingBody>PADI, SSI</jto:certifyingBody>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">350.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">PADI Open Water certification available in Aqaba. 3-4 day courses from multiple dive centers. Red Sea offers year-round diving with 20-30m visibility and coral reefs.</rdfs:comment>
    <rdfs:label xml:lang="en">Aqaba Diving Certification</rdfs:label>
    <rdfs:label xml:lang="ar">شهادة الغوص في العقبة</rdfs:label>
  </rdf:Description>

  <!-- CQ-274: Sun protection tips -->
  <rdf:Description rdf:about="{ns}JordanSunProtectionGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SafetyGuidance"/>
    <rdfs:comment xml:lang="en">Sun protection in Jordan: SPF50+ sunscreen essential, reapply every 2 hours. Wear wide-brim hat, UV sunglasses. Peak UV hours 10am-4pm. Drink 3+ liters water daily in summer. Seek shade during midday.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Sun Protection Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل الحماية من الشمس في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-275: Altitude sickness -->
  <rdf:Description rdf:about="{ns}JordanAltitudeGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SafetyGuidance"/>
    <rdfs:comment xml:lang="en">Jordan's highest point is Jabal Umm ad Dami at 1,854m — altitude sickness is not a concern for most travelers. The Dead Sea at -430m is the lowest point. Rapid altitude changes between the two may cause ear pressure.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Altitude Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل الارتفاع في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-278: Stargazing equipment rental -->
  <rdf:Description rdf:about="{ns}WadiRumTelescopeRental">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}EquipmentRental"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">25.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Telescope and stargazing equipment rental at Wadi Rum camps. Some camps include guided stargazing sessions with Bedouin astronomy storytelling. Bring binoculars for best experience.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Telescope Rental</rdfs:label>
    <rdfs:label xml:lang="ar">تأجير تلسكوب في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-283: Photography spots -->
  <rdf:Description rdf:about="{ns}JordanInstagramSpots">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PhotographyLocation"/>
    <rdfs:comment xml:lang="en">Top photography spots in Jordan: Petra Treasury at dawn, Wadi Rum desert arches, Dead Sea floating (salt crystals), King's Highway viewpoints, Amman Citadel sunset, Dana Reserve canyon overlook.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Photography Spots</rdfs:label>
    <rdfs:label xml:lang="ar">مواقع التصوير في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-288: Sign language services -->
  <rdf:Description rdf:about="{ns}JordanSignLanguageService">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SignLanguageService"/>
    <rdfs:comment xml:lang="en">Sign language interpretation available at Jordan Museum and select major sites by advance booking. Contact Jordan Tourism Board 48 hours ahead. Jordanian Sign Language (LIU) is the local variant.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Sign Language Service</rdfs:label>
    <rdfs:label xml:lang="ar">خدمة لغة الإشارة في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-293: Visa on arrival -->
  <rdf:Description rdf:about="{ns}JordanVisaOnArrival">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}VisaRequirement"/>
    <jto:visaFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">40.00</jto:visaFee>
    <rdfs:comment xml:lang="en">Visa on arrival available for most nationalities at Queen Alia Airport (40 JOD). Jordan Pass includes visa fee waiver if staying 3+ nights. Some nationalities require pre-arranged visa.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Visa on Arrival</rdfs:label>
    <rdfs:label xml:lang="ar">تأشيرة عند الوصول للأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-294: Currency exchange -->
  <rdf:Description rdf:about="{ns}JordanCurrencyExchange">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FinancialService"/>
    <rdfs:comment xml:lang="en">Jordanian Dinar (JOD) is pegged to USD at 0.709. ATMs widespread in cities. Exchange bureaus at airports and downtown Amman offer competitive rates. Credit cards accepted at hotels and larger shops.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Currency Exchange Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل صرف العملات في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-295: Health documents -->
  <rdf:Description rdf:about="{ns}JordanHealthRequirements">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}HealthRequirement"/>
    <rdfs:comment xml:lang="en">No mandatory vaccinations for Jordan entry. Recommended: Hepatitis A/B, Typhoid, routine boosters. Tap water not recommended for drinking — use bottled water. Travel health insurance strongly recommended.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Health Requirements</rdfs:label>
    <rdfs:label xml:lang="ar">المتطلبات الصحية للأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-296: Real-time wait times -->
  <rdf:Description rdf:about="{ns}PetraWaitTimeData">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WaitTime"/>
    <jto:currentWaitMinutes rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">15</jto:currentWaitMinutes>
    <jto:forLocation rdf:resource="{ns}PetraSite"/>
    <rdfs:comment xml:lang="en">Estimated wait time at Petra Visitor Centre ticket office. Peak hours 8-10am can reach 30+ minutes. Jordan Pass holders use fast-track lane. Quietest entry after 2pm.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Wait Time</rdfs:label>
    <rdfs:label xml:lang="ar">وقت الانتظار في البتراء</rdfs:label>
  </rdf:Description>

  <!-- CQ-298: Real-time traffic -->
  <rdf:Description rdf:about="{ns}JordanTrafficData">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}TrafficData"/>
    <rdfs:comment xml:lang="en">Amman traffic peaks 7-9am and 3-6pm. Desert Highway (Amman-Aqaba) generally clear. Dead Sea road busy on Fridays/holidays. Use Waze or Google Maps for real-time routing.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Traffic Data</rdfs:label>
    <rdfs:label xml:lang="ar">بيانات المرور في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-299: Real-time hotel availability -->
  <rdf:Description rdf:about="{ns}JordanHotelAvailability">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}RealTimeAvailability"/>
    <rdfs:comment xml:lang="en">Hotel availability in Jordan is seasonal: book Petra and Dead Sea hotels 2+ weeks ahead during peak season (Mar-May, Sep-Nov). Amman hotels generally available. Aqaba busy during Eid holidays and European winter.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Hotel Availability Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل توفر الفنادق في الأردن</rdfs:label>
  </rdf:Description>
""".replace("{ns}", NS)

with open(OWL_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

insert_point = content.rfind('</rdf:RDF>')
new_content = content[:insert_point] + NEW_INDIVIDUALS + "\n" + content[insert_point:]

with open(OWL_FILE, 'w', encoding='utf-8') as f:
    f.write(new_content)

import subprocess, xml.etree.ElementTree as ET
result = subprocess.run(['wc', '-l', OWL_FILE], capture_output=True, text=True)
print(f"v1.9 created: {result.stdout.strip()}")
tree = ET.parse(OWL_FILE)
root = tree.getroot()
rdf_ns = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
ni_uri = 'http://www.w3.org/2002/07/owl#NamedIndividual'
count = sum(1 for d in root.findall(f'{rdf_ns}Description') for t in d.findall(f'{rdf_ns}type') if t.get(f'{rdf_ns}resource') == ni_uri)
print(f"XML valid ✅ · Named individuals: {count}")
