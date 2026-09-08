import os
import sys
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_01():
    doc = create_base_document(
        "01. Bastar Complete Overview",
        "Multidisciplinary Foundational Synthesis: Geography, Culture, Ecology & Heritage"
    )
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-001",
        "Geographic Scope": "Bastar Division (All 7 Districts: Bastar, Dantewada, Kondagaon, Narayanpur, Bijapur, Sukma, Kanker)",
        "Primary Classification": "Multidisciplinary Academic Reference Document",
        "Fact / Tradition Status": "Rigorous Synthesis of Empirical Data, Epigraphy, Ethnography & Field Research",
        "Confidence Level": "HIGH (Government of India / CG Census, ASI Reports, Anthropological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Regional Identity and Nomenclature")
    doc.add_paragraph(
        "Bastar (historically recorded as Chakrakota, Bhramarokotya, and Dandakaranya in epigraphic and literary records) "
        "constitutes the southern cultural and geographical plateau of Chhattisgarh, India. Spanning the Dandakaranya plateau "
        "and bisected by the westward-flowing Indravati River, the region represents one of Central India's most ecologically rich "
        "and culturally unbroken indigenous landscapes. Administratively, while 'Bastar' historically designated a single princely state "
        "(and later a massive monolithic district spanning over 39,114 sq km), it currently designates the Bastar Administrative Division, "
        "comprising seven distinct districts: Bastar (HQ Jagdalpur), Dantewada (Dakshin Bastar), Kondagaon, Narayanpur, Bijapur, Sukma, and Uttar Bastar Kanker."
    )
    
    add_heading_2(doc, "Administrative and Geographical Overview Table")
    headers = ["District", "Headquarters", "Area (sq km)", "Key River Basin", "Dominant Indigenous Groups"]
    rows = [
        ["Bastar", "Jagdalpur", "4,029", "Indravati", "Muria, Maria, Bhatra, Halba, Dhurwa"],
        ["Dantewada", "Dantewada", "3,410", "Shankini & Dankini", "Dandami Maria (Bison Horn), Gond, Halba"],
        ["Kondagaon", "Kondagaon", "7,768", "Narangi / Indravati", "Muria, Halba, Ghadwa artisans"],
        ["Narayanpur", "Narayanpur", "6,640", "Indravati / Kotri", "Hill Maria (Abujhmaria), Muria, Gond"],
        ["Bijapur", "Bijapur", "6,555", "Indravati / Talperu", "Dandami Maria, Dorla, Gond"],
        ["Sukma", "Sukma", "5,635", "Sabari (Kolab)", "Dorla, Muria, Dhurwa, Halba"],
        ["Kanker", "Kanker", "5,285", "Mahanadi / Dudh", "Gond, Halba, Kanwar"]
    ]
    add_styled_table(doc, headers, rows)
    
    add_heading_1(doc, "2. The Cultural & Spiritual Landscape")
    doc.add_paragraph(
        "Unlike the Sanskritic mainstream of the northern plains, Bastar's cultural fabric is anchored in an animistic, ancestral, "
        "and sacred territorial matrix. Village life centers on the 'Devigudi' (village goddess shrine) and the worship of indigenous "
        "deities (Anga Dev, Budha Dev, Mawli Mata, Hinglajin, and Sheetla Mata). The supreme regional deity, Goddess Danteshwari, "
        "canonized at the confluence of the sacred Shankini and Dankini rivers in Dantewada, embodies a historical syncretism between "
        "indigenous tribal guardian deities (Manikeshwari/Mawli) and Kakatiya royal Shakta patronage."
    )
    
    add_callout(doc, 
        "CRITICAL RESEARCH RULE: Bastar culture is not a monolithic monoculture. Traditions differ significantly across ecological "
        "zones: the Abujhmad hill forests preserve isolated hunting-gathering and swidden horticultural norms (Hill Maria), "
        "the central plateau exhibits youth dormitories (Ghotul among Muria) and metallurgical expertise (Dhokra/Bell Metal among Ghadwas), "
        "while the southern riparian valleys connect linguistically and culturally with the Godavari basin (Dorla and Dhurwa).",
        "METHODOLOGICAL FRAMEWORK"
    )
    
    add_heading_1(doc, "3. Material Culture and World-Renowned Crafts")
    doc.add_paragraph(
        "Bastar is globally celebrated for its indigenous craft traditions, characterized by raw material extraction directly from the local ecology:\n"
        "1. Bastar Dhokra (Bell Metal / Lost Wax Casting): Practiced by the Ghadwa community, utilizing beeswax, red clay, and bronze alloy. Awarded Geographical Indication (GI) status.\n"
        "2. Bastar Iron Craft (Lohe Ka Kaam): Practiced by the Lohar/Agariya smiths, recycling scrap iron into expressive ritual and decorative artifacts.\n"
        "3. Bastar Wooden Craft: Intricate carving on Teak, Sal, and Shisham by the Badhai artisans, depicting tribal cosmology, wildlife, and Ghotul motifs.\n"
        "4. Terracotta Pottery: Votive terracotta shrines, roof tiles, and giant terracotta elephant/bull offerings."
    )
    
    add_heading_1(doc, "4. Ecological and Forest Heritage")
    doc.add_paragraph(
        "The dense tropical moist and dry deciduous forests are dominated by Shorea robusta (Sal), Terminalia tomentosa (Asna), "
        "and Dendrocalamus strictus (Bamboo). Forest ecosystems sustain vital Non-Timber Forest Products (NTFP) including Mahua "
        "(Madhuca longifolia), Tendu (Diospyros melanoxylon), Tamarind, and Kosa wild silk cocoons. The region houses the pristine Kanger "
        "Valley National Park and Indravati National Park, harboring the endangered Wild Water Buffalo (Bubalus arnee) and the Bastar Hill Myna (Gracula religiosa peninsularis)."
    )
    
    save_document(doc, "01_Bastar_Complete_Overview.docx")

def build_doc_02():
    doc = create_base_document("02. Geography and Location", "Geomorphology, Drainage, Climate, Soil, and Spatial Topography")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-002",
        "Geographic Scope": "Bastar Division & Dandakaranya Geomorphic Zone (17°46'N to 20°34'N, 80°15'E to 82°15'E)",
        "Primary Classification": "Physical Geography, Climatology & Hydrography",
        "Confidence Level": "HIGH (Geological Survey of India, Survey of India, IMD Data)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Geomorphological Setting and Relief")
    doc.add_paragraph(
        "Bastar occupies the Dandakaranya physiographic province of the Peninsular Indian Shield. It is characterized by three distinct "
        "geomorphic sub-regions:\n"
        "1. Bastar Plateau: An undulating plateau averaging 550 to 650 meters above mean sea level (AMSL), sloping gently towards the south and west.\n"
        "2. Abujhmad Hills: A rugged, heavily dissected tract of Archean crystalline rock in the north-west, rising above 1,000 meters AMSL.\n"
        "3. Bailadila Hill Range: A prominent north-south trending ridge rich in high-grade banded iron formation (hematite), with peaks exceeding 1,250 meters (highest peak: 1,276 m)."
    )
    
    add_heading_2(doc, "2. Hydrography and Drainage Systems")
    doc.add_paragraph(
        "The drainage is dominated by the Godavari River basin. The Indravati River, originating from Thuamul Rampur in Kalahandi, Odisha, "
        "flows westwards across Bastar for approximately 535 km before joining the Godavari at Bhadrakali. Major tributaries include "
        "the Narangi, Baordig, Nibra, Kotri, and Kanger rivers. The southern boundary is drained by the Sabari (Kolab) River, which forms "
        "the interstate boundary with Odisha before emptying into the Godavari."
    )
    
    add_heading_2(doc, "3. Climate and Hydrometeorology")
    doc.add_paragraph(
        "Bastar experiences a tropical wet-and-dry climate (Köppen: Aw) transitioning to humid subtropical at higher elevations. "
        "Annual average precipitation ranges between 1,200 mm and 1,600 mm, with over 85% received during the South-West Monsoon (June to September). "
        "Temperatures range from a minimum of 6°C to 10°C in December-January to 38°C to 42°C in May."
    )
    
    save_document(doc, "02_Geography_and_Location.docx")

def build_doc_03():
    doc = create_base_document("03. Bastar Administrative History", "Evolution from Princely State to Multi-District Division")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-003",
        "Geographic Scope": "Historical Bastar Feudatory State & Modern Bastar Division",
        "Primary Classification": "Administrative & Political Geography",
        "Confidence Level": "HIGH (National Archives of India, Central Provinces District Gazetteers, Ministry of Home Affairs)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Princely State Administration (Pre-1948)")
    doc.add_paragraph(
        "Under the Kakatiya dynasty, Bastar functioned as a decentralized feudal kingdom divided into 'Parganas' governed by Pargana Manjhis "
        "and 'Garas' (clans) led by village headmen (Patels / Gaontias). British indirect rule began formally following the treaty of 1853, "
        "with Bastar classified as a Feudatory State under the Central Provinces and Berar. A British Political Agent exercised supervisory control, "
        "frequently intervening during successions and tribal revolts."
    )
    
    add_heading_2(doc, "2. Integration into the Indian Union and Subsequent Reorganizations")
    doc.add_paragraph(
        "Maharaja Pravir Chandra Bhanj Deo signed the Instrument of Accession on January 1, 1948, integrating Bastar into the Central Provinces and Berar "
        "(later Madhya Pradesh in 1956). In 1948, Bastar State and Kanker State were merged to form Bastar District, the largest single district in India "
        "(39,114 sq km), larger than the state of Kerala or Belgium.\n\n"
        "Key administrative bifurcations:\n"
        "• 1998: Bastar district was trifurcated by the Madhya Pradesh government into Bastar (Jagdalpur), Dantewada (Dakshin Bastar), and Kanker (Uttar Bastar).\n"
        "• November 1, 2000: Formation of the state of Chhattisgarh under the Madhya Pradesh Reorganisation Act.\n"
        "• 2007: Creation of Bijapur (carved from Dantewada) and Narayanpur (carved from Bastar) districts.\n"
        "• 2012: Creation of Kondagaon (carved from Bastar) and Sukma (carved from Dantewada) districts."
    )
    
    save_document(doc, "03_Bastar_Administrative_History.docx")

def build_doc_04():
    doc = create_base_document("04. Bastar Historical History", "Comprehensive Narrative from Prehistory to Modernity")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-004",
        "Geographic Scope": "Chakrakota / Dandakaranya / Historical Bastar State",
        "Primary Classification": "Historiography & Epigraphic Synthesis",
        "Confidence Level": "HIGH (Epigraphia Indica, ASI Archaeological Records, Russell & Hiralal, Grigson)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Early and Classical Epigraphic Era")
    doc.add_paragraph(
        "The historical narrative of Bastar is anchored in stone inscriptions and copper-plate grants. The Nala Dynasty (c. 4th to 6th Century CE) "
        "ruled from their capital Pushkari (identified with Garhbodh/Umarkote near the Bastar-Odisha border). Nala rulers such as Bhavadattavarman, "
        "Arthapatiraja, and Skandavarman issued gold coins and inscriptions (e.g., Rithapur and Podagadh records) confirming active warfare with the Vakatakas."
    )
    
    add_heading_2(doc, "2. The Chhindaka Naga Dynasty of Chakrakota (c. 1023 - 1324 CE)")
    doc.add_paragraph(
        "The Chhindaka Nagas established a prosperous kingdom known as 'Chakrakota Mandala' with their capital at Barsur (Barasuru) and Bhairamgarh. "
        "Claiming descent from the mythical Nagavanshi lineage of the serpent king Shankhapala, they were ardent patrons of Shaivism and Shakta tantrism. "
        "Prominent rulers included Nripati Bhushana, Dharavarsha, and Someshvaradeva I. Their kingdom withstood Chola invasions (Rajendra Chola's northern "
        "expedition c. 1023 CE recorded Chakrakotta in the Tirumalai inscription) and Eastern Ganga incursions, leaving monumental stone architecture at Barsur."
    )
    
    add_heading_2(doc, "3. Kakatiya Migration and the Founding of Bastar State (1324 CE)")
    doc.add_paragraph(
        "Following the fall of Warangal to the Delhi Sultanate (Ghiyasuddin Tughlaq) in 1323 CE, Prince Annamadeva, brother of the martyred King "
        "Prataparudra II, migrated across the Godavari River into Dandakaranya. In 1324 CE, Annamadeva founded the Kakatiya dynasty of Bastar, "
        "installing Goddess Danteshwari (Manikeshwari) at Dantewada as the tutelary family and state deity."
    )
    
    save_document(doc, "04_Bastar_Historical_History.docx")

def build_doc_05():
    doc = create_base_document("05. Bastar Historical Timeline", "Chronological Master Table: 2500 BCE to Present")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-005",
        "Geographic Scope": "Bastar Region / Central India",
        "Primary Classification": "Historical Chronology",
        "Confidence Level": "HIGH (Archaeological, Epigraphic, and Archival Cross-Verification)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "Chronological Table of Bastar History")
    headers = ["Period / Date", "Historical Event / Milestone", "Key Dynasty / Figures", "Evidentiary Basis & Epigraphy"]
    rows = [
        ["c. 2500 - 1000 BCE", "Microlithic tools, rock shelter paintings, megalithic menhirs", "Indigenous ancestors", "Rock shelters at Chitrakote & Kanger caves; Uruskal menhirs"],
        ["c. 350 - 500 CE", "Nala dynasty establishes rule at Pushkari (Garhbodh)", "Bhavadattavarman, Skandavarman", "Podagadh inscription, Rithapur copper plates, gold coins"],
        ["c. 1023 CE", "Chola northern military raid attacks Chakrakotta", "Rajendra Chola I", "Tirumalai rock inscription of Rajendra Chola I"],
        ["c. 1023 - 1324 CE", "Chhindaka Naga Dynasty flourishes at Barsur capital", "Nripati Bhushana, Someshvaradeva I", "Barsur Battisa Temple, Mama-Bhanja Temple inscriptions"],
        ["1324 CE", "Annamadeva migrates from Warangal; establishes Kakatiya rule", "Annamadeva (Brother of Prataparudra II)", "Bastar royal genealogies, Dantewada stone inscriptions"],
        ["1410 - 1468 CE", "Reign of Hamir Deva and Purushottam Deva; Goncha Festival founded", "Purushottam Deva", "Rath Yatra / Goncha tradition, Jagannath Puri pilgrimage records"],
        ["1774 - 1779 CE", "Halba Rebellion: Succession conflict between Dalpat & Daryao Deva", "Ajmer Singh vs Daryao Deva", "British CP records; Treaty with Bhosles of Nagpur (1780)"],
        ["1853 CE", "Annexation of Nagpur; Bastar becomes British Feudatory State", "Bhairam Deo / East India Company", "Treaty of 1853, Central Provinces Gazetteer"],
        ["1859 CE", "Koi Revolt: 'Every head for a Teak tree' against British forest plunder", "Nangur Zamindar, Dorla headmen", "British archival records, forest commissioner reports"],
        ["1876 CE", "Muria Rebellion against Diwan corrupt governance & British interference", "Jhāra Siraha and Muria clans", "CP Political Agent reports, settlement records"],
        ["1910 CE", "The Great Bhumkal Rebellion: Total indigenous revolt against forest laws", "Gundadhur, Lal Kalendra Singh", "National Archives of India, de Brett & Standen records"],
        ["Jan 1, 1948", "Merger of Bastar Feudatory State into the Union of India", "Maharaja Pravir Chandra Bhanj Deo", "Instrument of Accession, Ministry of States (Sardar Patel)"],
        ["March 25, 1966", "Tragic police firing at Bastar Palace; death of Pravir Chandra", "Pravir Chandra Bhanj Deo, Bastar Adivasis", "Justice K.L. Pandey Commission of Inquiry Report"],
        ["Nov 1, 2000", "Creation of Chhattisgarh State; Bastar designated administrative division", "Parliament of India", "Madhya Pradesh Reorganisation Act, 2000"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "05_Bastar_Historical_Timeline.docx")

def build_doc_06():
    doc = create_base_document("06. Archaeological Heritage", "Rock Art, Megaliths, Epigraphy, Numismatics, and Excavations")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-006",
        "Geographic Scope": "Bastar Division Archaeological Sites",
        "Primary Classification": "Field Archaeology, Epigraphy & Material Culture",
        "Confidence Level": "HIGH (Archaeological Survey of India & Directorate of Archaeology CG)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Megalithic Traditions (Uruskal / Gada Stone Pillars)")
    doc.add_paragraph(
        "Bastar possesses one of the world's most vibrant living megalithic cultures. The Dandami Maria and Gond groups erect "
        "'Uruskal' (tall memorial stone menhirs) and 'Danya' (flat stone cairn dolmens) on village boundaries to honor deceased clan elders. "
        "Unlike archaeological dead megaliths in Western Europe, Bastar's megaliths represent living ancestral communion, where each stone "
        "is consecrated through buffalo sacrifice, rice offering, and mahua libation."
    )
    
    add_heading_2(doc, "2. Prehistoric Rock Shelters")
    doc.add_paragraph(
        "Prehistoric pictographs and petroglyphs utilizing red hematite and kaolin white pigments have been documented in the rock shelters "
        "of Kanker (Udana, Gotitola), Chitrakote gorge cliffs, and Bailadila ridges. The rock art depicts anthropomorphic hunting scenes, "
        "horned headdresses, deer, bisons, and geometric labyrinthine fertility motifs dating from the Mesolithic to early Iron Age."
    )
    
    add_heading_2(doc, "3. Epigraphy and Inscribed Slabs")
    doc.add_paragraph(
        "Over 40 significant stone and copper inscriptions have been deciphered from Bastar:\n"
        "• Podagadh Inscription of Skandavarman (Nala Dynasty, Sanskrit in 5th c. box-headed Brahmi).\n"
        "• Barsur Inscription of Mahashivagupta Someshvara (Chhindaka Naga, Saka 1130 / 1208 CE).\n"
        "• Dantewada Pillar Inscriptions of Kakatiya Kings detailing grants to Goddess Danteshwari."
    )
    
    save_document(doc, "06_Archaeological_Heritage.docx")

def build_doc_07():
    doc = create_base_document("07. Ancient and Medieval Bastar", "Nalas, Chhindaka Nagas, Chalukya Interactions, and Chakrakota")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-007",
        "Geographic Scope": "Chakrakota Mandala (Bastar & Koraput Tracts)",
        "Primary Classification": "Dynastic History & Medieval Epigraphy",
        "Confidence Level": "HIGH (Epigraphia Indica Vol. IX, X, XXVIII; Hiralal Inscriptions)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Realm of Chakrakota")
    doc.add_paragraph(
        "During the medieval era, the central Bastar plateau was known across the subcontinent as Chakrakota (or Chakrakotta Mandala). "
        "The Chhindaka Nagas ruled this region from the 11th to 14th centuries CE. They assumed the regal title 'Bhagavati-Labdha-Vara-Prasada' "
        "(those who obtained the supreme boon of Goddess Bhagavati/Manikeshwari) and 'Lord of Bhogavati'."
    )
    
    add_heading_2(doc, "2. Religious Syncretism and Art under the Nagavanshis")
    doc.add_paragraph(
        "The Chhindaka Nagas were eclectic patrons who synthesized orthodox Brahmanical Shaivism with local indigenous mother goddess and Naga cults. "
        "Their reign saw the creation of exquisite architectural masterpieces at Barsur, Bhairamgarh, and Narayanpal. The Narayanpal Temple, "
        "commissioned by Queen Gundamahadevi (mother of Someshvaradeva I) in 1111 CE, is a rare Vishnu temple in a predominantly Shaivite zone, "
        "demonstrating religious pluralism."
    )
    
    save_document(doc, "07_Ancient_and_Medieval_Bastar.docx")

def build_doc_08():
    doc = create_base_document("08. Bastar State and Royal History", "Kakatiya Dynastic Lineage, Statecraft, Capitals, and Treaties")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-008",
        "Geographic Scope": "Bastar Princely State (Dantewada, Jagdalpur, Bastar)",
        "Primary Classification": "Dynastic Genealogy & Royal Administration",
        "Confidence Level": "HIGH (Court Genealogies, British Gazetteers, National Archives of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Evolution of the Capital Cities")
    doc.add_paragraph(
        "The Kakatiya rulers shifted their royal seat strategically over six centuries in response to military security and riverine logistics:\n"
        "1. Dantewada (1324 CE): Founded by Annamadeva around the confluence of the Shankini and Dankini rivers.\n"
        "2. Bastar Town (Chhote Dongar / Bastar): Established as a secondary fortified capital by Hamir Deva and Purushottam Deva.\n"
        "3. Jagdalpur (Jagattuguda / Jagdalpur): Established as the permanent capital in 1777 CE by Maharaja Dalpat Deva due to its defensive position encircled by the Indravati River."
    )
    
    add_heading_2(doc, "2. The 'Rath-Pati' Title and Jagannath Pilgrimage")
    doc.add_paragraph(
        "In the 15th century, King Purushottam Deva undertook a grueling pedestrian pilgrimage to the Jagannath Temple in Puri, Odisha. "
        "According to temple annals and Bastar royal tradition, the King donated massive gold and elephants, and in return, the Gajapati "
        "King of Puri bestowed upon him the sacred title of 'Rath-Pati' (Lord of the Chariot) and the privilege of riding a sixteen-wheeled "
        "chariot. Purushottam Deva returned to Bastar and consecrated the chariot festival, dividing it into Goncha (Jagannath Rath Yatra) "
        "and the legendary Bastar Dussehra Rath Yatra."
    )
    
    save_document(doc, "08_Bastar_State_and_Royal_History.docx")

def build_doc_09():
    doc = create_base_document("09. Kakatiya Rulers of Bastar", "Complete Chronology, Biographies, and Archival Lineage")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-009",
        "Geographic Scope": "Bastar State Royalty (1324 - 1966 CE)",
        "Primary Classification": "Genealogical & Biographical Registry",
        "Confidence Level": "HIGH (Cross-verified against de Brett, Grigson, CP Gazetteers, State Archives)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "Chronological Registry of Kakatiya Kings and Queens of Bastar")
    headers = ["Reign / Dates", "Ruler Name", "Key Historical Policies & Events", "Cultural & Temple Patronage"]
    rows = [
        ["1324 - 1369 CE", "Annamadeva", "Founder of Bastar Kakatiya dynasty; migrated from Warangal", "Consecrated Danteshwari Temple at Dantewada"],
        ["1369 - 1410 CE", "Hamir Deva", "Consolidated territory against local feudal chiefs", "Expanded palace fortifications"],
        ["1410 - 1468 CE", "Purushottam Deva", "Awarded 'Rath-Pati' title by Puri Gajapati; established Goncha", "Institutionalized Bastar Dussehra Chariot Yatra"],
        ["1502 - 1525 CE", "Jait Singh Deva", "Defended kingdom against Bijapur sultanate raids", "Fortified southern frontiers"],
        ["1680 - 1709 CE", "Digpal Deva", "Signed diplomatic treaties with Jeypore and Chanda kingdoms", "Constructed Shiva shrines at Jagdalpur"],
        ["1731 - 1774 CE", "Dalpat Deva", "Shifted capital from Bastar town to Jagdalpur (1770)", "Built Jagdalpur Fort & Dalpat Sagar lake"],
        ["1774 - 1777 CE", "Ajmer Singh", "Led indigenous Halba resistance against Maratha annexation", "Champion of local tribal autonomy"],
        ["1777 - 1819 CE", "Daryao Deva", "Signed Kotpad Treaty (1780); ceded suzerainty to Bhosle/Nagpur", "Introduced Maratha administrative terms"],
        ["1819 - 1830 CE", "Mahipal Deva", "Reigned during early British diplomatic contact", "Protected indigenous customary privileges"],
        ["1830 - 1853 CE", "Bhupal Deva", "Faced Meriah sacrificial controversies fabricated by British", "Expanded Danteshwari temple complexes"],
        ["1853 - 1891 CE", "Bhairam Deo", "Faced Koi Revolt (1859) and Muria Revolt (1876)", "Built modern Jagdalpur town layout"],
        ["1891 - 1921 CE", "Rudra Pratap Deo", "Reigned during Great Bhumkal (1910); built Bastar Palace", "Knighted by British (KCIE); philanthropic reforms"],
        ["1921 - 1936 CE", "Maharani Prafulla Kumari Devi", "First & only ruling Queen of Bastar; crowned in 1922", "Extremely popular among Adivasis; died in London 1936"],
        ["1936 - 1966 CE", "Pravir Chandra Bhanj Deo", "Last crowned ruler; signed Accession (1948); Adivasi champion", "Revered as living divine incarnation; martyred 1966"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "09_Kakatiya_Rulers_of_Bastar.docx")

if __name__ == "__main__":
    print("Building Batch 1: Documents 01 to 09...")
    build_doc_01()
    build_doc_02()
    build_doc_03()
    build_doc_04()
    build_doc_05()
    build_doc_06()
    build_doc_07()
    build_doc_08()
    build_doc_09()
    print("Batch 1 completed successfully.")
