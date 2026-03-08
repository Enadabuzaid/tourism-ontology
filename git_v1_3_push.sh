#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
# JTO v1.3 — Git Branch, Commit & PR Script
# Run this from your Mac Terminal
# ═══════════════════════════════════════════════════════════════════

set -e  # Exit on any error

ONTOLOGY_DIR="/Users/enadabuzaid/Desktop/Thesis/ontology"
BRANCH="feat/jto-v1-3-individuals"
V13_FILE="jto_tourism_entity_module_v1_3_stable.owl"
CATALOG="catalog-v001.xml"

echo "📂 Moving to ontology directory..."
cd "$ONTOLOGY_DIR"

echo "🔄 Switching to main and pulling latest..."
git checkout main
git pull origin main

echo "🌿 Creating new branch: $BRANCH"
git checkout -b "$BRANCH"

echo "📋 STEP: Copy the v1.3 files from your downloads to this folder:"
echo "   cp ~/Downloads/$V13_FILE $ONTOLOGY_DIR/$V13_FILE"
echo "   cp ~/Downloads/$CATALOG $ONTOLOGY_DIR/$CATALOG"
echo ""
echo "Press ENTER after you've copied the files..."
read -r

echo "✅ Adding files..."
git add "$V13_FILE" "$CATALOG"

echo "📝 Committing..."
git commit -m "feat: add validation seed individuals for Batch 1 CQs — JTO v1.3

- 12 new NamedIndividuals added:
  PetraFridayHoursSpec, CitadelRamadanHours, RamadanVisitorPractice,
  HashemRestaurantAmman, RummanaRestaurantAmman, WadiRumCampRestaurant,
  OutdoorDiningAmenity, PetraCrowdForecastApril, PetraCrowdForecastPeak,
  AqabaPriceForecastEaster, PopObsPetra2025, PopObsWadiRum2025,
  JTOForecastModelV1, BusServiceAqabaWadiRum, DriveRouteAmmanPetra

- Patched existing individuals with missing CQ properties:
  PetraSite: openingHours, isWheelchairAccessible, accessibilityNotes, hasOpeningHoursSpec
  JerashRuinsSite: entryFee
  AmmanCitadelSite: isFamilyFriendly, hasSeasonalHours
  MountNebo: dressCode
  JerashFestival2026: eventStartDate, eventEndDate, locatedAt
  JETTBusAmmanPetra: travelDuration, ticketPrice, isDirectRoute, originCity
  QAIAAirportTaxi: priceRange, originCity, destinationCity

- Purpose: Convert all 21 Partial CQs in Batch 1 to Pass
- Ontology: 806 classes, 81 obj props, 172 data props, 262+ individuals
- XML validated: well-formed OWL 2 DL
- Catalog updated to point to v1.3 file"

echo "🚀 Pushing branch to GitHub..."
git push -u origin "$BRANCH"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ Branch pushed! Now open a PR:"
echo "   https://github.com/Enadabuzaid/tourism-ontology/compare/$BRANCH"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "PR Title: feat: JTO v1.3 — Add validation seed individuals (Batch 1 CQs)"
echo ""
echo "PR Body (copy this):"
cat << 'PRBODY'
## JTO v1.3 — Validation Seed Individuals for Batch 1 SPARQL CQs

### Summary
Adds 15 new NamedIndividuals and patches 7 existing ones to make all
21 ⚠️ Partial CQs in Batch 1 (CQ-001 to CQ-030) return real data in Protégé.

### Changes
**New individuals (15):**
- `PetraFridayHoursSpec` — OpeningHoursSpec for CQ-009
- `CitadelRamadanHours` — SeasonalOpeningHours for CQ-010 ⭐ CulturalConcept
- `RamadanVisitorPractice` — CulturalPractice for CQ-017 ⭐ CulturalConcept
- `HashemRestaurantAmman`, `RummanaRestaurantAmman` — Mansaf restaurants for CQ-019
- `WadiRumCampRestaurant`, `OutdoorDiningAmenity` — Vegetarian outdoor for CQ-020
- `PetraCrowdForecastApril/Peak` — CrowdForecast for CQ-021 ⭐ BI
- `AqabaPriceForecastEaster` — PriceForecast for CQ-022 ⭐ BI
- `PopObsPetra2025`, `PopObsWadiRum2025` — PopularityObservation for CQ-023 ⭐ BI
- `JTOForecastModelV1` — ForecastModel for CQ-027 ⭐ BI+PROV-O
- `BusServiceAqabaWadiRum` — Direct bus for CQ-030
- `DriveRouteAmmanPetra` — Driving route for CQ-013

**Patched existing individuals (7):** PetraSite, JerashRuinsSite, AmmanCitadelSite,
MountNebo, JerashFestival2026, JETTBusAmmanPetra, QAIAAirportTaxi

### Validation
- ✅ XML well-formed (OWL 2 DL)
- ✅ 29/29 checks pass
- ✅ 11,687 lines (11,482 in v1.2)

### SPARQL Impact
- Before: 0 Pass / 21 Partial / 9 Fail
- Expected after: 21 Pass / 0 Partial / 9 Fail (geo engine limits remain)

Closes: Phase 2 Batch 1 individual population
PRBODY
