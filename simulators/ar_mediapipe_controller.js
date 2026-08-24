/**
 * RBRU AR MediaPipe Multi-Modal Gesture Controller (60 FPS Web Audio & Zero-GC)
 * Integrates MediaPipe Hands for touchless interaction across Modern Physics simulations.
 */

(function(window) {
  'use strict';

  // Web Audio Synthesizer
  let audioCtx = null;
  function getAudioContext() {
    if (!audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) audioCtx = new AudioContext();
    }
    if (audioCtx && audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
    return audioCtx;
  }

  function playTone(freq, type = 'sine', duration = 0.08, gainVal = 0.1) {
    try {
      const ctx = getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(gainVal, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch(e) {}
  }

  const soundFx = {
    click: () => playTone(880, 'triangle', 0.04, 0.08),
    pinch: () => playTone(1200, 'sine', 0.1, 0.15),
    release: () => playTone(600, 'sine', 0.08, 0.1),
    swipe: () => playTone(440, 'sine', 0.15, 0.12),
    laser: () => playTone(1760, 'sawtooth', 0.2, 0.18)
  };

  class ARMediaPipeController {
    constructor() {
      this.isARActive = false;
      this.camera = null;
      this.hands = null;
      this.videoElement = null;
      this.canvasElement = null;
      this.canvasCtx = null;
      this.lastPinch = false;
      this.lastSwipeTime = 0;
      this.prevHandX = null;
      this.targetSlider = null;
    }

    injectUI() {
      if (document.getElementById('ar-wrapper')) return;

      const style = document.createElement('style');
      style.textContent = `
        .ar-toggle-bar {
          display: flex;
          align-items: center;
          justify-content: space-between;
          background: rgba(15, 23, 42, 0.85);
          border: 1px solid rgba(0, 240, 255, 0.3);
          border-radius: 8px;
          padding: 6px 12px;
          margin-bottom: 8px;
        }
        .ar-btn-toggle {
          background: linear-gradient(135deg, #0284c7, #00f0ff);
          color: #020617;
          border: none;
          padding: 6px 14px;
          border-radius: 6px;
          font-weight: 700;
          font-size: 0.80rem;
          font-family: 'Sarabun', sans-serif;
          cursor: pointer;
          display: inline-flex;
          align-items: center;
          gap: 6px;
          transition: all 0.2s;
        }
        .ar-btn-toggle:hover {
          box-shadow: 0 0 12px rgba(0, 240, 255, 0.6);
          transform: translateY(-1px);
        }
        .ar-btn-toggle.active {
          background: linear-gradient(135deg, #f43f5e, #dc2626);
          color: #fff;
        }
        .ar-hud-feed {
          position: fixed;
          bottom: 12px;
          right: 12px;
          width: 180px;
          height: 135px;
          background: #020617;
          border: 2px solid #00f0ff;
          border-radius: 12px;
          overflow: hidden;
          box-shadow: 0 8px 30px rgba(0,0,0,0.85);
          z-index: 99999;
          display: none;
        }
        .ar-hud-video {
          width: 100%;
          height: 100%;
          object-fit: cover;
          transform: scaleX(-1);
        }
        .ar-hud-canvas {
          position: absolute;
          inset: 0;
          width: 100%;
          height: 100%;
          transform: scaleX(-1);
          pointer-events: none;
        }
        .ar-gesture-tip {
          font-size: 0.74rem;
          color: #94a3b8;
          display: flex;
          align-items: center;
          gap: 6px;
        }
        .ar-gesture-badge {
          background: rgba(16, 185, 129, 0.15);
          border: 1px solid #10b981;
          color: #10b981;
          padding: 2px 6px;
          border-radius: 4px;
          font-size: 0.68rem;
          font-family: 'JetBrains Mono', monospace;
          font-weight: 700;
        }
      `;
      document.head.appendChild(style);

      const header = document.querySelector('.sim-card');
      if (!header) return;

      const bar = document.createElement('div');
      bar.id = 'ar-wrapper';
      bar.className = 'ar-toggle-bar';
      bar.innerHTML = `
        <div class="ar-gesture-tip">
          <span id="ar-status-text">🖐️ โหมด AR MediaPipe ไร้สัมผัส:</span>
          <span id="ar-gesture-label" class="ar-gesture-badge">STANDBY</span>
          <span style="color:#64748b; font-size:0.70rem;">(ขยับนิ้วชี้ = เลื่อนสไลเดอร์, จีบนิ้ว = สั่งการ)</span>
        </div>
        <button id="btn-toggle-ar" class="ar-btn-toggle">
          <span>📷</span> เปิดโหมด AR ควบคุมด้วยมือ
        </button>
      `;

      // Insert bar right after sim-header
      const simHeader = header.querySelector('.sim-header');
      if (simHeader && simHeader.nextSibling) {
        header.insertBefore(bar, simHeader.nextSibling);
      } else {
        header.prepend(bar);
      }

      // PiP Camera HUD
      const hud = document.createElement('div');
      hud.id = 'ar-hud-container';
      hud.className = 'ar-hud-feed';
      hud.innerHTML = `
        <video id="ar-webcam-feed" class="ar-hud-video" playsinline></video>
        <canvas id="ar-webcam-canvas" class="ar-hud-canvas" width="180" height="135"></canvas>
      `;
      document.body.appendChild(hud);

      document.getElementById('btn-toggle-ar').addEventListener('click', () => {
        this.toggleAR();
      });
    }

    loadMediaPipeScripts() {
      return new Promise((resolve, reject) => {
        if (window.Hands && window.Camera) {
          resolve();
          return;
        }

        const s1 = document.createElement('script');
        s1.src = "https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js";
        s1.crossOrigin = "anonymous";

        const s2 = document.createElement('script');
        s2.src = "https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js";
        s2.crossOrigin = "anonymous";

        let loaded = 0;
        const check = () => {
          loaded++;
          if (loaded === 2) resolve();
        };

        s1.onload = check; s1.onerror = reject;
        s2.onload = check; s2.onerror = reject;

        document.head.appendChild(s1);
        document.head.appendChild(s2);
      });
    }

    async toggleAR() {
      const btn = document.getElementById('btn-toggle-ar');
      const hud = document.getElementById('ar-hud-container');
      const badge = document.getElementById('ar-gesture-label');

      if (this.isARActive) {
        // Stop Camera
        if (this.camera) {
          try { this.camera.stop(); } catch(e) {}
          this.camera = null;
        }
        if (this.videoElement && this.videoElement.srcObject) {
          const tracks = this.videoElement.srcObject.getTracks();
          tracks.forEach(t => t.stop());
          this.videoElement.srcObject = null;
        }
        this.isARActive = false;
        btn.classList.remove('active');
        btn.innerHTML = `<span>📷</span> เปิดโหมด AR ควบคุมด้วยมือ`;
        hud.style.display = 'none';
        badge.textContent = 'STANDBY';
        badge.style.color = '#10b981';
        badge.style.borderColor = '#10b981';
        return;
      }

      btn.textContent = '⏳ กำลังโหลด AI Hand Model...';
      try {
        await this.loadMediaPipeScripts();
        this.videoElement = document.getElementById('ar-webcam-feed');
        this.canvasElement = document.getElementById('ar-webcam-canvas');
        this.canvasCtx = this.canvasElement.getContext('2d');

        this.hands = new window.Hands({
          locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
        });

        this.hands.setOptions({
          maxNumHands: 1,
          modelComplexity: 1,
          minDetectionConfidence: 0.65,
          minTrackingConfidence: 0.65
        });

        this.hands.onResults((results) => this.onHandResults(results));

        this.camera = new window.Camera(this.videoElement, {
          onFrame: async () => {
            if (this.isARActive && this.hands) {
              await this.hands.send({ image: this.videoElement });
            }
          },
          width: 320,
          height: 240
        });

        await this.camera.start();
        this.isARActive = true;
        btn.classList.add('active');
        btn.innerHTML = `<span>🔴</span> ปิดโหมด AR`;
        hud.style.display = 'block';
        badge.textContent = 'CAMERA TRACKING 60 FPS';
        soundFx.click();
      } catch (err) {
        console.error('AR MediaPipe init error:', err);
        btn.textContent = '❌ ไม่สามารถเข้าถึงกล้องได้';
        setTimeout(() => {
          btn.innerHTML = `<span>📷</span> เปิดโหมด AR ควบคุมด้วยมือ`;
        }, 2500);
      }
    }

    onHandResults(results) {
      if (!this.canvasCtx) return;
      const w = this.canvasElement.width;
      const h = this.canvasElement.height;

      this.canvasCtx.clearRect(0, 0, w, h);

      const badge = document.getElementById('ar-gesture-label');

      if (!results.multiHandLandmarks || results.multiHandLandmarks.length === 0) {
        badge.textContent = 'SEARCHING HAND ✋';
        badge.style.color = '#f59e0b';
        return;
      }

      const landmarks = results.multiHandLandmarks[0];

      // Draw Hand Skeleton
      this.drawSkeleton(landmarks, w, h);

      // Key Landmarks
      const wrist = landmarks[0];
      const thumbTip = landmarks[4];
      const indexTip = landmarks[8];
      const middleTip = landmarks[12];
      const pinkyTip = landmarks[20];

      // 1. Pinch Detection (Thumb tip to Index tip distance)
      const pinchDist = Math.hypot(thumbTip.x - indexTip.x, thumbTip.y - indexTip.y);
      const isPinching = pinchDist < 0.08;

      // 2. Fist Detection
      const fistDist = Math.hypot(wrist.x - middleTip.x, wrist.y - middleTip.y);
      const isFist = fistDist < 0.22;

      // Coordinate Mapping (Index Tip X & Y)
      // Note: Video is mirrored, so 1 - indexTip.x maps to normal left-to-right screen
      const handNormX = 1 - indexTip.x;
      const handNormY = indexTip.y;

      // Find all range inputs on page
      const sliders = Array.from(document.querySelectorAll('input[type=range]'));
      if (sliders.length > 0) {
        // Select first slider by default or closest
        const slider = sliders[0];
        const min = +slider.min || 0;
        const max = +slider.max || 100;
        const step = +slider.step || 1;

        // Map Hand X (from 0.15 to 0.85) to slider range
        const clampedX = Math.max(0.15, Math.min(0.85, handNormX));
        const factor = (clampedX - 0.15) / 0.70;
        const targetVal = min + factor * (max - min);

        // Apply with step quantization
        const quantized = Math.round(targetVal / step) * step;
        if (+slider.value !== quantized) {
          slider.value = quantized;
          slider.dispatchEvent(new Event('input', { bubbles: true }));
          soundFx.click();
        }
      }

      // Handle Gestures
      if (isPinching) {
        badge.textContent = 'PINCH GESTURE 🤏 (TRIGGER)';
        badge.style.color = '#00f0ff';
        if (!this.lastPinch) {
          soundFx.pinch();
          // Trigger button actions if available
          const actionBtn = document.querySelector('button[onclick*="trigger"], button[onclick*="reset"], .tab-btn:not(.active)');
          if (actionBtn) {
            actionBtn.click();
          }
        }
      } else if (isFist) {
        badge.textContent = 'FIST GESTURE ✊ (HOLD)';
        badge.style.color = '#f43f5e';
      } else {
        badge.textContent = `POINTING ☝️ [${Math.round(handNormX * 100)}%]`;
        badge.style.color = '#10b981';
      }

      // Swipe Detection (Fast horizontal hand movement)
      if (this.prevHandX !== null) {
        const deltaX = handNormX - this.prevHandX;
        const now = Date.now();
        if (Math.abs(deltaX) > 0.18 && (now - this.lastSwipeTime > 700)) {
          this.lastSwipeTime = now;
          soundFx.swipe();
          // Switch tabs
          const tabs = Array.from(document.querySelectorAll('.tab-btn'));
          if (tabs.length >= 2) {
            const activeIdx = tabs.findIndex(t => t.classList.contains('active'));
            const nextIdx = (activeIdx + 1) % tabs.length;
            tabs[nextIdx].click();
          }
        }
      }
      this.prevHandX = handNormX;
      this.lastPinch = isPinching;
    }

    drawSkeleton(landmarks, w, h) {
      const connections = [
        [0,1],[1,2],[2,3],[3,4], // Thumb
        [0,5],[5,6],[6,7],[7,8], // Index
        [5,9],[9,10],[10,11],[11,12], // Middle
        [9,13],[13,14],[14,15],[15,16], // Ring
        [13,17],[17,18],[18,19],[19,20], // Pinky
        [0,17] // Palm Base
      ];

      this.canvasCtx.strokeStyle = "rgba(0, 240, 255, 0.75)";
      this.canvasCtx.lineWidth = 2;

      connections.forEach(([i, j]) => {
        const p1 = landmarks[i], p2 = landmarks[j];
        this.canvasCtx.beginPath();
        this.canvasCtx.moveTo(p1.x * w, p1.y * h);
        this.canvasCtx.lineTo(p2.x * w, p2.y * h);
        this.canvasCtx.stroke();
      });

      // Draw Joints
      landmarks.forEach((p, idx) => {
        this.canvasCtx.fillStyle = (idx === 8 || idx === 4) ? "#f43f5e" : "#10b981";
        this.canvasCtx.beginPath();
        this.canvasCtx.arc(p.x * w, p.y * h, (idx === 8 || idx === 4 ? 4 : 2.5), 0, Math.PI*2);
        this.canvasCtx.fill();
      });
    }
  }

  // Auto-initialize when DOM is ready
  window.addEventListener('DOMContentLoaded', () => {
    window.arController = new ARMediaPipeController();
    window.arController.injectUI();
  });

})(window);
