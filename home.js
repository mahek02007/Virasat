/**
 * VIRASAT — The Heritage of India
 * Home Page Controller: Interactive Cultural Atlas & Explorations
 */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Central Data Verification
  const data = window.VIRASAT_DATA;
  if (!data) {
    console.error('VIRASAT_DATA repository not loaded.');
    return;
  }

  // =========================================================
  // 2. DOM Elements Selection
  // =========================================================
  const mapInteractiveLayer = document.getElementById('mapInteractiveLayer');
  const regionPopover = document.getElementById('regionPopover');
  const quickRegionsBar = document.getElementById('quickRegionsBar');
  const zoneFiltersStrip = document.getElementById('zoneFiltersStrip');

  // Search Elements
  const searchInput = document.getElementById('headerSearchInput');
  const searchDropdown = document.getElementById('searchResultsDropdown');
  const searchClearBtn = document.getElementById('searchClearBtn');

  // Profile Dropdown
  const profileToggleBtn = document.getElementById('profileToggleBtn');
  const profileDropdown = document.getElementById('profileDropdown');

  // Journey & Avatar Elements
  const journeyProgressFill = document.getElementById('journeyProgressFill');
  const journeyCountText = document.getElementById('journeyCountText');
  const journeyPercentText = document.getElementById('journeyPercentText');
  const avatarGreetingNative = document.getElementById('avatarGreetingNative');
  const avatarGreetingRoman = document.getElementById('avatarGreetingRoman');
  const cycleGreetingBtn = document.getElementById('cycleGreetingBtn');
  const playVoiceoverBtn = document.getElementById('playVoiceoverBtn');
  const voiceStatusText = document.getElementById('voiceStatusText');
  const avatarSpeechBubble = document.getElementById('avatarSpeechBubble');
  const avatarFrame = document.getElementById('avatarFrame');

  // Did You Know Elements
  const dykTag = document.getElementById('dykTag');
  const dykRegion = document.getElementById('dykRegion');
  const dykQuote = document.getElementById('dykQuote');
  const dykDesc = document.getElementById('dykDesc');
  const dykStoryLink = document.getElementById('dykStoryLink');
  const dykNextBtn = document.getElementById('dykNextBtn');

  // Audio Ambience Pill
  const homeAudioToggle = document.getElementById('homeAudioToggle');
  const homeAudioStatus = document.getElementById('homeAudioStatus');


  // =========================================================
  // 3. Interactive Map & Region Beacons
  // =========================================================
  let activeRegionId = null;
  let currentZoneFilter = 'all';

  function renderRegionBeacons() {
    if (!mapInteractiveLayer) return;
    mapInteractiveLayer.innerHTML = '';

    data.regions.forEach(region => {
      const beaconBtn = document.createElement('button');
      beaconBtn.className = 'region-beacon';
      beaconBtn.id = `beacon-${region.id}`;
      beaconBtn.setAttribute('data-region-id', region.id);
      beaconBtn.setAttribute('data-zone', region.zone);
      beaconBtn.setAttribute('aria-label', `Explore ${region.name} - ${region.tagline}`);
      
      // Position percentage coordinates
      beaconBtn.style.left = `${region.coords.x}%`;
      beaconBtn.style.top = `${region.coords.y}%`;

      beaconBtn.innerHTML = `
        <span class="beacon-core">
          <span class="beacon-pulse" style="background: ${region.colorAccent || 'rgba(200,90,50,0.45)'}"></span>
          <span class="beacon-dot" style="background: ${region.colorAccent || 'var(--ei-terracotta)'}"></span>
        </span>
        <span class="beacon-label">${region.name}</span>
      `;

      // Hover / Focus handlers
      beaconBtn.addEventListener('mouseenter', () => showRegionPopover(region, beaconBtn));
      beaconBtn.addEventListener('focus', () => showRegionPopover(region, beaconBtn));

      // Click to Navigate to Explore
      beaconBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        navigateToRegion(region.id);
      });

      mapInteractiveLayer.appendChild(beaconBtn);
    });
  }

  function showRegionPopover(region, anchorEl) {
    if (!regionPopover) return;
    activeRegionId = region.id;

    // Populate Popover Content
    regionPopover.innerHTML = `
      <div class="popover-header">
        <div class="popover-name-block">
          <span class="popover-region-name">${region.name}</span>
          <span class="popover-devanagari">${region.devanagari || ''}</span>
        </div>
        <span class="popover-status-badge">${region.badge || 'Available'}</span>
      </div>
      <p class="popover-tagline">${region.tagline}</p>
      <div class="popover-categories-chips">
        ${region.categories.map(c => `<span class="popover-category-chip">${c}</span>`).join('')}
      </div>
      <p style="font-size: 0.78rem; line-height: 1.45; color: var(--color-parchment-muted); margin-bottom: 0.85rem;">
        ${region.summary}
      </p>
      <a href="${['maharashtra','odisha'].includes(region.id) ? `regional-content.html?region=${region.id}` : `explore.html?region=${region.id}`}" class="popover-explore-cta" id="popoverCtaLink">
        <span>Explore ${region.name}</span>
        <svg viewBox="0 0 20 20" width="16" height="16" fill="currentColor">
          <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
        </svg>
      </a>
    `;

    // Position popover relative to map container
    const mapRect = mapInteractiveLayer.getBoundingClientRect();
    const anchorRect = anchorEl.getBoundingClientRect();

    let leftPercent = region.coords.x;
    let topPercent = region.coords.y;

    // Keep popover inside horizontal bounds
    if (leftPercent < 22) leftPercent = 22;
    if (leftPercent > 78) leftPercent = 78;

    regionPopover.style.left = `${leftPercent}%`;
    regionPopover.style.top = `${topPercent}%`;
    regionPopover.classList.add('active');

    // Highlight beacon
    document.querySelectorAll('.region-beacon').forEach(b => b.classList.remove('active'));
    anchorEl.classList.add('active');

    // Highlight matching pill in quick bar
    document.querySelectorAll('.quick-region-pill').forEach(pill => {
      pill.classList.toggle('active', pill.getAttribute('data-region') === region.id);
    });
  }

  function hideRegionPopover() {
    if (regionPopover) {
      regionPopover.classList.remove('active');
    }
    document.querySelectorAll('.region-beacon').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.quick-region-pill').forEach(p => p.classList.remove('active'));
    activeRegionId = null;
  }

  function navigateToRegion(regionId) {
    // Regions with fully-populated regional content pages
    const regionalContentRegions = ['maharashtra', 'odisha'];
    if (regionalContentRegions.includes(regionId)) {
      window.location.href = `regional-content.html?region=${encodeURIComponent(regionId)}`;
      return;
    }
    // All other regions route to explore.html?region=[id]
    window.location.href = `explore.html?region=${encodeURIComponent(regionId)}`;
  }

  // Zone Filters (All, North, West, South, East, Central, Northeast)
  if (zoneFiltersStrip) {
    zoneFiltersStrip.addEventListener('click', (e) => {
      const btn = e.target.closest('.zone-filter-pill');
      if (!btn) return;

      const zone = btn.getAttribute('data-zone');
      currentZoneFilter = zone;

      document.querySelectorAll('.zone-filter-pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');

      // Filter beacons
      document.querySelectorAll('.region-beacon').forEach(beacon => {
        const bZone = beacon.getAttribute('data-zone');
        if (zone === 'all' || bZone === zone) {
          beacon.classList.remove('dimmed');
        } else {
          beacon.classList.add('dimmed');
        }
      });

      hideRegionPopover();
    });
  }

  // Quick Regions Pill Strip
  if (quickRegionsBar) {
    quickRegionsBar.addEventListener('click', (e) => {
      const pill = e.target.closest('.quick-region-pill');
      if (!pill) return;
      const regId = pill.getAttribute('data-region');
      const targetRegion = data.regions.find(r => r.id === regId);
      const beaconBtn = document.getElementById(`beacon-${regId}`);
      if (targetRegion && beaconBtn) {
        showRegionPopover(targetRegion, beaconBtn);
        beaconBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  }

  // Hide popover when clicking anywhere outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.region-popover-card') && !e.target.closest('.region-beacon') && !e.target.closest('.quick-region-pill')) {
      hideRegionPopover();
    }
  });


  // =========================================================
  // 4. Cultural Search Engine & Dropdown
  // =========================================================
  function initSearchEngine() {
    if (!searchInput || !searchDropdown) return;

    let highlightedIdx = -1;
    let filteredItems = [];

    function handleSearchInput() {
      const query = searchInput.value.trim().toLowerCase();
      if (searchClearBtn) {
        searchClearBtn.classList.toggle('visible', query.length > 0);
      }

      if (query.length < 1) {
        searchDropdown.classList.remove('active');
        searchDropdown.innerHTML = '';
        filteredItems = [];
        return;
      }

      // Filter searchIndex items
      filteredItems = data.searchIndex.filter(item => {
        const matchTitle = item.title.toLowerCase().includes(query);
        const matchSub = item.subtitle.toLowerCase().includes(query);
        const matchKeywords = item.queryMatch && item.queryMatch.some(k => k.includes(query));
        return matchTitle || matchSub || matchKeywords;
      });

      renderSearchResults(query, filteredItems);
    }

    function renderSearchResults(query, items) {
      if (items.length === 0) {
        searchDropdown.innerHTML = `
          <div class="search-empty-state">
            <p>No heritage matches found for <strong>"${escapeHtml(query)}"</strong></p>
            <p style="font-size: 0.74rem; color: var(--color-gold); margin-top: 0.35rem;">
              Try: "Rajasthan", "Ajanta", "Kathak", "Diwali", "Brihadeeswarar"
            </p>
          </div>
        `;
        searchDropdown.classList.add('active');
        return;
      }

      // Group items by Type
      const grouped = {};
      items.forEach(item => {
        if (!grouped[item.type]) grouped[item.type] = [];
        grouped[item.type].push(item);
      });

      let html = '';
      Object.keys(grouped).forEach(type => {
        html += `<div class="search-category-group">`;
        html += `<div class="search-category-title">${type}s</div>`;
        grouped[type].forEach(item => {
          html += `
            <a href="${item.url}" class="search-item" data-region-id="${item.regionId || ''}">
              <div class="search-item-info">
                <span class="search-item-title">${highlightMatch(item.title, query)}</span>
                <span class="search-item-sub">${highlightMatch(item.subtitle, query)}</span>
              </div>
              <span class="search-item-type">${item.type}</span>
            </a>
          `;
        });
        html += `</div>`;
      });

      searchDropdown.innerHTML = html;
      searchDropdown.classList.add('active');
      highlightedIdx = -1;

      // Bind search items click
      searchDropdown.querySelectorAll('.search-item').forEach(itemEl => {
        itemEl.addEventListener('click', (e) => {
          const regionId = itemEl.getAttribute('data-region-id');
          if (regionId) {
            // Also highlight beacon on map
            const beacon = document.getElementById(`beacon-${regionId}`);
            const regionData = data.regions.find(r => r.id === regionId);
            if (beacon && regionData) {
              showRegionPopover(regionData, beacon);
            }
          }
        });
      });
    }

    searchInput.addEventListener('input', handleSearchInput);

    if (searchClearBtn) {
      searchClearBtn.addEventListener('click', () => {
        searchInput.value = '';
        handleSearchInput();
        searchInput.focus();
      });
    }

    // Keyboard navigation (Arrow keys + Enter + Escape)
    searchInput.addEventListener('keydown', (e) => {
      const items = searchDropdown.querySelectorAll('.search-item');
      if (!items.length) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        highlightedIdx = (highlightedIdx + 1) % items.length;
        updateSearchHighlight(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        highlightedIdx = (highlightedIdx - 1 + items.length) % items.length;
        updateSearchHighlight(items);
      } else if (e.key === 'Enter') {
        if (highlightedIdx >= 0 && items[highlightedIdx]) {
          e.preventDefault();
          items[highlightedIdx].click();
        }
      } else if (e.key === 'Escape') {
        searchDropdown.classList.remove('active');
      }
    });

    function updateSearchHighlight(items) {
      items.forEach((it, idx) => {
        it.classList.toggle('highlighted', idx === highlightedIdx);
        if (idx === highlightedIdx) it.scrollIntoView({ block: 'nearest' });
      });
    }

    // Global shortcut ⌘K or /
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        searchInput.focus();
      } else if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });

    // Close search dropdown on click outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.search-wrapper')) {
        searchDropdown.classList.remove('active');
      }
    });
  }

  function highlightMatch(text, query) {
    if (!query) return escapeHtml(text);
    const escaped = escapeRegex(query);
    const regex = new RegExp(`(${escaped})`, 'gi');
    return escapeHtml(text).replace(regex, '<span style="color: var(--color-gold); font-weight:700;">$1</span>');
  }

  function escapeHtml(str) {
    return String(str).replace(/[&<>"']/g, m => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[m]));
  }

  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }


  // =========================================================
  // 5. Journey Progress & Namaste Avatar with Voiceovers
  // =========================================================
  function initJourneyAndAvatar() {
    const uj = data.userJourney;
    if (!uj) return;

    if (journeyProgressFill) {
      journeyProgressFill.style.width = `${uj.progressPercent}%`;
    }
    if (journeyCountText) {
      journeyCountText.textContent = `${uj.exploredCount} / ${uj.totalRegions}`;
    }
    if (journeyPercentText) {
      journeyPercentText.textContent = `${uj.progressPercent}% Discovered`;
    }

    // Sacred Temple Bell Chime (Web Audio API)
    function playTempleBell() {
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = audioCtx || new AudioContext();
        if (ctx.state === 'suspended') ctx.resume();

        // Harmonious bell frequencies (Sa note ~ 554.37 Hz with harmonics)
        const bellPitches = [554.37, 830.61, 1108.73];
        bellPitches.forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, ctx.currentTime);

          const duration = 1.4 - idx * 0.25;
          gain.gain.setValueAtTime(0.06 / (idx + 1), ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);

          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(ctx.currentTime);
          osc.stop(ctx.currentTime + duration + 0.1);
        });
      } catch (err) {
        // Fallback silently if audio context is blocked
      }
    }

    // Voiceover Synthesis Engine
    function speakGreeting(greeting) {
      playTempleBell();

      if (!('speechSynthesis' in window)) {
        return;
      }

      window.speechSynthesis.cancel();

      const textToSpeak = greeting.speechText || greeting.text;
      const utterance = new SpeechSynthesisUtterance(textToSpeak);
      utterance.lang = greeting.langCode || 'hi-IN';
      utterance.rate = 0.92;
      utterance.pitch = 1.05;

      // Find best matched regional voice
      const voices = window.speechSynthesis.getVoices();
      if (voices && voices.length > 0) {
        const matchedVoice = voices.find(v => v.lang === greeting.langCode)
          || voices.find(v => v.lang.startsWith('hi'))
          || voices.find(v => v.lang.includes('IN'))
          || voices.find(v => v.name.toLowerCase().includes('india'));
        if (matchedVoice) {
          utterance.voice = matchedVoice;
        }
      }

      // UI state indicators
      if (avatarSpeechBubble) avatarSpeechBubble.classList.add('speaking');
      if (playVoiceoverBtn) playVoiceoverBtn.classList.add('speaking');
      if (voiceStatusText) voiceStatusText.textContent = 'Speaking...';

      utterance.onend = () => {
        if (avatarSpeechBubble) avatarSpeechBubble.classList.remove('speaking');
        if (playVoiceoverBtn) playVoiceoverBtn.classList.remove('speaking');
        if (voiceStatusText) voiceStatusText.textContent = 'Listen';
      };

      utterance.onerror = () => {
        if (avatarSpeechBubble) avatarSpeechBubble.classList.remove('speaking');
        if (playVoiceoverBtn) playVoiceoverBtn.classList.remove('speaking');
        if (voiceStatusText) voiceStatusText.textContent = 'Listen';
      };

      window.speechSynthesis.speak(utterance);
    }

    // Cycle Avatar Greetings
    let greetingIdx = 0;
    function showGreeting(idx, shouldSpeak = false) {
      const g = uj.avatarGreetings[idx % uj.avatarGreetings.length];
      if (!g) return;

      if (avatarGreetingNative) {
        avatarGreetingNative.style.opacity = 0;
        setTimeout(() => {
          avatarGreetingNative.textContent = g.text;
          avatarGreetingNative.style.opacity = 1;
        }, 120);
      }
      if (avatarGreetingRoman) {
        avatarGreetingRoman.style.opacity = 0;
        setTimeout(() => {
          avatarGreetingRoman.textContent = g.roman;
          avatarGreetingRoman.style.opacity = 1;
        }, 120);
      }

      if (shouldSpeak) {
        speakGreeting(g);
      }
    }

    // 1. Click on Listen Button
    if (playVoiceoverBtn) {
      playVoiceoverBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const currentGreeting = uj.avatarGreetings[greetingIdx % uj.avatarGreetings.length];
        speakGreeting(currentGreeting);
      });
    }

    // 2. Click on Switch Button
    if (cycleGreetingBtn) {
      cycleGreetingBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        greetingIdx++;
        showGreeting(greetingIdx, true);
      });
    }

    // 3. Tap anywhere on Avatar Frame to switch and hear voiceover
    if (avatarFrame) {
      avatarFrame.addEventListener('click', () => {
        greetingIdx++;
        showGreeting(greetingIdx, true);
      });

      avatarFrame.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          greetingIdx++;
          showGreeting(greetingIdx, true);
        }
      });
    }

    // Preload available synthesis voices
    if ('speechSynthesis' in window) {
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
    }
  }


  // =========================================================
  // 6. Did You Know? Fact Cycler
  // =========================================================
  function initDidYouKnow() {
    const facts = data.facts;
    if (!facts || !facts.length) return;

    let factIdx = 0;
    function renderFact(idx) {
      const f = facts[idx % facts.length];
      if (!f) return;

      if (dykTag) dykTag.textContent = f.tag;
      if (dykRegion) dykRegion.textContent = f.region;
      if (dykQuote) dykQuote.textContent = `"${f.quote}"`;
      if (dykDesc) dykDesc.textContent = f.description;
      if (dykStoryLink) {
        dykStoryLink.href = f.exploreLink || '#';
      }
    }

    renderFact(factIdx);

    if (dykNextBtn) {
      dykNextBtn.addEventListener('click', () => {
        factIdx++;
        renderFact(factIdx);
      });
    }
  }


  // =========================================================
  // 7. Profile Dropdown Toggle
  // =========================================================
  if (profileToggleBtn && profileDropdown) {
    profileToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      profileDropdown.classList.toggle('active');
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.profile-menu-container')) {
        profileDropdown.classList.remove('active');
      }
    });
  }


  // =========================================================
  // 8. Shared Web Audio Tanpura Ambience
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

    // Traditional C# Tanpura tuning (138.59, 207.65, 277.18, 554.37 Hz)
    const pitches = [138.59, 207.65, 277.18, 554.37];
    pitches.forEach((freq, idx) => {
      const osc = audioCtx.createOscillator();
      const noteGain = audioCtx.createGain();
      const filter = audioCtx.createBiquadFilter();

      osc.type = idx % 2 === 0 ? 'sawtooth' : 'triangle';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(450 + idx * 80, audioCtx.currentTime);
      filter.Q.setValueAtTime(1.8, audioCtx.currentTime);

      noteGain.gain.setValueAtTime(0.07 / (idx + 1), audioCtx.currentTime);

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
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.25, audioCtx.currentTime + 2.5);
      isAudioPlaying = true;
      if (homeAudioToggle) homeAudioToggle.classList.add('playing');
      if (homeAudioStatus) homeAudioStatus.textContent = 'Live';
    } else {
      masterGain.gain.cancelScheduledValues(audioCtx.currentTime);
      masterGain.gain.linearRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);
      isAudioPlaying = false;
      if (homeAudioToggle) homeAudioToggle.classList.remove('playing');
      if (homeAudioStatus) homeAudioStatus.textContent = 'Off';
    }
  }

  if (homeAudioToggle) {
    homeAudioToggle.addEventListener('click', toggleAudio);
  }


  // =========================================================
  // 9. Initialize Everything
  // =========================================================
  renderRegionBeacons();
  initSearchEngine();
  initJourneyAndAvatar();
  initDidYouKnow();

  // Focus on map beacon if URL has hash (e.g. #rajasthan)
  const hash = window.location.hash.replace('#', '');
  if (hash) {
    const reg = data.regions.find(r => r.id === hash);
    const beacon = document.getElementById(`beacon-${hash}`);
    if (reg && beacon) {
      setTimeout(() => showRegionPopover(reg, beacon), 400);
    }
  }

});
