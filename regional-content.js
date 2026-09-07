// VIRASAT Regional Cultural Content Page - JavaScript

// ==================== SMOOTH NAVIGATION ==================== //
document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeChatbot();
    initializeSuggestions();
    initializeScrollSpy();
    initializeMobileMenu();
});

// ==================== NAVIGATION FUNCTIONALITY ==================== //
function initializeNavigation() {
    const navLinks = document.querySelectorAll('.nav-link, .nav-sublist a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            
            // Check if it's an internal link
            if (href && href.startsWith('#')) {
                e.preventDefault();
                
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    // Smooth scroll to section
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // Update active state
                    updateActiveNavItem(this);
                }
            }
        });
    });
}

// Update active navigation item
function updateActiveNavItem(clickedLink) {
    // Remove active class from all nav items
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
    });
    
    // Add active class to parent nav-item
    const parentNavItem = clickedLink.closest('.nav-item');
    if (parentNavItem) {
        parentNavItem.classList.add('active');
    }
}

// ==================== SCROLL SPY ==================== //
function initializeScrollSpy() {
    const sections = document.querySelectorAll('.content-section');
    const navItems = document.querySelectorAll('.nav-item');
    
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px',
        threshold: 0
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.id;
                
                // Update navigation
                navItems.forEach(item => {
                    item.classList.remove('active');
                    const link = item.querySelector(`a[href="#${sectionId}"]`);
                    if (link) {
                        item.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });
}

// ==================== CHATBOT FUNCTIONALITY ==================== //
function initializeChatbot() {
    const chatInput = document.querySelector('.chat-input');
    const sendBtn = document.querySelector('.send-btn');
    const chatMessages = document.querySelector('.chat-messages');
    
    if (sendBtn && chatInput && chatMessages) {
        sendBtn.addEventListener('click', function() {
            sendMessage(chatInput, chatMessages);
        });
        
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage(chatInput, chatMessages);
            }
        });
    }
}

function sendMessage(inputElement, messagesContainer) {
    const message = inputElement.value.trim();
    
    if (message) {
        // Add user message
        addMessageToChat(message, 'user', messagesContainer);
        
        // Clear input
        inputElement.value = '';
        
        // Simulate AI response (in production, this would call an API)
        setTimeout(() => {
            const aiResponse = generateAIResponse(message);
            addMessageToChat(aiResponse, 'ai', messagesContainer);
        }, 1000);
    }
}

function addMessageToChat(message, sender, container) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${sender}-message`;
    
    const messageContent = document.createElement('p');
    messageContent.textContent = message;
    
    messageDiv.appendChild(messageContent);
    container.appendChild(messageDiv);
    
    // Scroll to bottom
    container.scrollTop = container.scrollHeight;
    
    // Add animation
    messageDiv.style.animation = 'fadeIn 0.4s ease-out';
}

// Simulate AI responses (placeholder for actual AI integration)
function generateAIResponse(userMessage) {
    const responses = {
        'default': "I'm Shrishti, your cultural guide. I'd be happy to tell you more about this region's rich heritage. Could you be more specific about what aspect interests you?",
        'festival': "The festivals of this region are deeply rooted in ancient traditions and agricultural cycles. Each celebration tells a story of the land and its people.",
        'food': "The cuisine here reflects centuries of cultural exchange and local agricultural bounty. Traditional cooking methods preserve authentic flavors passed down through generations.",
        'art': "The art forms of this region are living traditions, with techniques and knowledge transferred from master to student over centuries.",
        'history': "This region has a fascinating historical legacy that shaped not just local culture but influenced the broader cultural tapestry of India.",
        'place': "The historical monuments here stand as testament to the architectural brilliance and cultural sophistication of ancient times."
    };
    
    const lowerMessage = userMessage.toLowerCase();
    
    if (lowerMessage.includes('festival') || lowerMessage.includes('celebration')) {
        return responses.festival;
    } else if (lowerMessage.includes('food') || lowerMessage.includes('cuisine') || lowerMessage.includes('dish')) {
        return responses.food;
    } else if (lowerMessage.includes('art') || lowerMessage.includes('dance') || lowerMessage.includes('music')) {
        return responses.art;
    } else if (lowerMessage.includes('history') || lowerMessage.includes('historical')) {
        return responses.history;
    } else if (lowerMessage.includes('place') || lowerMessage.includes('monument') || lowerMessage.includes('temple')) {
        return responses.place;
    } else {
        return responses.default;
    }
}

// Add styles for chat messages dynamically
const chatStyles = document.createElement('style');
chatStyles.textContent = `
    .chat-message {
        margin-bottom: 1rem;
        padding: 0.75rem;
        border-radius: 8px;
        animation: fadeIn 0.4s ease-out;
    }
    
    .user-message {
        background: linear-gradient(135deg, var(--olive-dark) 0%, var(--forest-green) 100%);
        color: var(--white);
        margin-left: 2rem;
        border-bottom-right-radius: 2px;
    }
    
    .ai-message {
        background: var(--sand-beige);
        color: var(--text-primary);
        margin-right: 2rem;
        border-bottom-left-radius: 2px;
        border-left: 3px solid var(--terracotta);
    }
    
    .chat-message p {
        margin: 0;
        font-size: 0.9rem;
        line-height: 1.6;
    }
`;
document.head.appendChild(chatStyles);

// ==================== SUGGESTION BUTTONS ==================== //
function initializeSuggestions() {
    const suggestionBtns = document.querySelectorAll('.suggestion-btn');
    const chatInput = document.querySelector('.chat-input');
    const chatMessages = document.querySelector('.chat-messages');
    
    suggestionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const question = this.textContent.trim();
            
            if (chatInput && chatMessages) {
                // Add question to chat
                addMessageToChat(question, 'user', chatMessages);
                
                // Generate AI response
                setTimeout(() => {
                    const aiResponse = generateAIResponse(question);
                    addMessageToChat(aiResponse, 'ai', chatMessages);
                }, 1000);
            }
        });
    });
}

// ==================== MOBILE MENU TOGGLE ==================== //
function initializeMobileMenu() {
    // Create mobile menu toggle button
    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'mobile-menu-toggle';
    toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
    toggleBtn.setAttribute('aria-label', 'Toggle navigation menu');
    
    // Insert at beginning of body
    document.body.insertBefore(toggleBtn, document.body.firstChild);
    
    const sidebar = document.querySelector('.cultural-sidebar');
    
    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('open');
        this.classList.toggle('active');
        
        // Change icon
        const icon = this.querySelector('i');
        if (sidebar.classList.contains('open')) {
            icon.className = 'fas fa-times';
        } else {
            icon.className = 'fas fa-bars';
        }
    });
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 1200) {
            if (!sidebar.contains(e.target) && !toggleBtn.contains(e.target)) {
                sidebar.classList.remove('open');
                toggleBtn.classList.remove('active');
                toggleBtn.querySelector('i').className = 'fas fa-bars';
            }
        }
    });
}

// Add mobile menu button styles
const mobileMenuStyles = document.createElement('style');
mobileMenuStyles.textContent = `
    .mobile-menu-toggle {
        display: none;
        position: fixed;
        top: 1rem;
        left: 1rem;
        z-index: 1001;
        width: 48px;
        height: 48px;
        background: linear-gradient(135deg, var(--terracotta) 0%, var(--deep-maroon) 100%);
        color: var(--white);
        border: none;
        border-radius: 8px;
        font-size: 1.2rem;
        cursor: pointer;
        box-shadow: 0 4px 12px var(--shadow-medium);
        transition: transform 0.2s ease;
    }
    
    .mobile-menu-toggle:hover {
        transform: scale(1.05);
    }
    
    .mobile-menu-toggle:active {
        transform: scale(0.95);
    }
    
    @media (max-width: 1200px) {
        .mobile-menu-toggle {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .main-content {
            padding-top: 5rem;
        }
    }
`;
document.head.appendChild(mobileMenuStyles);

// ==================== IMAGE LAZY LOADING ==================== //
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// ==================== CARD HOVER EFFECTS ==================== //
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.festival-card, .food-card, .craft-card, .monument-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

// ==================== REGIONAL DATA LOADER ==================== //
// This function would be used to load regional data dynamically
function loadRegionalContent(regionData) {
    // Update region name
    const regionNameElements = document.querySelectorAll('.region-name, .avatar-region');
    regionNameElements.forEach(el => {
        el.textContent = regionData.name;
    });
    
    // Update regional avatar
    const avatarImg = document.querySelector('.regional-avatar');
    if (avatarImg && regionData.avatar) {
        avatarImg.src = regionData.avatar;
        avatarImg.alt = `${regionData.name} Cultural Guide`;
    }
    
    // Update header image
    const headerImg = document.querySelector('.header-image img');
    if (headerImg && regionData.headerImage) {
        headerImg.src = regionData.headerImage;
        headerImg.alt = regionData.name;
    }
    
    // Update introduction text
    const introText = document.querySelector('.intro-text');
    if (introText && regionData.introduction) {
        introText.textContent = regionData.introduction;
    }
    
    // Load section content
    if (regionData.sections) {
        loadSectionContent(regionData.sections);
    }
    
    console.log(`Loaded content for: ${regionData.name}`);
}

function loadSectionContent(sections) {
    // This would populate each section with the provided data
    // Implementation would depend on the structure of your data
    
    Object.keys(sections).forEach(sectionKey => {
        const sectionData = sections[sectionKey];
        const sectionElement = document.getElementById(sectionKey);
        
        if (sectionElement && sectionData) {
            // Dynamically generate content based on section type
            // This is where you'd transform the data into the appropriate UI components
            console.log(`Loading section: ${sectionKey}`);
        }
    });
}

// ==================== EXPORT FOR EXTERNAL USE ==================== //
window.VirasatRegionalPage = {
    loadRegionalContent: loadRegionalContent,
    updateActiveNavItem: updateActiveNavItem
};

// ==================== ACCESSIBILITY ENHANCEMENTS ==================== //
document.addEventListener('DOMContentLoaded', function() {
    // Add skip to content link
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link';
    skipLink.textContent = 'Skip to main content';
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Add aria-current to active nav items
    const navItems = document.querySelectorAll('.nav-item');
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'class') {
                const target = mutation.target;
                const link = target.querySelector('.nav-link');
                if (link) {
                    if (target.classList.contains('active')) {
                        link.setAttribute('aria-current', 'page');
                    } else {
                        link.removeAttribute('aria-current');
                    }
                }
            }
        });
    });
    
    navItems.forEach(item => {
        observer.observe(item, { attributes: true });
    });
});

// Add skip link styles
const skipLinkStyles = document.createElement('style');
skipLinkStyles.textContent = `
    .skip-link {
        position: absolute;
        top: -40px;
        left: 0;
        background: var(--deep-maroon);
        color: var(--white);
        padding: 8px 16px;
        text-decoration: none;
        z-index: 10000;
        border-radius: 0 0 4px 0;
    }
    
    .skip-link:focus {
        top: 0;
    }
`;
document.head.appendChild(skipLinkStyles);

console.log('VIRASAT Regional Content Page initialized successfully');
