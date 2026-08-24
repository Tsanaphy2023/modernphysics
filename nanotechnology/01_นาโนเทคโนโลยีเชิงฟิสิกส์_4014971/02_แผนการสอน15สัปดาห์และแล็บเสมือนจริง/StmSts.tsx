/**
 * Precision Instrument Console — STM/STS workbench: navy observation stage, ivory analysis panels,
 * and phosphor-lime reserved for active measurement and selected evidence.
 * All outputs are conceptual/semi-empirical teaching proxies, not experimental spectra or DFT.
 */
import { Link } from "wouter";
import { type MouseEvent, useMemo, useState } from "react";
import {
  ArrowLeft,
  Atom,
  CircleGauge,
  Crosshair,
  Lightbulb,
  Microscope,
  RotateCcw,
  ScanLine,
  Thermometer,
  Waves,
  Zap,
} from "lucide-react";
import { toast } from "sonner";
import "./StmSts.css";

type SampleId = "hopg" | "mos2" | "defect";
type SiteId = "terrace" | "site" | "defect";
type LinecutMode = "defect" | "interface";

type SamplePreset = {
  id: SampleId;
  label: string;
  tag: string;
  description: string;
  gap: number;
  workFunction: number;
  baseLdos: number;
  accent: string;
};

const heroImage = "/manus-storage/stm-sts-hero_89eba373.png";
const stageImage = "/manus-storage/stm-sts-stage_efb63148.png";

const samples: SamplePreset[] = [
  { id: "hopg", label: "HOPG-like", tag: "SEMIMETAL / REFERENCE", description: "finite LDOS around Eᶠ teaching preset", gap: 0.02, workFunction: 4.55, baseLdos: 0.78, accent: "#83c6dd" },
  { id: "mos2", label: "MoS₂-like", tag: "2D / GAPPED", description: "gapped 2D semiconductor teaching preset", gap: 1.58, workFunction: 4.8, baseLdos: 0.9, accent: "#c7f36b" },
  { id: "defect", label: "Defect-like", tag: "IN-GAP / LOCAL", description: "localized in-gap state teaching preset", gap: 1.58, workFunction: 4.7, baseLdos: 0.82, accent: "#e1ae76" },
];

const clamp = (value: number, minimum: number, maximum: number) => Math.min(maximum, Math.max(minimum, value));
const gaussian = (x: number, center: number, width: number, amplitude: number) => amplitude * Math.exp(-((x - center) ** 2) / (2 * width ** 2));
const logistic = (x: number, center: number, width: number) => 1 / (1 + Math.exp(-(x - center) / width));

function siteModifier(site: SiteId) {
  if (site === "site") return { ldos: 1.16, height: .35, label: "atomic site" };
  if (site === "defect") return { ldos: 1.38, height: -.26, label: "localized defect" };
  return { ldos: .9, height: 0, label: "terrace reference" };
}

function broadening(temperature: number) {
  return .025 + temperature * .00016;
}

function ldos(sample: SamplePreset, energy: number, temperature: number, site: SiteId) {
  const width = broadening(temperature);
  const local = siteModifier(site);
  if (sample.id === "hopg") {
    return clamp((.12 + .7 * Math.abs(energy) + gaussian(energy, .17, width * 1.7, .1)) * local.ldos, .015, 1.4);
  }
  const edge = sample.gap / 2;
  const bands = .045 + .72 * logistic(Math.abs(energy), edge, width * 1.7);
  const edgeResonance = gaussian(energy, edge + .12, width * 1.8, .19) + gaussian(energy, -edge - .12, width * 1.8, .14);
  const inGap = sample.id === "defect" || site === "defect" ? gaussian(energy, -.16, width * 1.35, .53) : 0;
  return clamp((bands + edgeResonance + inGap) * local.ldos, .01, 1.55);
}

function tunnellingModel(sample: SamplePreset, bias: number, distance: number, temperature: number, site: SiteId) {
  const local = siteModifier(site);
  const barrier = sample.workFunction - Math.min(.36, Math.abs(bias) * .15);
  const decayConstant = 1.025 * Math.sqrt(Math.max(barrier, 1));
  const ldosAtBias = ldos(sample, bias, temperature, site);
  const currentPa = 125 * (Math.abs(bias) / .55 + .11) * Math.exp(-1.72 * (distance - 5.4)) * (.62 + ldosAtBias) * local.ldos;
  const conductanceNs = clamp((currentPa / Math.max(Math.abs(bias), .045)) * .0048, .002, 4.8);
  const apparentHeight = local.height + Math.log(.62 + ldosAtBias) * .19;
  return { barrier, decayConstant, ldosAtBias, currentPa, conductanceNs, apparentHeight };
}

function StsSpectrum({ sample, temperature, site, bias }: { sample: SamplePreset; temperature: number; site: SiteId; bias: number }) {
  const points = Array.from({ length: 180 }, (_, index) => {
    const energy = -1.45 + (index / 179) * 2.9;
    const signal = ldos(sample, energy, temperature, site);
    return `${(7 + (index / 179) * 87).toFixed(2)},${(87 - signal * 46).toFixed(2)}`;
  }).join(" ");
  const marker = 7 + ((bias + 1.45) / 2.9) * 87;
  return <svg className="stm-chart" viewBox="0 0 100 100" role="img" aria-label="Conceptual dI dV tunneling spectrum"><path d="M7 87H94M7 10V87" className="stm-axis" /><path d="M50 10V87" className="stm-zero" /><polyline points={points} className="stm-spectrum-line" /><path d={`M${marker.toFixed(2)} 15V87`} className="stm-active-marker" /><text x="8" y="15">dI/dV</text><text x="78" y="97">eV</text><text x="48" y="94">Eᶠ</text></svg>;
}

function IZPlot({ sample, bias, temperature, site, distance }: { sample: SamplePreset; bias: number; temperature: number; site: SiteId; distance: number }) {
  const points = Array.from({ length: 125 }, (_, index) => {
    const z = 4.5 + (index / 124) * 4.1;
    const signal = tunnellingModel(sample, bias, z, temperature, site).currentPa;
    const logSignal = clamp(Math.log10(signal + .02), -1.7, 2.4);
    return `${(7 + (index / 124) * 87).toFixed(2)},${(84 - ((logSignal + 1.7) / 4.1) * 67).toFixed(2)}`;
  }).join(" ");
  const markerX = 7 + ((distance - 4.5) / 4.1) * 87;
  return <svg className="stm-chart" viewBox="0 0 100 100" role="img" aria-label="Conceptual tunneling current versus tip sample distance"><path d="M7 87H94M7 10V87" className="stm-axis" /><polyline points={points} className="stm-iz-line" /><path d={`M${markerX.toFixed(2)} 15V87`} className="stm-active-marker" /><text x="8" y="15">log I</text><text x="80" y="97">z / Å</text></svg>;
}

function AtomicMap({ selectedSite, onSelect }: { selectedSite: SiteId; onSelect: (site: SiteId) => void }) {
  const sites = Array.from({ length: 56 }, (_, index) => {
    const col = index % 8;
    const row = Math.floor(index / 8);
    const position = row === 3 && col === 4 ? "defect" : row === 2 && col === 3 ? "site" : "terrace";
    const isTarget = position === selectedSite && (position !== "terrace" || (row === 4 && col === 2));
    return <circle key={index} cx={12 + col * 11 + (row % 2 ? 5.5 : 0)} cy={13 + row * 13} r={position === "defect" ? 4.5 : 3.7} className={isTarget ? "stm-atom active" : position === "defect" ? "stm-atom defect" : "stm-atom"} onClick={() => onSelect(position)} />;
  });
  return <svg className="stm-atomic-map" viewBox="0 0 110 105" role="img" aria-label="Clickable conceptual atomic topography map"><rect width="110" height="105" className="stm-map-bg" />{sites}<path d="M8 96H32M8 96V72" className="stm-scale" /><text x="35" y="98">0.5 nm</text><text x="8" y="9">CONSTANT-I</text></svg>;
}

function linecutLdos(sample: SamplePreset, energy: number, temperature: number, position: number, mode: LinecutMode) {
  const width = broadening(temperature);
  const defectEnvelope = Math.exp(-((position - 52) ** 2) / (2 * 6.8 ** 2));
  if (mode === "defect") {
    const terrace = ldos(sample, energy, temperature, "terrace");
    const localizedState = gaussian(energy, -.16, width * 1.25, .62) + .075;
    return clamp(terrace + defectEnvelope * localizedState, .01, 1.55);
  }
  const interfaceFraction = logistic(position, 51, 4.2);
  const interfaceEnvelope = Math.exp(-((position - 51) ** 2) / (2 * 7.5 ** 2));
  const metalLike = .12 + .68 * Math.abs(energy) + gaussian(energy, .1, width * 1.7, .1);
  const gappedReference = ldos(sample.id === "hopg" ? samples[1] : sample, energy, temperature, "terrace");
  const interfaceState = gaussian(energy, .12, width * 1.55, .25);
  return clamp(metalLike * (1 - interfaceFraction) + gappedReference * interfaceFraction + interfaceEnvelope * interfaceState, .01, 1.55);
}

function linecutColor(value: number) {
  const normalized = clamp((value - .01) / 1.54, 0, 1);
  return `hsl(${218 - normalized * 112} ${42 + normalized * 18}% ${18 + normalized * 37}%)`;
}

function LinecutTrack({ mode, position, onProbe }: { mode: LinecutMode; position: number; onProbe: (position: number) => void }) {
  const selectPosition = (event: MouseEvent<SVGSVGElement>) => {
    const bounds = event.currentTarget.getBoundingClientRect();
    onProbe(clamp(((event.clientX - bounds.left) / bounds.width) * 100, 0, 100));
  };
  return <svg className="stm-linecut-track" viewBox="0 0 100 32" role="img" aria-label="Clickable conceptual STS linecut path" onClick={selectPosition}><path d="M4 22H96" className="stm-linecut-path" />{mode === "defect" ? <><circle cx="52" cy="22" r="5" className="stm-linecut-defect" /><path d="M52 6V29" className="stm-linecut-anchor" /></> : <><path d="M51 5V29" className="stm-linecut-interface" /><text x="53" y="10">interface</text><text x="10" y="29">metal-like</text><text x="76" y="29">gapped</text></>}<circle cx={position} cy="22" r="3.1" className="stm-linecut-probe" /><path d={`M${position} 5V28`} className="stm-linecut-cursor" /><text x="5" y="9">A</text><text x="92" y="9">B</text></svg>;
}

function SpatialEnergyMap({ sample, temperature, mode, position, onProbe }: { sample: SamplePreset; temperature: number; mode: LinecutMode; position: number; onProbe: (position: number) => void }) {
  const columns = 44;
  const rows = 52;
  const cells = Array.from({ length: columns * rows }, (_, index) => {
    const column = index % columns;
    const row = Math.floor(index / columns);
    const x = (column + .5) / columns * 100;
    const energy = 1.45 - (row + .5) / rows * 2.9;
    const signal = linecutLdos(sample, energy, temperature, x, mode);
    return <rect key={index} x={column * 100 / columns} y={row * 100 / rows} width={100 / columns + .1} height={100 / rows + .1} fill={linecutColor(signal)} onClick={() => onProbe(x)} />;
  });
  return <svg className="stm-linecut-map" viewBox="0 0 100 100" role="img" aria-label="Clickable conceptual spatial energy map of local density of states"><rect width="100" height="100" className="stm-linecut-map-bg" />{cells}<path d="M1 50H99" className="stm-linecut-ef" /><path d={`M${position.toFixed(2)} 1V99`} className="stm-linecut-map-cursor" /><circle cx={position} cy="50" r="2.1" className="stm-linecut-map-probe" /><text x="3" y="8">+E</text><text x="3" y="96">−E</text><text x="4" y="47">Eᶠ</text><text x="4" y="58">A</text><text x="93" y="96">B</text></svg>;
}

function LinecutSpectrum({ sample, temperature, mode, position }: { sample: SamplePreset; temperature: number; mode: LinecutMode; position: number }) {
  const points = Array.from({ length: 180 }, (_, index) => {
    const energy = -1.45 + index / 179 * 2.9;
    const signal = linecutLdos(sample, energy, temperature, position, mode);
    return `${(7 + index / 179 * 87).toFixed(2)},${(87 - signal * 46).toFixed(2)}`;
  }).join(" ");
  return <svg className="stm-chart stm-linecut-spectrum" viewBox="0 0 100 100" role="img" aria-label="Conceptual local dI dV spectrum selected from STS linecut"><path d="M7 87H94M7 10V87" className="stm-axis" /><path d="M50 10V87" className="stm-zero" /><polyline points={points} className="stm-linecut-spectrum-line" /><text x="8" y="15">dI/dV</text><text x="78" y="97">eV</text><text x="48" y="94">Eᶠ</text></svg>;
}

export default function StmSts() {
  const [sampleId, setSampleId] = useState<SampleId>("mos2");
  const [bias, setBias] = useState(.68);
  const [distance, setDistance] = useState(5.6);
  const [temperature, setTemperature] = useState(77);
  const [site, setSite] = useState<SiteId>("site");
  const [linecutMode, setLinecutMode] = useState<LinecutMode>("defect");
  const [linecutPosition, setLinecutPosition] = useState(52);
  const sample = samples.find((item) => item.id === sampleId) ?? samples[0];
  const model = useMemo(() => tunnellingModel(sample, bias, distance, temperature, site), [sample, bias, distance, temperature, site]);
  const linecutSignal = useMemo(() => linecutLdos(sample, bias, temperature, linecutPosition, linecutMode), [sample, bias, temperature, linecutPosition, linecutMode]);

  const reset = () => {
    setSampleId("mos2");
    setBias(.68);
    setDistance(5.6);
    setTemperature(77);
    setSite("site");
    setLinecutMode("defect");
    setLinecutPosition(52);
    toast("คืนค่า STM/STS teaching model แล้ว");
  };
  const runMeasurement = () => toast.success("อัปเดต STM/STS conceptual scan แล้ว", { description: `I = ${model.currentPa.toFixed(1)} pA · dI/dV proxy = ${model.conductanceNs.toFixed(3)} nS` });
  const selectSite = (nextSite: SiteId) => {
    setSite(nextSite);
    toast(`เลือก local probe: ${siteModifier(nextSite).label}`);
  };
  const selectLinecutProbe = (nextPosition: number) => {
    setLinecutPosition(nextPosition);
    toast(`เลือก linecut probe ที่ x ${nextPosition.toFixed(0)}%`);
  };

  return <div className="stm-shell">
    <header className="lab-header stm-header">
      <div className="materials-brand-group">
        <Link href="/" className="brand-lockup" aria-label="กลับสู่ Nanophysics Virtual Lab 01"><span className="stm-mark"><Microscope size={19} /><i /><b /><b /></span><span><strong>NANOPHYSICS</strong><em>VIRTUAL LAB / 01</em></span></Link>
        <span className="module-route-label">MODULE / STM + STS</span>
      </div>
      <div className="header-status"><span className="status-dot" /><span>QUANTUM TUNNELLING / LIVE</span><span className="header-divider" /><span>SEMI-EMPIRICAL</span></div>
      <div className="header-actions"><Link href="/quantum-materials" className="header-action"><Atom size={16} /> 2D + Quantum Lab</Link><Link href="/materials" className="header-action"><ArrowLeft size={16} /> Nano Materials</Link></div>
    </header>

    <main>
      <section className="stm-hero" style={{ backgroundImage: `linear-gradient(90deg, rgba(7,17,32,.98), rgba(7,17,32,.88) 45%, rgba(7,17,32,.28)), url(${heroImage})` }}>
        <div className="stm-hero-copy"><p className="eyebrow"><Zap size={15} /> SCANNING TUNNELLING MICROSCOPY</p><h1>เข้าใกล้ระดับอะตอม<br />แล้วอ่าน LDOS</h1><p>ปรับ bias, ระยะ tip–sample และอุณหภูมิ เพื่อเชื่อม tunnelling current กับ topographic contrast และ dI/dV spectroscopy ในกรอบแบบจำลองการสอน</p><div className="stm-hero-chip"><Crosshair size={14} /><span>ACTIVE OBSERVABLE / LDOS</span><b>causal relationships, not measured data or DFT</b></div></div>
        <div className="stm-hero-evidence" aria-hidden="true"><span>SCAN WINDOW / 1.8 nm</span><div><i /><i /><i /><i /><i /><i /></div><b>z → I(z) → dI/dV</b></div><div className="stm-hero-trace" aria-hidden="true"><span>OBSERVABLE STACK</span><svg viewBox="0 0 270 120"><path d="M6 101H260M6 25V101" /><polyline points="8,92 29,90 48,86 66,77 84,85 105,58 125,71 145,40 167,63 187,27 207,52 230,18 261,33" /><circle cx="145" cy="40" r="4" /></svg><b>I(z) ↔ dI/dV ↔ LDOS</b></div>
      </section>

      <section className="stm-sample-rack"><div><p className="section-kicker">SAMPLE PRESETS</p><h2>เลือก reference system</h2></div><div className="stm-rack-strip">{samples.map((item, index) => <button key={item.id} className={item.id === sampleId ? "stm-sample-card active" : "stm-sample-card"} onClick={() => setSampleId(item.id)} aria-pressed={item.id === sampleId}><span>0{index + 1}</span><em>RACK / P-{String(index + 1).padStart(2, "0")}</em><b>{item.label}</b><small>{item.tag}</small><u>OBS / LDOS</u><i style={{ background: item.accent }} /></button>)}</div></section>

      <section className="stm-workbench" aria-label="STM STS conceptual workbench">
        <aside className="stm-controls"><div className="stm-panel-heading"><span className="panel-index">A</span><div><p>CONTROL STACK</p><h2>Tunnelling junction</h2><span>tune one cause at a time</span></div></div>
          <div className="stm-control"><div><label htmlFor="stm-bias">Sample bias</label><output>{bias >= 0 ? "+" : ""}{bias.toFixed(2)} V</output></div><input id="stm-bias" type="range" min="-1.4" max="1.4" step="0.02" value={bias} onChange={(event) => setBias(Number(event.target.value))} /><p>occupied ← Eᶠ → empty states</p></div>
          <div className="stm-control"><div><label htmlFor="stm-distance">Tip–sample distance</label><output>{distance.toFixed(2)} Å</output></div><input id="stm-distance" type="range" min="4.5" max="8.6" step="0.05" value={distance} onChange={(event) => setDistance(Number(event.target.value))} /><p>vacuum-barrier width proxy</p></div>
          <div className="stm-control"><div><label htmlFor="stm-temperature">Temperature</label><output>{temperature.toFixed(1)} K</output></div><input id="stm-temperature" type="range" min="4.2" max="300" step="1" value={temperature} onChange={(event) => setTemperature(Number(event.target.value))} /><p>thermal broadening proxy</p></div>
          <div className="stm-control-note"><CircleGauge size={16} /><p><b>Calibration cue:</b> hold feedback conditions fixed before comparing apparent height or dI/dV between positions.</p></div>
          <div className="stm-control-actions"><button onClick={runMeasurement}><Zap size={16} fill="currentColor" /> Run conceptual scan</button><button onClick={reset} title="คืนค่าตัวควบคุม"><RotateCcw size={16} /></button></div>
        </aside>

        <article className="stm-stage" style={{ backgroundImage: `linear-gradient(180deg, rgba(7,17,32,.18), rgba(7,17,32,.82)), url(${stageImage})` }}>
          <div className="stm-stage-top"><span><Microscope size={14} /> ATOMIC TUNNELLING STAGE</span><span>RACK S-00 / {sample.tag}</span></div><div className="stm-stage-grid" /><div className="stm-stage-lattice" aria-hidden="true">{Array.from({ length: 48 }, (_, index) => <i key={index} />)}</div><div className="stm-scan-reticle" aria-hidden="true"><span>SCAN WINDOW</span><i /><b>1.8 nm</b></div><div className="stm-energy-trace" aria-hidden="true"><span>LDOS / eV</span><svg viewBox="0 0 100 45"><path d="M2 39H98" /><polyline points="2,36 12,35 20,33 27,18 34,33 46,35 55,35 63,15 70,29 80,34 91,19 98,28" /></svg></div><div className="stm-tip"><i /><b /><span>W TIP</span></div><div className="stm-gap-readout"><span>z</span><b>{distance.toFixed(2)} Å</b><i /></div><div className="stm-junction-glow" style={{ opacity: clamp(1.18 - (distance - 4.5) / 4.8, .25, .95) }} /><div className="stm-stage-footer"><span>BIAS</span><b>{bias >= 0 ? "+" : ""}{bias.toFixed(2)} V</b><span>SITE</span><b>{siteModifier(site).label}</b><span>MODE</span><b>constant-I proxy</b></div><div className="stm-stage-scope"><span>TOPOGRAPHY NOTE</span><b>geometry + electronic contrast</b></div></article>

        <aside className="stm-readout"><div className="stm-panel-heading"><span className="panel-index">B</span><div><p>JUNCTION READOUT</p><h2>Measured proxies</h2><span>conceptual output</span></div></div><div className="stm-main-metric"><span>Tunnelling current I</span><strong>{model.currentPa.toFixed(1)}<small> pA</small></strong><i /></div><dl><div><dt>dI/dV proxy</dt><dd>{model.conductanceNs.toFixed(3)} nS</dd></div><div><dt>LDOS at eV</dt><dd>{model.ldosAtBias.toFixed(2)} a.u.</dd></div><div><dt>Barrier proxy φ</dt><dd>{model.barrier.toFixed(2)} eV</dd></div><div><dt>Apparent height</dt><dd>{model.apparentHeight >= 0 ? "+" : ""}{model.apparentHeight.toFixed(2)} Å</dd></div></dl><div className="stm-caveat"><Lightbulb size={16} /><p>ค่า apparent height ไม่ใช่ geometric height โดยลำพัง เพราะ current ยังขึ้นกับ electronic states, tip condition และ setpoint.</p></div></aside>
      </section>

      <section className="stm-observables"><div className="stm-observables-heading"><div><p className="section-kicker">THREE CORRELATED OBSERVABLES</p><h2>ดู current, spectrum และ map<br />ก่อนสรุปสภาพอิเล็กทรอนิกส์</h2></div><div className="stm-observables-note"><Lightbulb size={18} /><p>ปรับตัวแปรหนึ่งค่า แล้วตรวจว่า I(z), dI/dV และ atomic contrast สนับสนุนสมมติฐานเดียวกันหรือไม่</p></div></div><div className="stm-analysis-grid">
        <article className="stm-analysis-card"><header><span>RACK S-01 / TOPOGRAPHY</span><b>Atomic contrast map</b><small>observable: constant-current apparent height</small></header><div className="stm-card-calibration"><i /><span>feedback setpoint</span><b>click local site</b></div><AtomicMap selectedSite={site} onSelect={selectSite} /><footer><span>selected probe / {siteModifier(site).label}</span><span>contrast = geometry + LDOS</span></footer></article>
        <article className="stm-analysis-card"><header><span>RACK S-02 / I–Z</span><b>Exponential distance response</b><small>observable: tunnelling current vs. z</small></header><div className="stm-card-calibration"><i /><span>bias fixed at {bias.toFixed(2)} V</span><b>marker: z</b></div><IZPlot sample={sample} bias={bias} temperature={temperature} site={site} distance={distance} /><footer><span>κ proxy / {model.decayConstant.toFixed(2)} Å⁻¹</span><span>log current axis</span></footer></article>
        <article className="stm-analysis-card"><header><span>RACK S-03 / STS</span><b>Local dI/dV spectrum</b><small>observable: LDOS proxy vs. energy</small></header><div className="stm-card-calibration"><i /><span>energy sweep</span><b>marker: eV</b></div><StsSpectrum sample={sample} temperature={temperature} site={site} bias={bias} /><footer><span>thermal width / {broadening(temperature).toFixed(3)} eV</span><span>not absolute DOS</span></footer></article>
      </div></section>

      <section className="stm-linecut-section"><div className="stm-linecut-heading"><div><p className="section-kicker">SPATIAL–ENERGY SPECTROSCOPY</p><h2>ลากเส้นข้าม defect หรือ interface<br />แล้วอ่าน LDOS ตามตำแหน่ง</h2></div><div className="stm-linecut-intro"><ScanLine size={18} /><p>เลือก path แล้วคลิก linecut หรือ heatmap เพื่อเปรียบเทียบ local dI/dV ตามพิกัด x และพลังงาน eV</p></div></div><div className="stm-linecut-workbench">
        <aside className="stm-linecut-controls"><span className="panel-index">C</span><p>LINECUT PROTOCOL</p><h3>Path configuration</h3><div className="stm-linecut-mode" role="radiogroup" aria-label="เลือกเส้นทาง STS linecut"><button className={linecutMode === "defect" ? "active" : ""} onClick={() => setLinecutMode("defect")} role="radio" aria-checked={linecutMode === "defect"}><span>PATH / 01</span><b>Defect crossing</b><small>localized in-gap state</small></button><button className={linecutMode === "interface" ? "active" : ""} onClick={() => setLinecutMode("interface")} role="radio" aria-checked={linecutMode === "interface"}><span>PATH / 02</span><b>Interface crossing</b><small>metal-like → gapped</small></button></div><div className="stm-linecut-control"><div><label htmlFor="linecut-position">Probe position</label><output>x {linecutPosition.toFixed(0)}%</output></div><input id="linecut-position" type="range" min="0" max="100" step="1" value={linecutPosition} onChange={(event) => setLinecutPosition(Number(event.target.value))} /><p>A ← position → B</p></div><div className="stm-linecut-calibration"><CircleGauge size={16} /><p><b>Calibration cue:</b> all spectra use the same energy window and temperature-broadening proxy.</p></div></aside>
        <article className="stm-linecut-stage"><header><span><Waves size={14} /> RACK S-04 / STS LINECUT</span><b>ACTIVE / {linecutMode.toUpperCase()}</b></header><div className="stm-linecut-track-frame"><LinecutTrack mode={linecutMode} position={linecutPosition} onProbe={selectLinecutProbe} /></div><div className="stm-linecut-map-frame"><SpatialEnergyMap sample={sample} temperature={temperature} mode={linecutMode} position={linecutPosition} onProbe={selectLinecutProbe} /></div><footer><span>click map to place probe</span><span>observable / dI/dV(x, E)</span></footer></article>
        <aside className="stm-linecut-readout"><span className="panel-index">D</span><p>LOCAL LINECUT PROBE</p><h3>dI/dV at x</h3><div className="stm-linecut-position"><span>POSITION</span><b>x {linecutPosition.toFixed(0)}% · {linecutMode === "defect" ? "defect axis" : "interface axis"}</b></div><dl><div><dt>Active energy</dt><dd>{bias >= 0 ? "+" : ""}{bias.toFixed(2)} eV</dd></div><div><dt>LDOS proxy</dt><dd>{linecutSignal.toFixed(2)} a.u.</dd></div><div><dt>Thermal width</dt><dd>{broadening(temperature).toFixed(3)} eV</dd></div><div><dt>Linecut mode</dt><dd>{linecutMode}</dd></div></dl><div className="stm-linecut-mini"><LinecutSpectrum sample={sample} temperature={temperature} mode={linecutMode} position={linecutPosition} /></div><p className="stm-linecut-question"><Lightbulb size={15} /> ความเข้ม in-gap ที่เพิ่มขึ้นใกล้ defect หรือ interface พอจะยืนยัน localized state ได้หรือยัง?</p></aside>
      </div><div className="stm-linecut-footer"><span>MODEL NOTE / linecut สร้างจาก LDOS proxy ตามตำแหน่งและพลังงาน ไม่ใช่ข้อมูล spectroscopy ที่ผ่าน lock-in, tip calibration หรือ deconvolution จริง</span><span>CHECK / เปรียบเทียบ map, local spectrum และ topography ก่อนสรุป defect state หรือ band alignment</span></div></section>

      <section className="stm-evidence-strip"><div><p className="section-kicker">MEASUREMENT LITERACY</p><h2>จากสัญญาณอุโมงค์<br />สู่ข้อสรุปทางฟิสิกส์</h2></div><div className="stm-evidence-flow"><article><span>CONTROL</span><b>V · z · T · position</b></article><i>→</i><article><span>JUNCTION</span><b>I ∝ e<sup>−κz</sup></b></article><i>→</i><article><span>OBSERVABLE</span><b>topography · dI/dV(x,E)</b></article><i>→</i><article><span>VALIDATE</span><b>tip + setpoint + map</b></article></div><p>คำถาม: ถ้า topography สว่างขึ้นพร้อม dI/dV เพิ่มขึ้น เราแยก structural height ออกจาก electronic contrast ได้เพียงใด?</p></section>
    </main>
    <footer className="lab-footer"><span>RACK STM-01 · semi-empirical nanophysics teaching lab</span><span>OBS / I(z) · dI/dV · dI/dV(x,E) · SETPOINT / V · z · T</span><span>Conceptual model — not a substitute for measured or first-principles data</span></footer>
  </div>;
}
