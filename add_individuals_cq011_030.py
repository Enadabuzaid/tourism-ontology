#!/usr/bin/env python3
"""
JTO v1.5 — Add Missing Individuals for CQ-011 to CQ-030
Run: cd /Users/enadabuzaid/Desktop/Thesis/ontology/ && python3 add_individuals_cq011_030.py
"""
import re, os

INPUT_FILE = "jto_tourism_entity_module_v1_4_stable.owl"
OUTPUT_FILE = "jto_tourism_entity_module_v1_5_stable.owl"
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

# NOTE: All properties use jto: prefix to match the ontology namespace.
# PROV-O and GeoSPARQL elements use FULL URIs (not prefixed).
# Uses rdf:Description + rdf:type NamedIndividual pattern (consistent with v1.3/v1.4).
NEW_INDIVIDUALS = """
    <!-- ========== JTO v1.5 INDIVIDUALS (CQ-011 to CQ-030) ========== -->

    <!-- CQ-011: Festival in Jerash July -->
    <rdf:Description rdf:about="{ns}JerashFestival2025">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Festival"/>
        <jto:locatedAt rdf:resource="{ns}JerashCity"/>
        <jto:startDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-07-22</jto:startDate>
        <jto:endDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-08-10</jto:endDate>
        <rdfs:label xml:lang="en">Jerash Festival of Culture and Arts 2025</rdfs:label>
        <rdfs:label xml:lang="ar">مهرجان جرش للثقافة والفنون 2025</rdfs:label>
    </rdf:Description>

    <!-- CQ-013: Driving route Amman to Petra -->
    <rdf:Description rdf:about="{ns}DriveRouteAmmanPetra">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}DrivingRoute"/>
        <jto:originCity rdf:resource="{ns}AmmanCity"/>
        <jto:destinationCity rdf:resource="{ns}PetraCity"/>
        <jto:drivingDistance rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">235.0</jto:drivingDistance>
        <jto:estimatedDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#string">3 hours via Desert Highway</jto:estimatedDuration>
        <rdfs:label xml:lang="en">Amman to Petra Driving Route</rdfs:label>
        <rdfs:label xml:lang="ar">مسار القيادة من عمان إلى البتراء</rdfs:label>
    </rdf:Description>

    <!-- CQ-017: Ramadan practices -->
    <rdf:Description rdf:about="{ns}RamadanSeason">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}ReligiousSeason"/>
        <rdfs:label xml:lang="en">Ramadan</rdfs:label>
        <rdfs:label xml:lang="ar">رمضان</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}RamadanEatingPractice">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}CulturalPractice"/>
        <jto:appliesToSeason rdf:resource="{ns}RamadanSeason"/>
        <rdfs:comment xml:lang="en">Avoid eating, drinking, or smoking in public during daylight hours.</rdfs:comment>
        <rdfs:label xml:lang="en">Ramadan Public Eating Etiquette</rdfs:label>
        <rdfs:label xml:lang="ar">آداب الأكل العام في رمضان</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}RamadanDressPractice">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}CulturalPractice"/>
        <jto:appliesToSeason rdf:resource="{ns}RamadanSeason"/>
        <rdfs:comment xml:lang="en">Dress more conservatively during Ramadan, especially near religious sites.</rdfs:comment>
        <rdfs:label xml:lang="en">Ramadan Dress Code Practice</rdfs:label>
        <rdfs:label xml:lang="ar">ممارسة اللباس في رمضان</rdfs:label>
    </rdf:Description>

    <!-- CQ-019: Mansaf in Amman -->
    <rdf:Description rdf:about="{ns}MansafDish">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Dish"/>
        <rdfs:label xml:lang="en">Mansaf</rdfs:label>
        <rdfs:label xml:lang="ar">منسف</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}HashemRestaurant">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <jto:servesDish rdf:resource="{ns}MansafDish"/>
        <jto:locatedIn rdf:resource="{ns}AmmanCity"/>
        <jto:hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">false</jto:hasVegetarianOptions>
        <rdfs:label xml:lang="en">Hashem Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم هاشم</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}SufraRestaurant">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <jto:servesDish rdf:resource="{ns}MansafDish"/>
        <jto:locatedIn rdf:resource="{ns}AmmanCity"/>
        <jto:hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasVegetarianOptions>
        <rdfs:label xml:lang="en">Sufra Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم سفرة</rdfs:label>
    </rdf:Description>

    <!-- CQ-020: Vegetarian + outdoor seating -->
    <rdf:Description rdf:about="{ns}OutdoorSeatingAmenity">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Amenity"/>
        <rdfs:label xml:lang="en">outdoor dining</rdfs:label>
        <rdfs:label xml:lang="ar">تناول الطعام في الهواء الطلق</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}WadiRumCampRestaurant">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <jto:hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:hasVegetarianOptions>
        <jto:hasAmenity rdf:resource="{ns}OutdoorSeatingAmenity"/>
        <jto:locatedIn rdf:resource="{ns}WadiRumArea"/>
        <rdfs:label xml:lang="en">Wadi Rum Camp Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم مخيم وادي رم</rdfs:label>
    </rdf:Description>

    <!-- CQ-021: Petra crowd forecast (BI) -->
    <rdf:Description rdf:about="{ns}PetraCrowdForecastMorning">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}CrowdForecast"/>
        <jto:forAttraction rdf:resource="{ns}PetraSite"/>
        <jto:timePeriod rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Early morning weekdays</jto:timePeriod>
        <jto:predictedCrowdLevel rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</jto:predictedCrowdLevel>
        <jto:forecastConfidence rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.85</jto:forecastConfidence>
        <jto:generatedBy rdf:resource="{ns}JTOForecastModelV1"/>
        <rdfs:label xml:lang="en">Petra Crowd Forecast - Morning</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}PetraCrowdForecastAfternoon">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}CrowdForecast"/>
        <jto:forAttraction rdf:resource="{ns}PetraSite"/>
        <jto:timePeriod rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Weekend afternoons</jto:timePeriod>
        <jto:predictedCrowdLevel rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">8</jto:predictedCrowdLevel>
        <jto:forecastConfidence rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.78</jto:forecastConfidence>
        <jto:generatedBy rdf:resource="{ns}JTOForecastModelV1"/>
        <rdfs:label xml:lang="en">Petra Crowd Forecast - Afternoon</rdfs:label>
    </rdf:Description>

    <!-- CQ-022: Aqaba Easter prices -->
    <rdf:Description rdf:about="{ns}AqabaPriceForecastEaster">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}PriceForecast"/>
        <jto:forLocation rdf:resource="{ns}AqabaCity"/>
        <jto:forSeason rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Easter</jto:forSeason>
        <jto:predictedAveragePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">85.0</jto:predictedAveragePrice>
        <jto:seasonalityScore rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.72</jto:seasonalityScore>
        <rdfs:label xml:lang="en">Aqaba Price Forecast - Easter</rdfs:label>
    </rdf:Description>

    <!-- CQ-023: Popularity trends -->
    <rdf:Description rdf:about="{ns}PopObsPetra2025">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}PopularityObservation"/>
        <jto:forAttraction rdf:resource="{ns}PetraSite"/>
        <jto:trendDirection rdf:datatype="http://www.w3.org/2001/XMLSchema#string">increasing</jto:trendDirection>
        <jto:observationYear rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2025</jto:observationYear>
        <rdfs:label xml:lang="en">Petra Popularity 2025</rdfs:label>
    </rdf:Description>

    <!-- CQ-026: PROV-O provenance agent -->
    <rdf:Description rdf:about="{ns}JordanTourismBoardSource">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="http://www.w3.org/ns/prov#Agent"/>
        <rdfs:label xml:lang="en">Jordan Tourism Board</rdfs:label>
        <rdfs:label xml:lang="ar">هيئة تنشيط السياحة الأردنية</rdfs:label>
    </rdf:Description>

    <!-- CQ-027: Forecast model (already exists as JTOForecastModelV1 in v1.3) -->

    <!-- CQ-028: Bus Amman to Petra -->
    <rdf:Description rdf:about="{ns}JETTBusAmmanPetra">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}BusService"/>
        <jto:departureTime rdf:datatype="http://www.w3.org/2001/XMLSchema#string">06:30</jto:departureTime>
        <jto:travelDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#string">3.5 hours</jto:travelDuration>
        <jto:ticketPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">11.0</jto:ticketPrice>
        <rdfs:label xml:lang="en">JETT Bus Amman to Petra</rdfs:label>
        <rdfs:label xml:lang="ar">باص جت عمان - البتراء</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}RouteAmmanPetraBus">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <jto:originCity rdf:resource="{ns}AmmanCity"/>
        <jto:destinationCity rdf:resource="{ns}PetraCity"/>
        <jto:hasTransportService rdf:resource="{ns}JETTBusAmmanPetra"/>
        <jto:isDirectRoute rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:isDirectRoute>
        <rdfs:label xml:lang="en">Amman to Petra Bus Route</rdfs:label>
    </rdf:Description>

    <!-- CQ-029: Taxi airport to Amman -->
    <rdf:Description rdf:about="{ns}QueenAliaAirportIndividual">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}Airport"/>
        <rdfs:label xml:lang="en">Queen Alia International Airport</rdfs:label>
        <rdfs:label xml:lang="ar">مطار الملكة علياء الدولي</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}AirportTaxiService">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}TaxiService"/>
        <jto:priceRange rdf:datatype="http://www.w3.org/2001/XMLSchema#string">20-35 JOD</jto:priceRange>
        <rdfs:label xml:lang="en">Queen Alia Airport Taxi Service</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}RouteAirportAmmanTaxi">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <jto:originCity rdf:resource="{ns}QueenAliaAirportIndividual"/>
        <jto:destinationCity rdf:resource="{ns}AmmanCity"/>
        <jto:hasTransportService rdf:resource="{ns}AirportTaxiService"/>
        <rdfs:label xml:lang="en">Airport to Amman Taxi Route</rdfs:label>
    </rdf:Description>

    <!-- CQ-030: Direct bus Aqaba to Wadi Rum -->
    <rdf:Description rdf:about="{ns}WadiRumBusService">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}BusService"/>
        <jto:travelDuration rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1 hour</jto:travelDuration>
        <jto:ticketPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">5.0</jto:ticketPrice>
        <rdfs:label xml:lang="en">Aqaba to Wadi Rum Bus</rdfs:label>
    </rdf:Description>

    <rdf:Description rdf:about="{ns}RouteAqabaWadiRumBus">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <jto:originCity rdf:resource="{ns}AqabaCity"/>
        <jto:destinationCity rdf:resource="{ns}WadiRumArea"/>
        <jto:hasTransportService rdf:resource="{ns}WadiRumBusService"/>
        <jto:isDirectRoute rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</jto:isDirectRoute>
        <rdfs:label xml:lang="en">Aqaba to Wadi Rum Bus Route</rdfs:label>
    </rdf:Description>

""".format(ns=NS)


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: {INPUT_FILE} not found. Run from /Users/enadabuzaid/Desktop/Thesis/ontology/")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure prov namespace in root tag
    if 'xmlns:prov=' not in content:
        content = content.replace('<rdf:RDF', '<rdf:RDF xmlns:prov="http://www.w3.org/ns/prov#"', 1)
        print("+ Added prov namespace")

    # Ensure geo namespace in root tag
    if 'xmlns:geo=' not in content:
        content = content.replace('<rdf:RDF', '<rdf:RDF xmlns:geo="http://www.opengis.net/ont/geosparql#"', 1)
        print("+ Added geo namespace")

    # Skip duplicates
    existing = set(re.findall(r'rdf:about="([^"]+)"', content))
    to_add = NEW_INDIVIDUALS
    skipped = []
    for iri in re.findall(r'rdf:about="([^"]+)"', to_add):
        if iri in existing:
            name = iri.split('#')[-1]
            skipped.append(name)
            to_add = re.sub(
                rf'    <owl:NamedIndividual rdf:about="{re.escape(iri)}">.*?</owl:NamedIndividual>\n',
                '', to_add, flags=re.DOTALL)

    if skipped:
        print(f"Skipping {len(skipped)} existing: {', '.join(skipped)}")

    content = content.replace('</rdf:RDF>', to_add + '</rdf:RDF>')

    # Also delete old v1.5 if it exists
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    added = len(re.findall(r'<owl:NamedIndividual', to_add))
    total = len(re.findall(r'<owl:NamedIndividual', content))
    lines = content.count('\n') + 1
    print(f"\n=== JTO v1.5 BUILD SUCCESS ===")
    print(f"Output: {OUTPUT_FILE}")
    print(f"New: {added} | Total: {total} | Lines: {lines} | Skipped: {len(skipped)}")
    print(f"\nNEXT: Open {OUTPUT_FILE} in Protege -> re-run CQ-011-030")

if __name__ == "__main__":
    main()
