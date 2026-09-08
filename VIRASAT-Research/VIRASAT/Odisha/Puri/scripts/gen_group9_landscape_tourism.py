"""
gen_group9_landscape_tourism.py - Generates Documents 25, 26, 33, 34, 35, 36, and 37.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_25():
    doc = PuriDocBuilder(
        title="The Cultural Landscape of Puri: An Interconnected Heritage Ecosystem",
        doc_number="25",
        category="Cultural Landscapes & Sacred Geography"
    )

    doc.add_h1("1. Puri as a Living Cultural Ecosystem")
    doc.add_paragraph("Puri cannot be understood simply as a collection of isolated monuments; it constitutes a fully unified, living cultural landscape where sacred geography, hydraulic engineering, agrarian supply chains, monastic institutions, and craft settlements operate in continuous mutual dependence:")

    headers = ["Landscape Component", "Spatial / Urban Role", "Systemic Interconnection in Puri Ecosystem"]
    rows = [
        ["Shree Mandira (Temple Vortex)", "The epicenter of Shankha Kshetra; focal point of all radial roads", "Directs ritual demand for daily agricultural produce, flowers, timber, textiles, and ghee."],
        ["Bada Danda (Grand Road)", "3 km ritual highway connecting Jagannath to Gundicha Temple", "The ceremonial stage for Rath Yatra; flanked by historic Mathas, markets, and guest houses."],
        ["Pancha Tirtha Hydrology", "Five sacred water tanks & the ocean (Mahodadhi)", "Recharges groundwater; provides ritual ablution points before temple darshan."],
        ["Matha Monastic Ring", "Dozens of multi-sectarian monastic compounds surrounding temple", "Manage agricultural land endowments; provide pilgrim hospitality and scholastic debate."],
        ["Raghurajpur & Pipili Craft Corridors", "Satellite artisanal craft villages within 15-35 km radius", "Manufacture sacred ritual objects: Pattachitra scrolls, wooden deities, and Rath cloth canopies."]
    ]
    doc.add_table(headers, rows, [1.5, 2.0, 3.0])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S008")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "25_Cultural_Landscape.docx"))

def generate_doc_26():
    doc = PuriDocBuilder(
        title="Natural Heritage: Coastal Ecosystems, Beaches, & Chilika Lagoon",
        doc_number="26",
        category="Natural Heritage & Biodiversity"
    )

    doc.add_h1("1. Coastal & Marine Biodiversity of Puri District")
    doc.add_paragraph("The natural environment of Puri district encompasses high-energy sandy beaches, littoral sand dunes, estuarine mangrove pockets, and the world-famous Chilika lagoon:")

    headers = ["Ecological Zone", "Geographical Scope & Protection", "Key Biodiversity & Conservation Values"]
    rows = [
        ["Puri Golden Beach", "Urban beach zone; Blue Flag certified stretch", "High water cleanliness, eco-tourism infrastructure, sustainable beach management."],
        ["Balukhand-Konark Wildlife Sanctuary", "71.72 km² coastal belt along Marine Drive", "Casuarina coastal shelterbelt; sanctuary for over 4,000 Spotted Deer (Axis axis) and Striped Hyenas."],
        ["Chilika Lake (Ramsar Site #229)", "1,165 km² brackish coastal lagoon (SW boundary)", "Habitat for endangered Irrawaddy Dolphins (Orcaella brevirostris); over 1 million wintering migratory birds."],
        ["Sea Turtle Nesting Context", "Rushikulya & Devi River estuaries (adjacent zones)", "Global mass nesting (Arribada) of Olive Ridley Sea Turtles (Lepidochelys olivacea)."]
    ]
    doc.add_table(headers, rows, [1.5, 1.8, 3.2])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S004"),
        get_source("PUR-S005")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "26_Natural_Heritage.docx"))

def generate_doc_33():
    doc = PuriDocBuilder(
        title="Tourism & Visitor Guide: Itineraries, Connectivity, & Exploration",
        doc_number="33",
        category="Visitor Guide & Tourism Logistics"
    )

    doc.add_h1("1. Comprehensive Travel Logistics & Connectivity")
    headers = ["Transit Mode", "Terminal / Route Details", "Key Practical Advice [TIME-SENSITIVE]"]
    rows = [
        ["By Air", "Biju Patnaik International Airport (BBI), Bhubaneswar (60 km)", "Frequent pre-paid taxis, airport shuttle buses, and national highway NH-316 connectivity (~1.5 hours)."],
        ["By Rail", "Puri Railway Station (PURI)", "Direct superfast & Vande Bharat express connections to Kolkata, New Delhi, Chennai, Mumbai, and Hyderabad."],
        ["By Road", "NH-316 (Bhubaneswar-Puri 4-lane expressway)", "Excellent state road transport (OSRTC) buses and private luxury coaches running every 15 minutes."],
        ["Local Commute", "Auto-rickshaws, cycle-rickshaws, e-rickshaws (Tuk-tuks)", "Negotiate fares or use app-based aggregators; cycle-rickshaws ideal for crowded Grand Road lanes."]
    ]
    doc.add_table(headers, rows, [1.3, 2.3, 2.9])

    doc.add_h1("2. Curated Cultural Itineraries")
    doc.add_bullet("One-Day Essential Pilgrimage: Dawn darshan at Singhadwara & Aruna Stambha (exterior/interior per eligibility), morning walk at Golden Beach, lunch of authentic Mahaprasad at Anand Bazaar, afternoon excursion to Raghurajpur Craft Village (14 km), evening arati at Swargadwar beach.", "1-Day Itinerary: ")
    doc.add_bullet("Two-Day Heritage Deep Dive: Day 1: Jagannath complex, Lokanath & Markandeshwar temples, Govardhan Math, evening cultural performance at beach. Day 2: Morning scenic drive along Marine Drive to Konark Sun Temple (35 km) & Chandrabhaga Beach; afternoon exploration of Pipili Applique market.", "2-Day Itinerary: ")
    doc.add_bullet("Three-Day Cultural & Ecological Odyssey: Days 1 & 2 as above. Day 3: Full-day boat excursion to Chilika Lake (Satapada, 50 km) for Irrawaddy dolphin watching, Alarnath Temple darshan at Brahmagiri on return journey.", "3-Day Itinerary: ")

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S004")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "33_Tourism_and_Visitor_Guide.docx"))

def generate_doc_34():
    doc = PuriDocBuilder(
        title="Cultural Etiquette & Visitor Protocol: Sacred Norms & Sensitivities",
        doc_number="34",
        category="Visitor Etiquette & Codes"
    )

    doc.add_h1("1. Temple Protocols & Sacred Etiquette")
    doc.add_paragraph("Puri's religious heritage requires respectful adherence to established socio-religious traditions:")
    doc.add_bullet("Non-Hindu Entry Regulation: Entry inside the Shree Jagannath Temple is strictly limited to practicing Hindus per statutory and centuries-old customary law. Non-Hindu visitors can view the Lion Gate, Aruna Stambha, and view the temple deula from the roof terrace of the Raghunandan Library.", "• ")
    doc.add_bullet("Dress Code & Footwear: Modest attire is required (shoulders and knees fully covered; traditional Indian dhotis/sarees/kurtas recommended). All leather items (belts, wallets, shoes) and footwear must be deposited at official cloakrooms (Jota Stand) before entering temple precincts.", "• ")
    doc.add_bullet("Electronic Devices & Photography: Mobile phones, cameras, smartwatches, and recording equipment are strictly prohibited inside the Jagannath Temple complex and will be confiscated.", "• ")
    doc.add_bullet("Anand Bazaar Etiquette: When purchasing Mahaprasad, treat the terracotta Kudua with utmost reverence; do not step over food or touch it with left hands. Never waste Mahaprasad.", "• ")

    doc.add_h1("2. Ethical Interaction with Artisans")
    doc.add_paragraph("In heritage villages like Raghurajpur and Pipili:")
    doc.add_bullet("Respect Intellectual Property: Always seek permission before photographing artists at work on their canvases or palm-leaf etchings.", "• ")
    doc.add_bullet("Fair Trade Purchasing: Support traditional masters directly rather than middleman agents; appreciate that authentic stone-pigment Pattachitra takes weeks of intensive hand labor.", "• ")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "34_Cultural_Etiquette.docx"))

def generate_doc_35():
    doc = PuriDocBuilder(
        title="Lesser-Known Puri: Hidden Shrines, Ancient Akhadas, & Secret Heritage",
        doc_number="35",
        category="Hidden Heritage & Explorations"
    )

    doc.add_h1("1. Hidden Shrines & Lesser-Known Architectural Jewels")
    doc.add_paragraph("Beyond the primary tourist trail, Puri conceals extraordinary spiritual, historical, and martial heritage sites:")

    headers = ["Lesser-Known Site", "Location & Character", "Historical Significance & Unique Features"]
    rows = [
        ["The Traditional Akhadas (ଜାଗା ଆଖଡ଼ା)", "Ancient traditional wrestling and martial arts gymnasia in the Sahis (quarters)", "Over 7 historic Sahi Akhadas (Baligotha, Talabichha, etc.) where youth train in Paika martial arts, Mallayuddha wrestling, and serve as temple security guards."],
        ["Gambhira (Sri Radha Kanta Matha)", "Balisahi lane near Grand Road", "The tiny subterranean chamber where Sri Chaitanya Mahaprabhu spent his final 12 years in intense mystical absorption; his wooden slippers (Paduka) and quilt are preserved."],
        ["Tota Gopinath Temple", "Quiet garden grove near Yameshwar Temple", "Sacred temple housing the kneeling Krishna deity carved from black stone by Chaitanya Mahaprabhu; site where Chaitanya is believed to have merged into the deity in 1533."],
        ["Atharanala Bridge (ଅଠରନଳା)", "Entrance to Puri town on Madhuban Road", "13th-century Eastern Ganga laterite stone bridge spanning 85 meters across 18 stone arches; historic gateway for all classical pilgrim caravans."],
        ["Bedi Mahavir (Sun Temple Hanuman)", "Chakratirtha Road on the sea beach", "Unique seaside Hanuman temple; legend holds Lord Hanuman was bound by golden chains by Jagannath to guard the beach and prevent ocean surges from flooding the sacred city."]
    ]
    doc.add_table(headers, rows, [1.5, 1.8, 3.2])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S018")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "35_Lesser_Known_Puri.docx"))

def generate_doc_36():
    doc = PuriDocBuilder(
        title="Modern Cultural Evolution: Then vs. Now & Changing Lifestyles in Puri",
        doc_number="36",
        category="Modern Evolution & Sociology"
    )

    doc.add_h1("1. Contemporary Cultural Transformation (Then vs. Now)")
    doc.add_paragraph("Puri has witnessed profound socio-economic and technological transformations over the past century while fiercely guarding its ritual core:")

    headers = ["Cultural Dimension", "Historical / Traditional Reality (Then)", "Contemporary Modern State (Now)"]
    rows = [
        ["Pilgrimage Transit", "Months-long arduous journey on foot, bullock carts, or coastal boats along Jagannath Sadak.", "High-speed Vande Bharat trains, 4-lane expressway NH-316, international flights via Bhubaneswar."],
        ["Craft Production", "Strictly hand-ground mineral pigments and natural cloth canvases sold exclusively to pilgrims.", "Global e-commerce exports, GI tag protection, national design collaborations, digital artisan stores."],
        ["Beach Culture", "Sacred Mahodadhi ablution and Swargadwar cremation rites; isolated fishing village.", "Blue Flag international eco-tourism certification, promenade parks, surfing festivals, sand art expos."],
        ["Temple Crowd Management", "Informal pilgrim gatherings managed organically by Panda guides.", "AI crowd-density tracking, multi-tier integrated command centers (ICCC), biometric queue systems during Rath Yatra."],
        ["Culinary Delivery", "Mahaprasad consumed exclusively on-site on banana leaves in Anand Bazaar.", "Eco-friendly clay pot courier deliveries across Odisha; standardized hygienic packaging."]
    ]
    doc.add_table(headers, rows, [1.4, 2.5, 2.6])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S004"),
        get_source("PUR-S008")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "36_Modern_Cultural_Evolution.docx"))

def generate_doc_37():
    doc = PuriDocBuilder(
        title="Heritage Preservation & Conservation: Challenges, Initiatives, & Field Work",
        doc_number="37",
        category="Conservation & Preservation"
    )

    doc.add_h1("1. Monument Conservation & Environmental Challenges")
    doc.add_paragraph("Puri's coastal location presents severe conservation challenges for historic stone architecture. Salt-laden marine air, high relative humidity (exceeding 85%), tropical cyclone impacts, and massive pilgrim footfall require continuous scientific interventions:")

    headers = ["Preservation Domain", "Primary Risk / Threat", "Institutional Intervention & Modern Program"]
    rows = [
        ["Structural Stone Corrosion", "Marine salt air causing exfoliation and pitting of Khondalite stone on the 65m deula", "ASI chemical preservation cell applies specialized silicone water repellents and lime mortar repointing."],
        ["Cyclone Damage Resilience", "High-velocity wind damage and saline ingress during major cyclonic storms (e.g. Cyclone Fani 2019)", "State Disaster Management Authority (OSDMA) and ASI structural reinforcement of roofs and boundary walls."],
        ["Urban Heritage Redevelopment", "Encroachments and congestion surrounding the Meghanada Pacheri", "Augmentation of Basic Amenities & Development of Heritage and Architecture (ABADHA) scheme; 75m sacred buffer corridor."],
        ["Intangible Craft Survival", "Economic vulnerability of younger generation artisans shifting to service jobs", "ODISHA Crafts, ORMAS skill centers, national craft stipends, and GI tag enforcement."]
    ]
    doc.add_table(headers, rows, [1.5, 2.3, 2.7])

    doc.add_h1("2. Future Field Research Recommendations")
    doc.add_paragraph("To further deepen academic and digital archives, upcoming multidisciplinary field research teams should prioritize:")
    doc.add_bullet("Oral History Recording: Conducting high-definition audio-visual interviews with senior Daitapati and Suara servitors to document unwritten oral nitis.", "1. ")
    doc.add_bullet("Palm-Leaf Manuscript Digitization: Establishing high-resolution multispectral scanning of private Matha archives (Emar, Raghunandan, Govardhan) before biological decay.", "2. ")
    doc.add_bullet("Living Craft Ethnography: Documenting generational transmission of natural pigment chemistry among women artisans in Raghurajpur and Dandashahi.", "3. ")

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "37_Preservation_and_Conservation.docx"))

if __name__ == "__main__":
    generate_doc_25()
    generate_doc_26()
    generate_doc_33()
    generate_doc_34()
    generate_doc_35()
    generate_doc_36()
    generate_doc_37()
    print("Group 9 completed successfully.")
