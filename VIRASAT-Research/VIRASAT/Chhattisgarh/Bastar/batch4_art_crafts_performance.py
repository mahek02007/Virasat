import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_26():
    doc = create_base_document("26. Bastar Art and Visual Culture", "Indigenous Aesthetics, Geometric Abstraction, Murals, and Symbolic Motifs")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-026",
        "Geographic Scope": "Bastar Division Craft Clusters (Kondagaon, Jagdalpur, Tokapal, Narayanpur)",
        "Primary Classification": "Art History, Indigenous Aesthetics & Visual Anthropology",
        "Confidence Level": "HIGH (National Museum New Delhi, Crafts Council of India, GI Registry)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Visual Semiotics of Bastar Art")
    doc.add_paragraph(
        "Bastar visual art is rooted in an organic animism where forms are simplified into dynamic geometric lines, elongated limbs, "
        "and rhythmic repetitions. Key visual motifs include:\n"
        "• Sun and Moon: Cosmic witnesses of human contracts and agricultural fertility.\n"
        "• Horned Animals: The Indian Gaur (Bison) representing virility, stamina, and ancestral protection.\n"
        "• Tree of Life (Kalpavriksha): Sheltering birds, monkeys, snakes, and spirits in harmonic equilibrium.\n"
        "• Danteshwari / Anga Dev Shrines: Depicted as stylized chariots, palanquins, and oracular ladders."
    )
    
    save_document(doc, "26_Bastar_Art_and_Visual_Culture.docx")

def build_doc_27():
    doc = create_base_document("27. Bastar Dhokra Metal Craft", "Lost-Wax Casting (Cire Perdue), Ghadwa Artisan Clusters, and GI Certification")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-027",
        "Geographic Scope": "Kondagaon, Bhelvapadar, Jagdalpur, Tokapal (GI Tagged Origin: Bastar Dhokra)",
        "Primary Classification": "Metallurgy, Material Culture & Craft Economy",
        "Confidence Level": "HIGH (Geographical Indications Registry GOI, Crafts Council of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Ancient Lost-Wax Process (Cire Perdue)")
    doc.add_paragraph(
        "Bastar Dhokra is an ancient hollow-casting metallurgy technique practiced by the Ghadwa (or Ghasiya) community, tracing direct lineage "
        "to the Bronze Age Dancing Girl of Mohenjo-daro (c. 2300 BCE). Awarded Geographical Indication (GI) status (GI Application No. 83), "
        "the authentic process involves seven distinct non-industrial steps:"
    )
    
    add_heading_2(doc, "Seven-Stage Production Process Table")
    headers = ["Stage", "Process Name", "Materials Used", "Technical Execution"]
    rows = [
        ["1", "Core Preparation", "Clay, anthill soil, rice husk, cow dung", "Clay core molded to approximate final artifact geometry and sun-dried"],
        ["2", "Wax String Production", "Beeswax, Damar resin (Jhuna), mustard oil", "Wax pressed through wooden piston (Pichki) into thin filigree threads"],
        ["3", "Wax Patterning", "Prepared wax strings", "Core wrapped completely with wax threads; details and textures sculpted by hand"],
        ["4", "Mould Encapsulation", "Fine clay slip and heavy outer clay shell", "Fine clay applied to capture wax detail; outer clay coat applied with drainage channels"],
        ["5", "Dewaxing & Channeling", "Kiln fire heat", "Mould heated; molten wax drains out through runner channels leaving hollow cavity"],
        ["6", "Metal Pouring", "Brass, bronze, scrap copper-zinc alloy", "Molten metal poured directly into the pre-heated red-hot mould cavity"],
        ["7", "Breaking & Polishing", "Hammers, wire brushes, river sand", "Clay mould broken open (single-use); cast artifact chiseled, filed, and polished"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "27_Bastar_Dhokra_Metal_Craft.docx")

def build_doc_28():
    doc = create_base_document("28. Bastar Wood Carving", "Badhai Artisan Guilds, Sacred Ghotul Pillars, Masks, and GI Status")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-028",
        "Geographic Scope": "Bastar District, Kondagaon, Narayanpur (GI Tagged: Bastar Wooden Craft)",
        "Primary Classification": "Woodcraft, Material Culture & Architectural Sculpture",
        "Confidence Level": "HIGH (Geographical Indications Registry, Ministry of Textiles GOI)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Indigenous Woodcarving Traditions")
    doc.add_paragraph(
        "Bastar Wooden Craft (GI Application No. 84) is practiced by the Muria, Gond, and Badhai woodcarvers. Utilizing seasoned Teak (Tectona grandis), "
        "Sal (Shorea robusta), Shisham (Dalbergia latifolia), and White Kura wood, artisans carve intricate narrative reliefs. Primary objects include "
        "the iconic Ghotul central pillars (Kamba), funeral memorial pillars, ritual masks (Mukhota), tobacco containers (Chor), and royal doorways."
    )
    
    save_document(doc, "28_Bastar_Wood_Carving.docx")

def build_doc_29():
    doc = create_base_document("29. Bastar Bamboo and Cane Crafts", "Dhurwa Basketry, Granary Weaving, Hunting Traps, and Daily Implements")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-029",
        "Geographic Scope": "Kanger Valley, Narayanpur, Dantewada, Sukma",
        "Primary Classification": "Ethno-Craft, Bamboo Technology & Sustainable Design",
        "Confidence Level": "HIGH (National Bamboo Mission, Tribal Research Institute)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Bamboo Architecture and Implements")
    doc.add_paragraph(
        "Bamboo (Dendrocalamus strictus / 'Bans') forms the structural backbone of Bastar daily life. The Dhurwa and Gond communities split "
        "and weave bamboo culms into heavy-duty grain storage bins (Doli), winnowing fans (Sup), fishing traps (Jhorka / Dandar), and "
        "waterproof rain hats (Khumri) interlaced with dried Bauhinia vahlii (Mahul) leaves."
    )
    
    save_document(doc, "29_Bastar_Bamboo_and_Cane_Crafts.docx")

def build_doc_30():
    doc = create_base_document("30. Bastar Iron Craft and Lohe Shikhar", "Agariya / Lohar Metallurgy, Hand-Forged Wrought Iron, and GI Heritage")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-030",
        "Geographic Scope": "Kondagaon, Umargaon, Jagdalpur, Dantewada (GI Tagged: Bastar Iron Craft)",
        "Primary Classification": "Blacksmithing, Wrought Iron Art & Traditional Metallurgy",
        "Confidence Level": "HIGH (Geographical Indications Registry No. 82, Ministry of MSME)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Art of Wrought Iron (Lohe Ka Kaam)")
    doc.add_paragraph(
        "Bastar Iron Craft (GI Application No. 82) is practiced by traditional blacksmiths (Lohars) and ancestral iron smelters (Agariyas). "
        "Without using casting moulds or modern electric welding, the artisans heat scrap iron rods in open charcoal hearths, beating them "
        "by hand with heavy hammers into expressive silhouettes of tribal musicians, deer, peacocks, lamps (Diyas), and the sacred "
        "'Lohe Shikhar' (votive iron tridents and lamp towers consecrated at Devigudi shrines)."
    )
    
    save_document(doc, "30_Bastar_Iron_Craft_and_Lohe_Shikhar.docx")

def build_doc_31():
    doc = create_base_document("31. Bastar Terracotta and Pottery", "Kumhar Votive Offerings, Sacred Elephants, and Khapra Roof Tiles")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-031",
        "Geographic Scope": "Nagarnar, Tokapal, Kondagaon, Kumhrawand",
        "Primary Classification": "Ceramic Heritage, Votive Terracotta & Ethno-Pottery",
        "Confidence Level": "HIGH (Crafts Council of India, Anthropological Survey)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Votive Shrines and Terracotta Offerings")
    doc.add_paragraph(
        "Terracotta in Bastar serves a primarily sacred and votive purpose rather than utilitarian storage. The Kumhar community crafts "
        "majestic multi-tiered terracotta elephants (Hathi), horses (Ghoda), and bulls (Bail) adorned with clay bells and oil lamps. "
        "These are consecrated in sacred groves and Devigudis as substitute sacrificial offerings to appease forest deities and ward off epidemics."
    )
    
    save_document(doc, "31_Bastar_Terracotta_and_Pottery.docx")

def build_doc_32():
    doc = create_base_document("32. Textiles, Clothing, and Adornment", "Kosa Wild Silk, Kotpad Natural Dyes, Aal Tree Extract & Weaving Heritage")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-032",
        "Geographic Scope": "Bastar-Koraput Border (Kotpad), Jagdalpur, Kanker (Kosa Belt)",
        "Primary Classification": "Textile Heritage, Natural Dyes & Weaving Anthropology",
        "Confidence Level": "HIGH (Textile Committee GOI, GI Registry for Kotpad Handloom)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Natural Dye and Handloom Traditions")
    doc.add_paragraph(
        "Bastar's textile heritage spans wild sericulture and organic plant dyeing:\n"
        "• Kosa Silk: Reeled from wild Antheraea mylitta silkworm cocoons harvested from Sal and Asna forest trees.\n"
        "• Kotpad Handloom (GI Certified): Woven by Mirgan weavers on pit looms using unbleached organic cotton yarn dyed with the crushed roots "
        "of the Aal tree (Morinda citrifolia), producing characteristic deep madder red, rusty brown, and chocolate hues with tribal motifs (axes, fish, temples)."
    )
    
    save_document(doc, "32_Textiles_Clothing_and_Adornment.docx")

def build_doc_33():
    doc = create_base_document("33. Tribal Jewellery and Ornaments", "Brass, Silver, Cowrie Shells, Coin Necklaces, and Godna Tattoo Art")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-033",
        "Geographic Scope": "All Indigenous Communities of Bastar",
        "Primary Classification": "Body Adornment, Ethno-Jewellery & Dermatoglyphic Art",
        "Confidence Level": "HIGH (Anthropological Survey of India, National Museum)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Materiality of Body Ornaments")
    doc.add_paragraph(
        "Bastar tribal jewellery reflects ecological adaptation, prestige, and protective apotropaic symbolism:\n"
        "• Hasli & Khagwali: Rigid, heavy silver and bell-metal neck torcs engraved with solar and floral patterns.\n"
        "• Rupiya Mala: Necklaces strung with British Indian silver rupee coins (Victoria, Edward VII, George V) signaling family wealth.\n"
        "• Cowrie Shell Bands: Adorning the forehead and headdresses of Maria dancers.\n"
        "• Godna (Traditional Tattooing): Permanent dermatoglyphic body art administered by specialized Godharin women, serving as indelible "
        "identity markers that accompany the human soul beyond physical death."
    )
    
    save_document(doc, "33_Tribal_Jewellery_and_Ornaments.docx")

def build_doc_34():
    doc = create_base_document("34. Music and Traditional Instruments", "Organology: Mandar, Dhol, Turturi, Mohri, Akum, and Devotional Rhythms")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-034",
        "Geographic Scope": "Bastar Division Ethnomusicological Circuits",
        "Primary Classification": "Ethnomusicology & Traditional Organology",
        "Confidence Level": "HIGH (Sangeet Natak Akademi, Tribal Research Institute)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Organological Classification of Bastar Instruments")
    headers = ["Instrument Name", "Organological Type", "Construction Materials", "Ritual / Performance Context"]
    rows = [
        ["Mandar (Madal)", "Membranophone", "Terracotta or wood barrel, goat/cow hide, iron paste", "Primary rhythm for Muria, Maria, and Halba collective dances"],
        ["Dhol", "Membranophone", "Hollowed wood cylinder, thick bull hide", "Processional drum for Dussehra, Madai fairs, and tiger hunts"],
        ["Turturi (Tutari)", "Aerophone (Trumpet)", "Curved brass tube with flaring bell", "Royal fanfares, deity arrival announcements at Danteshwari temple"],
        ["Mohri (Kohuk)", "Aerophone (Reed)", "Wood body, brass bell, palm-leaf double reed", "Melodic shawm leading all festive processions and marriage ceremonies"],
        ["Akum (Kodu Horn)", "Aerophone", "Curved brass or wild buffalo horn", "War signals, forest assembly calls, and Bhumkal rebellion signaling"],
        ["Gupit / Chikara", "Chordophone (Lute)", "Gourd resonator, bamboo neck, horsehair strings", "Accompaniment for oral ballad recitals and love lyrics in the Ghotul"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "34_Music_and_Traditional_Instruments.docx")

def build_doc_35():
    doc = create_base_document("35. Dance and Performance Traditions", "Gaur Dance, Gedi Acrobatics, Mandari, Kaksar, and Karma")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-035",
        "Geographic Scope": "Bastar Division Performance Landscapes",
        "Primary Classification": "Ethnochoreology & Performance Studies",
        "Confidence Level": "HIGH (Sangeet Natak Akademi, Indira Kala Sangit Vishwavidyalaya Khairagarh)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Living Choreographies of Bastar")
    doc.add_paragraph(
        "Bastar dances are characterized by egalitarian circular choreographies, interlocking arms, and synchronized ground stomping:\n"
        "• Gaur Dance (Bison Horn Dance): Performed by Dandami Maria men wearing towering headdresses of wild bison horns and peacock plumes, "
        "beating massive wooden drums hung from their necks, while women hold iron ringing sticks (Tirududi) in intricate rhythmic counterpoint.\n"
        "• Gedi Dance: Muria youth dance performed on high bamboo stilts with extraordinary acrobatic balance during the monsoon Hareli festival.\n"
        "• Kaksar Dance: Performed by Abujhmaria youth dressed in elaborate brass-belled skirts, seeking the blessings of Kaksar deity for fertility."
    )
    
    save_document(doc, "35_Dance_and_Performance_Traditions.docx")

if __name__ == "__main__":
    print("Building Batch 4: Documents 26 to 35...")
    build_doc_26()
    build_doc_27()
    build_doc_28()
    build_doc_29()
    build_doc_30()
    build_doc_31()
    build_doc_32()
    build_doc_33()
    build_doc_34()
    build_doc_35()
    print("Batch 4 completed successfully.")
