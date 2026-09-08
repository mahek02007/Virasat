"""
gen_group7_architecture_heritage.py - Generates Documents 18, 19, 20, and 28.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_18():
    doc = PuriDocBuilder(
        title="Architecture & Heritage Buildings: The Kalinga Classical Style & Urban Form",
        doc_number="18",
        category="Architecture & Heritage Structures"
    )

    doc.add_h1("1. The Kalinga Temple Architectural Canon")
    doc.add_paragraph("Kalinga architecture represents one of India's most mature regional temple styles (classified within the Nagara order), governed by ancient Odia architectural treatises such as the Silpa Prakasa, Bhuvana Pradipa, and Silpa Sarani. The canon divides structural typologies into three fundamental forms:")

    headers = ["Typology (Deula Style)", "Structural Profile & Roof Geometry", "Exemplar Structures in Puri"]
    rows = [
        ["Rekha Deula (ରେଖା ଦେଉଳ)", "Curvilinear spire (Sikhara) with vertical fluting (Rathas); crowning Amalaka and Kalasa", "Vimana (Main Sanctum) of Jagannath Temple (65m); Lokanath Temple."],
        ["Pidha Deula / Bhadra Deula", "Pyramidal stepped roof composed of receding horizontal tiers (Potalas / Pidhas)", "Jagamohana (Assembly Hall) & Bhoga Mandapa of Jagannath Temple; Gundicha Jagamohana."],
        ["Khakhara Deula (ଖାଖରା ଦେଉଳ)", "Barrel-vaulted semi-cylindrical roof resembling a gourd (Khakhara); exclusively Shakta", "Varahi Temple (Chaurasi); Maa Mangala Temple (Kakatpur); Vimala subsidiary sanctum."]
    ]
    doc.add_table(headers, rows, [1.6, 2.7, 2.2])

    doc.add_h1("2. Traditional Urban Form: Bada Danda & Matha Monastic Enclaves")
    doc.add_paragraph("The urban morphology of Puri is fundamentally sacred and ceremonial, anchored by the axial orientation of Bada Danda (Grand Road). Spanning ~3 km in length and over 40 meters in width, this ceremonial corridor connects the Shri Mandira to the Gundicha Temple. Flanking this sacred spine are dozens of historic Mathas—two-to-three-story monastic quadrangles characterized by internal courtyards (Chahala), arched verandas, carved wooden brackets, and subterranean relic libraries (e.g. Emar Matha, Raghunandan Library).")

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S020")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "18_Architecture_and_Heritage_Buildings.docx"))

def generate_doc_19():
    doc = PuriDocBuilder(
        title="Heritage Sites & Protected Monuments of Puri District",
        doc_number="19",
        category="Heritage Sites & Monuments"
    )

    doc.add_h1("1. ASI & State Protected Monuments in Puri Circuit")
    doc.add_paragraph("Puri district contains an extraordinary density of protected archaeological monuments, managed collaboratively by the Archaeological Survey of India (ASI) and the State Archaeology Department of Odisha:")

    headers = ["Monuments / Site", "Location / Distance", "Dynasty & Period", "Protection & Architectural Highlights"]
    rows = [
        ["Shree Jagannath Temple Complex", "Puri Core City (Bada Danda)", "Eastern Ganga (12th Century CE)", "Centrally Protected by ASI; monumental 65m Kalinga deula with 120+ inner shrines."],
        ["Lokanath Temple", "Western Puri (1.5 km from Jagannath Temple)", "Somavamsi / Early Ganga", "Submerged Shivalinga continuously bathed by natural underground spring water."],
        ["Markandeshwar Temple & Tank", "Northern Puri near Markandeya Pokhari", "Bhauma-Kara / Somavamsi (10th-11th c.)", "State Protected; ornate Kirtimukha carvings, Nataraja sculptures, and ghat stepped stone architecture."],
        ["Gundicha Temple (Yajna Vedi)", "Northern terminus of Bada Danda (2.5 km)", "Gajapati / Ganga reconstructions", "Garden temple in expansive walled orchard; annual summer residence of the Triad."],
        ["Sun Temple, Konark (Cultural Link)", "Konark (35 km east of Puri via Marine Drive)", "Eastern Ganga (Narasimhadeva I, 13th c.)", "UNESCO World Heritage Site; monumental colossal stone chariot dedicated to Surya."],
        ["Alarnath Temple, Brahmagiri", "Brahmagiri (25 km west of Puri)", "Early Medieval (Alwar / Ganga period)", "Four-armed Vishnu deity; focal pilgrimage shrine during 15-day Anavasara seclusion."]
    ]
    doc.add_table(headers, rows, [1.5, 1.4, 1.4, 2.2])

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S020")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "19_Heritage_Sites_and_Monuments.docx"))

def generate_doc_20():
    doc = PuriDocBuilder(
        title="Museums, Libraries, & Cultural Institutions of Puri",
        doc_number="20",
        category="Museums & Archives"
    )

    doc.add_h1("1. Repository Institutions of Puri's Cultural Heritage")
    doc.add_paragraph("The preservation of Puri's material, manuscript, and epigraphic heritage is stewarded by specialized archival and museum institutions:")

    headers = ["Institution Name", "Location & Type", "Key Collections & Holdings", "Significance & Visitor Info"]
    rows = [
        ["District Museum, Puri", "Station Road, Puri (Govt. of Odisha)", "Stone sculptures, palm-leaf manuscripts (Pothi), traditional textiles, and Pattachitra scrolls", "Open Tue-Sun (10:00 AM - 5:00 PM); essential introduction for cultural tourists."],
        ["Raghunandan Library", "Opposite Singhadwara (Emar Matha compound)", "Rare Sanskrit and Odia palm-leaf manuscripts, colonial gazetteers, historical temple records", "Historical scholarly institution with iconic terrace viewpoint overlooking Grand Road."],
        ["Odisha Crafts Museum (Kalabhoomi)", "Bhubaneswar (Heritage Gateway to Puri)", "Comprehensive master galleries of Pattachitra, Pipili Applique, Stone & Wood Carvings", "Premier state museum showcasing regional craft evolution from ancient to contemporary."],
        ["SJTA Archives & Madala Panji Cell", "Grand Road, Puri", "Official palm-leaf chronicles, royal Sanads, land endowments, and Sevayat Record of Rights", "Statutory research repository accessible for academic and judicial verification."]
    ]
    doc.add_table(headers, rows, [1.5, 1.4, 2.1, 1.5])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "20_Museums_and_Cultural_Institutions.docx"))

def generate_doc_28():
    doc = PuriDocBuilder(
        title="Temples & Heritage Sites Database: Master Archaeological Register",
        doc_number="28",
        category="Heritage Site Database"
    )

    doc.add_h1("1. Master Archaeological & Sacred Site Inventory")
    headers = ["Site ID", "Name of Monument", "Coordinates", "Style / Period", "Presiding Deity", "Protection Status"]
    rows = [
        ["SITE-001", "Shree Jagannath Temple", "19.8048° N, 85.8179° E", "Mature Kalinga (12th c. CE)", "Lord Jagannath, Balabhadra, Subhadra", "Centrally Protected (ASI)"],
        ["SITE-002", "Gundicha Temple", "19.8242° N, 85.8398° E", "Pidha & Rekha Deula (Ganga/Gajapati)", "Yajna Vedi (Chariot residence)", "State Protected / SJTA"],
        ["SITE-003", "Lokanath Temple", "19.7992° N, 85.8085° E", "Somavamsi (11th c. CE)", "Submerged Shiva Linga", "State Protected"],
        ["SITE-004", "Markandeshwar Temple", "19.8115° N, 85.8190° E", "Early Kalinga (10th c. CE)", "Lord Shiva (Markandeshwar)", "State Protected Archaeology"],
        ["SITE-005", "Alarnath Temple", "19.7612° N, 85.6792° E", "Kalinga Style (11th-12th c.)", "Four-armed Lord Vishnu", "State Protected"],
        ["SITE-006", "Sakhigopal Temple", "19.9515° N, 85.8302° E", "Pidha Style (19th c. reconstruction)", "Lord Krishna (Gopinatha)", "State Protected / Endowments"],
        ["SITE-007", "Narendra Pokhari Tank", "19.8162° N, 85.8245° E", "Medieval Hydraulic Architecture", "Chandan Mandapa (Water Temple)", "Puri Municipality / SJTA"],
        ["SITE-008", "Maa Mangala Temple", "20.0094° N, 86.0125° E", "Khakhara / Pidha (15th c. CE)", "Maa Mangala (Shakta Kakatpur)", "State Protected / Endowments"],
        ["SITE-009", "Varahi Temple, Chaurasi", "20.0452° N, 86.1158° E", "Khakhara Deula (10th c. CE)", "Goddess Varahi (Tantric)", "Centrally Protected (ASI)"],
        ["SITE-010", "Sun Temple, Konark", "19.8876° N, 86.0945° E", "Monumental Kalinga (13th c. CE)", "Surya (Sun God)", "UNESCO World Heritage Site / ASI"]
    ]
    doc.add_table(headers, rows, [0.8, 1.5, 1.2, 1.1, 1.1, 0.8])

    doc.add_sources_section([
        get_source("PUR-S001"),
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S020")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "28_Temples_and_Heritage_Site_Database.docx"))

if __name__ == "__main__":
    generate_doc_18()
    generate_doc_19()
    generate_doc_20()
    generate_doc_28()
    print("Group 7 completed successfully.")
