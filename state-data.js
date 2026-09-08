/**
 * VIRASAT — State Cultural Data Repository
 * Initial Mock Data for State / Cultural Exploration Page
 */

const VIRASAT_STATE_DATA = {
  maharashtra: {
    id: "maharashtra",
    name: "Maharashtra",
    devanagari: "महाराष्ट्र",
    tagline: "Land of Sahyadri Citadels, Sacred Rivers & Timeless Traditions",
    region: "Western India",
    capital: "Mumbai (Winter: Nagpur)",
    language: "Marathi (मराठी)",
    intro: "Nestled between the rugged Sahyadri ranges and the Arabian Sea, Maharashtra presents a grand continuum of civilization. From the UNESCO World Heritage rock-cut cave sanctums of Ajanta and Ellora to the invincible coastal sea forts of Shivaji Maharaj and the devotion of the Pandharpur Wari, Maharashtra’s living heritage weaves deep spiritual philosophy with vibrant folk celebrations.",
    heroStats: [
      { label: "UNESCO World Heritage Sites", value: "5 Sites" },
      { label: "Hill & Sea Forts", value: "350+ Forts" },
      { label: "Coastline", value: "720 km" },
      { label: "Living Traditions", value: "Ancient & Folk" }
    ],
    guide: {
      name: "Acharya Madhav",
      title: "Virasat Cultural Guide",
      archetype: "Sahyadri Chronicler",
      avatarInitials: "AM",
      greeting: "Namaskar! I am your cultural companion for Maharashtra. Traverse the basalt ramparts, decode ancient cave frescoes, or explore the rhythms of Lavani with me.",
      quickPrompts: [
        "Tell me about the architecture of Ajanta & Ellora",
        "Why is the Pandharpur Wari pilgrimage so historic?",
        "What makes Paithani silk sarees unique in craft?",
        "Explain the story behind the Dhol-Tasha tradition"
      ],
      quote: "“The rocks of the Sahyadri were carved not merely with chisels, but with unwavering devotion and centuries of patient mastery.”"
    },
    categories: [
      { id: "culture", name: "Culture", count: "12 Highlights", active: true },
      { id: "language", name: "Language", count: "Marathi & Dialects", active: false },
      { id: "art", name: "Art", count: "Warli & Caves", active: false },
      { id: "music", name: "Music", count: "Natya Sangeet & Folk", active: false },
      { id: "dance", name: "Dance", count: "Lavani & Lezim", active: false },
      { id: "attire", name: "Attire", count: "Paithani & Nauvari", active: false },
      { id: "cuisine", name: "Cuisine", count: "Puran Poli & Coastal", active: false },
      { id: "festivals", name: "Festivals", count: "Ganeshotsav & Wari", active: false },
      { id: "places", name: "Places", count: "Forts & Sanctuaries", active: false }
    ],
    featuredCards: [
      {
        tag: "MONUMENTAL ARCHITECTURE",
        title: "Ajanta & Ellora Rock-Cut Caves",
        subtitle: "Aurangabad (Chhatrapati Sambhaji Nagar) • 2nd Century BCE – 10th Century CE",
        description: "Thirty rock-hewn Buddhist cave monuments at Ajanta preserving world-renowned tempera murals, paired with Ellora's monolithic Kailash Temple carved top-down from a single volcanic basalt cliff.",
        badge: "UNESCO Heritage",
        keyAspects: ["Kailash Temple Monolith", "Ajanta Fresco Murals", "Buddhist, Hindu & Jain Harmony"]
      },
      {
        tag: "WARRIOR HERITAGE & FORTRESSES",
        title: "Sahyadri & Coastal Fort Network",
        subtitle: "Raigad, Murud-Janjira, Sinhagad & Sindhudurg",
        description: "An ingenious defense system engineered by Chhatrapati Shivaji Maharaj, blending mountain ridge bastions with deep-sea impregnable marine fortresses designed in harmony with monsoon weather patterns.",
        badge: "Maratha Architecture",
        keyAspects: ["High-Altitude Cisterns", "Sea Bastion Engineering", "Strategic Mountain Passes"]
      },
      {
        tag: "SACRED LIVING TRADITION",
        title: "The Pandharpur Wari Pilgrimage",
        subtitle: "800-Year-Old Sacred Walking Pilgrimage",
        description: "Over a million pilgrims (Varkaris) walk hundreds of kilometers singing the abhangs of Saint Dnyaneshwar and Saint Tukaram to reach the sanctum of Lord Vithoba, celebrating egalitarian brotherhood.",
        badge: "Intangible Heritage",
        keyAspects: ["Abhang Devotional Poetry", "Taal & Chipli Instruments", "Community Egalitarian Spirit"]
      },
      {
        tag: "INDIGENOUS FOLK ART",
        title: "Warli Tribal Painting & Paithani Silk",
        subtitle: "North Sahyadri Belt & Paithan Handloom Weavers",
        description: "Warli geometric circle-triangle-square pictorial language capturing Mother Earth and the Tarpa dance, alongside 2,000-year-old royal Paithani pure silk tapestries featuring peacock and lotus zari borders.",
        badge: "Master Craft Traditions",
        keyAspects: ["Natural Rice-Paste Pigments", "Pure Gold Thread Zari", "Geographical Indication (GI)"]
      }
    ]
  }
};
