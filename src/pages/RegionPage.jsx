import { useEffect, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import maharashtraHtml from '../../maharashtra.html?raw';
import odishaHtml from '../../odisha.html?raw';
import '../region.css';

function extractBody(html) {
  return new DOMParser().parseFromString(html, 'text/html').body.innerHTML
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/(src|href)="assets\//g, '$1="/assets/');
}

export default function RegionPage() {
  const { regionId } = useParams();
  const source = regionId === 'odisha' ? odishaHtml : maharashtraHtml;
  const controller = regionId === 'odisha' ? '/odisha.js' : '/maharashtra.js';
  const body = useMemo(() => extractBody(source), [source]);

  // Always reset scroll to the top when navigating to or switching regional pages.
  // On desktop the scroll container is .main-content (not window), so reset both.
  useEffect(() => {
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    // Also reset the per-column scroll container used on desktop
    const mainContent = document.querySelector('.main-content');
    if (mainContent) mainContent.scrollTop = 0;
  }, [regionId]);

  useEffect(() => {
    document.body.classList.add('regional-route');
    const script = document.createElement('script');
    script.src = controller;
    script.async = false;
    document.body.appendChild(script);

    // Setup mobile controls for regional sidebar and cultural assistant
    const setupMobileControls = () => {
      // Remove any previously created controls
      document.querySelector('.mobile-regional-bar')?.remove();
      document.querySelector('.mobile-regional-backdrop')?.remove();

      const sidebar = document.querySelector('.cultural-sidebar');
      const rightPanel = document.querySelector('.right-panel');

      if (!sidebar && !rightPanel) return;

      // Create mobile bottom action bar
      const bar = document.createElement('div');
      bar.className = 'mobile-regional-bar';
      bar.innerHTML = `
        <button type="button" class="mobile-bar-btn mobile-bar-btn-sidebar" id="mobileSidebarToggleBtn" aria-label="Toggle Regional Navigation">
          <i class="fas fa-compass"></i>
          <span>Topics</span>
        </button>
        <button type="button" class="mobile-bar-btn mobile-bar-btn-chat" id="mobileChatToggleBtn" aria-label="Toggle Cultural Assistant">
          <i class="fas fa-comment-dots"></i>
          <span>AI Guide</span>
        </button>
      `;

      // Backdrop overlay
      const backdrop = document.createElement('div');
      backdrop.className = 'mobile-regional-backdrop';

      document.body.appendChild(bar);
      document.body.appendChild(backdrop);

      const closeAll = () => {
        sidebar?.classList.remove('open');
        rightPanel?.classList.remove('open');
        backdrop.classList.remove('active');
        document.body.classList.remove('regional-drawer-open');
      };

      backdrop.addEventListener('click', closeAll);

      const sidebarBtn = bar.querySelector('#mobileSidebarToggleBtn');
      const chatBtn = bar.querySelector('#mobileChatToggleBtn');

      sidebarBtn?.addEventListener('click', () => {
        const isOpen = sidebar?.classList.contains('open');
        rightPanel?.classList.remove('open');
        if (isOpen) {
          sidebar?.classList.remove('open');
          backdrop.classList.remove('active');
          document.body.classList.remove('regional-drawer-open');
        } else {
          sidebar?.classList.add('open');
          backdrop.classList.add('active');
          document.body.classList.add('regional-drawer-open');
        }
      });

      chatBtn?.addEventListener('click', () => {
        const isOpen = rightPanel?.classList.contains('open');
        sidebar?.classList.remove('open');
        if (isOpen) {
          rightPanel?.classList.remove('open');
          backdrop.classList.remove('active');
          document.body.classList.remove('regional-drawer-open');
        } else {
          rightPanel?.classList.add('open');
          backdrop.classList.add('active');
          document.body.classList.add('regional-drawer-open');
        }
      });

      // Close drawers on sidebar topic link navigation
      sidebar?.querySelectorAll('.cultural-navigation a')?.forEach(link => {
        link.addEventListener('click', () => {
          if (window.innerWidth <= 1150) {
            closeAll();
          }
        });
      });
    };

    // Small delay to ensure injected HTML DOM is rendered before querying elements
    const timer = setTimeout(setupMobileControls, 50);

    return () => {
      clearTimeout(timer);
      script.remove();
      document.body.classList.remove('regional-route');
      document.body.classList.remove('regional-drawer-open');
      document.querySelector('.mobile-menu-toggle')?.remove();
      document.querySelector('.mobile-regional-bar')?.remove();
      document.querySelector('.mobile-regional-backdrop')?.remove();
    };
  }, [controller]);

  return <div className="regional-page" dangerouslySetInnerHTML={{ __html: body }} />;
}