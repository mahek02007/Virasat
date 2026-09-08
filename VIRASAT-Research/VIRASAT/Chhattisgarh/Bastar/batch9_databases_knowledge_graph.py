import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_91():
    doc = create_base_document("91. Bastar Heritage Site Database", "Relational Database Schema & Master Inventory of Archaeological & Cultural Monuments")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-091",
        "Geographic Scope": "Bastar Division Monumental Locations",
        "Primary Classification": "Relational Database Schema & Structured Heritage Inventory",
        "Confidence Level": "HIGH (Archaeological Survey of India & State Protected Monuments Registry)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Database Schema Specification: Heritage Sites")
    doc.add_paragraph("Schema: entity_id | entity_type | name | local_name | district | coordinates | period | significance | protection_status | confidence")
    
    headers = ["Site ID", "Site Name", "District", "Chronology", "Typology", "Protection Status", "Confidence"]
    rows = [
        ["BST-SIT-001", "Barsur Battisa Temple", "Dantewada", "1208 CE (Chhindaka Naga)", "Twin Shiva Sanctum (32 Pillars)", "State Protected (ASI Raipur)", "HIGH"],
        ["BST-SIT-002", "Barsur Mama-Bhanja Temple", "Dantewada", "12th - 13th c. CE", "Curvilinear Nagara Shikhara", "State Protected (ASI Raipur)", "HIGH"],
        ["BST-SIT-003", "Barsur Twin Ganesha Monoliths", "Dantewada", "11th c. CE", "Monolithic Granite Sculptures", "State Protected", "HIGH"],
        ["BST-SIT-004", "Narayanpal Vishnu Temple", "Bastar", "1111 CE (Gundamahadevi)", "Sandstone Vishnu Temple", "State Protected", "HIGH"],
        ["BST-SIT-005", "Danteshwari Temple Complex", "Dantewada", "1324 CE (Annamadeva)", "Royal Shakta Shakti Peetha", "Temple Trust / State Protected", "HIGH"],
        ["BST-SIT-006", "Bastar Palace & Durbar Hall", "Bastar (Jagdalpur)", "1777 / 1910 CE", "Royal Palace & Colonial Arches", "Heritage Monument", "HIGH"],
        ["BST-SIT-007", "Dholkal Ganesha Monolith", "Dantewada (Bailadila)", "10th - 11th c. CE", "Cliff-top Granite Monolith (3,000 ft)", "District Heritage Site", "HIGH"],
        ["BST-SIT-008", "Bhairamgarh Fort & Temples", "Bijapur", "12th - 13th c. CE", "Medieval Fortification & Inscriptions", "State Protected", "HIGH"],
        ["BST-SIT-009", "Garhbodh (Pushkari Capital)", "Bastar-Kalahandi", "4th - 6th c. CE (Nalas)", "Ancient Urban Remains & Brick Stupas", "Archaeological Site", "HIGH"],
        ["BST-SIT-010", "Kuruspal Inscription Site", "Bastar", "11th c. CE (Someshvara I)", "Hero Stone & Epigraphic Pillar", "Archaeological Site", "HIGH"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "91_Bastar_Heritage_Site_Database.docx")

def build_doc_92():
    doc = create_base_document("92. Bastar Community Database", "Structured Ethnographic Registry: Demographics, Clans, Languages, and Cultural Traits")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-092",
        "Geographic Scope": "All 7 Districts of Bastar Division",
        "Primary Classification": "Ethnographic Database Schema & Community Census Records",
        "Confidence Level": "HIGH (Census of India, Anthropological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Community ID", "Community Name", "Language / Family", "Primary Habitation", "Social Institution", "Craft / Livelihood", "Confidence"]
    rows = [
        ["BST-COM-001", "Gond (Koitur)", "Gondi (Central Dravidian)", "Division-wide", "4-Saga Phratry System", "Settled Agriculture & Forest Gathering", "HIGH"],
        ["BST-COM-002", "Hill Maria (Abujhmaria)", "Gondi (Dravidian)", "Abujhmad (Narayanpur)", "Penda (Swidden) & Male Dormitory", "Forestry & Shifting Cultivation (PVTG)", "HIGH"],
        ["BST-COM-003", "Dandami Maria (Bison Horn)", "Gondi (Dravidian)", "Dantewada, Bijapur, Sukma", "Uruskal Megaliths & Gaur Dance", "Agriculture & Terracotta Arts", "HIGH"],
        ["BST-COM-004", "Muria", "Gondi / Halbi", "Kondagaon, Central Bastar", "Ghotul Youth Dormitory", "Agriculture, Woodcraft, Mandari", "HIGH"],
        ["BST-COM-005", "Halba", "Halbi (Indo-Aryan)", "Bastar, Kondagaon, Kanker", "Purait/Surait Castes, Rahas", "Agriculture & Trade (Lingua Franca)", "HIGH"],
        ["BST-COM-006", "Dhurwa", "Parji (Central Dravidian)", "Kanger Valley (Bastar)", "Village Councils (Gaontia/Perma)", "Master Bamboo & Cane Weaving", "HIGH"],
        ["BST-COM-007", "Dorla", "Dorli / Koya (Dravidian)", "Sukma, Bijapur (Godavari)", "Riverine Clan Lineages", "Riparian Agriculture & Fishery", "HIGH"],
        ["BST-COM-008", "Bhatra", "Bhatri (Indo-Aryan)", "Eastern Bastar (Jagdalpur)", "Bhatra Tribal Councils", "Agriculture & Royal Temple Attendants", "HIGH"],
        ["BST-COM-009", "Ghadwa", "Halbi / Bhatri", "Kondagaon, Tokapal", "Hereditary Metallurgy Guild", "Bastar Dhokra Lost-Wax Metal Casting", "HIGH"],
        ["BST-COM-010", "Lohar / Agariya", "Halbi / Gondi", "Bastar, Dantewada", "Blacksmith Guild", "Bastar Wrought Iron Craft (Lohe Ka Kaam)", "HIGH"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "92_Bastar_Community_Database.docx")

def build_doc_93():
    doc = create_base_document("93. Bastar Festival Database", "Structured Calendar of Rituals: Seasonal Tithis, Communities & Ceremonial Protocols")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-093",
        "Geographic Scope": "Bastar Division Cultural Sphere",
        "Primary Classification": "Festivals Database & Ritual Ontology",
        "Confidence Level": "HIGH (District Administration & Temple Trust Schedules)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Festival ID", "Festival Name", "Timing / Month", "Presiding Deities", "Key Ritual Artifact / Performance", "Geographic Scope"]
    rows = [
        ["BST-FST-001", "Bastar Dussehra", "Shravana to Ashvina (75 Days)", "Goddess Danteshwari & Mawli Mata", "Multi-wheeled Chariot (Rath), Jogi Bithai, Thorn Bed", "Jagdalpur / Pan-Bastar"],
        ["BST-FST-002", "Goncha Festival", "Ashadha (June - July)", "Lord Jagannath, Subhadra, Balabhadra", "Tupki (Bamboo mock pistol) with Peng fruit bullets", "Jagdalpur City"],
        ["BST-FST-003", "Narayanpur Madai", "Phalguna (February - March)", "Mawli Mata & Regional Anga Devs", "Lath (Bamboo palanquins) parade, Cockfighting rings", "Narayanpur / Abujhmad"],
        ["BST-FST-004", "Dantewada Phagun Madai", "Phalguna (March)", "Goddess Danteshwari", "9-day sacred fair, royal deity processions, holi bonfires", "Dantewada Complex"],
        ["BST-FST-005", "Kaksar Festival", "Post-Harvest (May - June)", "Kaksar Pen (Deity of Health/Crops)", "Kaksar Dance with brass-belled skirts & iron rods", "Abujhmad / Narayanpur"],
        ["BST-FST-006", "Mati Puja (Earth Festival)", "Chaitra (March - April)", "Mati Devta (Mother Earth)", "Consecration of agrarian seeds prior to sowing", "All Tribal Villages"],
        ["BST-FST-007", "Hareli & Gedi Festival", "Shravana Amavasya (July - Aug)", "Kutki Dai & Agricultural Implements", "Gedi bamboo stilt dances & iron plow consecration", "Division-wide"],
        ["BST-FST-008", "Aamakhani", "Chaitra (Spring)", "Village Clan Deities", "First ritual tasting of seasonal green mangoes", "All Tribal Communities"],
        ["BST-FST-009", "Nawakhani", "Bhadrapada (Sept - Oct)", "Ancestral Spirits (Hanal)", "Ritual preparation of first new rice grains with milk", "Division-wide"],
        ["BST-FST-010", "Diyari Festival", "Kartika (Post-Diwali)", "Dhorai / Cattle Protector Deities", "Cattle decoration with peacock feathers & forest grass", "Division-wide"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "93_Bastar_Festival_Database.docx")

def build_doc_94():
    doc = create_base_document("94. Bastar Food Database", "Nutritional, Ethnobotanical & Culinary Registry of Agrarian and Wild Foods")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-094",
        "Geographic Scope": "Bastar Division Gastronomy",
        "Primary Classification": "Nutritional Database, Ethnobotanical Foods & GI Registry",
        "Confidence Level": "HIGH (ICAR, FSSAI, Fieldwork Nutrition Surveys)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Food ID", "Food / Beverage Name", "Primary Ingredients", "Preparation Technique", "Nutritional / Cultural Profile", "GI / Regional Status"]
    rows = [
        ["BST-FOD-001", "Chaprah (Red Ant Chutney)", "Oecophylla smaragdina ants & pupae, ginger, chilli", "Crushed raw in stone mortar", "High protein, zinc, calcium, formic acid; immunity tonic", "GI Certified"],
        ["BST-FOD-002", "Pej (Paje Gruel)", "Broken rice, Kodo millet, water, salt", "Slow-boiled into liquid porridge", "Daily hydrator, easy carbohydrate digestion, mineral rich", "Traditional Core Staple"],
        ["BST-FOD-003", "Chhilka Roti", "Rice flour, urad dal batter", "Steamed on earthen pans with Sal leaves", "Soft, oil-free digestible breakfast bread", "Traditional Bread"],
        ["BST-FOD-004", "Bobda / Bafauri", "Bengal gram / Chana paste, wild greens", "Steamed savory dumplings in spiced gravy", "High plant-based protein without deep frying", "Festive Dish"],
        ["BST-FOD-005", "Amat Soup", "Mixed forest tubers, bamboo shoots, ginger paste", "Slow-simmered vegetable broth", "Probiotic and digestive appetizing herbal soup", "Traditional Specialty"],
        ["BST-FOD-006", "Sulphi Sap", "Fresh sap of Caryota urens palm", "Naturally fermented on tree tap", "Sweet, mildly alcoholic, rich in B-vitamins & yeast", "Forest Beverage"],
        ["BST-FOD-007", "Mahua Spirit", "Distilled Madhuca longifolia flower wash", "Double-distilled earthen pot condensers", "Aromatic ancestral spirit used in libations and winter warmth", "Sacred Beverage"],
        ["BST-FOD-008", "Landa (Rice Beer)", "Fermented boiled rice with Ranu herbal yeast", "Multi-day anaerobic fermentation", "Thick probiotic beer consumed during collective harvest", "Community Beverage"],
        ["BST-FOD-009", "Sarai Phatu (Sal Mushrooms)", "Wild Termitomyces mushrooms from Sal forest floor", "Sauteed with mustard oil and dry spices", "Exceptional umami flavor, highly prized forest delicacy", "Seasonal NTFP"],
        ["BST-FOD-010", "Karil (Bamboo Shoot Curry)", "Tender seasonal bamboo shoots", "Sliced, water-leached, and braised", "High dietary fiber, low calorie, anti-inflammatory", "Seasonal Forest Food"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "94_Bastar_Food_Database.docx")

def build_doc_95():
    doc = create_base_document("95. Bastar Art and Craft Database", "Materiality, Artisans, GI Certifications, and Design Taxonomy")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-095",
        "Geographic Scope": "Bastar Division Craft Clusters",
        "Primary Classification": "Material Culture Database & IPR Registry",
        "Confidence Level": "HIGH (Geographical Indications Registry GOI, Crafts Council)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Craft ID", "Craft Name", "Artisan Community", "Raw Materials", "Iconic Motifs", "GI Tag Application", "Confidence"]
    rows = [
        ["BST-CRF-001", "Bastar Dhokra (Lost-Wax)", "Ghadwa (Ghasiya)", "Brass, beeswax, clay core, resin", "Tribal dancers, elephants, deities, oil lamps", "GI Tag No. 83", "HIGH"],
        ["BST-CRF-002", "Bastar Iron Craft (Wrought Iron)", "Lohar / Agariya", "Scrap wrought iron, charcoal heat", "Lohe Shikhar tridents, musicians, deer, diyas", "GI Tag No. 82", "HIGH"],
        ["BST-CRF-003", "Bastar Wooden Craft", "Badhai, Muria, Gond", "Teak, Sal, Shisham, Kura wood", "Ghotul pillars, masks, tribal narrative panels", "GI Tag No. 84", "HIGH"],
        ["BST-CRF-004", "Bastar Terracotta", "Kumhar", "Riverine clay, sand, organic slips", "Multi-tiered votive elephants, horses, roof tiles", "State Protected Craft", "HIGH"],
        ["BST-CRF-005", "Bastar Bamboo Craft", "Dhurwa, Gond", "Dendrocalamus strictus culms", "Doli grain bins, fish traps, rain hats (Khumri)", "State Forest Craft", "HIGH"],
        ["BST-CRF-006", "Kotpad Vegetable Dye Textile", "Mirgan / Mahra", "Organic cotton, Aal tree root dye", "Axes, fish, temple towers, crab motifs", "GI Certified Handloom", "HIGH"],
        ["BST-CRF-007", "Kosa Wild Silk Sericulture", "Panka, Kostha", "Antheraea mylitta wild silkworm cocoons", "Lustrous gold tussar silk sarees and stoles", "GI Tagged Chhattisgarh Kosa", "HIGH"],
        ["BST-CRF-008", "Godna (Body Tattoo Art)", "Godharin artists", "Kajal pigment, needle pricks, milk sap", "Geometric lines, peacocks, floral circles, deities", "Living Dermatoglyphic Art", "HIGH"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "95_Bastar_Art_and_Craft_Database.docx")

def build_doc_96():
    doc = create_base_document("96. Bastar Music and Dance Database", "Organology, Choreography, Performance Contexts & Acoustic Classifications")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-096",
        "Geographic Scope": "Bastar Division Performing Circuits",
        "Primary Classification": "Ethnomusicology & Ethnochoreology Database",
        "Confidence Level": "HIGH (Sangeet Natak Akademi & Indira Kala Sangit Vishwavidyalaya)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Perf ID", "Tradition Name", "Type", "Practicing Community", "Instruments Used", "Choreography / Meaning"]
    rows = [
        ["BST-PRF-001", "Gaur Dance (Bison Horn)", "Dance / Ritual", "Dandami Maria", "Large Maria Dhol, Tirududi iron ringing sticks", "Towering bison horn headdresses, powerful stomping rhythms celebrating virility and hunt"],
        ["BST-PRF-002", "Gedi Dance", "Dance / Acrobatic", "Muria Youth", "Bamboo stilts (Gedi), Mandar drums", "Extraordinary balance on tall stilts during monsoon Hareli festival; agrarian joy"],
        ["BST-PRF-003", "Mandari Dance", "Dance / Percussion", "Muria (Ghotul)", "Mandar terracotta/wood drums", "Circular counter-rhythmic drumming and intricate foot movements led by Chelik youth"],
        ["BST-PRF-004", "Kaksar Dance", "Dance / Devotional", "Hill Maria (Abujhmaria)", "Brass bell belts, wooden clappers", "Youth courtship and deity invocation for agricultural fertility and health"],
        ["BST-PRF-005", "Hulki Manda", "Dance / Folk", "Muria & Bhatra", "Mohri reed shawm, Dhol, Mandar", "Interlocking-arm undulating serpentine line dance performed at marriages and fairs"],
        ["BST-PRF-006", "Pradhan Epic Recital", "Music / Oral Epic", "Pradhan Bards", "Bana / Kingri bowed three-string lute", "Multi-day genealogical chant of Gond ancestors, Lingo Pen, and clan migrations"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "96_Bastar_Music_and_Dance_Database.docx")

def build_doc_97():
    doc = create_base_document("97. Bastar Folklore Database", "Oral Corpus Taxonomy: Myth vs Legend vs History vs Epigraphic Reality")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-097",
        "Geographic Scope": "Bastar Oral Epics & Myth Cycles",
        "Primary Classification": "Comparative Folklore Database & Epistemic Taxonomy",
        "Confidence Level": "HIGH (Verrier Elwin Folklore Archives & TRI Oral History)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Folklore ID", "Narrative Title", "Epistemic Category", "Key Characters / Entities", "Core Plot Summary & Cultural Function", "Confidence"]
    rows = [
        ["BST-FLK-001", "Pahandi Lingo & Creation of Koyatur", "MYTH / COSMOLOGY", "Pahandi Kupar Lingo, 4 Sagas, Kachargadh Cave", "Emergence of ancestral Gonds from sacred mountain; establishment of music, ethics, Ghotul", "HIGH"],
        ["BST-FLK-002", "Danteshwari's Migration with Annamadeva", "RELIGIOUS LEGEND", "Goddess Danteshwari, King Annamadeva, River Confluence", "Goddess follows King from Warangal with anklet bells; stops at Dankini-Shankini to become eternal protector", "HIGH"],
        ["BST-FLK-003", "Legend of the 147 Temples of Barsur", "LOCAL FOLKLORE / MEMORY", "Chhindaka Naga Kings, Twin Ganesha, Master Masons", "King commissions 147 ponds and temples so he could visit a new sacred site every day of the year", "MEDIUM"],
        ["BST-FLK-004", "The Secret Signals of Bhumkal (1910)", "HISTORICAL FACT / ORAL MEMORY", "Gundadhur, Lal Kalendra Singh, British Forces", "Distribution of mango branches, red chillies, and earth knots across 84 parganas to ignite total rebellion", "HIGH"],
        ["BST-FLK-005", "The Blind Fish of Kutumsar", "GEOLOGICAL FOLKLORE", "Subterranean spirits, Shankar Tiwari", "Legend of cave spirits removing the eyes of fish who entered the eternal dark sanctuary of Lord Shiva", "HIGH"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "97_Bastar_Folklore_Database.docx")

def build_doc_98():
    doc = create_base_document("98. Bastar Natural Heritage Database", "Geomorphology, Hydrography, Speleology & Biodiversity Sanctuaries")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-098",
        "Geographic Scope": "Bastar Division Natural Ecosystems",
        "Primary Classification": "Protected Areas, Hydrography & Speleological Database",
        "Confidence Level": "HIGH (Forest Survey of India, GSI, WII)",
        "Last Verified Date": "2026-09-07"
    })
    
    headers = ["Natural ID", "Site / Feature Name", "Geographic Category", "District", "Ecological Coordinates / Area", "Key Biodiversity / Geological Feature", "Confidence"]
    rows = [
        ["BST-NAT-001", "Chitrakote Falls", "Fluvial / Waterfall", "Bastar", "19°12'N, 81°42'E (Indravati)", "Horseshoe plunge (29m drop, ~300m monsoon width); India's widest waterfall", "HIGH"],
        ["BST-NAT-002", "Tirathgarh Falls", "Fluvial / Geological Cascade", "Bastar", "18°54'N, 81°51'E (Kanger)", "Stepped cascade (91m drop) cutting Proterozoic Cuddapah sandstones", "HIGH"],
        ["BST-NAT-003", "Kutumsar Karst Cave", "Speleological / Karst", "Bastar (Kanger NP)", "35m depth, 330m length", "Stalactites, stalagmites, endemic blind cave fish (Nemacheilus exiguus)", "HIGH"],
        ["BST-NAT-004", "Kailash Cave", "Speleological", "Bastar (Kanger NP)", "1 km cave passage", "Gigantic limestone dripstone pillar resembling natural Shiva Lingam", "HIGH"],
        ["BST-NAT-005", "Kanger Valley National Park", "Protected Biosphere", "Bastar", "200.00 sq km", "Dense moist deciduous Sal forest; prime habitat for Bastar Hill Myna", "HIGH"],
        ["BST-NAT-006", "Indravati National Park & TR", "Protected Tiger Reserve", "Bijapur", "1,258.37 sq km", "Vast grasslands; critical sanctuary for endangered Wild Water Buffalo", "HIGH"],
        ["BST-NAT-007", "Dalpat Sagar Lake", "Wetland / Artificial Lake", "Bastar (Jagdalpur)", "350 hectares", "18th-century royal rainwater reservoir; vital urban wetland habitat", "HIGH"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "98_Bastar_Natural_Heritage_Database.docx")

def build_doc_99():
    doc = create_base_document("99. Bastar Knowledge Graph", "Ontological Architecture, RDF Triples, Entity Graph & Cypher Database Queries")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-099",
        "Geographic Scope": "Digital Humanities & Semantic Web Architecture",
        "Primary Classification": "Knowledge Graph Ontology, Linked Open Data (LOD) & Graph Queries",
        "Confidence Level": "HIGH (W3C RDF/OWL Standards & Neo4j Graph Database Schema)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Knowledge Graph Ontological Entity Classes")
    doc.add_paragraph(
        "The Bastar Knowledge Graph is structured across 18 core entity classes:\n"
        ":Place | :District | :Village | :Community | :Person | :Festival | :Deity | :Temple | :ArchaeologicalSite | "
        ":NaturalSite | :Waterfall | :Cave | :Craft | :Instrument | :Dance | :Food | :Language | :HistoricalEvent"
    )
    
    add_heading_2(doc, "2. Master RDF Triples (Subject - Predicate - Object)")
    headers = ["Subject Entity (URI / Class)", "Predicate / Relationship", "Object Entity (URI / Class)"]
    rows = [
        ["bastar:DanteshwariTemple", "located_in", "bastar:DantewadaDistrict"],
        ["bastar:DanteshwariTemple", "consecrated_by", "bastar:Annamadeva"],
        ["bastar:DanteshwariTemple", "dedicated_to", "bastar:GoddessDanteshwari"],
        ["bastar:BastarDussehra", "celebrated_in_honor_of", "bastar:GoddessDanteshwari"],
        ["bastar:BastarDussehra", "has_duration_days", "75"],
        ["bastar:BastarDhokra", "has_gi_tag_number", "GI_83"],
        ["bastar:BastarDhokra", "practiced_by", "bastar:GhadwaCommunity"],
        ["bastar:BarsurBattisaTemple", "built_during", "bastar:ChhindakaNagaDynasty"],
        ["bastar:GaurDance", "performed_by", "bastar:DandamiMariaCommunity"],
        ["bastar:KutumsarCave", "located_within", "bastar:KangerValleyNationalPark"],
        ["bastar:BastarHillMyna", "has_conservation_status", "StateBirdOfChhattisgarh"],
        ["bastar:ChaprahChutney", "prepared_from", "bastar:OecophyllaSmaragdinaAnts"],
        ["bastar:BhumkalRebellion_1910", "led_by", "bastar:GundadhurOfNethanar"],
        ["bastar:GhotulInstitution", "patron_deity", "bastar:LingoPen"],
        ["bastar:HalbiLanguage", "belongs_to_family", "bastar:EasternIndoAryan"]
    ]
    add_styled_table(doc, headers, rows)
    
    add_heading_2(doc, "3. Cypher Graph Query Example for Interactive Retrieval")
    doc.add_paragraph(
        "MATCH (c:Community {name: 'Muria'})-[:PRACTICES]->(cr:Craft)\n"
        "MATCH (c)-[:RESIDES_IN]->(d:District)\n"
        "MATCH (f:Festival)-[:CELEBRATED_BY]->(c)\n"
        "RETURN c.name, cr.name, d.name, f.name;"
    )
    
    save_document(doc, "99_Bastar_Knowledge_Graph.docx")

if __name__ == "__main__":
    print("Building Batch 9: Documents 91 to 99...")
    build_doc_91()
    build_doc_92()
    build_doc_93()
    build_doc_94()
    build_doc_95()
    build_doc_96()
    build_doc_97()
    build_doc_98()
    build_doc_99()
    print("Batch 9 completed successfully.")
