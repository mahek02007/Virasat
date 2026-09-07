/**
 * VIRASAT — The Heritage of India
 * Central Cultural Data Repository
 */

const VIRASAT_DATA = {
  // Pilot and Featured Regions
  regions: [
    {
      id: "rajasthan",
      name: "Rajasthan",
      devanagari: "राजस्थान",
      tagline: "Forts • Folk Art • Cuisine",
      status: "available",
      isPilot: true,
      zone: "west",
      // Normalized percentage coordinates on india_map_cultural.jpg
      coords: { x: 37.5, y: 31.0 },
      categories: ["Royal Hill Forts", "Ghoomar & Kalbelia", "Thar Desert Lore", "Dal Baati Churma"],
      summary: "Explore the desert realm of Rajput chivalry, impenetrable sandstone forts, vibrant block-printing, and soulful Manganiyar melodies.",
      highlights: ["Mehrangarh Fort", "Hawa Mahal", "Pushkar Lake", "Jaisalmer Haveli"],
      colorAccent: "#C85A32",
      badge: "Pilot Region"
    },
    {
      id: "maharashtra",
      name: "Maharashtra",
      devanagari: "महाराष्ट्र",
      tagline: "Caves • Maratha Forts • Lavani",
      status: "available",
      isPilot: true,
      zone: "west",
      coords: { x: 41.5, y: 57.0 },
      categories: ["Ajanta & Ellora Caves", "Shivaji Hill Forts", "Warli Tribal Art", "Ganesh Utsav"],
      summary: "Traverse monumental rock-cut cave temples, rugged Sahyadri hill fortresses, and high-energy folk rhythms of Lavani.",
      highlights: ["Ellora Kailasa Temple", "Raigad Fort", "Ajanta Frescoes", "Elephanta Caves"],
      colorAccent: "#B84E29",
      badge: "Pilot Region"
    },
    {
      id: "tamil-nadu",
      name: "Tamil Nadu",
      devanagari: "तमिलनाडु",
      tagline: "Dravidian Temples • Carnatic • Bharatanatyam",
      status: "available",
      isPilot: true,
      zone: "south",
      coords: { x: 43.0, y: 72.5 },
      categories: ["Great Chola Temples", "Bharatanatyam Mudras", "Kanchipuram Silks", "Chettinad Flavors"],
      summary: "The cradle of classical Tamil antiquity, towering temple gopurams, ancient bronze iconography, and rich temple traditions.",
      highlights: ["Brihadeeswarar Temple", "Meenakshi Amman", "Shore Temple Mahabalipuram", "Thanjavur Paintings"],
      colorAccent: "#97572C",
      badge: "Pilot Region"
    },
    {
      id: "kerala",
      name: "Kerala",
      devanagari: "केरल",
      tagline: "Backwaters • Kathakali • Ayurveda",
      status: "available",
      isPilot: true,
      zone: "south",
      coords: { x: 39.5, y: 81.0 },
      categories: ["Kathakali Theatrical Art", "Theyyam Ritual Dance", "Kalaripayattu Martial Lore", "Spice Trade Routes"],
      summary: "Lush coastal sanctum celebrated for trance-like Theyyam rituals, ancient Ayurvedic lineages, and tranquil palm-fringed backwaters.",
      highlights: ["Kathakali Mudras", "Padmanabhaswamy Temple", "Bekal Fort", "Munnar Tea Hills"],
      colorAccent: "#1C4834",
      badge: "Pilot Region"
    },
    {
      id: "jammu-kashmir",
      name: "Jammu & Kashmir",
      devanagari: "जम्मू और कश्मीर",
      tagline: "Sufiana • Pashmina • Chinar Valleys",
      status: "available",
      isPilot: true,
      zone: "north",
      coords: { x: 42.8, y: 13.8 },
      categories: ["Pashmina & Carpet Weaving", "Sufiana Kalam Music", "Wooden Khatamband", "Wazwan Feasts"],
      summary: "High-altitude Himalayan majesty, centuries of sacred Sufi poetry, paper-mâché artistry, and intricately carved deodar shrines.",
      highlights: ["Dal Lake Shikaras", "Martand Sun Temple", "Charar-e-Sharief", "Gulmarg Valleys"],
      colorAccent: "#183E54",
      badge: "Pilot Region"
    },
    {
      id: "west-bengal",
      name: "West Bengal",
      devanagari: "पश्चिम बंगाल",
      tagline: "Terracotta • Literature • Baul",
      status: "available",
      isPilot: true,
      zone: "east",
      coords: { x: 62.0, y: 45.0 },
      categories: ["Bishnupur Terracotta", "Baul Mystic Folk", "Durga Puja Spectacle", "Shantiniketan Renaissance"],
      summary: "The cultural hub of literature, terracotta temple spires, mystic Baul singers, and the grand festive celebration of Durga Puja.",
      highlights: ["Bishnupur Temples", "Sundarbans Lore", "Victoria Memorial", "Dakshineswar"],
      colorAccent: "#6E1B24",
      badge: "Pilot Region"
    },
    {
      id: "gujarat",
      name: "Gujarat",
      devanagari: "गुजरात",
      tagline: "Stepwells • Garba • Textile Weaving",
      status: "available",
      isPilot: false,
      zone: "west",
      coords: { x: 31.0, y: 46.5 },
      categories: ["Rani ki Vav Stepwell", "Patola Silk Weaving", "Navratri Garba", "Kutch Lippan Art"],
      summary: "Mastery of subterranean stepwell architecture, vibrant mirrored Kutchi embroideries, and sacred coastal pilgrim trails.",
      highlights: ["Rani ki Vav", "Somnath Temple", "Rann of Kutch", "Modhera Sun Temple"],
      colorAccent: "#C1834B",
      badge: "Featured Region"
    },
    {
      id: "madhya-pradesh",
      name: "Madhya Pradesh",
      devanagari: "मध्य प्रदेश",
      tagline: "Khajuraho • Gond Art • Stupas",
      status: "available",
      isPilot: false,
      zone: "central",
      coords: { x: 48.0, y: 50.0 },
      categories: ["Khajuraho Sculptures", "Sanchi Buddhist Stupa", "Gond & Bhil Tribal Lore", "Gwalior Royal Heritage"],
      summary: "The heart of India featuring UNESCO rock shelters, magnificent erotic stone carvings, and sacred Narmada river ghats.",
      highlights: ["Khajuraho Temples", "Sanchi Stupa", "Bhimbetka Caves", "Orchha Palaces"],
      colorAccent: "#8F371B",
      badge: "Featured Region"
    },
    {
      id: "odisha",
      name: "Odisha",
      devanagari: "ओडिशा",
      tagline: "Konark Sun Temple • Odissi • Pattachitra",
      status: "available",
      isPilot: false,
      zone: "east",
      coords: { x: 57.5, y: 58.5 },
      categories: ["Konark Sun Chariot", "Odissi Classical Dance", "Raghurajpur Pattachitra", "Puri Rath Yatra"],
      summary: "Land of monumental stone chariots, ancient palm-leaf scrolls, celestial Odissi dancer postures, and maritime Kalinga trade.",
      highlights: ["Konark Sun Temple", "Jagannath Puri", "Udayagiri Caves", "Chilika Lake"],
      colorAccent: "#D4AF37",
      badge: "Featured Region"
    },
    {
      id: "assam",
      name: "Assam",
      devanagari: "असम",
      tagline: "Bihu • Muga Silk • Brahmaputra Lore",
      status: "available",
      isPilot: false,
      zone: "northeast",
      coords: { x: 75.0, y: 35.0 },
      categories: ["Golden Muga Silk", "Rongali Bihu Rhythms", "Kamakhya Sacred Sanctum", "Majuli Island Satras"],
      summary: "Verdant tea riverlands, the world's largest river island Majuli, shimmering golden silks, and rich Vaishnavite monastery arts.",
      highlights: ["Kamakhya Temple", "Majuli Satras", "Kaziranga", "Sivasagar Ahom Palaces"],
      colorAccent: "#585334",
      badge: "Featured Region"
    }
  ],

  // Comprehensive Search Index (Regions, Sites, Performing Arts, Festivals, Crafts)
  searchIndex: [
    { title: "Rajasthan", type: "Region", subtitle: "Western India • Forts, Folk Music & Cuisine", queryMatch: ["rajasthan", "rajput", "desert", "jaipur", "jodhpur"], url: "explore.html?region=rajasthan", regionId: "rajasthan" },
    { title: "Maharashtra", type: "Region", subtitle: "Western India • Caves, Maratha Forts & Lavani", queryMatch: ["maharashtra", "mumbai", "pune", "maratha", "shivaji"], url: "explore.html?region=maharashtra", regionId: "maharashtra" },
    { title: "Tamil Nadu", type: "Region", subtitle: "Southern India • Dravidian Temples & Carnatic Arts", queryMatch: ["tamil nadu", "tamil", "chennai", "chola", "dravidian"], url: "explore.html?region=tamil-nadu", regionId: "tamil-nadu" },
    { title: "Kerala", type: "Region", subtitle: "Southern Coast • Backwaters, Kathakali & Ayurveda", queryMatch: ["kerala", "malabar", "cochin", "trivandrum", "ayurveda"], url: "explore.html?region=kerala", regionId: "kerala" },
    { title: "Jammu & Kashmir", type: "Region", subtitle: "Northern Valleys • Sufiana Kalam & Pashmina Crafts", queryMatch: ["jammu", "kashmir", "srinagar", "himalayas", "chinar"], url: "explore.html?region=jammu-kashmir", regionId: "jammu-kashmir" },
    { title: "West Bengal", type: "Region", subtitle: "Eastern India • Bishnupur Terracotta & Baul Lore", queryMatch: ["west bengal", "bengal", "kolkata", "durga", "baul"], url: "explore.html?region=west-bengal", regionId: "west-bengal" },
    { title: "Gujarat", type: "Region", subtitle: "Western India • Stepwells, Garba & Textile Weaving", queryMatch: ["gujarat", "ahmedabad", "kutch", "garba", "patola"], url: "explore.html?region=gujarat", regionId: "gujarat" },
    { title: "Madhya Pradesh", type: "Region", subtitle: "Central Heart • Khajuraho Spire Reliefs & Gond Art", queryMatch: ["madhya pradesh", "bhopal", "khajuraho", "sanchi", "gond"], url: "explore.html?region=madhya-pradesh", regionId: "madhya-pradesh" },
    { title: "Odisha", type: "Region", subtitle: "Eastern Coast • Konark Sun Temple & Odissi Dance", queryMatch: ["odisha", "orissa", "konark", "puri", "bhubaneswar"], url: "explore.html?region=odisha", regionId: "odisha" },
    { title: "Assam", type: "Region", subtitle: "Northeastern Valley • Bihu Folk & Muga Golden Silk", queryMatch: ["assam", "guwahati", "majuli", "bihu", "brahmaputra"], url: "explore.html?region=assam", regionId: "assam" },

    // Monuments & Heritage Sites
    { title: "Ajanta Caves", type: "Monument", subtitle: "Rock-cut Buddhist cave monuments with ancient frescoes", queryMatch: ["ajanta", "ajanta caves", "frescoes", "buddhist art", "caves"], url: "explore.html?region=maharashtra&focus=ajanta", regionId: "maharashtra" },
    { title: "Brihadeeswarar Temple", type: "Monument", subtitle: "Great Living Chola Temple with 80-tonne granite dome", queryMatch: ["brihadeeswarar", "tanjore", "thanjavur", "chola temple", "big temple"], url: "explore.html?region=tamil-nadu&focus=brihadeeswarar", regionId: "tamil-nadu" },
    { title: "Mehrangarh Fort", type: "Monument", subtitle: "Towering 15th-century cliffside fort in Jodhpur", queryMatch: ["mehrangarh", "mehrangarh fort", "jodhpur fort", "blue city"], url: "explore.html?region=rajasthan&focus=mehrangarh", regionId: "rajasthan" },
    { title: "Konark Sun Temple", type: "Monument", subtitle: "13th-century chariot of Surya with 24 carved stone wheels", queryMatch: ["konark", "sun temple", "black pagoda", "odisha temple"], url: "explore.html?region=odisha&focus=konark", regionId: "odisha" },
    { title: "Khajuraho Monuments", type: "Monument", subtitle: "UNESCO Nagara-style temples with celestial sculptures", queryMatch: ["khajuraho", "chandelas", "sculptures", "temples of love"], url: "explore.html?region=madhya-pradesh&focus=khajuraho", regionId: "madhya-pradesh" },

    // Performing Arts & Dance
    { title: "Bharatanatyam", type: "Performing Art", subtitle: "Ancient classical temple dance codified in Natya Shastra", queryMatch: ["bharatanatyam", "classical dance", "mudras", "abhinaya", "tamil dance"], url: "explore.html?region=tamil-nadu&focus=bharatanatyam", regionId: "tamil-nadu" },
    { title: "Kathakali", type: "Performing Art", subtitle: "Dramatic dance-drama with stylized makeup and facial mudras", queryMatch: ["kathakali", "kerala dance", "mudras", "theatrical"], url: "explore.html?region=kerala&focus=kathakali", regionId: "kerala" },
    { title: "Kathak", type: "Performing Art", subtitle: "Classical storytelling dance known for rapid spins (chakkars)", queryMatch: ["kathak", "storytelling", "chakkars", "ghunghru", "lucknow"], url: "explore.html?region=rajasthan&focus=kathak", regionId: "rajasthan" },
    { title: "Ghoomar", type: "Folk Art", subtitle: "Traditional Rajasthani folk dance performed with swirling ghagras", queryMatch: ["ghoomar", "rajasthani dance", "folk dance", "marwar"], url: "explore.html?region=rajasthan&focus=ghoomar", regionId: "rajasthan" },

    // Festivals & Living Traditions
    { title: "Diwali", type: "Festival", subtitle: "Festival of lights celebrating knowledge and prosperity", queryMatch: ["diwali", "deepavali", "lights", "festival of lights", "diyas"], url: "explore.html?region=rajasthan&focus=diwali", regionId: "rajasthan" },
    { title: "Durga Puja", type: "Festival", subtitle: "Intangible UNESCO heritage celebrating the victory of good over evil", queryMatch: ["durga puja", "durgotsav", "pandal", "dhunuchi", "bengal festival"], url: "explore.html?region=west-bengal&focus=durga-puja", regionId: "west-bengal" },
    { title: "Navratri & Garba", type: "Festival", subtitle: "Nine nights of rhythmic circle dancing and devotional celebration", queryMatch: ["garba", "navratri", "dandiya", "gujarat festival"], url: "explore.html?region=gujarat&focus=garba", regionId: "gujarat" },

    // Folk Arts & Living Crafts
    { title: "Madhubani Painting", type: "Folk Craft", subtitle: "Folk painting of Bihar created using natural pigments and twigs", queryMatch: ["madhubani", "mithila", "folk art", "bihar painting", "natural dyes"], url: "explore.html?region=west-bengal&focus=madhubani", regionId: "west-bengal" },
    { title: "Pashmina Weaving", type: "Master Craft", subtitle: "Ultra-fine cashmere wool hand-woven in Kashmir valleys", queryMatch: ["pashmina", "cashmere", "shawls", "kashmiri wool", "charkha"], url: "explore.html?region=jammu-kashmir&focus=pashmina", regionId: "jammu-kashmir" },
    { title: "Pattachitra", type: "Master Craft", subtitle: "Intricate cloth-based scroll paintings from Raghurajpur, Odisha", queryMatch: ["pattachitra", "patachitra", "odisha painting", "palm leaf"], url: "explore.html?region=odisha&focus=pattachitra", regionId: "odisha" }
  ],

  // Curated Cultural Facts for "Did You Know?"
  facts: [
    {
      id: 1,
      tag: "MITHILA PAINTINGS",
      region: "Mithila, Bihar",
      quote: "Madhubani painting originated in the Mithila region of Bihar.",
      description: "Traditionally painted by village women on fresh mud walls during festivals, artists use natural pigments ground from turmeric, indigo, soot, and marigolds with twig brushes to illustrate ancient folklore and harmony with nature.",
      exploreLink: "explore.html?region=west-bengal&topic=madhubani"
    },
    {
      id: 2,
      tag: "LIVING BIO-ENGINEERING",
      region: "Cherrapunji, Meghalaya",
      quote: "The Living Root Bridges of Meghalaya are grown, not built.",
      description: "Indigenous Khasi and Jaintia tribes guide the aerial roots of Ficus elastica trees across rushing monsoon gorges using hollowed betel nut trunks. Over 15 to 30 years, the roots knit into suspension bridges that grow stronger with age.",
      exploreLink: "explore.html?region=assam&topic=root-bridges"
    },
    {
      id: 3,
      tag: "DRAVIDIAN ENGINEERING",
      region: "Thanjavur, Tamil Nadu",
      quote: "The 80-tonne granite dome of Brihadeeswarar was hauled via a 6 km ramp.",
      description: "Built in 1010 CE by Emperor Raja Raja Chola I without binding mortar, the 216-foot vimana tower is capped by a massive octagonal monolith, raised by war elephants along an inclined earthen causeway over six years.",
      exploreLink: "explore.html?region=tamil-nadu&topic=brihadeeswarar"
    },
    {
      id: 4,
      tag: "DESERT ARCHITECTURE",
      region: "Jodhpur, Rajasthan",
      quote: "The blue wash of Jodhpur houses was originally a natural coolant.",
      description: "Looking down from Mehrangarh Fort, Jodhpur glows in shades of indigo. The copper sulfate and limestone wash was applied to repel termites, deflect harsh sunlight, and keep ancient stone havelis naturally cool in 48°C desert heat.",
      exploreLink: "explore.html?region=rajasthan&topic=blue-city"
    },
    {
      id: 5,
      tag: "ANCIENT MARITIME SILKS",
      region: "Kanchipuram, Tamil Nadu",
      quote: "Kanchipuram silk weavers trace their lineage directly to the sage Markandeya.",
      description: "Renowned for their heavy pure mulberry silk and pure silver zari dipped in gold, traditional Kanchipuram sarees feature the 'Korvai' interlocking technique, weaving temple borders so seamlessly that the seam is nearly indestructible.",
      exploreLink: "explore.html?region=tamil-nadu&topic=kanchipuram"
    }
  ],

  // Featured Heritage Cards (4 prominent cards)
  featuredHeritage: [
    {
      id: "classical-dance",
      title: "Indian Classical Dance",
      subtitle: "The Natya Shastra & Living Mudra Traditions",
      category: "Performing Arts",
      image: "assets/featured_dance.jpg",
      readTime: "5 min exploration",
      summary: "Discover the 8 classical dance traditions codified over 2,000 years ago, where intricate footwork, eye expressions, and sacred hand mudras narrate timeless epics.",
      exploreUrl: "explore.html?feature=classical-dance",
      tags: ["Bharatanatyam", "Kathakali", "Kathak", "Odissi"]
    },
    {
      id: "ancient-temples",
      title: "Ancient Sacred Temples",
      subtitle: "Monolithic Spires & Dravidian Dynasties",
      category: "Sacred Architecture",
      image: "assets/featured_temples.jpg",
      readTime: "7 min exploration",
      summary: "Explore rock-hewn sanctums, towering sculpted gopurams, and acoustic stone pillars engineered across the Chola, Pallava, and Vijayanagara empires.",
      exploreUrl: "explore.html?feature=ancient-temples",
      tags: ["Brihadeeswarar", "Konark", "Khajuraho", "Meenakshi"]
    },
    {
      id: "folk-festivals",
      title: "Folk Festivals & Rituals",
      subtitle: "Communal Celebrations & Sacred Rhythms",
      category: "Living Traditions",
      image: "assets/featured_festivals.jpg",
      readTime: "6 min exploration",
      summary: "Step inside vibrant communal celebrations, from the ecstatic Garba circles of Gujarat and Pushkar's camel gathering to Kerala's trance-like Theyyam nights.",
      exploreUrl: "explore.html?feature=folk-festivals",
      tags: ["Pushkar Mela", "Theyyam", "Durga Puja", "Garba"]
    },
    {
      id: "regional-cuisine",
      title: "Regional Living Cuisine",
      subtitle: "Spice Routes & Ceremonial Thalis",
      category: "Culinary Heritage",
      image: "assets/featured_cuisine.jpg",
      readTime: "4 min exploration",
      summary: "Taste ancient spice routes across diverse regional thalis, temple prasad recipes, slow-cooked royal Wazwan feasts, and fermented coastal delicacies.",
      exploreUrl: "explore.html?feature=regional-cuisine",
      tags: ["Rajasthani Thali", "Wazwan", "Sadhya", "Chettinad"]
    }
  ],

  // Mock User Journey Progress
  userJourney: {
    exploredCount: 3,
    totalRegions: 7,
    progressPercent: 43,
    rank: "Heritage Explorer",
    nextMilestone: "Level 2: Cultural Cartographer",
    recentDiscovery: "Mehrangarh Royal Gateway",
    unlockedCards: [
      { id: "c1", title: "Mehrangarh Fort", region: "Rajasthan", icon: "🏰" },
      { id: "c2", title: "Kathakali Mudra", region: "Kerala", icon: "🎭" },
      { id: "c3", title: "Brihadeeswarar Vimana", region: "Tamil Nadu", icon: "🛕" }
    ],
    avatarGreetings: [
      { 
        lang: "Hindi", 
        langCode: "hi-IN", 
        text: "नमस्ते! भारत की जीवंत सांस्कृतिक धरोहर में आपका स्वागत है।", 
        speechText: "नमस्ते! भारत की जीवंत सांस्कृतिक धरोहर में आपका स्वागत है। किसी भी क्षेत्र को चुनकर अपनी यात्रा शुरू करें।", 
        roman: "Namaste! Choose a region on the map to begin exploring." 
      },
      { 
        lang: "Rajasthani", 
        langCode: "hi-IN", 
        text: "खम्मा घणी! किणी एक प्रदेश सूं आपरी यात्रा शुरू करो।", 
        speechText: "खम्मा घणी! किणी एक प्रदेश सूं आपरी यात्रा शुरू करो।", 
        roman: "Khamma Ghani! Discover royal forts & desert stories." 
      },
      { 
        lang: "Tamil", 
        langCode: "ta-IN", 
        text: "வணக்கம்! உங்கள் கலாச்சார பயணத்தை வரைபடத்தில் தொடங்குங்கள்.", 
        speechText: "வணக்கம்! உங்கள் கலாச்சார பயணத்தை வரைபடத்தில் தொடங்குங்கள்.", 
        roman: "Vanakkam! Explore temple architecture & ancient arts." 
      },
      { 
        lang: "Kashmiri", 
        langCode: "hi-IN", 
        text: "आदाब! कश्मीर की खूबसूरत वादियों में आपका स्वागत है।", 
        speechText: "आदाब! कश्मीर की खूबसूरत वादियों में आपका स्वागत है।", 
        roman: "Adaab! Experience the serenity of northern valleys." 
      },
      { 
        lang: "Marathi", 
        langCode: "mr-IN", 
        text: "नमस्कार! महाराष्ट्राच्या ऐतिहासिक संस्कृतीचा शोध घ्या.", 
        speechText: "नमस्कार! महाराष्ट्राच्या ऐतिहासिक संस्कृतीचा शोध घ्या.", 
        roman: "Namaskar! Dive into Maratha fortresses & rock caves." 
      }
    ]
  }
};

// Global export for vanilla browser and node environments
if (typeof window !== 'undefined') {
  window.VIRASAT_DATA = VIRASAT_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = VIRASAT_DATA;
}
