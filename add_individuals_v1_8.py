#!/usr/bin/env python3
"""Add individuals for CQ-201 to CQ-250 to create JTO v1.8"""

OWL_FILE = "/home/claude/tourism-ontology/jto_tourism_entity_module_v1_8_stable.owl"
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

NEW_INDIVIDUALS = """
  <!-- ====== JTO v1.8 — New Individuals for CQ-201 to CQ-250 ====== -->

  <!-- CQ-201: Eco-tourism sustainability certification -->
  <rdf:Description rdf:about="{ns}JordanEcoTourismCertification">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SustainabilityCertification"/>
    <jto:certifyingBody>Royal Society for Conservation of Nature (RSCN)</jto:certifyingBody>
    <jto:certificationLevel>Gold</jto:certificationLevel>
    <rdfs:comment xml:lang="en">Jordan's eco-tourism sustainability certification program managed by RSCN. Lodges meeting environmental standards receive Gold, Silver, or Bronze certification.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Eco-Tourism Certification</rdfs:label>
    <rdfs:label xml:lang="ar">شهادة السياحة البيئية الأردنية</rdfs:label>
  </rdf:Description>

  <!-- CQ-202: Dead Sea environmental policy -->
  <rdf:Description rdf:about="{ns}DeadSeaEnvironmentalPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}EnvironmentalPolicy"/>
    <rdfs:comment xml:lang="en">Environmental protection policies for the Dead Sea region. Hotels must meet water recycling standards. Mud extraction is regulated. Industrial diversion of Jordan River water is the primary ecological threat.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Environmental Policy</rdfs:label>
    <rdfs:label xml:lang="ar">السياسة البيئية للبحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-203: JREDS conservation -->
  <rdf:Description rdf:about="{ns}JREDSConservation">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ConservationOrganization"/>
    <jto:organizationName>JREDS (Jordan Royal Ecological Diving Society)</jto:organizationName>
    <rdfs:comment xml:lang="en">JREDS manages Aqaba Marine Park and coral reef conservation. Offers eco-diving programs and marine wildlife education for tourists.</rdfs:comment>
    <rdfs:label xml:lang="en">JREDS Marine Conservation</rdfs:label>
    <rdfs:label xml:lang="ar">الجمعية الملكية الأردنية للغوص البيئي</rdfs:label>
  </rdf:Description>

  <!-- CQ-205: Volunteer tourism -->
  <rdf:Description rdf:about="{ns}JordanVolunteerTourism">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}VolunteerActivity"/>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">14.0</jto:activityDuration>
    <rdfs:comment xml:lang="en">Volunteer tourism opportunities in Jordan: wildlife conservation at Dana/Shaumari reserves, community development projects, archaeological digs at Jerash, and English teaching programs.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Volunteer Tourism</rdfs:label>
    <rdfs:label xml:lang="ar">السياحة التطوعية في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-206: Convention center -->
  <rdf:Description rdf:about="{ns}KingHusseinConventionCenter">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ConventionCenter"/>
    <jto:locatedIn rdf:resource="{ns}DeadSeaArea"/>
    <jto:seatingCapacity rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">3000</jto:seatingCapacity>
    <jto:hasVideoConferencing rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasVideoConferencing>
    <rdfs:comment xml:lang="en">King Hussein Bin Talal Convention Centre at the Dead Sea. Jordan's largest conference venue with capacity for 3,000+ delegates. Used for WEF and major international conferences.</rdfs:comment>
    <rdfs:label xml:lang="en">King Hussein Convention Centre</rdfs:label>
    <rdfs:label xml:lang="ar">مركز الملك حسين بن طلال للمؤتمرات</rdfs:label>
  </rdf:Description>

  <!-- CQ-207: Corporate team building -->
  <rdf:Description rdf:about="{ns}WadiRumTeamBuilding">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}TeamBuilding"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">75.00</jto:activityPrice>
    <jto:groupSize>10-50 participants</jto:groupSize>
    <rdfs:comment xml:lang="en">Corporate team-building experiences in Wadi Rum: desert survival challenges, Bedouin cooking competitions, navigation exercises, and stargazing programs.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Team Building</rdfs:label>
    <rdfs:label xml:lang="ar">بناء الفريق في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-208: Business hotels -->
  <rdf:Description rdf:about="{ns}AmmanBusinessHotel">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}BusinessHotel"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:hasBusinessCenter rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasBusinessCenter>
    <jto:hasMeetingRooms rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasMeetingRooms>
    <rdfs:comment xml:lang="en">Business-class hotels in Amman's Abdali district with dedicated business centers, meeting rooms, high-speed WiFi, and airport transfer services.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Business Hotel District</rdfs:label>
    <rdfs:label xml:lang="ar">فنادق الأعمال في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-210: Unique venue Petra -->
  <rdf:Description rdf:about="{ns}PetraCaveVenue">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}UniqueVenue"/>
    <jto:availableAt rdf:resource="{ns}PetraSite"/>
    <jto:seatingCapacity rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">200</jto:seatingCapacity>
    <rdfs:comment xml:lang="en">Unique event venue inside Petra's cave restaurants. Available for private dinners, corporate events, and cultural evenings with Nabataean ambiance.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Cave Venue</rdfs:label>
    <rdfs:label xml:lang="ar">قاعة الكهف في البتراء</rdfs:label>
  </rdf:Description>

  <!-- CQ-211: Luxury helicopter charter -->
  <rdf:Description rdf:about="{ns}JordanHelicopterCharter">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}CharterFlight"/>
    <jto:servicePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2500.00</jto:servicePrice>
    <jto:route>Amman to Petra, Wadi Rum, or Dead Sea</jto:route>
    <rdfs:comment xml:lang="en">Private helicopter charter service connecting Amman with Petra, Wadi Rum, and Dead Sea. Journey time 45 minutes vs 3-4 hours by road.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Helicopter Charter</rdfs:label>
    <rdfs:label xml:lang="ar">تأجير طائرة هليكوبتر في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-213: Private dining -->
  <rdf:Description rdf:about="{ns}WadiRumPrivateDining">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PrivateDining"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">150.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Exclusive private dining under the stars in Wadi Rum with personal Bedouin chef. Includes traditional zarb feast and live oud music.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Private Dining</rdfs:label>
    <rdfs:label xml:lang="ar">عشاء خاص في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-215: Orient Express style luxury -->
  <rdf:Description rdf:about="{ns}HejazRailwayExperience">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}LuxuryTransport"/>
    <jto:historicalPeriod>Ottoman era (1908)</jto:historicalPeriod>
    <rdfs:comment xml:lang="en">Historic Hejaz Railway experience from Amman to Wadi Rum. Restored Ottoman-era coaches with luxury dining service and desert panoramas.</rdfs:comment>
    <rdfs:label xml:lang="en">Hejaz Railway Luxury Experience</rdfs:label>
    <rdfs:label xml:lang="ar">تجربة سكة حديد الحجاز الفاخرة</rdfs:label>
  </rdf:Description>

  <!-- CQ-216: Budget hotel Amman -->
  <rdf:Description rdf:about="{ns}AmmanBudgetHotel">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}BudgetHotel"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:pricePerNight rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">25.00</jto:pricePerNight>
    <rdfs:comment xml:lang="en">Budget hotels in downtown Amman near Rainbow Street. Clean, basic rooms from 25 JOD/night. Walking distance to Citadel and Roman Theater.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Budget Hotels</rdfs:label>
    <rdfs:label xml:lang="ar">فنادق اقتصادية في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-217: Free activities -->
  <rdf:Description rdf:about="{ns}JordanFreeActivities">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FreeAttraction"/>
    <rdfs:comment xml:lang="en">Free activities in Jordan: Rainbow Street walking (Amman), Amman Citadel sunset viewing, downtown souk browsing, King Abdullah Mosque (free entry for visitors), Roman Theater exterior, Aqaba public beaches.</rdfs:comment>
    <rdfs:label xml:lang="en">Free Activities in Jordan</rdfs:label>
    <rdfs:label xml:lang="ar">أنشطة مجانية في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-218: Street food -->
  <rdf:Description rdf:about="{ns}AmmanStreetFood">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}StreetFoodVendor"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:averagePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2.00</jto:averagePrice>
    <rdfs:comment xml:lang="en">Amman's best street food areas: Downtown Al-Balad for falafel and shawarma, Hashemite Square for fresh juice, Rainbow Street for trendy street bites. Average meal 1-3 JOD.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Street Food Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل طعام الشارع في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-219: Tourist pass / discount card -->
  <rdf:Description rdf:about="{ns}AmmanCityPass">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}TouristPass"/>
    <jto:passPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">15.00</jto:passPrice>
    <jto:sitesIncluded>Amman Citadel, Roman Theater, Jordan Museum, National Gallery</jto:sitesIncluded>
    <rdfs:comment xml:lang="en">Amman City Pass covers entry to major Amman attractions at a discounted bundle price. Valid 3 days.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman City Pass</rdfs:label>
    <rdfs:label xml:lang="ar">بطاقة مدينة عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-220: Wild camping -->
  <rdf:Description rdf:about="{ns}JordanWildCamping">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WildCamping"/>
    <rdfs:comment xml:lang="en">Wild camping is generally allowed in Jordan outside national parks and reserves. Popular spots: Dana highlands, Wadi Rum outskirts, Ajloun forests. Always ask local permission and leave no trace.</rdfs:comment>
    <rdfs:label xml:lang="en">Wild Camping in Jordan</rdfs:label>
    <rdfs:label xml:lang="ar">التخييم البري في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-221: Romantic accommodation -->
  <rdf:Description rdf:about="{ns}DeadSeaRomanticSuite">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}RomanticAccommodation"/>
    <jto:locatedIn rdf:resource="{ns}DeadSeaArea"/>
    <jto:hasPrivatePool rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasPrivatePool>
    <jto:pricePerNight rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">350.00</jto:pricePerNight>
    <rdfs:comment xml:lang="en">Romantic suites at Dead Sea resorts with private plunge pools, couples spa treatments, and sunset balconies overlooking the Dead Sea.</rdfs:comment>
    <rdfs:label xml:lang="en">Dead Sea Romantic Suite</rdfs:label>
    <rdfs:label xml:lang="ar">جناح رومانسي في البحر الميت</rdfs:label>
  </rdf:Description>

  <!-- CQ-222: Wedding photography -->
  <rdf:Description rdf:about="{ns}PetraWeddingPhotography">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WeddingPhotography"/>
    <jto:availableAt rdf:resource="{ns}PetraSite"/>
    <jto:requiresPermit rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:requiresPermit>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">500.00</jto:activityPrice>
    <rdfs:comment xml:lang="en">Professional wedding photography at Petra. Requires Jordan Tourism Board commercial permit. Best spots: Treasury, Monastery, Siq entrance. Early morning sessions recommended.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Wedding Photography</rdfs:label>
    <rdfs:label xml:lang="ar">تصوير حفلات الزفاف في البتراء</rdfs:label>
  </rdf:Description>

  <!-- CQ-223: Proposal locations -->
  <rdf:Description rdf:about="{ns}JordanProposalSpots">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}RomanticActivity"/>
    <rdfs:comment xml:lang="en">Best proposal spots in Jordan: Petra Treasury at sunrise, Wadi Rum hot air balloon, Dead Sea sunset float, Mount Nebo viewpoint, Aqaba glass-bottom boat.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Proposal Spots</rdfs:label>
    <rdfs:label xml:lang="ar">أماكن لطلب الزواج في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-226: Senior/elderly accessibility -->
  <rdf:Description rdf:about="{ns}JordanSeniorTravelerGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SeniorTraveler"/>
    <jto:mobilityLevel>moderate</jto:mobilityLevel>
    <rdfs:comment xml:lang="en">Guide for senior travelers in Jordan: accessible sites (Amman Citadel has ramps, Dead Sea resorts are flat), recommended pace (2-3 sites per day), medical facilities available in Amman and Aqaba, travel insurance strongly recommended.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Senior Traveler Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل المسافر المسن في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-228: Medical facility -->
  <rdf:Description rdf:about="{ns}AmmanMedicalFacility">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}MedicalFacility"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:is24Hours rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:is24Hours>
    <jto:hasEnglishSpeakingStaff rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasEnglishSpeakingStaff>
    <rdfs:comment xml:lang="en">Jordan Hospital and Specialty Hospital in Amman — 24/7 emergency with English-speaking staff. Jordan is a medical tourism hub with internationally accredited facilities.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Medical Facilities</rdfs:label>
    <rdfs:label xml:lang="ar">المرافق الطبية في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-229: Pharmacy / medication -->
  <rdf:Description rdf:about="{ns}JordanPharmacyGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}HealthService"/>
    <rdfs:comment xml:lang="en">Pharmacies widely available in Jordan's cities, many open late. Common medications available without prescription. Bring prescriptions for controlled substances. Pharmacists often speak English.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Pharmacy Guide</rdfs:label>
    <rdfs:label xml:lang="ar">دليل الصيدليات في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-231: Solo female safety -->
  <rdf:Description rdf:about="{ns}JordanSoloFemaleSafety">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WomenTravelerSafety"/>
    <jto:safetyRating>High</jto:safetyRating>
    <rdfs:comment xml:lang="en">Jordan ranks among the safest Middle Eastern countries for solo female travelers. Tourist Police hotline: 110. Tips: dress modestly outside resorts, use registered taxis, avoid isolated areas at night, learn basic Arabic greetings.</rdfs:comment>
    <rdfs:label xml:lang="en">Solo Female Travel Safety</rdfs:label>
    <rdfs:label xml:lang="ar">سلامة السفر المنفرد للنساء</rdfs:label>
  </rdf:Description>

  <!-- CQ-233: Women-only hostel -->
  <rdf:Description rdf:about="{ns}AmmanWomenOnlyHostel">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WomenOnlyHostel"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:pricePerNight rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">18.00</jto:pricePerNight>
    <rdfs:comment xml:lang="en">Women-only hostel options in Amman providing safe, affordable accommodation for solo female travelers. Private rooms and dorms with female-only floors.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Women-Only Hostel</rdfs:label>
    <rdfs:label xml:lang="ar">نزل للنساء فقط في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-234: Women taxi service -->
  <rdf:Description rdf:about="{ns}JordanWomenTaxiService">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}WomenTaxi"/>
    <jto:operatesIn rdf:resource="{ns}Amman"/>
    <rdfs:comment xml:lang="en">Women-driven taxi services available in Amman through apps like Careem (women-only driver option) and dedicated women taxi companies. Provides safe transport for solo female travelers.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Women Taxi Service</rdfs:label>
    <rdfs:label xml:lang="ar">خدمة سيارات أجرة للنساء</rdfs:label>
  </rdf:Description>

  <!-- CQ-235: Female tour guides -->
  <rdf:Description rdf:about="{ns}JordanFemaleTourGuide">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FemaleTourGuide"/>
    <jto:languages>Arabic, English</jto:languages>
    <rdfs:comment xml:lang="en">Licensed female tour guides available through Jordan Tourism Board. Can be requested for Petra, Amman, Jerash, and other major sites. Booking through official tourism offices recommended.</rdfs:comment>
    <rdfs:label xml:lang="en">Female Tour Guide Service</rdfs:label>
    <rdfs:label xml:lang="ar">خدمة المرشدات السياحيات</rdfs:label>
  </rdf:Description>

  <!-- CQ-236: Group policy -->
  <rdf:Description rdf:about="{ns}JordanGroupTourPolicy">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}GroupPolicy"/>
    <jto:maxGroupSize rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">50</jto:maxGroupSize>
    <rdfs:comment xml:lang="en">Group tour policies: maximum 50 people per guided group at Petra, advance booking required for groups of 15+, group parking available at all major sites, licensed guide mandatory for groups over 10.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Group Tour Policy</rdfs:label>
    <rdfs:label xml:lang="ar">سياسة الجولات الجماعية</rdfs:label>
  </rdf:Description>

  <!-- CQ-238: Parking facilities -->
  <rdf:Description rdf:about="{ns}PetraParkingFacility">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}ParkingFacility"/>
    <jto:locatedAt rdf:resource="{ns}PetraSite"/>
    <jto:parkingFee rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.00</jto:parkingFee>
    <jto:capacity rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">500</jto:capacity>
    <rdfs:comment xml:lang="en">Free parking at Petra Visitor Centre. Capacity 500+ vehicles. Shaded parking limited — arrive early. Bus parking also available.</rdfs:comment>
    <rdfs:label xml:lang="en">Petra Parking Facility</rdfs:label>
    <rdfs:label xml:lang="ar">مواقف سيارات البتراء</rdfs:label>
  </rdf:Description>

  <!-- CQ-239: Roadside assistance -->
  <rdf:Description rdf:about="{ns}JordanRoadsideAssistance">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}EmergencyService"/>
    <jto:emergencyNumber>911</jto:emergencyNumber>
    <rdfs:comment xml:lang="en">Jordan Automobile Association provides roadside assistance. Rental car companies include 24/7 breakdown service. Desert Highway has regular fuel stations every 50km. Emergency number: 911.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Roadside Assistance</rdfs:label>
    <rdfs:label xml:lang="ar">المساعدة على الطريق في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-240: Cultural activities -->
  <rdf:Description rdf:about="{ns}AmmanCulturalWalk">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}CulturalActivity"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">30.00</jto:activityPrice>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">3.0</jto:activityDuration>
    <rdfs:comment xml:lang="en">Guided cultural walking tour through Amman's historic downtown, Jabal al-Weibdeh art district, and Rainbow Street. Includes street food tastings and local artisan visits.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Cultural Walking Tour</rdfs:label>
    <rdfs:label xml:lang="ar">جولة ثقافية سيراً في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-241: Cooking class with permit -->
  <rdf:Description rdf:about="{ns}MansafCookingClass">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}MansafCookingClass"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">55.00</jto:activityPrice>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">4.0</jto:activityDuration>
    <rdfs:comment xml:lang="en">Learn to cook Jordan's national dish Mansaf from local chefs. Includes market tour, hands-on cooking, and communal dining experience.</rdfs:comment>
    <rdfs:label xml:lang="en">Mansaf Cooking Class</rdfs:label>
    <rdfs:label xml:lang="ar">دورة طبخ المنسف</rdfs:label>
  </rdf:Description>

  <!-- CQ-243: Craft workshop -->
  <rdf:Description rdf:about="{ns}AmmanPotteryWorkshop">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}CraftWorkshop"/>
    <jto:locatedIn rdf:resource="{ns}Amman"/>
    <jto:activityPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">35.00</jto:activityPrice>
    <jto:activityDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">2.0</jto:activityDuration>
    <rdfs:comment xml:lang="en">Hands-on pottery workshop in Amman's Jabal al-Weibdeh art district. Learn traditional Jordanian pottery techniques and take your creation home.</rdfs:comment>
    <rdfs:label xml:lang="en">Amman Pottery Workshop</rdfs:label>
    <rdfs:label xml:lang="ar">ورشة فخار في عمان</rdfs:label>
  </rdf:Description>

  <!-- CQ-244: Sunrise location -->
  <rdf:Description rdf:about="{ns}WadiRumSunriseSpot">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}SunriseLocation"/>
    <jto:availableAt rdf:resource="{ns}WadiRum"/>
    <rdfs:comment xml:lang="en">Wadi Rum sunrise viewpoints: Jebel Umm Adami (highest peak), Lawrence's Spring rock bridge, and camp rooftops. Best experienced October-March for cooler temperatures and clearer skies.</rdfs:comment>
    <rdfs:label xml:lang="en">Wadi Rum Sunrise Spots</rdfs:label>
    <rdfs:label xml:lang="ar">مواقع شروق الشمس في وادي رم</rdfs:label>
  </rdf:Description>

  <!-- CQ-246: Filming permit -->
  <rdf:Description rdf:about="{ns}JordanFilmingPermit">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}FilmingPermit"/>
    <jto:issuedBy>Royal Film Commission of Jordan</jto:issuedBy>
    <jto:processingTime>5-10 business days</jto:processingTime>
    <rdfs:comment xml:lang="en">Professional filming in Jordan requires permit from Royal Film Commission (RFC). Jordan offers 10-25% cash rebate for film productions. Famous filming locations: Petra (Indiana Jones), Wadi Rum (The Martian, Dune).</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Filming Permit</rdfs:label>
    <rdfs:label xml:lang="ar">تصريح التصوير في الأردن</rdfs:label>
  </rdf:Description>

  <!-- CQ-248: Commercial photography permit -->
  <rdf:Description rdf:about="{ns}JordanCommercialPhotoPermit">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}PhotographyPermit"/>
    <jto:issuedBy>Jordan Tourism Board</jto:issuedBy>
    <rdfs:comment xml:lang="en">Commercial photography at Jordan's archaeological sites requires a permit from the Jordan Tourism Board. Personal photography is free. Tripods allowed at most sites except inside museums.</rdfs:comment>
    <rdfs:label xml:lang="en">Commercial Photography Permit</rdfs:label>
    <rdfs:label xml:lang="ar">تصريح التصوير التجاري</rdfs:label>
  </rdf:Description>

  <!-- CQ-249: No-fly zones -->
  <rdf:Description rdf:about="{ns}JordanNoFlyZones">
    <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
    <rdf:type rdf:resource="{ns}NoFlyZone"/>
    <rdfs:comment xml:lang="en">Drone no-fly zones in Jordan: all archaeological sites (Petra, Jerash, Citadel), military installations, Royal Palaces, airports (5km radius), border areas. CARC permit required for all drone flights.</rdfs:comment>
    <rdfs:label xml:lang="en">Jordan Drone No-Fly Zones</rdfs:label>
    <rdfs:label xml:lang="ar">مناطق حظر الطيران في الأردن</rdfs:label>
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
print(f"v1.8 created: {result.stdout.strip()}")
tree = ET.parse(OWL_FILE)
root = tree.getroot()
rdf_ns = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'
ni_uri = 'http://www.w3.org/2002/07/owl#NamedIndividual'
count = sum(1 for d in root.findall(f'{rdf_ns}Description') for t in d.findall(f'{rdf_ns}type') if t.get(f'{rdf_ns}resource') == ni_uri)
print(f"XML valid ✅ · Named individuals: {count}")
