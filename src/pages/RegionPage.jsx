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

  useEffect(() => {
    document.body.classList.add('regional-route');
    const script = document.createElement('script');
    script.src = controller;
    script.async = false;
    document.body.appendChild(script);
    return () => {
      script.remove();
      document.body.classList.remove('regional-route');
      document.querySelector('.mobile-menu-toggle')?.remove();
    };
  }, [controller]);

  return <div className="regional-page" dangerouslySetInnerHTML={{ __html: body }} />;
}