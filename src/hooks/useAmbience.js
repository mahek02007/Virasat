import { useState, useRef, useEffect } from 'react';

export function useAmbience() {
  const [playing, setPlaying] = useState(false);
  const context = useRef(null);
  const gain = useRef(null);

  const toggle = () => {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;

    if (!context.current) {
      context.current = new AudioContext();
      gain.current = context.current.createGain();
      gain.current.gain.value = 0.04;
      gain.current.connect(context.current.destination);

      [138.59, 207.65, 277.18, 554.37].forEach((frequency) => {
        const oscillator = context.current.createOscillator();
        oscillator.type = 'triangle';
        oscillator.frequency.value = frequency;
        oscillator.connect(gain.current);
        oscillator.start();
      });
    }

    if (context.current.state === 'suspended') {
      context.current.resume();
    }

    if (playing) {
      if (gain.current.gain.setValueAtTime) {
        gain.current.gain.setValueAtTime(0.0001, context.current.currentTime);
      } else {
        gain.current.gain.value = 0.0001;
      }
      setPlaying(false);
    } else {
      if (gain.current.gain.setValueAtTime) {
        gain.current.gain.setValueAtTime(0.04, context.current.currentTime);
      } else {
        gain.current.gain.value = 0.04;
      }
      setPlaying(true);
    }
  };

  useEffect(() => {
    return () => {
      if (context.current && context.current.state !== 'closed') {
        try {
          context.current.close();
        } catch (_) {}
        context.current = null;
      }
    };
  }, []);

  return [playing, toggle];
}

export default useAmbience;
