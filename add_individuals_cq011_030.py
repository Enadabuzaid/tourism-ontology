#!/usr/bin/env python3
"""
JTO v1.5 — Add Missing Individuals for CQ-011 to CQ-030
=========================================================
Run this script from your ontology folder:
  cd /Users/enadabuzaid/Desktop/Thesis/ontology/
  python3 add_individuals_cq011_030.py

It reads jto_tourism_entity_module_v1_4_stable.owl,
adds individuals that make CQ-011–030 return actual rows in Protégé,
and saves as jto_tourism_entity_module_v1_5_stable.owl
"""

import re
import os
from datetime import datetime

INPUT_FILE = "jto_tourism_entity_module_v1_4_stable.owl"
OUTPUT_FILE = "jto_tourism_entity_module_v1_5_stable.owl"

# Canonical namespace
NS = "http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#"

# ============================================================
# NEW INDIVIDUALS — Each block targets a specific CQ
# ============================================================

NEW_INDIVIDUALS = """

    <!-- =====================================================
         CQ-011: Cultural events in Jerash in July
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}JerashFestival2025">
        <rdf:type rdf:resource="{ns}Festival"/>
        <locatedAt rdf:resource="{ns}JerashCity"/>
        <startDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-07-22</startDate>
        <endDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-08-10</endDate>
        <rdfs:label xml:lang="en">Jerash Festival of Culture and Arts 2025</rdfs:label>
        <rdfs:label xml:lang="ar">مهرجان جرش للثقافة والفنون 2025</rdfs:label>
        <rdfs:comment xml:lang="en">Annual cultural festival held at the ancient ruins of Jerash featuring music, dance, and theater performances.</rdfs:comment>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}AmmanSummerFestival2025">
        <rdf:type rdf:resource="{ns}Festival"/>
        <locatedAt rdf:resource="{ns}AmmanCity"/>
        <startDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-07-01</startDate>
        <endDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2025-07-15</endDate>
        <rdfs:label xml:lang="en">Amman Summer Festival 2025</rdfs:label>
        <rdfs:label xml:lang="ar">مهرجان عمان الصيفي 2025</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-013: Driving distance Amman to Petra
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}DriveRouteAmmanPetra">
        <rdf:type rdf:resource="{ns}DrivingRoute"/>
        <originCity rdf:resource="{ns}AmmanCity"/>
        <destinationCity rdf:resource="{ns}PetraCity"/>
        <drivingDistance>235 km</drivingDistance>
        <estimatedDuration>3 hours</estimatedDuration>
        <rdfs:label xml:lang="en">Amman to Petra Drive Route</rdfs:label>
        <rdfs:label xml:lang="ar">طريق القيادة من عمان إلى البتراء</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}DriveRouteDeadSeaPetra">
        <rdf:type rdf:resource="{ns}DrivingRoute"/>
        <originCity rdf:resource="{ns}DeadSeaArea"/>
        <destinationCity rdf:resource="{ns}PetraCity"/>
        <drivingDistance>280 km</drivingDistance>
        <estimatedDuration>3.5 hours</estimatedDuration>
        <rdfs:label xml:lang="en">Dead Sea to Petra Drive Route</rdfs:label>
        <rdfs:label xml:lang="ar">طريق القيادة من البحر الميت إلى البتراء</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-017: Visiting during Ramadan — Cultural practices
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}RamadanSeason">
        <rdf:type rdf:resource="{ns}ReligiousSeason"/>
        <rdfs:label xml:lang="en">Ramadan</rdfs:label>
        <rdfs:label xml:lang="ar">رمضان</rdfs:label>
        <rdfs:comment xml:lang="en">Islamic holy month of fasting observed throughout Jordan.</rdfs:comment>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}RamadanEatingPractice">
        <rdf:type rdf:resource="{ns}CulturalPractice"/>
        <appliesToSeason rdf:resource="{ns}RamadanSeason"/>
        <description>Avoid eating, drinking, or smoking in public during daylight hours out of respect for those fasting.</description>
        <rdfs:label xml:lang="en">Ramadan Public Eating Etiquette</rdfs:label>
        <rdfs:label xml:lang="ar">آداب الأكل العام في رمضان</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}RamadanDressPractice">
        <rdf:type rdf:resource="{ns}CulturalPractice"/>
        <appliesToSeason rdf:resource="{ns}RamadanSeason"/>
        <description>Dress more conservatively during Ramadan, especially near religious sites.</description>
        <rdfs:label xml:lang="en">Ramadan Dress Code Practice</rdfs:label>
        <rdfs:label xml:lang="ar">ممارسة اللباس في رمضان</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-019: Where to eat Mansaf in Amman
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}MansafDish">
        <rdf:type rdf:resource="{ns}Dish"/>
        <rdfs:label xml:lang="en">Mansaf</rdfs:label>
        <rdfs:label xml:lang="ar">منسف</rdfs:label>
        <rdfs:comment xml:lang="en">Jordan's national dish made with lamb, yogurt sauce, and rice.</rdfs:comment>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}HashemRestaurant">
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <servesDish rdf:resource="{ns}MansafDish"/>
        <locatedIn rdf:resource="{ns}AmmanCity"/>
        <hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">false</hasVegetarianOptions>
        <rdfs:label xml:lang="en">Hashem Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم هاشم</rdfs:label>
        <rdfs:comment xml:lang="en">Famous downtown Amman restaurant known for traditional Jordanian cuisine including Mansaf.</rdfs:comment>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}SufraRestaurant">
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <servesDish rdf:resource="{ns}MansafDish"/>
        <locatedIn rdf:resource="{ns}AmmanCity"/>
        <hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</hasVegetarianOptions>
        <rdfs:label xml:lang="en">Sufra Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم سفرة</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-020: Vegetarian restaurants with outdoor seating
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}OutdoorSeatingAmenity">
        <rdf:type rdf:resource="{ns}Amenity"/>
        <rdfs:label xml:lang="en">outdoor dining</rdfs:label>
        <rdfs:label xml:lang="ar">تناول الطعام في الهواء الطلق</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}WadiRumCampRestaurant">
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</hasVegetarianOptions>
        <hasAmenity rdf:resource="{ns}OutdoorSeatingAmenity"/>
        <locatedIn rdf:resource="{ns}WadiRumArea"/>
        <rdfs:label xml:lang="en">Wadi Rum Camp Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم مخيم وادي رم</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}FeynanEcolodgeRestaurant">
        <rdf:type rdf:resource="{ns}Restaurant"/>
        <hasVegetarianOptions rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</hasVegetarianOptions>
        <hasAmenity rdf:resource="{ns}OutdoorSeatingAmenity"/>
        <locatedIn rdf:resource="{ns}DanaReserve"/>
        <rdfs:label xml:lang="en">Feynan Ecolodge Restaurant</rdfs:label>
        <rdfs:label xml:lang="ar">مطعم فينان إيكولودج</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-021: When is Petra least crowded (BI CrowdForecast)
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}PetraCrowdForecastMorning">
        <rdf:type rdf:resource="{ns}CrowdForecast"/>
        <forAttraction rdf:resource="{ns}PetraSite"/>
        <timePeriod>Early morning weekdays</timePeriod>
        <predictedCrowdLevel rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</predictedCrowdLevel>
        <forecastConfidence rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.85</forecastConfidence>
        <generatedBy rdf:resource="{ns}ForecastModelV1"/>
        <rdfs:label xml:lang="en">Petra Crowd Forecast — Morning</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}PetraCrowdForecastAfternoon">
        <rdf:type rdf:resource="{ns}CrowdForecast"/>
        <forAttraction rdf:resource="{ns}PetraSite"/>
        <timePeriod>Weekend afternoons</timePeriod>
        <predictedCrowdLevel rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">8</predictedCrowdLevel>
        <forecastConfidence rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.78</forecastConfidence>
        <generatedBy rdf:resource="{ns}ForecastModelV1"/>
        <rdfs:label xml:lang="en">Petra Crowd Forecast — Afternoon</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-022: Hotel prices in Aqaba during Easter
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}AqabaPriceForecastEaster">
        <rdf:type rdf:resource="{ns}PriceForecast"/>
        <forLocation rdf:resource="{ns}AqabaCity"/>
        <forSeason>Easter</forSeason>
        <predictedAveragePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">85.0</predictedAveragePrice>
        <seasonalityScore rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.72</seasonalityScore>
        <rdfs:label xml:lang="en">Aqaba Price Forecast — Easter</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}AqabaPriceForecastSummer">
        <rdf:type rdf:resource="{ns}PriceForecast"/>
        <forLocation rdf:resource="{ns}AqabaCity"/>
        <forSeason>Summer</forSeason>
        <predictedAveragePrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">65.0</predictedAveragePrice>
        <seasonalityScore rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">0.55</seasonalityScore>
        <rdfs:label xml:lang="en">Aqaba Price Forecast — Summer</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-023: Attractions with increasing popularity
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}PopObsPetra2025">
        <rdf:type rdf:resource="{ns}PopularityObservation"/>
        <forAttraction rdf:resource="{ns}PetraSite"/>
        <trendDirection>increasing</trendDirection>
        <observationYear rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2025</observationYear>
        <rdfs:label xml:lang="en">Petra Popularity Observation 2025</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}PopObsWadiRum2025">
        <rdf:type rdf:resource="{ns}PopularityObservation"/>
        <forAttraction rdf:resource="{ns}WadiRumDesert"/>
        <trendDirection>increasing</trendDirection>
        <observationYear rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2025</observationYear>
        <rdfs:label xml:lang="en">Wadi Rum Popularity Observation 2025</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-024: Bilingual code-switching test
         (PetraSite should already have EN+AR labels from v1.4)
         ===================================================== -->


    <!-- =====================================================
         CQ-026: PROV-O provenance for Petra opening hours
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}PetraHoursProvenance">
        <rdf:type rdf:resource="http://www.w3.org/ns/prov#Entity"/>
        <prov:wasDerivedFrom rdf:resource="{ns}JordanTourismBoardSource"/>
        <prov:generatedAtTime rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2025-01-15T10:00:00</prov:generatedAtTime>
        <rdfs:label xml:lang="en">Petra Opening Hours Data</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}JordanTourismBoardSource">
        <rdf:type rdf:resource="http://www.w3.org/ns/prov#Agent"/>
        <rdfs:label xml:lang="en">Jordan Tourism Board</rdfs:label>
        <rdfs:label xml:lang="ar">هيئة تنشيط السياحة الأردنية</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-027: Forecast model metadata (BI + PROV-O)
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}ForecastModelV1">
        <rdf:type rdf:resource="{ns}ForecastModel"/>
        <trainingDataMonths rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">24</trainingDataMonths>
        <rdfs:label xml:lang="en">JTO Forecast Model v1</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-028: Bus from Amman to Petra
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}RouteAmmanPetraBus">
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <originCity rdf:resource="{ns}AmmanCity"/>
        <destinationCity rdf:resource="{ns}PetraCity"/>
        <hasTransportService rdf:resource="{ns}JETTBusAmmanPetra"/>
        <isDirectRoute rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</isDirectRoute>
        <rdfs:label xml:lang="en">Amman to Petra Bus Route</rdfs:label>
        <rdfs:label xml:lang="ar">خط باص عمان إلى البتراء</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}JETTBusAmmanPetra">
        <rdf:type rdf:resource="{ns}BusService"/>
        <departureTime>06:30</departureTime>
        <travelDuration>3.5 hours</travelDuration>
        <ticketPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">11.0</ticketPrice>
        <rdfs:label xml:lang="en">JETT Bus Amman to Petra</rdfs:label>
        <rdfs:label xml:lang="ar">باص جت عمان - البتراء</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-029: Taxi from airport to Amman
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}RouteAirportAmmanTaxi">
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <originCity rdf:resource="{ns}QueenAliaAirport"/>
        <destinationCity rdf:resource="{ns}AmmanCity"/>
        <hasTransportService rdf:resource="{ns}AirportTaxiService"/>
        <rdfs:label xml:lang="en">Airport to Amman Taxi Route</rdfs:label>
        <rdfs:label xml:lang="ar">خط تاكسي المطار - عمان</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}AirportTaxiService">
        <rdf:type rdf:resource="{ns}TaxiService"/>
        <priceRange>20-35 JOD</priceRange>
        <rdfs:label xml:lang="en">Queen Alia Airport Taxi Service</rdfs:label>
        <rdfs:label xml:lang="ar">خدمة تاكسي مطار الملكة علياء</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}QueenAliaAirport">
        <rdf:type rdf:resource="{ns}Airport"/>
        <rdfs:label xml:lang="en">Queen Alia International Airport</rdfs:label>
        <rdfs:label xml:lang="ar">مطار الملكة علياء الدولي</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         CQ-030: Direct bus Aqaba to Wadi Rum
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}RouteAqabaWadiRumBus">
        <rdf:type rdf:resource="{ns}TransportRoute"/>
        <originCity rdf:resource="{ns}AqabaCity"/>
        <destinationCity rdf:resource="{ns}WadiRumArea"/>
        <hasTransportService rdf:resource="{ns}WadiRumBusService"/>
        <isDirectRoute rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</isDirectRoute>
        <rdfs:label xml:lang="en">Aqaba to Wadi Rum Bus Route</rdfs:label>
        <rdfs:label xml:lang="ar">خط باص العقبة - وادي رم</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}WadiRumBusService">
        <rdf:type rdf:resource="{ns}BusService"/>
        <travelDuration>1 hour</travelDuration>
        <ticketPrice rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">5.0</ticketPrice>
        <rdfs:label xml:lang="en">Aqaba to Wadi Rum Bus</rdfs:label>
        <rdfs:label xml:lang="ar">باص العقبة - وادي رم</rdfs:label>
    </owl:NamedIndividual>


    <!-- =====================================================
         GeoSPARQL: Add geo:hasGeometry + WKT to key locations
         (These work in Apache Jena, NOT Protégé)
         ===================================================== -->

    <owl:NamedIndividual rdf:about="{ns}PetraSiteGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.4444 30.3285)</geo:asWKT>
        <rdfs:label xml:lang="en">Petra Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}RomanTheaterGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.9339 31.9510)</geo:asWKT>
        <rdfs:label xml:lang="en">Roman Theater Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}AmmanCitadelGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.9340 31.9522)</geo:asWKT>
        <rdfs:label xml:lang="en">Amman Citadel Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}DeadSeaGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.4732 31.5085)</geo:asWKT>
        <rdfs:label xml:lang="en">Dead Sea Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}WadiRumGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.4260 29.5722)</geo:asWKT>
        <rdfs:label xml:lang="en">Wadi Rum Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}JerashGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.8961 32.2746)</geo:asWKT>
        <rdfs:label xml:lang="en">Jerash Geometry</rdfs:label>
    </owl:NamedIndividual>

    <owl:NamedIndividual rdf:about="{ns}AqabaGeometry">
        <rdf:type rdf:resource="http://www.opengis.net/ont/geosparql#Geometry"/>
        <geo:asWKT rdf:datatype="http://www.opengis.net/ont/geosparql#wktLiteral">POINT(35.0063 29.5267)</geo:asWKT>
        <rdfs:label xml:lang="en">Aqaba Geometry</rdfs:label>
    </owl:NamedIndividual>

""".format(ns=NS)

# ============================================================
# GEO LINKS: Link existing sites to their geometries
# ============================================================

GEO_LINKS = """
    <!-- Link existing attraction individuals to their geometries -->
    <!-- Add these INSIDE existing individuals or as annotation patches -->
"""

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: {INPUT_FILE} not found in current directory.")
        print(f"Run this script from: /Users/enadabuzaid/Desktop/Thesis/ontology/")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        owl_content = f.read()

    # Check if geo namespace is declared
    if 'xmlns:geo=' not in owl_content:
        owl_content = owl_content.replace(
            'xmlns:prov="http://www.w3.org/ns/prov#"',
            'xmlns:prov="http://www.w3.org/ns/prov#"\n     xmlns:geo="http://www.opengis.net/ont/geosparql#"'
        )

    # Find the closing </rdf:RDF> tag and insert before it
    close_tag = '</rdf:RDF>'
    if close_tag not in owl_content:
        print("ERROR: Could not find </rdf:RDF> closing tag")
        return

    # Check for duplicates - skip individuals that already exist
    individuals_to_add = NEW_INDIVIDUALS
    existing_iris = re.findall(r'rdf:about="([^"]+)"', owl_content)

    new_iris = re.findall(r'rdf:about="([^"]+)"', individuals_to_add)
    skipped = []
    for iri in new_iris:
        if iri in existing_iris:
            skipped.append(iri.split('#')[-1])

    if skipped:
        print(f"NOTE: {len(skipped)} individuals already exist and will be skipped: {', '.join(skipped[:5])}...")
        for iri_local in skipped:
            full_iri = NS + iri_local
            # Remove the entire NamedIndividual block for this IRI
            pattern = rf'    <owl:NamedIndividual rdf:about="{re.escape(full_iri)}">.*?</owl:NamedIndividual>\n'
            individuals_to_add = re.sub(pattern, '', individuals_to_add, flags=re.DOTALL)

    # Insert new individuals
    owl_content = owl_content.replace(
        close_tag,
        f"\n    <!-- ========== JTO v1.5 INDIVIDUALS (Added {datetime.now().strftime('%Y-%m-%d')}) ========== -->\n"
        + individuals_to_add
        + "\n" + close_tag
    )

    # Write output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(owl_content)

    # Count
    new_count = len(re.findall(r'<owl:NamedIndividual', individuals_to_add))
    total_count = len(re.findall(r'<owl:NamedIndividual', owl_content))
    total_lines = owl_content.count('\n') + 1

    print(f"""
╔══════════════════════════════════════════════╗
║  JTO v1.5 BUILD COMPLETE                     ║
╠══════════════════════════════════════════════╣
║  Input:  {INPUT_FILE}
║  Output: {OUTPUT_FILE}
║  New individuals added:  {new_count}
║  Total individuals:      {total_count}
║  Total lines:            {total_lines}
║  Skipped (duplicates):   {len(skipped)}
╠══════════════════════════════════════════════╣
║  NEXT STEPS:                                 ║
║  1. Open {OUTPUT_FILE} in Protégé            ║
║  2. Re-run CQ-011–030 queries                ║
║  3. CQs should now return actual rows!       ║
║  4. For GeoSPARQL: use Apache Jena Fuseki    ║
╚══════════════════════════════════════════════╝
""")

if __name__ == "__main__":
    main()
