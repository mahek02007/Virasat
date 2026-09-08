import os
from docx.shared import Inches, Pt, RGBColor
from docx_helper import (
    create_base_document, add_metadata_box, add_heading_1, add_heading_2, 
    add_heading_3, add_callout, add_styled_table, save_document
)

def build_doc_48():
    doc = create_base_document("48. Archaeological and Heritage Sites", "Master Registry: Barsur, Narayanpal, Bhairamgarh, Dholkal, and Garhbodh")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-048",
        "Geographic Scope": "Bastar Division Archaeological Sites",
        "Primary Classification": "Archaeological Inventory, Monumental Architecture & Epigraphy",
        "Confidence Level": "HIGH (Archaeological Survey of India & Directorate of Archaeology CG)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Archaeological Site Inventory")
    headers = ["Site Name", "District", "Chronology / Period", "Architectural Highlights & State of Conservation"]
    rows = [
        ["Barsur", "Dantewada", "11th - 13th c. CE (Chhindaka Naga)", "Battisa Temple (twin sanctum on 32 pillars), Chandraditya Temple, Twin Ganesha monoliths, Mama-Bhanja Temple"],
        ["Narayanpal", "Bastar (near Chitrakote)", "1111 CE (Chhindaka Naga)", "Vishnu temple commissioned by Queen Gundamahadevi; fine sandstone sikhara and carved mandapa"],
        ["Dholkal Ganesha", "Dantewada (Bailadila Hills)", "10th - 11th c. CE (Naga period)", "Granite Ganesha monolith perched at 3,000 ft on Bailadila cliff-edge peak; restored after 2017 vandalism"],
        ["Bhairamgarh", "Bijapur", "12th - 13th c. CE (Naga/Kakatiya)", "Remains of ancient stone fort, Bhairava temple, rock-cut moats, and stone inscriptions"],
        ["Garhbodh / Pushkari", "Bastar-Kalahandi border", "4th - 6th c. CE (Nala Dynasty)", "Ancient capital of Nala kings; brick structures, gold coin hoards, Podagadh epigraphs"],
        ["Kuruspal", "Bastar (near Jagdalpur)", "11th - 12th c. CE", "Site of famous Kuruspal inscription of Someshvaradeva I detailing extensive conquest campaigns"]
    ]
    add_styled_table(doc, headers, rows)
    
    save_document(doc, "48_Archaeological_and_Heritage_Sites.docx")

def build_doc_49():
    doc = create_base_document("49. Temples and Religious Sites", "Sacred Architecture: Nagara Shikharas, Phamsana Mandapas, and Tribal Shrines")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-049",
        "Geographic Scope": "Bastar Division Temple Complexes",
        "Primary Classification": "Temple Architecture, Iconography & Religious Heritage",
        "Confidence Level": "HIGH (ASI Raipur Circle, State Protected Monuments)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Stylistic Analysis of Bastar Temple Architecture")
    doc.add_paragraph(
        "Temples in Bastar exhibit a synthesis of Kalinga (Odisha) and Western Chalukyan architectural idioms modified to suit local grey chlorite "
        "and sandstone geology. The typical temple plan features a square Garbha Griha crowned by a stepped Nagara or Phamsana superstructure, "
        "preceded by an open hypostyle pillared Mandapa supported by lathe-turned or square-faceted stone pillars."
    )
    
    save_document(doc, "49_Temples_and_Religious_Sites.docx")

def build_doc_50():
    doc = create_base_document("50. Danteshwari Temple and Dantewada", "The Confluence Citadel: Sanctum Anatomy, Rituals, and Royal Shakta Heritage")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-050",
        "Geographic Scope": "Dantewada Town, Shankini-Dankini River Confluence",
        "Primary Classification": "Sacred Geography, Royal Cult & Epigraphic Temple Study",
        "Confidence Level": "HIGH (Temple Trust Records, ASI Documentation, District Gazetteers)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Sacred Geomorphology of Dantewada")
    doc.add_paragraph(
        "The Danteshwari Temple stands at the exact confluence of two distinct rivers: the Dankini (carrying lighter, clear waters) and "
        "the Shankini (carrying dark, mineral-rich red waters). Consecrated by Annamadeva in 1324 CE, the sanctum enshrines a 14th-century "
        "black chlorite idol of the multi-armed Goddess holding weapons, receiving daily royal Tantric and indigenous tribal offerings."
    )
    
    save_document(doc, "50_Danteshwari_Temple_and_Dantewada.docx")

def build_doc_51():
    doc = create_base_document("51. Barsur Heritage", "The City of 147 Temples and 147 Ponds: Battisa, Chandraditya, and Twin Ganesha")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-051",
        "Geographic Scope": "Barsur Ancient City, Dantewada District",
        "Primary Classification": "Archaeological Monograph & Medieval Urban History",
        "Confidence Level": "HIGH (Archaeological Survey of India Protected Monument Dossier)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. The Medieval Metropolis of Barsur")
    doc.add_paragraph(
        "According to local historical memory and archaeological surveys, medieval Barsur was a sprawling garden city containing 147 stone temples "
        "and 147 excavated water tanks (Pokhars). Masterpieces surviving today include:\n"
        "• Battisa Temple (1208 CE): A unique flat-roofed hypostyle temple supported on 32 elaborately carved stone pillars, housing twin Shiva lingams in twin sanctums.\n"
        "• Chandraditya Temple: Built by Mahamandaleshvara Chandraditya (feudatory of Dharavarsha), facing a large stone-lined stepwell (Kund).\n"
        "• Twin Ganesha Monoliths: Two colossal monolithic Ganesha statues (the larger measuring 3.5 meters in height and 2.5 meters in width), sculpted from single granite boulders.\n"
        "• Mama-Bhanja Temple: A soaring 50-foot Nagara temple built by two master mason relatives, preserving full vertical shikhara geometry."
    )
    
    save_document(doc, "51_Barsur_Heritage.docx")

def build_doc_52():
    doc = create_base_document("52. Chitrakote Waterfalls", "The Niagara of India: Fluvial Dynamics, Indravati Gorge & Eco-Cultural Matrix")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-052",
        "Geographic Scope": "Chitrakote Village, Bastar District (38 km west of Jagdalpur)",
        "Primary Classification": "Fluvial Geomorphology, Natural Monument & Tourism Geography",
        "Confidence Level": "HIGH (Central Water Commission, Geological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Fluvial Dynamics and Horseshoe Canyon")
    doc.add_paragraph(
        "Chitrakote Falls constitutes India's widest waterfall, spanning nearly 300 meters during the peak monsoon season. "
        "The Indravati River plunges 29 meters over a massive horseshoe-shaped escarpment composed of resistant horizontally-bedded "
        "Proterozoic sandstones overlying softer siltstone strata, creating deep plunge pools and turbulent mist cauldrons."
    )
    
    save_document(doc, "52_Chitrakote_Waterfalls.docx")

def build_doc_53():
    doc = create_base_document("53. Tirathgarh Waterfalls", "The Stepped Cascade of Kanger Valley: Geology, Flora & Sacred Shaivite Environs")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-053",
        "Geographic Scope": "Kanger Valley National Park, Bastar District",
        "Primary Classification": "Geomorphology, Forest Hydrology & Eco-Tourism",
        "Confidence Level": "HIGH (Forest Department CG, Geological Survey of India)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Geomorphic Anatomy of Tirathgarh")
    doc.add_paragraph(
        "Tirathgarh Falls is a 91-meter (299-foot) block-stepped cascade formed along the Mugabahar (Kanger) river. The water splits "
        "into multiple foaming rivulets cascading over terraced sandstone ledges surrounded by dense Sal forest. At the base of the waterfall "
        "stands an ancient Shiva shrine where local villagers offer prayers during Maha Shivratri."
    )
    
    save_document(doc, "53_Tirathgarh_Waterfalls.docx")

def build_doc_54():
    doc = create_base_document("54. Kutumsar and Kanger Valley", "Subterranean Speleology, Karst Hydrology & Troglobitic Biological Systems")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-054",
        "Geographic Scope": "Kanger Valley Limestone Karst Belt",
        "Primary Classification": "Speleology, Karst Hydrology & Biospeleology",
        "Confidence Level": "HIGH (Zoological Survey of India, National Speleological Research)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Speleological Exploration and Discovery")
    doc.add_paragraph(
        "Kutumsar Cave was scientifically mapped in the mid-20th century by Dr. Shankar Tiwari. The cave is reached via a narrow vertical shaft "
        "descending 35 meters below the forest floor. Inside, total darkness and constant ambient humidity (~95%) have fostered the evolution "
        "of blind, depigmented troglobites, including the cave loach Nemacheilus exiguus."
    )
    
    save_document(doc, "54_Kutumsar_and_Kanger_Valley.docx")

def build_doc_55():
    doc = create_base_document("55. Kanger Valley National Park", "Ecological Core, Biodiversity Hotspot, Tribal Eco-Development & Management")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-055",
        "Geographic Scope": "Kanger Valley National Park (200 sq km)",
        "Primary Classification": "Conservation Biology & Protected Area Management",
        "Confidence Level": "HIGH (Management Plan KVNP, Chhattisgarh Forest Department)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Ecological Significance and Management Zones")
    doc.add_paragraph(
        "Declared a National Park in 1982, Kanger Valley encompasses 200 sq km of unbroken moist deciduous Sal-Teak mixed canopy. "
        "The park is managed in participatory partnership with local Dhurwa and Gond Eco-Development Committees (EDCs), providing sustainable "
        "community-guided nature walks, cave tours, and homestay hospitality while safeguarding the critical habitat of the Bastar Hill Myna."
    )
    
    save_document(doc, "55_Kanger_Valley_National_Park.docx")

def build_doc_56():
    doc = create_base_document("56. Bastar Palace and Royal Heritage", "Jagdalpur Royal Residence: Architecture, Durbar Hall, Armory & Historical Memory")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-056",
        "Geographic Scope": "Jagdalpur Royal Compound, Bastar District",
        "Primary Classification": "Palace Architecture, Royal Material Culture & Political History",
        "Confidence Level": "HIGH (Royal Trust Records, CP Gazetteers, State Archives)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Architectural Features and Historical Legacy")
    doc.add_paragraph(
        "The Bastar Palace at Jagdalpur was constructed by the Kakatiya rulers following the shift of the capital in 1777 CE and renovated "
        "by Maharaja Rudra Pratap Deo in the early 20th century. The palace exhibits a blend of traditional Rajput-Maratha arches with European "
        "colonial colonial verandas and high ceilings. Key sections include the Durbar Hall (where Dussehra tribal councils are convened), "
        "the Royal Danteshwari temple, and the private royal armory containing ancient matchlocks, curved swords, and tribal battle axes."
    )
    
    save_document(doc, "56_Bastar_Palace_and_Royal_Heritage.docx")

def build_doc_57():
    doc = create_base_document("57. Jagdalpur and Cultural Capital Context", "Urban History, Dalpat Sagar Lake, Haats, and Regional Gateway")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-057",
        "Geographic Scope": "Jagdalpur Municipal Area & Urban Fringe",
        "Primary Classification": "Urban Geography, Cultural Planning & Regional Economics",
        "Confidence Level": "HIGH (Jagdalpur Municipal Corporation, Town & Country Planning CG)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Urban Evolution of Jagdalpur")
    doc.add_paragraph(
        "Founded as 'Jagattuguda' on the southern bank of the Indravati River, Jagdalpur was systematically planned around Dalpat Sagar—a massive "
        "man-made rainwater lake spanning over 350 hectares constructed by Maharaja Dalpat Deva in the 18th century. Today, Jagdalpur functions "
        "as the administrative, educational, commercial, and transportation nucleus of the entire Bastar division."
    )
    
    save_document(doc, "57_Jagdalpur_and_Cultural_Capital_Context.docx")

def build_doc_58():
    doc = create_base_document("58. Bastar Villages and Rural Heritage", "Settlement Topography, Para/Tola Spatial Morphology, Architecture & Community Spaces")
    add_metadata_box(doc, {
        "Document ID": "BST-DOC-058",
        "Geographic Scope": "Rural Bastar Settlements (Muria, Maria, Dhurwa, Halba Villages)",
        "Primary Classification": "Rural Sociology, Vernacular Architecture & Settlement Geography",
        "Confidence Level": "HIGH (Anthropological Survey of India, Field Ethnographies)",
        "Last Verified Date": "2026-09-07"
    })
    
    add_heading_1(doc, "1. Settlement Topography and Hamlet Morphology")
    doc.add_paragraph(
        "Unlike clustered villages of northern India, a Bastar tribal village is dispersed across distinct clan hamlets called 'Paras' or 'Tolas', "
        "interspersed with agricultural fields and forest patches. Each household compound is enclosed by a living fence of bamboo or timber posts, "
        "containing a mud-plastered dwelling, a cattle shed (Kotha), a grain storage platform, and a private kitchen garden (Bari)."
    )
    
    save_document(doc, "58_Bastar_Villages_and_Rural_Heritage.docx")

if __name__ == "__main__":
    print("Building Batch 6: Documents 48 to 58...")
    build_doc_48()
    build_doc_49()
    build_doc_50()
    build_doc_51()
    build_doc_52()
    build_doc_53()
    build_doc_54()
    build_doc_55()
    build_doc_56()
    build_doc_57()
    build_doc_58()
    print("Batch 6 completed successfully.")
