import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_59():
    doc = create_base_document("59. Sacred Groves and Sacred Landscapes", "Devkot Ecology, Taboo Governance, Biocultural Refugia & Biodiversity Preservation")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-059",
        "Geographic Scope": "Bastar Division Rural Landscape (Over 800 Documented Devkots)",
        "Primary Classification": "Sacred Ecology, Ethnobotany & Conservation Anthropology",
        "Confidence Level": "HIGH (UNESCO Sacred Natural Sites Registry, Forest Dept CG)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Devkot System as Living Biocultural Sanctuaries")
    doc.add_paragraph(
        "In Bastar, sacred groves (locally known as 'Devkot' or 'Matagudi') constitute ancient patches of climax forest preserved inviolate "
        "through strict customary religious taboos. Dedicated to village deities and ancestral spirits, entering a Devkot with footwear, cutting timber, "
        "hunting, or gathering dry fuel wood is universally prohibited. As a result, Devkots serve as vital relic gene pools for endangered "
        "medicinal lianas, ancient Sal trees, subterranean springs, and rare birds."
    )
    
    save_document(doc, "59_Sacred_Groves_and_Sacred_Landscapes.docx")

def build_doc_60():
    doc = create_base_document("60. Tribal Markets and Haats", "Weekly Haat Network: Tokapal, Narayanpur, Geedam: Barter, Cockfights, and Social Media")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-060",
        "Geographic Scope": "Bastar Division Weekly Haat Circuits",
        "Primary Classification": "Economic Anthropology, Peasant Markets & Information Networks",
        "Confidence Level": "HIGH (District Marketing Federations, Fieldwork Ethnography)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Multidimensional Function of Weekly Haats")
    doc.add_paragraph(
        "The weekly tribal market ('Haat-Bazaar') functions as the commercial, social, romantic, and news-disseminating heartbeat of Bastar life. "
        "Villagers walk dozens of kilometers carrying forest produce (Mahua, Tendu, honey, mushrooms) to exchange for salt, dried fish, "
        "iron tools, and cloth. Key haats include Tokapal (famous for pottery and metal craft), Narayanpur (famous for forest honey and cane), "
        "and Geedam (major agricultural hub). The haat also hosts traditional rooster fights ('Kukuda Ladai'), where razor-spurred cocks duel "
        "in intense community sporting rings governed by unwritten honour codes."
    )
    
    save_document(doc, "60_Tribal_Markets_and_Haats.docx")

def build_doc_61():
    doc = create_base_document("61. Museums and Cultural Institutions", "Custodians of Heritage: Zonal Anthropological Museum, Bastar Art Galleries & TRI")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-061",
        "Geographic Scope": "Jagdalpur, Raipur, Bhopal (Bastar Heritage Collections)",
        "Primary Classification": "Museology, Archival Science & Cultural Preservation",
        "Confidence Level": "HIGH (Anthropological Survey of India, Ministry of Culture)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Premier Cultural Repositories")
    doc.add_paragraph(
        "Bastar's material and intangible heritage is documented and preserved across major institutional museums:\n"
        "• Zonal Anthropological Museum (Jagdalpur): Established by the Anthropological Survey of India (AnSI), exhibiting authentic dioramas "
        "of Maria, Muria, Bhatra, and Dhurwa dwellings, original Ghotul pillars, hunting weapons, and musical instruments.\n"
        "• Bastar Tribal Museum (Dharampura): Showcasing masterworks of Dhokra bell metal, wrought iron craft, and terracotta votive statues.\n"
        "• Tribal Research and Training Institute (TRI Raipur): State archival body maintaining linguistic records, tribal customary law texts, and ethnographic monographs."
    )
    
    save_document(doc, "61_Museums_and_Cultural_Institutions.docx")

def build_doc_62():
    doc = create_base_document("62. Heritage Researchers and Important People", "Biographical Directory: Elwin, Grigson, Gundadhur, Pravir Chandra, Jaidev Baghel")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-062",
        "Geographic Scope": "Bastar Historical & Cultural Figures",
        "Primary Classification": "Biographical History & Intellectual Historiography",
        "Confidence Level": "HIGH (Scholarly Biographies, National Archives, State Records)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Key Historical, Scholarly, and Artistic Personalities")
    headers = ["Name", "Lifespan / Dates", "Domain / Role", "Key Contribution to Bastar Heritage"]
    rows = [
        ["Gundadhur", "Fl. 1910 CE", "Indigenous Freedom Fighter", "Leader of the 1910 Bhumkal Rebellion from Nethanar village; symbol of anti-colonial forest resistance"],
        ["Maharaja Pravir Chandra Bhanj Deo", "1929 - 1966 CE", "Last Crowned King & Adivasi Leader", "Advocate of tribal autonomy; author of 'I Take This Word'; martyred in police firing at Jagdalpur Palace"],
        ["Dr. Verrier Elwin", "1902 - 1964 CE", "Anthropologist & Author", "Pioneered landmark ethnographies: 'The Muria and Their Ghotul' (1947), 'The Tribal Art of Middle India'"],
        ["W.V. Grigson", "1896 - 1948 CE", "Colonial Administrator & Ethnographer", "Authored 'The Maria Gonds of Bastar' (1938), documenting customary laws, clans, and shifting cultivation"],
        ["Dr. Shankar Tiwari", "1928 - 1998 CE", "Geographer & Speleologist", "Scientifically explored and mapped Kutumsar Cave, Kailash Cave, and Kanger Valley biodiversity"],
        ["Jaidev Baghel", "1949 - 2014 CE", "Master Craftsman (Ghadwa)", "National Awardee who elevated Bastar Dhokra lost-wax metal craft to international modern art galleries"],
        ["Dharampal Saini", "1930 - Present", "Social Worker & Educator", "Founded Mata Rukmini Ashram, pioneering female education and athletic excellence among tribal girls in Bastar"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "62_Heritage_Researchers_and_Important_People.docx")

def build_doc_63():
    doc = create_base_document("63. Literature and Bastar Cultural Representation", "Historiography, Ethnographies, Hindi Literature, and Postcolonial Critique")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-063",
        "Geographic Scope": "Scholarly Literature & Creative Arts on Bastar",
        "Primary Classification": "Literary Criticism, Postcolonial Studies & Cultural Representation",
        "Confidence Level": "HIGH (Academic Journals, Sahitya Akademi, Ethnographic Literature)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Critical Analysis of Bastar in Literary Imagination")
    doc.add_paragraph(
        "Bastar has occupied a complex space in literary representation, oscillating between colonial 'noble savage' romanticism, "
        "sensationalized journalistic framing, and authentic subaltern tribal literature. Renowned Hindi writers such as Vinod Kumar Shukla "
        "and ethnographers have explored Bastar's deep forest consciousness, while modern Gondi poets and Halbi oral bards are reclaiming "
        "their historical narratives from external stereotypes."
    )
    
    save_document(doc, "63_Literature_and_Bastar_Cultural_Representation.docx")

def build_doc_64():
    doc = create_base_document("64. Bastar in Indian History", "Dandakaranya to Frontier Realm: Epic Geography, Chalukya Clashes & Maratha Treaties")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-064",
        "Geographic Scope": "Dandakaranya Macro-Region / Central-Southern India",
        "Primary Classification": "Macro-History, Historical Geography & Geopolitics",
        "Confidence Level": "HIGH (Epigraphia Indica, R.C. Majumdar, State Gazetteers)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Dandakaranya in Early Subcontinental Geopolitics")
    doc.add_paragraph(
        "In ancient epic and Puranic geography, Bastar formed the dense core of 'Dandakaranya', the great southern wilderness crossed by Lord Rama "
        "during his exile. Epigraphically, the territory functioned as an impenetrable frontier buffer kingdom between the Northern Deccan empires "
        "(Vakatakas, Kalachuris) and the Eastern Peninsular powers (Eastern Chalukyas, Cholas, and Eastern Gangas), maintaining a fierce "
        "regional political independence protected by its rugged mountain barriers and malaria-shielded dense Sal forests."
    )
    
    save_document(doc, "64_Bastar_in_Indian_History.docx")

def build_doc_65():
    doc = create_base_document("65. Bastar During Colonial Rule", "British Indirect Rule, Forest Enclosures, Meriah Inquiries & Feudatory Statecraft")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-065",
        "Geographic Scope": "Bastar Feudatory State under Central Provinces & Berar",
        "Primary Classification": "Colonial History, Imperial Forestry & Subaltern Studies",
        "Confidence Level": "HIGH (National Archives of India, Central Provinces Administrative Reports)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. British Penetration and Forest Enclosure Policies")
    doc.add_paragraph(
        "Following the lapse of the Nagpur Maratha state to the British East India Company in 1853, Bastar was placed under indirect colonial "
        "supervision. The British introduced commercial forestry, reserving vast tracts of Sal and Teak forests for railway sleeper extraction, "
        "imposing heavy taxes on forest produce, prohibiting swidden agriculture (Penda), and extracting unpaid forced labor (Begar), "
        "triggering widespread indigenous unrest."
    )
    
    save_document(doc, "65_Bastar_During_Colonial_Rule.docx")

def build_doc_66():
    doc = create_base_document("66. Bastar Resistance and Rebellions", "Chronology of Anti-Colonial Uprisings: Halba, Koi, Muria, and Lingagiri Revolts")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-066",
        "Geographic Scope": "Bastar Princely State Uprisings (1774 - 1876 CE)",
        "Primary Classification": "Subaltern Resistance, Tribal Rebellions & Military History",
        "Confidence Level": "HIGH (National Archives of India, CP Administrative Records)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Chronological Master Table of Anti-Colonial Tribal Revolts")
    headers = ["Rebellion Name", "Year / Period", "Primary Leaders", "Core Causes & Historical Significance"]
    rows = [
        ["Halba Rebellion", "1774 - 1779 CE", "Ajmer Singh", "Halba militia defended sovereign autonomy against Maratha-backed usurper Daryao Deva"],
        ["Bhopalpatnam Struggle", "1795 CE", "Gond warrior chiefs", "Gond archers routed British Captain Blunt's survey expedition, maintaining sovereign isolation"],
        ["Tara Rebellion", "1842 - 1854 CE", "Dalganjan Singh", "Armed resistance against British interference in internal court affairs and taxation"],
        ["Lingagiri Rebellion", "1856 - 1857 CE", "Nagraj / Dhurwa chiefs", "Part of the First Indian War of Independence (1857); anti-British guerrilla rebellion"],
        ["Koi Revolt", "1859 CE", "Dorla/Koi headmen & Nangur Zamindar", "Legendary forest conservation revolt: 'Every head for a Teak tree'; stopped British timber plunder"],
        ["Muria Rebellion", "1876 CE", "Jhāra Siraha & Muria youth", "Encircled King Bhairam Deo; forced dismissal of corrupt British-appointed Diwan Gopinath"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "66_Bastar_Resistance_and_Rebellions.docx")

def build_doc_67():
    doc = create_base_document("67. Bhumkal Rebellion", "The Great 1910 Uprising: Gundadhur, Secret Signals, Forest Sovereignty & Historiography")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-067",
        "Geographic Scope": "Pan-Bastar State (Jagdalpur, Kanger, Bijapur, Antagarh)",
        "Primary Classification": "Subaltern Resistance, Anti-Imperialism & Ethno-History",
        "Confidence Level": "HIGH (National Archives of India Foreign & Political Dept, Standen & de Brett Reports)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Great Bhumkal (Earthquake of Resistance) of 1910")
    doc.add_paragraph(
        "The Bhumkal of 1910 represents one of the most sophisticated, coordinated anti-colonial tribal uprisings in Indian history. "
        "Triggered by the British reservation of two-thirds of Bastar's forests, the brutal suppression of traditional livelihood rights, "
        "and forced school-construction labor, the rebellion engulfed the entire kingdom within weeks under the military leadership of "
        "Gundadhur of Nethanar village, supported by Rajmata Subran Kunwar and Lal Kalendra Singh."
    )
    
    add_heading_2(doc, "2. Symbolic Communication and Forest Warfare")
    doc.add_paragraph(
        "The rebels organized covert communication across hundreds of forest villages using secret emissaries carrying three sacred symbols:\n"
        "1. Mango Twigs (Amba Phali): Signaling common kinship and collective identity.\n"
        "2. Dried Red Chillies (Lal Mirch): Signaling revolutionary fire, bravery, and urgency.\n"
        "3. Arrows and Earth Knots: Designating combat assembly coordinates and dates.\n\n"
        "The rebels liberated police stations, opened government grain granaries to starving villagers, and blockaded British troops at "
        "Kurutguda and Dabpal before facing heavy artillery under British Major Geary."
    )
    
    save_document(doc, "67_Bhumkal_Rebellion.docx")

def build_doc_68():
    doc = create_base_document("68. Post-Independence Bastar", "Accession (1948), The Dandakaranya Refugee Project, and Creation of Chhattisgarh")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-068",
        "Geographic Scope": "Bastar District (Madhya Pradesh / Chhattisgarh Eras)",
        "Primary Classification": "Modern Political History & Developmental Geography",
        "Confidence Level": "HIGH (Ministry of States, Planning Commission of India, Census)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Post-Independence Integration and the Dandakaranya Project")
    doc.add_paragraph(
        "Following the 1948 merger, the Government of India launched the 'Dandakaranya Project' in the 1950s to rehabilitate displaced East Pakistani "
        "(Bengali) refugees across Paralkote, Pakhanjore, and Kondagaon tracts. While introducing new agricultural techniques, this massive demographic "
        "influx altered local tribal-non-tribal land equations and accelerated forest clearing."
    )
    
    save_document(doc, "68_Post_Independence_Bastar.docx")

def build_doc_69():
    doc = create_base_document("69. Modern Bastar and Cultural Change", "Urbanization, Mobile Digital Access, Youth Aspiration & Continuity of Identity")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-069",
        "Geographic Scope": "Bastar Division Urban & Semi-Urban Centers",
        "Primary Classification": "Sociology of Modernization & Cultural Change",
        "Confidence Level": "HIGH (Sociological Field Surveys, Census of India 2011/2021 Data)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Dialectic of Tradition and Digital Modernity")
    doc.add_paragraph(
        "Contemporary Bastar is undergoing rapid socio-cultural evolution driven by high-speed fiber-optic connectivity, national highway expansions, "
        "and higher education. While youth participate in digital creative economies and modern athletics, core cultural pillars—such as Devigudi "
        "worship, community marriage negotiations, and participation in the Dussehra chariot pulling—remain resiliently unbroken."
    )
    
    save_document(doc, "69_Modern_Bastar_and_Cultural_Change.docx")

def build_doc_70():
    doc = create_base_document("70. Socioeconomic Profile", "Demographics, Female Sex Ratio, Human Development Indicators, and Agrarian Baseline")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-070",
        "Geographic Scope": "Bastar Division (All 7 Districts)",
        "Primary Classification": "Demography, Development Economics & Gender Sociology",
        "Confidence Level": "HIGH (Census of India, NITI Aayog Aspirational Districts Indicators)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Demographic and Gender Profile")
    doc.add_paragraph(
        "A striking demographic feature of Bastar Division is its positive female sex ratio (averaging 1,020 to 1,040 females per 1,000 males across "
        "tribal districts), significantly higher than the national Indian average. This reflects high cultural gender parity, absence of female "
        "foeticide, and equal participation of women in agricultural, market, and social spheres."
    )
    
    save_document(doc, "70_Socioeconomic_Profile.docx")

def build_doc_71():
    doc = create_base_document("71. Education and Development", "Ashram Shalas, Multilingual Education (Gondi/Halbi), and Higher Institutions")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-071",
        "Geographic Scope": "Bastar Division Educational Infrastructure",
        "Primary Classification": "Educational Policy, Tribal Pedagogy & Human Resource Development",
        "Confidence Level": "HIGH (Dept of School Education CG, Ministry of Tribal Affairs)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Educational Transformation and Mother-Tongue Pedagogy")
    doc.add_paragraph(
        "Education in Bastar has expanded through residential 'Ashram Shalas', Eklavya Model Residential Schools (EMRS), and bilingual education "
        "initiatives incorporating Gondi, Halbi, and Bhatri in primary grades to bridge the transition to standard Hindi. Higher education is anchored "
        "by Shaheed Mahendra Karma Vishwavidyalaya (Bastar University) and Government Medical College, Jagdalpur."
    )
    
    save_document(doc, "71_Education_and_Development.docx")

def build_doc_72():
    doc = create_base_document("72. Tribal Rights and Governance Context", "Fifth Schedule, PESA Act 1996, Gram Sabha Sovereignty, and Customary Law")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-072",
        "Geographic Scope": "Scheduled Areas under Fifth Schedule (Bastar Division)",
        "Primary Classification": "Constitutional Law, Tribal Jurisprudence & Local Self-Governance",
        "Confidence Level": "HIGH (Constitution of India, Ministry of Panchayati Raj, Supreme Court Rulings)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Constitutional Protection and Gram Sabha Empowerment")
    doc.add_paragraph(
        "The entire Bastar Division is notified under the Fifth Schedule of the Constitution of India. Under the Provisions of the Panchayats "
        "(Extension to Scheduled Areas) Act (PESA), 1996, and Chhattisgarh PESA Rules 2022, the village Gram Sabha is empowered with statutory "
        "sovereignty over minor forest produce, dispute resolution under customary law, water resources, and mandatory prior informed consent "
        "for any land acquisition or mining exploration."
    )
    
    save_document(doc, "72_Tribal_Rights_and_Governance_Context.docx")

def build_doc_73():
    doc = create_base_document("73. Forest Rights and Community Relationships", "The Forest Rights Act (FRA 2006): Individual & Community Forest Resource Rights")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-073",
        "Geographic Scope": "Bastar Division Forest Tracts & Protected Areas",
        "Primary Classification": "Environmental Law, Agrarian Land Titling & Community Forestry",
        "Confidence Level": "HIGH (Ministry of Tribal Affairs, CFR-Learning Network India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Implementation of the Forest Rights Act (2006)")
    doc.add_paragraph(
        "The Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006 (FRA) has been a pivotal instrument "
        "for historical restitution in Bastar. Thousands of tribal farmers have received Individual Forest Rights (IFR) land titles, while entire "
        "villages inside Kanger Valley National Park have successfully secured Community Forest Resource Rights (CFRR), granting them statutory "
        "management, protection, and harvesting authority over their ancestral forest homelands."
    )
    
    save_document(doc, "73_Forest_Rights_and_Community_Relationships.docx")

if __name__ == "__main__":
    print("Building Batch 7: Documents 59 to 73...")
    build_doc_59()
    build_doc_60()
    build_doc_61()
    build_doc_62()
    build_doc_63()
    build_doc_64()
    build_doc_65()
    build_doc_66()
    build_doc_67()
    build_doc_68()
    build_doc_69()
    build_doc_70()
    build_doc_71()
    build_doc_72()
    build_doc_73()
    print("Batch 7 completed successfully.")
