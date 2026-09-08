"""
gen_group2_religion_jagannath.py - Generates Documents 04, 05, 06, and 09.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_04():
    doc = PuriDocBuilder(
        title="Religious & Spiritual Heritage of Puri: The Syncretic Mahapitha",
        doc_number="04",
        category="Religious & Spiritual Heritage"
    )

    doc.add_h1("1. The Char Dham Paradigm & Sacred Geography")
    doc.add_paragraph("In classical Sanatana Dharma cosmology, Puri occupies a preeminent position as the Eastern cardinal quadrant of the all-India Char Dham circuit (alongside Badrinath in the North, Rameswaram in the South, and Dwarka in the West). Adi Shankaracharya in the 8th–9th century CE consecrated this spatial geometry by establishing the Govardhan Math at Puri, assigning it custody over the Rigveda and the Mahavakya 'Prajnanam Brahma'.")

    headers = ["Sacred Dimension", "Theological Alignment", "Ritual / Institutional Manifestation"]
    rows = [
        ["Char Dham Eastern Gate", "Bhogakshetra (Abode of Divine Dining)", "Tradition holds Vishnu bathes at Rameswaram, meditates at Badrinath, rules at Dwarka, and eats at Puri (Mahaprasad)."],
        ["Shakta Peetha Tradition", "Vimala Temple (Ugra Tara / Bhairavi)", "Recognized in Tantric texts as an Uddiyana/Utkala Shakta Peetha; offerings become Mahaprasad only after consecration to Goddess Vimala."],
        ["Shaivite Guardianship", "Ashta Sambhu (Eight Shiva Temples)", "Lokanath, Markandeshwar, Jameswar, Kapalmochan, Nilakantha, Yameshwar, Beleswar, and Isaneswar encircle the Kshetra."],
        ["Vaishnava Synthesis", "Pancha Shakha & Gaudiya lineages", "Integration of Ramanuja's Sri Sampradaya (Emara Matha), Madhva, Nimbarka, Vallabha, and Chaitanya's Gaudiya ecstatic kirtan."]
    ]
    doc.add_table(headers, rows, [1.5, 2.0, 3.0])

    doc.add_h1("2. Syncretic Integration: Vedic, Tribal, Shakta, and Buddhist Strands")
    doc.add_paragraph("Puri's religious fabric is defined by profound syncretism, reconciling divergent philosophical traditions into a harmonious whole:")
    doc.add_bullet("Sabara Tribal Heritage: The non-Brahmin Daitapati servitors, claiming descent from the Sabara chieftain Viswavasu, perform intimate body rituals (Angaraga), secret medicinal convalescence (Anavasara), and the burial and reconstitution of the divine bodies during Nabakalebara.", "• ")
    doc.add_bullet("Tantric-Shakta Substratum: The installation of Yantras beneath the Ratnavedi and the worship of Subhadra as Bhuvaneshwari or Katyayani reflect deep Tantric foundations.", "• ")
    doc.add_bullet("Scholarly Buddhist Hypotheses: 19th and early 20th-century scholars (Rajendralala Mitra, Swami Vivekananda) hypothesized connections between the Triad (Jagannath, Balabhadra, Subhadra) and the Buddhist Triratna (Buddha, Dharma, Sangha), though modern epigraphy interprets Jagannath firmly within archaic tribal-Vaishnava syncretism.", "• ")

    doc.add_callout(
        title="Theology of Non-Sectarian Divine Accessibility",
        text="Unlike strict sectarian orthodoxies, Jagannath is conceived as 'Patitapabana' (The Redeemer of the Fallen). On the Ratnavedi he is inaccessible to outcastes and non-Hindus, but during Rath Yatra he steps out onto the Grand Road, making himself accessible to all humanity regardless of caste, creed, or nationality.",
        tag="RELIGIOUS PHILOSOPHY",
        confidence="HIGH"
    )

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S010"),
        get_source("PUR-S018")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "04_Religious_and_Spiritual_Heritage.docx"))

def generate_doc_05():
    doc = PuriDocBuilder(
        title="Jagannath Culture: Theology, Iconography, Rituals, & Nabakalebara",
        doc_number="05",
        category="Jagannath Culture (Deep Dive)"
    )

    doc.add_h1("1. The Chaturdha Murti (The Four-Fold Deities)")
    doc.add_paragraph("On the elevated stone platform known as the Ratnavedi (Jeweled Altar) inside the inner sanctum (Garbhagriha), reside four wooden deities (Chaturdha Murti):")

    headers = ["Deity", "Iconographic Form & Color", "Cosmic & Theological Symbolism", "Sacred Tree (Daru)"]
    rows = [
        ["Lord Jagannath", "Dark Black (Shyama); large round circular eyes; outstretched armless stumps", "Supreme Soul (Paramatman / Purushottama / Krishna); represents void (Sunya) and infinite consciousness", "Neem (Azadirachta indica) bearing Shankha, Chakra, Gada, Padma marks"],
        ["Lord Balabhadra", "Pure White (Gaura); oval eyes; arms at right angles; hood of Ananta Sesha", "Elder Brother; Balarama / Sankarshana; embodiment of cosmic strength and knowledge (Jnana)", "Neem tree with plough (Hala) and pestle (Musala) natural bark formations"],
        ["Devi Subhadra", "Golden Yellow (Pita); oval eyes; no hands or feet; graceful columnar torso", "Sister; Yogamaya / Ekanamsha / Durga-Bhuvaneshwari; embodiment of cosmic energy (Shakti)", "Neem tree exhibiting lotus or five-petaled floral bark signatures"],
        ["Sudarshana Chakra", "Wooden cylindrical pillar; carved geometric yantric patterns", "Cosmic Wheel of Time; absolute weapon of Vishnu; Shaivite-Shakta kinetic energy", "Neem tree devoid of branches, straight and pristine"]
    ]
    doc.add_table(headers, rows, [1.2, 1.8, 2.3, 1.2])

    doc.add_h1("2. Origin Hypotheses: Tribal, Vedic, & Anthropological Debates")
    doc.add_paragraph("Scholarly investigations into the origin of Jagannath have generated major historiographical frameworks:")
    doc.add_bullet("Tribal (Sabara) Origin Theory: Championed by Dr. Benimadhab Padhi and Prof. Anncharlott Eschmann, emphasizing the uncarved wooden log (Daru Brahma), the wooden icon replacement (Nabakalebara), and the exclusive priestly authority of tribal Daitapatis.", "1. ")
    doc.add_bullet("Vedic-Purushottama Synthesis: Supported by Dr. K.C. Panigrahi, linking the deity to the Purusha Sukta of the Rigveda, where the cosmic Purusha floats across the ocean as an uncarved timber.", "2. ")
    doc.add_bullet("Tantric-Vajrayana Interaction: Indrabhuti's 8th-century text Jnanasiddhi opens with an invocation to Jagannath, demonstrating early Tantric Buddhist integration in coastal Odra/Kalinga.", "3. ")

    doc.add_h1("3. The Sacred Mystery of Nabakalebara (Divine Metempsychosis)")
    doc.add_paragraph("Nabakalebara ('Acquisition of a New Body') is the periodic ritual renewal of the wooden deities, occurring when an intercalary leap month (Adhimasa / Mala Masa) of Ashadha occurs in the Hindu lunisolar calendar (every 8, 12, or 19 years; recent ceremonies occurred in 1977, 1996, and 2015):")

    doc.add_bullet("Banajaga Yatra: The search expedition for the sacred Neem trees led by Daitapatis who travel to the Kakatpur Mangala temple to receive divine directional dreams.", "Phase 1: ")
    doc.add_bullet("Daru Chhedana: Felling the sacred trees with gold, silver, and iron axes with Vedic purification rites.", "Phase 2: ")
    doc.add_bullet("Gupta Niti (Carving): Secret carving of the new forms inside the Koili Baikuntha enclosure by hereditary Maharanas.", "Phase 3: ")
    doc.add_bullet("Brahma Parivartana: The midnight transference of the mysterious life-force (Brahma Padartha) from the old deities to the new by blindfolded senior Daitapatis with hands wrapped in sacred silk.", "Phase 4: ")
    doc.add_bullet("Maha Samadhi (Burial): Sacred burial of the old wooden forms in the subterranean cemetery of Koili Baikuntha, followed by full mourning rituals by the sevayats.", "Phase 5: ")

    doc.add_callout(
        title="The Brahma Padartha Mystery",
        text="The exact physical nature of the Brahma Padartha transferred during Nabakalebara remains an inviolable secret. Devotional lore associates it with the unburned heart of Lord Krishna; anthropological scholars suggest an ancient salagrama sila, metallic relic casket, or sacred Tantric yantra.",
        tag="RELIGIOUS TRADITION & SCHOLARLY ANALYSIS",
        confidence="HIGH"
    )

    doc.add_h1("4. The Sevayat System: Chhatisa Nijoga")
    doc.add_paragraph("The Shree Jagannath Temple features one of the world's most complex hereditary ritual hierarchies, formalized into 36 distinct functional servitor guilds (Chhatisa Nijoga) comprising over 119 specific sub-categories recorded in the statutory Record of Rights (RoR):")
    doc.add_bullet("Palia Pushpalaka & Daitapati: Ritual dressing, garland decoration, and secret convalescence rites.", "• ")
    doc.add_bullet("Suara & Mahasuar: The hereditary guild of master temple chefs responsible for preparing the 56 bhog in the Roshaghara.", "• ")
    doc.add_bullet("Chunara & Garabadu: Servitors responsible for ascending the 65m deula daily to change the Patitapabana flag and handling sacred water vessels.", "• ")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S008"),
        get_source("PUR-S010"),
        get_source("PUR-S016"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "05_Jagannath_Culture.docx"))

def generate_doc_06():
    doc = PuriDocBuilder(
        title="Temples & Religious Sites: Complete Profile of the Jagannath Complex",
        doc_number="06",
        category="Temples & Sacred Monuments"
    )

    doc.add_h1("1. Architectural Anatomy of the Jagannath Temple Complex")
    doc.add_paragraph("The Shree Jagannath Temple complex covers an expansive area of over 10.7 acres, enclosed by two concentric stone boundary walls: the outer Meghnad Pacheri (665 ft x 640 ft, height 20-24 ft) and the inner Kurma Bedha. Constructed from khondalite stone in the mature Kalinga architectural tradition, the main temple comprises four axial contiguous halls:")

    headers = ["Architectural Component", "Structure / Dimensions", "Functional & Ritual Role"]
    rows = [
        ["Vimana (Bada Deula)", "Rekha Deula style; 65 meters (214 ft 8 in) tall; crowned by Nilachakra (eight-metal alloy)", "The inner sanctum (Garbhagriha) housing the Ratnavedi where the Chaturdha Murti are enthroned."],
        ["Jagamohana (Mukhasala)", "Pidha Deula style; pyramidal stepped roof; massive supporting stone pillars", "The assembly hall for devotees witnessing the public darshan and offering arati."],
        ["Natamandapa (Dancing Hall)", "Hypostyle flat-roofed hall added during the Gajapati period (15th c.)", "The hall where Maharis traditionally performed ritual dance and where Garuda Stambha stands."],
        ["Bhoga Mandapa (Offering Hall)", "Ornate pyramidal hall added by Purushottama Deva (15th c.)", "The ceremonial hall for the mass consecration of offerings (Chhatra Bhoga / Mahaprasad)."]
    ]
    doc.add_table(headers, rows, [1.5, 2.0, 3.0])

    doc.add_h1("2. The Four Sacred Gateways (Dwaras)")
    doc.add_paragraph("The outer perimeter is pierced by four cardinal monumental gates flanked by animal guardians:")
    doc.add_bullet("Singhadwara (Lion's Gate - East): The grand main portal facing Bada Danda; fronted by the 16-sided monolithic Aruna Stambha (chlorite sun pillar brought from Konark in the 18th century by the Marathas). Features the 22 sacred steps (Baisi Pahacha).", "1. ")
    doc.add_bullet("Vyaghradwara (Tiger's Gate - West): Associated with ascetics, renunciation, and spiritual aspirants.", "2. ")
    doc.add_bullet("Hastidwara (Elephant's Gate - North): The entry associated with the royal procession of the Gajapatis and Annapurna shrine.", "3. ")
    doc.add_bullet("Ashwadwara (Horse's Gate - South): Associated with warrior traditions and victory over cosmic ignorance.", "4. ")

    doc.add_h1("3. Significant Subsidiary Shrines within Kurma Bedha")
    doc.add_paragraph("Over 120 subsidiary shrines encircle the main sanctum inside the inner Kurma Bedha courtyard:")
    doc.add_bullet("Maa Vimala Temple: 9th-century sanctum; supreme Tantric protector where sanctified food becomes Mahaprasad.", "• ")
    doc.add_bullet("Maa Mahalakshmi Temple: Reconstructed by Chodaganga Deva; oversees the divine kitchen (Roshaghara).", "• ")
    doc.add_bullet("Mukti Mandapa: 16-pillared open-air council hall established by Ramachandra Deva I, housing the assembly of traditional Brahmin scholars arbitrating socio-religious disputations.", "• ")
    doc.add_bullet("Kalpabriksha (Bata Vriksha): Ancient sacred banyan tree believed to fulfill devotee prayers.", "• ")

    doc.add_callout(
        title="Visitor Regulations & Non-Hindu Entry Policy",
        text="Under the statutory Shree Jagannath Temple Act, 1955, and traditional customs established over centuries, entry into the inner temple precincts is strictly reserved for orthodox followers of the Hindu faith. Non-Hindu visitors, international dignitaries, and foreign tourists are accommodated at the Raghunandan Library vantage point overlooking the Lion Gate and can freely participate in the public Rath Yatra on the Grand Road.",
        tag="CURRENT STATUTORY & RITUAL POLICY [TIME-SENSITIVE]",
        confidence="HIGH"
    )

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S002"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S020")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "06_Temples_and_Religious_Sites.docx"))

def generate_doc_09():
    doc = PuriDocBuilder(
        title="Varkari, Gaudiya, & Pan-Indian Devotional Traditions at Puri",
        doc_number="09",
        category="Devotional Traditions & Mathas"
    )

    doc.add_h1("1. Pan-Indian Pilgrimage Confluence at Puri")
    doc.add_paragraph("Puri served as a primary nexus for the pan-Indian Bhakti movement between the 11th and 18th centuries. Saints, philosophers, and spiritual reformers from every major linguistic and sectarian territory traveled to Nilachala to encounter Lord Jagannath:")

    headers = ["Spiritual Master / Movement", "Origin / Sampradaya", "Historical Presence & Structural Legacy in Puri"]
    rows = [
        ["Adi Shankaracharya (8th-9th c.)", "Advaita Vedanta (Kerala)", "Founded Govardhan Math, established rigorous Vedic scholarship and monastic monastic lineages."],
        ["Ramanujacharya (12th c.)", "Vishishtadvaita (Tamil Nadu)", "Visited Puri c. 1122 CE; founded Emar Matha and Vijayanagar-associated mathas; introduced Pancharatra puja reforms."],
        ["Nimbarkacharya & Madhvacharya", "Dvaitadvaita & Dvaita", "Established Radhaballabha Matha and Madhva monastic houses along Grand Road."],
        ["Chaitanya Mahaprabhu (1510-1533)", "Gaudiya Vaishnavism (Bengal)", "Lived 24 years at Gambhira; catalyzed widespread Harinama Sankirtana across Eastern India."],
        ["Guru Nanak Dev (1506 CE)", "Sikhism (Punjab)", "Composed the cosmic arati 'Gagan Mein Thaal' at Puri beach; Bauli Matha commemorates his visit."],
        ["Sant Kabir & Sant Namdev", "Nirguni Bhakti & Varkari Sampradaya", "Kabir Chaura Matha preserves the syncretic legacy; Varkari pilgrims visit Puri during Ashadha Yatra."]
    ]
    doc.add_table(headers, rows, [1.5, 1.8, 3.2])

    doc.add_h1("2. The Bhakta Salabega Tradition: Transcending Social Barriers")
    doc.add_paragraph("One of the most celebrated devotional figures of Puri is Salabega (early 17th century), the son of a Mughal military commander (Lalbeg) and a Brahmin widow. Denied entry to the temple due to his Islamic birth, Salabega composed some of the most poignant Jananas and Bhajans in the Odia language (e.g., 'Ahe Nila Saila'). Devotional tradition records that when Salabega was delayed returning from Vrindavan during Rath Yatra, the grand chariot Nandighosh came to a complete halt at Balagandi until the devotee arrived to offer his heartfelt prayers. His memorial samadhi stands along the Grand Road today.")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S018")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "09_Varkari_and_Other_Devotional_Traditions.docx"))

if __name__ == "__main__":
    generate_doc_04()
    generate_doc_05()
    generate_doc_06()
    generate_doc_09()
    print("Group 2 completed successfully.")
