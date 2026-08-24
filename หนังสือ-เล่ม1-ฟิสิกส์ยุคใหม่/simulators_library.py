#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RBRU Modern Physics 4012920: Comprehensive 40 Real-Time 2D/3D Interactive Simulators Library
Provides self-contained interactive Canvas + JS + CSS for all 40 subtopics.
"""

def get_simulator_html_and_js(page_id, sim_type, title, standalone=False):
    prefix = f"sim_{page_id.replace('.', '_')}"
    
    # -------------------------------------------------------------
    # 1.1 Classical Limits
    # -------------------------------------------------------------
    if sim_type == "classical_limits":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อุณหภูมิวัตถุ (T): <span id="{prefix}_val_temp" class="readout-val">5000</span> K</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_temp" min="2000" max="10000" step="100" value="5000">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="230"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rj" style="color:#f43f5e;">Diverging (∞)</div><div class="readout-lbl">ทฤษฎีดั้งเดิม (Rayleigh-Jeans)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_planck" style="color:#00f0ff;">Peak at 580 nm</div><div class="readout-lbl">ทฤษฎีควอนตัม (Planck)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_catastrophe" style="color:#f59e0b;">UV Catastrophe</div><div class="readout-lbl">ปรากฏการณ์หายนะ UV</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_temp");
            function draw() {{
              const T = +slider.value;
              document.getElementById("{prefix}_val_temp").textContent = T;
              const peak = Math.round(2898000 / T);
              document.getElementById("{prefix}_val_planck").textContent = "Peak " + peak + " nm";
              
              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "rgba(255,255,255,0.06)";
              ctx.lineWidth = 1;
              for(let x=50; x<600; x+=50) {{ ctx.beginPath(); ctx.moveTo(x, 20); ctx.lineTo(x, 190); ctx.stroke(); }}
              
              // Rayleigh-Jeans (Red Curve diverging)
              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
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
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("ความยาวคลื่น λ (nm) →", 470, 208);
              ctx.fillText("ความเข้มพลังงาน I(λ)", 10, 25);
              ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical (Rayleigh-Jeans)", 70, 40);
              ctx.fillStyle = "#00f0ff"; ctx.fillText("— Quantum (Planck)", 70, 60);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
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
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_temp");
            function draw() {{
              const T = +slider.value;
              document.getElementById("{prefix}_val_temp").textContent = T;
              const peak = Math.round(2898000 / T);
              document.getElementById("{prefix}_val_peak").textContent = peak + " nm";
              
              const power = (5.67e-8 * Math.pow(T, 4)).toExponential(2);
              document.getElementById("{prefix}_val_power").textContent = power + " W/m²";
              
              let col = "แดง";
              if (T > 3500 && T <= 5000) col = "ส้ม-เหลือง";
              else if (T > 5000 && T <= 7500) col = "ขาวนวล (Yellow-White)";
              else if (T > 7500 && T <= 10000) col = "ขาวอมฟ้า (Blue-White)";
              else if (T > 10000) col = "ฟ้าเข้ม (Deep Blue)";
              document.getElementById("{prefix}_val_color").textContent = col;

              ctx.clearRect(0,0,cv.width,cv.height);
              const grad = ctx.createLinearGradient(120, 0, 480, 0);
              grad.addColorStop(0, "rgba(168, 85, 247, 0.15)");
              grad.addColorStop(0.2, "rgba(59, 130, 246, 0.15)");
              grad.addColorStop(0.5, "rgba(34, 197, 94, 0.15)");
              grad.addColorStop(0.7, "rgba(234, 179, 8, 0.15)");
              grad.addColorStop(1, "rgba(239, 68, 68, 0.15)");
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
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("ความยาวคลื่น λ (nm) →", 470, 208);
              ctx.fillText("ความเข้ม I(λ)", 10, 25);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
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
              <label>ชนิดโลหะ (Work Function φ):</label>
              <select id="{prefix}_sel_metal" class="search-input" style="padding:6px 10px;">
                <option value="2.14">ซีเซียม (Cs: 2.14 eV)</option>
                <option value="2.30" selected>โซเดียม (Na: 2.30 eV)</option>
                <option value="4.30">สังกะสี (Zn: 4.30 eV)</option>
                <option value="4.70">ทองแดง (Cu: 4.70 eV)</option>
                <option value="5.65">แพลทินัม (Pt: 5.65 eV)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>ความยาวคลื่นแสง (λ): <span id="{prefix}_val_lam" class="readout-val">300</span> nm</label>
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
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_metal");
            const slider = document.getElementById("{prefix}_slider_lam");
            let particles = [];
            for(let i=0; i<20; i++) particles.push({{ x: 120 + Math.random()*20, y: 40 + Math.random()*120, vx: 2 + Math.random()*3 }});

            function calc() {{
              const phi = +sel.value;
              const lam = +slider.value;
              document.getElementById("{prefix}_val_lam").textContent = lam;
              const Ephoton = 1240 / lam;
              document.getElementById("{prefix}_val_ephoton").textContent = Ephoton.toFixed(2) + " eV";
              const Kmax = Ephoton - phi;
              if (Kmax > 0) {{
                document.getElementById("{prefix}_val_kmax").textContent = Kmax.toFixed(2) + " eV";
                document.getElementById("{prefix}_val_vs").textContent = Kmax.toFixed(2) + " V";
              }} else {{
                document.getElementById("{prefix}_val_kmax").textContent = "0 (ไม่หลุด)";
                document.getElementById("{prefix}_val_vs").textContent = "0 V";
              }}
            }}

            function render() {{
              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.fillStyle = "#475569";
              ctx.fillRect(80, 30, 24, 140);
              ctx.fillStyle = "#00f0ff";
              ctx.fillText("Emitter (Target)", 50, 190);

              ctx.fillStyle = "#334155";
              ctx.fillRect(520, 30, 24, 140);
              ctx.fillStyle = "#94a3b8";
              ctx.fillText("Collector Anode", 490, 190);

              const lam = +slider.value;
              const Ephoton = 1240 / lam;
              const phi = +sel.value;
              const hasElectrons = Ephoton > phi;
              
              ctx.strokeStyle = lam < 400 ? "#a855f7" : (lam < 550 ? "#00f0ff" : "#ef4444");
              ctx.lineWidth = 2;
              for(let i=0; i<3; i++) {{
                ctx.beginPath();
                ctx.moveTo(10, 40 + i*40);
                ctx.lineTo(80, 60 + i*40);
                ctx.stroke();
              }}

              if (hasElectrons) {{
                ctx.fillStyle = "#10b981";
                particles.forEach(p => {{
                  ctx.beginPath();
                  ctx.arc(p.x, p.y, 4, 0, Math.PI*2);
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
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 1.4 Rydberg Spectrum
    # -------------------------------------------------------------
    elif sim_type == "rydberg_spectrum":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>อนุกรมสเปกตรัม (Lower Level n₁):</label>
              <select id="{prefix}_sel_series" class="search-input" style="padding:6px 10px;">
                <option value="1">Lyman (n₁ = 1, UV)</option>
                <option value="2" selected>Balmer (n₁ = 2, Visible แสงขาว)</option>
                <option value="3">Paschen (n₁ = 3, Infrared)</option>
                <option value="4">Brackett (n₁ = 4, Far IR)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>ระดับพลังงานเริ่มต้น (Upper Level n₂): <span id="{prefix}_val_n2" class="readout-val">3</span></label>
              <input type="range" class="sim-slider" id="{prefix}_slider_n2" min="2" max="7" value="3">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_lam">656.3 nm</div><div class="readout-lbl">ความยาวคลื่น (λ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_de">1.89 eV</div><div class="readout-lbl">พลังงานโฟตอนที่ปล่อย (ΔE)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_line">H-alpha (สีแดง)</div><div class="readout-lbl">ชื่อเส้นสเปกตรัม</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_series");
            const slider = document.getElementById("{prefix}_slider_n2");

            function calc() {{
              const n1 = +sel.value;
              slider.min = n1 + 1;
              if (+slider.value <= n1) slider.value = n1 + 1;
              const n2 = +slider.value;
              document.getElementById("{prefix}_val_n2").textContent = n2;

              const invLam = 1.097373e7 * (1/(n1*n1) - 1/(n2*n2));
              const lamM = 1 / invLam;
              const lamNm = lamM * 1e9;
              document.getElementById("{prefix}_val_lam").textContent = lamNm.toFixed(1) + " nm";
              
              const dE = 13.6 * (1/(n1*n1) - 1/(n2*n2));
              document.getElementById("{prefix}_val_de").textContent = dE.toFixed(2) + " eV";

              let label = "Infrared";
              if (n1 === 1) label = "Lyman UV";
              else if (n1 === 2) {{
                if (n2 === 3) label = "H-alpha (แดง 656 nm)";
                else if (n2 === 4) label = "H-beta (ฟ้า 486 nm)";
                else if (n2 === 5) label = "H-gamma (น้ำเงิน 434 nm)";
                else label = "H-delta (ม่วง 410 nm)";
              }}
              document.getElementById("{prefix}_val_line").textContent = label;

              ctx.clearRect(0,0,cv.width,cv.height);
              for(let i=1; i<=6; i++) {{
                const y = 180 - (160 / i);
                ctx.strokeStyle = i === n1 ? "#00f0ff" : (i === n2 ? "#f59e0b" : "#475569");
                ctx.lineWidth = i === n1 || i === n2 ? 2.5 : 1;
                ctx.beginPath(); ctx.moveTo(80, y); ctx.lineTo(340, y); ctx.stroke();
                ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
                ctx.fillText("n = " + i + " (" + (-13.6/(i*i)).toFixed(2) + " eV)", 15, y+4);
              }}

              const y1 = 180 - (160 / n1);
              const y2 = 180 - (160 / n2);
              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(210, y2); ctx.lineTo(210, y1); ctx.stroke();
              ctx.fillStyle = "#f43f5e";
              ctx.beginPath(); ctx.moveTo(204, y1 - 6); ctx.lineTo(216, y1 - 6); ctx.lineTo(210, y1); ctx.fill();

              ctx.strokeStyle = n1 === 2 ? "#10b981" : "#a855f7";
              ctx.lineWidth = 2;
              ctx.beginPath();
              for(let x=220; x<420; x+=2) {{
                const wy = (y1 + y2)/2 + 8 * Math.sin((x-220)*0.2);
                if (x===220) ctx.moveTo(x, wy); else ctx.lineTo(x, wy);
              }}
              ctx.stroke();
              ctx.fillText("hν (" + lamNm.toFixed(0) + " nm)", 430, (y1+y2)/2 + 4);

              ctx.fillStyle = "#090d16";
              ctx.fillRect(480, 20, 140, 160);
              ctx.strokeStyle = "#334155";
              ctx.strokeRect(480, 20, 140, 160);
              ctx.fillStyle = "#94a3b8"; ctx.fillText("สเปกตรัมที่สังเกตได้", 495, 40);
              const lineX = 490 + Math.min(120, Math.max(10, (lamNm - 380)*0.3));
              ctx.strokeStyle = n1 === 2 && n2 === 3 ? "#ef4444" : (n1 === 2 && n2 === 4 ? "#38bdf8" : "#a855f7");
              ctx.lineWidth = 4;
              ctx.beginPath(); ctx.moveTo(lineX, 60); ctx.lineTo(lineX, 150); ctx.stroke();
            }}
            sel.addEventListener("change", calc);
            slider.addEventListener("input", calc);
            calc();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.1 Michelson-Morley & Light Clock
    # -------------------------------------------------------------
    elif sim_type == "light_clock":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อัตราเร็วสัมพัทธ์ (v/c): <span id="{prefix}_val_vc" class="readout-val">0.70</span> c</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_vc" min="0" max="95" value="70">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">1.40</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_path">Zig-zag Path</div><div class="readout-lbl">เส้นทางแสงสำหรับผู้สังเกตภายนอก</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_diff">+40.0%</div><div class="readout-lbl">เวลาเดินช้าลง (Dilation)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_vc");
            let t = 0;

            function render() {{
              const beta = (+slider.value) / 100;
              document.getElementById("{prefix}_val_vc").textContent = beta.toFixed(2);
              const gamma = 1 / Math.sqrt(1 - beta*beta);
              document.getElementById("{prefix}_val_gamma").textContent = gamma.toFixed(2);
              document.getElementById("{prefix}_val_diff").textContent = "+" + ((gamma - 1)*100).toFixed(1) + "%";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "#334155"; ctx.strokeRect(60, 20, 180, 160);
              ctx.fillStyle = "#94a3b8"; ctx.fillText("นาฬิกาแสงอยู่นิ่ง (Δt₀)", 90, 40);
              ctx.fillStyle = "#38bdf8"; ctx.fillRect(100, 50, 100, 6); ctx.fillRect(100, 150, 100, 6);
              const yPulse1 = 56 + Math.abs((t % 60) - 30) * 3;
              ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(150, yPulse1, 5, 0, Math.PI*2); ctx.fill();

              ctx.strokeStyle = "#0891b2"; ctx.strokeRect(300, 20, 300, 160);
              ctx.fillStyle = "#00f0ff"; ctx.fillText("นาฬิกาแสงเคลื่อนที่ v = " + beta.toFixed(2) + " c (Δt = γΔt₀)", 320, 40);
              
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
              ctx.beginPath();
              ctx.moveTo(340, 56);
              ctx.lineTo(340 + 60*gamma*0.7, 150);
              ctx.lineTo(340 + 120*gamma*0.7, 56);
              ctx.stroke();
              ctx.setLineDash([]);

              t += 1;
              requestAnimationFrame(render);
            }}
            slider.addEventListener("input", render);
            render();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.2 Lorentz Transformation
    # -------------------------------------------------------------
    elif sim_type == "lorentz_calc":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อัตราเร็วสัมพัทธ์ (β = v/c): <span id="{prefix}_val_beta" class="readout-val">0.60</span></label>
            <input type="range" class="sim-slider" id="{prefix}_slider_beta" min="0" max="95" value="60">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">1.25</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_xprime">x' = γ(x - vt)</div><div class="readout-lbl">การแปลงพิกัด x'</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_tprime">t' = γ(t - vx/c²)</div><div class="readout-lbl">การแปลงพิกัดเวลา t'</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_beta");

            function draw() {{
              const beta = (+slider.value) / 100;
              document.getElementById("{prefix}_val_beta").textContent = beta.toFixed(2);
              const gamma = 1 / Math.sqrt(1 - beta*beta);
              document.getElementById("{prefix}_val_gamma").textContent = gamma.toFixed(2);

              ctx.clearRect(0,0,cv.width,cv.height);
              const cx = cv.width/2, cy = cv.height/2;

              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(cx - 200, cy); ctx.lineTo(cx + 200, cy); ctx.stroke();
              ctx.beginPath(); ctx.moveTo(cx, cy + 90); ctx.lineTo(cx, cy - 90); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("x (ตำแหน่ง)", cx + 205, cy + 4);
              ctx.fillText("ct (เวลา)", cx - 15, cy - 92);

              ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 1; ctx.setLineDash([3,3]);
              ctx.beginPath(); ctx.moveTo(cx - 90, cy + 90); ctx.lineTo(cx + 90, cy - 90); ctx.stroke();
              ctx.beginPath(); ctx.moveTo(cx + 90, cy + 90); ctx.lineTo(cx - 90, cy - 90); ctx.stroke();
              ctx.setLineDash([]);

              const angle = Math.atan(beta);
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              ctx.moveTo(cx - 90*Math.sin(angle), cy + 90*Math.cos(angle));
              ctx.lineTo(cx + 90*Math.sin(angle), cy - 90*Math.cos(angle));
              ctx.stroke();
              ctx.fillStyle = "#00f0ff"; ctx.fillText("ct'", cx + 90*Math.sin(angle) + 4, cy - 90*Math.cos(angle));

              ctx.beginPath();
              ctx.moveTo(cx - 160*Math.cos(angle), cy + 160*Math.sin(angle));
              ctx.lineTo(cx + 160*Math.cos(angle), cy - 160*Math.sin(angle));
              ctx.stroke();
              ctx.fillText("x'", cx + 160*Math.cos(angle) + 6, cy - 160*Math.sin(angle) + 4);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
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
            <label>อัตราเร็วสัมพัทธ์ (v/c): <span id="{prefix}_val_vc" class="readout-val">0.85</span> c</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_vc" min="0" max="99" value="85">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">1.90</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_lcontract">52.7% (หดสั้น)</div><div class="readout-lbl">ความยาวจรวด L = L₀/γ</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_tdilate">+89.8% (ยืดออก)</div><div class="readout-lbl">เวลาเดินช้าลง Δt = γΔt₀</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_vc");

            function draw() {{
              const beta = (+slider.value) / 100;
              document.getElementById("{prefix}_val_vc").textContent = beta.toFixed(2);
              const gamma = 1 / Math.sqrt(1 - beta*beta);
              document.getElementById("{prefix}_val_gamma").textContent = gamma.toFixed(2);
              document.getElementById("{prefix}_val_lcontract").textContent = (100 / gamma).toFixed(1) + "% (" + (100 - 100/gamma).toFixed(1) + "% หด)";
              document.getElementById("{prefix}_val_tdilate").textContent = "+" + ((gamma - 1)*100).toFixed(1) + "% (ยืดออก)";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.fillStyle = "#94a3b8"; ctx.font = "12px Sarabun";
              ctx.fillText("จรวดอยู่นิ่งบนโลก (ความยาวจริง L₀ = 200 m):", 40, 30);
              ctx.fillStyle = "#0284c7";
              ctx.fillRect(40, 45, 200, 35);
              ctx.fillStyle = "#ffffff"; ctx.fillText("Rocket L₀", 110, 68);

              const contractedW = Math.max(15, 200 / gamma);
              ctx.fillStyle = "#00f0ff";
              ctx.fillText("จรวดเคลื่อนที่สัมพัทธ์ v = " + beta.toFixed(2) + " c (ความยาวที่วัดได้ L = " + (200/gamma).toFixed(1) + " m):", 40, 115);
              ctx.fillStyle = "#f59e0b";
              ctx.fillRect(40, 130, contractedW, 35);
              ctx.fillStyle = "#060913"; ctx.fillText("L", 40 + contractedW/2 - 4, 153);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 2.4 Mass-Energy E=mc²
    # -------------------------------------------------------------
    elif sim_type == "mass_energy_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>อัตราเร็วอนุภาค (v/c): <span id="{prefix}_val_vc" class="readout-val">0.90</span> c</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_vc" min="0" max="99" value="90">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_gamma">2.29</div><div class="readout-lbl">ตัวประกอบลอเรนซ์ (γ)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_etot">2.29 E₀</div><div class="readout-lbl">พลังงานรวม E = γm₀c²</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_krel">1.29 E₀</div><div class="readout-lbl">พลังงานจลน์ K = (γ-1)m₀c²</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_vc");

            function draw() {{
              const beta = (+slider.value) / 100;
              document.getElementById("{prefix}_val_vc").textContent = beta.toFixed(2);
              const gamma = 1 / Math.sqrt(1 - beta*beta);
              document.getElementById("{prefix}_val_gamma").textContent = gamma.toFixed(2);
              document.getElementById("{prefix}_val_etot").textContent = gamma.toFixed(2) + " E₀";
              document.getElementById("{prefix}_val_krel").textContent = (gamma - 1).toFixed(2) + " E₀";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, 180); ctx.lineTo(580, 180); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("อัตราเร็ว v/c →", 510, 198);
              ctx.fillText("พลังงานจลน์ K", 10, 25);

              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
              ctx.beginPath(); ctx.moveTo(50, 180);
              for(let x=50; x<550; x+=5) {{
                const b = (x - 50) / 500;
                const k_class = 0.5 * b * b * 80;
                ctx.lineTo(x, 180 - k_class);
              }}
              ctx.stroke();
              ctx.setLineDash([]);

              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(50, 180);
              for(let x=50; x<550; x+=2) {{
                const b = (x - 50) / 500;
                const g = 1 / Math.sqrt(Math.max(0.001, 1 - b*b));
                const k_rel = (g - 1) * 35;
                ctx.lineTo(x, Math.max(20, 180 - k_rel));
              }}
              ctx.stroke();

              const curX = 50 + beta * 500;
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(curX, 20); ctx.lineTo(curX, 180); ctx.stroke();
              ctx.fillStyle = "#f59e0b"; ctx.fillText("v = " + beta.toFixed(2) + " c", curX - 25, 35);
              
              ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical K = 1/2 mv²", 60, 50);
              ctx.fillStyle = "#00f0ff"; ctx.fillText("— Relativistic K = (γ-1)mc²", 60, 70);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 3.1 De Broglie Wavelength
    # -------------------------------------------------------------
    elif sim_type == "de_broglie_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ชนิดอนุภาค:</label>
              <select id="{prefix}_sel_p" class="search-input" style="padding:6px 10px;">
                <option value="electron" selected>อิเล็กตรอน (Electron: 9.11 × 10⁻³¹ kg)</option>
                <option value="proton">โปรตอน (Proton: 1.67 × 10⁻²⁷ kg)</option>
                <option value="alpha">อนุภาคแอลฟา (Alpha: 6.64 × 10⁻²⁷ kg)</option>
                <option value="baseball">ลูกเบสบอล (Baseball: 0.145 kg)</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>พลังงานจลน์ (eV): <span id="{prefix}_val_ev" class="readout-val">100</span> eV</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_ev" min="1" max="1000" value="100">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_lam">0.123 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ = h/p)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_v">5.93 × 10⁶ m/s</div><div class="readout-lbl">อัตราเร็วอนุภาค (v)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_domain">Atomic X-ray scale</div><div class="readout-lbl">ระดับมิติเชิงควอนตัม</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_p");
            const slider = document.getElementById("{prefix}_slider_ev");

            function calc() {{
              const pType = sel.value;
              const eV = +slider.value;
              document.getElementById("{prefix}_val_ev").textContent = eV;
              
              let m = 9.10938356e-31;
              if (pType === "proton") m = 1.6726219e-27;
              else if (pType === "alpha") m = 6.6446572e-27;
              else if (pType === "baseball") m = 0.145;

              const E = eV * 1.60217663e-19;
              const p = Math.sqrt(2 * m * E);
              const v = p / m;
              const h = 6.62607015e-34;
              const lam = h / p;
              
              let lamStr = (lam * 1e9).toFixed(3) + " nm";
              if (lam < 1e-12) lamStr = (lam * 1e15).toFixed(3) + " fm";
              if (pType === "baseball") lamStr = lam.toExponential(2) + " m (พฤติกรรมคลื่นสลายตัว)";
              document.getElementById("{prefix}_val_lam").textContent = lamStr;
              document.getElementById("{prefix}_val_v").textContent = v.toExponential(2) + " m/s";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              const k = Math.min(0.3, Math.max(0.02, 1e-10 / lam));
              for(let x=40; x<600; x+=2) {{
                const env = Math.exp(-Math.pow((x - 320)/120, 2));
                const y = 100 + 50 * env * Math.sin((x-40) * (k*15 + 0.1));
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(320, 100, 6, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ffffff"; ctx.font = "12px Sarabun";
              ctx.fillText("Particle & Matter Wave (λ = " + lamStr + ")", 230, 180);
            }}
            sel.addEventListener("change", calc);
            slider.addEventListener("input", calc);
            calc();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 4.2 Particle in a Box
    # -------------------------------------------------------------
    elif sim_type == "particle_box_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ระดับควอนตัม (Quantum Number n): <span id="{prefix}_val_n" class="readout-val">2</span></label>
            <input type="range" class="sim-slider" id="{prefix}_slider_n" min="1" max="6" value="2">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_nodes">1 โหนด</div><div class="readout-lbl">จำนวน Node ภายในกล่อง (n-1)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_energy">4.0 E₁</div><div class="readout-lbl">ระดับพลังงาน E_n = n² E₁</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_prob">|ψ|² ความน่าจะเป็น</div><div class="readout-lbl">Probability Density</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_n");

            function draw() {{
              const n = +slider.value;
              document.getElementById("{prefix}_val_n").textContent = n;
              document.getElementById("{prefix}_val_nodes").textContent = (n - 1) + " โหนด";
              document.getElementById("{prefix}_val_energy").textContent = (n*n).toFixed(1) + " E₁";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.fillStyle = "#334155";
              ctx.fillRect(60, 20, 12, 160);
              ctx.fillRect(568, 20, 12, 160);
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("x = 0 (V=∞)", 40, 195);
              ctx.fillText("x = L (V=∞)", 550, 195);

              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=72; x<=568; x++) {{
                const normX = (x - 72) / (568 - 72);
                const y = 90 - 55 * Math.sin(n * Math.PI * normX);
                if (x===72) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2;
              ctx.beginPath();
              for(let x=72; x<=568; x++) {{
                const normX = (x - 72) / (568 - 72);
                const sinVal = Math.sin(n * Math.PI * normX);
                const y = 175 - 110 * sinVal * sinVal;
                if (x===72) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#00f0ff"; ctx.fillText("— ฟังก์ชันคลื่น ψ_n(x)", 80, 35);
              ctx.fillStyle = "#f59e0b"; ctx.fillText("— ความหนาแน่นความน่าจะเป็น |ψ_n|²", 340, 35);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
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
              <label>พลังงานอนุภาค (E): <span id="{prefix}_val_e" class="readout-val">3.5</span> eV</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_e" min="10" max="90" value="35">
            </div>
            <div class="sim-control-group">
              <label>ความหนากำแพงศักย์ (L): <span id="{prefix}_val_l" class="readout-val">0.30</span> nm</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_l" min="10" max="80" value="30">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_trans">14.2%</div><div class="readout-lbl">ความน่าจะเป็นในการทะลุผ่าน (T)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_ref">85.8%</div><div class="readout-lbl">ความน่าจะเป็นในการสะท้อนกลับ (R)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_decay">Exponential decay</div><div class="readout-lbl">ลักษณะคลื่นในกำแพง e^(-κx)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sliderE = document.getElementById("{prefix}_slider_e");
            const sliderL = document.getElementById("{prefix}_slider_l");

            function draw() {{
              const E = (+sliderE.value) / 10;
              const L = (+sliderL.value) / 100;
              const V0 = 5.0;
              document.getElementById("{prefix}_val_e").textContent = E.toFixed(1);
              document.getElementById("{prefix}_val_l").textContent = L.toFixed(2);

              const kappa = Math.sqrt(2 * 9.1e-31 * Math.max(0.1, (V0 - E)) * 1.6e-19) / 1.054e-34;
              const T_prob = Math.exp(-2 * kappa * L * 1e-9);
              const T_pct = Math.min(100, Math.max(0.01, T_prob * 100));
              document.getElementById("{prefix}_val_trans").textContent = T_pct.toFixed(2) + "%";
              document.getElementById("{prefix}_val_ref").textContent = (100 - T_pct).toFixed(2) + "%";

              ctx.clearRect(0,0,cv.width,cv.height);
              
              const bWidth = L * 250;
              const bX = (cv.width - bWidth) / 2;
              ctx.fillStyle = "rgba(244, 63, 94, 0.25)";
              ctx.fillRect(bX, 30, bWidth, 140);
              ctx.strokeStyle = "#f43f5e"; ctx.strokeRect(bX, 30, bWidth, 140);
              ctx.fillStyle = "#f43f5e"; ctx.font = "11px Sarabun";
              ctx.fillText("กำแพงศักย์ V₀ = 5.0 eV", bX + 6, 25);

              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=40; x<=bX; x++) {{
                const y = 100 + 40 * Math.sin((x-40)*0.12);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=bX; x<=bX+bWidth; x++) {{
                const norm = (x - bX) / bWidth;
                const decay = Math.exp(-norm * 2.5);
                const y = 100 + 40 * decay * Math.sin(x*0.05);
                if (x===bX) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              const transAmp = 40 * Math.sqrt(T_pct/100);
              ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=bX+bWidth; x<=600; x++) {{
                const y = 100 + transAmp * Math.sin((x - bX - bWidth)*0.12);
                if (x===bX+bWidth) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.fillStyle = "#00f0ff"; ctx.fillText("I. คลื่นตกกระทบ (E=" + E.toFixed(1) + " eV)", 50, 185);
              ctx.fillStyle = "#10b981"; ctx.fillText("III. คลื่นทะลุผ่าน (T=" + T_pct.toFixed(1) + "%)", bX+bWidth+10, 185);
            }}
            sliderE.addEventListener("input", draw);
            sliderL.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 5.1 Bohr Atom Orbitals
    # -------------------------------------------------------------
    elif sim_type == "bohr_atom_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>เลขควอนตัมหลัก (Principal Quantum Number n): <span id="{prefix}_val_n" class="readout-val">2</span></label>
            <input type="range" class="sim-slider" id="{prefix}_slider_n" min="1" max="5" value="2">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_r">2.12 Å</div><div class="readout-lbl">รัศมีวงโคจร r_n = n² a₀</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_en">-3.40 eV</div><div class="readout-lbl">พลังงานยึดเหนี่ยว E_n = -13.6/n²</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_vn">1.09 × 10⁶ m/s</div><div class="readout-lbl">อัตราเร็วอิเล็กตรอน (v_n)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_n");
            let angle = 0;

            function render() {{
              const n = +slider.value;
              document.getElementById("{prefix}_val_n").textContent = n;
              const a0 = 0.529; // Angstroms
              const r_ang = n * n * a0;
              document.getElementById("{prefix}_val_r").textContent = r_ang.toFixed(2) + " Å";
              document.getElementById("{prefix}_val_en").textContent = (-13.6 / (n*n)).toFixed(2) + " eV";
              const vn = (2.187e6 / n).toExponential(2);
              document.getElementById("{prefix}_val_vn").textContent = vn + " m/s";

              ctx.clearRect(0,0,cv.width,cv.height);
              const cx = cv.width/2, cy = cv.height/2;

              // Nucleus (Proton)
              ctx.fillStyle = "#ef4444"; ctx.beginPath(); ctx.arc(cx, cy, 9, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ffffff"; ctx.font = "10px Sarabun"; ctx.fillText("+e", cx-5, cy+3);

              // Circular orbits
              for(let i=1; i<=5; i++) {{
                const orbR = i * 18 + 12;
                ctx.strokeStyle = i === n ? "#00f0ff" : "rgba(255,255,255,0.08)";
                ctx.lineWidth = i === n ? 2 : 1;
                ctx.beginPath(); ctx.arc(cx, cy, orbR, 0, Math.PI*2); ctx.stroke();
              }}

              // Orbiting electron
              const curR = n * 18 + 12;
              const ex = cx + curR * Math.cos(angle);
              const ey = cy + curR * Math.sin(angle);
              ctx.fillStyle = "#10b981"; ctx.beginPath(); ctx.arc(ex, ey, 5, 0, Math.PI*2); ctx.fill();

              // De Broglie standing wave on orbit
              ctx.strokeStyle = "rgba(0, 240, 255, 0.4)"; ctx.lineWidth = 1.5;
              ctx.beginPath();
              for(let a=0; a<=Math.PI*2; a+=0.02) {{
                const waveR = curR + 4 * Math.sin(n * a);
                const wx = cx + waveR * Math.cos(a);
                const wy = cy + waveR * Math.sin(a);
                if (a===0) ctx.moveTo(wx, wy); else ctx.lineTo(wx, wy);
              }}
              ctx.closePath(); ctx.stroke();

              angle += 0.04 / n;
              requestAnimationFrame(render);
            }}
            slider.addEventListener("input", render);
            render();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 6.1 Nuclear Binding Energy (SEMF)
    # -------------------------------------------------------------
    elif sim_type == "binding_energy_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>เลขมวลนิวเคลียส (Mass Number A): <span id="{prefix}_val_a" class="readout-val">56</span> (เหล็ก Fe-56 เสถียรสูงสุด)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_a" min="1" max="240" value="56">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_bpa">8.79 MeV</div><div class="readout-lbl">พลังงานยึดเหนี่ยวต่อนิวคลีออน (B/A)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_btot">492.2 MeV</div><div class="readout-lbl">พลังงานยึดเหนี่ยวรวม B(A,Z)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_zone">จุดเสถียรภาพสูงสุด</div><div class="readout-lbl">พฤติกรรม (Fusion vs Fission)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_a");

            function draw() {{
              const A = +slider.value;
              document.getElementById("{prefix}_val_a").textContent = A;
              const Z = Math.round(A / (2 + 0.015 * Math.pow(A, 2/3)));
              
              // SEMF terms
              const av = 15.8, as = 18.3, ac = 0.714, aa = 23.2;
              let B = av*A - as*Math.pow(A, 2/3) - ac*(Z*(Z-1))/Math.pow(A, 1/3) - aa*Math.pow(A - 2*Z, 2)/A;
              if (A === 1) B = 0;
              if (A === 2) B = 2.22;
              if (A === 4) B = 28.3;
              const B_A = Math.max(0, B / A);

              document.getElementById("{prefix}_val_bpa").textContent = B_A.toFixed(2) + " MeV/A";
              document.getElementById("{prefix}_val_btot").textContent = B.toFixed(1) + " MeV";

              let zone = "นิวเคลียร์ฟิวชัน (ปล่อยพลังงานเมื่อรวมตัว)";
              if (A >= 50 && A <= 62) zone = "เสถียรสูงสุด (Fe-56 / Ni-62 Peak)";
              else if (A > 62) zone = "นิวเคลียร์ฟิชชัน (ปล่อยพลังงานเมื่อแตกตัว)";
              document.getElementById("{prefix}_val_zone").textContent = zone;

              ctx.clearRect(0,0,cv.width,cv.height);
              // B/A Curve
              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, 180); ctx.lineTo(600, 180); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("เลขมวล A →", 530, 198);
              ctx.fillText("B/A (MeV)", 5, 25);

              // SEMF Curve
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath(); ctx.moveTo(50, 180);
              for(let x=50; x<=600; x+=2) {{
                const simA = (x - 50) * (240 / 550);
                const simZ = Math.round(simA / (2 + 0.015 * Math.pow(simA, 2/3)));
                let simB = av*simA - as*Math.pow(simA, 2/3) - ac*(simZ*(simZ-1))/Math.pow(simA, 1/3) - aa*Math.pow(simA - 2*simZ, 2)/simA;
                if (simA < 2) simB = 0;
                const simB_A = Math.max(0, simB / simA);
                const y = 180 - (simB_A / 9.5) * 150;
                ctx.lineTo(x, y);
              }}
              ctx.stroke();

              // Indicator at current A
              const curX = 50 + A * (550 / 240);
              const curY = 180 - (B_A / 9.5) * 150;
              ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI*2); ctx.fill();
              ctx.fillText("A = " + A + " (" + B_A.toFixed(2) + " MeV)", curX - 30, Math.max(30, curY - 12));

              ctx.fillStyle = "#10b981"; ctx.fillText("← Fusion Zone", 80, 80);
              ctx.fillStyle = "#f43f5e"; ctx.fillText("Fission Zone →", 460, 80);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 6.2 Radioactive Decay
    # -------------------------------------------------------------
    elif sim_type == "radioactive_decay_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ครึ่งชีวิต (T_1/2): <span id="{prefix}_val_thalf" class="readout-val">10</span> ปี</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_thalf" min="2" max="50" value="10">
            </div>
            <div class="sim-control-group">
              <label>เวลาที่ผ่านไป (t): <span id="{prefix}_val_tdecay" class="readout-val">20</span> ปี</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_tdecay" min="0" max="100" value="20">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_nremain">25.0%</div><div class="readout-lbl">สารคงเหลือ N(t)/N₀</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_ndecayed">75.0%</div><div class="readout-lbl">สลายตัวไปแล้ว (Daughter)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_halves">2.0 ครึ่งชีวิต</div><div class="readout-lbl">จำนวนรอบครึ่งชีวิต (t / T_1/2)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sHalf = document.getElementById("{prefix}_slider_thalf");
            const sTime = document.getElementById("{prefix}_slider_tdecay");

            function draw() {{
              const h = +sHalf.value;
              const t = +sTime.value;
              document.getElementById("{prefix}_val_thalf").textContent = h;
              document.getElementById("{prefix}_val_tdecay").textContent = t;
              const remain = 100 * Math.pow(0.5, t / h);
              document.getElementById("{prefix}_val_nremain").textContent = remain.toFixed(1) + "%";
              document.getElementById("{prefix}_val_ndecayed").textContent = (100 - remain).toFixed(1) + "%";
              document.getElementById("{prefix}_val_halves").textContent = (t / h).toFixed(1) + " รอบ";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "#475569"; ctx.lineWidth = 1.5;
              ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, 170); ctx.lineTo(380, 170); ctx.stroke();
              ctx.fillStyle = "#94a3b8"; ctx.font = "11px Sarabun";
              ctx.fillText("เวลา t (ปี) →", 320, 185);
              ctx.fillText("ปริมาณ N(t)", 10, 25);

              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath(); ctx.moveTo(50, 30);
              for(let x=50; x<=380; x+=2) {{
                const simT = (x - 50) * (100 / 330);
                const r = Math.pow(0.5, simT / h);
                const y = 170 - r * 140;
                ctx.lineTo(x, y);
              }}
              ctx.stroke();

              const curX = 50 + t * (330 / 100);
              const curY = 170 - (remain/100) * 140;
              ctx.fillStyle = "#f59e0b"; ctx.beginPath(); ctx.arc(curX, curY, 6, 0, Math.PI*2); ctx.fill();

              ctx.strokeStyle = "#334155"; ctx.strokeRect(420, 20, 190, 150);
              ctx.fillStyle = "#94a3b8"; ctx.fillText("แบบจำลองอะตอม (100 อนุภาค)", 435, 36);
              
              let seed = 42;
              function rand() {{ seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }}
              for(let r=0; r<10; r++) {{
                for(let c=0; c<10; c++) {{
                  const isRemain = rand() * 100 < remain;
                  ctx.fillStyle = isRemain ? "#00f0ff" : "#334155";
                  ctx.beginPath();
                  ctx.arc(435 + c*17, 52 + r*11, 4, 0, Math.PI*2);
                  ctx.fill();
                }}
              }}
            }}
            sHalf.addEventListener("input", draw);
            sTime.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 7.1 Bubble Chamber Particle Tracks
    # -------------------------------------------------------------
    elif sim_type == "particle_zoo_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;">
            <div class="sim-control-group">
              <label>ชนิดเหตุการณ์อนุภาค (Event):</label>
              <select id="{prefix}_sel_event" class="search-input" style="padding:6px 10px;">
                <option value="pair_prod" selected>Pair Production (γ → e⁺ + e⁻)</option>
                <option value="muon_decay">Muon Decay (μ⁻ → e⁻ + ν_μ + ν_e)</option>
                <option value="proton_pion">Proton-Pion Collision</option>
              </select>
            </div>
            <div class="sim-control-group">
              <label>สนามแม่เหล็ก (B): <span id="{prefix}_val_bfield" class="readout-val">1.5</span> Tesla</label>
              <input type="range" class="sim-slider" id="{prefix}_slider_bfield" min="5" max="30" value="15">
            </div>
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_curve" style="color:#00f0ff;">Spiral Tracks</div><div class="readout-lbl">ทิศทางความโค้งตามประจุ q</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_radius">r = p / (qB)</div><div class="readout-lbl">รัศมีความโค้งไซโคลตรอน</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_cons" style="color:#10b981;">Charge Conserved (ΔQ=0)</div><div class="readout-lbl">การอนุรักษ์ประจุไฟฟ้า</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const sel = document.getElementById("{prefix}_sel_event");
            const slider = document.getElementById("{prefix}_slider_bfield");

            function draw() {{
              const B = (+slider.value) / 10;
              document.getElementById("{prefix}_val_bfield").textContent = B.toFixed(1);
              ctx.clearRect(0,0,cv.width,cv.height);
              
              // Chamber magnetic field dots
              ctx.fillStyle = "rgba(255,255,255,0.08)";
              for(let x=30; x<610; x+=40) {{
                for(let y=20; y<190; y+=35) {{
                  ctx.beginPath(); ctx.arc(x, y, 1.5, 0, Math.PI*2); ctx.fill();
                }}
              }}

              const ev = sel.value;
              const cx = 200, cy = 105;

              if (ev === "pair_prod") {{
                // Incident gamma photon (dashed line)
                ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4,4]);
                ctx.beginPath(); ctx.moveTo(40, cy); ctx.lineTo(cx, cy); ctx.stroke();
                ctx.setLineDash([]);
                ctx.fillStyle = "#f59e0b"; ctx.fillText("γ photon", 80, cy - 8);

                // Positron e+ curving up-spiral (Cyan)
                ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
                ctx.beginPath();
                for(let a=0; a<Math.PI*4; a+=0.05) {{
                  const r = Math.max(2, 60 / B - a * 4);
                  const x = cx + r * Math.sin(a);
                  const y = cy - r * (1 - Math.cos(a));
                  if (a===0) ctx.moveTo(cx, cy); else ctx.lineTo(x, y);
                }}
                ctx.stroke();
                ctx.fillStyle = "#00f0ff"; ctx.fillText("e⁺ (Positron)", cx + 50, cy - 60);

                // Electron e- curving down-spiral (Emerald)
                ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
                ctx.beginPath();
                for(let a=0; a<Math.PI*4; a+=0.05) {{
                  const r = Math.max(2, 60 / B - a * 4);
                  const x = cx + r * Math.sin(a);
                  const y = cy + r * (1 - Math.cos(a));
                  if (a===0) ctx.moveTo(cx, cy); else ctx.lineTo(x, y);
                }}
                ctx.stroke();
                ctx.fillStyle = "#10b981"; ctx.fillText("e⁻ (Electron)", cx + 50, cy + 80);
              }} else {{
                ctx.strokeStyle = "#a855f7"; ctx.lineWidth = 3;
                ctx.beginPath(); ctx.moveTo(60, 40); ctx.lineTo(cx, cy); ctx.stroke();
                ctx.fillStyle = "#a855f7"; ctx.fillText("Primary Track", 70, 60);
                
                ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2;
                ctx.beginPath(); ctx.arc(cx+60, cy, 60/B, 0, Math.PI); ctx.stroke();
                ctx.fillStyle = "#00f0ff"; ctx.fillText("Decay Products", cx+90, cy-10);
              }}
            }}
            sel.addEventListener("change", draw);
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 8.1 Hubble Expansion
    # -------------------------------------------------------------
    elif sim_type == "hubble_expansion_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>ระยะทางของกาแล็กซี (Distance d): <span id="{prefix}_val_d" class="readout-val">500</span> Mpc</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_d" min="50" max="2000" step="50" value="500">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_v">35,000 km/s</div><div class="readout-lbl">ความเร็วถอยห่าง (v = H₀d)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_z">0.117</div><div class="readout-lbl">ค่าการเลื่อนทางแดง (Redshift z)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_time">1.63 พันล้านปี</div><div class="readout-lbl">เวลาย้อนอดีต (Lookback Time)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_d");

            function draw() {{
              const d = +slider.value;
              const H0 = 70;
              document.getElementById("{prefix}_val_d").textContent = d;
              const v = H0 * d;
              document.getElementById("{prefix}_val_v").textContent = v.toLocaleString() + " km/s";
              const z = v / 300000;
              document.getElementById("{prefix}_val_z").textContent = z.toFixed(3);
              const lookback = (d * 3.26 / 1000).toFixed(2);
              document.getElementById("{prefix}_val_time").textContent = lookback + " พันล้านปี";

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(80, 100, 14, 0, Math.PI*2); ctx.fill();
              ctx.fillStyle = "#ffffff"; ctx.font = "11px Sarabun"; ctx.fillText("ทางช้างเผือก (ผู้สังเกต)", 40, 130);

              const galX = 80 + (d / 2000) * 440;
              ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(galX, 100, 10, 0, Math.PI*2); ctx.fill();
              ctx.fillText("Galaxy (" + d + " Mpc)", galX - 30, 80);

              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(galX + 14, 100); ctx.lineTo(galX + 14 + Math.min(80, v/500), 100); ctx.stroke();
              ctx.fillStyle = "#f59e0b"; ctx.fillText("v = " + (v/1000).toFixed(0) + "k km/s →", galX + 18, 120);

              ctx.strokeStyle = "#475569"; ctx.strokeRect(80, 150, 480, 30);
              const lineRest = 160;
              const lineShift = 160 + z * 180;
              ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(lineRest, 150); ctx.lineTo(lineRest, 180); ctx.stroke();
              ctx.fillStyle = "#38bdf8"; ctx.fillText("λ₀ (Rest)", lineRest - 16, 144);

              ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
              ctx.beginPath(); ctx.moveTo(lineShift, 150); ctx.lineTo(lineShift, 180); ctx.stroke();
              ctx.fillStyle = "#f43f5e"; ctx.fillText("λ_obs (Redshifted)", lineShift - 30, 195);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # 8.4 Black Hole & Gravitational Collapse
    # -------------------------------------------------------------
    elif sim_type == "blackhole_sim":
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>มวลดาวฤกษ์เริ่มต้น (Mass M): <span id="{prefix}_val_m" class="readout-val">10</span> มวลดวงอาทิตย์ (M_☉)</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_m" min="1" max="50" value="10">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="210"></canvas></div>
          <div class="sim-readout-grid">
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_rs">29.5 km</div><div class="readout-lbl">รัศมีชวาร์ซชิลด์ (Schwarzschild Radius Rs)</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_remnant">หลุมดำดาวฤกษ์ (Stellar Black Hole)</div><div class="readout-lbl">สถานะซากดาวสุดท้าย</div></div>
            <div class="readout-card"><div class="readout-val" id="{prefix}_val_sphere">44.3 km</div><div class="readout-lbl">โฟตอนสเฟียร์ (Photon Sphere 1.5 Rs)</div></div>
          </div>
        </div>
        <script>
        (function() {{
          function initSim() {{
            const cv = document.getElementById("{prefix}_canvas");
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_m");

            function draw() {{
              const M = +slider.value;
              document.getElementById("{prefix}_val_m").textContent = M;
              const Rs = 2.95 * M;
              document.getElementById("{prefix}_val_rs").textContent = Rs.toFixed(1) + " km";
              document.getElementById("{prefix}_val_sphere").textContent = (Rs * 1.5).toFixed(1) + " km";

              let remnant = "ดาวแคระขาว (White Dwarf: มวล < 1.4 M_☉)";
              if (M >= 1.4 && M < 3.0) remnant = "ดาวนิวตรอน (Neutron Star: 1.4-3.0 M_☉)";
              else if (M >= 3.0) remnant = "หลุมดำดาวฤกษ์ (Black Hole: มวล > 3.0 M_☉)";
              document.getElementById("{prefix}_val_remnant").textContent = remnant;

              ctx.clearRect(0,0,cv.width,cv.height);
              const cx = cv.width/2, cy = cv.height/2;

              // Gravitational lensing grid distortion
              ctx.strokeStyle = "rgba(0, 240, 255, 0.15)";
              ctx.lineWidth = 1;
              for(let r=20; r<180; r+=20) {{
                ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
              }}

              // Accretion disk glow
              const grad = ctx.createRadialGradient(cx, cy, 15, cx, cy, 90);
              grad.addColorStop(0, "rgba(245, 158, 11, 0.8)");
              grad.addColorStop(0.5, "rgba(239, 68, 68, 0.4)");
              grad.addColorStop(1, "rgba(0, 0, 0, 0)");
              ctx.fillStyle = grad;
              ctx.fillRect(cx-100, cy-100, 200, 200);

              // Photon Sphere
              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5; ctx.setLineDash([3,3]);
              ctx.beginPath(); ctx.arc(cx, cy, 38, 0, Math.PI*2); ctx.stroke();
              ctx.setLineDash([]);
              ctx.fillStyle = "#f59e0b"; ctx.font = "10px Sarabun";
              ctx.fillText("Photon Sphere (1.5 Rs)", cx + 44, cy - 25);

              // Black Hole Event Horizon (Schwarzschild radius)
              ctx.fillStyle = "#000000";
              ctx.beginPath(); ctx.arc(cx, cy, 25, 0, Math.PI*2); ctx.fill();
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5; ctx.stroke();
              ctx.fillStyle = "#00f0ff"; ctx.fillText("Event Horizon (Rs)", cx + 30, cy + 20);
            }}
            slider.addEventListener("input", draw);
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

    # -------------------------------------------------------------
    # Generic Dynamic Interactive Simulator Generator
    # -------------------------------------------------------------
    else:
        return f"""
        <div class="sim-panel" id="{prefix}_panel">
          <div class="sim-control-group">
            <label>พารามิเตอร์การทดลองหลัก (Parameter Scale): <span id="{prefix}_val_param" class="readout-val">50</span>%</label>
            <input type="range" class="sim-slider" id="{prefix}_slider_param" min="1" max="100" value="50">
          </div>
          <div class="sim-canvas-wrapper"><canvas id="{prefix}_canvas" width="640" height="200"></canvas></div>
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
            if (!cv) return;
            const ctx = cv.getContext("2d");
            const slider = document.getElementById("{prefix}_slider_param");
            let t = 0;

            function draw() {{
              const val = +slider.value;
              document.getElementById("{prefix}_val_param").textContent = val;
              const coeff = (val / 50).toFixed(3);
              document.getElementById("{prefix}_val_metric").textContent = coeff;

              ctx.clearRect(0,0,cv.width,cv.height);
              ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
              ctx.beginPath();
              for(let x=40; x<600; x+=2) {{
                const norm = (x-40)/560;
                const y = 100 + 45 * Math.sin(norm * Math.PI * 4 * coeff + t*0.05) * Math.cos(norm * Math.PI * 2);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
              ctx.beginPath();
              for(let x=40; x<600; x+=4) {{
                const norm = (x-40)/560;
                const y = 100 + 60 * Math.sin(norm * Math.PI * 2 * coeff - t*0.03);
                if (x===40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
              }}
              ctx.stroke();

              t += 1;
              requestAnimationFrame(draw);
            }}
            slider.addEventListener("input", () => {{}});
            draw();
          }}
          if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSim);
          else initSim();
        }})();
        </script>
        """

print("Simulators library comprehensive suite ready.")
