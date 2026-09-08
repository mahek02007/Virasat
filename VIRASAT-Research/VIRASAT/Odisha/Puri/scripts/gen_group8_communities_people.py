"""
gen_group8_communities_people.py - Generates Documents 21, 22, 23, 24, and 27.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_21():
    doc = PuriDocBuilder(
        title="Communities & Social Culture of Puri: Sevayats, Artisans, & Monastics",
        doc_number="21",
        category="Social Structure & Communities"
    )

    doc.add_h1("1. The Sevayat Community Matrix (Chhatisa Nijoga)")
    doc.add_paragraph("Puri's social organization is uniquely structured around the functioning of the Shree Jagannath Temple. The hereditary servitors (sevayats) belong to a complex spectrum of castes and lineages that cooperate in ritual interdependence:")

    headers = ["Community / Guild", "Hereditary Lineage / Caste Group", "Primary Ritual & Social Responsibilities"]
    rows = [
        ["Daitapati Nijoga", "Sabara tribal ancestry; non-Brahmin ritualists", "Sole custodians during Anavasara, Rath Yatra Pahandi, and Nabakalebara; perform bodily rituals."],
        ["Palia Pushpalaka (Singhari)", "Vedic Brahmin servitors", "Adorning the deities with garments, floral garlands (Tahias), and conducting inner sanctum arati."],
        ["Suara & Mahasuar Nijoga", "Hereditary culinary masters", "Exclusive custody of Roshaghara; cooking 56 bhog across 752 hearths daily."],
        ["Chitrakara Nijoga", "Traditional painter caste (Mahapatra / Moharana)", "Painting Anasara Pattachitra, Rath Yatra chariot murals, and temple wall art."],
        ["Panda / Tirthaguru Community", "Pilgrim-guide Brahmin lineages", "Welcoming, hosting, and guiding regional pilgrims across India; maintaining pilgrim family ledgers."]
    ]
    doc.add_table(headers, rows, [1.5, 2.0, 3.0])

    doc.add_h1("2. Artisanal and Maritime Communities")
    doc.add_paragraph("Complementing temple servitors are vital coastal and craft communities:")
    doc.add_bullet("Kaibarta & Nolia Fisher Communities: Inhabiting the coastal beach settlements (Pentakota), operating traditional wooden catamarans and modern mechanized fishing craft in the Bay of Bengal.", "• ")
    doc.add_bullet("Pipili Muslim Artisans: The Darji (tailor) community of Pipili has for centuries hand-stitched the massive Applique cloth canopies (Mandani) covering the three Rath Yatra chariots, embodying communal harmony.", "• ")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S008"),
        get_source("PUR-S010"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "21_Communities_and_Social_Culture.docx"))

def generate_doc_22():
    doc = PuriDocBuilder(
        title="Traditional Occupations & Guild Systems of Puri",
        doc_number="22",
        category="Traditional Occupations & Economy"
    )

    doc.add_h1("1. The Guild-Based Heritage Economy")
    doc.add_paragraph("Traditional occupations in Puri are sustained by the perpetual cycle of temple rituals, festival processions, and pilgrimage demand. These professions are organized into hereditary guilds (Nijogas) and artisanal cooperatives:")

    headers = ["Traditional Occupation", "Guild / Community", "Tools & Methodologies", "Modern Adaptation & Economic Health"]
    rows = [
        ["Rath Maharana (Chariot Carpenters)", "Maharana woodworkers guild", "Chisels, adzes, traditional wooden measuring canes (Hatha)", "Vibrant; state stipends provided during annual 60-day construction."],
        ["Pattachitra Scroll Painters", "Chitrakara community", "Handmade cloth canvas, stone pigments, mongoose-hair brushes", "Highly prosperous through global e-commerce and Raghurajpur tourism."],
        ["Anand Bazaar Mahaprasad Vendors", "Suara servitor families", "Terracotta Kudua pots, bamboo baskets (Pahandi pakhia)", "Robust daily trade serving tens of thousands of visiting pilgrims."],
        ["Tirtha Panda Guides", "Brahmin panda lineages", "Genealogical palm-leaf records (Pothi / Khata)", "Modernized with digital booking, phone networks, and lodge ownership."],
        ["Conch & Shell Artisans", "Swargadwar beach craft clusters", "Diamond-point rotary cutters, manual polishing wheels", "Active trade catering to domestic souvenirs and ritual buyers."]
    ]
    doc.add_table(headers, rows, [1.5, 1.4, 1.8, 1.8])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "22_Traditional_Occupations.docx"))

def generate_doc_23():
    doc = PuriDocBuilder(
        title="Traditional Knowledge Systems: Ecology, Herbalism, & Metallurgy",
        doc_number="23",
        category="Traditional Knowledge & Sciences"
    )

    doc.add_h1("1. Indigenous Ecological & Material Sciences in Puri")
    doc.add_paragraph("Puri preserves extensive traditional knowledge systems developed over a millennium of temple administration, hydraulic engineering, and coastal survival:")

    headers = ["Knowledge Domain", "Traditional Practice / Formulation", "Scientific & Cultural Mechanism"]
    rows = [
        ["Phuluri Tela (Herbal Oil)", "15-day root-infused sesame oil stored underground in earthen jars", "Applied to deities during Anavasara; anti-fungal, moisture-regulating herbal wood preservative."],
        ["Hydraulic Tank Engineering", "Concentric silt-settling ponds (Narendra, Indradyumna)", "Maintained freshwater aquifers in high-salinity coastal zone through natural sand-filtration layers."],
        ["Natural Pigment Chemistry", "Crushed conch (calcium carbonate) + Haritala (arsenic trisulfide)", "Forms chemically inert, lightfast mineral pigments impervious to tropical humidity."],
        ["Daru Selection Silpa Shastra", "Rigorous botanical diagnostic for Neem trees (absence of bird nests, specific bark marks)", "Ensures selection of dense, resin-rich Azadirachta indica timber with natural anti-termite properties."],
        ["Ashtadhatu Metallurgy", "Eight-metal alloy casting for Nilachakra crest (gold, silver, copper, zinc, lead, tin, iron, mercury)", "Engineered to withstand coastal salt air corrosion for centuries atop the 65m spire."]
    ]
    doc.add_table(headers, rows, [1.5, 2.3, 2.7])

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S002"),
        get_source("PUR-S008"),
        get_source("PUR-S010")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "23_Traditional_Knowledge.docx"))

def generate_doc_24():
    doc = PuriDocBuilder(
        title="Indigenous & Tribal Heritage: The Sabara Substratum of Jagannath",
        doc_number="24",
        category="Indigenous & Tribal Heritage"
    )

    doc.add_h1("1. The Sabara Tribe Connection: Anthropological Analysis")
    doc.add_paragraph("While Odisha boasts 62 distinct Scheduled Tribe communities concentrated predominantly in the interior highlands (Mayurbhanj, Koraput, Sundargarh), Puri is culturally unique in preserving an archaic tribal-Brahmanic synthesis. Anthropologists and historians (Dr. Benimadhab Padhi, Verrier Elwin, Prof. Hermann Kulke) have established that Lord Jagannath originated as a wooden pillar deity (Kitung / Daru Brahma) worshipped by the Austroasiatic Sabara (Saora) tribe:")

    headers = ["Tribal Cultural Element", "Sabara Custom / Practice", "Manifestation in Shree Jagannath Temple, Puri"]
    rows = [
        ["Daitapati Priestly Descent", "Direct lineage traced to tribal chieftain Viswavasu", "Daitapatis hold supreme authority over the deities during intimate, non-Vedic ceremonies."],
        ["Wooden Deity (Daru Brahma)", "Saora 'Kitung' tree totem worship", "Jagannath is sculpted from wood rather than stone/metal, renewed periodically via Nabakalebara."],
        ["Kudua & Raw Herbal Offerings", "Tribal cooking in unglazed clay vessels over woodfire", "Roshaghara cooking methods reflect ancient pre-Vedic community culinary traditions."],
        ["Mourning Rites (Asoucha)", "Tribal death rituals and purification for deceased kin", "Daitapatis observe formal 10-day family bereavement mourning when old deities are buried in Koili Baikuntha."]
    ]
    doc.add_table(headers, rows, [1.5, 2.3, 2.7])

    doc.add_callout(
        title="Geographic Specificity Rule",
        text="It is vital to distinguish between the specific Sabara-Daitapati heritage of Puri and the broader tribal cultures of western and southern Odisha (Dongria Kondh, Santhal, Bonda). General tribal rituals from interior Odisha must not be incorrectly transplanted to coastal Puri.",
        tag="ANTHROPOLOGICAL CAUTION",
        confidence="HIGH"
    )

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S008"),
        get_source("PUR-S010")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "24_Indigenous_and_Tribal_Heritage.docx"))

def generate_doc_27():
    doc = PuriDocBuilder(
        title="Important People of Puri: Kings, Saints, Scholars, & Masters",
        doc_number="27",
        category="Biographical Register"
    )

    doc.add_h1("1. Master Biographical Register of Historical Figures")
    headers = ["Person ID", "Name & Lifespan", "Historical Role", "Major Contribution to Puri", "Sources & Authority"]
    rows = [
        ["PERS-001", "Anantavarman Chodaganga Deva (1077–1147 CE)", "Eastern Ganga Emperor", "Initiated construction of the 65m high Shree Jagannath Temple Vimana.", "Epigraphia Indica [PUR-S016]"],
        ["PERS-002", "Anangabhima Deva III (r. 1211–1238 CE)", "Eastern Ganga King", "Completed the temple; dedicated the empire to Jagannath; instituted Sevayat Record of Rights.", "Madala Panji [PUR-S019]"],
        ["PERS-003", "Gajapati Kapilendra Deva (1434–1466 CE)", "Founder of Suryavamsi Dynasty", "Built outer Meghnad Pacheri wall; patron of vernacular Odia identity.", "Inscriptions of Orissa [PUR-S009]"],
        ["PERS-004", "Gajapati Purushottama Deva (1466–1497 CE)", "Gajapati Emperor", "Hero of Kanchi-Kaveri expedition; introduced Bhoga Mandapa to temple complex.", "Historical Monograph [PUR-S009]"],
        ["PERS-005", "Gajapati Prataparudra Deva (1497–1540 CE)", "Gajapati King", "Royal patron and disciple of Chaitanya Mahaprabhu; established public Kirtan.", "Chaitanya Charitamrita [PUR-S018]"],
        ["PERS-006", "Adi Shankaracharya (788–820 CE)", "Advaita Philosopher", "Established Govardhan Math at Puri, naming it the Eastern Char Dham Peetha.", "Govardhan Peeth Records [PUR-S006]"],
        ["PERS-007", "Shri Chaitanya Mahaprabhu (1486–1533 CE)", "Bhakti Saint & Mystic", "Resided in Gambhira, Puri for 24 years; transformed Gaudiya Vaishnavism.", "Krishnadasa Kaviraja [PUR-S018]"],
        ["PERS-008", "Atibadi Jagannatha Das (1491–1550 CE)", "Panchasakha Saint-Poet", "Composed the Odia Bhagavata; founded Bada Odiya Matha; close associate of Chaitanya.", "Utkal Sahitya [PUR-S012]"],
        ["PERS-009", "Bhakta Salabega (Early 17th Century)", "Devotional Poet", "Composed iconic Odia Jananas; halted Nandighosh chariot through sincere prayer.", "Odia Literature Corpus [PUR-S012]"],
        ["PERS-010", "Guru Kelucharan Mohapatra (1926–2004)", "Odissi Dance Maestro", "Born in Raghurajpur; revived Gotipua & Mahari techniques into global classical Odissi.", "Sangeet Natak Akademi [PUR-S011]"]
    ]
    doc.add_table(headers, rows, [0.8, 1.5, 1.1, 1.8, 1.3])

    doc.add_sources_section([
        get_source("PUR-S008"),
        get_source("PUR-S009"),
        get_source("PUR-S011"),
        get_source("PUR-S016"),
        get_source("PUR-S018"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "27_Important_People.docx"))

if __name__ == "__main__":
    generate_doc_21()
    generate_doc_22()
    generate_doc_23()
    generate_doc_24()
    generate_doc_27()
    print("Group 8 completed successfully.")
