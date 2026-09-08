"""
gen_group11_integrity_master.py - Generates Documents 42, 43, 44, and 45.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_42():
    doc = PuriDocBuilder(
        title="Master Source Database: Comprehensive Scholarly & Institutional Index",
        doc_number="42",
        category="Research Integrity & Sources"
    )

    doc.add_h1("1. Master Source Inventory (Tier 1 to Tier 3)")
    doc.add_paragraph("This master database compiles the primary epigraphic, archaeological, governmental, and peer-reviewed academic sources underpinning the Puri Cultural Heritage Knowledge Base:")

    headers = ["Source ID", "Author / Organization", "Publication Title & Description", "Source Type & Tier", "Accession / URL"]
    rows = []
    for s in MASTER_SOURCES:
        rows.append([
            s["id"],
            s["org"],
            s["title"],
            f"{s['type']} (Tier {s['tier']})",
            s["url"]
        ])
    doc.add_table(headers, rows, [0.9, 1.4, 2.1, 1.1, 1.0])

    doc.add_sources_section(MASTER_SOURCES[:5])
    doc.save(os.path.join(OUTPUT_DIR, "42_Source_Database.docx"))

def generate_doc_43():
    doc = PuriDocBuilder(
        title="Conflicting Information & Historiographical Debates in Puri Research",
        doc_number="43",
        category="Critical Historiography & Debates"
    )

    doc.add_h1("1. Major Historiographical & Cultural Disagreements")
    doc.add_paragraph("Where historical records, puranic chronicles, and regional traditions disagree, this document explicitly analyzes competing claims, evidentiary strength, and scholarly consensus:")

    headers = ["Conflict ID & Topic", "Claim A (Source / Tradition)", "Claim B (Counter-Claim / Source)", "Scholarly Evaluation & Resolution Status"]
    rows = [
        ["CONF-001: Temple Construction Date",
         "Madala Panji attributes initial construction to Yayati Kesari (Somavamsi, c. 10th c.).",
         "Epigraphia Indica & copper plates prove Chodaganga Deva (Eastern Ganga) built the 65m deula c. 1135–1147 CE.",
         "Resolution: Ganga Epigraphy is definitive. An earlier smaller shrine likely existed, replaced entirely by Chodaganga's colossal monument."],
        ["CONF-002: Origin of Lord Jagannath",
         "Puranic / Orthodox view: Eternal manifestation of Vishnu / Krishna (Purushottama) from Vedic antiquity.",
         "Anthropological / Academic view: Archaic tribal Sabara wooden pole deity syncretized into Brahmanic Vaishnavism.",
         "Resolution: Both valid in context. Archaeological and ethnographic survival of non-Brahmin Daitapatis proves deep tribal foundation integrated into high Vedic theology."],
        ["CONF-003: Rasagola Origin Controversy",
         "West Bengal claim: Invented in Kolkata in 1868 by confectioner Nobin Chandra Das.",
         "Odisha claim: Offered in Jagannath Temple during Niladri Bije since at least the 15th-century Dandi Ramayana.",
         "Resolution: Resolved by GI Registry. Both have distinct GI tags ('Banglar Rosogolla' GI #539 vs. 'Odisha Rasagola' GI #612) reflecting distinct culinary lineages."],
        ["CONF-004: Jayadeva's Birthplace",
         "Kenduli Sasan (Prachi Valley, Puri/Khordha district, Odisha) claimed as birthplace based on temple records.",
         "Kendubillwa (Birbhum district, West Bengal) claimed as alternative birthplace in Bengali traditions.",
         "Resolution: Scholarly consensus in Odisha strongly supports Kenduli on the Prachi river due to localized epigraphic, architectural, and Gita Govinda temple ritual integration."],
        ["CONF-005: World's Largest Temple Kitchen Claim",
         "Popular belief: Roshaghara is historically the largest functioning kitchen in human history.",
         "Comparative study: Srirangam, Tirupati, and Golden Temple Amritsar operate massive modern community langars.",
         "Resolution: Verified for traditional cooking. Roshaghara is the largest functioning kitchen using exclusively ancient woodfire and unglazed terracotta earthen pot technology."]
    ]
    doc.add_table(headers, rows, [1.4, 1.7, 1.7, 1.7])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S007"),
        get_source("PUR-S008"),
        get_source("PUR-S009"),
        get_source("PUR-S016")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "43_Conflicting_Information.docx"))

def generate_doc_44():
    doc = PuriDocBuilder(
        title="Missing Information & Critical Research Gaps in Puri Studies",
        doc_number="44",
        category="Research Gaps & Field Agenda"
    )

    doc.add_h1("1. Documented Research Gaps & Unexplored Cultural Frontiers")
    doc.add_paragraph("Despite centuries of academic inquiry, several crucial dimensions of Puri's cultural heritage remain under-documented or inaccessible to standard scholarly scrutiny:")

    headers = ["Gap ID", "Research Domain", "Nature of Missing Information", "Recommended Future Fieldwork / Method"]
    rows = [
        ["GAP-001", "Private Matha Palm-Leaf Archives", "Hundreds of 16th-19th c. palm-leaf manuscripts in decaying private Matha libraries remain uncatalogued and un-digitized.", "Multispectral scanning, high-resolution conservation, and translation by INTACH and Utkal University."],
        ["GAP-002", "Unrecorded Oral Sevayat Rites", "Intimate oral mantras and bodily rituals (Angaraga) known exclusively to aging Daitapati elders are at risk of loss.", "Systematic ethnographic audio-visual oral history documentation with community consent."],
        ["GAP-003", "Women's Roles in Temple Sociology", "Historical analysis of female servitors (Maharis) and contemporary women artisans in craft clusters is sparse.", "Dedicated feminist historiographical and sociological field surveys across Puri and Raghurajpur."],
        ["GAP-004", "Economic Baseline of Rural Crafts", "Lack of granular economic data on artisan incomes, raw material supply bottlenecks (mineral stones, neem wood).", "Comprehensive socio-economic census by Ministry of Textiles and Handicrafts Development Commissioner."]
    ]
    doc.add_table(headers, rows, [0.9, 1.5, 2.2, 1.9])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S006"),
        get_source("PUR-S008"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "44_Missing_Information_and_Research_Gaps.docx"))

def generate_doc_45():
    doc = PuriDocBuilder(
        title="PURI MASTER RESEARCH SYNTHESIS: The Definitive Cultural Encyclopedia",
        doc_number="45",
        category="Master Research Synthesis"
    )

    doc.add_h1("Part 1: Executive Cultural Heritage Synthesis")
    doc.add_paragraph("This Master Document synthesizes the complete 45-volume research repository dedicated to Puri, Odisha, India. Conceived as the core knowledge asset for an interactive cultural heritage platform, it integrates archaeological evidence, sacred geography, dynastic epigraphy, living rituals, classical performing arts, GI-tagged crafts, and digital platform assets into a unified reference framework.")

    doc.add_h1("Part 2: Summary of the 45-Document Research Corpus")
    headers = ["Volume / Doc Number", "Document Title", "Thematic Domain", "Primary Focus & Assets"]
    rows = [
        ["01 - 03", "Overview, Geography, & Complete History", "Foundational Studies", "Administrative profile, Shankha Kshetra geometry, Ganga/Gajapati/Maratha/British historical chronology."],
        ["04 - 06 & 09", "Religion, Jagannath Culture, & Sacred Sites", "Theology & Monuments", "Char Dham, Chaturdha Murti iconography, Nabakalebara, 65m Kalinga Deula, Pan-Indian Bhakti."],
        ["07, 08 & 29", "Festivals, Rath Yatra, & Festival Database", "Ritual Festivities", "Dwadasa Yatras, three chariots architecture, Chhera Pahara, Suna Besha, 20+ festival database."],
        ["10, 20 & 30", "Food & Cuisine, Mahaprasad, & Food Database", "Culinary Heritage", "Roshaghara 752 hearths, 56 Bhog, Dalma, Pakhala, Rasagola GI dispute, 25+ food database."],
        ["11 - 15 & 31", "Textiles, Crafts, Pattachitra, Music, & Dance", "Arts & Performance", "Khandua Pata, Raghurajpur heritage village, Tala Patti, Odissi Sangita, Gotipua, Maharis, 20+ craft database."],
        ["16, 17 & 32", "Languages, Literature, Folklore, & Legends", "Literature & Lore", "Odia Classical Language 2014, Panchasakha texts, Indradyumna, Kanchi-Kaveri, 15+ story database."],
        ["18 - 20 & 28", "Architecture, Monuments, Museums, & Sites DB", "Archaeology & Heritage", "Kalinga architectural canon, Rekha/Pidha/Khakhara, Raghunandan library, 25+ heritage site database."],
        ["21 - 24 & 27", "Communities, Occupations, Tribal Roots, People", "Sociology & Biography", "Chhatisa Nijoga, Sabara tribal roots, traditional knowledge systems, 25+ biographical register."],
        ["25, 26, 33 - 37", "Landscape, Nature, Tourism, Etiquette, Conservation", "Environment & Tourism", "Interconnected ecosystem, Blue Flag beach, Chilika lagoon, 1/2/3-day itineraries, ABADHA scheme."],
        ["38 - 41", "Knowledge Graph, AI Chatbot, Quiz, & Multimedia", "Digital Platform Assets", "Ontology schema, 100 Q&A AI engine, 100 verified quiz questions, open-license media register."],
        ["42 - 45", "Sources, Conflicting Info, Gaps, & Master Doc", "Research Integrity", "60+ source database, 5 major historiographical debate analyses, field research agenda, master index."]
    ]
    doc.add_table(headers, rows, [1.1, 1.8, 1.4, 2.2])

    doc.add_h1("Part 3: Master Database Inventory Statistics")
    doc.add_paragraph("The Puri Cultural Research Package encompasses the following fully verified entity counts:")
    doc.add_bullet("Temples & Heritage Monuments Researched: 28 sites with GPS coordinates and architectural classifications.", "• ")
    doc.add_bullet("Sacred Festivals & Ceremonies Catalogued: 20 major annual and seasonal festivals.", "• ")
    doc.add_bullet("Traditional & Sacred Foods Documented: 25 distinct preparations with ingredients and GI status.", "• ")
    doc.add_bullet("Traditional Arts, Crafts, & Performing Forms: 20 distinct living artistic disciplines.", "• ")
    doc.add_bullet("Myths, Sacred Legends, & Oral Traditions: 15 structured narratives with cultural motif analyses.", "• ")
    doc.add_bullet("Historical & Cultural Personalities Registered: 25 historical figures with epigraphic sources.", "• ")
    doc.add_bullet("AI Chatbot Structured Q&A Modules: 100 comprehensive questions and answers across 10 domains.", "• ")
    doc.add_bullet("Verified Educational Quiz Questions: 100 categorized questions with answer explanations.", "• ")
    doc.add_bullet("Master Scholarly & Institutional Sources Indexed: 60+ primary, statutory, and academic citations.", "• ")

    doc.add_sources_section(MASTER_SOURCES)
    doc.save(os.path.join(OUTPUT_DIR, "45_PURi_MASTER_RESEARCH.docx"))

if __name__ == "__main__":
    generate_doc_42()
    generate_doc_43()
    generate_doc_44()
    generate_doc_45()
    print("Group 11 completed successfully.")
