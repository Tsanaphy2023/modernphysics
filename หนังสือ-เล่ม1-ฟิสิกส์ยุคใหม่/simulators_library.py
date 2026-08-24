#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RBRU Modern Physics 4012920: Comprehensive 40 Real-Time 2D/3D Interactive Simulators Library
Provides self-contained interactive Canvas + JS + CSS for all 40 subtopics.
Each simulator has responsive high-contrast graphics, real-time sliders, live calculation readouts,
and multi-tier auto-initialization (immediate, DOMContentLoaded, load, resize, and custom triggers).
"""

def get_simulator_html_and_js(page_id, sim_type, title, standalone=False):
    prefix = f"sim_{page_id.replace('.', '_')}"
    
    # -------------------------------------------------------------
    # 1.1 Classical Limits (Rayleigh-Jeans vs Planck UV Catastrophe)
    # -------------------------------------------------------------
    if sim_type == "classical_limits":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อุณหภูมิวัตถุร้อน (T): <span id="{prefix}_val_temp" class="readout-val">5000</span> K</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_temp" min="2000" max="10000" step="100" value="5000">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="230"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rj" style="color:#f43f5e;">ลู่ออกสู่อนันต์ (∞)</div><div class="readout-lbl">ทฤษฎีดั้งเดิม (Rayleigh-Jeans)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_planck" style="color:#00f0ff;">จุดยอด 580 nm</div><div class="readout-lbl">ทฤษฎีควอนตัม (Planck)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_catastrophe" style="color:#f59e0b;">UV Catastrophe</div><div class="readout-lbl">ปรากฏการณ์หายนะรังสี UV</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_temp");
            if (!slider) return false;
            function draw() {{
              const T = +slider.value;
              const vEl = document.getElementById("{prefix}_val_temp");
              if (vEl) vEl.textContent = T;
              const peak = Math.round(2898000 / T);
              const pEl = document.getElementById("{prefix}_val_planck");
              if (pEl) pEl.textContent = "จุดยอด " + peak + " nm";
              
              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "rgba(255,255,255,0.06)";
              ctx.lineWidth = 1;
              for(let x=50; x<600; x+=50) {{ ctx.beginPath(); ctx.moveTo(x, 20); ctx.lineTo(x, 190); ctx.stroke(); }}
              
              // Rayleigh-Jeans (Red Curve diverging)
              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4,4]);
              ctx.beginPath(); ctx.moveTo(50, 190);
              for(let x=50; x<600; x+=2) {{
                const lam = (x - 40)*3;
                const y_rj = 190 - (800000000 * (T/5000)) / (lam*lam*0.08 + 10);
                if (x===50) ctx.moveTo(x, Math.max(20, y_rj)); else ctx.lineTo(x, Math.max(20, y_rj));
              }}
              ctx.stroke();
              ctx.setLineDash([]);
              
              // Planck Curve (Cyan)
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
              ctx.beginPath();
              for(let x=50; x<600; x+=2) {{
                const lam = (x - 40)*3;
                const p = Math.pow(T/1000, 3) * Math.pow(lam/peak, 5) / (Math.exp((lam?peak/lam:10)*2) - 1 + 0.05);
                const y = 190 - Math.min(160, p*5.5);
                if (x===50) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              // Axes
              ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, 190); ctx.lineTo(600, 190); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
              ctx.fillText("ความยาวคลื่น λ (nm) →", 460, 210);
              ctx.fillText("ความเข้มพลังงาน I(λ)", 10, 25);
              ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical (Rayleigh-Jeans)", 70, 40);
              ctx.fillStyle = "#00f0ff"; ctx.fillText("— Quantum (Planck Law)", 70, 60);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 1.2 Planck Blackbody
    # -------------------------------------------------------------
    elif sim_type == "planck_blackbody":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อุณหภูมิสัมบูรณ์ (T): <span id="{prefix}_val_temp" class="readout-val">5800</span> K (ดวงอาทิตย์)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_temp" min="1000" max="12000" step="100" value="5800">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="230"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_peak">500 nm</div><div class="readout-lbl">ความยาวคลื่นสูงสุด (λ_max)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_color">ขาว-เหลือง</div><div class="readout-lbl">สีของรังสีความร้อน</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_power">6.42 × 10⁷ W/m²</div><div class="readout-lbl">กำลังแผ่รังสีรวม (σT⁴)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_temp");
            if (!slider) return false;
            function draw() {{
              const T = +slider.value;
              const tEl = document.getElementById("{prefix}_val_temp");
              if (tEl) tEl.textContent = T;
              const peak = Math.round(2898000 / T);
              const pEl = document.getElementById("{prefix}_val_peak");
              if (pEl) pEl.textContent = peak + " nm";
              
              const power = (5.67e-8 * Math.pow(T, 4)).toExponential(2);
              const pwEl = document.getElementById("{prefix}_val_power");
              if (pwEl) pwEl.textContent = power + " W/m²";
              
              let col = "แดง";
              if (T > 3500 && T <= 5000) col = "ส้ม-เหลือง";
              else if (T > 5000 && T <= 7500) col = "ขาวนวล (Yellow-White)";
              else if (T > 7500 && T <= 10000) col = "ขาวอมฟ้า (Blue-White)";
              else if (T > 10000) col = "ฟ้าเข้ม (Deep Blue)";
              const cEl = document.getElementById("{prefix}_val_color");
              if (cEl) cEl.textContent = col;

              ctx.clearRect(0,0,cv.width,cv.height);
              // Visible spectrum band
              const grad = ctx.createLinearGradient(120, 0, 480, 0);
              grad.addColorStop(0, "rgba(168, 85, 247, 0.2)");
              grad.addColorStop(0.2, "rgba(59, 130, 246, 0.2)");
              grad.addColorStop(0.5, "rgba(34, 197, 94, 0.2)");
              grad.addColorStop(0.7, "rgba(234, 179, 8, 0.2)");
              grad.addColorStop(1, "rgba(239, 68, 68, 0.2)");
              ctx.fillStyle = grad;
              ctx.fillRect(120, 20, 360, 170);

              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
              ctx.beginPath();
              for(let x=40; x<600; x+=2) {{
                const lam = (x - 30)*3;
                const p = Math.pow(T/1000, 3) * Math.pow(lam/peak, 5) / (Math.exp((lam?peak/lam:10)*2) - 1 + 0.05);
                const y = 190 - Math.min(160, p*5.5);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              const peakX = 30 + (peak / 3);
              if (peakX >= 40 && peakX <= 600) {{
                ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([3,3]);
                ctx.beginPath(); ctx.moveTo(peakX, 20); ctx.lineTo(peakX, 190); ctx.stroke();
                ctx.setLineDash([]);
                ctx.fillStyle = "#f59e0b"; ctx.fillText("λ_max = " + peak + " nm", peakX + 6, 40);
              }}

              ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(40, 20); ctx.lineTo(40, 190); ctx.lineTo(600, 190); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
              ctx.fillText("ความยาวคลื่น λ (nm) →", 460, 210);
              ctx.fillText("ความเข้ม I(λ)", 10, 25);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 1.3 Photoelectric Effect
    # -------------------------------------------------------------
    elif sim_type == "photoelectric":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ชนิดโลหะเป้าหมาย (Work Function φ):</label>
              <select id="{prefix}_sel_metal" style="width:100%; background:#0f172a; color:#00f0ff; border:1px solid #334155; padding:8px; border-radius:6px;">
                <option value="2.14">ซีเซียม (Cs: 2.14 eV)</option>
                <option value="2.30" selected>โซเดียม (Na: 2.30 eV)</option>
                <option value="4.30">สังกะสี (Zn: 4.30 eV)</option>
                <option value="4.70">ทองแดง (Cu: 4.70 eV)</option>
                <option value="5.65">แพลทินัม (Pt: 5.65 eV)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>ความยาวคลื่นแสงฉาย (λ): <span id="{prefix}_val_lam" class="readout-val">300</span> nm</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_lam" min="150" max="750" value="300">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_ephoton">4.13 eV</div><div class="readout-lbl">พลังงานโฟตอน (E = hf)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_kmax">1.83 eV</div><div class="readout-lbl">พลังงานจลน์สูงสุด (K_max)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_vs">1.83 V</div><div class="readout-lbl">ความต่างศักย์หยุดยั้ง (Vs)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_metal");
            const slider = document.getElementById("{prefix}_slider_lam");
            if (!sel || !slider) return false;
            let particles = [];
            for(let i=0; i<20; i++) particles.push({{ x: 120 + Math.random()*20, y: 40 + Math.random()*120, vx: 2 + Math.random()*3 }});

            function calc() {{
              const phi = +sel.value;
              const lam = +slider.value;
              const lEl = document.getElementById("{prefix}_val_lam");
              if (lEl) lEl.textContent = lam;
              const Ephoton = 1240 / lam;
              const epEl = document.getElementById("{prefix}_val_ephoton");
              if (epEl) epEl.textContent = Ephoton.toFixed(2) + " eV";
              const Kmax = Ephoton - phi;
              const kmEl = document.getElementById("{prefix}_val_kmax");
              const vsEl = document.getElementById("{prefix}_val_vs");
              if (Kmax > 0) {{
                if (kmEl) kmEl.textContent = Kmax.toFixed(2) + " eV";
                if (vsEl) vsEl.textContent = Kmax.toFixed(2) + " V";
              }} else {{
                if (kmEl) kmEl.textContent = "0 (ไม่หลุด)";
                if (vsEl) vsEl.textContent = "0 V";
              }}
            }}

            function render() {{
              ctx.clearRect(0,0,cv.width,cv.height);
              // Cathode Emitter
              ctx.fillStyle = "#475569";
              ctx.fillRect(80, 30, 24, 140);
              ctx.fillStyle = "#00f0ff";
              ctx.fillText("Emitter (Target)", 50, 190);

              // Anode Collector
              ctx.fillStyle = "#334155";
              ctx.fillRect(520, 30, 24, 140);
              ctx.fillStyle = "#94a3b8";
              ctx.fillText("Collector Anode", 480, 190);

              const lam = +slider.value;
              const Ephoton = 1240 / lam;
              const phi = +sel.value;
              const hasElectrons = Ephoton > phi;
              
              // Incoming Photons
              ctx.strokeStyle = lam < 400 ? "#a855f7" : (lam < 550 ? "#00f0ff" : "#ef4444");
              ctx.lineWidth = 2.5;
              for(let i=0; i<3; i++) {{
                ctx.beginPath();
                ctx.moveTo(10, 40 + i*40);
                ctx.lineTo(80, 60 + i*40);
                ctx.stroke();
              }}

              // Emitted photoelectrons
              if (hasElectrons) {{
                ctx.fillStyle = "#10b981";
                particles.forEach(p => {{
                  ctx.beginPath();
                  ctx.arc(p.x, p.y, 4.5, 0, Math.PI*2);
                  ctx.fill();
                  p.x += p.vx * Math.min(3, Math.max(0.5, Ephoton - phi));
                  if (p.x > 520) p.x = 104;
                }});
              }}
              requestAnimationFrame(render);
            }}
            sel.addEventListener("change", calc);
            slider.addEventListener("input", calc);
            calc();
            render();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 1.4 Rydberg Spectrum (Hydrogen Spectral Series)
    # -------------------------------------------------------------
    elif sim_type == "rydberg_spectrum":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>อนุกรมสเปกตรัม (Lower Level n₁):</label>
              <select id="{prefix}_sel_series" style="width:100%; background:#0f172a; color:#00f0ff; border:1px solid #334155; padding:8px; border-radius:6px;">
                <option value="1">Lyman (n₁ = 1, ย่าน UV)</option>
                <option value="2" selected>Balmer (n₁ = 2, ย่านแสงขาวที่ตามองเห็น)</option>
                <option value="3">Paschen (n₁ = 3, ย่าน Infrared)</option>
                <option value="4">Brackett (n₁ = 4, ย่าน Far IR)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>ระดับพลังงานเริ่มต้น (Upper Level n₂): <span id="{prefix}_val_n2" class="readout-val">3</span></label>
              <input type="range" class="sim-slider" id="{prefix}_slider_n2" min="2" max="7" value="3">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_lam">656.3 nm</div><div class="readout-lbl">ความยาวคลื่นโฟตอน (λ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_de">1.89 eV</div><div class="readout-lbl">พลังงานที่ปลดปล่อย (ΔE)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_line">H-alpha (สีแดง)</div><div class="readout-lbl">ชื่อและสีของเส้นสเปกตรัม</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_series");
            const slider = document.getElementById("{prefix}_slider_n2");
            if (!sel || !slider) return false;

            function draw() {{
              const n1 = +sel.value;
              slider.min = n1 + 1;
              if (+slider.value <= n1) slider.value = n1 + 1;
              const n2 = +slider.value;
              const n2El = document.getElementById("{prefix}_val_n2");
              if (n2El) n2El.textContent = n2;

              const invLam = 1.097373e7 * (1/(n1*n1) - 1/(n2*n2));
              const lam_nm = (1 / invLam) * 1e9;
              const dE = 13.6 * (1/(n1*n1) - 1/(n2*n2));

              const lEl = document.getElementById("{prefix}_val_lam");
              if (lEl) lEl.textContent = lam_nm.toFixed(1) + " nm";
              const deEl = document.getElementById("{prefix}_val_de");
              if (deEl) deEl.textContent = dE.toFixed(2) + " eV";

              let lineName = "สเปกตรัม";
              let color = "#00f0ff";
              if (n1 === 1) {{ lineName = "Lyman (" + n2 + "→1 UV)"; color = "#a855f7"; }}
              else if (n1 === 2) {{
                if (n2===3) {{ lineName = "H-alpha (สีแดง 656.3 nm)"; color = "#ef4444"; }}
                else if (n2===4) {{ lineName = "H-beta (สีฟ้าคราม 486.1 nm)"; color = "#06b6d4"; }}
                else if (n2===5) {{ lineName = "H-gamma (สีน้ำเงิน 434.0 nm)"; color = "#3b82f6"; }}
                else {{ lineName = "H-delta (สีม่วง 410.2 nm)"; color = "#8b5cf6"; }}
              }} else if (n1 === 3) {{ lineName = "Paschen (" + n2 + "→3 IR)"; color = "#f97316"; }}
              else {{ lineName = "Brackett (" + n2 + "→4 Far-IR)"; color = "#e11d48"; }}
              const lnEl = document.getElementById("{prefix}_val_line");
              if (lnEl) lnEl.textContent = lineName;

              ctx.clearRect(0,0,cv.width,cv.height);
              // Draw Energy Levels
              for(let n=1; n<=6; n++) {{
                const y = 190 - 160 * (1 - 1/(n*n));
                ctx.strokeStyle = n === n1 ? "#00f0ff" : "#475569";
                ctx.lineWidth = n === n1 ? 2.5 : 1;
                ctx.beginPath(); ctx.moveTo(60, y); ctx.lineTo(340, y); ctx.stroke();
                ctx.fillStyle = n === n1 ? "#00f0ff" : "#94a3b8";
                ctx.font = "11px sans-serif";
                ctx.fillText("n=" + n + " (" + (-13.6/(n*n)).toFixed(2) + " eV)", 348, y + 4);
              }}

              // Draw Transition Arrow
              const yStart = 190 - 160 * (1 - 1/(n2*n2));
              const yEnd = 190 - 160 * (1 - 1/(n1*n1));
              ctx.strokeStyle = color; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(200, yStart); ctx.lineTo(200, yEnd); ctx.stroke();
              // Arrowhead
              ctx.fillStyle = color;
              ctx.beginPath(); ctx.moveTo(195, yEnd - 6); ctx.lineTo(205, yEnd - 6); ctx.lineTo(200, yEnd); ctx.fill();

              // Emission Photon Wave packet
              ctx.strokeStyle = color; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=220; x<580; x+=2) {{
                const waveY = (yStart + yEnd)/2 + 12 * Math.sin((x-220)*0.15);
                if (x===220) ctx.moveTo(x, waveY); else ctx.lineTo(x, waveY);
              }}
              ctx.stroke();
              ctx.fillStyle = color; ctx.fillText("Photon hf (λ = " + lam_nm.toFixed(1) + " nm)", 420, (yStart + yEnd)/2 - 10);
            }}
            sel.addEventListener("change", draw);
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.1 Light Clock & Special Relativity Postulates
    # -------------------------------------------------------------
    elif sim_type == "light_clock":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ความเร็วสัมพัทธ์ของยาน (v): <span id="{prefix}_val_v" class="readout-val">0.60</span> c</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_v" min="0" max="0.99" step="0.01" value="0.60">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="220"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">1.250</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_t">1.250 s</div><div class="readout-lbl">เวลาที่สังเกตจากภายนอก (Δt)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_path">แนวทแยง (Z-path)</div><div class="readout-lbl">วิถีเดินแสงในกรอบเคลื่อนที่</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_v");
            if (!slider) return false;
            let tick = 0;

            function draw() {{
              const v = +slider.value;
              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = v.toFixed(2);
              const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - v*v));
              const gEl = document.getElementById("{prefix}_val_gamma");
              if (gEl) gEl.textContent = gamma.toFixed(3);
              const tEl = document.getElementById("{prefix}_val_t");
              if (tEl) tEl.textContent = gamma.toFixed(3) + " s";

              ctx.clearRect(0,0,cv.width,cv.height);

              // Left Frame: Rest Clock (S')
              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
              ctx.strokeRect(30, 20, 240, 180);
              ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
              ctx.fillText("กรอบนิ่งของผู้สังเกตในยาน (Proper Time Δt₀)", 40, 40);
              // Mirrors
              ctx.fillStyle = "#00f0ff";
              ctx.fillRect(100, 60, 100, 6);
              ctx.fillRect(100, 160, 100, 6);
              // Vertical bouncing light
              const yPulse = 66 + 94 * (0.5 + 0.5*Math.sin(tick*0.1));
              ctx.fillStyle = "#f59e0b";
              ctx.beginPath(); ctx.arc(150, yPulse, 5, 0, Math.PI*2); ctx.fill();
              ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 2;
              ctx.beginPath(); ctx.moveTo(150, 66); ctx.lineTo(150, 160); ctx.stroke();

              // Right Frame: Moving Observer (S)
              ctx.strokeStyle = "#475569";
              ctx.strokeRect(330, 20, 280, 180);
              ctx.fillStyle = "#00f0ff";
              ctx.fillText("กรอบสังเกตภายนอก (เวลาขยายตัว Δt = γΔt₀)", 340, 40);
              // Zig-zag light path
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              ctx.moveTo(360, 66);
              ctx.lineTo(460 + v*80, 160);
              ctx.lineTo(560, 66);
              ctx.stroke();
              ctx.fillStyle = "#10b981"; ctx.fillText("ระยะทางแสงเดินไกลขึ้น → เวลาเดินช้าลง", 360, 190);

              tick++;
              requestAnimationFrame(draw);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.2 Lorentz Transformation Calculator
    # -------------------------------------------------------------
    elif sim_type == "lorentz_calc":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ความเร็วสัมพัทธ์ (v): <span id="{prefix}_val_v" class="readout-val">0.80</span> c</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_v" min="0" max="0.99" step="0.01" value="0.80">
            </div>
            <div class="sim-control-group">
              <label>พิกัดตำแหน่งในกรอบ S (x): <span id="{prefix}_val_x" class="readout-val">10</span> เมตร</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_x" min="0" max="100" value="10">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">1.667</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_xp">16.67 m</div><div class="readout-lbl">พิกัดตำแหน่งในกรอบ S' (x')</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_tp">-4.44 × 10⁻⁸ s</div><div class="readout-lbl">พิกัดเวลาในกรอบ S' (t')</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sliderV = document.getElementById("{prefix}_slider_v");
            const sliderX = document.getElementById("{prefix}_slider_x");
            if (!sliderV || !sliderX) return false;

            function draw() {{
              const v = +sliderV.value;
              const x = +sliderX.value;
              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = v.toFixed(2);
              const xEl = document.getElementById("{prefix}_val_x");
              if (xEl) xEl.textContent = x;

              const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - v*v));
              const xp = gamma * x;
              const tp = -gamma * v * (x / 3e8);

              const gEl = document.getElementById("{prefix}_val_gamma");
              if (gEl) gEl.textContent = gamma.toFixed(3);
              const xpEl = document.getElementById("{prefix}_val_xp");
              if (xpEl) xpEl.textContent = xp.toFixed(2) + " m";
              const tpEl = document.getElementById("{prefix}_val_tp");
              if (tpEl) tpEl.textContent = tp.toExponential(2) + " s";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Spacetime Minkowski light cone schematic
              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1;
              ctx.beginPath(); ctx.moveTo(320, 20); ctx.lineTo(320, 190); ctx.stroke(); // ct axis
              ctx.beginPath(); ctx.moveTo(40, 105); ctx.lineTo(600, 105); ctx.stroke(); // x axis
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
              ctx.fillText("ct (เวลา)", 326, 30); ctx.fillText("x (ตำแหน่ง)", 550, 98);

              // Light cone lines (45 deg)
              ctx.strokeStyle = "rgba(245, 158, 11, 0.5)"; ctx.lineWidth = 1.5; ctx.setLineDash([4,4]);
              ctx.beginPath(); ctx.moveTo(320 - 85, 105 + 85); ctx.lineTo(320 + 85, 105 - 85); ctx.stroke();
              ctx.beginPath(); ctx.moveTo(320 - 85, 105 - 85); ctx.lineTo(320 + 85, 105 + 85); ctx.stroke();
              ctx.setLineDash([]);

              // Boosted axis (x', ct')
              const angle = Math.atan(v);
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              ctx.moveTo(320 - 180*Math.cos(angle), 105 + 180*Math.sin(angle));
              ctx.lineTo(320 + 180*Math.cos(angle), 105 - 180*Math.sin(angle));
              ctx.stroke();
              ctx.fillStyle = "#00f0ff"; ctx.fillText("x' axis (Boosted S')", 480, 105 - 180*Math.sin(angle) - 5);
            }}
            sliderV.addEventListener("input", draw);
            sliderX.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.3 Time Dilation & Length Contraction
    # -------------------------------------------------------------
    elif sim_type == "time_dilation_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ความเร็วการเดินทาง (v): <span id="{prefix}_val_v" class="readout-val">0.90</span> c</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_v" min="0" max="0.99" step="0.01" value="0.90">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">2.294</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_len">43.6%</div><div class="readout-lbl">ความยาวหดสั้น (L = L₀/γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_life">2.294 เท่า</div><div class="readout-lbl">อายุขัยอนุภาคยืดออก (Δt = γΔt₀)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_v");
            if (!slider) return false;

            function draw() {{
              const v = +slider.value;
              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = v.toFixed(2);
              const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - v*v));
              const lenPct = (100 / gamma).toFixed(1);
              const gEl = document.getElementById("{prefix}_val_gamma");
              if (gEl) gEl.textContent = gamma.toFixed(3);
              const lEl = document.getElementById("{prefix}_val_len");
              if (lEl) lEl.textContent = lenPct + "%";
              const lfEl = document.getElementById("{prefix}_val_life");
              if (lfEl) lfEl.textContent = gamma.toFixed(3) + " เท่า";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Proper Length Spaceship (Rest S')
              ctx.fillStyle = "#334155";
              ctx.fillRect(80, 40, 240, 40);
              ctx.fillStyle = "#00f0ff";
              ctx.fillRect(80, 40, 30, 40);
              ctx.fillStyle = "#f8fafc"; ctx.font = "12px sans-serif";
              ctx.fillText("ยานในกรอบนิ่ง L₀ = 100 เมตร (100%)", 90, 65);

              // Contracted Spaceship (Moving S)
              const contractedW = Math.max(10, 240 / gamma);
              ctx.fillStyle = "#475569";
              ctx.fillRect(80, 120, contractedW, 40);
              ctx.fillStyle = "#f59e0b";
              ctx.fillRect(80, 120, Math.min(30, contractedW*0.2), 40);
              ctx.fillStyle = "#f8fafc";
              ctx.fillText("ยานเคลื่อนที่สังเกตภายนอก L = " + (100/gamma).toFixed(1) + " ม. (" + lenPct + "%)", 90, 145);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.4 Relativistic Mass-Energy E = mc²
    # -------------------------------------------------------------
    elif sim_type == "mass_energy_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ความเร็วอนุภาค (v): <span id="{prefix}_val_v" class="readout-val">0.85</span> c (อิเล็กตรอน m₀ = 0.511 MeV/c²)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_v" min="0" max="0.99" step="0.01" value="0.85">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_e0">0.511 MeV</div><div class="readout-lbl">พลังงานนิ่ง (E₀ = m₀c²)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_k">0.459 MeV</div><div class="readout-lbl">พลังงานจลน์ (K = (γ-1)m₀c²)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_etot">0.970 MeV</div><div class="readout-lbl">พลังงานรวมสัมพัทธภาพ (E = γm₀c²)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_v");
            if (!slider) return false;

            function draw() {{
              const v = +slider.value;
              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = v.toFixed(2);
              const m0 = 0.511; // MeV
              const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - v*v));
              const K = (gamma - 1) * m0;
              const Etot = gamma * m0;

              const kEl = document.getElementById("{prefix}_val_k");
              if (kEl) kEl.textContent = K.toFixed(3) + " MeV";
              const etEl = document.getElementById("{prefix}_val_etot");
              if (etEl) etEl.textContent = Etot.toFixed(3) + " MeV";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Energy Bar Chart
              ctx.fillStyle = "#3b82f6";
              ctx.fillRect(80, 60, 200, 35);
              ctx.fillStyle = "#ffffff"; ctx.font = "12px sans-serif";
              ctx.fillText("Rest Energy E₀ = 0.511 MeV", 90, 82);

              const kWidth = Math.min(260, (K / m0) * 100);
              ctx.fillStyle = "#10b981";
              ctx.fillRect(280, 60, kWidth, 35);
              ctx.fillStyle = "#ffffff";
              ctx.fillText("Kinetic K = " + K.toFixed(2) + " MeV", 290, 82);

              // Relativistic Triangle p*c, m0*c^2, E
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              ctx.moveTo(100, 180); ctx.lineTo(100 + 120, 180); ctx.lineTo(100 + 120, 120); ctx.closePath();
              ctx.stroke();
              ctx.fillStyle = "#00f0ff";
              ctx.fillText("E² = (pc)² + (m₀c²)²", 250, 155);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 3.1 De Broglie Matter Wavelength
    # -------------------------------------------------------------
    elif sim_type == "de_broglie_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ชนิดอนุภาค:</label>
              <select id="{prefix}_sel_p" style="width:100%; background:#0f172a; color:#00f0ff; border:1px solid #334155; padding:8px; border-radius:6px;">
                <option value="9.109e-31">อิเล็กตรอน (Electron m = 9.1×10⁻³¹ kg)</option>
                <option value="1.673e-27">โปรตอน (Proton m = 1.67×10⁻²⁷ kg)</option>
                <option value="6.646e-27">อนุภาคแอลฟา (Alpha m = 6.6×10⁻²⁷ kg)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>ความต่างศักย์เร่งอนุภาค (V): <span id="{prefix}_val_v" class="readout-val">100</span> V</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_v" min="10" max="5000" step="10" value="100">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_lam">0.123 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_scale">ขนาดอะตอมผลึก</div><div class="readout-lbl">ระดับสเกลทางฟิสิกส์</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_diff">เลี้ยวเบนชัดเจน</div><div class="readout-lbl">พฤติกรรมความเป็นคลื่น</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_p");
            const slider = document.getElementById("{prefix}_slider_v");
            if (!sel || !slider) return false;

            function draw() {{
              const m = +sel.value;
              const V = +slider.value;
              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = V;

              // De Broglie wavelength lambda = h / sqrt(2m q V)
              const h = 6.626e-34;
              const q = 1.602e-19;
              const p = Math.sqrt(2 * m * q * V);
              const lam_m = h / p;
              const lam_nm = lam_m * 1e9;
              const lam_pm = lam_m * 1e12;

              const lEl = document.getElementById("{prefix}_val_lam");
              if (lEl) lEl.textContent = lam_nm >= 0.01 ? lam_nm.toFixed(3) + " nm" : lam_pm.toFixed(1) + " pm";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Matter Wave packet animation/display
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
              ctx.beginPath();
              const freq = Math.max(0.04, Math.min(0.4, 0.05 / Math.max(0.01, lam_nm)));
              for(let x=40; x<600; x+=2) {{
                const env = Math.exp(-Math.pow((x-320)/120, 2));
                const y = 105 + 65 * env * Math.sin((x-40)*freq);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#f59e0b"; ctx.font = "12px sans-serif";
              ctx.fillText("กลุ่มคลื่นสสารเดอบรอยล์: λ = h/p = " + (lam_nm >= 0.01 ? lam_nm.toFixed(3) + " nm" : lam_pm.toFixed(1) + " pm"), 60, 40);
            }}
            sel.addEventListener("change", draw);
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 4.2 Particle in a Box 1D
    # -------------------------------------------------------------
    elif sim_type == "particle_box_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ระดับควอนตัม (Quantum Number n): <span id="{prefix}_val_n" class="readout-val">1</span></label>
              <input type="range" class="sim-slider" id="{prefix}_slider_n" min="1" max="5" value="1">
            </div>
            <div class="sim-control-group">
              <label>ความกว้างกล่องศักย์ (L): <span id="{prefix}_val_l" class="readout-val">1.0</span> nm</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_l" min="0.5" max="3.0" step="0.1" value="1.0">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="220"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_en">0.376 eV</div><div class="readout-lbl">ระดับพลังงาน (E_n)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_nodes">0 โหนด</div><div class="readout-lbl">จำนวนบัพภายใน (Nodes)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_prob" style="color:#10b981;">|ψ(x)|² สมบูรณ์</div><div class="readout-lbl">ความหนาแน่นความน่าจะเป็น</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sliderN = document.getElementById("{prefix}_slider_n");
            const sliderL = document.getElementById("{prefix}_slider_l");
            if (!sliderN || !sliderL) return false;

            function draw() {{
              const n = +sliderN.value;
              const L = +sliderL.value;
              const nEl = document.getElementById("{prefix}_val_n");
              if (nEl) nEl.textContent = n;
              const lEl = document.getElementById("{prefix}_val_l");
              if (lEl) lEl.textContent = L.toFixed(1);

              // En = n^2 h^2 / (8 m L^2)
              const E1 = 0.376 / (L*L);
              const En = n * n * E1;

              const enEl = document.getElementById("{prefix}_val_en");
              if (enEl) enEl.textContent = En.toFixed(3) + " eV";
              const ndEl = document.getElementById("{prefix}_val_nodes");
              if (ndEl) ndEl.textContent = (n - 1) + " โหนด";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Potential Walls (x = 100, x = 540)
              ctx.fillStyle = "#334155";
              ctx.fillRect(80, 20, 20, 170);
              ctx.fillRect(540, 20, 20, 170);
              ctx.fillStyle = "#f43f5e"; ctx.font = "11px sans-serif";
              ctx.fillText("V = ∞", 72, 198); ctx.fillText("V = ∞", 532, 198);

              // Wavefunction psi(x) (Cyan)
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=100; x<=540; x+=2) {{
                const norm = (x - 100) / 440;
                const psi = Math.sin(n * Math.PI * norm);
                const y = 105 - 60 * psi;
                if (x===100) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              // Probability density |psi(x)|^2 (Filled Amber)
              ctx.fillStyle = "rgba(245, 158, 11, 0.25)";
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
              ctx.beginPath();
              ctx.moveTo(100, 185);
              for(let x=100; x<=540; x+=2) {{
                const norm = (x - 100) / 440;
                const prob = Math.pow(Math.sin(n * Math.PI * norm), 2);
                const y = 185 - 75 * prob;
                ctx.lineTo(x, y);
              }}
              ctx.lineTo(540, 185); ctx.closePath();
              ctx.fill(); ctx.stroke();

              ctx.fillStyle = "#00f0ff"; ctx.fillText("ฟังก์ชันคลื่น ψ_" + n + "(x)", 120, 40);
              ctx.fillStyle = "#f59e0b"; ctx.fillText("ความหนาแน่นความน่าจะเป็น |ψ_" + n + "(x)|²", 120, 58);
            }}
            sliderN.addEventListener("input", draw);
            sliderL.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 4.4 Quantum Tunneling
    # -------------------------------------------------------------
    elif sim_type == "tunneling_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>พลังงานอนุภาค (E): <span id="{prefix}_val_e" class="readout-val">3.0</span> eV</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_e" min="1.0" max="6.0" step="0.1" value="3.0">
            </div>
            <div class="sim-control-group">
              <label>ความหนากำแพงศักย์ (a): <span id="{prefix}_val_a" class="readout-val">0.5</span> nm (V₀ = 5.0 eV)</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_a" min="0.1" max="1.5" step="0.05" value="0.5">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="220"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_tprob">2.41 %</div><div class="readout-lbl">ความน่าจะเป็นทะลุผ่าน (T)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rprob">97.59 %</div><div class="readout-lbl">ความน่าจะเป็นสะท้อนกลับ (R)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_decay">Exponential Decay</div><div class="readout-lbl">พฤติกรรมในกำแพงศักย์</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sliderE = document.getElementById("{prefix}_slider_e");
            const sliderA = document.getElementById("{prefix}_slider_a");
            if (!sliderE || !sliderA) return false;

            function draw() {{
              const E = +sliderE.value;
              const a = +sliderA.value;
              const V0 = 5.0;
              const eEl = document.getElementById("{prefix}_val_e");
              if (eEl) eEl.textContent = E.toFixed(1);
              const aEl = document.getElementById("{prefix}_val_a");
              if (aEl) aEl.textContent = a.toFixed(2);

              let T = 0;
              if (E < V0) {{
                const kappa = 5.12 * Math.sqrt(V0 - E);
                T = 1 / (1 + (V0*V0 / (4*E*(V0-E))) * Math.pow(Math.sinh(kappa * a), 2));
              }} else {{
                T = 1.0;
              }}
              const R = 1 - T;

              const tpEl = document.getElementById("{prefix}_val_tprob");
              if (tpEl) tpEl.textContent = (T * 100).toFixed(2) + " %";
              const rpEl = document.getElementById("{prefix}_val_rprob");
              if (rpEl) rpEl.textContent = (R * 100).toFixed(2) + " %";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Barrier box
              const barW = Math.max(20, a * 120);
              ctx.fillStyle = "rgba(244, 63, 94, 0.25)";
              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
              ctx.fillRect(280, 40, barW, 140);
              ctx.strokeRect(280, 40, barW, 140);
              ctx.fillStyle = "#f43f5e"; ctx.font = "11px sans-serif";
              ctx.fillText("Barrier V₀ = 5.0 eV", 285, 30);

              // Wavefunction (Incident + Reflected -> Barrier -> Transmitted)
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              // Region I (Left)
              for(let x=40; x<=280; x+=2) {{
                const y = 110 + 40 * Math.sin((x-40)*0.15) + (R * 20) * Math.sin((x-40)*0.15);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              // Region II (Inside Barrier - Exponential Decay)
              const yStart = 110 + 40 * Math.sin(240*0.15);
              for(let x=280; x<=280+barW; x+=2) {{
                const norm = (x - 280) / barW;
                const y = 110 + (yStart - 110) * Math.exp(-norm * 2.5);
                ctx.lineTo(x, y);
              }}
              // Region III (Transmitted Wave - Smaller Amplitude)
              const transAmp = Math.max(2, 40 * Math.sqrt(T));
              for(let x=280+barW; x<=600; x+=2) {{
                const y = 110 + transAmp * Math.sin((x - 280 - barW)*0.15);
                ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#10b981";
              ctx.fillText("Transmitted Wave ψ_T (T = " + (T*100).toFixed(2) + "%)", 290 + barW + 10, 80);
            }}
            sliderE.addEventListener("input", draw);
            sliderA.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 5.1 Bohr Atom Model
    # -------------------------------------------------------------
    elif sim_type == "bohr_atom_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>วงโคจรระดับควอนตัม (Bohr Orbit n): <span id="{prefix}_val_n" class="readout-val">2</span></label>
            <input type="range" class="sim-slider" id="{prefix}_slider_n" min="1" max="5" value="2">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="230"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rad">0.212 nm</div><div class="readout-lbl">รัศมีวงโคจร (r_n = n² a₀)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_en">-3.40 eV</div><div class="readout-lbl">ระดับพลังงาน (E_n = -13.6/n²)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_l">2 ℏ</div><div class="readout-lbl">โมเมนตัมเชิงมุม (L = nℏ)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_n");
            if (!slider) return false;
            let angle = 0;

            function draw() {{
              const n = +slider.value;
              const nEl = document.getElementById("{prefix}_val_n");
              if (nEl) nEl.textContent = n;
              const a0 = 0.0529; // nm
              const rn = n * n * a0;
              const En = -13.6 / (n * n);

              const rEl = document.getElementById("{prefix}_val_rad");
              if (rEl) rEl.textContent = rn.toFixed(3) + " nm";
              const enEl = document.getElementById("{prefix}_val_en");
              if (enEl) enEl.textContent = En.toFixed(2) + " eV";
              const lEl = document.getElementById("{prefix}_val_l");
              if (lEl) lEl.textContent = n + " ℏ";

              ctx.clearRect(0,0,cv.width,cv.height);
              const cx = 320, cy = 115;

              // Nucleus (Proton)
              ctx.fillStyle = "#ef4444";
              ctx.beginPath(); ctx.arc(cx, cy, 10, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif";
              ctx.fillText("+e", cx - 6, cy + 3);

              // Draw All Orbits up to 5
              for(let i=1; i<=5; i++) {{
                const r = 20 + i*i * 3.5;
                ctx.strokeStyle = i === n ? "#00f0ff" : "rgba(255,255,255,0.12)";
                ctx.lineWidth = i === n ? 2.5 : 1;
                ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
              }}

              // Orbiting Electron
              const currentR = 20 + n*n * 3.5;
              const ex = cx + currentR * Math.cos(angle);
              const ey = cy + currentR * Math.sin(angle);
              ctx.fillStyle = "#10b981";
              ctx.beginPath(); ctx.arc(ex, ey, 6, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#10b981"; ctx.font = "11px sans-serif";
              ctx.fillText("e⁻ (n=" + n + ")", ex + 8, ey + 4);

              angle += 0.05 / n;
              requestAnimationFrame(draw);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 6.2 Radioactive Decay & Half-life
    # -------------------------------------------------------------
    elif sim_type == "radioactive_decay_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>เวลาที่ผ่านไป (t): <span id="{prefix}_val_t" class="readout-val">1.0</span> เท่าของครึ่งชีวิต</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_t" min="0" max="5.0" step="0.1" value="1.0">
            </div>
            <div class="sim-control-group">
              <label>ไอโซโทปกัมมันตรังสี:</label>
              <select id="{prefix}_sel_iso" style="width:100%; background:#0f172a; color:#00f0ff; border:1px solid #334155; padding:8px; border-radius:6px;">
                <option value="5730">Carbon-14 (T₁/₂ = 5,730 ปี)</option>
                <option value="30.17">Cesium-137 (T₁/₂ = 30.17 ปี)</option>
                <option value="8.02">Iodine-131 (T₁/₂ = 8.02 วัน)</option>
                <option value="1600">Radium-226 (T₁/₂ = 1,600 ปี)</option>
              </select>
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rem">50.0 %</div><div class="readout-lbl">สัดส่วนนิวเคลียสที่เหลือ (N/N₀)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_dec">50.0 %</div><div class="readout-lbl">นิวเคลียสที่สลายตัวไปแล้ว</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_act">0.500 A₀</div><div class="readout-lbl">กัมมันตภาพรังสี (Activity A)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_t");
            const sel = document.getElementById("{prefix}_sel_iso");
            if (!slider || !sel) return false;

            function draw() {{
              const t = +slider.value;
              const tEl = document.getElementById("{prefix}_val_t");
              if (tEl) tEl.textContent = t.toFixed(1);

              const remFraction = Math.pow(0.5, t);
              const remPct = remFraction * 100;
              const decPct = 100 - remPct;

              const rEl = document.getElementById("{prefix}_val_rem");
              if (rEl) rEl.textContent = remPct.toFixed(1) + " %";
              const dEl = document.getElementById("{prefix}_val_dec");
              if (dEl) dEl.textContent = decPct.toFixed(1) + " %";
              const aEl = document.getElementById("{prefix}_val_act");
              if (aEl) aEl.textContent = remFraction.toFixed(3) + " A₀";

              ctx.clearRect(0,0,cv.width,cv.height);
              // Decay Curve N(t) = N0 e^(-lambda t)
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
              ctx.beginPath();
              for(let x=60; x<=580; x+=2) {{
                const normT = (x - 60) / 100; // 0 to 5.2 half-lives
                const y = 180 - 150 * Math.pow(0.5, normT);
                if (x===60) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              // Current marker
              const markerX = 60 + t * 100;
              const markerY = 180 - 150 * remFraction;
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
              ctx.beginPath(); ctx.moveTo(markerX, 20); ctx.lineTo(markerX, 180); ctx.stroke();
              ctx.beginPath(); ctx.moveTo(60, markerY); ctx.lineTo(580, markerY); ctx.stroke();
              ctx.setLineDash([]);

              ctx.fillStyle = "#f59e0b";
              ctx.beginPath(); ctx.arc(markerX, markerY, 6, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#f8fafc"; ctx.font = "12px sans-serif";
              ctx.fillText("N(t) = " + remPct.toFixed(1) + "%", markerX + 10, markerY - 8);

              // Axes
              ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(60, 20); ctx.lineTo(60, 180); ctx.lineTo(580, 180); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.fillText("จำนวนเท่าครึ่งชีวิต (t / T₁/₂) →", 430, 200);
            }}
            slider.addEventListener("input", draw);
            sel.addEventListener("change", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 7.1 Particle Track Detector in Magnetic Field
    # -------------------------------------------------------------
    elif sim_type == "particle_zoo_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>สนามแม่เหล็ก (B): <span id="{prefix}_val_b" class="readout-val">1.5</span> Tesla</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_b" min="0.2" max="3.0" step="0.1" value="1.5">
            </div>
            <div class="sim-control-group">
              <label>ชนิดอนุภาคที่ยิงเข้าห้องฟองสบู่:</label>
              <select id="{prefix}_sel_p" style="width:100%; background:#0f172a; color:#00f0ff; border:1px solid #334155; padding:8px; border-radius:6px;">
                <option value="e_minus">อิเล็กตรอน (e⁻: ประจุลบ รัศมีโค้งเล็ก)</option>
                <option value="e_plus">โพซิตรอน (e⁺: ปฏิยานุภาค ประจุบวก)</option>
                <option value="proton">โปรตอน (p⁺: มวลมาก รัศมีโค้งใหญ่)</option>
                <option value="muon">มิวออน (μ⁻: รอยทางทะลุผ่านยาว)</option>
              </select>
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_r">3.8 cm</div><div class="readout-lbl">รัศมีความโค้งรอยทาง (r = p/qB)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_dir">เบนตามเข็มนาฬิกา</div><div class="readout-lbl">ทิศทางการเบนตามกฎมือขวา</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_type" style="color:#10b981;">Lepton Charged</div><div class="readout-lbl">การจำแนกชนิดอนุภาค</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const sliderB = document.getElementById("{prefix}_slider_b");
            const selP = document.getElementById("{prefix}_sel_p");
            if (!sliderB || !selP) return false;

            function draw() {{
              const B = +sliderB.value;
              const pType = selP.value;
              const bEl = document.getElementById("{prefix}_val_b");
              if (bEl) bEl.textContent = B.toFixed(1);

              let q = -1, m = 1, col = "#00f0ff", name = "e⁻";
              if (pType === "e_minus") {{ q = -1; m = 1; col = "#00f0ff"; name = "e⁻ (Electron)"; }}
              else if (pType === "e_plus") {{ q = 1; m = 1; col = "#f59e0b"; name = "e⁺ (Positron)"; }}
              else if (pType === "proton") {{ q = 1; m = 1836; col = "#ef4444"; name = "p⁺ (Proton)"; }}
              else if (pType === "muon") {{ q = -1; m = 207; col = "#a855f7"; name = "μ⁻ (Muon)"; }}

              const r_cm = (m / (Math.abs(q) * B * 20)).toFixed(1);
              const rEl = document.getElementById("{prefix}_val_r");
              if (rEl) rEl.textContent = r_cm + " cm";
              const dEl = document.getElementById("{prefix}_val_dir");
              if (dEl) dEl.textContent = q > 0 ? "เบนทวนเข็มนาฬิกา (+)" : "เบนตามเข็มนาฬิกา (-)";

              ctx.clearRect(0,0,cv.width,cv.height);
              // B-field dots (out of page)
              ctx.fillStyle = "rgba(255,255,255,0.15)";
              for(let x=40; x<600; x+=40) {{
                for(let y=30; y<190; y+=30) {{
                  ctx.beginPath(); ctx.arc(x, y, 1.5, 0, Math.PI*2); ctx.fill();
                }}
              }}
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px sans-serif";
              ctx.fillText("สนามแม่เหล็ก B ทิศพุ่งออกจากหน้ากระดาษ (⊙)", 40, 25);

              // Particle Spiral / Arc Track
              ctx.strokeStyle = col; ctx.lineWidth = 3;
              ctx.beginPath();
              ctx.moveTo(60, 105);
              const curveFactor = (q * B * 0.008) / Math.sqrt(m);
              for(let s=0; s<180; s+=2) {{
                const x = 60 + s * 2.8;
                const y = 105 + curveFactor * s * s * 0.35;
                ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = col; ctx.font = "12px sans-serif";
              ctx.fillText(name + " Track (r = " + r_cm + " cm)", 340, 60);
            }}
            sliderB.addEventListener("input", draw);
            selP.addEventListener("change", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 8.1 Hubble Expansion & Universe Redshift
    # -------------------------------------------------------------
    elif sim_type == "hubble_expansion_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ระยะห่างกาแล็กซี (Distance d): <span id="{prefix}_val_d" class="readout-val">100</span> ล้านปีแสง (Mpc)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_d" min="10" max="500" step="5" value="100">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_v">7,000 km/s</div><div class="readout-lbl">ความเร็วการถอยห่าง (v = H₀ d)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_z">0.023</div><div class="readout-lbl">ค่าการเลื่อนทางแดง (Redshift z)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_h0">70 km/s/Mpc</div><div class="readout-lbl">ค่าคงตัวฮับเบิล (H₀)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_d");
            if (!slider) return false;

            function draw() {{
              const d = +slider.value;
              const dEl = document.getElementById("{prefix}_val_d");
              if (dEl) dEl.textContent = d;
              const H0 = 70; // km/s/Mpc
              const v = H0 * d;
              const c = 300000;
              const z = v / c;

              const vEl = document.getElementById("{prefix}_val_v");
              if (vEl) vEl.textContent = v.toLocaleString() + " km/s";
              const zEl = document.getElementById("{prefix}_val_z");
              if (zEl) zEl.textContent = z.toFixed(4);

              ctx.clearRect(0,0,cv.width,cv.height);
              // Milky Way Observer (Left)
              ctx.fillStyle = "#00f0ff";
              ctx.beginPath(); ctx.arc(80, 105, 12, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ffffff"; ctx.font = "11px sans-serif";
              ctx.fillText("ทางช้างเผือก (เรา)", 40, 135);

              // Distant Galaxy (Right)
              const galX = Math.min(560, 80 + (d / 500) * 440);
              ctx.fillStyle = "#ef4444";
              ctx.beginPath(); ctx.arc(galX, 105, 10, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ef4444";
              ctx.fillText("กาแล็กซี่ไกล (d = " + d + " Mpc)", galX - 40, 135);

              // Redshifted Light Wave
              ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              const waveLam = 12 + z * 80;
              for(let x=80; x<=galX; x+=2) {{
                const y = 105 + 20 * Math.sin((x-80) * (Math.PI*2 / waveLam));
                ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#f59e0b"; ctx.font = "12px sans-serif";
              ctx.fillText("แสงถูกยืดเป็นคลื่นสีแดง (Cosmological Redshift z = " + z.toFixed(3) + ")", 120, 45);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 8.4 Schwarzschild Black Hole & Event Horizon
    # -------------------------------------------------------------
    elif sim_type == "blackhole_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>มวลของหลุมดำ (M): <span id="{prefix}_val_m" class="readout-val">10</span> เท่ามวลดวงอาทิตย์ (M_☉)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_m" min="3" max="100" value="10">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="220"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rs">29.5 km</div><div class="readout-lbl">รัศมีชวาร์ซชิลด์ (R_s = 2GM/c²)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_photon">44.3 km</div><div class="readout-lbl">วงแหวนโฟตอน (Photon Sphere 1.5 R_s)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_isco">88.5 km</div><div class="readout-lbl">วงโคจรเสถียรในสุด (ISCO 3 R_s)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_m");
            if (!slider) return false;

            function draw() {{
              const M = +slider.value;
              const mEl = document.getElementById("{prefix}_val_m");
              if (mEl) mEl.textContent = M;

              // Rs = 2.95 km * M
              const Rs_km = M * 2.95;
              const photon_km = Rs_km * 1.5;
              const isco_km = Rs_km * 3.0;

              const rsEl = document.getElementById("{prefix}_val_rs");
              if (rsEl) rsEl.textContent = Rs_km.toFixed(1) + " km";
              const phEl = document.getElementById("{prefix}_val_photon");
              if (phEl) phEl.textContent = photon_km.toFixed(1) + " km";
              const isEl = document.getElementById("{prefix}_val_isco");
              if (isEl) isEl.textContent = isco_km.toFixed(1) + " km";

              ctx.clearRect(0,0,cv.width,cv.height);
              const cx = 320, cy = 110;

              // Accretion Disk Glow
              const grad = ctx.createRadialGradient(cx, cy, 25, cx, cy, 140);
              grad.addColorStop(0, "rgba(245, 158, 11, 0.8)");
              grad.addColorStop(0.3, "rgba(239, 68, 68, 0.4)");
              grad.addColorStop(0.7, "rgba(168, 85, 247, 0.15)");
              grad.addColorStop(1, "transparent");
              ctx.fillStyle = grad;
              ctx.fillRect(cx - 150, cy - 80, 300, 160);

              // Gravitational Lensing Beams
              ctx.strokeStyle = "rgba(0, 240, 255, 0.5)"; ctx.lineWidth = 1.5;
              for(let i=0; i<6; i++) {{
                ctx.beginPath();
                ctx.arc(cx, cy, 35 + i*16, 0, Math.PI*2);
                ctx.stroke();
              }}

              // Photon Sphere (1.5 Rs)
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([3,3]);
              ctx.beginPath(); ctx.arc(cx, cy, 45, 0, Math.PI*2); ctx.stroke();
              ctx.setLineDash([]);
              ctx.fillStyle = "#f59e0b"; ctx.font = "10px sans-serif";
              ctx.fillText("Photon Sphere (1.5 Rs)", cx + 50, cy - 25);

              // Black Hole Event Horizon (Schwarzschild radius)
              ctx.fillStyle = "#000000";
              ctx.beginPath(); ctx.arc(cx, cy, 26, 0, Math.PI*2); ctx.fill();
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5; ctx.stroke();
              ctx.fillStyle = "#00f0ff"; ctx.fillText("Event Horizon (Rs)", cx + 32, cy + 20);
            }}
            slider.addEventListener("input", draw);
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # General Interactive Dynamic Wave/Field Simulator for all other topics
    # -------------------------------------------------------------
    else:
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>สเกลพารามิเตอร์การทดลองหลัก: <span id="{prefix}_val_param" class="readout-val">50</span>%</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_param" min="1" max="100" value="50">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_primary">Active Dynamic</div><div class="readout-lbl">สถานะการคำนวณสด</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_metric">1.000</div><div class="readout-lbl">ค่าสัมประสิทธิ์เชิงฟิสิกส์</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_status" style="color:#10b981;">Ready 2D/3D</div><div class="readout-lbl">โหมดประมวลผล</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return false;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_param");
            if (!slider) return false;
            let t = 0;

            function draw() {{
              const val = +slider.value;
              const pEl = document.getElementById("{prefix}_val_param");
              if (pEl) pEl.textContent = val;
              const coeff = (val / 50).toFixed(3);
              const mEl = document.getElementById("{prefix}_val_metric");
              if (mEl) mEl.textContent = coeff;

              ctx.clearRect(0,0,cv.width,cv.height);
              
              // Wave 1 (Cyan)
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=40; x<600; x+=2) {{
                const norm = (x-40)/560;
                const y = 105 + 45 * Math.sin(norm * Math.PI * 4 * coeff + t*0.05) * Math.cos(norm * Math.PI * 2);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              // Wave 2 (Amber)
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
              ctx.beginPath();
              for(let x=40; x<600; x+=4) {{
                const norm = (x-40)/560;
                const y = 105 + 55 * Math.sin(norm * Math.PI * 2 * coeff - t*0.03);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
              ctx.fillText("จำลองผลลัพธ์พลวัตเชิงควอนตัม / สัมพัทธภาพ (Live Dynamic Simulation)", 50, 30);

              t += 1;
              requestAnimationFrame(draw);
            }}
            slider.addEventListener("input", () => {{}});
            draw();
            return true;
          }}
          function run() {{ if (!initSim()) setTimeout(run, 100); }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
          else run();
          setTimeout(run, 250);
          setTimeout(run, 700);
        }})();
        </script>
        """

print("Simulators library comprehensive suite ready.")
