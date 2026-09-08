"""
gen_group3_festivals.py - Generates Documents 07, 08, and 29.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_07():
    doc = PuriDocBuilder(
        title="Festivals & Ceremonial Calendar of Puri (The Dwadasa Yatras)",
        doc_number="07",
        category="Festivals & Ceremonial Heritage"
    )

    doc.add_h1("1. The Principle of Continuous Divine Festivity (Dwadasa Yatra)")
    doc.add_paragraph("In Puri, the calendar is marked by twelve grand classical festivals (Dwadasa Yatra) along with dozens of seasonal, puranic, and agricultural celebrations that engage every tier of the urban populace and sevayat hierarchy. The cycle aligns strictly with the Odia lunisolar calendar:")

    headers = ["Festival Name (Odia)", "Lunar Month & Tithi", "Ritual Essence & Public Observance"]
    rows = [
        ["Chandan Yatra (ଚନ୍ଦନ ଯାତ୍ରା)", "Akshaya Tritiya (Vaisakha) - 42 Days", "Longest festival; deities cruise on sacred barges at Narendra Pokhari; begins chariot construction."],
        ["Snana Yatra (ସ୍ନାନ ଯାତ୍ରା)", "Jyeshtha Purnima (May-June)", "Deities bathed with 108 pots of herbal water; Gajanana Besha (elephant attire); enters Anavasara seclusion."],
        ["Rath Yatra (ରଥଯାତ୍ରା)", "Ashadha Shukla Dwitiya (June-July)", "Grand chariot procession to Gundicha Temple; 9-day annual journey."],
        ["Bahuda Yatra (ବାହୁଡ଼ା ଯାତ୍ରା)", "Ashadha Shukla Dashami", "Return journey of the chariots; stops at Mausi Maa temple for Poda Pitha offering."],
        ["Suna Besha (ସୁନା ବେଶ)", "Ashadha Shukla Ekadashi", "Deities adorned with over 208 kg of solid gold jewelry while resting on their chariots outside Singhadwara."],
        ["Niladri Bije (ନୀଳାଦ୍ରି ବିଜେ)", "Ashadha Trayodashi", "Return of deities to the Ratnavedi; Lord Jagannath placates Goddess Lakshmi with sweet Rasagola."],
        ["Jhulan Yatra (ଝୁଲଣ ଯାତ୍ରା)", "Shravana Shukla Dashami to Purnima", "Swing festival celebrated in temple and mathas; elaborate floral swing decorations."],
        ["Dola Yatra (ଦୋଳ ଯାତ୍ରା)", "Phalguna Purnima (Holi)", "Procession of representative deities with fagu (red natural powder) and royal palanquins."]
    ]
    doc.add_table(headers, rows, [1.6, 1.8, 3.1])

    doc.add_h1("2. Snana Yatra and the Anavasara Seclusion")
    doc.add_paragraph("On Jyeshtha Purnima, the deities are brought to the elevated Snana Mandapa overlooking the Grand Road. Poured with 108 pitchers of water infused with sandalwood, saffron, and aromatic herbs drawn from the sacred Suna Kua (Golden Well), the deities contract a ritual fever and enter a 15-day total seclusion known as Anavasara:")
    doc.add_bullet("Gupta Niti & Secret Treatment: During Anavasara, the sanctum is sealed. The Daitapatis administer medicinal herbal pastes (Phuluri Tela), pure fruits, and roots.", "• ")
    doc.add_bullet("Anasara Pattachitra: While the deities are secluded, three painted cloth scrolls depicting Ananta Narayana (Jagannath), Ananta Vasudeva (Balabhadra), and Bhubaneswari (Subhadra) are placed in front of the sanctum for devotee darshan.", "• ")
    doc.add_bullet("Alarnath Pilgrimage: Devotees travel 25 km to Brahmagiri to visit Lord Alarnath, where the deity is believed to manifest the living presence of Jagannath during the seclusion period.", "• ")

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S008"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "07_Festivals_and_Ceremonies.docx"))

def generate_doc_08():
    doc = PuriDocBuilder(
        title="Rath Yatra: Comprehensive Architectural, Ritual, & Sociological Research",
        doc_number="08",
        category="Rath Yatra (Maximum Depth)"
    )

    doc.add_h1("1. The Three Sacred Chariots: Architecture & Engineering")
    doc.add_paragraph("The construction of the three massive wooden chariots is an extraordinary architectural tradition revived annually from scratch without blueprints, measuring tapes, or metallic nails. Built using 862 pieces of timber procured from the forests of Dasapalla and Nayagarh, work begins on Akshaya Tritiya by hereditary master craftsmen (Maharanas, Kamaras, and Rupa Karas):")

    headers = ["Feature", "Nandighosh (Jagannath)", "Taladhwaja (Balabhadra)", "Darpadalana (Subhadra)"]
    rows = [
        ["Total Height", "45 feet (13.7 m)", "44 feet (13.4 m)", "43 feet (13.1 m)"],
        ["Number of Wheels", "16 Wheels (diam. ~7 ft)", "14 Wheels (diam. ~6.5 ft)", "12 Wheels (diam. ~6 ft)"],
        ["Canopy Colors", "Red and Yellow Fabric", "Red and Bluish-Green Fabric", "Red and Black Fabric"],
        ["Guardian Deity (Sarathi)", "Daruka", "Matali", "Arjuna"],
        ["Horses (Colors)", "4 White Horses (Sankha, Balahaka, Suweta, Haridashwa)", "4 Black Horses (Tibra, Ghora, Dirghashrama, Swarnanava)", "4 Red Horses (Rochika, Mochika, Jita, Aparajita)"],
        ["Flag / Crest (Dhwaja)", "Trailokyamohana / Garuda", "Unnani / Tala (Palm)", "Nadambika / Padmadhwaja"]
    ]
    doc.add_table(headers, rows, [1.3, 1.7, 1.7, 1.8])

    doc.add_h1("2. Sequential Ritual Choreography")
    doc.add_paragraph("The Rath Yatra unfolds across tightly regulated ritual stages witnessed by over a million pilgrims:")
    doc.add_bullet("Pahandi Bije: The ecstatic, rhythmic procession where the heavy wooden deities, adorned with elaborate floral tiaras (Tahias), are swayed forward onto the chariots by the Daitapatis to the sound of hundreds of clashing Ghanta (cymbals) and Kahali horns.", "Step 1: ")
    doc.add_bullet("Chhera Pahara: The reigning Gajapati Maharaja arrives in a silver palanquin, climbs each chariot, sprinkles aromatic water, and sweeps the platform with a gold-handled broom (Khadika), demonstrating absolute humility before the Lord.", "Step 2: ")
    doc.add_bullet("Ratha Tana (Pulling the Chariots): Lakhs of devotees pull the massive coir ropes (Sankhachuda) along the 2.5 km stretch of Bada Danda to the Gundicha Temple (Yajna Vedi / Janma Janaki).", "Step 3: ")
    doc.add_bullet("Gundicha Stay & Hera Panchami: The deities reside at Gundicha Temple for 7 days. On the 5th day (Hera Panchami), Goddess Lakshmi arrives in fury, enters the Gundicha temple secretly, and breaks a piece of Jagannath's chariot (Nandighosh) out of jealousy before returning to the main temple.", "Step 4: ")
    doc.add_bullet("Bahuda Yatra, Suna Besha, & Adhara Pana: Return procession, golden embellishment on Ekadashi, and the offering of large clay pitchers of consecrated milk beverage (Adhara Pana) offered to pacify guardian spirits.", "Step 5: ")
    doc.add_bullet("Niladri Bije & Rasagola Offering: On Trayodashi, Goddess Lakshmi locks the temple gate in indignation; Lord Jagannath presents her with sweet Rasagolas to appease her before entering the sanctum.", "Step 6: ")

    doc.add_callout(
        title="Crowd Management & Global Impact",
        text="Rath Yatra attracts between 1.0 to 1.5 million devotees annually. The Odisha State Police, District Administration, and Indian Railways deploy specialized integrated command control centers (ICCC), AI crowd-density monitoring, and disaster response forces (ODRAF/NDRF) to ensure safe execution along the 3 km Grand Road.",
        tag="ADMINISTRATIVE & LOGISTICAL RECORD [TIME-SENSITIVE]",
        confidence="HIGH"
    )

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S008"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "08_Rath_Yatra.docx"))

def generate_doc_29():
    doc = PuriDocBuilder(
        title="Cultural Festivals Database: Comprehensive Inventory of Sacred Celebrations",
        doc_number="29",
        category="Festival Knowledge Database"
    )

    doc.add_h1("1. Master Inventory of Festivals Celebrated in Puri")
    doc.add_paragraph("This database indexes the major, minor, and seasonal festivals observed in the Shree Jagannath Temple, the Ashta Sambhu shrines, and the wider Puri cultural landscape.")

    headers = ["Fest ID", "Festival Name", "Odia Name", "Timing / Lunar Tithi", "Primary Location", "Key Rituals & Significance"]
    rows = [
        ["FEST-001", "Chandan Yatra", "ଚନ୍ଦନ ଯାତ୍ରା", "Akshaya Tritiya (Vaisakha)", "Narendra Tank", "42 days; water sports of representative deities; initiation of chariot construction."],
        ["FEST-002", "Snana Yatra", "ସ୍ନାନ ଯାତ୍ରା", "Jyeshtha Purnima", "Snana Mandapa", "108 pitchers bath; Gajanana Besha; initiates 15-day Anavasara period."],
        ["FEST-003", "Rath Yatra", "ରଥଯାତ୍ରା", "Ashadha Shukla Dwitiya", "Bada Danda to Gundicha", "World-renowned chariot festival; Pahandi, Chhera Pahara, public darshan."],
        ["FEST-004", "Hera Panchami", "ହେରା ପଞ୍ଚମୀ", "Ashadha Shukla Panchami", "Gundicha Temple", "Goddess Lakshmi's ritual visit; breaks part of Jagannath's chariot in mock anger."],
        ["FEST-005", "Bahuda Yatra", "ବାହୁଡ଼ା ଯାତ୍ରା", "Ashadha Shukla Dashami", "Bada Danda", "Return journey of chariots; Poda Pitha offering at Mausi Maa shrine."],
        ["FEST-006", "Suna Besha", "ସୁନା ବେଶ", "Ashadha Shukla Ekadashi", "Singhadwara Chariots", "Deities adorned in 208 kg gold attire; public darshan on chariots."],
        ["FEST-007", "Adhara Pana", "ଅଧର ପଣା", "Ashadha Shukla Dwadashi", "On Chariots", "Offering of sweet herbal drink in 9 large clay vessels broken for guardian spirits."],
        ["FEST-008", "Niladri Bije", "ନୀଳାଦ୍ରି ବିଜେ", "Ashadha Shukla Trayodashi", "Singhadwara & Sanctum", "Return to Ratnavedi; Rasagola offering to Lakshmi; Rasagola Dibasa."],
        ["FEST-009", "Jhulan Yatra", "ଝୁଲଣ ଯାତ୍ରା", "Shravana Shukla Dashami-Purnima", "Temple & Mathas", "Monsoon swing festival; classical music, Gotipua dance, floral decorations."],
        ["FEST-010", "Radhashtami", "ରାଧାଷ୍ଟମୀ", "Bhadrapada Shukla Ashtami", "Jagannath Temple", "Celebration of Radha's appearance; special alankara and temple nitis."],
        ["FEST-011", "Kartika Purnima", "କାର୍ତ୍ତିକ ପୂର୍ଣ୍ଣିମା", "Kartika Purnima (Nov)", "Mahodadhi & Temple", "Boita Bandana maritime ceremony; miniature boat floating at Puri beach."],
        ["FEST-012", "Dola Yatra", "ଦୋଳ ଯାତ୍ରା", "Phalguna Purnima", "Dola Mandapa", "Spring color festival; palanquin processions with fagu (herbal vermillion)."],
        ["FEST-013", "Maha Shivaratri", "ମହା ଶିବରାତ୍ରୀ", "Phalguna Krishna Chaturdashi", "Lokanath Temple", "All-night vigil; Hari-Hara bheta; lifting of the Mahadipa at midnight."],
        ["FEST-014", "Magha Saptami", "ମାଘ ସପ୍ତମୀ", "Magha Shukla Saptami", "Chandrabhaga & Puri Beach", "Sun worship at sea; mass sacred holy dip at dawn in memory of Samba."]
    ]
    doc.add_table(headers, rows, [0.8, 1.2, 1.0, 1.2, 1.1, 1.2])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S008"),
        get_source("PUR-S019")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "29_Cultural_Festivals_Database.docx"))

if __name__ == "__main__":
    generate_doc_07()
    generate_doc_08()
    generate_doc_29()
    print("Group 3 completed successfully.")
