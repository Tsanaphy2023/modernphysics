/**
 * Precision Instrument Console — 2D & Quantum Materials Lab turns a semi-empirical teaching model
 * into a traceable workflow: choose material, tune external controls, then inspect band/optical/transport proxies.
 */
import { Link } from "wouter";
import { type MouseEvent, useMemo, useState } from "react";
import {
  ArrowLeft,
  Atom,
  CircleGauge,
  Crosshair,
  Layers3,
  Lightbulb,
  Orbit,
  RotateCcw,
  ScanLine,
  Sparkles,
  Thermometer,
  Waves,
  Zap,
} from "lucide-react";
import { toast } from "sonner";
import "./QuantumMaterials.css";
import "./QuantumMapping.css";

type MaterialId = "mos2" | "wse2" | "bilayerGraphene" | "graphene";
type MapMode = "strain" | "pl" | "raman";
type MaterialPreset = {
  id: MaterialId;
  label: string;
  formula: string;
  description: string;
  tag: string;
  baseGap: number;
  bulkGap: number;
  baseBinding: number;
  mobility: number;
  strainCoefficient: number;
  fieldCoefficient: number;
  direct: boolean;
  dirac: boolean;
  accent: string;
};

const heroImage = "/manus-storage/quantum-materials-hero_24f6e417.png";
const layerImage = "/manus-storage/quantum-materials-layer-stack_67a196e2.png";
const strainImage = "/manus-storage/quantum-materials-strain-map_b442ebbd.png";

const materials: MaterialPreset[] = [
  { id: "mos2", label: "MoS₂-like", formula: "MX₂", description: "direct-gap TMD teaching preset", tag: "TMD / DIRECT", baseGap: 1.88, bulkGap: 1.25, baseBinding: .48, mobility: 58, strainCoefficient: -.075, fieldCoefficient: .035, direct: true, dirac: false, accent: "#c7f36b" },
  { id: "wse2", label: "WSe₂-like", formula: "MX₂", description: "strain-responsive exciton preset", tag: "TMD / EXCITON", baseGap: 1.65, bulkGap: 1.18, baseBinding: .42, mobility: 74, strainCoefficient: -.064, fieldCoefficient: .028, direct: true, dirac: false, accent: "#81d9e8" },
  { id: "bilayerGraphene", label: "Bilayer graphene-like", formula: "C₂", description: "gate-tunable gap teaching preset", tag: "BILAYER / GATE", baseGap: .03, bulkGap: .01, baseBinding: .13, mobility: 420, strainCoefficient: -.012, fieldCoefficient: .22, direct: false, dirac: true, accent: "#e9ad73" },
  { id: "graphene", label: "Graphene-like", formula: "C", description: "gapless Dirac reference preset", tag: "DIRAC / REFERENCE", baseGap: .01, bulkGap: .01, baseBinding: .08, mobility: 730, strainCoefficient: -.004, fieldCoefficient: .008, direct: false, dirac: true, accent: "#d9e4dc" },
];

const clamp = (value: number, minimum: number, maximum: number) => Math.min(maximum, Math.max(minimum, value));
const gaussian = (x: number, center: number, width: number, amplitude: number) => amplitude * Math.exp(-((x - center) ** 2) / (2 * width ** 2));

function modelProperties(material: MaterialPreset, layers: number, strain: number, gateField: number, screening: number, temperature: number) {
  const layerFraction = 1 - Math.exp(-(layers - 1) / 2.15);
  const layerGap = material.baseGap - (material.baseGap - material.bulkGap) * layerFraction;
  const strainGap = material.strainCoefficient * strain;
  const fieldGap = material.fieldCoefficient * Math.abs(gateField) * (material.id === "bilayerGraphene" ? 1 : .28);
  const temperatureGap = -.00024 * (temperature - 300);
  const gap = clamp(layerGap + strainGap + fieldGap + temperatureGap, material.id === "graphene" ? 0 : .015, 2.6);
  const excitonBinding = clamp(material.baseBinding * (1 + Math.abs(strain) * .045) / Math.sqrt(screening * Math.max(1, layers * .72)), .025, .65);
  const opticalEnergy = clamp(gap - excitonBinding, .01, 2.55);
  const transport = clamp(material.mobility * (1 + .08 * Math.abs(gateField)) * (1 + .07 * (layers - 1)) * Math.exp(-.0017 * (temperature - 300)) * (1 - .055 * Math.abs(strain)), 2, 1200);
  const valleySplit = material.direct ? Math.abs(strain) * 14 + Math.abs(gateField) * 7 : 0;
  const transition = material.direct && layers <= 2 ? "direct-like" : material.dirac ? gap < .05 ? "Dirac-like" : "field-opened" : "indirect-like";
  return { gap, excitonBinding, opticalEnergy, transport, valleySplit, transition };
}

function BandDiagram({ material, gap, gateField }: { material: MaterialPreset; gap: number; gateField: number }) {
  const points = Array.from({ length: 110 }, (_, index) => {
    const k = -1 + (index / 109) * 2;
    const energy = material.dirac ? Math.sqrt((k * .86) ** 2 + (gap / 2) ** 2) : gap / 2 + .72 * k ** 2;
    const conduction = 50 - energy * 28 - gateField * 1.4 * k;
    const valence = 50 + energy * 28 - gateField * 1.4 * k;
    return { x: 8 + ((k + 1) / 2) * 85, conduction, valence };
  });
  const toPoints = (band: "conduction" | "valence") => points.map((point) => `${point.x.toFixed(2)},${point[band].toFixed(2)}`).join(" ");
  const gapHeight = Math.max(3, gap * 28);
  return <svg className="qm-band-svg" viewBox="0 0 100 100" role="img" aria-label="Conceptual band structure"><path d="M8 50H93M8 8V91" className="qm-axis" /><polyline points={toPoints("conduction")} className="qm-band-conduction" /><polyline points={toPoints("valence")} className="qm-band-valence" /><path d={`M50 ${50 - gapHeight / 2}V${50 + gapHeight / 2}`} className="qm-gap-marker" /><text x="54" y="50">E₉</text><text x="86" y="97">k</text><text x="10" y="13">E</text></svg>;
}

function OpticalResponse({ opticalEnergy, excitonBinding, temperature }: { opticalEnergy: number; excitonBinding: number; temperature: number }) {
  const width = .045 + temperature * .00018;
  const points = Array.from({ length: 130 }, (_, index) => {
    const energy = .35 + (index / 129) * 2.25;
    const signal = .05 + gaussian(energy, opticalEnergy, width, .8) + gaussian(energy, opticalEnergy + .18 + excitonBinding * .22, width * 1.5, .25);
    return `${(7 + (index / 129) * 87).toFixed(2)},${(89 - signal * 68).toFixed(2)}`;
  }).join(" ");
  const peakX = 7 + ((opticalEnergy - .35) / 2.25) * 87;
  return <svg className="qm-optical-svg" viewBox="0 0 100 100" role="img" aria-label="Conceptual optical response"><path d="M7 90H94M7 10V90" className="qm-axis" /><polyline points={points} className="qm-optical-line" /><path d={`M${peakX.toFixed(2)} 17V90`} className="qm-optical-marker" /><text x="9" y="15">ABS.</text><text x="70" y="98">Photon energy</text></svg>;
}

function spectroscopyProperties(material: MaterialPreset, opticalEnergy: number, zeroStrainOpticalEnergy: number, strain: number, temperature: number) {
  const isTmd = material.id === "mos2" || material.id === "wse2";
  const plWidth = .042 + temperature * .00009 + Math.abs(strain) * .004;
  const plIntensity = material.direct ? clamp(.92 - Math.abs(strain) * .11 - Math.max(0, temperature - 280) * .0006, .16, .94) : clamp(.13 - Math.abs(strain) * .025, .035, .15);
  const primaryBase = material.id === "mos2" ? 385 : material.id === "wse2" ? 250 : 1582;
  const secondaryBase = material.id === "mos2" ? 405 : material.id === "wse2" ? 260 : 2700;
  const primarySlope = isTmd ? -3.2 : -18.5;
  const secondarySlope = isTmd ? -1.25 : -42;
  const thermalSlope = isTmd ? -.010 : -.016;
  const primary = primaryBase + primarySlope * strain + thermalSlope * (temperature - 300);
  const secondary = secondaryBase + secondarySlope * strain + thermalSlope * .7 * (temperature - 300);
  return {
    plEnergy: opticalEnergy,
    plReferenceEnergy: zeroStrainOpticalEnergy,
    plShiftMeV: (opticalEnergy - zeroStrainOpticalEnergy) * 1000,
    plWidth,
    plIntensity,
    ramanPrimary: primary,
    ramanSecondary: secondary,
    ramanPrimaryBase: primaryBase + thermalSlope * (temperature - 300),
    ramanSecondaryBase: secondaryBase + thermalSlope * .7 * (temperature - 300),
    primaryLabel: isTmd ? "E′ in-plane" : "G mode",
    secondaryLabel: isTmd ? "A′₁ out-of-plane" : "2D mode",
  };
}

function PLStrainPlot({ currentEnergy, referenceEnergy, width, intensity }: { currentEnergy: number; referenceEnergy: number; width: number; intensity: number }) {
  const minEnergy = 0;
  const maxEnergy = 2.4;
  const toPoints = (center: number, peakWidth: number, amplitude: number) => Array.from({ length: 150 }, (_, index) => {
    const energy = minEnergy + (index / 149) * (maxEnergy - minEnergy);
    const signal = .025 + gaussian(energy, center, peakWidth, amplitude);
    return `${(7 + (index / 149) * 87).toFixed(2)},${(89 - signal * 68).toFixed(2)}`;
  }).join(" ");
  const refX = 7 + (referenceEnergy / maxEnergy) * 87;
  const currentX = 7 + (currentEnergy / maxEnergy) * 87;
  return <svg className="qm-spec-svg" viewBox="0 0 100 100" role="img" aria-label="Conceptual strain-dependent photoluminescence emission"><path d="M7 90H94M7 10V90" className="qm-axis" /><polyline points={toPoints(referenceEnergy, width * .85, .65)} className="qm-reference-trace" /><polyline points={toPoints(currentEnergy, width, intensity)} className="qm-pl-trace" /><path d={`M${refX.toFixed(2)} 16V90`} className="qm-reference-marker" /><path d={`M${currentX.toFixed(2)} 18V90`} className="qm-active-marker" /><text x="9" y="15">PL</text><text x="68" y="98">Photon energy</text></svg>;
}

function RamanStrainPlot({ material, primary, secondary, primaryBase, secondaryBase }: { material: MaterialPreset; primary: number; secondary: number; primaryBase: number; secondaryBase: number }) {
  const isTmd = material.id === "mos2" || material.id === "wse2";
  const minShift = isTmd ? 200 : 1200;
  const maxShift = isTmd ? 480 : 2900;
  const width = isTmd ? 8 : 34;
  const toPoints = (first: number, second: number) => Array.from({ length: 160 }, (_, index) => {
    const shift = minShift + (index / 159) * (maxShift - minShift);
    const signal = .025 + gaussian(shift, first, width, .78) + gaussian(shift, second, width * 1.15, .53);
    return `${(7 + (index / 159) * 87).toFixed(2)},${(89 - signal * 70).toFixed(2)}`;
  }).join(" ");
  const toX = (shift: number) => 7 + ((shift - minShift) / (maxShift - minShift)) * 87;
  return <svg className="qm-spec-svg" viewBox="0 0 100 100" role="img" aria-label="Conceptual strain-dependent Raman spectrum"><path d="M7 90H94M7 10V90" className="qm-axis" /><polyline points={toPoints(primaryBase, secondaryBase)} className="qm-reference-trace" /><polyline points={toPoints(primary, secondary)} className="qm-raman-trace" /><path d={`M${toX(primary).toFixed(2)} 20V90`} className="qm-active-marker" /><path d={`M${toX(secondary).toFixed(2)} 38V90`} className="qm-active-marker secondary" /><text x="9" y="15">RAMAN</text><text x="63" y="98">Raman shift</text></svg>;
}

function localStrainField(x: number, y: number, nominalStrain: number) {
  const dx = (x - 50) / 50;
  const dy = (y - 50) / 50;
  const localDeformation = Math.exp(-((dx - .12) ** 2 + (dy + .08) ** 2) / .16);
  const wrinkle = .17 * Math.exp(-((dx + .44) ** 2 + (dy - .28) ** 2) / .035);
  return nominalStrain * (.12 + .88 * localDeformation + wrinkle);
}

function mapColor(mode: MapMode, value: number, nominalStrain: number) {
  if (mode === "strain") {
    const normalized = clamp((value / Math.max(Math.abs(nominalStrain), .15) + 1) / 2, 0, 1);
    return `hsl(${220 - normalized * 200} 54% ${29 + normalized * 28}%)`;
  }
  if (mode === "pl") {
    const normalized = clamp((value + 160) / 320, 0, 1);
    return `hsl(${225 - normalized * 170} 56% ${27 + normalized * 30}%)`;
  }
  const normalized = clamp((value + 9) / 18, 0, 1);
  return `hsl(${230 - normalized * 135} 50% ${27 + normalized * 28}%)`;
}

function MappingHeatmap({ mode, nominalStrain, material, layers, gateField, screening, temperature, onProbe, probe }: { mode: MapMode; nominalStrain: number; material: MaterialPreset; layers: number; gateField: number; screening: number; temperature: number; onProbe: (point: { x: number; y: number }) => void; probe: { x: number; y: number } }) {
  const grid = 22;
  const zero = modelProperties(material, layers, 0, gateField, screening, temperature);
  const cells = Array.from({ length: grid * grid }, (_, index) => {
    const col = index % grid;
    const row = Math.floor(index / grid);
    const x = (col + .5) / grid * 100;
    const y = (row + .5) / grid * 100;
    const localStrain = localStrainField(x, y, nominalStrain);
    const local = modelProperties(material, layers, localStrain, gateField, screening, temperature);
    const localSpectra = spectroscopyProperties(material, local.opticalEnergy, zero.opticalEnergy, localStrain, temperature);
    const value = mode === "strain" ? localStrain : mode === "pl" ? localSpectra.plShiftMeV : localSpectra.ramanPrimary - localSpectra.ramanPrimaryBase;
    return <rect key={index} x={col * (100 / grid)} y={row * (100 / grid)} width={100 / grid + .1} height={100 / grid + .1} fill={mapColor(mode, value, nominalStrain)} onClick={() => onProbe({ x, y })} />;
  });
  return <svg className="qm-map-svg" viewBox="0 0 100 100" role="img" aria-label="Clickable conceptual two-dimensional spectroscopy map"><rect width="100" height="100" fill="#12263b" />{cells}<path d="M50 1V99M1 50H99" className="qm-map-axis" /><circle cx={probe.x} cy={probe.y} r="4" className="qm-probe-ring" /><circle cx={probe.x} cy={probe.y} r="1.35" className="qm-probe-dot" /><text x="4" y="8">Y</text><text x="91" y="97">X</text></svg>;
}

function LayerStack({ layers, material, strain }: { layers: number; material: MaterialPreset; strain: number }) {
  return <div className="qm-layer-stack" aria-label={`${layers} atomically thin layers`} style={{ "--layer-accent": material.accent } as React.CSSProperties}>{Array.from({ length: layers }, (_, index) => <span key={index} style={{ transform: `translate(-50%, ${index * 13 - ((layers - 1) * 13) / 2}px) skewX(${strain * .6}deg)` }}><i /><i /><i /><i /><i /></span>)}</div>;
}

export default function QuantumMaterials() {
  const [materialId, setMaterialId] = useState<MaterialId>("mos2");
  const [layers, setLayers] = useState(1);
  const [strain, setStrain] = useState(.2);
  const [gateField, setGateField] = useState(.25);
  const [screening, setScreening] = useState(4.2);
  const [temperature, setTemperature] = useState(300);
  const [mapMode, setMapMode] = useState<MapMode>("strain");
  const [probe, setProbe] = useState({ x: 56, y: 42 });
  const material = materials.find((item) => item.id === materialId) ?? materials[0];
  const result = useMemo(() => modelProperties(material, layers, strain, gateField, screening, temperature), [material, layers, strain, gateField, screening, temperature]);
  const zeroStrainResult = useMemo(() => modelProperties(material, layers, 0, gateField, screening, temperature), [material, layers, gateField, screening, temperature]);
  const spectroscopy = useMemo(() => spectroscopyProperties(material, result.opticalEnergy, zeroStrainResult.opticalEnergy, strain, temperature), [material, result.opticalEnergy, zeroStrainResult.opticalEnergy, strain, temperature]);
  const probeStrain = useMemo(() => localStrainField(probe.x, probe.y, strain), [probe.x, probe.y, strain]);
  const probeResult = useMemo(() => modelProperties(material, layers, probeStrain, gateField, screening, temperature), [material, layers, probeStrain, gateField, screening, temperature]);
  const probeZero = useMemo(() => modelProperties(material, layers, 0, gateField, screening, temperature), [material, layers, gateField, screening, temperature]);
  const probeSpectroscopy = useMemo(() => spectroscopyProperties(material, probeResult.opticalEnergy, probeZero.opticalEnergy, probeStrain, temperature), [material, probeResult.opticalEnergy, probeZero.opticalEnergy, probeStrain, temperature]);

  const resetControls = () => {
    setMaterialId("mos2");
    setLayers(1);
    setStrain(.2);
    setGateField(.25);
    setScreening(4.2);
    setTemperature(300);
    toast("คืนค่าชุดควบคุมของ 2D quantum workbench แล้ว");
  };

  const runMeasurement = () => toast.success("อัปเดต quantum material model แล้ว", { description: `E₉ = ${result.gap.toFixed(3)} eV · optical proxy = ${result.opticalEnergy.toFixed(3)} eV` });
  const selectProbe = (point: { x: number; y: number }) => { setProbe(point); toast(`เลือก probe ที่ x ${point.x.toFixed(0)} · y ${point.y.toFixed(0)}`); };

  return <div className="quantum-shell">
    <header className="lab-header quantum-header">
      <div className="materials-brand-group">
        <Link href="/" className="brand-lockup" aria-label="กลับสู่ Nanophysics Virtual Lab 01"><span className="quantum-mark"><Atom size={20} /><i /><b /><b /><b /></span><span><strong>NANOPHYSICS</strong><em>VIRTUAL LAB / 01</em></span></Link>
        <span className="module-route-label">MODULE / 2D + QUANTUM</span>
      </div>
      <div className="header-status"><span className="status-dot" /><span>TEACHING MODEL / LIVE</span><span className="header-divider" /><span>SEMI-EMPIRICAL</span></div>
      <div className="header-actions"><Link href="/materials" className="header-action"><ArrowLeft size={16} /> Nano Materials</Link><Link href="/" className="header-action">Lab 01 Geometry</Link></div>
    </header>

    <main>
      <section className="quantum-hero" style={{ backgroundImage: `linear-gradient(90deg, rgba(7,17,32,.97), rgba(7,17,32,.84) 46%, rgba(7,17,32,.28)), url(${heroImage})` }}>
        <div className="quantum-hero-copy"><p className="eyebrow"><Sparkles size={15} /> 2D MATERIALS & QUANTUM MATERIALS</p><h1>ทดสอบสมมติฐาน:<br />layer · strain · gate<br />→ quantum response</h1><p>ปรับตัวแปรหนึ่งค่า แล้วตรวจว่าความสัมพันธ์ระหว่างโครงสร้างระดับอะตอมกับ band / exciton / transport response เปลี่ยนอย่างไร</p><div className="quantum-hero-chip"><Crosshair size={14} /><span>MODEL SCOPE</span><b>causal relationships, not a DFT calculation</b></div></div><div className="quantum-hero-trace" aria-hidden="true"><span>VIRTUAL OBSERVABLES</span><svg viewBox="0 0 270 120"><path d="M6 101H260M6 25V101" /><polyline points="8,90 30,83 50,88 72,70 95,79 116,52 138,64 160,36 185,48 208,28 235,34 261,17" /><circle cx="160" cy="36" r="4" /></svg><b>E₉ ↔ X₀ ↔ μ</b></div>
      </section>

      <section className="qm-material-rack"><div><p className="section-kicker">MATERIAL PRESETS</p><h2>เลือก reference system</h2></div><div className="qm-rack-strip">{materials.map((item, index) => <button key={item.id} className={item.id === materialId ? "qm-material-card active" : "qm-material-card"} onClick={() => setMaterialId(item.id)} aria-pressed={item.id === materialId}><span>0{index + 1}</span><b>{item.label}</b><small>{item.tag}</small><i style={{ background: item.accent }} /></button>)}</div></section>

      <section className="qm-workbench" aria-label="2D quantum materials workbench">
        <aside className="qm-controls"><div className="qm-panel-heading"><span className="panel-index">A</span><div><p>CONTROL STACK</p><h2>External parameters</h2><span>tune one cause at a time</span></div></div>
          <div className="qm-control"><div><label htmlFor="layers">Layer count</label><output>{layers}L</output></div><input id="layers" type="range" min="1" max="8" step="1" value={layers} onChange={(event) => setLayers(Number(event.target.value))} /><p>Interlayer coupling proxy</p></div>
          <div className="qm-control"><div><label htmlFor="strain">Biaxial strain</label><output>{strain.toFixed(1)}%</output></div><input id="strain" type="range" min="-2.5" max="2.5" step="0.1" value={strain} onChange={(event) => setStrain(Number(event.target.value))} /><p>compressive ← → tensile</p></div>
          <div className="qm-control"><div><label htmlFor="gate">Gate field</label><output>{gateField.toFixed(2)} V/nm</output></div><input id="gate" type="range" min="-1" max="1" step="0.05" value={gateField} onChange={(event) => setGateField(Number(event.target.value))} /><p>out-of-plane field proxy</p></div>
          <div className="qm-control"><div><label htmlFor="screening">Dielectric screening</label><output>κ {screening.toFixed(1)}</output></div><input id="screening" type="range" min="1" max="12" step="0.1" value={screening} onChange={(event) => setScreening(Number(event.target.value))} /><p>environment / encapsulation proxy</p></div>
          <div className="qm-control"><div><label htmlFor="temperature">Temperature</label><output>{temperature} K</output></div><input id="temperature" type="range" min="40" max="400" step="5" value={temperature} onChange={(event) => setTemperature(Number(event.target.value))} /><p>thermal broadening proxy</p></div>
          <div className="qm-control-actions"><button onClick={runMeasurement}><Zap size={16} fill="currentColor" /> Update model</button><button onClick={resetControls} title="คืนค่าตัวควบคุม"><RotateCcw size={16} /></button></div>
        </aside>

        <article className="qm-specimen-stage" style={{ backgroundImage: `linear-gradient(180deg, rgba(7,17,32,.18), rgba(7,17,32,.79)), url(${layerImage})` }}>
          <div className="qm-stage-top"><span><Layers3 size={14} /> ATOMICALLY THIN STACK</span><span>PRESET / {material.tag}</span></div><div className="qm-grid" /><LayerStack layers={layers} material={material} strain={strain} /><div className="qm-field-arrow"><Zap size={17} /><span>{gateField >= 0 ? "+E" : "−E"}</span></div><div className="qm-stage-readout"><span>MATERIAL</span><b>{material.label}</b><span>LAYERS</span><b>{layers} atomic layer{layers > 1 ? "s" : ""}</b><span>STRAIN</span><b>{strain.toFixed(1)}%</b></div><div className="qm-strain-marker" style={{ backgroundImage: `linear-gradient(90deg, rgba(7,17,32,.3), rgba(7,17,32,.85)), url(${strainImage})` }}><span>STRAIN LANDSCAPE</span><b>{strain >= 0 ? "tensile channel" : "compressive channel"}</b></div>
        </article>

        <aside className="qm-readout"><div className="qm-panel-heading"><span className="panel-index">B</span><div><p>MODEL READOUT</p><h2>Quantum response</h2><span>conceptual output</span></div></div><div className="qm-main-metric"><span>Band gap E<sub>g</sub></span><strong>{result.gap.toFixed(3)}<small> eV</small></strong><i /></div><dl><div><dt>Transition</dt><dd>{result.transition}</dd></div><div><dt>Exciton binding</dt><dd>{result.excitonBinding.toFixed(3)} eV</dd></div><div><dt>Optical proxy X₀</dt><dd>{result.opticalEnergy.toFixed(3)} eV</dd></div><div><dt>Valley split proxy</dt><dd>{result.valleySplit.toFixed(1)} meV</dd></div></dl><div className="qm-caveat"><CircleGauge size={16} /><p>Output แสดงแนวโน้มจากแบบจำลองกึ่งประจักษ์ ไม่แทน DFT หรือค่าจากตัวอย่างจริงที่ขึ้นกับ substrate, defect, stacking และ doping</p></div></aside>
      </section>

      <section className="qm-observables"><div className="qm-observables-heading"><div><p className="section-kicker">ELECTRONIC + OPTICAL OBSERVABLES</p><h2>เปรียบเทียบ observable<br />ก่อนสรุปสมบัติ</h2></div><div className="qm-observables-note"><Lightbulb size={18} /><p>ปรับ control เพียงตัวเดียว แล้วตรวจว่า band, optical และ transport proxy ให้หลักฐานไปในทิศทางเดียวกันหรือไม่</p></div></div><div className="qm-plots"><article className="qm-plot-card"><header><span>RACK Q-01 / BAND</span><b>Conceptual band structure</b><small>observable: band edge · {material.dirac ? "Dirac-like dispersion" : "parabolic band-edge proxy"}</small></header><div className="qm-card-calibration"><i /><span>k-space reference</span><b>selected marker: E<sub>g</sub></b></div><BandDiagram material={material} gap={result.gap} gateField={gateField} /><footer><span>gap marker / proxy</span><span>E<sub>g</sub> = {result.gap.toFixed(3)} eV</span></footer></article><article className="qm-plot-card"><header><span>RACK Q-02 / OPTICS</span><b>Exciton optical response</b><small>observable: absorption proxy · temperature-dependent linewidth</small></header><div className="qm-card-calibration"><i /><span>energy scan</span><b>selected marker: X₀</b></div><OpticalResponse opticalEnergy={result.opticalEnergy} excitonBinding={result.excitonBinding} temperature={temperature} /><footer><span>X₀ marker / proxy</span><span>{result.opticalEnergy.toFixed(3)} eV</span></footer></article><article className="qm-transport-card"><header><span>RACK Q-03 / TRANSPORT</span><b>Mobility proxy</b></header><div className="qm-card-calibration"><i /><span>channel estimate</span><b>selected value: μ</b></div><div className="qm-transport-meter"><div style={{ height: `${clamp(result.transport / 12, 5, 100)}%` }} /><span>{result.transport.toFixed(0)}</span><small>cm²/V·s</small></div><div className="qm-transport-notes"><p><Thermometer size={15} /> T = {temperature} K</p><p><Orbit size={15} /> κ = {screening.toFixed(1)}</p><p><ScanLine size={15} /> field = {gateField.toFixed(2)} V/nm</p></div><footer><span>trend indicator / not mobility prediction</span></footer></article></div>
      </section>

      <section className="qm-spectroscopy"><div className="qm-spectroscopy-heading"><div><p className="section-kicker">STRAIN SPECTROSCOPY BENCH</p><h2>เปรียบเทียบ PL และ Raman<br />เมื่อ strain เปลี่ยน</h2></div><div className="qm-spectroscopy-prompt"><Waves size={18} /><p><b>คำถาม:</b> peak shift ของ PL และ Raman สนับสนุนสมมติฐานเรื่อง strain เพียงพอหรือยัง หรือควรควบคุม doping, defect และ substrate เพิ่มเติม?</p></div></div><div className="qm-spectroscopy-grid"><article className="qm-spec-card"><header><span>RACK Q-04 / PL</span><b>Excitonic photoluminescence</b><small>reference = strain 0% · current = selected strain</small></header><div className="qm-card-calibration"><i /><span>emission scan</span><b>active marker: X₀</b></div><PLStrainPlot currentEnergy={spectroscopy.plEnergy} referenceEnergy={spectroscopy.plReferenceEnergy} width={spectroscopy.plWidth} intensity={spectroscopy.plIntensity} /><div className="qm-trace-legend"><span><i className="reference" /> reference / 0%</span><span><i className="active" /> current / {strain.toFixed(1)}%</span></div><dl><div><dt>Current PL proxy</dt><dd>{spectroscopy.plEnergy.toFixed(3)} eV</dd></div><div><dt>Shift from reference</dt><dd>{spectroscopy.plShiftMeV >= 0 ? "+" : ""}{spectroscopy.plShiftMeV.toFixed(1)} meV</dd></div><div><dt>Relative intensity</dt><dd>{(spectroscopy.plIntensity * 100).toFixed(0)}%</dd></div></dl></article><article className="qm-spec-card"><header><span>RACK Q-05 / RAMAN</span><b>Phonon-mode response</b><small>mode positions are a strain proxy, not a unique strain measurement</small></header><div className="qm-card-calibration"><i /><span>phonon scan</span><b>active marker: ω</b></div><RamanStrainPlot material={material} primary={spectroscopy.ramanPrimary} secondary={spectroscopy.ramanSecondary} primaryBase={spectroscopy.ramanPrimaryBase} secondaryBase={spectroscopy.ramanSecondaryBase} /><div className="qm-trace-legend"><span><i className="reference" /> reference / 0%</span><span><i className="active" /> current / {strain.toFixed(1)}%</span></div><dl><div><dt>{spectroscopy.primaryLabel}</dt><dd>{spectroscopy.ramanPrimary.toFixed(1)} cm⁻¹</dd></div><div><dt>{spectroscopy.secondaryLabel}</dt><dd>{spectroscopy.ramanSecondary.toFixed(1)} cm⁻¹</dd></div><div><dt>Primary shift</dt><dd>{(spectroscopy.ramanPrimary - spectroscopy.ramanPrimaryBase) >= 0 ? "+" : ""}{(spectroscopy.ramanPrimary - spectroscopy.ramanPrimaryBase).toFixed(1)} cm⁻¹</dd></div></dl></article></div><div className="qm-spectroscopy-footer"><span>MODEL NOTE / coefficients are deliberately illustrative and vary with material, strain direction, substrate, doping, defects, laser energy and temperature.</span><span>CHECK / use PL + Raman as converging evidence, not as a single-variable proof.</span></div></section>

      <section className="qm-mapping-section"><div className="qm-mapping-heading"><div><p className="section-kicker">HYPERSPECTRAL MAP / CONCEPTUAL</p><h2>ค้นหา strain ที่ไม่สม่ำเสมอ<br />ด้วย PL และ Raman maps</h2></div><p>เลือก observable แล้วคลิกบนแผนที่เพื่อเปรียบเทียบ local response กับค่าเฉลี่ยของแผ่นวัสดุ</p></div><div className="qm-mapping-workbench"><aside className="qm-map-controls"><span className="panel-index">C</span><p>OBSERVABLE LAYER</p><h3>Map selector</h3><div className="qm-map-mode" role="radiogroup" aria-label="เลือก observable ของแผนที่"><button className={mapMode === "strain" ? "active" : ""} onClick={() => setMapMode("strain")} role="radio" aria-checked={mapMode === "strain"}>STRAIN<br /><small>ε / %</small></button><button className={mapMode === "pl" ? "active" : ""} onClick={() => setMapMode("pl")} role="radio" aria-checked={mapMode === "pl"}>PL SHIFT<br /><small>ΔE / meV</small></button><button className={mapMode === "raman" ? "active" : ""} onClick={() => setMapMode("raman")} role="radio" aria-checked={mapMode === "raman"}>RAMAN<br /><small>Δω / cm⁻¹</small></button></div><div className="qm-map-scale"><span>MAP SCALE</span><div><i /><i /><i /><i /><i /></div><small>{mapMode === "strain" ? "compressive ← tensile" : mapMode === "pl" ? "lower energy ← higher energy" : "downshift ← upshift"}</small></div><div className="qm-map-note"><ScanLine size={16} /><p>สนาม strain ใช้ Gaussian local-deformation proxy เพื่อสื่อแนวคิดของ wrinkle หรือ nanoindentation ไม่ใช่ strain tensor ที่ fit จากภาพจริง</p></div></aside><article className="qm-map-stage"><header><span><Crosshair size={14} /> 2D SPECTROSCOPY MAP</span><b>ACTIVE / {mapMode.toUpperCase()}</b></header><div className="qm-map-frame"><MappingHeatmap mode={mapMode} nominalStrain={strain} material={material} layers={layers} gateField={gateField} screening={screening} temperature={temperature} onProbe={selectProbe} probe={probe} /><div className="qm-map-crosshair"><span>X {probe.x.toFixed(0)}</span><span>Y {probe.y.toFixed(0)}</span></div></div><footer><span>click cell to place probe</span><span>map field follows current control stack</span></footer></article><aside className="qm-probe-readout"><span className="panel-index">D</span><p>LOCAL PROBE</p><h3>Point spectrum</h3><div className="qm-probe-coordinates"><span>POSITION</span><b>x {probe.x.toFixed(0)} · y {probe.y.toFixed(0)}</b></div><dl><div><dt>Local strain proxy</dt><dd>{probeStrain.toFixed(2)}%</dd></div><div><dt>Local PL proxy</dt><dd>{probeSpectroscopy.plEnergy.toFixed(3)} eV</dd></div><div><dt>PL shift</dt><dd>{probeSpectroscopy.plShiftMeV >= 0 ? "+" : ""}{probeSpectroscopy.plShiftMeV.toFixed(1)} meV</dd></div><div><dt>{probeSpectroscopy.primaryLabel}</dt><dd>{probeSpectroscopy.ramanPrimary.toFixed(1)} cm⁻¹</dd></div></dl><div className="qm-probe-mini"><PLStrainPlot currentEnergy={probeSpectroscopy.plEnergy} referenceEnergy={probeSpectroscopy.plReferenceEnergy} width={probeSpectroscopy.plWidth} intensity={probeSpectroscopy.plIntensity} /></div><p className="qm-probe-question"><Lightbulb size={15} /> ถ้า PL และ Raman map ให้ pattern ไม่สอดคล้องกัน ควรตั้งสมมติฐานเรื่องอะไรเพิ่มเติม?</p></aside></div><div className="qm-mapping-footer"><span>INTERPRETATION RULE / a map is a spatial hypothesis; confirm with calibration, fitting quality, acquisition conditions and complementary measurements.</span><span>LOCAL RESPONSE / {material.label} · {layers}L · T {temperature} K</span></div></section>

      <section className="qm-learning-strip"><div><p className="section-kicker">EVIDENCE CHECK</p><h2>จาก virtual model<br />สู่การวัดจริง</h2></div><div className="qm-evidence-flow"><article><span>CONTROL</span><b>layers / strain / gate</b></article><i>→</i><article><span>VIRTUAL RESPONSE</span><b>gap / exciton / μ</b></article><i>→</i><article><span>MEASUREMENT</span><b>PL, Raman, transport, ARPES*</b></article><i>→</i><article><span>VALIDATION</span><b>uncertainty + device context</b></article></div><p>* เลือกเครื่องมือให้สอดคล้องกับ observable ที่ต้องการยืนยัน</p></section>
    </main>
    <footer className="lab-footer"><span>2D MATERIALS & QUANTUM MATERIALS · semi-empirical teaching lab</span><span>layers / strain / gate / dielectric / temperature</span><span>Conceptual model — not a substitute for measured or first-principles data</span></footer>
  </div>;
}
