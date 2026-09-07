/**
 * VIRASAT — The Heritage of India
 * Landing Page Interactive Controller
 */

document.addEventListener('DOMContentLoaded', () => {

  // =========================================================
  // 1. DOM Elements
  // =========================================================
  const entryModal = document.getElementById('entryModal');
  const closeModalBtn = document.getElementById('closeModalBtn');
  const primaryCtaBtn = document.getElementById('primaryCtaBtn');
  const navSignInBtn = document.getElementById('navSignInBtn');
  const quickGuestBtn = document.getElementById('quickGuestBtn');
  const heroGuestBtn = document.getElementById('heroGuestBtn');
  const heroSignInLink = document.getElementById('heroSignInLink');
  const modalGuestEnterBtn = document.getElementById('modalGuestEnterBtn');
  const overviewCtaBtn = document.getElementById('overviewCtaBtn');
  const overviewGuestBtn = document.getElementById('overviewGuestBtn');
  const footerGuestBtn = document.getElementById('footerGuestBtn');
  const footerSignInBtn = document.getElementById('footerSignInBtn');

  // Auth Tabs
  const tabSignIn = document.getElementById('tabSignIn');
  const tabSignUp = document.getElementById('tabSignUp');
  const authSubmitBtn = document.getElementById('authSubmitBtn');
  const authBtnText = document.getElementById('authBtnText');
  const authForm = document.getElementById('authForm');

  // Welcome Toast
  const welcomeToast = document.getElementById('welcomeToast');
  const toastTitle = document.getElementById('toastTitle');
  const toastDesc = document.getElementById('toastDesc');

  // Pillar Cards & Modal
  const cardDiscover = document.getElementById('cardDiscover');
  const cardExperience = document.getElementById('cardExperience');
  const cardPlay = document.getElementById('cardPlay');
  const pillarModal = document.getElementById('pillarModal');
  const closePillarModalBtn = document.getElementById('closePillarModalBtn');
  const pillarModalContent = document.getElementById('pillarModalContent');

  // Ambient Audio Toggle
  const ambientSoundToggle = document.getElementById('ambientSoundToggle');
  const audioStatusText = document.getElementById('audioStatusText');


  // =========================================================
  // 2. Modal Management (Sign In / Guest Entry)
  // =========================================================
  function openEntryModal(defaultTab = 'guest') {
    if (!entryModal) return;
    entryModal.removeAttribute('hidden');
    document.body.style.overflow = 'hidden';

    if (defaultTab === 'signin') {
      setAuthTab('signin');
    } else if (defaultTab === 'signup') {
      setAuthTab('signup');
    }
  }

  function closeEntryModal() {
    if (!entryModal) return;
    entryModal.setAttribute('hidden', '');
    document.body.style.overflow = '';
  }

  function setAuthTab(tab) {
    if (tab === 'signup') {
      tabSignUp.classList.add('active');
      tabSignUp.setAttribute('aria-selected', 'true');
      tabSignIn.classList.remove('active');
      tabSignIn.setAttribute('aria-selected', 'false');
      authBtnText.textContent = 'Create Account & Begin';
    } else {
      tabSignIn.classList.add('active');
      tabSignIn.setAttribute('aria-selected', 'true');
      tabSignUp.classList.remove('active');
      tabSignUp.setAttribute('aria-selected', 'false');
      authBtnText.textContent = 'Sign In to Virasat';
    }
  }

  // Event Listeners for Opening Modal
  if (primaryCtaBtn) primaryCtaBtn.addEventListener('click', () => openEntryModal('guest'));
  if (navSignInBtn) navSignInBtn.addEventListener('click', () => openEntryModal('signin'));
  if (heroSignInLink) heroSignInLink.addEventListener('click', () => openEntryModal('signin'));
  if (overviewCtaBtn) overviewCtaBtn.addEventListener('click', () => openEntryModal('guest'));
  if (footerSignInBtn) footerSignInBtn.addEventListener('click', () => openEntryModal('signin'));

  // Close handlers
  if (closeModalBtn) closeModalBtn.addEventListener('click', closeEntryModal);
  if (entryModal) {
    entryModal.addEventListener('click', (e) => {
      if (e.target === entryModal) closeEntryModal();
    });
  }

  if (tabSignIn) tabSignIn.addEventListener('click', () => setAuthTab('signin'));
  if (tabSignUp) tabSignUp.addEventListener('click', () => setAuthTab('signup'));


  // =========================================================
  // 3. Frictionless "Continue as Guest" Flow
  // =========================================================
  function triggerGuestAccess(sourceName = 'Guest') {
    closeEntryModal();
    closePillarModal();

    // Show celebratory feedback toast
    if (welcomeToast && toastTitle && toastDesc) {
      toastTitle.textContent = `Welcome, Explorer! (Guest Mode)`;
      toastDesc.textContent = `Access granted to all 28 States & 8 UTs. Unlocking cultural journeys...`;
      welcomeToast.classList.add('show');

      // Auto-hide toast after 4.5 seconds
      setTimeout(() => {
        welcomeToast.classList.remove('show');
      }, 4500);
    }

    // Play subtle chime if audio is enabled
    playChimeEffect();
  }

  // Bind all "Continue as Guest" triggers
  const guestTriggers = [quickGuestBtn, heroGuestBtn, modalGuestEnterBtn, overviewGuestBtn, footerGuestBtn];
  guestTriggers.forEach(btn => {
    if (btn) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        triggerGuestAccess('Guest');
      });
    }
  });

  // Auth Form Submit
  if (authForm) {
    authForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('inputEmail').value;
      closeEntryModal();

      if (welcomeToast && toastTitle && toastDesc) {
        toastTitle.textContent = `Welcome back to Virasat!`;
        toastDesc.textContent = `Signed in as ${email}. Syncing your cultural journey...`;
        welcomeToast.classList.add('show');

        setTimeout(() => {
          welcomeToast.classList.remove('show');
        }, 4500);
      }
      playChimeEffect();
    });
  }


  // =========================================================
  // 4. Pillar Card Previews & Detail Modal
  // =========================================================
  const pillarData = {
    discover: {
      tag: 'PILLAR 01 • DISCOVER',
      title: 'The Cultural Atlas of India',
      highlight: 'Interactive 3D Mapping of 28 States & 8 Union Territories',
      iconClass: 'icon-discover',
      iconSvg: `<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>`,
      description: 'The Cultural Atlas provides an interactive, state-by-state geographic journey across India. Each region unfolds into historic forts, temple architecture, stepwells, sacred riverbanks, and distinct biodiversity sanctuaries.',
      samples: [
        { name: 'Architectural Sanctums', desc: 'Hampi, Khajuraho, Tanjore Brihadeeswarar & Konark' },
        { name: 'Tribal Belts & Crafts', desc: 'Bastar metal craft, Warli art, Dhokra bronze casting' },
        { name: 'Living Landscapes', desc: 'Himalayan monasteries to Sundarbans water folklore' },
        { name: 'Regional Gateways', desc: 'Delhi Lal Qila, Jodhpur Mehrangarh, Mysore Palace' }
      ]
    },
    experience: {
      tag: 'PILLAR 02 • EXPERIENCE',
      title: 'Living Stories & Sensory Journeys',
      highlight: 'Folk Traditions, Classical Performing Arts, Master Crafts & Cuisine',
      iconClass: 'icon-experience',
      iconSvg: `<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>`,
      description: 'Step directly into living traditions. Through audio-visual narration, master artisan demonstrations, and regional culinary tales, experience how culture lives in daily rituals, festive celebrations, and seasonal songs.',
      samples: [
        { name: 'Classical & Folk Dances', desc: 'Kathakali mudras, Ghoomar spins, Bihu celebrations' },
        { name: 'Textile Heritage', desc: 'Kanchipuram silk, Pashmina weaving, Banarasi brocade' },
        { name: 'Culinary Chronicles', desc: 'Spice routes, regional thalis, sacred prasad recipes' },
        { name: 'Oral Legends & Epics', desc: 'Folk ballads, puppet lore, and oral family histories' }
      ]
    },
    play: {
      tag: 'PILLAR 03 • PLAY',
      title: 'Cultural Quests & Collectible Badges',
      highlight: 'Gamified Challenges, Milestone XP, Streaks & Heritage Cards',
      iconClass: 'icon-play',
      iconSvg: `<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>`,
      description: 'Gamification engineered to deepen reverence and retention. Solve visual pattern challenges, identify monument spires, test your regional dialect knowledge, and build your digital heritage collection.',
      samples: [
        { name: 'Collectible Heritage Cards', desc: 'Rare cards for historic monuments & folk instruments' },
        { name: 'Regional Trivia Quests', desc: 'Bite-sized quizzes with rich contextual explanations' },
        { name: 'Cultural Avatar Badges', desc: 'Unlock regional turbans, sarees, jewelry & regalia' },
        { name: 'National Leaderboard', desc: 'Celebrate cultural learning milestones with friends' }
      ]
    }
  };

  function openPillarModal(pillarKey) {
    const data = pillarData[pillarKey];
    if (!data || !pillarModalContent) return;

    pillarModalContent.innerHTML = `
      <div class="pm-header">
        <div class="pm-icon ${data.iconClass}">
          ${data.iconSvg}
        </div>
        <div class="pm-title-group">
          <span>${data.tag}</span>
          <h3>${data.title}</h3>
        </div>
      </div>
      <p class="pm-highlight" style="color: var(--ei-terracotta); font-weight: 600; font-size: 0.95rem;">${data.highlight}</p>
      <p class="pm-description">${data.description}</p>
      <div class="pm-samples-list">
        ${data.samples.map(s => `
          <div class="pm-sample-item">
            <span class="pm-sample-name">${s.name}</span>
            <span class="pm-sample-desc">${s.desc}</span>
          </div>
        `).join('')}
      </div>
      <div style="margin-top: 1rem; display: flex; gap: 0.8rem; align-items: center;">
        <button class="btn-guest-enter" id="pmExploreBtn" style="padding: 0.6rem 1.2rem; font-size: 0.88rem;">
          Try This Feature as Guest
        </button>
      </div>
    `;

    pillarModal.removeAttribute('hidden');
    document.body.style.overflow = 'hidden';

    // Hook the inner CTA
    const pmExploreBtn = document.getElementById('pmExploreBtn');
    if (pmExploreBtn) {
      pmExploreBtn.addEventListener('click', () => triggerGuestAccess());
    }
  }

  function closePillarModal() {
    if (!pillarModal) return;
    pillarModal.setAttribute('hidden', '');
    document.body.style.overflow = '';
  }

  if (cardDiscover) cardDiscover.addEventListener('click', () => openPillarModal('discover'));
  if (cardExperience) cardExperience.addEventListener('click', () => openPillarModal('experience'));
  if (cardPlay) cardPlay.addEventListener('click', () => openPillarModal('play'));

  // Nav links to pillars
  document.querySelectorAll('.nav-link[data-pillar]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const p = link.getAttribute('data-pillar');
      openPillarModal(p);
    });
  });

  if (closePillarModalBtn) closePillarModalBtn.addEventListener('click', closePillarModal);
  if (pillarModal) {
    pillarModal.addEventListener('click', (e) => {
      if (e.target === pillarModal) closePillarModal();
    });
  }

  // Keyboard accessibility
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeEntryModal();
      closePillarModal();
    }
  });


  // =========================================================
  // 5. Canvas Floating Golden Dust / Diya Particles
  // =========================================================
  const canvas = document.getElementById('particlesCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];
    const particleCount = 38;

    function resizeCanvas() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    class Particle {
      constructor() {
        this.reset();
      }
      reset() {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = Math.random() * 2.4 + 0.8;
        this.speedX = (Math.random() - 0.5) * 0.4;
        this.speedY = -Math.random() * 0.45 - 0.15; // float gently upward like diya embers
        this.opacity = Math.random() * 0.7 + 0.2;
        this.fadeSpeed = Math.random() * 0.008 + 0.003;
        this.increasing = Math.random() > 0.5;
      }
      update() {
        this.x += this.speedX;
        this.y += this.speedY;

        // Twinkle
        if (this.increasing) {
          this.opacity += this.fadeSpeed;
          if (this.opacity >= 0.85) this.increasing = false;
        } else {
          this.opacity -= this.fadeSpeed;
          if (this.opacity <= 0.15) this.increasing = true;
        }

        // Out of bounds reset
        if (this.y < -10 || this.x < -10 || this.x > width + 10) {
          this.y = height + 10;
          this.x = Math.random() * width;
        }
      }
      draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(212, 175, 55, ${this.opacity})`;
        ctx.shadowBlur = 8;
        ctx.shadowColor = 'rgba(245, 200, 80, 0.6)';
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    }

    for (let i = 0; i < particleCount; i++) {
      particles.push(new Particle());
    }

    function animateParticles() {
      ctx.clearRect(0, 0, width, height);
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      requestAnimationFrame(animateParticles);
    }
    animateParticles();
  }


  // =========================================================
  // 6. Generative Indian Tanpura Ambience (Web Audio API)
  // =========================================================
  let audioCtx = null;
  let isAudioPlaying = false;
  let oscillators = [];
  let masterGain = null;

  function initAudio() {
    if (audioCtx) return;
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    audioCtx = new AudioContext();

    masterGain = audioCtx.createGain();
    masterGain.gain.setValueAtTime(0.001, audioCtx.currentTime);
    masterGain.connect(audioCtx.destination);

    // Traditional Tanpura tuning in C# (Sa-Pa drone)
    // C#3 = 138.59 Hz (Sa), G#3 = 207.65 Hz (Pa), C#4 = 277.18 Hz (Sa oct)
    const pitches = [138.59, 207.65, 277.18, 554.37];

    pitches.forEach((freq, idx) => {
      const osc = audioCtx.createOscillator();
      const noteGain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc.type = idx % 2 === 0 ? 'sawtooth' : 'triangle';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      // Warm low-pass filter for rich wooden acoustic tone
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(450 + idx * 80, audioCtx.currentTime);
      filter.Q.setValueAtTime(1.8, audioCtx.currentTime);

      // Subtle slow pitch drift (vibrato/chorus)
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
      oscillators.push(osc);
    });
  }

  function toggleAudio() {
    initAudio();
    if (!audioCtx) return;

    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    if (!isAudioPlaying) {
      // Fade in gently
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.28, audioCtx.currentTime + 2.5);
      isAudioPlaying = true;
      if (ambientSoundToggle) ambientSoundToggle.classList.add('playing');
      if (audioStatusText) audioStatusText.textContent = 'Live';
    } else {
      // Fade out
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);
      isAudioPlaying = false;
      if (ambientSoundToggle) ambientSoundToggle.classList.remove('playing');
      if (audioStatusText) audioStatusText.textContent = 'Off';
    }
  }

  if (ambientSoundToggle) {
    ambientSoundToggle.addEventListener('click', toggleAudio);
  }

  // Short pleasant chime feedback when entering as guest
  function playChimeEffect() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) return;
      const ctx = audioCtx || new AudioContext();
      if (ctx.state === 'suspended') ctx.resume();

      const chimeNotes = [554.37, 659.25, 830.61, 1108.73]; // C# E G# C# pentatonic arpeggio
      chimeNotes.forEach((freq, i) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, ctx.currentTime + i * 0.12);

        gain.gain.setValueAtTime(0.001, ctx.currentTime + i * 0.12);
        gain.gain.linearRampToValueAtTime(0.12, ctx.currentTime + i * 0.12 + 0.04);
        gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + i * 0.12 + 1.2);

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(ctx.currentTime + i * 0.12);
        osc.stop(ctx.currentTime + i * 0.12 + 1.3);
      });
    } catch (err) {
      // Audio not permitted or supported; silent fallback
    }
  }

});
