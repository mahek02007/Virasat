"""
gen_group1_overview_geo_history.py - Generates Documents 01, 02, and 03.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_01():
    doc = PuriDocBuilder(
        title="Puri Overview: Basic Identity, Etymology, & Significance",
        doc_number="01",
        category="Foundational Overview"
    )

    doc.add_h1("1. Executive Identity & Administrative Profile")
    doc.add_paragraph("Puri (historically known as Purushottama Kshetra, Shrikshetra, Shankha Kshetra, and Nilachala) is a globally revered coastal city and the administrative headquarters of Puri district in the eastern state of Odisha, India. Nestled along the Bay of Bengal, it is one of the four cardinal pilgrimage sites (Char Dham) established by Adi Shankaracharya in Hinduism, centered around the 12th-century monumental Shree Jagannath Temple.")

    # Metadata Table
    headers = ["Attribute", "Official Data / Details", "Reference / Authority"]
    rows = [
        ["Official Name", "Puri (Odia: ପୁରୀ)", "Govt. of Odisha Gazette [PUR-S003]"],
        ["Historical / Sacred Names", "Purushottama Kshetra, Shrikshetra, Nilachala, Shankha Kshetra, Jagannath Puri", "Skanda Purana & Epigraphia Indica [PUR-S016]"],
        ["State & District", "Odisha (State) | Puri District (Headquarters)", "District Administration [PUR-S004]"],
        ["Geographical Coordinates", "19.8135° N, 85.8312° E", "Survey of India"],
        ["Elevation & Area", "0 to 10 meters above MSL | Municipality Area: ~16.84 km²", "Puri Municipality & Census 2011"],
        ["Population (Urban Core)", "200,564 (2011 Census); Urban Agglomeration est. ~255,000+", "Office of the Registrar General of India [PUR-S004]"],
        ["Primary Languages", "Odia (Official & Primary), Hindi, Bengali, English", "Linguistic Survey of India [PUR-S012]"],
        ["Religious Significance", "Supreme seat of Lord Jagannath; Char Dham pilgrimage", "SJTA & Shankaracharya Peeth [PUR-S002]"],
        ["Ecological / Coastal Status", "Blue Flag Certified Golden Beach; Coastal Regulation Zone (CRZ-I/II)", "Ministry of Environment & Tourism [PUR-S003]"]
    ]
    doc.add_table(headers, rows, [1.5, 3.2, 1.8])

    doc.add_h1("2. Etymology and Sacred Geographical Connotations")
    doc.add_paragraph("The modern toponym 'Puri' is a shortened linguistic derivation of 'Jagannath Puri' (City of Jagannath) or 'Purushottama Puri'. Historically, classical texts and royal charters did not refer to the settlement simply as Puri; it acquired distinct ontological and geopolitical titles:")
    doc.add_bullet("Purushottama Kshetra: Found in the Mahabharata, Matsya Purana, Brahma Purana, and Skanda Purana, designating the sacred territory of the Supreme Being (Purushottama / Vishnu-Krishna).", "1. ")
    doc.add_bullet("Shrikshetra: 'The Sacred Abode of Shree' (Goddess Lakshmi), underscoring the co-equal theological presence of Mahalakshmi in the temple complex.", "2. ")
    doc.add_bullet("Nilachala / Niladri: 'The Blue Mountain', derived from the elevated sandy mound (Nilasaila) upon which the grand sanctum is constructed.", "3. ")
    doc.add_bullet("Shankha Kshetra: The traditional geo-sacred mapping of Puri in the anatomical shape of a conch shell (Shankha), where vital limbs of the shell house protective Shaivite and Shakta guardian deities (Ashta Sambhus and Ashta Chandi) surrounding the central navel (the Jagannath sanctum).", "4. ")

    doc.add_callout(
        title="Distinction Between Puri City, Puri District, and Odisha",
        text="It is a critical ethnographic and historical principle that Puri City represents a unique consecrated urban ecosystem (Kshetra), whereas Puri District encompasses rural agricultural belts, maritime lagoons (Chilika), and craft corridors (Raghurajpur, Pipili). Regional traditions of western or northern Odisha must not be conflated with the localized, hereditary sevayat traditions of Puri.",
        tag="SCHOLARLY DISTINCTION",
        confidence="HIGH"
    )

    doc.add_h1("3. Multi-Tier Standard Introductions")
    doc.add_h2("One-Line Description")
    doc.add_paragraph("Puri is Odisha's sacred coastal Char Dham city, globally renowned for the 12th-century Jagannath Temple, the world's largest chariot festival (Rath Yatra), and an ancient syncretic heritage integrating Vedic, tribal, Shakta, and Vaishnava cultures.")

    doc.add_h2("100-Word Summary")
    doc.add_paragraph("Puri, situated along the Bay of Bengal in eastern Odisha, is one of Hinduism's most sacred Char Dham pilgrimage centers. Revered as Purushottama Kshetra and Shankha Kshetra, the city centers upon the monumental 12th-century Shree Jagannath Temple. Known worldwide for the annual Rath Yatra (Chariot Festival), the sacred Mahaprasad culinary tradition, and the Govardhan Math established by Adi Shankaracharya, Puri represents an extraordinary living continuum of spiritual traditions, classical Odissi arts, heritage craft settlements like Raghurajpur, and pristine coastal landscapes.")

    doc.add_h2("500-Word Master Synthesis")
    doc.add_paragraph("Puri stands as the cultural, spiritual, and artistic heartbeat of Odisha. Emerging into historical prominence under the Eastern Ganga dynasty in the 12th century, the city was conceived not merely as an administrative enclave, but as a consecrated cosmic geography—the Shankha Kshetra. At its spiritual vortex is the Shree Jagannath Temple, an architectural triumph of the Kalinga style rising 65 meters, housing Lord Jagannath, Lord Balabhadra, Devi Subhadra, and Sudarshana Chakra.\n\nWhat renders Puri unique in the history of world religions is the syncretic nature of its deity. Lord Jagannath is neither exclusively Vedic nor sectarian; his wooden icon (Daru Brahma), large unblinking eyes, and distinctive iconography reflect an archaic fusion of indigenous tribal (Sabara) cosmology, Tantric Shakta practices, Shaivism, and profound Gaudiya and Ramanandi Vaishnavism. The temple's hereditary servitors (sevayats)—numbering 36 principal functional divisions (Chhatisa Nijoga)—include both Vedic Brahmins and the non-Brahmin Daitapatis of tribal lineage who attend intimately to the deities during periods of illness (Anavasara) and divine renewal (Nabakalebara).\n\nBeyond the sacred precincts of the Bada Danda (Grand Road), Puri is the epicenter of Eastern India's classical performing arts and handicrafts. It gave birth to the Mahari and Gotipua traditions—the direct progenitors of classical Odissi dance, revived in the 20th century by legends like Guru Kelucharan Mohapatra. Nearby heritage villages like Raghurajpur preserve Pattachitra cloth scroll painting and Tala Pattachitra (palm-leaf engraving), recognized with Geographical Indication (GI) status.\n\nAs a modern tourism destination, Puri integrates sacred pilgrimage with coastal leisure, featuring the Blue Flag-certified Golden Beach, historic mathas (monastic orders) representing India's leading philosophical lineages, and the proximity to Chilika Lake. It remains a living cultural landscape where ancient ritual protocols continue unbroken in the 21st century.")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S004"),
        get_source("PUR-S008"),
        get_source("PUR-S016")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "01_Puri_Overview.docx"))

def generate_doc_02():
    doc = PuriDocBuilder(
        title="Geography, Coastal Ecology, & Environmental Heritage of Puri",
        doc_number="02",
        category="Geography & Environment"
    )

    doc.add_h1("1. Regional Geography & Coastal Morphology")
    doc.add_paragraph("Puri district occupies a total geographic expanse of 3,479 km² in the coastal plains of eastern Odisha. It is bounded by the Bay of Bengal along a dynamic coastline extending over 150 km, bordered by Khordha district to the north, Jagatsinghpur to the northeast, and Ganjam to the southwest across the Chilika lagoon.")

    headers = ["Geographical Feature", "Physical Dimensions / Extent", "Ecological & Cultural Interconnection"]
    rows = [
        ["Bay of Bengal Coastline", "~150 km total district coastline; Puri urban beach ~7 km", "Center of maritime fishing (Kaibarta/Nolia), beach tourism, and Swargadwar sacred rites."],
        ["Blue Flag Golden Beach", "Certified stretch at Puri Main Beachfront", "International eco-label certification for water quality, environmental management, and safety."],
        ["Daya & Bhargavi Rivers", "Distributaries of the Mahanadi delta system", "Hydrological lifelines supporting paddy cultivation and sacred tanks (Narendra, Indradyumna)."],
        ["Chilika Lake Lagoon", "1,165 km² (monsoon max); SW boundary of Puri district", "Asia's largest brackish lagoon, Ramsar site #229, home to Irrawaddy dolphins and migratory waterfowl."],
        ["Balukhand-Konark Sanctuary", "71.72 km² coastal strip along Puri-Konark Marine Drive", "Casuarina and cashew plantations stabilizing coastal sand dunes; habitat for Spotted Deer (Axis axis)."]
    ]
    doc.add_table(headers, rows, [1.5, 2.2, 2.8])

    doc.add_h1("2. Climate, Monsoonal Regimes, and Cyclone Vulnerability")
    doc.add_paragraph("Puri experiences a tropical maritime climate characterized by high humidity (often exceeding 80-85% in monsoon months), moderate winters (16°C to 28°C), and hot, humid summers (27°C to 38°C). Annual rainfall averages between 1,400 mm and 1,550 mm, with 75% delivered by the Southwest Monsoon between late June and October.")

    doc.add_callout(
        title="Vulnerability to Severe Tropical Cyclones",
        text="Situated along the north-western arc of the Bay of Bengal, Puri is historically vulnerable to high-intensity cyclones. Significant catastrophic events include the 1999 Super Cyclone (05B), Cyclone Phailin (2013), and Cyclone Fani (May 2019), which made landfall directly near Puri with wind speeds reaching 215 km/h. These events cause substantial damage to traditional thatched architecture, coastal vegetation, and heritage matha structures, necessitating robust disaster resilience protocols by the ASI and state administration.",
        tag="ENVIRONMENTAL HAZARD",
        confidence="HIGH"
    )

    doc.add_h1("3. Sacred Hydrology: The Sacred Tanks (Pancha Tirtha)")
    doc.add_paragraph("Puri's urban form is structured around an ancient wetland and hydrological network that serves both utilitarian water management and ritual purification functions. Five water bodies constitute the 'Pancha Tirtha', where pilgrims are mandated to perform ablutions:")
    doc.add_bullet("Narendra Tank (Narendra Pokhari): Spanning over 14 acres with a central island temple (Chandan Mandapa), this tank hosts the 42-day Chandan Yatra water festival where the representative deities (Madanmohana) enjoy divine boat cruises (Chapa Khela).", "1. ")
    doc.add_bullet("Markandeshwar Tank: Adjacent to the 12th-century Markandeshwar Shiva temple, linked in puranic lore to Sage Markandeya's penance.", "2. ")
    doc.add_bullet("Indradyumna Tank: Associated with King Indradyumna's Ashwamedha sacrifice; fed by natural aquifers and renowned for freshwater turtles.", "3. ")
    doc.add_bullet("Swargadwar Sea Bathing (Mahodadhi Tirtha): The Bay of Bengal itself at Swargadwar, where the ocean is revered as Mahodadhi, a sacred personification of divine purification.", "4. ")
    doc.add_bullet("Rohini Kunda: Located within the inner precinct of the Jagannath Temple, containing sacred water sanctified by the presence of the mythical Crow (Kaka Bhusundi).", "5. ")

    doc.add_h1("4. Interconnection: Geography, Occupation, and Food Systems")
    doc.add_paragraph("The physical geography of Puri directly dictates its cultural and economic patterns:")
    doc.add_bullet("Alluvial Plains & Sacred Agriculture: The fertile delta soils of the Bhargavi and Daya rivers produce indigenous short-grain aromatic rice varieties (such as Kalajeera and Padmakeshari) reserved exclusively for Mahaprasad temple preparations.", "• ")
    doc.add_bullet("Maritime Resources: The littoral ecosystem sustains traditional artisanal fishing communities (Kaibartas and Telugu-speaking Nolia migrants) operating catamarans and motorized dinghies.", "• ")
    doc.add_bullet("Saline Agro-Ecosystems: Coastal coconut and betel-leaf (Paan) groves in Puri district form a major agricultural export commodity, with Puri Paan holding high commercial and ritual reverence.", "• ")

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S004"),
        get_source("PUR-S005"),
        get_source("PUR-S006")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "02_Geography_and_Environment.docx"))

def generate_doc_03():
    doc = PuriDocBuilder(
        title="Comprehensive History of Puri: From Antiquity to Modern Era",
        doc_number="03",
        category="Historical Chronology"
    )

    doc.add_h1("1. Ancient Foundations & Early Epigraphic Traces")
    doc.add_paragraph("The historical origins of Puri as a sacred center are deeply intertwined with the ancient geo-political entities of Kalinga, Odra, and Utkala. While puranic narratives (Brahma Purana, Skanda Purana) attribute its founding to the legendary King Indradyumna of the Solar Dynasty, epigraphic and archaeological records trace human occupation and localized tribal tree-worship back to the pre-Mauryan and early historic periods.")

    doc.add_callout(
        title="Early Historic Epigraphy & the Kurmeswar / Bhauma Inscriptions",
        text="The earliest verifiable epigraphic allusions to Purushottama at Puri appear during the 7th–8th century CE under the Shailodbhava and early Bhauma-Kara dynasties. Epigraphist D.C. Sircar and historian K.C. Panigrahi note that before the present stone temple, an earlier shrine existed, documented in the 8th-century Anargharaghava of Murari and confirmed by the Ganjam plates.",
        tag="HISTORICAL EVIDENCE",
        confidence="HIGH"
    )

    doc.add_h1("2. Dynastic Chronology of Puri and the Jagannath Complex")
    headers = ["Historical Era / Dynasty", "Chronological Period", "Key Rulers & Major Historical Developments"]
    rows = [
        ["Early Kingdoms & Somavamsis", "c. 7th – 11th Century CE", "Yayati I (Yayati Kesari) according to Madala Panji traditions rebuilt the early shrine and consecrated the deities after recovering them from Sonepur."],
        ["Eastern Ganga Dynasty", "1078 – 1434 CE", "Anantavarman Chodaganga Deva (r. 1077–1147) commissioned the colossal 65m high Jagannath Deula. Completed under Anangabhima Deva III (r. 1211–1238), who consecrated the empire to Jagannath (Purushottama-Samrajya)."],
        ["Suryavamsi Gajapati Dynasty", "1434 – 1541 CE", "Kapilendra Deva, Purushottama Deva, and Prataparudra Deva. The concept of 'Gajapati as the Royal Servitor (Rauta / First Sevaka)' solidified. Grand road expansions and Natamandapa/Bhoga Mandapa additions."],
        ["Bhakti & Chaitanya Era", "1510 – 1533 CE", "Shri Chaitanya Mahaprabhu resided in Puri for 24 years at Gambhira, transforming Gaudiya Vaishnavism and popularizing ecstatic devotional singing (Kirtan)."],
        ["Sultanate & Mughal Era", "1568 – 1751 CE", "Kalapahar invasion (1568); deities secretly relocated to Chilika islands (Gurubai, Marada) multiple times to evade desecration. Ramachandra Deva I of Khurda re-consecrated the deities (Dutiya Indradyumna)."],
        ["Maratha Administration", "1751 – 1803 CE", "Marathas established rigorous administrative endowments, built mathas, repaired temple gates, and regularized pilgrim security across the Jagannath Sadak."],
        ["Colonial British Period", "1803 – 1947 CE", "British East India Company seized Puri in 1803; passed Regulation IV of 1806 (Pilgrim Tax). Transferred direct temple management back to the Raja of Khurda in 1840. Railway line reached Puri in 1900."],
        ["Post-Independence & Modernity", "1947 – Present", "Passage of the Shri Jagannath Temple Act, 1955 (SJTA established). Conservation overseen by ASI; transformation into global cultural and beach tourism center."]
    ]
    doc.add_table(headers, rows, [1.4, 1.2, 3.9])

    doc.add_h1("3. The Concept of Gajapati Rulers as 'Adya Sevaka'")
    doc.add_paragraph("A defining feature of Puri's medieval statecraft was the theological surrender of royal sovereignty to the deity. Initiated by Anangabhima Deva III in the early 13th century, the emperor declared Lord Jagannath as the supreme 'Rastra-devata' (King of the realm), designating himself merely as His regent or deputy (Rauta). This structural ideology was fiercely maintained by the Suryavamsi Gajapatis:")
    doc.add_bullet("Chhera Pahara: During the annual Rath Yatra, the reigning Gajapati King sweeps the floors of the three chariots with a gold-handled broom, demonstrating humility and absolute submission before the divine, regardless of political stature.", "• ")
    doc.add_bullet("Madala Panji Chronicles: The temple's palm-leaf chronicle records royal accessions, temple gifts, invasions, and ritual infractions from medieval times to the present.", "• ")

    doc.add_h1("4. Periods of Crisis: Deity Concealment and Resistance")
    doc.add_paragraph("Between the 16th and 18th centuries, during aggressive incursions by Bengal Sultanate commanders (notably Kalapahar in 1568) and Mughal subahdars (such as Hashim Khan and Taqi Khan), the servitors demonstrated remarkable loyalty. The sacred wooden deities were secretly evacuated and hidden in remote locations across coastal and riverine Odisha:")
    doc.add_bullet("Marada Temple (Ganjam): Known as 'Chhada Deula' where deities were sheltered undisturbed for over 28 months.", "1. ")
    doc.add_bullet("Chilika Islands (Gurubai & Chakanasi): Hidden in secluded brackish inlets.", "2. ")
    doc.add_bullet("Tikali & Mandarani: Remote forest zones where daily nitis were maintained in secret.", "3. ")

    doc.add_sources_section([
        get_source("PUR-S008"),
        get_source("PUR-S009"),
        get_source("PUR-S015"),
        get_source("PUR-S016"),
        get_source("PUR-S017"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "03_History.docx"))

if __name__ == "__main__":
    generate_doc_01()
    generate_doc_02()
    generate_doc_03()
    print("Group 1 completed successfully.")
