import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_10():
    doc = create_base_document("10. Gond Heritage and History", "The Koyatur Universe: Cosmology, Phratries, and Historical Trajectory")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-010",
        "Geographic Scope": "Central India & Bastar Division (Gondwana Cultural Zone)",
        "Primary Classification": "Cultural Anthropology, Ethnography & Indigenous History",
        "Confidence Level": "HIGH (Verrier Elwin, Christoph von Fürer-Haimendorf, Anthropological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Koyatur Identity and Myth of Origin")
    doc.add_paragraph(
        "The Gonds, who self-identify as 'Koitur' or 'Koyatur' (meaning 'people of the earth' or 'descendants of the womb of Mother Nature'), "
        "form the demographic and mythological foundation of Bastar. According to the supreme Gondi epic narrated by traditional bards "
        "(Pradhans), the Koyatur ancestors emerged from the sacred cave of Kachargadh under the leadership of the legendary culture hero "
        "Pahandi Kupar Lingo. Pahandi Lingo established the social code, the four-phratry kinship division, musical instruments (the Bana), "
        "and the worship of the invisible supreme reality, Phersa Pen (or Budha Dev)."
    )
    
    add_heading_2(doc, "2. Phratry (Saga) and Clan (Gotra) Organization")
    doc.add_paragraph(
        "The social universe is segmented into four exogamous phratries (Sagas), defined by the number of ancestral deities (Vens) worshipped:\n"
        "• 4-Deo Phratry (Nalwen): Totem = Tortoise / Crocodile\n"
        "• 5-Deo Phratry (Seiwen): Totem = Crane / Hawk\n"
        "• 6-Deo Phratry (Sarwen): Totem = Tiger / Peepal\n"
        "• 7-Deo Phratry (Yelwen): Totem = Porcupine / Snake\n\n"
        "Marriage is strictly exogamous between different Sagas. Cross-cousin marriage (Doodh Lautana, or 'returning the milk') is the "
        "preferred kinship alliance, ensuring economic cohesion and social solidarity."
    )
    
    save_document(doc, "10_Gond_Heritage_and_History.docx")

def build_doc_11():
    doc = create_base_document("11. Maria Heritage and Culture", "Comparative Ethnography of Hill Maria (Abujhmaria) & Dandami Maria (Bison Horn)")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-011",
        "Geographic Scope": "Abujhmad Plateau (Narayanpur/Bijapur) & Dantewada/Sukma Basin",
        "Primary Classification": "Ethnographic Analysis & Indigenous Material Culture",
        "Confidence Level": "HIGH (W.V. Grigson 'The Maria Gonds of Bastar', Census PVTG Reports)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Critical Ethnographic Distinction")
    doc.add_paragraph(
        "Anthropological research strictly distinguishes between two culturally distinct Maria groups:\n"
        "1. Hill Maria (Meta Koitur / Abujhmaria): Inhabitants of the isolated Abujhmad hills; classified as a Particularly Vulnerable "
        "Tribal Group (PVTG). They historically practice 'Penda' (rotational swidden cultivation) and maintain untouched forest-dwelling autonomy.\n"
        "2. Dandami Maria (Bison Horn Maria / Khalpati Koitur): Inhabitants of the plains and river valleys of Dantewada, Bijapur, and Sukma. "
        "Renowned for their majestic 'Gaur Dance' (featuring headdresses made from wild bison horns and cowrie shells) and living megalithic menhir erections."
    )
    
    add_heading_2(doc, "Comparative Matrix: Hill Maria vs Dandami Maria")
    headers = ["Cultural Domain", "Hill Maria (Abujhmaria)", "Dandami Maria (Bison Horn Maria)"]
    rows = [
        ["Habitat & Elevation", "Dense forest hills of Abujhmad (>800m)", "Riverine plains of Dantewada/Bijapur (300-600m)"],
        ["Agricultural System", "Penda (Swidden/Slash-and-Burn farming)", "Settled wetland rice & Kosra cultivation"],
        ["Iconic Performance", "Kaksar harvest dance with brass bells", "Gaur Dance with massive bison horn headdresses"],
        ["Youth Institution", "Separate male dormitory (Ghotul variant)", "Informal youth gathering spaces"],
        ["Megalithic Practice", "Wooden poles (Khamba) occasionally", "Stone menhirs (Uruskal) and cairns (Danya)"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "11_Maria_Heritage_and_Culture.docx")

def build_doc_12():
    doc = create_base_document("12. Muria Heritage and Culture", "Ghotul Youth Institution, Social Structure, and Aesthetic Traditions")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-012",
        "Geographic Scope": "Central Bastar Plateau & Kondagaon District",
        "Primary Classification": "Social Anthropology & Ethnomusicology",
        "Confidence Level": "HIGH (Verrier Elwin 'The Muria and Their Ghotul', Anthropological Survey)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Muria Social Fabric and the Ghotul")
    doc.add_paragraph(
        "The Muria represent one of the most culturally organized tribal groups of the Bastar plateau. Their community life is famously "
        "centered around the 'Ghotul', a co-educational village youth dormitory that serves as an institutional school for civic duties, "
        "ethics, egalitarian cooperation, oral history, music, dance, and democratic self-governance."
    )
    
    add_callout(doc,
        "ACADEMIC RE-EVALUATION: The Ghotul has frequently been sensationalized in colonial and non-scholarly literature. Anthropological "
        "evidence confirms that the Ghotul is fundamentally a sacred social university presided over by the deity Lingo Pen. "
        "Adolescent boys (Cheliks) and girls (Motiaris) learn village governance, hospitality, funeral assistance, agricultural labor "
        "reciprocity, and artistic excellence under elected student leaders (Sirdar and Belosa).",
        "SCHOLARLY RIGOR & CULTURAL SENSITIVITY"
    )
    
    add_heading_2(doc, "2. Dances and Musical Rhythms")
    doc.add_paragraph(
        "Muria cultural expression features energetic dances such as the 'Mandari Dance' (performed with cylindrical terracotta and wood drums), "
        "'Hulki Manda', and 'Gedi Dance' (acrobatic balance on bamboo stilts during the monsoon Hareli festival)."
    )
    
    save_document(doc, "12_Muria_Heritage_and_Culture.docx")

def build_doc_13():
    doc = create_base_document("13. Halba Heritage and Culture", "Soldier-Cultivators, Linguistic Dominance, and Cultural Syncretism")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-013",
        "Geographic Scope": "Northern and Central Bastar, Kondagaon, Kanker",
        "Primary Classification": "Ethnography, Military History & Socio-Linguistics",
        "Confidence Level": "HIGH (Russell & Hiralal, Anthropological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Historical Identity as Royal Militia")
    doc.add_paragraph(
        "The Halbas historically served as the elite personal military guard and soldier-cultivators of the Kakatiya Kings of Bastar. "
        "Their language, Halbi (an Eastern Indo-Aryan language with archaic Marathi, Odia, and Chhattisgarhi affinities), became the primary "
        "lingua franca (trade language) of the entire Bastar region, facilitating communication between disparate Dravidian-speaking tribal clans."
    )
    
    add_heading_2(doc, "2. Social Stratification and Religious Practices")
    doc.add_paragraph(
        "The Halba community is divided into two primary endogamous sub-groups:\n"
        "• Purait (Pure Halba): Descendants of the original landed aristocracy and royal soldiers.\n"
        "• Surait (Mixed Halba): Descendants of secondary lineage unions.\n\n"
        "Religious practices blend ancestor worship with Vaishnavism and the Kabirpanth reform movement, reflecting their role as "
        "a cultural bridge between tribal animism and Sanskritic traditions."
    )
    
    save_document(doc, "13_Halba_Heritage_and_Culture.docx")

def build_doc_14():
    doc = create_base_document("14. Dhurwa and Dorla Heritage", "Riparian Adaptations, Parji Linguistic Heritage, and Godavari Connections")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-014",
        "Geographic Scope": "Southern Bastar, Kanger Valley, Sukma & Bijapur (Godavari Basin)",
        "Primary Classification": "Linguistic Anthropology & Ethno-Ecology",
        "Confidence Level": "HIGH (T. Burrow & M.B. Emeneau 'The Parji Language', Census Reports)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Dhurwa Heritage and Master Basketry")
    doc.add_paragraph(
        "The Dhurwas (historically referred to as Parjas in early linguistic literature) inhabit the dense forests around the Kanger Valley. "
        "They speak 'Parji' (Dhurwa), an archaic and highly distinct Central Dravidian language. Dhurwas are celebrated as master craftsmen "
        "of cane and bamboo, producing weather-proof hunting baskets, granaries, and the 'Chhind' wild-palm rain shields."
    )
    
    add_heading_2(doc, "2. Dorla Cultural Continuum with the Godavari Valley")
    doc.add_paragraph(
        "The Dorlas inhabit the southernmost taluks of Sukma and Bijapur along the Sabari and Godavari rivers. Speaking Dorli (a dialect of Koya, "
        "belonging to South-Central Dravidian), their culture shares deep architectural, culinary, and musical affinities with the Koya and "
        "Gondi populations of neighboring Telangana and Andhra Pradesh."
    )
    
    save_document(doc, "14_Dhurwa_and_Dorla_Heritage.docx")

def build_doc_15():
    doc = create_base_document("15. Other Communities and Cultural Groups", "Bhatra, Gadaba, Ghadwa, Lohar, Mahra, and Artisan Castes")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-015",
        "Geographic Scope": "Bastar Division Trans-Border Zones",
        "Primary Classification": "Sociology of Artisan Guilds & Inter-community Symbiosis",
        "Confidence Level": "HIGH (Tribal Research and Training Institute Raipur, Census Data)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Artisan and Specialized Guild Communities")
    doc.add_paragraph(
        "Bastar's socio-economic ecosystem relies upon intricate symbiotic relationships between agrarian tribes and hereditary artisan guilds:\n"
        "• Ghadwa: Hereditary brass smiths practicing lost-wax Dhokra metal casting.\n"
        "• Agariya / Lohar: Traditional iron-smelters and blacksmiths forging agricultural and ritual implements.\n"
        "• Kumhar: Potters shaping votive terracotta deities and roofing tiles.\n"
        "• Mahra / Panka: Weavers producing coarse cotton fabrics, gamchhas, and traditional sarees.\n"
        "• Bhatra: Agrarian community speaking Bhatri, historically serving as royal temple attendants and literate courtiers."
    )
    
    save_document(doc, "15_Other_Communities_and_Cultural_Groups.docx")

def build_doc_16():
    doc = create_base_document("16. Tribal Societies and Social Structure", "Kinship Systems, Clan Exogamy, Village Councils, and Customary Law")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-016",
        "Geographic Scope": "Bastar Division Indigenous Communities",
        "Primary Classification": "Social Systems & Customary Jurisprudence",
        "Confidence Level": "HIGH (Anthropological Survey of India & PESA Legal Framework)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Traditional Village Governance Matrix")
    doc.add_paragraph(
        "Traditional Bastar villages are governed through a tri-partite customary leadership structure:\n"
        "1. Patel / Gaontia: The secular administrative head responsible for village boundary disputes, taxation, and state interaction.\n"
        "2. Waddai / Perma / Pujari: The religious priest presiding over village deity rituals, seed-consecration, and harvest offerings.\n"
        "3. Siraha / Guniya: The spiritual shaman and healer who communicates with spirits and ancestral forces in trance states.\n"
        "4. Kotwar: The village messenger and watchman (usually from the Mahra community), announcing assemblies and haat dates."
    )
    
    save_document(doc, "16_Tribal_Societies_and_Social_Structure.docx")

def build_doc_17():
    doc = create_base_document("17. Indigenous Knowledge Systems", "Forest Botany, Hydrology, Swidden Management, and Metallurgy")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-017",
        "Geographic Scope": "Bastar Forest Ecosystems",
        "Primary Classification": "Traditional Ecological Knowledge (TEK) & Ethno-Science",
        "Confidence Level": "HIGH (Ethnobotanical Surveys, Botanical Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Ethno-Botanical and Pharmacological Wisdom")
    doc.add_paragraph(
        "Bastar's tribal elders preserve profound empirical knowledge regarding forest ecosystems:\n"
        "• Phyto-Therapeutics: Over 450 plant species are utilized for targeted herbal remedies (e.g., Tinospora cordifolia / Giloy for fever; "
        "Andrographis paniculata / Bhuineem for liver ailments; Chlorophytum borivilianum / Safed Musli for vitality).\n"
        "• Forest Phenology: Reading flowering cycles of Sal (Sarai) and Mahua to predict monsoon onset and draught patterns.\n"
        "• Indigenous Metallurgy: Charcoal-fired clay blast furnaces capable of smelting local laterite/hematite iron ores at high purities."
    )
    
    save_document(doc, "17_Indigenous_Knowledge_Systems.docx")

def build_doc_18():
    doc = create_base_document("18. Languages and Linguistic Heritage", "Gondi, Halbi, Bhatri, Parji, Dorli: Phylogeny, Contact & Endangerment")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-018",
        "Geographic Scope": "Bastar Division Linguistic Zone",
        "Primary Classification": "Comparative Linguistics & Sociolinguistics",
        "Confidence Level": "HIGH (Linguistic Survey of India, G.A. Grierson, UNESCO Atlas of Endangered Languages)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Polyglot Matrix of Bastar")
    doc.add_paragraph(
        "Bastar constitutes a premier linguistic contact zone where Dravidian and Indo-Aryan language families have interpenetrated for millennia."
    )
    
    add_heading_2(doc, "Linguistic Classification Table")
    headers = ["Language / Dialect", "Language Family", "Primary Speakers", "Linguistic Status & Script"]
    rows = [
        ["Gondi (Muria/Maria)", "Central Dravidian", "Muria, Maria, Gond groups", "Vulnerable; Oral tradition, Devanagari & Gunjala Gondi scripts"],
        ["Halbi", "Eastern Indo-Aryan", "Halba; Regional Lingua Franca", "Widely spoken trade language; written in Devanagari"],
        ["Bhatri", "Eastern Indo-Aryan (Odia link)", "Bhatra community (Eastern Bastar)", "Stable; Transitional dialect bridge to Odia"],
        ["Parji (Dhurwa)", "Central Dravidian (Kolami-Parji branch)", "Dhurwa community (Kanger tract)", "Critically Endangered; Highly conservative grammatical archaisms"],
        ["Dorli", "South-Central Dravidian (Koya branch)", "Dorla community (Sukma/Bijapur)", "Vulnerable; High mutual intelligibility with Telugu & Koya"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "18_Languages_and_Linguistic_Heritage.docx")

if __name__ == "__main__":
    print("Building Batch 2: Documents 10 to 18...")
    build_doc_10()
    build_doc_11()
    build_doc_12()
    build_doc_13()
    build_doc_14()
    build_doc_15()
    build_doc_16()
    build_doc_17()
    build_doc_18()
    print("Batch 2 completed successfully.")
