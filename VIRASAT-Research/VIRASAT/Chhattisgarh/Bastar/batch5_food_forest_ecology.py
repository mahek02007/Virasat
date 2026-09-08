import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_36():
    doc = create_base_document("36. Food and Culinary Heritage", "Agrarian Staples, Minor Millets, Pej Gruel, and Fermented Delicacies")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-036",
        "Geographic Scope": "Bastar Division Domestic Kitchens & Haats",
        "Primary Classification": "Gastronomy, Agrarian Nutrition & Culinary Heritage",
        "Confidence Level": "HIGH (ICAR Nutrition Surveys, Anthropological Studies)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Agrarian Staples and Everyday Diet")
    doc.add_paragraph(
        "Bastar cuisine is grounded in wholesome, unrefined grains and forest foraging. The fundamental daily staple across all tribal communities "
        "is 'Pej' (or 'Paje'), a nutritious rice or millet gruel made by boiling broken rice, Kodo millet (Paspalum scrobiculatum), or Kutki "
        "(Little millet) with excess water, consumed lukewarm with roasted green chillies, wild herbs, or dried fish. Other domestic culinary items include:\n"
        "• Chhilka Roti: Delicate, crepe-like steamed pancakes prepared from ground rice and black gram batter.\n"
        "• Bobda / Bafauri: Steamed lentil dumplings prepared with wild leafy greens.\n"
        "• Amat: A sour and savory traditional soup prepared with mixed forest vegetables, bamboo shoots, and ginger paste."
    )
    
    save_document(doc, "36_Food_and_Culinary_Heritage.docx")

def build_doc_37():
    doc = create_base_document("37. Forest Foods and Traditional Cuisine", "Chaprah Red Ant Chutney, Wild Mushrooms, Bamboo Shoots & Beverages")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-037",
        "Geographic Scope": "Bastar Forest Ecosystems & Weekly Haats",
        "Primary Classification": "Ethno-Gastronomy, Entomophagy & Non-Timber Forest Foods",
        "Confidence Level": "HIGH (ICAR, Food Safety and Standards Authority of India, GI Registry)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. World-Famous Forest Foods and Entomophagy")
    doc.add_paragraph(
        "Forest gathering supplies high-protein and micronutrient-rich delicacies unique to Bastar:\n"
        "• Chaprah (Red Weaver Ant Chutney): Prepared by crushing adult red weaver ants (Oecophylla smaragdina) and their protein-rich white pupae "
        "with salt, ginger, garlic, and red chillies. The formic acid gives the chutney a sharp citrus zing. Conferred Geographical Indication (GI) status.\n"
        "• Karil & Bastar Baans (Bamboo Shoots): Tender young bamboo shoots fermented into Karil or dried as Bastar Baans for savory curries.\n"
        "• Poda / Phatu (Wild Mushrooms): Over 20 documented edible wild mushroom varieties (e.g., Jam Phatu, Sarai Phatu) gathered from Sal leaf litter.\n"
        "• Traditional Fermented Beverages:\n"
        "  - Sulphi: Naturally fermented sweet sap tapped from the Sulphi palm (Caryota urens).\n"
        "  - Mahua: Aromatic spirit distilled from fermented flowers of Madhuca longifolia.\n"
        "  - Landa: Thick, probiotic fermented rice and millet beer consumed during communal work and celebrations."
    )
    
    save_document(doc, "37_Forest_Foods_and_Traditional_Cuisine.docx")

def build_doc_38():
    doc = create_base_document("38. Traditional Occupations and Livelihoods", "Agrarian Economy, Non-Timber Forest Produce Collection, and Craft Guilds")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-038",
        "Geographic Scope": "Bastar Division Rural & Forest Tracts",
        "Primary Classification": "Rural Economics & Occupational Sociology",
        "Confidence Level": "HIGH (Census of India, TRI Raipur, District Economic Profiles)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Occupational Pluriactivity")
    doc.add_paragraph(
        "Bastar rural households practice seasonal occupational diversification (pluriactivity). Rather than relying on a single livelihood, "
        "families synchronize settled rain-fed agriculture (kharif season), dry season forest produce gathering (Mahua, Tendu, Harra, Baheda, Lac), "
        "artisanal craft manufacturing, and livestock rearing."
    )
    
    save_document(doc, "38_Traditional_Occupations_and_Livelihoods.docx")

def build_doc_39():
    doc = create_base_document("39. Agriculture and Farming Traditions", "Paddy Varieties, Minor Millets, Swidden Penda Dynamics & Seed Sovereignty")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-039",
        "Geographic Scope": "Bastar Plateau Agrarian Basins",
        "Primary Classification": "Agronomy, Ethno-Agriculture & Crop Diversity",
        "Confidence Level": "HIGH (Indira Gandhi Krishi Vishwavidyalaya Raipur, ICAR)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Agrarian Landscapes and Indigenous Seed Sovereignty")
    doc.add_paragraph(
        "Agricultural topography in Bastar is classified into four distinct elevation land types:\n"
        "1. Marhan: Upland stony slopes used for minor millets (Kodo, Kutki, Kosra).\n"
        "2. Tikra: Elevated light soils used for pulses, oilseeds (Niger/Ramtil), and maize.\n"
        "3. Mal: Mid-slope terraced fields with medium moisture for rainfed paddy.\n"
        "4. Gabhar / Bahal: Lowland deep fertile valleys retaining moisture for long-duration traditional aromatic rice varieties (e.g., Dubraj, Jawaphool, Badshahbhog)."
    )
    
    save_document(doc, "39_Agriculture_and_Farming_Traditions.docx")

def build_doc_40():
    doc = create_base_document("40. Forest Dependency and Forest Culture", "The Sal-Mahua-Tendu Matrix: Sacred Groves and NTFP Economics")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-040",
        "Geographic Scope": "Bastar Division Forest Divisions",
        "Primary Classification": "Forest Ecology, Silviculture & Ethno-Forestry",
        "Confidence Level": "HIGH (Chhattisgarh Forest Department, Forest Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Trinity of Bastar Forest Trees")
    doc.add_paragraph(
        "Three arboreal species form the cultural and economic spine of Bastar civilization:\n"
        "• Sal (Shorea robusta): Revered as the sacred 'Sarai' tree, home to deities; provides timber, resin (Damar/Ral for incense and lost-wax casting), and leaf plates (Pattal).\n"
        "• Mahua (Madhuca longifolia): The 'Tree of Life'; fleshy corollas eaten raw, dried, or distilled; seeds pressed for cooking oil (Tora Tel).\n"
        "• Tendu (Diospyros melanoxylon): Leaves harvested during peak summer as a premier source of seasonal cash income through government-regulated cooperatives."
    )
    
    save_document(doc, "40_Forest_Dependency_and_Forest_Culture.docx")

def build_doc_41():
    doc = create_base_document("41. Traditional Medicine and Healing", "Ethnobotanical Pharmacology, Traditional Healers (Vaidyas), and Clinical Boundaries")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-041",
        "Geographic Scope": "Bastar Forest Ecosystems & Healer Networks",
        "Primary Classification": "Ethno-Medicine, Medical Anthropology & Pharmacognosy",
        "Confidence Level": "HIGH (Traditional Healers Association, National Medicinal Plants Board)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Ethnomedicinal Practices and Key Botanicals")
    doc.add_paragraph(
        "Traditional medicine in Bastar is administered by traditional herbalists (Vaidyas) and spiritual healers (Sirahas). "
        "Over 400 medicinal herbs have been scientifically validated for bioactive compounds:"
    )
    
    add_heading_2(doc, "Key Ethnomedicinal Plant Registry")
    headers = ["Botanical Name", "Local Name", "Plant Part Used", "Traditional Therapeutic Application"]
    rows = [
        ["Tinospora cordifolia", "Giloy / Guruch", "Stem", "Chronic fevers, immunity enhancement, malaria management"],
        ["Andrographis paniculata", "Bhuineem / Kalmegh", "Whole plant", "Hepatoprotective agent, liver disorders, antipyretic"],
        ["Chlorophytum borivilianum", "Safed Musli", "Tuberous roots", "Nutritive tonic, restorative adaptogen, vitality booster"],
        ["Rauvolfia serpentina", "Sarpagandha", "Root", "Hypertension, snakebite antidote, sedative calming"],
        ["Holarrhena antidysenterica", "Kuda / Indrajau", "Bark and seeds", "Amoebic dysentery, gastrointestinal infections"]
    ]
    add_styled_table(doc, headers, rows)
    
    add_callout(doc,
        "EVIDENTIARY DISCLAIMER: Ethnomedicinal descriptions are recorded here strictly as anthropological and ethnobotanical documentation. "
        "They should not be substituted for certified modern clinical advice without medical oversight.",
        "MEDICAL SAFETY & COMPLIANCE"
    )
    
    save_document(doc, "41_Traditional_Medicine_and_Healing.docx")

def build_doc_42():
    doc = create_base_document("42. Traditional Ecological Knowledge", "Customary Conservation, Sacred Sanctuaries, and Water Harvesting")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-042",
        "Geographic Scope": "Bastar Division Sacred Landscapes",
        "Primary Classification": "Traditional Ecological Knowledge (TEK) & Environmental Ethics",
        "Confidence Level": "HIGH (UNESCO MAB Programme, Environmental Anthropological Research)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Customary Ecological Restraints and Taboos")
    doc.add_paragraph(
        "Bastar communities have maintained sustainable ecosystems for centuries through cultural taboos and seasonal bans:\n"
        "• Closed Hunting Seasons: Traditional hunting (Parad) is strictly restricted to ritual festival windows (e.g., Chaitrai Parad), "
        "ensuring breeding seasons of wild animals remain undisturbed.\n"
        "• Sacred Tree Inviolability: Prohibitions against cutting Mahua, Saja, or Banyan trees.\n"
        "• Sacred Grove Protection: Complete ban on timber felling, hunting, or grazing in community sacred groves (Devkot)."
    )
    
    save_document(doc, "42_Traditional_Ecological_Knowledge.docx")

def build_doc_43():
    doc = create_base_document("43. Bastar Forests and Biodiversity", "Tropical Deciduous Biomes, Phytosociology, Endemic Flora, and Carbon Sinks")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-043",
        "Geographic Scope": "Bastar Division Forest Circles (Jagdalpur, Kanker, Dantewada)",
        "Primary Classification": "Plant Ecology, Phytosociology & Forest Conservation",
        "Confidence Level": "HIGH (Forest Survey of India State of Forest Report, ICFRE)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Forest Cover and Canopy Classifications")
    doc.add_paragraph(
        "Bastar Division holds over 55% of its geographic area under forest cover, encompassing Champion and Seth's Tropical Moist Deciduous "
        "(3B/C1c) and Tropical Dry Deciduous (5A/C1b) forest types. Sal (Shorea robusta) accounts for the dominant biomass on the upper plateau, "
        "while Mixed Deciduous forests (Teak, Terminalia, Pterocarpus marsupium, Anogeissus latifolia) thrive in the southern river basins."
    )
    
    save_document(doc, "43_Bastar_Forests_and_Biodiversity.docx")

def build_doc_44():
    doc = create_base_document("44. Wildlife and Natural Heritage", "Faunal Diversity: Wild Water Buffalo, Bastar Hill Myna, Predators, and Avifauna")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-044",
        "Geographic Scope": "Indravati River Basin & Kanger Valley Sanctuaries",
        "Primary Classification": "Zoology, Wildlife Biology & Conservation Ecology",
        "Confidence Level": "HIGH (Wildlife Institute of India, ZSI, IUCN Red List)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Flagship and State Species of Bastar")
    doc.add_paragraph(
        "Bastar harbors critical habitats for two official state symbols of Chhattisgarh:\n"
        "• Wild Water Buffalo (Bubalus arnee / Van Bhainsa): The State Animal of Chhattisgarh; an endangered bovine surviving in genetically "
        "pure wild herds within the protected grasslands of Indravati National Park and Pamed Sanctuary.\n"
        "• Bastar Hill Myna (Gracula religiosa peninsularis / Pahadi Myna): The State Bird of Chhattisgarh; an endemic subspecies restricted "
        "to the dense canopy hollows of Kanger Valley National Park, famous for its extraordinary ability to mimic human speech and forest sounds."
    )
    
    save_document(doc, "44_Wildlife_and_Natural_Heritage.docx")

def build_doc_45():
    doc = create_base_document("45. Rivers, Waterfalls, and Water Heritage", "Hydrography: Indravati, Sabari, Kanger, Chitrakote, and Tirathgarh Cascades")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-045",
        "Geographic Scope": "Indravati-Godavari Catchment System",
        "Primary Classification": "Geomorphology, Hydrology & Eco-Tourism",
        "Confidence Level": "HIGH (Central Water Commission, Geological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Major Waterfalls and Fluvial Geomorphology")
    headers = ["Waterfall Name", "River / Stream", "Drop Height (m)", "Geological Formation & Key Characteristics"]
    rows = [
        ["Chitrakote Falls", "Indravati River", "29 m (95 ft)", "Horseshoe-shaped plunge waterfall; widest in India (~300m during monsoon); 'Niagara of India'"],
        ["Tirathgarh Falls", "Kanger / Mugabahar River", "91 m (299 ft)", "Block-stepped cascade slicing through bedded Vindhyan/Cuddapah sandstones in Kanger Valley"],
        ["Mendri Ghumar", "Seasonal stream / Indravati gorge", "70 m (230 ft)", "Dramatic seasonal gorge plunge nestled in lush forested amphitheatre near Chitrakote"],
        ["Tamda Ghumar", "Seasonal rivulet", "45 m (148 ft)", "Scenic cliff-edge waterfall surrounded by deep sal forest and bird nesting colonies"],
        ["Chitradhara", "Indravati tributary", "20 m (66 ft)", "Horseshoe-shaped stepped cascade located near Potanar village"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "45_Rivers_Waterfalls_and_Water_Heritage.docx")

def build_doc_46():
    doc = create_base_document("46. Caves, Geological, and Natural Sites", "Karst Speleology: Kutumsar, Kailash, Dandak Caves and Subterranean Fauna")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-046",
        "Geographic Scope": "Kanger Valley Karst Limestone Formations",
        "Primary Classification": "Speleology, Karst Geology & Biospeleology",
        "Confidence Level": "HIGH (Geological Survey of India, Zoological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Karst Speleology of the Kanger Valley")
    doc.add_paragraph(
        "The Kanger Valley contains one of Central India's most extensive subterranean karst cave systems, formed through the dissolution "
        "of late Proterozoic limestone and dolomite beds by acidic groundwater. Key caverns include:\n"
        "• Kutumsar Cave: Located 35 meters below surface level, extending over 330 meters with magnificent stalactites, stalagmites, and subterranean pools.\n"
        "• Kailash Cave: Known for its gigantic limestone pillar resembling a Shiva lingam.\n"
        "• Dandak Cave: Multi-chambered cave with massive dripstone draperies and natural acoustics."
    )
    
    add_heading_2(doc, "2. Endemic Subterranean Biospeleology")
    doc.add_paragraph(
        "Kutumsar Cave houses unique troglobitic (cave-adapted) fauna that have lost pigmentation and ocular function over evolutionary time:\n"
        "• Blind Cave Fish (Nemacheilus exiguus / Indoreonectes evezardi kempianus): A blind, pigmentless loach adapted to dark subterranean streams.\n"
        "• Cave Cricket (Kempiola shankari): An endemic troglophilic cricket species."
    )
    
    save_document(doc, "46_Caves_Geological_and_Natural_Sites.docx")

def build_doc_47():
    doc = create_base_document("47. National Parks and Wildlife Sanctuaries", "Protected Area Networks: Kanger Valley NP, Indravati NP, and Bhairamgarh")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-047",
        "Geographic Scope": "Bastar Division Protected Area Network",
        "Primary Classification": "Protected Area Management & Biodiversity Conservation",
        "Confidence Level": "HIGH (Chhattisgarh Forest Department, National Tiger Conservation Authority)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Protected Area Network of Bastar")
    headers = ["Protected Area", "Status & Year", "Area (sq km)", "District", "Ecological Importance & Key Species"]
    rows = [
        ["Kanger Valley National Park", "National Park (1982)", "200.00", "Bastar (Jagdalpur)", "Pristine Sal forests, karst caves, Tirathgarh falls, Bastar Hill Myna habitat"],
        ["Indravati National Park & Tiger Reserve", "National Park (1981), Tiger Reserve (1983)", "1,258.37", "Bijapur", "Prime grassland and deciduous habitat for endangered Wild Water Buffalo & Royal Bengal Tiger"],
        ["Bhairamgarh Wildlife Sanctuary", "Sanctuary (1983)", "138.95", "Bijapur", "Southern mixed deciduous forest sheltering Wild Buffalo, Leopard, Chital"],
        ["Pamed Wildlife Sanctuary", "Sanctuary (1983)", "262.00", "Bijapur", "Corridor connecting with Telangana and Andhra Pradesh forests; Teak and Bamboo biome"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "47_National_Parks_and_Wildlife_Sanctuaries.docx")

if __name__ == "__main__":
    print("Building Batch 5: Documents 36 to 47...")
    build_doc_36()
    build_doc_37()
    build_doc_38()
    build_doc_39()
    build_doc_40()
    build_doc_41()
    build_doc_42()
    build_doc_43()
    build_doc_44()
    build_doc_45()
    build_doc_46()
    build_doc_47()
    print("Batch 5 completed successfully.")
