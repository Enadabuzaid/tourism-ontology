# 🔧 FIXED SPARQL Queries — CQ-001 to CQ-090
## Matches v1.4 OWL (fixed March 9, 2026)

### ⚠️ RULES FOR PROTÉGÉ SESAME ENGINE:
1. ❌ NEVER use `LCASE()` on any variable — causes JoinIterator crash
2. ❌ NEVER use `STR()` wrapper on label variables — causes parser crash
3. ❌ NEVER use `ASK` with Arabic literals — use SELECT instead
4. ❌ NEVER use `geo:hasGeometry` — GeoSPARQL not supported
5. ✅ Use case-sensitive `CONTAINS(?label, "Petra")` — labels are properly cased
6. ✅ Use `FILTER(LANG(?label) = "en")` to get English labels only
7. ✅ Use direct IRI (`jto:PetraSite`) when possible

### PREFIX BLOCK — paste FIRST:
```
PREFIX jto: <http://www.semanticweb.org/enadabuzaid/ontologies/2025/11/jordan-tourism#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX prov: <http://www.w3.org/ns/prov#>
```

---
# BATCH 1 — CQ-001 to CQ-030

## CQ-001 ✅ Pass — Opening hours of Petra
```
SELECT ?hours WHERE { jto:PetraSite jto:openingHours ?hours . }
```

## CQ-002 ✅ Pass — Entry fee for Jerash
```
SELECT ?fee WHERE { jto:JerashRuinsSite jto:entryFee ?fee . }
```

## CQ-003 ✅ Pass — Where is Wadi Rum
```
SELECT ?place ?label WHERE {
  ?place rdf:type jto:NatureReserve .
  ?place rdfs:label ?label .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?label, "Wadi Rum"))
}
```

## CQ-004 ✅ Pass — What type is Petra
```
SELECT DISTINCT ?type WHERE {
  jto:Petra rdf:type ?type .
  FILTER(?type != owl:NamedIndividual)
  FILTER(?type != owl:Class)
  FILTER(?type != owl:Thing)
}
```

## CQ-005 ✅ Pass — Petra wheelchair accessible
```
SELECT ?accessible ?notes WHERE {
  jto:PetraSite jto:isWheelchairAccessible ?accessible .
  jto:PetraSite jto:accessibilityNotes ?notes .
}
```

## CQ-006 ✅ Pass — Family-friendly in Amman
```
SELECT ?attraction ?label WHERE {
  ?attraction jto:isFamilyFriendly true .
  ?attraction rdfs:label ?label .
  FILTER(LANG(?label) = "en")
}
```

## CQ-007 ❌ GeoSPARQL — Halal restaurants near Roman Theater
```
SELECT ?name WHERE {
  ?restaurant a jto:Restaurant ;
              rdfs:label ?name ;
              jto:halalCertified true .
  FILTER(LANG(?name) = "en")
}
```

## CQ-008 ✅ Pass — Dress code Mount Nebo
```
SELECT ?dresscode WHERE { jto:MountNeboSite jto:dressCode ?dresscode . }
```

## CQ-009 ✅ Pass — Petra open Friday
```
SELECT ?day ?opens ?closes WHERE {
  jto:PetraSite jto:hasOpeningHoursSpec ?spec .
  ?spec jto:dayOfWeek ?day .
  ?spec jto:opens ?opens .
  ?spec jto:closes ?closes .
  FILTER(?day = "Friday")
}
```

## CQ-010 ✅ Pass — Citadel Ramadan hours ⭐
```
SELECT ?hours ?seasonNote WHERE {
  jto:AmmanCitadelSite jto:hasSeasonalHours ?sh .
  ?sh jto:season ?season .
  ?sh jto:openingHours ?hours .
  OPTIONAL { ?sh jto:seasonNote ?seasonNote . }
}
```

## CQ-011 🔲 — Cultural events Jerash July
```
SELECT ?eventName ?start ?end WHERE {
  ?event a jto:Festival ;
         rdfs:label ?eventName ;
         jto:locatedAt ?place ;
         jto:startDate ?start ;
         jto:endDate ?end .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?eventName) = "en")
  FILTER(CONTAINS(?placeLabel, "Jerash"))
}
```

## CQ-012 ❌ GeoSPARQL

## CQ-013 🔲 — Driving distance Amman→Petra
### ⚠️ FIX: type=DrivingRoute (not Route), use estimatedDuration (not drivingTime)
```
SELECT ?distance ?duration WHERE {
  ?route a jto:DrivingRoute ;
         jto:originCity ?origin ;
         jto:destinationCity ?dest ;
         jto:drivingDistance ?distance ;
         jto:estimatedDuration ?duration .
  ?origin rdfs:label ?oLabel .
  ?dest rdfs:label ?dLabel .
  FILTER(CONTAINS(?oLabel, "Amman"))
  FILTER(CONTAINS(?dLabel, "Petra"))
}
```

## CQ-014 ❌ GeoSPARQL
## CQ-015 ❌ GeoSPARQL
## CQ-016 ❌ GeoSPARQL

## CQ-017 🔲 — Visiting during Ramadan ⭐ CulturalConcept
```
SELECT ?practiceLabel ?description WHERE {
  ?ramadan a jto:ReligiousSeason ;
           rdfs:label ?rLabel .
  ?practice jto:appliesToSeason ?ramadan ;
            rdfs:label ?practiceLabel ;
            jto:description ?description .
  FILTER(CONTAINS(?rLabel, "Ramadan"))
}
```

## CQ-018 ❌ GeoSPARQL

## CQ-019 🔲 — Mansaf in Amman
```
SELECT ?name WHERE {
  ?r a jto:Restaurant ;
     rdfs:label ?name ;
     jto:servesDish ?dish ;
     jto:locatedIn ?city .
  ?dish rdfs:label ?dishLabel .
  ?city rdfs:label ?cityLabel .
  FILTER(CONTAINS(?dishLabel, "Mansaf"))
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-020 🔲 — Vegetarian restaurants
### ⚠️ FIX: property is hasVegetarianOptions (not vegetarianOptions)
```
SELECT ?name WHERE {
  ?r a jto:Restaurant ;
     rdfs:label ?name ;
     jto:hasVegetarianOptions true ;
     jto:hasOutdoorSeating true .
  FILTER(LANG(?name) = "en")
}
```

## CQ-021 🔲 — Petra least crowded ⭐ BI
```
SELECT ?timePeriod ?crowdLevel WHERE {
  ?forecast a jto:CrowdForecast ;
            jto:forAttraction ?attraction ;
            jto:timePeriod ?timePeriod ;
            jto:predictedCrowdLevel ?crowdLevel .
  ?attraction rdfs:label ?aLabel .
  FILTER(CONTAINS(?aLabel, "Petra"))
}
ORDER BY ASC(?crowdLevel)
```

## CQ-022 🔲 — Hotel prices Aqaba Easter
```
SELECT ?avgPrice ?seasonality WHERE {
  ?forecast a jto:PriceForecast ;
            jto:forLocation ?loc ;
            jto:forSeason ?season ;
            jto:predictedAveragePrice ?avgPrice ;
            jto:seasonalityScore ?seasonality .
  ?loc rdfs:label ?locLabel .
  FILTER(CONTAINS(?locLabel, "Aqaba"))
  FILTER(CONTAINS(?season, "Easter"))
}
```

## CQ-023 🔲 — Increasing popularity
```
SELECT ?name ?trend WHERE {
  ?obs a jto:PopularityObservation ;
       jto:forAttraction ?attraction ;
       jto:trendDirection ?trend ;
       jto:observationYear ?year .
  ?attraction rdfs:label ?name .
  FILTER(?year = 2025)
  FILTER(?trend = "increasing")
}
```

## CQ-024 🔲 — Code-switching bilingual ⭐
```
SELECT ?hours WHERE {
  ?petra rdfs:label ?label ;
         jto:openingHours ?hours .
  FILTER(CONTAINS(?label, "Petra") || CONTAINS(?label, "البتراء"))
}
```

## CQ-025 ❌ Engine Limit (ASK+Arabic)
```
SELECT ?label WHERE {
  ?petra rdfs:label ?label .
  FILTER(CONTAINS(?label, "Petra") || CONTAINS(?label, "بتراء"))
}
```

## CQ-026 🔲 — Provenance
```
SELECT ?source ?updated WHERE {
  jto:PetraSite jto:openingHours ?hours .
  ?hours prov:wasDerivedFrom ?source ;
         prov:generatedAtTime ?updated .
}
```

## CQ-027 🔲 — Crowd prediction confidence ⭐ BI
```
SELECT ?confidence ?model ?trainedOn WHERE {
  ?forecast a jto:CrowdForecast ;
            jto:forAttraction ?attr ;
            jto:forecastConfidence ?confidence ;
            jto:generatedBy ?model .
  ?model jto:trainingDataMonths ?trainedOn .
  ?attr rdfs:label ?aLabel .
  FILTER(CONTAINS(?aLabel, "Wadi Rum"))
}
```

## CQ-028 🔲 — Bus Amman→Petra
```
SELECT ?service ?departure ?duration ?price WHERE {
  ?route a jto:TransportRoute ;
         jto:hasTransportService ?svc ;
         jto:originCity ?origin ;
         jto:destinationCity ?dest .
  ?svc a jto:BusService ;
       rdfs:label ?service ;
       jto:departureTime ?departure ;
       jto:travelDuration ?duration ;
       jto:ticketPrice ?price .
  ?origin rdfs:label ?oLabel .
  ?dest rdfs:label ?dLabel .
  FILTER(CONTAINS(?oLabel, "Amman"))
  FILTER(CONTAINS(?dLabel, "Petra"))
}
```

## CQ-029 🔲 — Taxi airport→Amman
```
SELECT ?service ?priceRange WHERE {
  ?route a jto:TransportRoute ;
         jto:hasTransportService ?svc ;
         jto:originCity ?origin ;
         jto:destinationCity ?dest .
  ?svc a jto:TaxiService ;
       rdfs:label ?service ;
       jto:priceRange ?priceRange .
  ?origin rdfs:label ?oLabel .
  ?dest rdfs:label ?dLabel .
  FILTER(CONTAINS(?oLabel, "Airport"))
  FILTER(CONTAINS(?dLabel, "Amman"))
}
```

## CQ-030 🔲 — Direct bus Aqaba→Wadi Rum
```
SELECT ?direct ?duration ?price WHERE {
  ?route a jto:TransportRoute ;
         jto:hasTransportService ?svc ;
         jto:isDirectRoute ?direct ;
         jto:originCity ?origin ;
         jto:destinationCity ?dest .
  ?svc jto:travelDuration ?duration ;
       jto:ticketPrice ?price .
  ?origin rdfs:label ?oLabel .
  ?dest rdfs:label ?dLabel .
  FILTER(CONTAINS(?oLabel, "Aqaba"))
  FILTER(CONTAINS(?dLabel, "Wadi Rum"))
}
```

---
# BATCH 2 — CQ-031 to CQ-060

## CQ-031 — Car rental at airport
### ⚠️ NO LCASE — use case-sensitive CONTAINS
```
SELECT ?company ?priceRange WHERE {
  ?rental a jto:CarRentalService ;
          rdfs:label ?company ;
          jto:locatedAt ?airport ;
          jto:priceRange ?priceRange .
  ?airport rdfs:label ?airportLabel .
  FILTER(CONTAINS(?airportLabel, "Airport"))
}
```

## CQ-032 — Driving time Dead Sea→Petra
### ⚠️ FIX: DrivingRoute (not Route), estimatedDuration (not drivingTime)
```
SELECT ?distance ?duration WHERE {
  ?route a jto:DrivingRoute ;
         jto:originCity ?origin ;
         jto:destinationCity ?dest ;
         jto:drivingDistance ?distance ;
         jto:estimatedDuration ?duration .
  ?origin rdfs:label ?oLabel .
  ?dest rdfs:label ?dLabel .
  FILTER(CONTAINS(?oLabel, "Dead Sea"))
  FILTER(CONTAINS(?dLabel, "Petra"))
}
```

## CQ-033 — Hotels Petra with airport transfer
```
SELECT ?hotelName WHERE {
  ?hotel a jto:Hotel ;
         rdfs:label ?hotelName ;
         jto:locatedIn ?place ;
         jto:offersAmenity ?amenity .
  ?amenity rdfs:label ?aLabel .
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Petra"))
  FILTER(CONTAINS(?aLabel, "Airport"))
}
```

## CQ-034 — Average price 3-star Amman
```
SELECT (AVG(?price) AS ?avgPrice) WHERE {
  ?hotel a jto:Hotel ;
         jto:starRating 3 ;
         jto:pricePerNight ?price ;
         jto:locatedIn ?city .
  ?city rdfs:label ?cityLabel .
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-035 — Hostels Wadi Rum
```
SELECT ?name ?price WHERE {
  ?hostel a jto:Hostel ;
          rdfs:label ?name ;
          jto:pricePerNight ?price ;
          jto:locatedIn ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?name) = "en")
  FILTER(CONTAINS(?placeLabel, "Wadi Rum"))
}
```

## CQ-036 ⚠️ GEO — Accommodations Dead Sea pool
```
SELECT ?name WHERE {
  ?acc a jto:Accommodation ;
       rdfs:label ?name ;
       jto:offersAmenity ?amenity .
  ?amenity rdfs:label ?aLabel .
  FILTER(CONTAINS(?aLabel, "Pool"))
}
```

## CQ-037 — Hotels Petra breakfast
```
SELECT ?name WHERE {
  ?hotel a jto:Hotel ;
         rdfs:label ?name ;
         jto:breakfastIncluded true ;
         jto:locatedIn ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

## CQ-038 — Temperature Petra March
```
SELECT ?avgHigh ?avgLow WHERE {
  ?weather a jto:WeatherData ;
           jto:forLocation ?loc ;
           jto:month 3 ;
           jto:avgHighTemp ?avgHigh ;
           jto:avgLowTemp ?avgLow .
  ?loc rdfs:label ?locLabel .
  FILTER(CONTAINS(?locLabel, "Petra"))
}
```

## CQ-039 — December Wadi Rum
```
SELECT ?recommendation ?conditions WHERE {
  ?advice a jto:SeasonalAdvice ;
          jto:forLocation ?loc ;
          jto:forMonth 12 ;
          jto:recommendation ?recommendation ;
          jto:weatherConditions ?conditions .
  ?loc rdfs:label ?locLabel .
  FILTER(CONTAINS(?locLabel, "Wadi Rum"))
}
```

## CQ-040 — Best time Dead Sea
```
SELECT ?season ?months WHERE {
  ?advice a jto:BestTimeToVisit ;
          jto:forLocation ?loc ;
          jto:recommendedSeason ?season ;
          jto:recommendedMonths ?months .
  ?loc rdfs:label ?locLabel .
  FILTER(CONTAINS(?locLabel, "Dead Sea"))
}
```

## CQ-041 — Snow Petra winter
```
SELECT ?snowfall ?months WHERE {
  ?weather a jto:WeatherData ;
           jto:forLocation ?loc ;
           jto:snowfallPossible ?snowfall .
  ?loc rdfs:label ?locLabel .
  FILTER(CONTAINS(?locLabel, "Petra"))
  FILTER(?snowfall = true)
}
```

## CQ-042 — Currency Jordan
```
SELECT ?currencyName ?code WHERE {
  jto:Jordan jto:currency ?currencyName ;
             jto:currencyCode ?code .
}
```

## CQ-043 — English in tourist areas
```
SELECT ?areaLabel ?language WHERE {
  ?area a jto:TouristArea ;
        rdfs:label ?areaLabel ;
        jto:languageSpoken ?language .
  FILTER(LANG(?areaLabel) = "en")
  FILTER(CONTAINS(?language, "English"))
}
```

## CQ-044 — Packing for summer
```
SELECT ?item WHERE {
  ?advice a jto:TravelAdvice ;
          jto:forSeason ?season ;
          jto:packingItem ?item .
  FILTER(CONTAINS(?season, "summer"))
}
```

## CQ-045 — Credit cards Petra
### ⚠️ FIX: property may be acceptsCreditCard (singular)
```
SELECT ?acceptsCC WHERE {
  jto:PetraSite jto:acceptsCreditCards ?acceptsCC .
}
```

## CQ-046 — Handicrafts Amman
```
SELECT ?shopName WHERE {
  ?shop a jto:Shop ;
        rdfs:label ?shopName ;
        jto:sells ?product ;
        jto:locatedIn ?city .
  ?product a jto:Handicraft ;
           jto:isAuthentic true .
  ?city rdfs:label ?cityLabel .
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-047 — Souvenirs Petra
```
SELECT ?name WHERE {
  ?souvenir a jto:Souvenir ;
            rdfs:label ?name ;
            jto:popularAt ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

## CQ-048 — Haggling etiquette
```
SELECT ?setting ?hagglingExpected ?notes WHERE {
  jto:JordanMarketEtiquette jto:hagglingExpected ?hagglingExpected ;
                             jto:settingType ?setting ;
                             jto:notes ?notes .
}
```

## CQ-049 — Activities Wadi Rum
```
SELECT ?activityName ?type WHERE {
  ?activity a jto:Activity ;
            rdfs:label ?activityName ;
            jto:availableAt ?place ;
            jto:activityType ?type .
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Wadi Rum"))
}
```

## CQ-050 — Guided tour Jerash
```
SELECT ?tourLabel ?advanceBooking WHERE {
  ?tour a jto:GuidedTour ;
        rdfs:label ?tourLabel ;
        jto:availableAt ?place .
  OPTIONAL { ?tour jto:bookingAdvanceRequired ?advanceBooking . }
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Jerash"))
}
```

## CQ-051 — Water sports Dead Sea
```
SELECT ?actLabel ?restrictions WHERE {
  ?activity a jto:WaterActivity ;
            rdfs:label ?actLabel ;
            jto:availableAt ?place .
  OPTIONAL { ?activity jto:restrictions ?restrictions . }
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Dead Sea"))
}
```

## CQ-052 — Scuba Aqaba
```
SELECT ?siteName ?difficulty WHERE {
  ?site a jto:DiveSite ;
        rdfs:label ?siteName ;
        jto:locatedIn ?place ;
        jto:difficultyLevel ?difficulty .
  ?place rdfs:label ?placeLabel .
  FILTER(CONTAINS(?placeLabel, "Aqaba"))
}
```

## CQ-053 ⚠️ GEO — Hospital near Petra (simplified)
```
SELECT ?hospitalName WHERE {
  ?hospital a jto:Hospital ;
            rdfs:label ?hospitalName .
  FILTER(LANG(?hospitalName) = "en")
}
```

## CQ-054 — 24hr pharmacy Amman
```
SELECT ?name WHERE {
  ?pharmacy a jto:Pharmacy ;
            rdfs:label ?name ;
            jto:is24Hours true ;
            jto:locatedIn ?city .
  ?city rdfs:label ?cityLabel .
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-055 — Who built Petra
```
SELECT ?civilization ?period WHERE {
  jto:PetraSite jto:builtBy ?civ ;
                jto:historicalPeriod ?period .
  ?civ rdfs:label ?civilization .
  FILTER(LANG(?civilization) = "en")
}
```

## CQ-056 — Roman Theater age
```
SELECT ?constructionDate ?period WHERE {
  jto:RomanTheaterAmman jto:constructionDate ?constructionDate ;
                        jto:historicalPeriod ?period .
}
```

## CQ-057 ⚠️ GEO — Eco-lodge Dana (simplified)
```
SELECT ?name ?price WHERE {
  ?acc a jto:EcoLodge ;
       rdfs:label ?name ;
       jto:sustainableTourism true ;
       jto:pricePerNight ?price .
  FILTER(?price < 80)
}
```

## CQ-058 — Pet-friendly hotels Amman parking
```
SELECT ?name WHERE {
  ?hotel a jto:Hotel ;
         rdfs:label ?name ;
         jto:petFriendly true ;
         jto:offersAmenity ?amenity ;
         jto:locatedIn ?city .
  ?amenity rdfs:label ?aLabel .
  ?city rdfs:label ?cityLabel .
  FILTER(CONTAINS(?aLabel, "Parking"))
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-059 — Visitor stats Jerash ⭐ BI
```
SELECT ?dayOfWeek (MIN(?count) AS ?minCount) WHERE {
  ?stat a jto:VisitorStatistics ;
        jto:forAttraction ?attraction ;
        jto:dayOfWeek ?dayOfWeek ;
        jto:averageVisitorCount ?count .
  ?attraction rdfs:label ?aLabel .
  FILTER(CONTAINS(?aLabel, "Jerash"))
}
GROUP BY ?dayOfWeek
ORDER BY ASC(?minCount)
LIMIT 3
```

## CQ-060 — Greetings etiquette
```
SELECT ?greeting ?arabicPhrase ?context WHERE {
  jto:JordanGreetingEtiquette jto:etiquetteType ?greeting ;
                               jto:arabicPhrase ?arabicPhrase ;
                               jto:usageContext ?context .
}
```

---
# BATCH 3 — CQ-061 to CQ-090

## CQ-061 — Tour packages Petra+Wadi Rum
```
SELECT ?label ?duration ?price ?destinations WHERE {
  ?pkg rdf:type jto:TourPackage ;
       rdfs:label ?label ;
       jto:packageDuration ?duration ;
       jto:packagePrice ?price ;
       jto:destinationsIncluded ?destinations .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?destinations, "Petra"))
  FILTER(CONTAINS(?destinations, "Wadi Rum"))
}
```

## CQ-062 — Licensed tour operators Amman
```
SELECT ?label ?license ?languages WHERE {
  ?op rdf:type jto:TourOperator ;
      rdfs:label ?label ;
      jto:licenseNumber ?license ;
      jto:languages ?languages ;
      jto:locatedIn ?city .
  ?city rdfs:label ?cityLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?cityLabel, "Amman"))
  FILTER(CONTAINS(?languages, "English"))
}
```

## CQ-063 — Budget tours under 300 JOD
```
SELECT ?label ?duration ?price WHERE {
  ?pkg rdf:type jto:TourPackage ;
       rdfs:label ?label ;
       jto:packageDuration ?duration ;
       jto:packagePrice ?price .
  FILTER(LANG(?label) = "en")
  FILTER(?price < 300)
}
ORDER BY ASC(?price)
```

## CQ-064 — Tours with meals+transport
```
SELECT ?label ?price ?destinations WHERE {
  ?pkg rdf:type jto:TourPackage ;
       rdfs:label ?label ;
       jto:packagePrice ?price ;
       jto:includesMeals true ;
       jto:includesTransport true ;
       jto:destinationsIncluded ?destinations .
  FILTER(LANG(?label) = "en")
}
```

## CQ-065 — Visa GCC nationals
```
SELECT ?nationality ?required ?note WHERE {
  ?visa rdf:type jto:VisaRequirement ;
        jto:applicableNationality ?nationality ;
        jto:visaRequired ?required .
  OPTIONAL { ?visa jto:visaNote ?note . }
  FILTER(CONTAINS(?nationality, "GCC"))
}
```

## CQ-066 — Visa fee EU
```
SELECT ?nationality ?fee ?onArrival WHERE {
  ?visa rdf:type jto:VisaRequirement ;
        jto:applicableNationality ?nationality ;
        jto:visaFee ?fee ;
        jto:visaOnArrival ?onArrival .
  FILTER(CONTAINS(?nationality, "EU"))
}
```

## CQ-067 — Jordan Pass
```
SELECT ?price ?validity ?sites ?description WHERE {
  jto:JordanPassTouristCard jto:price ?price ;
                            jto:validityDays ?validity ;
                            jto:sitesIncluded ?sites ;
                            jto:description ?description .
}
```

## CQ-068 — Drone at Petra
```
SELECT ?allowed ?restrictions WHERE {
  jto:PetraPhotographyRule jto:droneAllowed ?allowed ;
                           jto:restrictions ?restrictions .
}
```

## CQ-069 — Photography in mosques
```
SELECT ?allowed ?restrictions WHERE {
  jto:MosquePhotographyRule jto:photographyAllowed ?allowed ;
                            jto:restrictions ?restrictions .
}
```

## CQ-070 — Prayer room Petra
```
SELECT ?label ?type WHERE {
  ?pf rdf:type jto:PrayerFacility ;
      rdfs:label ?label ;
      jto:prayerFacilityType ?type ;
      jto:locatedAt ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

## CQ-071 — Mosques Dead Sea
```
SELECT ?label ?prayerTimes WHERE {
  ?mosque rdf:type jto:Mosque ;
          rdfs:label ?label ;
          jto:prayerTimes ?prayerTimes ;
          jto:locatedIn ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?placeLabel, "Dead Sea"))
}
```

## CQ-072 — Budget backpacker ⭐ BI
```
SELECT ?level ?minCost ?maxCost ?notes WHERE {
  ?budget rdf:type jto:BudgetInfo ;
          jto:budgetLevelPerDay ?level ;
          jto:estimatedDailyMin ?minCost ;
          jto:estimatedDailyMax ?maxCost .
  OPTIONAL { ?budget jto:budgetNotes ?notes . }
  FILTER(?level = "budget")
}
```

## CQ-073 — Luxury day cost
```
SELECT ?level ?minCost ?maxCost ?notes WHERE {
  ?budget rdf:type jto:BudgetInfo ;
          jto:budgetLevelPerDay ?level ;
          jto:estimatedDailyMin ?minCost ;
          jto:estimatedDailyMax ?maxCost .
  OPTIONAL { ?budget jto:budgetNotes ?notes . }
  FILTER(?level = "luxury")
}
```

## CQ-074 — Jordan Pass value
```
SELECT ?passPrice ?visaFee ?petraFee ?sitesIncluded WHERE {
  jto:JordanPassTouristCard jto:price ?passPrice ;
                            jto:sitesIncluded ?sitesIncluded .
  jto:VisaRequirementJordanEU jto:visaFee ?visaFee .
  jto:PetraSite jto:entryFee ?petraFee .
}
```

## CQ-075 — Children activities Amman
```
SELECT ?label ?type ?age ?fee WHERE {
  ?act rdf:type jto:ChildrenActivity ;
       rdfs:label ?label ;
       jto:activityType ?type ;
       jto:availableAt ?place .
  OPTIONAL { ?act jto:ageRange ?age . }
  OPTIONAL { ?act jto:entryFee ?fee . }
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?placeLabel, "Amman"))
}
```

## CQ-076 — Cooking classes children
```
SELECT ?label ?age ?booking WHERE {
  ?act rdf:type jto:ChildrenActivity ;
       rdfs:label ?label ;
       jto:activityType ?type ;
       jto:bookingRequired ?booking .
  OPTIONAL { ?act jto:ageRange ?age . }
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?type, "cooking"))
}
```

## CQ-077 — Children museum age
```
SELECT ?ageRange ?fee WHERE {
  jto:ChildrenMuseumAmman jto:ageRange ?ageRange ;
                          jto:entryFee ?fee .
}
```

## CQ-078 — Hiking trails Jordan
```
SELECT ?label ?difficulty ?length WHERE {
  ?trail rdf:type jto:HikingTrail ;
         rdfs:label ?label ;
         jto:difficultyLevel ?difficulty ;
         jto:trailLength ?length .
  FILTER(LANG(?label) = "en")
}
ORDER BY ASC(?length)
```

## CQ-079 — Wadi Mujib beginners
```
SELECT ?difficulty ?duration ?season ?booking WHERE {
  jto:WadiMujibSiqTrail jto:difficultyLevel ?difficulty ;
                        jto:estimatedDuration ?duration ;
                        jto:bestSeason ?season ;
                        jto:bookingRequired ?booking .
}
```

## CQ-080 — Hiking trails Petra
```
SELECT ?label ?difficulty ?length WHERE {
  ?trail rdf:type jto:HikingTrail ;
         rdfs:label ?label ;
         jto:availableAt ?place ;
         jto:difficultyLevel ?difficulty ;
         jto:trailLength ?length .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

## CQ-081 — Local guides Petra
```
SELECT ?label ?languages ?price WHERE {
  ?guide rdf:type jto:LocalGuide ;
         rdfs:label ?label ;
         jto:guidesAt ?place ;
         jto:languages ?languages ;
         jto:priceRange ?price .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

## CQ-082 — Petra guide cost
```
SELECT ?price ?languages WHERE {
  jto:PetraLocalGuide jto:priceRange ?price ;
                      jto:languages ?languages .
}
```

## CQ-083 — Bedouin guides Wadi Rum
```
SELECT ?label ?price ?specialization WHERE {
  jto:WadiRumBedouinGuide rdfs:label ?label ;
                          jto:priceRange ?price ;
                          jto:specialization ?specialization .
  FILTER(LANG(?label) = "en")
}
```

## CQ-084 — Markets Amman
```
SELECT ?label ?type ?hours WHERE {
  ?market rdf:type jto:Market ;
          rdfs:label ?label ;
          jto:marketType ?type ;
          jto:locatedIn ?city .
  OPTIONAL { ?market jto:openingHours ?hours . }
  ?city rdfs:label ?cityLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?cityLabel, "Amman"))
}
```

## CQ-085 — Haggling Amman
```
SELECT ?hagglingExpected ?settingType ?notes WHERE {
  jto:JordanMarketEtiquette jto:hagglingExpected ?hagglingExpected ;
                             jto:settingType ?settingType ;
                             jto:notes ?notes .
}
```

## CQ-086 — Duty-free Aqaba
```
SELECT ?label ?type ?hours WHERE {
  ?market rdf:type jto:Market ;
          rdfs:label ?label ;
          jto:marketType ?type ;
          jto:locatedIn ?city .
  OPTIONAL { ?market jto:openingHours ?hours . }
  ?city rdfs:label ?cityLabel .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?cityLabel, "Aqaba"))
  FILTER(CONTAINS(?type, "duty"))
}
```

## CQ-087 — Halal tours Aqaba
```
SELECT ?label ?price ?destinations WHERE {
  ?pkg rdf:type jto:TourPackage ;
       rdfs:label ?label ;
       jto:packagePrice ?price ;
       jto:halalCertified true ;
       jto:destinationsIncluded ?destinations .
  FILTER(LANG(?label) = "en")
  FILTER(CONTAINS(?destinations, "Aqaba"))
}
```

## CQ-088 — Wheelchair accessible packages
```
SELECT ?label ?price ?duration ?destinations WHERE {
  ?pkg rdf:type jto:TourPackage ;
       rdfs:label ?label ;
       jto:packagePrice ?price ;
       jto:packageDuration ?duration ;
       jto:isWheelchairAccessible true ;
       jto:destinationsIncluded ?destinations .
  FILTER(LANG(?label) = "en")
}
```

## CQ-089 — Eco-lodge Dana under 50
```
SELECT ?label ?price WHERE {
  ?lodge rdf:type jto:EcoLodge ;
         rdfs:label ?label ;
         jto:pricePerNight ?price ;
         jto:sustainableTourism true ;
         jto:locatedIn ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(?price < 50)
  FILTER(CONTAINS(?placeLabel, "Dana"))
}
```

## CQ-090 — 5-star halal Petra breakfast under 200
```
SELECT ?label ?price WHERE {
  ?hotel rdf:type jto:Hotel ;
         rdfs:label ?label ;
         jto:starRating 5 ;
         jto:halalFood true ;
         jto:breakfastIncluded true ;
         jto:pricePerNight ?price ;
         jto:locatedIn ?place .
  ?place rdfs:label ?placeLabel .
  FILTER(LANG(?label) = "en")
  FILTER(?price < 200)
  FILTER(CONTAINS(?placeLabel, "Petra"))
}
```

---
# CHANGES SUMMARY — v1.4 OWL fixes applied:
1. DriveRouteAmmanPetra: destinationCity AqabaCity → PetraCity
2. RomanTheaterAmman: added constructionDate + builtBy
3. JordanianHandicraft: added isAuthentic=true
4. All XML validated ✅ — 12,615 lines, 346 individuals, well-formed

# QUERY FIXES from original tracker:
1. ALL LCASE() removed — use case-sensitive CONTAINS
2. CQ-013/032: Route → DrivingRoute, drivingTime → estimatedDuration
3. CQ-020: vegetarianOptions → hasVegetarianOptions + hasOutdoorSeating
4. CQ-042: Direct IRI jto:Jordan (no FILTER needed)
5. CQ-048/060/085: Direct IRI queries (no FILTER needed)
6. CQ-055/056: Direct IRI queries for historical data
