"""
gen_group5_arts_crafts.py - Generates Documents 11, 12, 13, 14, 15, and 31.
"""

import os
from doc_builder import PuriDocBuilder
from sources_data import MASTER_SOURCES, get_source

OUTPUT_DIR = r"C:\Users\YADAVI\.gemini\antigravity\scratch\PURI_ODISHA_RESEARCH"

def generate_doc_11():
    doc = PuriDocBuilder(
        title="Traditional Clothing, Textiles, & Temple Vestments of Puri",
        doc_number="11",
        category="Textiles & Traditional Attire"
    )

    doc.add_h1("1. Sacred Textiles & Temple Vestments (Khandua Pata)")
    doc.add_paragraph("Textiles in Puri are intrinsically tied to the daily dressing rituals (Beshas) of Lord Jagannath. The most revered textile is the sacred Khandua Pata (also known as Gitagovinda Pata), woven traditionally by the Weavers of Nuapatna (Tigiria) for the temple. Verses from Jayadeva's 12th-century Sanskrit lyric poem Gita Govinda are woven directly into the red and yellow mulberry/tussar silk fabric using ikat tie-dye techniques. Lord Jagannath is draped in Khandua Pata during the nightly Badasinghara Besha before retiring to sleep.")

    headers = ["Textile / Attire Form", "Materials & Weaving Technique", "Cultural Context & Geographic Origin"]
    rows = [
        ["Khandua Pata (ଗୀତଗୋବିନ୍ଦ ପାଟ)", "Pure Silk; Bandha (Ikat) tie-dye; Gitagovinda calligraphic weave", "Reserved for Jagannath's nightly ritual; Nuapatna-Cuttack corridor."],
        ["Gamucha (ଗାମୁଛା)", "Pure unbleached handloom cotton; red or orange checked borders", "Ubiquitous Odia handloom towel worn by sevayats, fishermen, and pilgrims."],
        ["Sevayat Dhoti & Uttariya", "Fine white cotton with sacred yellow/red borders (Sadha / Pata)", "Mandatory ritual attire for priests serving on the Ratnavedi."],
        ["Bomkai & Sambalpuri Sarees", "Silk/Cotton Bandha with Shankha, Chakra, Padma, and Temple borders", "Distinct regional weaves from southern and western Odisha worn during temple visits."]
    ]
    doc.add_table(headers, rows, [1.6, 2.3, 2.6])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S007"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "11_Clothing_and_Textiles.docx"))

def generate_doc_12():
    doc = PuriDocBuilder(
        title="Arts & Crafts of Puri District: Stone, Wood, Appliqué, & Marine Crafts",
        doc_number="12",
        category="Traditional Handicrafts"
    )

    doc.add_h1("1. The Living Craft Tradition of Puri District")
    doc.add_paragraph("Puri district constitutes one of India's richest handicraft clusters, sustained historically by royal temple patronage and continuous pilgrim demand. The craft ecosystem ranges from monumental stone carving to delicate marine shell crafts:")

    headers = ["Craft Tradition", "Primary Materials Used", "Artisan Communities & Locations", "GI / Heritage Status"]
    rows = [
        ["Stone Carving (ଶିଳ୍ପକଳା)", "Sandstone, Khondalite, Chlorite (Kochila pathara), Soapstone", "Pathuria community; Puri town, Konark, Raghurajpur", "National Award-winning heritage; temple restoration"],
        ["Pipili Applique Work (ଚାନ୍ଦୁଆ)", "Colored cotton/velvet fabrics stitched onto base cloth; mirrors, motifs", "Darji / Muslim artisan community of Pipili (35 km from Puri)", "GI Registered (Pipili Applique No. 86); used in Rath canopies"],
        ["Wood Carving (କାଠ ଖୋଦେଇ)", "Maharukha, Gambhari, Neem, Sal, Teak wood", "Maharana woodworkers; Puri, Raghurajpur", "Chariot construction, wooden temple deities, mask-making"],
        ["Conch & Seashell Craft", "Natural sea conch (Turbinella pyrum), cowrie shells, mother-of-pearl", "Coastal artisanal clusters in Puri town (Swargadwar beach)", "Bangles, ritual conches, decorative sculptures"],
        ["Puri Sand Art (ବାଲୁକା କଳା)", "Puri Golden Beach natural sea sand and water", "Modern master sculptors (e.g. Sudarsan Pattnaik)", "Internationally acclaimed contemporary cultural art form"]
    ]
    doc.add_table(headers, rows, [1.4, 1.8, 1.8, 1.5])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S007"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "12_Arts_and_Crafts.docx"))

def generate_doc_13():
    doc = PuriDocBuilder(
        title="Pattachitra & Raghurajpur: Master Scroll Painting & Heritage Craft Village",
        doc_number="13",
        category="Pattachitra & Raghurajpur (Deep Dive)"
    )

    doc.add_h1("1. The Ancient Art of Odisha Pattachitra (GI Registered)")
    doc.add_paragraph("Pattachitra (derived from Sanskrit 'Patta' meaning canvas/cloth and 'Chitra' meaning painting) is a classical scroll painting tradition rooted in the sacred rituals of the Jagannath Temple since at least the 12th century CE. It received Geographical Indication (GI) Tag No. 51 in 2008:")

    headers = ["Production Stage", "Materials & Chemical Process", "Artisan Technique & Aesthetics"]
    rows = [
        ["Patta (Cloth Base)", "Layers of pure cotton/silk treated with tamarind seed paste (Niryas) and chalk powder (Khadya)", "Polished with semi-precious agate stones (Khaddar) to create a smooth, leather-like canvas."],
        ["100% Natural Pigments", "Hingula (vermillion), Haritala (yellow arsenic stone), Sankha (conch white), Lamp Black (Kajala), Geru (ochre)", "Zero synthetic chemicals; crushed by hand and bound with tree gum (Babool resin)."],
        ["Fine Brushwork", "Brushes made from fine mongoose, mouse, or squirrel hair fixed into bamboo quills", "Intricate hair-thin line work (Poli and Dhala work) with signature floral lace borders (Laccha)."],
        ["Finishing (Varnish)", "Natural lac (Jaunsa) coating melted over glowing charcoal", "Renders the painting waterproof, lustrous, and remarkably resilient for decades."]
    ]
    doc.add_table(headers, rows, [1.4, 2.3, 2.8])

    doc.add_h1("2. Raghurajpur: India's Premier Heritage Craft Village")
    doc.add_paragraph("Located 14 km north of Puri amidst coconut and betel groves on the southern bank of the Bhargavi river, Raghurajpur is an internationally celebrated heritage village designated by INTACH and the Ministry of Tourism in 2000. Unique in South Asia, virtually every one of its ~140 households is actively engaged in master handicrafts:")
    doc.add_bullet("Urban Layout & Mural Architecture: Two parallel rows of traditional brick and thatched houses facing a central shrine dedicated to Radha-Mohan, with house facades decorated with vibrant exterior murals.", "• ")
    doc.add_bullet("Tala Pattachitra (Palm Leaf Engraving): Dried palm leaves (Corypha umbraculifera) etched with a fine iron stylus (Lekhani) and rubbed with lamp black to reveal microscopic, exquisite line illustrations.", "• ")
    doc.add_bullet("Gotipua Gurukuls: Birthplace of Padma Vibhushan Guru Kelucharan Mohapatra; home to active Gotipua dance gurukuls preserving traditional performance disciplines.", "• ")

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S006"),
        get_source("PUR-S007"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "13_Pattachitra_and_Raghurajpur.docx"))

def generate_doc_14():
    doc = PuriDocBuilder(
        title="Music & Dance: Odissi Classical Traditions, Mardala, & Panchamahabadya",
        doc_number="14",
        category="Performing Arts & Music"
    )

    doc.add_h1("1. Odissi Classical Music Tradition (Odissi Sangita)")
    doc.add_paragraph("Odissi Sangita is an ancient classical musical system distinct from both North Indian Hindustani and South Indian Carnatic systems, documented in classical treatises such as the Sangita Narayana and Gita Prakasa. Characterized by unique ragas (such as Kalyana Ahari, Mohana, Asavari), talas (Jhampa, Triputa, Khemta), and lyrical compositions derived from Jayadeva's Gita Govinda, Odissi music constitutes the auditory soul of Puri's temple worship.")

    headers = ["Musical Dimension", "Instruments / Vocal Style", "Ritual & Cultural Function"]
    rows = [
        ["Mardala (ମର୍ଦ୍ଦଳ)", "Two-headed barrel drum made of seasoned wood and leather; high pitch precision", "The primary percussive accompaniment for Odissi dance and temple rituals; recognized classical drum."],
        ["Panchamahabadya", "Five sacred instruments: Ghanta (cymbals), Kahali (metal horn), Dhol, Bheri, Mahuri (oboe-like)", "Played during deity processions (Pahandi, Chandan Yatra, daily royal services)."],
        ["Temple Gita Govinda Recitation", "Sung nightly at Badasinghara by hereditary Sevakas (Gita Govinda Gayakas)", "Devotional lullaby sung to Jagannath accompanied by cymbals before the temple doors are locked."],
        ["Kirtan & Sankirtana", "Harinama Kirtan using Mridanga and Karatalas", "Vibrant community congregational singing popularized across Puri by Chaitanya Mahaprabhu."]
    ]
    doc.add_table(headers, rows, [1.5, 2.3, 2.7])

    doc.add_sources_section([
        get_source("PUR-S002"),
        get_source("PUR-S003"),
        get_source("PUR-S011"),
        get_source("PUR-S018")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "14_Music_and_Dance.docx"))

def generate_doc_15():
    doc = PuriDocBuilder(
        title="Gotipua, Classical Odissi, & Traditional Theatrical Arts",
        doc_number="15",
        category="Dance & Performance Traditions"
    )

    doc.add_h1("1. The Evolution of Odissi Dance: From Maharis to Global Stages")
    doc.add_paragraph("Odissi, one of India's eight classical dance forms, traces its archaeological origins to the 2nd century BCE friezes of the Udayagiri and Khandagiri caves and its living ritual lineage to the temple dancing girls (Maharis) of the Shree Jagannath Temple:")

    headers = ["Tradition / Epoch", "Performers & Characteristics", "Historical Trajectory & 20th-Century Revival"]
    rows = [
        ["Mahari Temple Tradition (ମାହାରୀ)", "Consecrated female servitors of Jagannath; danced in the Natamandapa", "Strictly ritualistic; declined in the early 20th century; formally abolished with the end of the devadasi system."],
        ["Gotipua Tradition (ଗୋଟିପୁଅ)", "Young boys (ages 6 to 14) dressed as female damsels; dynamic acrobatics (Bandha Nritya)", "Emerged in the 16th century with the patronage of Raja Ramachandra Deva and Akhadas; direct stylistic progenitor of modern Odissi."],
        ["Classical Odissi Revival (1950s)", "Formalized solo classical repertoire based on Tribhangi (three-bend posture) and Chauka", "Revived by the Jayantika association and great gurus: Guru Kelucharan Mohapatra, Guru Pankaj Charan Das, and Guru Deba Prasad Das."]
    ]
    doc.add_table(headers, rows, [1.5, 2.3, 2.7])

    doc.add_h1("2. Traditional Folk Theatre: Pala and Daskathia")
    doc.add_paragraph("Beyond classical dance, Puri district preserves dynamic narrative theatrical traditions:")
    doc.add_bullet("Pala (ପାଲା): A sophisticated performance by a troupe of 5-6 artists led by a Gayaka (lead singer) holding a Chamara (flywhisk) and cymbals, debating Sanskrit puranic texts, Odia poetry, and philosophy through dramatic dialogues and humor.", "• ")
    doc.add_bullet("Daskathia (ଦାସକାଠିଆ): A dynamic two-person ballad performance where the performers click pairs of polished wooden castanets (Kathi), narrating religious myths and historical epics with rapid metrical verses.", "• ")

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S011"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "15_Gotipua_Odissi_and_Performance_Traditions.docx"))

def generate_doc_31():
    doc = PuriDocBuilder(
        title="Arts & Crafts Database: Master Inventory of Handicrafts & Performance Disciplines",
        doc_number="31",
        category="Arts & Crafts Knowledge Database"
    )

    doc.add_h1("1. Master Inventory of Arts, Crafts, and Performing Arts")
    headers = ["Art / Craft ID", "Craft Name", "Primary Medium", "Artisan Communities", "Core Production Cluster", "Heritage / GI Status"]
    rows = [
        ["CRAFT-001", "Pattachitra", "Treated Cotton/Silk Cloth; Stone Pigments", "Chitrakara guild", "Raghurajpur, Puri City, Dandashahi", "GI Registered (GI No. 51)"],
        ["CRAFT-002", "Tala Pattachitra", "Dried Palm Leaves; Lamp Black; Stylus", "Chitrakara / Traditional Artists", "Raghurajpur, Kankana, Puri", "National Heritage Handicraft"],
        ["CRAFT-003", "Pipili Applique", "Stitched Fabric, Mirrors, Embroidery", "Darji (Tailor) Artisans", "Pipili Town (Puri District)", "GI Registered (GI No. 86)"],
        ["CRAFT-004", "Stone Sculpture", "Khondalite, Chlorite, Sandstone", "Pathuria stone carvers", "Puri, Konark, Emar Matha lane", "Classical Architectural Guild"],
        ["CRAFT-005", "Wood Carving", "Neem, Sal, Teak, Gambhari wood", "Maharana carpenters", "Puri City (Rath Khala), Raghurajpur", "Rath Yatra Construction Heritage"],
        ["CRAFT-006", "Gotipua Dance", "Acrobatic Bandha Nritya; Boy dancers", "Gurukul disciples (Guru-Shishya)", "Raghurajpur, Dimirisena, Puri", "Sangeet Natak Akademi Recognized"],
        ["CRAFT-007", "Odissi Classical Dance", "Classical solo dance; Tribhangi stance", "Classical dancers & Gurus", "Puri, Bhubaneswar, Worldwide", "Classical Indian Dance (UNESCO List Int.)"],
        ["CRAFT-008", "Conch Shell Craft", "Sea conch shells (Shankha)", "Artisanal shell carvers", "Swargadwar Beach Ward, Puri", "Traditional Coastal Craft"],
        ["CRAFT-009", "Puri Sand Art", "Sea beach sand & saltwater", "Contemporary Master Artists", "Puri Golden Beach", "Global Cultural Art Movement"],
        ["CRAFT-010", "Pala Performance", "Musical ballad troupe (Gayaka & Bayaka)", "Traditional performing troupes", "Puri District Rural & Temple Corridors", "Intangible Performing Heritage"]
    ]
    doc.add_table(headers, rows, [0.8, 1.2, 1.3, 1.1, 1.1, 1.0])

    doc.add_sources_section([
        get_source("PUR-S003"),
        get_source("PUR-S007"),
        get_source("PUR-S011"),
        get_source("PUR-S014")
    ])

    doc.save(os.path.join(OUTPUT_DIR, "31_Arts_Crafts_Database.docx"))

if __name__ == "__main__":
    generate_doc_11()
    generate_doc_12()
    generate_doc_13()
    generate_doc_14()
    generate_doc_15()
    generate_doc_31()
    print("Group 5 completed successfully.")
