// VIRASAT Regional Data Template
// This file demonstrates the data structure for regional content
// Copy this template for each of the 8 regions and fill with actual data

const regionalDataTemplate = {
    // Region identifier
    id: "region-name-slug",
    
    // Display name
    name: "[Region Name]",
    
    // Regional avatar image path
    avatar: "path/to/regional-avatar.png",
    
    // Hero/header image
    headerImage: "path/to/header-image.jpg",
    
    // Short introduction (2-3 sentences)
    introduction: "[Brief cultural introduction about the region - what makes it unique, its geographical significance, and cultural importance]",
    
    // ==================== SECTIONS ==================== //
    
    sections: {
        // HISTORY & HISTORICAL SIGNIFICANCE
        history: {
            mainText: "[Detailed historical background of the region]",
            image: "path/to/historical-image.jpg",
            facts: [
                {
                    title: "Historical Era",
                    content: "[Time period and dynasty information]"
                },
                {
                    title: "Key Figures",
                    content: "[Important historical personalities]"
                },
                {
                    title: "Legacy",
                    content: "[Cultural and historical impact]"
                }
            ],
            timeline: [
                {
                    period: "[Time Period]",
                    event: "[Major historical event]"
                }
            ]
        },
        
        // FESTIVALS & CUSTOMS
        festivals: [
            {
                name: "[Festival Name]",
                image: "path/to/festival-image.jpg",
                description: "[Detailed description of the festival, its significance, and how it's celebrated]",
                time: "[When celebrated - month/season]",
                significance: "[Cultural and religious importance]",
                customs: [
                    "[Custom 1]",
                    "[Custom 2]"
                ]
            }
            // Add more festivals
        ],
        
        // ART FORMS
        artForms: {
            // Dance
            dance: [
                {
                    name: "[Dance Form Name]",
                    image: "path/to/dance-image.jpg",
                    description: "[Detailed description of the dance form]",
                    characteristics: [
                        "[Characteristic 1]",
                        "[Characteristic 2]",
                        "[Characteristic 3]"
                    ],
                    history: "[Origin and evolution of the dance form]",
                    occasions: "[When performed]"
                }
                // Add more dance forms
            ],
            
            // Music
            music: [
                {
                    name: "[Music Tradition Name]",
                    image: "path/to/music-image.jpg",
                    description: "[Detailed description of musical tradition]",
                    instruments: [
                        {
                            name: "[Instrument Name]",
                            description: "[Brief description]"
                        }
                    ],
                    significance: "[Cultural importance]"
                }
                // Add more music traditions
            ],
            
            // Painting
            painting: [
                {
                    name: "[Painting Style Name]",
                    image: "path/to/painting-image.jpg",
                    description: "[Detailed description of painting style]",
                    technique: "[Painting techniques used]",
                    themes: "[Common themes depicted]",
                    materials: "[Traditional materials used]"
                }
                // Add more painting styles
            ],
            
            // Crafts
            crafts: [
                {
                    name: "[Craft Name]",
                    image: "path/to/craft-image.jpg",
                    description: "[Detailed description of the craft]",
                    technique: "[How it's made]",
                    significance: "[Cultural importance]",
                    materials: "[Materials used]"
                }
                // Add more crafts
            ]
        },
        
        // CUISINE
        cuisine: {
            introduction: "[Overview of regional culinary traditions and influences]",
            dishes: [
                {
                    name: "[Dish Name]",
                    image: "path/to/dish-image.jpg",
                    description: "[Detailed description of the dish, ingredients, and preparation]",
                    category: "[Main Course/Dessert/Snack/Beverage]",
                    type: "[Vegetarian/Non-Vegetarian/Vegan]",
                    occasion: "[When typically served]",
                    culturalSignificance: "[Why this dish is important]"
                }
                // Add more dishes
            ],
            ingredients: [
                {
                    name: "[Key Ingredient]",
                    significance: "[Why it's important to this cuisine]"
                }
            ],
            cookingMethods: [
                "[Traditional cooking method 1]",
                "[Traditional cooking method 2]"
            ]
        },
        
        // TRADITIONAL CLOTHING
        clothing: [
            {
                name: "[Garment Name]",
                image: "path/to/clothing-image.jpg",
                description: "[Detailed description of the garment, how it's worn, and its variations]",
                gender: "[Men/Women/Unisex]",
                fabric: "[Type of fabric traditionally used]",
                occasion: "[When worn - daily/festival/special occasions]",
                significance: "[Cultural and social significance]",
                colors: "[Traditional colors and their meanings]",
                accessories: [
                    {
                        name: "[Accessory Name]",
                        description: "[Brief description]"
                    }
                ]
            }
            // Add more clothing items
        ],
        
        // LANGUAGES / DIALECTS
        languages: [
            {
                name: "[Language/Dialect Name]",
                description: "[Information about the language, its speakers, and characteristics]",
                script: "[Writing system used]",
                speakers: "[Number/percentage of speakers]",
                sample: {
                    phrase: "[Sample phrase in the language]",
                    translation: "[English translation]",
                    pronunciation: "[Pronunciation guide]"
                },
                significance: "[Cultural importance of the language]",
                status: "[Official/Regional/Dialect]"
            }
            // Add more languages
        ],
        
        // HISTORICAL PLACES & MONUMENTS
        monuments: [
            {
                name: "[Monument Name]",
                image: "path/to/monument-image.jpg",
                description: "[Detailed description of the monument, its history, architecture, and significance]",
                period: "[Time period when built]",
                dynasty: "[Dynasty/ruler who built it]",
                architecturalStyle: "[Architectural style and influences]",
                significance: "[Historical and cultural importance]",
                unescoHeritage: true/false,
                location: "[Specific location within region]",
                features: [
                    "[Notable feature 1]",
                    "[Notable feature 2]"
                ],
                currentStatus: "[Well-preserved/Under restoration/etc.]"
            }
            // Add more monuments
        ],
        
        // INDIGENOUS / TRIBAL PRACTICES
        tribal: {
            overview: "[Overview of indigenous and tribal communities in the region]",
            image: "path/to/tribal-image.jpg",
            communities: [
                {
                    name: "[Tribe/Community Name]",
                    description: "[Description of the community]",
                    population: "[Approximate population]",
                    location: "[Where they primarily live]"
                }
            ],
            practices: [
                {
                    name: "[Practice Name]",
                    description: "[Detailed description of the traditional practice]",
                    significance: "[Why this practice is important]",
                    currentStatus: "[Still practiced/Revived/Endangered]"
                }
                // Add more practices
            ],
            traditions: [
                "[Traditional practice 1]",
                "[Traditional practice 2]"
            ],
            challenges: "[Contemporary challenges faced by these communities]",
            preservation: "[Efforts to preserve these practices]"
        }
    }
};

// ==================== EXAMPLE: SAMPLE REGIONAL DATA ==================== //
// This is a partial example showing how to structure the data

const sampleRegionData = {
    id: "maharashtra",
    name: "Maharashtra",
    avatar: "assets/avatars/maharashtra-avatar.png",
    headerImage: "assets/regions/maharashtra-hero.jpg",
    introduction: "Maharashtra, the land of Marathas, is a vibrant tapestry of history, culture, and tradition. From the ancient cave temples to the bustling cities, this region embodies the spirit of diverse India while maintaining its unique cultural identity rooted in centuries of rich heritage.",
    
    sections: {
        history: {
            mainText: "Maharashtra has been home to some of India's most powerful empires and has played a crucial role in shaping the nation's history. The region witnessed the rise of the Maratha Empire under Chhatrapati Shivaji Maharaj, who established Hindavi Swarajya and became a symbol of courage and administrative brilliance.",
            image: "assets/history/maharashtra-history.jpg",
            facts: [
                {
                    title: "Historical Era",
                    content: "Ancient Buddhist period to Maratha Empire (3rd century BCE - 19th century CE)"
                },
                {
                    title: "Key Figures",
                    content: "Chhatrapati Shivaji Maharaj, Jijabai, Sambhaji Maharaj, Peshwas"
                },
                {
                    title: "Legacy",
                    content: "Administrative reforms, naval supremacy, fort architecture, and social justice movements"
                }
            ]
        },
        
        festivals: [
            {
                name: "Ganesh Chaturthi",
                image: "assets/festivals/ganesh-chaturthi.jpg",
                description: "Ganesh Chaturthi is Maharashtra's grandest festival, celebrating the birth of Lord Ganesha. The 10-day festival transforms cities and villages with elaborate pandals, cultural programs, and devotional fervor, culminating in the immersion ceremony.",
                time: "August-September (Bhadrapada month)",
                significance: "Celebrates wisdom, prosperity, and new beginnings",
                customs: [
                    "Installation of Ganesha idols in homes and public pandals",
                    "Daily prayers and aarti",
                    "Cultural performances",
                    "Visarjan (immersion) procession"
                ]
            }
        ],
        
        cuisine: {
            introduction: "Maharashtrian cuisine is a delightful blend of coastal and inland flavors, characterized by its use of peanuts, coconut, and traditional spices. The food culture reflects the region's agricultural abundance and historical trading connections.",
            dishes: [
                {
                    name: "Vada Pav",
                    image: "assets/food/vada-pav.jpg",
                    description: "Often called Mumbai's burger, Vada Pav consists of a spiced potato fritter (batata vada) served in a pav (bread roll) with chutneys. This iconic street food represents the spirit of Maharashtra's working class and has become a cultural symbol.",
                    category: "Snack",
                    type: "Vegetarian",
                    occasion: "Daily street food, anytime snack",
                    culturalSignificance: "Symbol of Mumbai's fast-paced life and democratic food culture"
                }
            ]
        }
    }
};

// ==================== DATA LOADING FUNCTION ==================== //
// This function demonstrates how to load regional data into the page

function initializeRegionalPage(regionData) {
    console.log('Loading regional data for:', regionData.name);
    
    // Use the global function from regional-content.js
    if (window.VirasatRegionalPage && window.VirasatRegionalPage.loadRegionalContent) {
        window.VirasatRegionalPage.loadRegionalContent(regionData);
    }
}

// ==================== EXPORT ==================== //
// Export the template and sample data
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        regionalDataTemplate,
        sampleRegionData,
        initializeRegionalPage
    };
}

// ==================== USAGE INSTRUCTIONS ==================== //
/*

TO USE THIS TEMPLATE FOR YOUR 8 REGIONS:

1. Create 8 separate data files, one for each region:
   - regional-data-region1.js
   - regional-data-region2.js
   - etc.

2. Copy the regionalDataTemplate structure into each file

3. Fill in the actual cultural data you'll provide for each region

4. Load the appropriate regional data file based on which region page is being displayed

5. Call initializeRegionalPage(regionData) to populate the page

EXAMPLE:
// In your HTML or main script:
<script src="regional-data-maharashtra.js"></script>
<script>
    // After page loads
    initializeRegionalPage(maharashtraData);
</script>

The template is designed to be flexible - you can add or remove fields as needed
based on the actual data you have for each region.

*/
