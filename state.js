/**
 * VIRASAT — State / Cultural Exploration Controller
 * Handles state parameter resolution, category navigation shell, and guide interactions
 */

document.addEventListener('DOMContentLoaded', () => {

  // =========================================================
  // 1. Resolve State from URL Query Parameter
  // =========================================================
  const urlParams = new URLSearchParams(window.location.search);
  const stateQuery = (urlParams.get('state') || 'maharashtra').toLowerCase();

  // Retrieve state data from repository (fallback to Maharashtra)
  const stateData = (typeof VIRASAT_STATE_DATA !== 'undefined' && VIRASAT_STATE_DATA[stateQuery])
    ? VIRASAT_STATE_DATA[stateQuery]
    : (typeof VIRASAT_STATE_DATA !== 'undefined' ? VIRASAT_STATE_DATA['maharashtra'] : null);

  // =========================================================
  // 2. Populate Header & Metadata if Dynamic Data Exists
  // =========================================================
  if (stateData) {
    const breadcrumbState = document.getElementById('breadcrumbStateName');
    const stateDevanagari = document.getElementById('stateDevanagari');
    const stateRegion = document.getElementById('stateRegion');
    const stateHeading = document.getElementById('stateHeading');
    const stateTagline = document.getElementById('stateTagline');
    const stateIntroText = document.getElementById('stateIntroText');

    if (breadcrumbState) breadcrumbState.textContent = stateData.name;
    if (stateDevanagari) stateDevanagari.textContent = stateData.devanagari;
    if (stateRegion) stateRegion.textContent = stateData.region;
    if (stateHeading) stateHeading.textContent = stateData.name;
    if (stateTagline) stateTagline.textContent = stateData.tagline;
    if (stateIntroText) stateIntroText.textContent = stateData.intro;

    // Guide info
    if (stateData.guide) {
      const guideName = document.getElementById('guideName');
      const guideTitle = document.getElementById('guideTitle');
      const guideArchetype = document.getElementById('guideArchetype');
      const guideInitials = document.getElementById('guideInitials');
      const guideSpeechBubble = document.getElementById('guideSpeechBubble');
      const guideQuoteText = document.getElementById('guideQuoteText');

      if (guideName) guideName.textContent = stateData.guide.name;
      if (guideTitle) guideTitle.textContent = stateData.guide.title;
      if (guideArchetype) guideArchetype.textContent = stateData.guide.archetype;
      if (guideInitials) guideInitials.textContent = stateData.guide.avatarInitials;
      if (guideSpeechBubble) guideSpeechBubble.textContent = `“${stateData.guide.greeting}”`;
      if (guideQuoteText) guideQuoteText.textContent = stateData.guide.quote;
    }
  }

  // =========================================================
  // 3. Category Navigation Switching (Layout & Active State)
  // =========================================================
  const categoryBtns = document.querySelectorAll('.cat-nav-btn');
  const contentCategoryEyebrow = document.getElementById('contentCategoryEyebrow');
  const contentMainTitle = document.getElementById('contentMainTitle');
  const contentMainDesc = document.getElementById('contentMainDesc');

  const categoryHeadings = {
    culture: {
      eyebrow: "EXPLORATION • CULTURE & LIVING TRADITIONS",
      title: "Foundations of Maharashtrian Heritage",
      desc: "Explore key pillars that define Maharashtra's historical continuity — where ancient stone cave monasteries meet enduring saint traditions and defensive citadel architectures."
    },
    language: {
      eyebrow: "EXPLORATION • LANGUAGE & LITERATURE",
      title: "The Eloquence of Marathi & Regional Dialects",
      desc: "From the classical roots of Maharashtri Prakrit and Sant Dnyaneshwar’s Bhavartha Dipika to the vibrant cadence of Varhadi, Malvani, and Ahirani dialects."
    },
    art: {
      eyebrow: "EXPLORATION • VISUAL ARTS & CRAFTS",
      title: "Warli Murals, Cave Frescoes & Metalcraft",
      desc: "Indigenous ritual expressions of the Sahyadri tribes, Ajanta mineral pigments, and copper-bronze casting traditions of the Deccan plateau."
    },
    music: {
      eyebrow: "EXPLORATION • MUSICAL TRADITIONS",
      title: "Natya Sangeet, Abhangs & Folk Rhythms",
      desc: "Semi-classical theatrical music of Bal Gandharva, divine devotional abhangs of the Varkaris, and high-energy Dhol-Tasha festive beats."
    },
    dance: {
      eyebrow: "EXPLORATION • DANCE & PERFORMING ARTS",
      title: "Lavani, Lezim, Koli & Gondhal",
      desc: "Expressive footwork of Lavani theatre, the synchronized martial fitness of Lezim, rhythmic coastal Koli dances, and ceremonial Gondhal storytelling."
    },
    attire: {
      eyebrow: "EXPLORATION • TEXTILES & TRADITIONAL ATTIRE",
      title: "Paithani Weaves, Nauvari & Puneri Pagadi",
      desc: "Centuries-old royal silk borders handwoven with real gold zari, nine-yard Nauvari drapes worn by warrior queens, and distinguished regional turbans."
    },
    cuisine: {
      eyebrow: "EXPLORATION • CULINARY HERITAGE",
      title: "Coastal Malvani, Deshastha Thali & Street Flavors",
      desc: "Distinct spice balances of Goda masala, festive sweetness of Puran Poli and Ukdiche Modak, paired with fiery Kolhapuri rassa and coastal coconut curries."
    },
    festivals: {
      eyebrow: "EXPLORATION • SACRED FESTIVALS & PILGRIMAGES",
      title: "Ganeshotsav, Pandharpur Wari & Gudi Padwa",
      desc: "The monumental community solidarity of Sarvajanik Ganeshotsav, Maharashtra’s New Year celebration at Gudi Padwa, and the 800-year-old walking Wari."
    },
    places: {
      eyebrow: "EXPLORATION • HISTORIC PLACES & GEOGRAPHY",
      title: "Sahyadri Fortresses, Rock Sanctums & Coastlines",
      desc: "Impregnable sea forts of Sindhudurg and Murud-Janjira, Shivaji Maharaj's capital at Raigad, and the misty peaks of Western Ghat biosphere reserves."
    }
  };

  categoryBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      categoryBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const catKey = btn.getAttribute('data-category');
      const catInfo = categoryHeadings[catKey];

      if (catInfo) {
        if (contentCategoryEyebrow) contentCategoryEyebrow.textContent = catInfo.eyebrow;
        if (contentMainTitle) contentMainTitle.textContent = catInfo.title;
        if (contentMainDesc) contentMainDesc.textContent = catInfo.desc;
      }
    });
  });

  // =========================================================
  // 4. Virasat Cultural Guide Interactive Prompt Handling
  // =========================================================
  const promptChips = document.querySelectorAll('.prompt-chip-btn');
  const guideSpeechBubble = document.getElementById('guideSpeechBubble');

  const guideResponses = {
    "Ajanta & Ellora architecture": "Ajanta's 30 caves preserve 2,000-year-old Buddhist tempera murals painted with lapis lazuli and ochre. Ellora Cave 16 (Kailash Temple) is a world marvel — 200,000 tonnes of basalt carved top-down without joints or scaffolding!",
    "Pandharpur Wari history": "The Wari is an 800-year-old egalitarian pilgrimage where over one million Varkaris walk 250 km singing Saint Tukaram's abhangs, embodying casteless harmony and devotion to Lord Vithoba.",
    "Paithani silk craft": "Paithani sarees date back to the Satavahana dynasty (2nd c. BCE). Master weavers spend up to 18 months hand-interlocking pure silk and metallic gold zari to create signature Mor (peacock) motifs without reverse loose threads.",
    "Dhol Tasha tradition": "Dhol-Tasha troupes are the heartbeat of Maharashtra's Ganeshotsav. Originally popularized during the freedom movement to unite communities, their thunderous polyrhythms require immense discipline and stamina."
  };

  promptChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const promptKey = chip.getAttribute('data-prompt');
      const response = guideResponses[promptKey];
      if (response && guideSpeechBubble) {
        guideSpeechBubble.style.opacity = '0';
        setTimeout(() => {
          guideSpeechBubble.textContent = `“${response}”`;
          guideSpeechBubble.style.opacity = '1';
        }, 180);
      }
    });
  });

  // =========================================================
  // 5. Shared Procedural Web Audio Tanpura Ambience
  // =========================================================
  const ambientSoundToggle = document.getElementById('ambientSoundToggle');
  const audioStatusText = document.getElementById('audioStatusText');
  let audioCtx = null;
  let isAudioPlaying = false;
  let masterGain = null;

  function initAudio() {
    if (audioCtx) return;
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    audioCtx = new AudioContext();

    masterGain = audioCtx.createGain();
    masterGain.gain.setValueAtTime(0.001, audioCtx.currentTime);
    masterGain.connect(audioCtx.destination);

    const pitches = [138.59, 207.65, 277.18, 554.37]; // Sa-Pa tuning in C#

    pitches.forEach((freq, idx) => {
      const osc = audioCtx.createOscillator();
      const noteGain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc.type = idx % 2 === 0 ? 'sawtooth' : 'triangle';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(450 + idx * 80, audioCtx.currentTime);
      filter.Q.setValueAtTime(1.8, audioCtx.currentTime);

      const lfo = audioCtx.createOscillator();
      const lfoGain = audioCtx.createGain();
      lfo.frequency.setValueAtTime(0.15 + idx * 0.05, audioCtx.currentTime);
      lfoGain.gain.setValueAtTime(0.8, audioCtx.currentTime);
      lfo.connect(osc.frequency);
      lfo.start();

      noteGain.gain.setValueAtTime(0.08 / (idx + 1), audioCtx.currentTime);

      osc.connect(filter);
      filter.connect(noteGain);
      noteGain.connect(masterGain);

      osc.start();
    });
  }

  function toggleAudio() {
    initAudio();
    if (!audioCtx) return;

    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    if (!isAudioPlaying) {
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.25, audioCtx.currentTime + 2);
      isAudioPlaying = true;
      if (ambientSoundToggle) ambientSoundToggle.classList.add('playing');
      if (audioStatusText) audioStatusText.textContent = 'Live';
    } else {
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.0001, audioCtx.currentTime + 1);
      isAudioPlaying = false;
      if (ambientSoundToggle) ambientSoundToggle.classList.remove('playing');
      if (audioStatusText) audioStatusText.textContent = 'Off';
    }
  }

  if (ambientSoundToggle) {
    ambientSoundToggle.addEventListener('click', toggleAudio);
  }

});
