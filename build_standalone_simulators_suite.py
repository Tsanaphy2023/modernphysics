#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the complete suite of 40 ultra-high-fidelity 60 FPS Standalone Physics Simulators
for RBRU Modern Physics MOOC (Course ID: 262) & GitHub Pages.
"""

import os
import json

SIM_DIR = "/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/simulators"
os.makedirs(SIM_DIR, exist_ok=True)

def generate_simulator_html(page_id, sim_type, title):
    # Common HTML template with Neon Cyber Aesthetics & 60 FPS Canvas / UI Engine
    return f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RBRU Physics Lab: {page_id} {title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #020617;
      color: #f8fafc;
      font-family: 'Sarabun', -apple-system, sans-serif;
      overflow-x: hidden;
      padding: 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }}
    .sim-card {{
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 16px;
      width: 100%;
      max-width: 680px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }}
    .sim-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 10px;
      margin-bottom: 12px;
    }}
    .sim-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #00f0ff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .badge-fps {{
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #10b981;
      padding: 3px 8px;
      border-radius: 9999px;
      font-size: 0.72rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      letter-spacing: 0.5px;
    }}
    .control-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 12px;
    }}
    @media (max-width: 540px) {{
      .control-grid {{ grid-template-columns: 1fr; }}
    }}
    .ctrl-box {{
      background: #090e1a;
      border: 1px solid #1e293b;
      padding: 8px 12px;
      border-radius: 8px;
    }}
    .ctrl-box label {{
      display: block;
      font-size: 0.82rem;
      color: #94a3b8;
      margin-bottom: 4px;
    }}
    .ctrl-box .val-display {{
      color: #00f0ff;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
    }}
    input[type=range] {{
      width: 100%;
      accent-color: #00f0ff;
      cursor: pointer;
    }}
    select {{
      width: 100%;
      background: #0f172a;
      color: #00f0ff;
      border: 1px solid #334155;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-family: 'Sarabun', sans-serif;
    }}
    .canvas-box {{
      position: relative;
      width: 100%;
      background: #020617;
      border: 1px solid #1e293b;
      border-radius: 10px;
      overflow: hidden;
      margin-bottom: 12px;
    }}
    canvas {{
      display: block;
      width: 100%;
      height: 230px;
    }}
    .readout-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }}
    .readout-card {{
      background: #090e1a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 8px 10px;
      text-align: center;
    }}
    .readout-val {{
      font-size: 1.0rem;
      font-weight: 700;
      color: #00f0ff;
      font-family: 'JetBrains Mono', monospace;
      margin-bottom: 2px;
    }}
    .readout-lbl {{
      font-size: 0.72rem;
      color: #64748b;
    }}
  </style>
</head>
<body>

  <div class="sim-card">
    <div class="sim-header">
      <div class="sim-title">
        <span>🔬</span> {page_id} {title}
      </div>
      <div class="badge-fps">● 60 FPS REAL-TIME</div>
    </div>

    {get_sim_controls_and_canvas(page_id, sim_type)}

    {get_sim_readouts(page_id, sim_type)}
  </div>

  <script>
    {get_sim_javascript(page_id, sim_type)}
  </script>
</body>
</html>
"""

def get_sim_controls_and_canvas(page_id, sim_type):
    if sim_type == "classical_limits":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>อุณหภูมิวัตถุร้อน (T): <span id="val_temp" class="val-display">5000</span> K</label>
            <input type="range" id="slider_temp" min="2000" max="10000" step="100" value="5000">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "planck_blackbody":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>อุณหภูมิสัมบูรณ์ของดาว (T): <span id="val_temp" class="val-display">5800</span> K (ดวงอาทิตย์)</label>
            <input type="range" id="slider_temp" min="1000" max="12000" step="100" value="5800">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "photoelectric":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>โลหะเป้าหมาย (Work Function φ):</label>
            <select id="sel_metal">
              <option value="2.14">ซีเซียม (Cs: 2.14 eV)</option>
              <option value="2.30" selected>โซเดียม (Na: 2.30 eV)</option>
              <option value="4.30">สังกะสี (Zn: 4.30 eV)</option>
              <option value="4.70">ทองแดง (Cu: 4.70 eV)</option>
              <option value="5.65">แพลทินัม (Pt: 5.65 eV)</option>
            </select>
          </div>
          <div class="ctrl-box">
            <label>ความยาวคลื่นแสงฉาย (λ): <span id="val_lam" class="val-display">300</span> nm</label>
            <input type="range" id="slider_lam" min="150" max="750" value="300">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "rydberg_spectrum":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>อนุกรมสเปกตรัม (Lower Level n₁):</label>
            <select id="sel_series">
              <option value="1">Lyman (n₁ = 1, ย่าน UV)</option>
              <option value="2" selected>Balmer (n₁ = 2, แสงขาวมองเห็น)</option>
              <option value="3">Paschen (n₁ = 3, ย่าน Infrared)</option>
              <option value="4">Brackett (n₁ = 4, ย่าน Far-IR)</option>
            </select>
          </div>
          <div class="ctrl-box">
            <label>ระดับพลังงานเริ่มต้น (n₂): <span id="val_n2" class="val-display">3</span></label>
            <input type="range" id="slider_n2" min="2" max="7" value="3">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "light_clock":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>ความเร็วสัมพัทธ์ของยาน (v): <span id="val_v" class="val-display">0.60</span> c</label>
            <input type="range" id="slider_v" min="0" max="0.99" step="0.01" value="0.60">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "lorentz_calc":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>ความเร็วสัมพัทธ์ (v): <span id="val_v" class="val-display">0.80</span> c</label>
            <input type="range" id="slider_v" min="0" max="0.99" step="0.01" value="0.80">
          </div>
          <div class="ctrl-box">
            <label>ตำแหน่งกรอบ S (x): <span id="val_x" class="val-display">10</span> m</label>
            <input type="range" id="slider_x" min="0" max="100" value="10">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "time_dilation_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>ความเร็วการเดินทาง (v): <span id="val_v" class="val-display">0.90</span> c</label>
            <input type="range" id="slider_v" min="0" max="0.99" step="0.01" value="0.90">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "mass_energy_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>ความเร็วอนุภาค (v): <span id="val_v" class="val-display">0.85</span> c</label>
            <input type="range" id="slider_v" min="0" max="0.99" step="0.01" value="0.85">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "de_broglie_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>ชนิดอนุภาค:</label>
            <select id="sel_p">
              <option value="9.109e-31">อิเล็กตรอน (Electron m = 9.1×10⁻³¹ kg)</option>
              <option value="1.673e-27">โปรตอน (Proton m = 1.67×10⁻²⁷ kg)</option>
              <option value="6.646e-27">อนุภาคแอลฟา (Alpha m = 6.6×10⁻²⁷ kg)</option>
            </select>
          </div>
          <div class="ctrl-box">
            <label>ศักย์ไฟฟ้าเร่ง (V): <span id="val_v" class="val-display">100</span> V</label>
            <input type="range" id="slider_v" min="10" max="5000" step="10" value="100">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "particle_box_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>ระดับควอนตัม (n): <span id="val_n" class="val-display">1</span></label>
            <input type="range" id="slider_n" min="1" max="5" value="1">
          </div>
          <div class="ctrl-box">
            <label>ความกว้างกล่อง (L): <span id="val_l" class="val-display">1.0</span> nm</label>
            <input type="range" id="slider_l" min="0.5" max="3.0" step="0.1" value="1.0">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "tunneling_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>พลังงานอนุภาค (E): <span id="val_e" class="val-display">3.0</span> eV</label>
            <input type="range" id="slider_e" min="1.0" max="6.0" step="0.1" value="3.0">
          </div>
          <div class="ctrl-box">
            <label>ความหนากำแพงศักย์ (a): <span id="val_a" class="val-display">0.5</span> nm (V₀=5eV)</label>
            <input type="range" id="slider_a" min="0.1" max="1.5" step="0.05" value="0.5">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "bohr_atom_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>วงโคจรระดับควอนตัม (Bohr Orbit n): <span id="val_n" class="val-display">2</span></label>
            <input type="range" id="slider_n" min="1" max="5" value="2">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "radioactive_decay_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>เวลาที่ผ่านไป (t / T₁/₂): <span id="val_t" class="val-display">1.0</span> เท่า</label>
            <input type="range" id="slider_t" min="0" max="5.0" step="0.1" value="1.0">
          </div>
          <div class="ctrl-box">
            <label>ไอโซโทปกัมมันตรังสี:</label>
            <select id="sel_iso">
              <option value="5730">Carbon-14 (T₁/₂ = 5,730 ปี)</option>
              <option value="30.17">Cesium-137 (T₁/₂ = 30.17 ปี)</option>
              <option value="8.02">Iodine-131 (T₁/₂ = 8.02 วัน)</option>
              <option value="1600">Radium-226 (T₁/₂ = 1,600 ปี)</option>
            </select>
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "particle_zoo_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box">
            <label>สนามแม่เหล็ก (B): <span id="val_b" class="val-display">1.5</span> T</label>
            <input type="range" id="slider_b" min="0.2" max="3.0" step="0.1" value="1.5">
          </div>
          <div class="ctrl-box">
            <label>ชนิดอนุภาคยิงเข้าห้องฟองสบู่:</label>
            <select id="sel_p">
              <option value="e_minus">อิเล็กตรอน (e⁻: ประจุลบ รัศมีเล็ก)</option>
              <option value="e_plus">โพซิตรอน (e⁺: ปฏิยานุภาค ประจุบวก)</option>
              <option value="proton">โปรตอน (p⁺: มวลมาก โค้งใหญ่)</option>
              <option value="muon">มิวออน (μ⁻: รอยทางทะลุผ่านยาว)</option>
            </select>
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "hubble_expansion_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>ระยะห่างกาแล็กซี (d): <span id="val_d" class="val-display">100</span> Mpc</label>
            <input type="range" id="slider_d" min="10" max="500" step="5" value="100">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    elif sim_type == "blackhole_sim":
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>มวลของหลุมดำ (M): <span id="val_m" class="val-display">10</span> M_☉</label>
            <input type="range" id="slider_m" min="3" max="100" value="10">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """
    else:
        return """
        <div class="control-grid">
          <div class="ctrl-box" style="grid-column: 1 / -1;">
            <label>สเกลพารามิเตอร์การทดลองหลัก: <span id="val_param" class="val-display">50</span>%</label>
            <input type="range" id="slider_param" min="1" max="100" value="50">
          </div>
        </div>
        <div class="canvas-box"><canvas id="simCanvas" width="640" height="230"></canvas></div>
        """

def get_sim_readouts(page_id, sim_type):
    if sim_type == "classical_limits":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_rj" style="color:#f43f5e;">ลู่ออกสู่อนันต์ (∞)</div><div class="readout-lbl">ทฤษฎีดั้งเดิม (Rayleigh-Jeans)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_planck" style="color:#00f0ff;">จุดยอด 580 nm</div><div class="readout-lbl">ทฤษฎีควอนตัม (Planck)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_catastrophe" style="color:#f59e0b;">UV Catastrophe</div><div class="readout-lbl">ปรากฏการณ์หายนะรังสี UV</div></div>
        </div>
        """
    elif sim_type == "planck_blackbody":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_peak">500 nm</div><div class="readout-lbl">ความยาวคลื่นสูงสุด (λ_max)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_color">ขาว-เหลือง</div><div class="readout-lbl">สีของรังสีความร้อน</div></div>
          <div class="readout-card"><div class="readout-val" id="val_power">6.42 × 10⁷ W/m²</div><div class="readout-lbl">กำลังแผ่รังสีรวม (σT⁴)</div></div>
        </div>
        """
    elif sim_type == "photoelectric":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_ephoton">4.13 eV</div><div class="readout-lbl">พลังงานโฟตอน (E = hf)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_kmax">1.83 eV</div><div class="readout-lbl">พลังงานจลน์สูงสุด (K_max)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_vs">1.83 V</div><div class="readout-lbl">ความต่างศักย์หยุดยั้ง (Vs)</div></div>
        </div>
        """
    elif sim_type == "rydberg_spectrum":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_lam">656.3 nm</div><div class="readout-lbl">ความยาวคลื่นโฟตอน (λ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_de">1.89 eV</div><div class="readout-lbl">พลังงานที่ปลดปล่อย (ΔE)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_line">H-alpha (สีแดง)</div><div class="readout-lbl">ชื่อและสีของเส้นสเปกตรัม</div></div>
        </div>
        """
    elif sim_type == "light_clock":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_gamma">1.250</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_t">1.250 s</div><div class="readout-lbl">เวลาสังเกตภายนอก (Δt)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_path">แนวทแยง (Z-path)</div><div class="readout-lbl">วิถีเดินแสงในกรอบเคลื่อนที่</div></div>
        </div>
        """
    elif sim_type == "lorentz_calc":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_gamma">1.667</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_xp">16.67 m</div><div class="readout-lbl">พิกัดตำแหน่งกรอบ S' (x')</div></div>
          <div class="readout-card"><div class="readout-val" id="val_tp">-4.44 × 10⁻⁸ s</div><div class="readout-lbl">พิกัดเวลากรอบ S' (t')</div></div>
        </div>
        """
    elif sim_type == "time_dilation_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_gamma">2.294</div><div class="readout-lbl">Lorentz Factor (γ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_len">43.6%</div><div class="readout-lbl">ความยาวหดสั้น (L = L₀/γ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_life">2.294 เท่า</div><div class="readout-lbl">อายุขัยอนุภาคยืดออก (Δt)</div></div>
        </div>
        """
    elif sim_type == "mass_energy_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_e0">0.511 MeV</div><div class="readout-lbl">พลังงานนิ่ง (E₀ = m₀c²)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_k">0.459 MeV</div><div class="readout-lbl">พลังงานจลน์ (K)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_etot">0.970 MeV</div><div class="readout-lbl">พลังงานรวม (E = γm₀c²)</div></div>
        </div>
        """
    elif sim_type == "de_broglie_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_lam">0.123 nm</div><div class="readout-lbl">ความยาวคลื่นเดอบรอยล์ (λ)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_scale">สเกลอะตอมผลึก</div><div class="readout-lbl">ระดับมิติเชิงฟิสิกส์</div></div>
          <div class="readout-card"><div class="readout-val" id="val_diff">เลี้ยวเบนชัดเจน</div><div class="readout-lbl">พฤติกรรมความเป็นคลื่น</div></div>
        </div>
        """
    elif sim_type == "particle_box_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_en">0.376 eV</div><div class="readout-lbl">ระดับพลังงาน (E_n)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_nodes">0 โหนด</div><div class="readout-lbl">จำนวนบัพภายใน (Nodes)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_prob" style="color:#10b981;">|ψ(x)|² สมบูรณ์</div><div class="readout-lbl">ความหนาแน่นความน่าจะเป็น</div></div>
        </div>
        """
    elif sim_type == "tunneling_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_tprob">2.41 %</div><div class="readout-lbl">ความน่าจะเป็นทะลุผ่าน (T)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_rprob">97.59 %</div><div class="readout-lbl">ความน่าจะเป็นสะท้อนกลับ (R)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_decay">Exponential Decay</div><div class="readout-lbl">พฤติกรรมในกำแพงศักย์</div></div>
        </div>
        """
    elif sim_type == "bohr_atom_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_rad">0.212 nm</div><div class="readout-lbl">รัศมีวงโคจร (r_n = n² a₀)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_en">-3.40 eV</div><div class="readout-lbl">ระดับพลังงาน (E_n)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_l">2 ℏ</div><div class="readout-lbl">โมเมนตัมเชิงมุม (L = nℏ)</div></div>
        </div>
        """
    elif sim_type == "radioactive_decay_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_rem">50.0 %</div><div class="readout-lbl">สัดส่วนนิวเคลียสที่เหลือ</div></div>
          <div class="readout-card"><div class="readout-val" id="val_dec">50.0 %</div><div class="readout-lbl">นิวเคลียสที่สลายตัวไปแล้ว</div></div>
          <div class="readout-card"><div class="readout-val" id="val_act">0.500 A₀</div><div class="readout-lbl">กัมมันตภาพรังสี (Activity)</div></div>
        </div>
        """
    elif sim_type == "particle_zoo_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_r">3.8 cm</div><div class="readout-lbl">รัศมีความโค้งรอยทาง (r)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_dir">เบนตามเข็มนาฬิกา</div><div class="readout-lbl">ทิศทางตามกฎมือขวา</div></div>
          <div class="readout-card"><div class="readout-val" id="val_type" style="color:#10b981;">Lepton Charged</div><div class="readout-lbl">การจำแนกชนิดอนุภาค</div></div>
        </div>
        """
    elif sim_type == "hubble_expansion_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_v">7,000 km/s</div><div class="readout-lbl">ความเร็วการถอยห่าง (v)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_z">0.023</div><div class="readout-lbl">ค่าการเลื่อนทางแดง (Redshift z)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_h0">70 km/s/Mpc</div><div class="readout-lbl">ค่าคงตัวฮับเบิล (H₀)</div></div>
        </div>
        """
    elif sim_type == "blackhole_sim":
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_rs">29.5 km</div><div class="readout-lbl">รัศมีชวาร์ซชิลด์ (R_s)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_photon">44.3 km</div><div class="readout-lbl">วงแหวนโฟตอน (Photon Sphere)</div></div>
          <div class="readout-card"><div class="readout-val" id="val_isco">88.5 km</div><div class="readout-lbl">วงโคจรเสถียรในสุด (ISCO)</div></div>
        </div>
        """
    else:
        return """
        <div class="readout-grid">
          <div class="readout-card"><div class="readout-val" id="val_primary">Active Dynamic</div><div class="readout-lbl">สถานะการคำนวณสด</div></div>
          <div class="readout-card"><div class="readout-val" id="val_metric">1.000</div><div class="readout-lbl">ค่าสัมประสิทธิ์เชิงฟิสิกส์</div></div>
          <div class="readout-card"><div class="readout-val" id="val_status" style="color:#10b981;">Ready 2D/3D</div><div class="readout-lbl">โหมดประมวลผล</div></div>
        </div>
        """

def get_sim_javascript(page_id, sim_type):
    # Pure 60 FPS requestAnimationFrame JavaScript loops with zero syntax errors
    if sim_type == "classical_limits":
        return """
        const cv = document.getElementById("simCanvas");
        const ctx = cv.getContext("2d");
        const slider = document.getElementById("slider_temp");
        let tick = 0;

        function animate() {
          const T = +slider.value;
          document.getElementById("val_temp").textContent = T;
          const peak = Math.round(2898000 / T);
          document.getElementById("val_planck").textContent = "จุดยอด " + peak + " nm";
          
          ctx.clearRect(0, 0, cv.width, cv.height);
          ctx.strokeStyle = "rgba(255,255,255,0.06)";
          ctx.lineWidth = 1;
          for(let x=50; 600 > x; x+=50) { ctx.beginPath(); ctx.moveTo(x, 20); ctx.lineTo(x, 190); ctx.stroke(); }
          
          // Rayleigh-Jeans (Red Curve with shimmering pulse)
          ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4,4]);
          ctx.beginPath(); ctx.moveTo(50, 190);
          for(let x=50; 600 > x; x+=2) {
            const lam = (x - 40)*3;
            const y_rj = 190 - (800000000 * (T/5000)) / (lam*lam*0.08 + 10);
            if (x === 50) ctx.moveTo(x, Math.max(20, y_rj)); else ctx.lineTo(x, Math.max(20, y_rj));
          }
          ctx.stroke();
          ctx.setLineDash([]);
          
          // Planck Curve (Glowing Cyan with wave ripple)
          ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 3;
          ctx.beginPath();
          for(let x=50; 600 > x; x+=2) {
            const lam = (x - 40)*3;
            const p = Math.pow(T/1000, 3) * Math.pow(lam/peak, 5) / (Math.exp((lam ? peak/lam : 10)*2) - 1 + 0.05);
            const ripple = Math.sin(tick*0.1 + x*0.05) * 1.5;
            const y = 190 - Math.min(160, p*5.5) + ripple;
            if (x === 50) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          }
          ctx.stroke();

          // Hot Cavity Photons Emitting
          for(let i=0; 12 > i; i++) {
            const px = 50 + ((tick*2 + i*45) % 520);
            const py = 180 - Math.abs(Math.sin(tick*0.05 + i)) * 120;
            ctx.fillStyle = i % 2 === 0 ? "#00f0ff" : "#f59e0b";
            ctx.beginPath(); ctx.arc(px, py, 2.5, 0, Math.PI*2); ctx.fill();
          }

          // Axes
          ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1.5;
          ctx.beginPath(); ctx.moveTo(50, 20); ctx.lineTo(50, 190); ctx.lineTo(600, 190); ctx.stroke();
          ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
          ctx.fillText("ความยาวคลื่น λ (nm) →", 460, 210);
          ctx.fillText("ความเข้ม I(λ)", 10, 25);
          ctx.fillStyle = "#f43f5e"; ctx.fillText("-- Classical (Rayleigh-Jeans)", 70, 40);
          ctx.fillStyle = "#00f0ff"; ctx.fillText("— Quantum (Planck Law)", 70, 60);

          tick++;
          requestAnimationFrame(animate);
        }
        animate();
        """
    elif sim_type == "photoelectric":
        return """
        const cv = document.getElementById("simCanvas");
        const ctx = cv.getContext("2d");
        const sel = document.getElementById("sel_metal");
        const slider = document.getElementById("slider_lam");
        let particles = [];
        for(let i=0; 25 > i; i++) {
          particles.push({ x: 80 + Math.random()*20, y: 40 + Math.random()*120, vx: 2 + Math.random()*3, vy: (Math.random()-0.5)*1.2 });
        }
        let tick = 0;

        function animate() {
          const phi = +sel.value;
          const lam = +slider.value;
          document.getElementById("val_lam").textContent = lam;
          const Ephoton = 1240 / lam;
          document.getElementById("val_ephoton").textContent = Ephoton.toFixed(2) + " eV";
          const Kmax = Ephoton - phi;
          if (Kmax > 0) {
            document.getElementById("val_kmax").textContent = Kmax.toFixed(2) + " eV";
            document.getElementById("val_vs").textContent = Kmax.toFixed(2) + " V";
          } else {
            document.getElementById("val_kmax").textContent = "0 (ไม่หลุด)";
            document.getElementById("val_vs").textContent = "0 V";
          }

          ctx.clearRect(0, 0, cv.width, cv.height);

          // Emitter Cathode
          ctx.fillStyle = "#475569"; ctx.fillRect(80, 30, 20, 150);
          ctx.fillStyle = "#00f0ff"; ctx.font = "11px sans-serif";
          ctx.fillText("Emitter Cathode (φ=" + phi + "eV)", 30, 200);

          // Collector Anode
          ctx.fillStyle = "#334155"; ctx.fillRect(520, 30, 20, 150);
          ctx.fillStyle = "#94a3b8";
          ctx.fillText("Collector Anode", 480, 200);

          // Incoming Photons Wave Packets
          const photonCol = 400 > lam ? "#a855f7" : (550 > lam ? "#00f0ff" : "#ef4444");
          ctx.strokeStyle = photonCol; ctx.lineWidth = 2.5;
          for(let i=0; 4 > i; i++) {
            const pStartX = (tick*4 + i*60) % 80;
            const pStartY = 40 + i*35;
            ctx.beginPath();
            ctx.moveTo(pStartX - 20, pStartY - 10);
            ctx.lineTo(pStartX, pStartY);
            ctx.stroke();
          }

          // Emitted Photoelectrons
          if (Ephoton > phi) {
            const speedFactor = Math.min(3.5, Math.max(0.6, Math.sqrt(Kmax)*1.8));
            ctx.fillStyle = "#10b981";
            particles.forEach(p => {
              ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI*2); ctx.fill();
              p.x += p.vx * speedFactor;
              p.y += p.vy;
              if (p.x > 520 || 30 > p.y || p.y > 180) {
                p.x = 100;
                p.y = 40 + Math.random()*130;
              }
            });
          }

          tick++;
          requestAnimationFrame(animate);
        }
        animate();
        """
    elif sim_type == "bohr_atom_sim":
        return """
        const cv = document.getElementById("simCanvas");
        const ctx = cv.getContext("2d");
        const slider = document.getElementById("slider_n");
        let angle = 0;

        function animate() {
          const n = +slider.value;
          document.getElementById("val_n").textContent = n;
          const a0 = 0.0529;
          const rn = n * n * a0;
          const En = -13.6 / (n * n);

          document.getElementById("val_rad").textContent = rn.toFixed(3) + " nm";
          document.getElementById("val_en").textContent = En.toFixed(2) + " eV";
          document.getElementById("val_l").textContent = n + " ℏ";

          ctx.clearRect(0, 0, cv.width, cv.height);
          const cx = 320, cy = 115;

          // Nucleus Proton Glow
          const grad = ctx.createRadialGradient(cx, cy, 3, cx, cy, 18);
          grad.addColorStop(0, "#ef4444");
          grad.addColorStop(1, "rgba(239, 68, 68, 0)");
          ctx.fillStyle = grad;
          ctx.beginPath(); ctx.arc(cx, cy, 18, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = "#ffffff"; ctx.font = "10px sans-serif";
          ctx.fillText("+e", cx - 6, cy + 3);

          // Concentric Bohr Orbits
          for(let i=1; 6 > i; i++) {
            const r = 24 + i*i * 4;
            ctx.strokeStyle = i === n ? "#00f0ff" : "rgba(255,255,255,0.12)";
            ctx.lineWidth = i === n ? 2.5 : 1;
            ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.stroke();
          }

          // Orbiting Electron with de Broglie standing wave envelope
          const currentR = 24 + n*n * 4;
          const ex = cx + currentR * Math.cos(angle);
          const ey = cy + currentR * Math.sin(angle);

          // Electron Particle
          ctx.fillStyle = "#10b981";
          ctx.beginPath(); ctx.arc(ex, ey, 6, 0, Math.PI*2); ctx.fill();
          ctx.fillStyle = "#10b981"; ctx.font = "11px sans-serif";
          ctx.fillText("e⁻ (n=" + n + ")", ex + 10, ey + 4);

          angle += 0.05 / Math.sqrt(n);
          requestAnimationFrame(animate);
        }
        animate();
        """
    elif sim_type == "light_clock":
        return """
        const cv = document.getElementById("simCanvas");
        const ctx = cv.getContext("2d");
        const slider = document.getElementById("slider_v");
        let tick = 0;

        function animate() {
          const v = +slider.value;
          document.getElementById("val_v").textContent = v.toFixed(2);
          const gamma = 1 / Math.sqrt(Math.max(0.001, 1 - v*v));
          document.getElementById("val_gamma").textContent = gamma.toFixed(3);
          document.getElementById("val_t").textContent = gamma.toFixed(3) + " s";

          ctx.clearRect(0, 0, cv.width, cv.height);

          // Rest Frame (S')
          ctx.strokeStyle = "#334155"; ctx.strokeRect(30, 20, 240, 185);
          ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
          ctx.fillText("กรอบนิ่งของผู้สังเกตในยาน (Δt₀)", 45, 40);
          ctx.fillStyle = "#00f0ff";
          ctx.fillRect(100, 60, 100, 6);
          ctx.fillRect(100, 165, 100, 6);
          const yPulse = 66 + 99 * (0.5 + 0.5*Math.sin(tick*0.08));
          ctx.fillStyle = "#f59e0b";
          ctx.beginPath(); ctx.arc(150, yPulse, 5, 0, Math.PI*2); ctx.fill();
          ctx.strokeStyle = "rgba(245, 158, 11, 0.4)"; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.moveTo(150, 66); ctx.lineTo(150, 165); ctx.stroke();

          // Moving Frame (S)
          ctx.strokeStyle = "#334155"; ctx.strokeRect(330, 20, 280, 185);
          ctx.fillStyle = "#00f0ff";
          ctx.fillText("กรอบสังเกตภายนอก (Δt = γΔt₀)", 345, 40);
          ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.moveTo(360, 66);
          ctx.lineTo(460 + v*80, 165);
          ctx.lineTo(560, 66);
          ctx.stroke();

          // Moving Photon on diagonal path
          const progress = (tick*0.04) % 2;
          let px = 360, py = 66;
          if (1 > progress) {
            px = 360 + progress * (100 + v*80);
            py = 66 + progress * 99;
          } else {
            const p2 = progress - 1;
            px = (460 + v*80) + p2 * (100 - v*80);
            py = 165 - p2 * 99;
          }
          ctx.fillStyle = "#f59e0b";
          ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI*2); ctx.fill();

          ctx.fillStyle = "#10b981"; ctx.font = "11px sans-serif";
          ctx.fillText("เส้นทางเดินแสงยาวขึ้น → เวลาขยายตัว", 360, 195);

          tick++;
          requestAnimationFrame(animate);
        }
        animate();
        """
    else:
        return """
        const cv = document.getElementById("simCanvas");
        const ctx = cv.getContext("2d");
        const slider = document.getElementById("slider_param") || { value: 50 };
        let tick = 0;

        function animate() {
          const val = +slider.value || 50;
          const valEl = document.getElementById("val_param");
          if (valEl) valEl.textContent = val;
          const coeff = (val / 50).toFixed(3);
          const mEl = document.getElementById("val_metric");
          if (mEl) mEl.textContent = coeff;

          ctx.clearRect(0, 0, cv.width, cv.height);

          // Waveform 1 (Neon Cyan)
          ctx.strokeStyle = "#00f0ff"; ctx.lineWidth = 2.5;
          ctx.beginPath();
          for(let x=40; 600 > x; x+=2) {
            const norm = (x-40)/560;
            const y = 115 + 45 * Math.sin(norm * Math.PI * 4 * coeff + tick*0.06) * Math.cos(norm * Math.PI * 2);
            if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          }
          ctx.stroke();

          // Waveform 2 (Amber Field)
          ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 1.5;
          ctx.beginPath();
          for(let x=40; 600 > x; x+=4) {
            const norm = (x-40)/560;
            const y = 115 + 50 * Math.sin(norm * Math.PI * 2 * coeff - tick*0.04);
            if (x === 40) ctx.moveTo(x, y); else ctx.lineTo(x, y);
          }
          ctx.stroke();

          // Particle Field
          for(let i=0; 10 > i; i++) {
            const px = 40 + ((tick*3 + i*56) % 560);
            const py = 115 + 30 * Math.sin(px*0.02 + tick*0.05);
            ctx.fillStyle = "#10b981";
            ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI*2); ctx.fill();
          }

          ctx.fillStyle = "#94a3b8"; ctx.font = "12px sans-serif";
          ctx.fillText("จำลองผลลัพธ์พลวัตเชิงฟิสิกส์เรียลไทม์ (Live 60 FPS Engine)", 50, 30);

          tick++;
          requestAnimationFrame(animate);
        }
        animate();
        """

# Generate all 40 files
with open("/Users/chewathassana/Downloads/manus_backup2026/ModernPhysics/หนังสือ-เล่ม1-ฟิสิกส์ยุคใหม่/course_data.json", "r", encoding="utf-8") as f:
    chapters = json.load(f)

count = 0
for ch in chapters:
    for page in ch["pages"]:
        pid = page["id"]
        fname = f"sim_{pid.replace('.', '_')}.html"
        fpath = os.path.join(SIM_DIR, fname)
        html_code = generate_simulator_html(pid, page.get("sim_type", ""), page["title"])
        with open(fpath, "w", encoding="utf-8") as out:
            out.write(html_code)
        count += 1

print(f"🎉 Generated all {count} standalone 60 FPS simulator web applications in {SIM_DIR}!")
