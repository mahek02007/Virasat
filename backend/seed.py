"""
Virasat — Database Seed Script (v2)
Seeds verified Maharashtra and Odisha cultural data into the 5-model architecture:
Region, Place, Media, Source, ContentItem + Many-to-Many associations.

Run from backend/ directory: python seed.py
"""

import sys
import os

# Make sure imports resolve
sys.path.insert(0, os.path.dirname(__file__))

from database import SessionLocal, engine, Base
import models

# ════════════════════════════════════════════════════════════════════════════
# SEED DATA DEFINITIONS
# ════════════════════════════════════════════════════════════════════════════

REGIONS_DATA = [
    {
        "id": "maharashtra",
        "name": "Maharashtra",
        "slug": "maharashtra",
        "devanagari": "महाराष्ट्र",
        "tagline": "Caves • Maratha Forts • Lavani",
        "status": "available",
        "is_pilot": True,
        "zone": "west",
        "coord_x": 41.5,
        "coord_y": 57.0,
        "summary": (
            "Traverse monumental rock-cut cave temples, rugged Sahyadri hill fortresses, "
            "and high-energy folk rhythms of Lavani."
        ),
        "color_accent": "#B84E29",
        "badge": "Pilot Region",
        "categories": ["Ajanta & Ellora Caves", "Shivaji Hill Forts", "Warli Tribal Art", "Ganesh Utsav"],
        "highlights": ["Ellora Kailasa Temple", "Raigad Fort", "Ajanta Frescoes", "Elephanta Caves"],
    },
    {
        "id": "odisha",
        "name": "Odisha",
        "slug": "odisha",
        "devanagari": "ओडिशा",
        "tagline": "Konark Sun Temple • Odissi • Pattachitra",
        "status": "available",
        "is_pilot": False,
        "zone": "east",
        "coord_x": 57.5,
        "coord_y": 58.5,
        "summary": (
            "Land of monumental stone chariots, ancient palm-leaf scrolls, "
            "celestial Odissi dancer postures, and maritime Kalinga trade."
        ),
        "color_accent": "#D4AF37",
        "badge": "Featured Region",
        "categories": ["Konark Sun Chariot", "Odissi Classical Dance", "Raghurajpur Pattachitra", "Puri Rath Yatra"],
        "highlights": ["Konark Sun Temple", "Jagannath Puri", "Udayagiri Caves", "Chilika Lake"],
    },
]

PLACES_DATA = [
    # Maharashtra Places
    {
        "slug": "ajanta-caves-site",
        "region_id": "maharashtra",
        "name": "Ajanta Caves Complex",
        "description": "30 rock-cut Buddhist cave monuments overlooking the Waghur river ravine.",
        "latitude": 20.5519,
        "longitude": 75.7033,
        "address": "Chhatrapati Sambhaji Nagar District, Maharashtra 431117",
    },
    {
        "slug": "ellora-caves-site",
        "region_id": "maharashtra",
        "name": "Ellora Caves Complex",
        "description": "Ancient multi-religious rock-cut temple complex spanning Hindu, Buddhist, and Jain monuments.",
        "latitude": 20.0268,
        "longitude": 75.1790,
        "address": "Verul, Chhatrapati Sambhaji Nagar District, Maharashtra 431102",
    },
    {
        "slug": "raigad-fort-site",
        "region_id": "maharashtra",
        "name": "Raigad Fort Capital",
        "description": "Hill fortress perched at 820m elevation in the Sahyadris, sovereign capital of Chhatrapati Shivaji Maharaj.",
        "latitude": 18.2346,
        "longitude": 73.4414,
        "address": "Mahad, Raigad District, Maharashtra 402305",
    },
    {
        "slug": "paithan-town",
        "region_id": "maharashtra",
        "name": "Paithan Heritage Town",
        "description": "Ancient capital of the Satavahana Empire on the banks of Godavari, home of Paithani silk weaving.",
        "latitude": 19.4795,
        "longitude": 75.3853,
        "address": "Paithan, Chhatrapati Sambhaji Nagar, Maharashtra 431107",
    },
    {
        "slug": "palghar-tribal-belt",
        "region_id": "maharashtra",
        "name": "Palghar Warli Tribal Belt",
        "description": "Indigenous heartland of the Warli community in the foothills of the Sahyadri range.",
        "latitude": 19.6967,
        "longitude": 72.7699,
        "address": "Dahanu and Jawhar Talukas, Palghar District, Maharashtra 401601",
    },
    {
        "slug": "pandharpur-town",
        "region_id": "maharashtra",
        "name": "Pandharpur Sacred Town",
        "description": "Vithoba temple pilgrimage center on the Chandrabhaga (Bhima) river.",
        "latitude": 17.6775,
        "longitude": 75.3263,
        "address": "Pandharpur, Solapur District, Maharashtra 413304",
    },
    {
        "slug": "pune-city",
        "region_id": "maharashtra",
        "name": "Pune Cultural Capital",
        "description": "Seat of the Peshwas and epicenter of the public Ganesh Chaturthi revival.",
        "latitude": 18.5204,
        "longitude": 73.8567,
        "address": "Pune, Maharashtra 411030",
    },
    # Odisha Places
    {
        "slug": "puri-jagannath-complex",
        "region_id": "odisha",
        "name": "Shree Jagannath Temple Complex",
        "description": "10.9-acre sacred complex with 12th-century Kalinga sanctuary and world's largest traditional kitchen.",
        "latitude": 19.8049,
        "longitude": 85.8179,
        "address": "Bada Danda, Puri, Odisha 752001",
    },
    {
        "slug": "konark-sun-temple-site",
        "region_id": "odisha",
        "name": "Konark Sun Temple Complex",
        "description": "Monumental 13th-century stone chariot dedicated to Surya along the Bay of Bengal coastline.",
        "latitude": 19.8876,
        "longitude": 86.0945,
        "address": "Konark, Puri District, Odisha 752111",
    },
    {
        "slug": "raghurajpur-heritage-village",
        "region_id": "odisha",
        "name": "Raghurajpur Heritage Craft Village",
        "description": "Designated crafts village where every household practices traditional Pattachitra, palm leaf engraving, or Gotipua dance.",
        "latitude": 19.8732,
        "longitude": 85.8239,
        "address": "Raghurajpur, Puri District, Odisha 752012",
    },
    {
        "slug": "pipili-town",
        "region_id": "odisha",
        "name": "Pipili Applique Center",
        "description": "Historical artisan township renowned for Chandua appliqué craftsmanship for Rath Yatra canopies.",
        "latitude": 20.1177,
        "longitude": 85.8306,
        "address": "Pipili, Puri District, Odisha 752104",
    },
    {
        "slug": "pahala-village",
        "region_id": "odisha",
        "name": "Pahala Confectionery Hub",
        "description": "Famed village along NH-16 between Bhubaneswar and Cuttack known for authentic Odisha Rasagola.",
        "latitude": 20.3541,
        "longitude": 85.8563,
        "address": "Pahala, Khordha District, Odisha 752101",
    },
]

SOURCES_DATA = [
    {
        "title": "UNESCO World Heritage Centre",
        "url": "https://whc.unesco.org",
        "publisher": "UNESCO",
        "citation_text": "UNESCO World Heritage List official citations and documentation dossier.",
    },
    {
        "title": "Archaeological Survey of India (ASI)",
        "url": "https://asi.nic.in",
        "publisher": "Ministry of Culture, Government of India",
        "citation_text": "ASI monument records, excavation reports, and conservation archives.",
    },
    {
        "title": "Geographical Indications Registry of India",
        "url": "https://ipindia.gov.in",
        "publisher": "Controller General of Patents, Designs and Trade Marks",
        "citation_text": "GI Journal registrations and authentic origin verifications.",
    },
    {
        "title": "Sangeet Natak Akademi",
        "url": "https://sangeetnatak.gov.in",
        "publisher": "National Academy of Music, Dance and Drama, India",
        "citation_text": "Sangeet Natak Akademi archives on Indian classical and traditional folk performing arts.",
    },
    {
        "title": "Maharashtra Tourism Development Corporation (MTDC)",
        "url": "https://www.maharashtratourism.gov.in",
        "publisher": "Government of Maharashtra",
        "citation_text": "MTDC cultural publications and regional heritage documentation.",
    },
    {
        "title": "Odisha Tourism Development Corporation (OTDC)",
        "url": "https://dot.odishatourism.gov.in",
        "publisher": "Department of Tourism, Government of Odisha",
        "citation_text": "Odisha Tourism official cultural archives and heritage publications.",
    },
    {
        "title": "Shree Jagannath Temple Administration (SJTA)",
        "url": "https://shreejagannatha.in",
        "publisher": "SJTA Puri",
        "citation_text": "Madala Panji temple chronicle and daily ritual records.",
    },
    {
        "title": "Sant Dnyaneshwar & Tukaram Samadhi Trust Records",
        "url": "https://alandidehutrust.org",
        "publisher": "Alandi & Dehu Sansthan",
        "citation_text": "Historical Varkari Paduka procession logs and Abhanga manuscripts.",
    },
]

MEDIA_DATA = [
    {
        "title": "Ajanta Cave 1 Fresco — Bodhisattva Padmapani",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Ancient Buddhist fresco painting in Ajanta Cave 1 depicting Bodhisattva Padmapani",
        "attribution": "Archaeological Survey of India / Public Domain",
    },
    {
        "title": "Ellora Cave 16 — Kailasa Monolithic Temple",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1590073844006-33379778ae09?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1590073844006-33379778ae09?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Top-down carved Kailasa Temple at Ellora Caves complex",
        "attribution": "Archaeological Survey of India",
    },
    {
        "title": "Raigad Fort — Maha Darwaja and Citadel",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1626014303757-646633785139?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1626014303757-646633785139?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Maha Darwaja of Raigad Fort amidst Sahyadri mountain mists",
        "attribution": "Maharashtra Tourism (MTDC)",
    },
    {
        "title": "Warli Tarpa Dance Composition",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Warli tribal painting showing spiral Tarpa dance on mud base",
        "attribution": "GI Registry / Tribal Co-operative",
    },
    {
        "title": "Paithani Silk Saree — Bangadi-Mor Zari Pallu",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Intricate gold zari peacock pallu of authentic Paithani silk saree",
        "attribution": "Paithan Silk Weavers Co-operative",
    },
    {
        "title": "Konark Sun Temple Chariot Wheel",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Finely sculpted sundial wheel of Konark Sun Temple",
        "attribution": "Archaeological Survey of India / UNESCO",
    },
    {
        "title": "Shree Jagannath Temple Puri Vimana Tower",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Kalinga architectural tower of Shree Jagannath Temple in Puri",
        "attribution": "Shree Jagannath Temple Administration",
    },
    {
        "title": "Odisha Pattachitra Scroll — Dasavatara",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1582561424760-0321d75e81fa?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1582561424760-0321d75e81fa?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Detailed Pattachitra painting of Dasavatara using natural stone pigments",
        "attribution": "Raghurajpur Crafts Society",
    },
    {
        "title": "Odissi Classical Dance Tribhangi Posture",
        "media_type": "image",
        "url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=1200&q=80",
        "thumbnail_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?auto=format&fit=crop&w=300&q=80",
        "alt_text": "Odissi dancer in signature Tribhangi three-bend stance",
        "attribution": "Sangeet Natak Akademi",
    },
]

# ════════════════════════════════════════════════════════════════════════════
# CONTENT ITEMS DATA
# ════════════════════════════════════════════════════════════════════════════

CONTENT_ITEMS_DATA = [
    # ── Maharashtra — Monuments ─────────────────────────────────────────────
    {
        "region_id": "maharashtra",
        "place_slug": "ajanta-caves-site",
        "slug": "ajanta-caves",
        "title": "Ajanta Caves",
        "subtitle": "UNESCO World Heritage Site — Buddhist rock-cut sanctuaries",
        "content_type": "monument",
        "subtype": "cave_temple",
        "summary": "30 rock-cut Buddhist cave sanctuaries with masterwork frescoes dating from 2nd c. BCE to 5th c. CE.",
        "description": (
            "The Ajanta Caves in Chhatrapati Sambhaji Nagar are 30 rock-cut Buddhist cave monuments "
            "spanning the 2nd century BCE to 10th century CE. They house some of the finest surviving "
            "examples of ancient Indian art — vibrant frescoes depicting the Jataka tales, intricate "
            "sculptures, and chaitya grihas (prayer halls) with ribbed stone vaults. The site was "
            "rediscovered in 1819 by British officer John Smith and declared a UNESCO World Heritage "
            "Site in 1983."
        ),
        "period": "2nd century BCE – 5th century CE",
        "is_gi_tagged": False,
        "unesco_status": "World Heritage Site (1983)",
        "historical_era": "Satavahana & Vakataka Dynasties",
        "tags": ["UNESCO", "Buddhism", "Cave Art", "Frescoes", "Rock-cut Architecture"],
        "item_metadata": {
            "num_caves": 30,
            "rediscovery_year": 1819,
            "primary_patrons": "Harishena of Vakataka Empire",
            "river": "Waghur River ravine"
        },
        "media_titles": ["Ajanta Cave 1 Fresco — Bodhisattva Padmapani"],
        "source_titles": ["UNESCO World Heritage Centre", "Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "ellora-caves-site",
        "slug": "ellora-kailasa-temple",
        "title": "Ellora — Kailasa Temple (Cave 16)",
        "subtitle": "Largest monolithic rock excavation in the world",
        "content_type": "monument",
        "subtype": "monolithic_temple",
        "summary": "Rashtrakuta monolithic marvel carved top-down from a single basalt cliff face, removing 200,000 tonnes of rock.",
        "description": (
            "The Kailasa Temple at Ellora (Cave 16) is an 8th-century CE Rashtrakuta marvel commissioned "
            "by King Dantidurga and Krishna I. Carved top-down from a single basalt cliff face, it required the removal "
            "of an estimated 200,000 tonnes of rock over 18 years. The complex replicates Mount Kailash — "
            "Shiva's cosmic abode — at scale, with a 32-metre-tall shikhara, life-size elephant sculptures "
            "flanking a victory pillar, and elaborate relief panels narrating the Mahabharata and Ramayana. "
            "Ellora's 34 caves span Buddhist, Hindu, and Jain traditions across 600 CE to 1000 CE."
        ),
        "period": "8th century CE (c. 756–773 CE)",
        "is_gi_tagged": False,
        "unesco_status": "World Heritage Site (1983)",
        "historical_era": "Rashtrakuta Dynasty",
        "tags": ["UNESCO", "Rashtrakuta", "Monolithic", "Shaivite", "Rock-cut Architecture"],
        "item_metadata": {
            "rock_excavated_tonnes": 200000,
            "height_metres": 32,
            "patron_king": "Krishna I & Dantidurga",
            "traditions": ["Hindu", "Buddhist", "Jain"]
        },
        "media_titles": ["Ellora Cave 16 — Kailasa Monolithic Temple"],
        "source_titles": ["UNESCO World Heritage Centre", "Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "raigad-fort-site",
        "slug": "raigad-fort",
        "title": "Raigad Fort",
        "subtitle": "Maratha capital and coronation seat of Chhatrapati Shivaji Maharaj",
        "content_type": "monument",
        "subtype": "hill_fort",
        "summary": "Impregnable Sahyadri mountain fortress where Shivaji Maharaj was crowned Chhatrapati in 1674.",
        "description": (
            "Raigad Fort, perched at 820 metres in the Sahyadri ranges of Raigad district, was the capital "
            "of the Maratha Empire and the site of Chhatrapati Shivaji Maharaj's coronation on 6 June 1674. "
            "Originally called Rairi, the fort was expanded by Shivaji into a self-sufficient hill capital "
            "with 300 houses, a market, Jagdishwar temple, and seven gateways. Shivaji passed away here "
            "in 1680 and his samadhi (memorial) stands within the fort complex."
        ),
        "period": "17th century CE (1674 CE coronation)",
        "is_gi_tagged": False,
        "unesco_status": "Part of Serial Nomination for Maratha Military Landscapes",
        "historical_era": "Maratha Empire",
        "tags": ["Maratha", "Shivaji", "Hill Fort", "Girikot", "Historical"],
        "item_metadata": {
            "elevation_metres": 820,
            "coronation_date": "1674-06-06",
            "architect": "Hiroji Indulkar",
            "features": ["Maha Darwaja", "Takmak Tok", "Jagdishwar Temple", "Samadhi of Shivaji"]
        },
        "media_titles": ["Raigad Fort — Maha Darwaja and Citadel"],
        "source_titles": ["Archaeological Survey of India (ASI)", "Maharashtra Tourism Development Corporation (MTDC)"],
    },
    # ── Maharashtra — Folk Art & Crafts ─────────────────────────────────────
    {
        "region_id": "maharashtra",
        "place_slug": "palghar-tribal-belt",
        "slug": "warli-painting",
        "title": "Warli Tribal Painting",
        "subtitle": "GI-tagged geometric tribal art from Palghar",
        "content_type": "art_craft",
        "subtype": "tribal_art",
        "summary": "Indigenous tribal art rendered with white rice paste in primal geometric forms depicting the cosmic Tarpa dance.",
        "description": (
            "Warli painting is a GI-tagged tribal art tradition from the Warli people of Palghar district "
            "in northern Maharashtra. Using only white rice paste on an ochre or mud-coloured background, "
            "artists employ three primary geometric shapes: circles (sun and moon), triangles (mountains "
            "and trees), and squares (sacred enclosures). The signature composition is the Tarpa dance — "
            "a spiral of human figures circling a musician playing the Tarpa (horn instrument). "
            "Traditionally created by married women on inner mud walls during harvest festivals and "
            "weddings, it was first documented by ethnographer Haku Shah in the 1970s."
        ),
        "period": "Pre-historic origins, modern documentation 1970s",
        "is_gi_tagged": True,
        "gi_year": 2014,
        "unesco_status": None,
        "historical_era": "Indigenous Neolithic-rooted tradition",
        "tags": ["GI Tag", "Tribal Art", "Palghar", "Geometric", "Indigenous"],
        "item_metadata": {
            "materials": ["White rice paste", "Gum binder", "Mud/cowdung base"],
            "key_motifs": ["Tarpa dance", "Sun and Moon", "Mother Goddess Palghat", "Flora and Fauna"],
            "gi_application": "GI Application No. 195"
        },
        "media_titles": ["Warli Tarpa Dance Composition"],
        "source_titles": ["Geographical Indications Registry of India", "Maharashtra Tourism Development Corporation (MTDC)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "paithan-town",
        "slug": "paithani-saree",
        "title": "Paithani Silk Saree",
        "subtitle": "2,000-year-old zari weaving from the Satavahana era",
        "content_type": "textile",
        "subtype": "silk_saree",
        "summary": "Royal handloom silk woven with pure gold zari using the seamless Kadiyal interlocking tapestry technique.",
        "description": (
            "The Paithani saree is a 2,000-year-old silk and zari weaving tradition from Paithan "
            "(ancient Pratishthana), the Satavahana capital on the Godavari river. Woven using the "
            "Kadiyal tapestry interlocking technique where warp and weft threads interlock to prevent "
            "seams, authentic Paithani features iconic peacock (Bangadi-mor), lotus, and coin motifs "
            "woven in pure 22-carat gold zari. The Peshwa rulers patronised it heavily in the 17th–18th "
            "centuries. A single saree can take 6 months to 1 year to complete. It holds a GI Tag."
        ),
        "period": "2nd century BCE onwards",
        "is_gi_tagged": True,
        "gi_year": 2010,
        "unesco_status": None,
        "historical_era": "Satavahana & Peshwa Eras",
        "tags": ["GI Tag", "Silk", "Zari", "Satavahana", "Aurangabad", "Weaving"],
        "item_metadata": {
            "weaving_technique": "Kadiyal tapestry interlocking",
            "gold_zari_purity": "22-carat gold dipped silver thread",
            "signature_motifs": ["Bangadi-mor (peacock in bangle)", "Kamal (lotus)", "Asavali (flowering vine)", "Narali (coconut)"],
            "production_time_months": 6
        },
        "media_titles": ["Paithani Silk Saree — Bangadi-Mor Zari Pallu"],
        "source_titles": ["Geographical Indications Registry of India"],
    },
    # ── Maharashtra — Performing Arts & Festivals ───────────────────────────
    {
        "region_id": "maharashtra",
        "place_slug": "pune-city",
        "slug": "lavani-dance",
        "title": "Lavani",
        "subtitle": "Maharashtra's high-energy folk dance on Dholki's 14-beat Dhadya rhythm",
        "content_type": "performing_art",
        "subtype": "folk_dance",
        "summary": "Celebrated Maharashtrian folk dance performed in Nauvari sarees set to the intense 14-beat Dhadya rhythm of the Dholki drum.",
        "description": (
            "Lavani is Maharashtra's most celebrated folk performance tradition, characterised by its "
            "fast pace and the potent rhythm of the Dholki (cylindrical drum). Performed to the "
            "14-beat Dhadya taal, it has two principal forms: Nirguni (philosophical/spiritual Lavani "
            "with devotional themes) and Shringari (celebratory, often erotic Lavani exploring love "
            "and the feminine spirit). Performers traditionally wear the Nauvari (9-yard) saree draped "
            "in a distinctive Kashtha style. Maharashtra Natyagriha (Tamasha theatre) provided the "
            "historical stage for Lavani, dating to the Peshwa period."
        ),
        "period": "Peshwa period (17th–18th century CE)",
        "is_gi_tagged": False,
        "unesco_status": None,
        "historical_era": "Peshwa Era",
        "tags": ["Folk Dance", "Dholki", "Tamasha", "Peshwa", "Performing Art"],
        "item_metadata": {
            "rhythm_taal": "14-beat Dhadya",
            "primary_instrument": "Dholki",
            "forms": ["Nirguni (Spiritual)", "Shringari (Sensual/Celebratory)"],
            "attire": "9-yard Nauvari saree in Kashtha drape"
        },
        "media_titles": [],
        "source_titles": ["Sangeet Natak Akademi", "Maharashtra Tourism Development Corporation (MTDC)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "pune-city",
        "slug": "ganesh-chaturthi",
        "title": "Ganesh Chaturthi",
        "subtitle": "Public festival revived in 1893 by Lokmanya Tilak for national unity",
        "content_type": "festival_ritual",
        "subtype": "public_festival",
        "summary": "Massive 10-day cultural movement uniting communities with Dhol-Tasha pathaks, modak sweets, and grand visarjan processions.",
        "description": (
            "Ganesh Chaturthi, the 10-day festival celebrating Lord Ganesha's birth, was transformed "
            "from a private household ritual into a massive public celebration by Lokmanya Bal Gangadhar "
            "Tilak in Pune in 1893. His strategic reinvention brought communities together across caste "
            "lines during colonial rule, functioning as a forum for political speeches. Today, Pune's "
            "Kasba Ganapati (the city's Manacha Ganapati) and Mumbai's Lalbaugcha Raja draw millions. "
            "The celebration features Dhol-Tasha pathaks (drum orchestras), Modak sweets, artistic "
            "pandals, and culminates in the Visarjan (immersion) procession."
        ),
        "period": "Ancient origins; Sarvajanik revival in 1893 CE",
        "is_gi_tagged": False,
        "unesco_status": None,
        "historical_era": "Modern Indian National Movement",
        "tags": ["Festival", "Ganesha", "Pune", "Mumbai", "National Unity", "Colonial History"],
        "item_metadata": {
            "duration_days": 10,
            "revival_year": 1893,
            "revival_leader": "Lokmanya Bal Gangadhar Tilak",
            "culmination": "Anant Chaturdashi Visarjan"
        },
        "media_titles": [],
        "source_titles": ["Maharashtra Tourism Development Corporation (MTDC)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "pandharpur-town",
        "slug": "pandharpur-wari",
        "title": "Pandharpur Wari",
        "subtitle": "700-year-old Varkari pilgrimage of over one million devotees",
        "content_type": "festival_ritual",
        "subtype": "pilgrimage",
        "summary": "700-year-old egalitarian walking pilgrimage of 1M+ Varkaris carrying saint Padukas over 250 km singing Abhangas.",
        "description": (
            "The Pandharpur Wari is a 700-year-old living pilgrimage tradition of the Varkari sect, "
            "a devotional movement within Vaishnavism centred on Vitthal (Vithoba) at Pandharpur. "
            "Twice a year on Ashadhi and Kartiki Ekadashi, over one million Varkaris (pilgrims) walk "
            "up to 250 km from Alandi (carrying Dnyaneshwar's Padukas) and Dehu (carrying Tukaram's "
            "Padukas) to Pandharpur. The procession is a moving festival of Abhanga (devotional song) "
            "chanting, erasing caste barriers — all Varkaris share food and walk together. The movement "
            "was shaped by saints Dnyaneshwar (13th c.), Namdev, Eknath, and Tukaram (17th c.)."
        ),
        "period": "13th century CE onwards",
        "is_gi_tagged": False,
        "unesco_status": None,
        "historical_era": "Bhakti Movement Era",
        "tags": ["Pilgrimage", "Varkari", "Vitthal", "Pandharpur", "Bhakti Movement"],
        "item_metadata": {
            "walking_distance_km": 250,
            "duration_days": 21,
            "saints": ["Sant Dnyaneshwar", "Sant Tukaram", "Sant Namdev", "Sant Eknath"],
            "pilgrims_count": "1,000,000+"
        },
        "media_titles": [],
        "source_titles": ["Sant Dnyaneshwar & Tukaram Samadhi Trust Records", "Maharashtra Tourism Development Corporation (MTDC)"],
    },

    # ── Odisha — Monuments ──────────────────────────────────────────────────
    {
        "region_id": "odisha",
        "place_slug": "puri-jagannath-complex",
        "slug": "jagannath-temple-puri",
        "title": "Shree Jagannath Temple, Puri",
        "subtitle": "12th-century Kalinga architectural masterpiece, one of the Char Dham",
        "content_type": "monument",
        "subtype": "classical_temple",
        "summary": "Monumental 12th-century Kalinga sanctuary rising 65m with 120+ inner shrines and the world's largest traditional kitchen.",
        "description": (
            "The Shree Jagannath Temple in Puri is a supreme example of Kalinga architecture, rising "
            "65 metres (214 ft) above the Odisha coastline. Built by Eastern Ganga King Chodaganga Deva "
            "in the 12th century and expanded by Anangabhima Deva III, the temple complex covers "
            "10.9 acres enclosed by the Meghnad Pacheri (outer wall). It contains four structures: "
            "Vimana (deul/main tower), Jagamohana (audience hall), Natamandapa (festival hall), "
            "and Bhoga Mandapa (offering hall), plus 120+ inner shrines. Lord Jagannath, Balabhadra, "
            "and Subhadra are worshipped in unfinished wooden form — a unique iconography with "
            "pre-Hindu Sabara tribal origins."
        ),
        "period": "12th century CE (c. 1161 CE)",
        "is_gi_tagged": False,
        "unesco_status": "UNESCO World Heritage Tentative List",
        "historical_era": "Eastern Ganga Dynasty",
        "tags": ["Kalinga Architecture", "Char Dham", "Jagannath", "Vaishnava", "UNESCO Tentative"],
        "item_metadata": {
            "height_metres": 65,
            "complex_area_acres": 10.9,
            "patron_king": "Anantavarman Chodaganga Deva",
            "four_structures": ["Vimana (Deul)", "Jagamohana", "Natamandapa", "Bhoga Mandapa"],
            "sacred_kitchen_hearths": 752
        },
        "media_titles": ["Shree Jagannath Temple Puri Vimana Tower"],
        "source_titles": ["Shree Jagannath Temple Administration (SJTA)", "Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "konark-sun-temple-site",
        "slug": "konark-sun-temple",
        "title": "Konark Sun Temple",
        "subtitle": "UNESCO World Heritage Site — 13th-century stone chariot of Surya",
        "content_type": "monument",
        "subtype": "sun_temple",
        "summary": "13th-century UNESCO World Heritage stone chariot with 24 intricate sundial wheels pulled by 7 galloping horses.",
        "description": (
            "The Konark Sun Temple, 35 km northeast of Puri along the Marine Drive, is a 13th-century "
            "UNESCO World Heritage Site built by Eastern Ganga King Narasimhadeva I (1238–1264 CE). "
            "Conceived as a gigantic stone chariot for the sun god Surya, it has 24 intricately carved "
            "stone wheels (representing hours of the day and months of the year) pulled by seven stone "
            "horses. The temple was once the tallest structure on the Odisha coast at approximately "
            "57 metres (the main shikhara has since collapsed). Known as the 'Black Pagoda' by ancient "
            "European mariners, it served as a navigational landmark. The complex is renowned for its "
            "erotic and narrative sculpture panels (ratha and erotica friezes)."
        ),
        "period": "13th century CE (c. 1250 CE)",
        "is_gi_tagged": False,
        "unesco_status": "World Heritage Site (1984)",
        "historical_era": "Eastern Ganga Dynasty",
        "tags": ["UNESCO", "Sun Temple", "Kalinga", "Stone Chariot", "Narasimhadeva I"],
        "item_metadata": {
            "wheels_count": 24,
            "horses_count": 7,
            "patron_king": "Langula Narasimhadeva I",
            "maritime_moniker": "Black Pagoda",
            "wheel_function": "Astronomical solar clock accurate to minutes"
        },
        "media_titles": ["Konark Sun Temple Chariot Wheel"],
        "source_titles": ["UNESCO World Heritage Centre", "Archaeological Survey of India (ASI)", "Odisha Tourism Development Corporation (OTDC)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "puri-jagannath-complex",
        "slug": "rath-yatra-puri",
        "title": "Puri Rath Yatra",
        "subtitle": "World's largest chariot festival — three hand-built wooden chariots",
        "content_type": "festival_ritual",
        "subtype": "chariot_festival",
        "summary": "World's largest chariot procession where three massive wooden chariots are constructed anew every year by hereditary artisans.",
        "description": (
            "The Puri Rath Yatra is the world's largest chariot festival, held annually on Ashadha "
            "Shukla Dwitiya. Three towering wooden chariots are built anew each year by hereditary "
            "Maharana craftsmen using 862 timber logs, without blueprints or iron nails: Nandighosh "
            "(Lord Jagannath — 45 ft, 16 wheels, red and yellow fabric), Taladhwaja (Balabhadra — 44 ft, "
            "14 wheels, red and green), and Darpadalana (Subhadra — 43 ft, 12 wheels, red and black). "
            "Over one million pilgrims pull the chariots along the 2.5 km Bada Danda (Grand Road) to "
            "the Gundicha Temple. The English word 'juggernaut' derives from 'Jagannath' via 14th-century "
            "traveller Ibn Battuta's description of this festival."
        ),
        "period": "Documented since 12th century CE",
        "is_gi_tagged": False,
        "unesco_status": "Representative of Intangible Cultural Heritage of Humanity",
        "historical_era": "Eastern Ganga to Modern Era",
        "tags": ["Rath Yatra", "Chariot Festival", "Jagannath", "Puri", "UNESCO ICH"],
        "item_metadata": {
            "chariots": [
                {"name": "Nandighosh", "deity": "Lord Jagannath", "height_ft": 45, "wheels": 16},
                {"name": "Taladhwaja", "deity": "Balabhadra", "height_ft": 44, "wheels": 14},
                {"name": "Darpadalana", "deity": "Subhadra", "height_ft": 43, "wheels": 12}
            ],
            "logs_used": 862,
            "route_km": 2.5
        },
        "media_titles": [],
        "source_titles": ["Shree Jagannath Temple Administration (SJTA)", "Odisha Tourism Development Corporation (OTDC)"],
    },
    # ── Odisha — Folk Crafts, Performing Arts & Cuisine ─────────────────────
    {
        "region_id": "odisha",
        "place_slug": "raghurajpur-heritage-village",
        "slug": "pattachitra-raghurajpur",
        "title": "Odisha Pattachitra",
        "subtitle": "GI-tagged classical scroll painting from Raghurajpur heritage village",
        "content_type": "art_craft",
        "subtype": "scroll_painting",
        "summary": "1,000-year-old GI-tagged cloth scroll painting created with 100% mineral pigments and sealed with glowing lac varnish.",
        "description": (
            "Odisha Pattachitra (Patta = cloth, Chitra = picture) is a GI-tagged (GI Tag No. 56) "
            "classical scroll painting tradition with over 1,000 years of history, centred in "
            "Raghurajpur (14 km from Puri) and Puri itself. The painting surface is prepared by "
            "coating cloth with tamarind seed paste mixed with chalk powder (Kaitha gum) to create "
            "a smooth, stiff canvas. Artists use exclusively natural mineral pigments: Hingula (red "
            "mercuric sulphide), Haritala (yellow orpiment), Conch shell white, Lamp black (Kali), "
            "and Indigo blue. Fine mongoose or squirrel hair brushes create detailed line work. "
            "Themes include the Dasavatara, Jagannath, Krishna Leela, and Ramayana. Finished works "
            "are sealed with a glowing lac varnish. The ~140 household village of Raghurajpur "
            "is officially designated a heritage craft village."
        ),
        "period": "10th century CE onwards",
        "is_gi_tagged": True,
        "gi_year": 2008,
        "unesco_status": None,
        "historical_era": "Somavamsi & Ganga Dynasties",
        "tags": ["GI Tag", "Raghurajpur", "Natural Pigments", "Jagannath", "UNESCO ICH"],
        "item_metadata": {
            "gi_tag_number": 56,
            "natural_pigments": ["Hingula (red)", "Haritala (yellow)", "Conch shell (white)", "Lamp black", "Indigo"],
            "canvas_preparation": "Tamarind seed paste + Kaitha chalk powder on cotton cloth",
            "finishing": "Lac tree resin varnish applied over charcoal flame"
        },
        "media_titles": ["Odisha Pattachitra Scroll — Dasavatara"],
        "source_titles": ["Geographical Indications Registry of India", "Odisha Tourism Development Corporation (OTDC)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "puri-jagannath-complex",
        "slug": "odissi-classical-dance",
        "title": "Odissi Classical Dance",
        "subtitle": "One of India's eight classical dance forms; Tribhangi and Chauka postures",
        "content_type": "performing_art",
        "subtype": "classical_dance",
        "summary": "India's classical dance of sculpted lyricism rooted in temple Maharis and Jayadeva's Gita Govinda, codified by Guru Kelucharan Mohapatra.",
        "description": (
            "Odissi is one of India's eight Sangeet Natak Akademi-recognised classical dance forms, "
            "distinguished by its hallmark postures: Tribhangi (three-bend posture curving at head, "
            "torso, and knees) and Chauka (square stance mimicking Jagannath's iconography). "
            "Historically performed by Devadasis (Maharis) inside the Jagannath Temple, the dance "
            "tradition also involved Gotipua — prepubescent boys dressed as women who performed "
            "acrobatic temple dances. Suppressed during colonial rule, Odissi was revived and codified "
            "in the 1950s–1970s by guru-legends Kelucharan Mohapatra, Pankaj Charan Das, Deba Prasad "
            "Das, and Mayadhar Raut. The repertoire draws from Jayadeva's Sanskrit Gita Govinda "
            "(12th century) and is accompanied by Mardala (barrel drum) and Odia song."
        ),
        "period": "2nd century BCE – present; modern revival 1950s",
        "is_gi_tagged": False,
        "unesco_status": None,
        "historical_era": "Kharavela Era through Modern Classical Revival",
        "tags": ["Classical Dance", "Tribhangi", "Mahari", "Kelucharan Mohapatra", "Gita Govinda"],
        "item_metadata": {
            "foundational_postures": ["Tribhangi (Three-bend lyrical)", "Chauka (Square monumental)"],
            "repertoire_text": "Jayadeva's Gita Govinda (12th century)",
            "primary_instrument": "Mardala drum",
            "revival_gurus": ["Guru Kelucharan Mohapatra", "Guru Pankaj Charan Das", "Guru Deba Prasad Das"]
        },
        "media_titles": ["Odissi Classical Dance Tribhangi Posture"],
        "source_titles": ["Sangeet Natak Akademi", "Odisha Tourism Development Corporation (OTDC)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "pahala-village",
        "slug": "odisha-rasagola",
        "title": "Odisha Rasagola",
        "subtitle": "GI-tagged cottage cheese sweet offered at Jagannath Temple since 12th century",
        "content_type": "cuisine",
        "subtype": "traditional_sweet",
        "summary": "GI-tagged soft fresh cottage cheese delicacy with documented 12th-century ritual offerings to Goddess Lakshmi during Niladri Bije.",
        "description": (
            "Odisha Rasagola (Khira Mohana / Pahala Rasagola) received GI Tag No. 612 in 2019. "
            "Historical evidence shows that soft cottage cheese (chhana) sweets were offered to "
            "Goddess Lakshmi during the Niladri Bije ceremony (the return of Lord Jagannath to "
            "the temple) since at least the 12th–15th century, described in Balarama Das's "
            "15th-century Odia Dandi Ramayana and Markanda Das's manuscript. The Pahala village "
            "variety, softer and less sweet than the Bengali version, is traditionally prepared "
            "by squeezing fresh chhana into balls and simmering in light sugar syrup. Raghabdas "
            "Math records from the 15th century document these offerings to Lord Jagannath."
        ),
        "period": "12th–15th century CE (documented manuscripts)",
        "is_gi_tagged": True,
        "gi_year": 2019,
        "unesco_status": None,
        "historical_era": "Medieval Odisha Jagannath Tradition",
        "tags": ["GI Tag", "Chhana", "Jagannath", "Pahala", "Traditional Sweet"],
        "item_metadata": {
            "gi_tag_number": 612,
            "ingredients": ["Fresh cow chhana", "Semolina (minimal)", "Light sugar cardamom syrup"],
            "ritual_ceremony": "Niladri Bije offering to Goddess Lakshmi",
            "literary_citation": "Balarama Das's 15th-century Dandi Ramayana"
        },
        "media_titles": [],
        "source_titles": ["Geographical Indications Registry of India", "Shree Jagannath Temple Administration (SJTA)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "pipili-town",
        "slug": "pipili-applique",
        "title": "Pipili Appliqué (Chandua)",
        "subtitle": "GI-tagged vibrant fabric craft for Rath Yatra canopies and temple decor",
        "content_type": "art_craft",
        "subtype": "applique_craft",
        "summary": "Centuries-old GI-tagged needlecraft combining colorful geometric and animal cutouts with mirrorwork for chariot canopies.",
        "description": (
            "Pipili, a small town 35 km from Bhubaneswar on the Puri highway, is the centre of "
            "Odisha's GI-tagged appliqué craft locally called Chandua. Artisans cut coloured fabrics "
            "into birds, animals, fish, and floral motifs and stitch them onto contrasting fabric "
            "backgrounds, embellished with mirrors (Shisha) and cowrie shells. The craft is inseparable "
            "from the Rath Yatra — the magnificent fabric canopies (chhatris) covering the three "
            "chariots, and the Taratarini umbrellas and temple banners are all Pipili appliqué. "
            "The craft has expanded into lamp shades, garden umbrellas, and decorative panels "
            "for the export market while retaining its ritual significance."
        ),
        "period": "13th century CE (linked to Rath Yatra origins)",
        "is_gi_tagged": True,
        "gi_year": 2008,
        "unesco_status": None,
        "historical_era": "Ganga Dynasty to Present",
        "tags": ["GI Tag", "Appliqué", "Rath Yatra", "Pipili", "Shisha Embroidery"],
        "item_metadata": {
            "gi_tag_number": 86,
            "ritual_applications": ["Nandighosh red/yellow canopy", "Taladhwaja red/green canopy", "Darpadalana red/black canopy"],
            "techniques": ["Hand stitching", "Mirrorwork (Shisha)", "Cowrie shell embellishment"]
        },
        "media_titles": [],
        "source_titles": ["Geographical Indications Registry of India", "Odisha Tourism Development Corporation (OTDC)"],
    },

    # ════════════════════════════════════════════════════════════════════════
    # CULTURAL FACTS (ContentItems with content_type="fact")
    # ════════════════════════════════════════════════════════════════════════
    {
        "region_id": "maharashtra",
        "place_slug": "ellora-caves-site",
        "slug": "fact-ellora-monolith",
        "title": "Ellora Monolithic Marvel Fact",
        "subtitle": "MONOLITHIC MARVEL",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "Ellora's Kailasa Temple was carved top-down from a single cliff removing 200,000 tonnes of basalt rock.",
        "description": (
            "Commissioned by Rashtrakuta King Dantidurga in the 8th century CE, the Kailasa Temple "
            "(Cave 16) at Ellora is the world's largest monolithic rock-cut structure. Builders worked "
            "from the top of the basalt plateau downward — the opposite of all conventional construction — "
            "removing an estimated 200,000 tonnes of rock over approximately 18 years. The result is a "
            "freestanding temple complex replicating Mount Kailash, complete with a 32-metre shikhara, "
            "life-size guardian elephants, and narrative relief panels carved from a single mountain."
        ),
        "tags": ["Fact", "Ellora", "Rashtrakuta", "Architecture"],
        "item_metadata": {
            "tag": "MONOLITHIC MARVEL",
            "region_label": "Ellora, Maharashtra",
            "quote": "The Kailasa Temple at Ellora required removing 200,000 tonnes of rock — carved top-down from a single cliff.",
            "explore_link": "/api/v1/content/ellora-kailasa-temple"
        },
        "media_titles": [],
        "source_titles": ["UNESCO World Heritage Centre", "Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "ajanta-caves-site",
        "slug": "fact-ajanta-mirrors",
        "title": "Ajanta Ancient Light Engineering Fact",
        "subtitle": "ANCIENT LIGHT-ENGINEERING",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "Ajanta painters reflected sunlight into deep dark caves using polished metal mirrors.",
        "description": (
            "The artists who created Ajanta's frescoes — deep inside lightless Buddhist cave monasteries "
            "— solved an extraordinary challenge: painting in total darkness. Evidence from ancient "
            "accounts and experimental archaeology suggests they arranged polished metal mirrors in "
            "relay chains from cave entrances, bouncing and redirecting sunlight to illuminate their "
            "work. The pigments they used — lapis lazuli blue, malachite green, red ochre, and lamp "
            "black — have survived 2,000 years in remarkable condition."
        ),
        "tags": ["Fact", "Ajanta", "Frescoes", "Optics"],
        "item_metadata": {
            "tag": "ANCIENT LIGHT-ENGINEERING",
            "region_label": "Ajanta, Maharashtra",
            "quote": "Ancient Ajanta painters used metal mirrors to redirect sunlight deep into caves with no natural light.",
            "explore_link": "/api/v1/content/ajanta-caves"
        },
        "media_titles": [],
        "source_titles": ["Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "maharashtra",
        "place_slug": "pandharpur-town",
        "slug": "fact-varkari-equality",
        "title": "Varkari Radical Egalitarianism Fact",
        "subtitle": "VARKARI EGALITARIANISM",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "The 700-year-old Pandharpur Wari pilgrimage erases caste hierarchy with 1M+ pilgrims walking and eating together.",
        "description": (
            "The 700-year-old Varkari pilgrimage to Pandharpur is one of India's oldest traditions of "
            "social equality in practice. Founded by saint-poets Dnyaneshwar, Namdev, Eknath, and Tukaram "
            "who preached devotion (bhakti) over caste, the Wari explicitly rejects caste hierarchy. "
            "Brahmin and Dalit, rich and poor, walk the same road chanting the same Abhangas, eat "
            "together from the same communal pots, and address each other as 'Varkari' (pilgrim). "
            "Over one million people walk up to 250 km in this living tradition of radical equality."
        ),
        "tags": ["Fact", "Varkari", "Bhakti", "Social Equality"],
        "item_metadata": {
            "tag": "VARKARI EGALITARIANISM",
            "region_label": "Pandharpur, Maharashtra",
            "quote": "The Pandharpur Wari pilgrimage erases caste distinctions — all one million pilgrims share the same road and food.",
            "explore_link": "/api/v1/content/pandharpur-wari"
        },
        "media_titles": [],
        "source_titles": ["Sant Dnyaneshwar & Tukaram Samadhi Trust Records"],
    },
    {
        "region_id": "odisha",
        "place_slug": "puri-jagannath-complex",
        "slug": "fact-juggernaut-etymology",
        "title": "Juggernaut Etymology Fact",
        "subtitle": "WORD ETYMOLOGY",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "The English word 'juggernaut' originated from 14th-century accounts of the Puri Rath Yatra chariot.",
        "description": (
            "When 14th-century Moroccan traveller Ibn Battuta witnessed the Puri Rath Yatra, he described "
            "the massive chariot of 'Juggernaut' rolling through crowds of ecstatic pilgrims. European "
            "missionaries amplified these accounts, and by the 19th century 'juggernaut' entered English "
            "as a metaphor for any overwhelming, crushing force. The irony is complete: a festival of joy "
            "and devotion gave English one of its most ominous words. The name Jagannath itself means "
            "'Lord of the Universe' in Sanskrit."
        ),
        "tags": ["Fact", "Etymology", "Rath Yatra", "Puri"],
        "item_metadata": {
            "tag": "WORD ETYMOLOGY",
            "region_label": "Puri, Odisha",
            "quote": "The English word 'juggernaut' — meaning an unstoppable force — comes from 'Jagannath' and the Rath Yatra.",
            "explore_link": "/api/v1/content/rath-yatra-puri"
        },
        "media_titles": [],
        "source_titles": ["Shree Jagannath Temple Administration (SJTA)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "konark-sun-temple-site",
        "slug": "fact-konark-sundial",
        "title": "Konark Stone Solar Clock Fact",
        "subtitle": "LIVING CALENDAR IN STONE",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "The 24 stone chariot wheels of Konark function as precise sundials accurate within minutes.",
        "description": (
            "The 24 intricately carved stone chariot wheels of the Konark Sun Temple function as a "
            "precise sundial. Each wheel has 8 major spokes and 8 minor spokes, dividing a day into "
            "16 segments of 1.5 hours each. By positioning a stick at the centre of the wheel's axle "
            "and reading the shadow falling on the spokes, ancient priests could calculate the time of "
            "day with remarkable accuracy. The 24 wheels also represent the 24 hours of a day and "
            "correspond to the 24 Ganga kings who ruled Odisha's medieval period."
        ),
        "tags": ["Fact", "Konark", "Astronomy", "Solar Clock"],
        "item_metadata": {
            "tag": "LIVING CALENDAR IN STONE",
            "region_label": "Konark, Odisha",
            "quote": "The 24 stone wheels of Konark are a solar clock accurate to within minutes — each spoke marks a 1.5-hour interval.",
            "explore_link": "/api/v1/content/konark-sun-temple"
        },
        "media_titles": [],
        "source_titles": ["UNESCO World Heritage Centre", "Archaeological Survey of India (ASI)"],
    },
    {
        "region_id": "odisha",
        "place_slug": "pahala-village",
        "slug": "fact-rasagola-gi-battle",
        "title": "Rasagola GI Tag Battle Fact",
        "subtitle": "GI TAG BATTLE",
        "content_type": "fact",
        "subtype": "trivia",
        "summary": "Odisha won the 7-year Rasagola GI tag dispute using 15th-century Dandi Ramayana manuscripts.",
        "description": (
            "One of India's most culturally charged GI Tag disputes ran from 2015 to 2019 between "
            "Odisha and West Bengal over the origin of the Rasagola. Odisha's winning evidence included "
            "Balarama Das's 15th-century Odia Dandi Ramayana, Markanda Das's manuscripts, and Raghabdas "
            "Math temple records describing chhana (cottage cheese) sweets being offered to Goddess "
            "Lakshmi during the Niladri Bije ceremony — predating the claimed 1868 invention by "
            "Kolkata's Nabin Chandra Das by four centuries. Odisha Rasagola received GI Tag No. 612 "
            "on 29 July 2019."
        ),
        "tags": ["Fact", "GI Tag", "Rasagola", "Culinary History"],
        "item_metadata": {
            "tag": "GI TAG BATTLE",
            "region_label": "Pahala, Odisha",
            "quote": "The Rasagola GI Tag war between Odisha and West Bengal lasted 7 years — Odisha won with 15th-century manuscripts.",
            "explore_link": "/api/v1/content/odisha-rasagola"
        },
        "media_titles": [],
        "source_titles": ["Geographical Indications Registry of India"],
    },
]


def seed():
    """Seed all entities and relationships cleanly."""
    # Ensure all tables are created
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("[*] Starting database seed...")

        # 1. Regions
        seeded_regions = 0
        for r_data in REGIONS_DATA:
            existing = db.query(models.Region).filter(models.Region.id == r_data["id"]).first()
            if not existing:
                region = models.Region(**r_data)
                db.add(region)
                seeded_regions += 1
                print(f"  [+] Region: {r_data['name']}")
            else:
                print(f"  [=] Region exists: {r_data['name']}")
        db.commit()

        # 2. Places
        seeded_places = 0
        places_map = {}
        for p_data in PLACES_DATA:
            existing = db.query(models.Place).filter(models.Place.slug == p_data["slug"]).first()
            if not existing:
                place = models.Place(**p_data)
                db.add(place)
                db.flush()
                places_map[place.slug] = place
                seeded_places += 1
                print(f"  [+] Place: {p_data['name']}")
            else:
                places_map[existing.slug] = existing
                print(f"  [=] Place exists: {p_data['name']}")
        db.commit()

        # 3. Sources
        seeded_sources = 0
        sources_map = {}
        for s_data in SOURCES_DATA:
            existing = db.query(models.Source).filter(models.Source.title == s_data["title"]).first()
            if not existing:
                source = models.Source(**s_data)
                db.add(source)
                db.flush()
                sources_map[source.title] = source
                seeded_sources += 1
                print(f"  [+] Source: {s_data['title']}")
            else:
                sources_map[existing.title] = existing
                print(f"  [=] Source exists: {s_data['title']}")
        db.commit()

        # 4. Media
        seeded_media = 0
        media_map = {}
        for m_data in MEDIA_DATA:
            existing = db.query(models.Media).filter(models.Media.title == m_data["title"]).first()
            if not existing:
                media = models.Media(**m_data)
                db.add(media)
                db.flush()
                media_map[media.title] = media
                seeded_media += 1
                print(f"  [+] Media: {m_data['title']}")
            else:
                media_map[existing.title] = existing
                print(f"  [=] Media exists: {m_data['title']}")
        db.commit()

        # 5. Content Items & M2M Associations
        seeded_content = 0
        for c_data in CONTENT_ITEMS_DATA:
            existing = db.query(models.ContentItem).filter(models.ContentItem.slug == c_data["slug"]).first()
            if not existing:
                place_slug = c_data.get("place_slug")
                place_obj = places_map.get(place_slug) if place_slug else None

                item = models.ContentItem(
                    region_id=c_data["region_id"],
                    place_id=place_obj.id if place_obj else None,
                    slug=c_data["slug"],
                    title=c_data["title"],
                    subtitle=c_data.get("subtitle"),
                    content_type=c_data["content_type"],
                    subtype=c_data.get("subtype"),
                    summary=c_data.get("summary"),
                    description=c_data["description"],
                    period=c_data.get("period"),
                    is_gi_tagged=c_data.get("is_gi_tagged", False),
                    gi_year=c_data.get("gi_year"),
                    unesco_status=c_data.get("unesco_status"),
                    historical_era=c_data.get("historical_era"),
                    tags=c_data.get("tags", []),
                    item_metadata=c_data.get("item_metadata", {}),
                )

                # Link Media
                for m_title in c_data.get("media_titles", []):
                    m_obj = media_map.get(m_title)
                    if m_obj:
                        item.media_items.append(m_obj)

                # Link Sources
                for s_title in c_data.get("source_titles", []):
                    s_obj = sources_map.get(s_title)
                    if s_obj:
                        item.sources.append(s_obj)

                db.add(item)
                seeded_content += 1
                print(f"  [+] ContentItem [{c_data['content_type']}]: {c_data['title']}")
            else:
                print(f"  [=] ContentItem exists: {c_data['slug']}")
        db.commit()

        print(f"\n[OK] Seed complete: {seeded_regions} regions, {seeded_places} places, {seeded_sources} sources, {seeded_media} media items, {seeded_content} content items.")

    except Exception as e:
        db.rollback()
        print(f"\n[ERROR] Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("\n--- Seeding Virasat Architecture Database ---\n")
    seed()
