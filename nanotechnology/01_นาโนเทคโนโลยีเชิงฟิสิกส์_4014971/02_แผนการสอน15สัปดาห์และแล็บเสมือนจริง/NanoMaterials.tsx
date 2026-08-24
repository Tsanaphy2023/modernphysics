/**
 * Precision Instrument Console — Nano Materials Lab extends the original dark observation stage,
 * warm analysis surfaces, and phosphor-lime active states into a multi-instrument learning hub.
 */
import { Link } from "wouter";
import { useMemo, useState } from "react";
import "./NanoMaterials.css";
import {
  Activity,
  ArrowLeft,
  Atom,
  Beaker,
  Binoculars,
  CircleGauge,
  Crosshair,
  Disc3,
  FlaskConical,
  Layers3,
  Microscope,
  MoveDiagonal2,
  Orbit,
  Play,
  ScanLine,
  Sparkles,
  Waves,
  Zap,
} from "lucide-react";
import { toast } from "sonner";

type InstrumentId = "afm" | "mfm" | "sem" | "tem" | "xrd" | SpectralInstrumentId;
type SpectralInstrumentId = "raman" | "xps" | "uvvis";
type LineShape = "gaussian" | "lorentzian" | "voigt";
type FitParameters = { center: number; fwhm: number; amplitude: number; baseline: number; lineShape: LineShape };
type SpectrumConfig = { label: string; subtitle: string; axis: string; unit: string; min: number; max: number; center: number; fwhm: number; amplitude: number; baseline: number; secondaryCenter: number; secondaryAmplitude: number; peakLabel: string; icon: typeof Disc3; lineShape: LineShape };

type CoreInstrument = {
  id: InstrumentId;
  code: string;
  title: string;
  subtitle: string;
  family: string;
  icon: typeof Microscope;
  image: string;
  goal: string;
  control: { label: string; min: number; max: number; step: number; unit: string; initial: number };
  signals: [string, string, string];
};

const heroImage = "/manus-storage/nanolab-instrument-hub-hero_18eec310.png";
const afmImage = "/manus-storage/nanolab-afm-mfm-stage_00c75b2f.png";
const electronImage = "/manus-storage/nanolab-electron-microscopy-stage_336c176f.png";
const xrdImage = "/manus-storage/nanolab-xrd-stage_437e17c5.png";
const labLogoImage = "/manus-storage/nanolab-calibration-logo_831cda46.png";

const spectrumConfigs: Record<SpectralInstrumentId, SpectrumConfig> = {
  raman: { label: "Raman", subtitle: "Vibrational band fitting", axis: "Raman shift", unit: "cm⁻¹", min: 1150, max: 1750, center: 1350, fwhm: 72, amplitude: .78, baseline: .08, secondaryCenter: 1586, secondaryAmplitude: .46, peakLabel: "vibrational band", icon: Disc3, lineShape: "lorentzian" },
  xps: { label: "XPS", subtitle: "Chemical-state peak fitting", axis: "Binding energy", unit: "eV", min: 526, max: 537, center: 531.1, fwhm: 1.7, amplitude: .76, baseline: .10, secondaryCenter: 532.9, secondaryAmplitude: .28, peakLabel: "chemical-state peak", icon: Sparkles, lineShape: "voigt" },
  uvvis: { label: "UV-Vis", subtitle: "Optical absorption fitting", axis: "Wavelength", unit: "nm", min: 360, max: 780, center: 522, fwhm: 92, amplitude: .70, baseline: .06, secondaryCenter: 415, secondaryAmplitude: .16, peakLabel: "absorption maximum", icon: Waves, lineShape: "gaussian" },
};

const lineShapeOptions: { id: LineShape; label: string; note: string }[] = [
  { id: "gaussian", label: "Gaussian", note: "symmetric core" },
  { id: "lorentzian", label: "Lorentzian", note: "broader wings" },
  { id: "voigt", label: "Voigt", note: "pseudo-Voigt mix" },
];

const coreInstruments: CoreInstrument[] = [
  { id: "afm", code: "01", title: "AFM", subtitle: "Atomic Force Microscopy", family: "SURFACE / TOPOGRAPHY", icon: ScanLine, image: afmImage, goal: "สแกน height map และอ่านค่า roughness ของฟิล์มนาโน", control: { label: "Scan size", min: 80, max: 800, step: 20, unit: "nm", initial: 320 }, signals: ["RMS roughness", "Peak-to-valley", "Line profile"] },
  { id: "mfm", code: "02", title: "MFM", subtitle: "Magnetic Force Microscopy", family: "MAGNETIC / DOMAINS", icon: Orbit, image: afmImage, goal: "สังเกต contrast ของ magnetic domains ที่ความสูงยกหัววัดต่างกัน", control: { label: "Lift height", min: 15, max: 160, step: 5, unit: "nm", initial: 55 }, signals: ["Phase contrast", "Domain spacing", "Signal decay"] },
  { id: "sem", code: "03", title: "SEM", subtitle: "Scanning Electron Microscopy", family: "ELECTRON / MORPHOLOGY", icon: Microscope, image: electronImage, goal: "ปรับเงื่อนไขลำอิเล็กตรอนเพื่ออ่าน morphology และขนาดอนุภาค", control: { label: "Accelerating voltage", min: 1, max: 25, step: 1, unit: "kV", initial: 8 }, signals: ["Edge contrast", "Particle diameter", "Depth cue"] },
  { id: "tem", code: "04", title: "TEM", subtitle: "Transmission Electron Microscopy", family: "ELECTRON / LATTICE", icon: Atom, image: electronImage, goal: "อ่าน transmission contrast, lattice fringe และ diffraction cue", control: { label: "Sample thickness", min: 10, max: 180, step: 5, unit: "nm", initial: 70 }, signals: ["Transmission", "d-spacing", "Defect cue"] },
  { id: "xrd", code: "05", title: "XRD", subtitle: "X-Ray Diffraction", family: "DIFFRACTION / PHASE", icon: Waves, image: xrdImage, goal: "เปรียบเทียบ peak position และ broadening ของ crystallite ขนาดต่างกัน", control: { label: "Crystallite size", min: 4, max: 80, step: 2, unit: "nm", initial: 20 }, signals: ["2θ peak", "FWHM", "Phase match"] },
  { id: "raman", code: "06", title: "Raman", subtitle: "Vibrational Spectroscopy", family: "SPECTRUM / VIBRATION", icon: Disc3, image: afmImage, goal: "ปรับ peak model เพื่อแยกตำแหน่ง band ความกว้าง และ relative intensity", control: { label: "Fit control", min: 0, max: 1, step: .1, unit: "a.u.", initial: 1 }, signals: ["Band center", "FWHM", "Peak assignment"] },
  { id: "xps", code: "07", title: "XPS", subtitle: "X-Ray Photoelectron Spectroscopy", family: "SPECTRUM / CHEMISTRY", icon: Sparkles, image: electronImage, goal: "ฝึกแยก chemical-state component ออกจาก background ด้วย peak fitting", control: { label: "Fit control", min: 0, max: 1, step: .1, unit: "a.u.", initial: 1 }, signals: ["Binding energy", "Component area", "Chemical state"] },
  { id: "uvvis", code: "08", title: "UV-Vis", subtitle: "Optical Absorption", family: "SPECTRUM / OPTICS", icon: Waves, image: xrdImage, goal: "เชื่อม absorption maximum และ linewidth กับแบบจำลองสเปกตรัม", control: { label: "Fit control", min: 0, max: 1, step: .1, unit: "a.u.", initial: 1 }, signals: ["Absorption max", "Band width", "Optical transition"] },
];

const catalog = [
  { group: "SURFACE & PROBE", icon: ScanLine, tools: ["STM", "Optical profiler", "Stylus profilometer", "Contact angle", "KPFM", "c-AFM"] },
  { group: "ELECTRON & ION", icon: Microscope, tools: ["STEM", "FIB-SEM", "EDS / EDX", "EELS", "EBSD", "Cryo-EM"] },
  { group: "SPECTROSCOPY", icon: Sparkles, tools: ["FT-IR", "ToF-SIMS", "Photoluminescence", "Fluorescence lifetime"] },
  { group: "SCATTERING & THERMAL", icon: Waves, tools: ["GI-XRD", "SAXS / WAXS", "DLS", "Zeta potential", "BET", "TGA / DSC"] },
  { group: "ELECTRICAL & MAGNETIC", icon: Activity, tools: ["Four-point probe", "Hall effect", "I–V probe station", "Nanoindenter", "VSM", "SQUID / PPMS"] },
  { group: "SYNTHESIS & GROWTH", icon: Beaker, tools: ["Wet colloidal synthesis", "Hydrothermal", "CVD / PECVD", "ALD", "Sputter PVD", "Evaporation", "MBE / MOCVD", "Electrospinning", "Ball milling", "Annealing"] },
  { group: "PATTERNING & PROCESS", icon: Layers3, tools: ["Photolithography", "E-beam lithography", "Nanoimprint", "FIB milling", "RIE / ICP", "Wet etch", "Lift-off", "CMP"] },
];

function gaussian(x: number, center: number, width: number, amplitude: number) {
  return amplitude * Math.exp(-((x - center) ** 2) / (2 * width ** 2));
}

function lorentzian(x: number, center: number, fwhm: number, amplitude: number) {
  return amplitude / (1 + 4 * ((x - center) / fwhm) ** 2);
}

function lineProfile(shape: LineShape, x: number, center: number, fwhm: number, amplitude: number) {
  if (shape === "gaussian") return gaussian(x, center, fwhm / 2.355, amplitude);
  if (shape === "lorentzian") return lorentzian(x, center, fwhm, amplitude);
  // Pseudo-Voigt provides a computationally lightweight Gaussian/Lorentzian mixture for conceptual fitting.
  return .55 * lorentzian(x, center, fwhm, amplitude) + .45 * gaussian(x, center, fwhm / 2.355, amplitude);
}

function isSpectralInstrument(id: InstrumentId): id is SpectralInstrumentId {
  return id === "raman" || id === "xps" || id === "uvvis";
}

type SpectrumPoint = { t: number; raw: number; fit: number; component: number; residual: number };

function buildSpectrumSeries(instrument: SpectralInstrumentId, parameters: FitParameters): SpectrumPoint[] {
  const config = spectrumConfigs[instrument];
  return Array.from({ length: 150 }, (_, index) => {
    const t = index / 149;
    const x = config.min + t * (config.max - config.min);
    const raw = config.baseline + lineProfile(config.lineShape, x, config.center, config.fwhm, config.amplitude) + lineProfile(config.lineShape, x, config.secondaryCenter, config.fwhm, config.secondaryAmplitude) + Math.sin(index * 1.77) * .018;
    const fit = parameters.baseline + lineProfile(parameters.lineShape, x, parameters.center, parameters.fwhm, parameters.amplitude) + lineProfile(config.lineShape, x, config.secondaryCenter, config.fwhm, config.secondaryAmplitude);
    const component = parameters.baseline + lineProfile(parameters.lineShape, x, parameters.center, parameters.fwhm, parameters.amplitude);
    return { t, raw, fit, component, residual: raw - fit };
  });
}

function residualSummary(instrument: SpectralInstrumentId, parameters: FitParameters) {
  const series = buildSpectrumSeries(instrument, parameters);
  const mean = series.reduce((total, point) => total + point.residual, 0) / series.length;
  const rmse = Math.sqrt(series.reduce((total, point) => total + point.residual ** 2, 0) / series.length);
  const maxAbs = Math.max(...series.map((point) => Math.abs(point.residual)));
  return { mean, rmse, maxAbs };
}

function SpectrumFitPlot({ instrument, parameters }: { instrument: SpectralInstrumentId; parameters: FitParameters }) {
  const config = spectrumConfigs[instrument];
  const series = buildSpectrumSeries(instrument, parameters);
  const toPoints = (value: keyof Pick<SpectrumPoint, "raw" | "fit" | "component"> | "baseline") => series.map((point) => {
    const signal = value === "baseline" ? parameters.baseline : point[value];
    return `${(6 + point.t * 90).toFixed(2)},${(91 - signal * 67).toFixed(2)}`;
  }).join(" ");

  return <svg className="signal-svg spectrum-signal" viewBox="0 0 100 100" role="img" aria-label={`${instrument} conceptual spectrum with adjustable fitted model`}><path d="M5 91H97M5 9V91" className="signal-axis" /><polyline points={toPoints("baseline")} className="spectrum-baseline" /><polyline points={toPoints("raw")} className="spectrum-raw" /><polyline points={toPoints("component")} className="spectrum-component" /><polyline points={toPoints("fit")} className="spectrum-fit" /><text x="6" y="14">SIGNAL</text><text x="57" y="98">{config.axis}</text></svg>;
}

function ResidualPlot({ instrument, parameters }: { instrument: SpectralInstrumentId; parameters: FitParameters }) {
  const config = spectrumConfigs[instrument];
  const series = buildSpectrumSeries(instrument, parameters);
  const summary = residualSummary(instrument, parameters);
  const scale = Math.max(summary.maxAbs * 1.25, .025);
  const points = series.map((point) => `${(6 + point.t * 90).toFixed(2)},${(50 - (point.residual / scale) * 34).toFixed(2)}`).join(" ");
  return <div className="residual-panel"><div className="residual-panel-head"><span>RESIDUAL / measured − fitted</span><b>RMSE {summary.rmse.toFixed(3)} a.u.</b></div><svg className="residual-svg" viewBox="0 0 100 100" role="img" aria-label={`${instrument} residual plot`}><path d="M5 50H97M5 13V87" className="residual-axis" /><path d="M5 50H97" className="residual-zero" /><polyline points={points} className="residual-line" /><text x="6" y="16">+</text><text x="6" y="87">−</text><text x="57" y="98">{config.axis}</text></svg><div className="residual-foot"><span>zero reference</span><span>max |r| {summary.maxAbs.toFixed(3)} a.u.</span><span>mean {summary.mean.toFixed(3)} a.u.</span></div></div>;
}

function fitQuality(instrument: SpectralInstrumentId, parameters: FitParameters) {
  const config = spectrumConfigs[instrument];
  const centerPenalty = Math.abs(parameters.center - config.center) / (config.max - config.min) * 70;
  const widthPenalty = Math.abs(parameters.fwhm - config.fwhm) / config.fwhm * 32;
  const amplitudePenalty = Math.abs(parameters.amplitude - config.amplitude) * 35;
  const baselinePenalty = Math.abs(parameters.baseline - config.baseline) * 55;
  const shapePenalty = parameters.lineShape === config.lineShape ? 0 : 12;
  return Math.max(0, Math.min(99.8, 98.6 - centerPenalty - widthPenalty - amplitudePenalty - baselinePenalty - shapePenalty));
}

function InstrumentSignal({ instrument, value, runCount }: { instrument: CoreInstrument; value: number; runCount: number }) {
  const seed = runCount * 0.09;
  if (instrument.id === "xrd") {
    const size = value;
    const width = Math.max(0.34, 2.9 / Math.sqrt(size));
    const points = Array.from({ length: 150 }, (_, index) => {
      const x = index / 149;
      const angle = 20 + x * 52;
      const signal = 0.04 + gaussian(angle, 28.4, width, 0.72) + gaussian(angle, 38.7, width * 1.12, 0.54) + gaussian(angle, 56.9, width * .9, 0.88);
      return `${(x * 100).toFixed(2)},${(91 - signal * 72).toFixed(2)}`;
    }).join(" ");
    return <svg className="signal-svg xrd-signal" viewBox="0 0 100 100" role="img" aria-label="Conceptual XRD diffractogram"><path d="M4 90H98M4 9V90" className="signal-axis" /><polyline points={points} className="signal-line" /><text x="5" y="15">INTENSITY</text><text x="75" y="98">2θ</text></svg>;
  }

  if (instrument.id === "tem") {
    const dots = Array.from({ length: 64 }, (_, index) => {
      const col = index % 8;
      const row = Math.floor(index / 8);
      const x = 17 + col * 10 + (row % 2 ? 4 : 0);
      const y = 17 + row * 9;
      const opacity = 0.26 + (((index * 17) % 7) / 11);
      return <circle key={index} cx={x} cy={y} r={2.3} fill={`rgba(237,247,233,${opacity})`} />;
    });
    return <svg className="signal-svg tem-signal" viewBox="0 0 100 100" role="img" aria-label="Conceptual TEM transmission image"><rect width="100" height="100" fill="#101b28" />{dots}<path d="M12 78 C32 59, 52 91, 88 35" className="defect-line" /><path d="M16 18H35M16 18V37" className="scale-line" /><text x="16" y="45">5 nm</text></svg>;
  }

  if (instrument.id === "sem") {
    const particles = Array.from({ length: 26 }, (_, index) => {
      const x = 9 + ((index * 31) % 83);
      const y = 11 + ((index * 19) % 76);
      const r = 2.5 + ((index * 11) % 8) / 2;
      return <circle key={index} cx={x} cy={y} r={r} fill={`rgba(229,239,235,${0.2 + (index % 5) * .12})`} stroke="rgba(199,243,107,.46)" strokeWidth=".45" />;
    });
    return <svg className="signal-svg sem-signal" viewBox="0 0 100 100" role="img" aria-label="Conceptual SEM micrograph"><rect width="100" height="100" fill="#101b28" />{particles}<path d="M64 90H90" className="scale-line" /><text x="64" y="84">100 nm</text></svg>;
  }

  const isMfm = instrument.id === "mfm";
  const cells = Array.from({ length: 144 }, (_, index) => {
    const col = index % 12;
    const row = Math.floor(index / 12);
    const signal = Math.sin(col * .78 + seed) * Math.cos(row * .55 - seed) + (isMfm ? Math.sin((col + row) * .45) : .18 * Math.sin(row * 2));
    const lightness = 22 + (signal + 2) * 17;
    const hue = isMfm ? (signal > 0 ? 93 : 205) : 185 - signal * 15;
    return <rect key={index} x={col * 8.34} y={row * 8.34} width="8.6" height="8.6" fill={`hsl(${hue} 48% ${lightness}%)`} />;
  });
  return <svg className="signal-svg scan-signal" viewBox="0 0 100 100" role="img" aria-label={isMfm ? "Conceptual MFM magnetic contrast map" : "Conceptual AFM topography map"}>{cells}<path d="M12 87H36" className="scale-line" /><text x="12" y="80">{instrument.id === "afm" ? `${Math.round(value / 8)} nm` : "domain"}</text></svg>;
}

function measurementFor(instrument: InstrumentId, value: number) {
  if (instrument === "afm") return [`${(0.18 + 60 / value).toFixed(2)} nm`, `${(0.72 + 148 / value).toFixed(2)} nm`, "height map"];
  if (instrument === "mfm") return [`${(1.18 * Math.exp(-value / 130)).toFixed(2)}°`, `${(40 + value * .62).toFixed(0)} nm`, "phase contrast"];
  if (instrument === "sem") return [`${(1.6 + value * .22).toFixed(1)} nm`, `${(22 + value * 4.3).toFixed(0)} k×`, "edge response"];
  if (instrument === "tem") return [`${(0.19 + value / 900).toFixed(3)} nm`, `${(88 - value * .22).toFixed(0)}%`, "transmission"];
  return [`${(0.22 + 2.75 / Math.sqrt(value)).toFixed(2)}°`, `${(28.4 + (value % 8) * .02).toFixed(2)}°`, "peak FWHM"];
}

export default function NanoMaterials() {
  const [selectedId, setSelectedId] = useState<InstrumentId>("afm");
  const selected = coreInstruments.find((instrument) => instrument.id === selectedId) ?? coreInstruments[0];
  const [settings, setSettings] = useState<Record<InstrumentId, number>>(() => Object.fromEntries(coreInstruments.map((instrument) => [instrument.id, instrument.control.initial])) as Record<InstrumentId, number>);
  const [runCount, setRunCount] = useState(1);
  const [fitSettings, setFitSettings] = useState<Record<SpectralInstrumentId, FitParameters>>({
    raman: { center: spectrumConfigs.raman.center, fwhm: spectrumConfigs.raman.fwhm, amplitude: spectrumConfigs.raman.amplitude, baseline: spectrumConfigs.raman.baseline, lineShape: spectrumConfigs.raman.lineShape },
    xps: { center: spectrumConfigs.xps.center, fwhm: spectrumConfigs.xps.fwhm, amplitude: spectrumConfigs.xps.amplitude, baseline: spectrumConfigs.xps.baseline, lineShape: spectrumConfigs.xps.lineShape },
    uvvis: { center: spectrumConfigs.uvvis.center, fwhm: spectrumConfigs.uvvis.fwhm, amplitude: spectrumConfigs.uvvis.amplitude, baseline: spectrumConfigs.uvvis.baseline, lineShape: spectrumConfigs.uvvis.lineShape },
  });
  const value = settings[selected.id];
  const metrics = useMemo(() => measurementFor(selected.id, value), [selected.id, value]);
  const selectedSpectrumId = isSpectralInstrument(selectedId) ? selectedId : null;
  const isSpectral = selectedSpectrumId !== null;
  const selectedSpectrum = selectedSpectrumId ? spectrumConfigs[selectedSpectrumId] : null;
  const activeFit = selectedSpectrumId ? fitSettings[selectedSpectrumId] : null;
  const quality = selectedSpectrumId && activeFit ? fitQuality(selectedSpectrumId, activeFit) : 0;
  const residualMetrics = selectedSpectrumId && activeFit ? residualSummary(selectedSpectrumId, activeFit) : null;

  const chooseInstrument = (id: InstrumentId) => {
    setSelectedId(id);
    setRunCount((count) => count + 1);
  };

  const runSimulation = () => {
    setRunCount((count) => count + 1);
    toast.success(`อัปเดตสัญญาณ ${selected.title} แล้ว`, { description: `ใช้ ${selected.control.label} = ${value} ${selected.control.unit} เป็นค่าเชิงการสอน` });
  };

  const updateFit = (parameter: keyof FitParameters, nextValue: FitParameters[keyof FitParameters]) => {
    if (!selectedSpectrumId) return;
    setFitSettings((previous) => ({ ...previous, [selectedSpectrumId]: { ...previous[selectedSpectrumId], [parameter]: nextValue } }));
  };

  const applyFit = () => {
    if (!selectedSpectrumId || !activeFit) return;
    setRunCount((count) => count + 1);
    toast.success(`อัปเดต ${selected.title} fit แล้ว`, { description: `${activeFit.lineShape} profile · conceptual match score ${quality.toFixed(1)}% — ตรวจสมมติฐานของ peak model ก่อนตีความ` });
  };

  const resetFit = () => {
    if (!selectedSpectrumId) return;
    const config = spectrumConfigs[selectedSpectrumId];
    setFitSettings((previous) => ({ ...previous, [selectedSpectrumId]: { center: config.center, fwhm: config.fwhm, amplitude: config.amplitude, baseline: config.baseline, lineShape: config.lineShape } }));
    toast(`คืนค่า ${selected.title} fitting model แล้ว`);
  };

  return (
    <div className="materials-shell">
      <header className="lab-header materials-header">
        <div className="materials-brand-group">
          <Link href="/" className="brand-lockup" aria-label="กลับสู่ Nanophysics Virtual Lab 01">
            <span className="brand-specimen-mark"><img className="brand-mark" src={labLogoImage} alt="Nanophysics Virtual Lab mark" /><i aria-hidden="true"><b /><b /><b /></i></span>
            <span><strong>NANOPHYSICS</strong><em>VIRTUAL LAB / 01</em></span>
          </Link>
          <span className="module-route-label">MODULE / NANO MATERIALS</span>
        </div>
        <div className="header-status"><span className="status-dot" /><span>SIMULATION CATALOG ONLINE</span><span className="header-divider" /><span>CORE / {String(coreInstruments.length).padStart(2, "0")}</span></div>
        <div className="header-actions"><Link href="/stm-sts" className="header-action"><Zap size={16} /> STM / STS Lab</Link><Link href="/quantum-materials" className="header-action"><Atom size={16} /> 2D + Quantum Lab</Link><Link href="/" className="header-action"><ArrowLeft size={16} /> Lab 01 Geometry</Link></div>
      </header>

      <main>
        <section className="materials-hero" style={{ backgroundImage: `linear-gradient(90deg, rgba(7,17,32,.98), rgba(7,17,32,.84) 44%, rgba(7,17,32,.50)), url(${heroImage})` }}>
          <div className="materials-hero-copy">
            <p className="eyebrow"><FlaskConical size={15} /> NANO MATERIALS LABORATORY</p>
            <h1>สร้าง · วัด · ตีความ<br />วัสดุนาโน</h1>
            <p>สำรวจ workflow ตั้งแต่การสังเคราะห์และสร้าง thin film ไปจนถึง microscopy, diffraction, spectroscopy และการวัดสมบัติผ่านโมดูลจำลองเชิงการสอน</p>
            <div className="materials-hero-stats"><span><b>08</b> interactive core instruments</span><span><b>03</b> spectrum-fitting modules</span><span><b>50+</b> tools in learning catalog</span></div>
          </div>
          <div className="materials-hero-evidence" aria-hidden="true">
            <div><span>SPECIMEN / 07</span><b>CALIBRATED TRACE</b></div>
            <svg viewBox="0 0 330 190"><g className="hero-evidence-grid"><path d="M0 38H330M0 76H330M0 114H330M0 152H330M55 0V190M110 0V190M165 0V190M220 0V190M275 0V190" /></g><polyline points="8,140 36,131 58,144 82,108 105,118 131,70 153,85 181,46 201,63 230,37 255,52 285,24 323,33" /><circle cx="181" cy="46" r="4" /></svg>
            <small>SCAN MAP · DIFFRACTION · CONTRAST</small>
          </div>
          <div className="materials-route"><span>SPECIMEN</span><i /><span>PROCESS</span><i /><span>MEASURE</span><i /><b>INTERPRET</b></div>
        </section>

        <section className="instrument-selector-section">
          <div className="section-intro"><p className="section-kicker">INTERACTIVE CORE</p><h2>เลือกเครื่องมือ แล้วปรับตัวแปรเพื่ออ่านสัญญาณ</h2><p>ผลลัพธ์เป็น signal model สำหรับสร้าง intuition ทางฟิสิกส์ ไม่ใช่ข้อมูลแทนการสอบเทียบเครื่องมือจริง</p></div>
          <div className="calibration-strip"><span>RACK / CORE INSTRUMENTS</span><i /><span>08 MODULES</span><i /><span>LIVE SIGNAL MODELS</span><i /><span>FITTING ENABLED</span></div>
          <div className="instrument-strip">
            {coreInstruments.map((instrument) => {
              const Icon = instrument.icon;
              return <button key={instrument.id} onClick={() => chooseInstrument(instrument.id)} className={selectedId === instrument.id ? "instrument-choice active" : "instrument-choice"} aria-pressed={selectedId === instrument.id}><span className="instrument-number">RACK / {instrument.code}</span><Icon size={22} /><strong>{instrument.title}</strong><small>{instrument.family}</small><small className="instrument-observable">OBS / {instrument.signals[0]}</small></button>;
            })}
          </div>
        </section>

        <section className="instrument-workbench" aria-label="Instrument simulation workbench">
          <aside className="instrument-control-panel">
            <div className="instrument-panel-title"><span className="panel-index">A</span><div><p>METHOD SETUP</p><h2>{selected.title}</h2><span>{selected.subtitle}</span></div></div>
            <div className="instrument-photo" style={{ backgroundImage: `linear-gradient(135deg, rgba(7,17,32,.12), rgba(7,17,32,.72)), url(${selected.image})` }} />
            <p className="instrument-goal">{selected.goal}</p>
            {isSpectral && selectedSpectrum && activeFit ? <div className="fit-controls" aria-label="Spectrum fitting controls">
              <div className="fit-control-title"><span>FIT PARAMETERS</span><b>CONCEPTUAL MODEL</b></div>
              <div className="line-shape-control"><div><span>LINE SHAPE</span><b>{activeFit.lineShape === "voigt" ? "PSEUDO-VOIGT" : activeFit.lineShape.toUpperCase()}</b></div><div className="line-shape-options" role="radiogroup" aria-label="เลือกรูปแบบเส้นโค้ง"><span className="shape-guide">CORE</span>{lineShapeOptions.map((option) => <button key={option.id} className={activeFit.lineShape === option.id ? "shape-choice active" : "shape-choice"} role="radio" aria-checked={activeFit.lineShape === option.id} onClick={() => updateFit("lineShape", option.id)}><b>{option.label}</b><small>{option.note}</small></button>)}</div><p>{activeFit.lineShape === "gaussian" ? "Gaussian: สาธิตเส้นพีกสมมาตรที่มีหางลดลงรวดเร็ว" : activeFit.lineShape === "lorentzian" ? "Lorentzian: สาธิตพีกที่มี wings กว้างกว่า Gaussian" : "Voigt: pseudo-Voigt แบบผสม Gaussian/Lorentzian เพื่อฝึกตีความ broadening ที่ซ้อนกัน"}</p></div>
              <div className="fit-slider"><div><label htmlFor="fit-center">Peak position</label><output>{activeFit.center.toFixed(selected.id === "xps" ? 1 : 0)} {selectedSpectrum.unit}</output></div><input id="fit-center" type="range" min={selectedSpectrum.min + (selectedSpectrum.max - selectedSpectrum.min) * .18} max={selectedSpectrum.max - (selectedSpectrum.max - selectedSpectrum.min) * .18} step={selected.id === "xps" ? .1 : 1} value={activeFit.center} onChange={(event) => updateFit("center", Number(event.target.value))} /></div>
              <div className="fit-slider"><div><label htmlFor="fit-width">FWHM</label><output>{activeFit.fwhm.toFixed(selected.id === "xps" ? 1 : 0)} {selectedSpectrum.unit}</output></div><input id="fit-width" type="range" min={selected.id === "xps" ? .4 : 18} max={selected.id === "xps" ? 5 : selected.id === "raman" ? 150 : 190} step={selected.id === "xps" ? .1 : 1} value={activeFit.fwhm} onChange={(event) => updateFit("fwhm", Number(event.target.value))} /></div>
              <div className="fit-slider"><div><label htmlFor="fit-amplitude">Peak amplitude</label><output>{activeFit.amplitude.toFixed(2)} a.u.</output></div><input id="fit-amplitude" type="range" min="0.1" max="1.2" step="0.02" value={activeFit.amplitude} onChange={(event) => updateFit("amplitude", Number(event.target.value))} /></div>
              <div className="fit-slider"><div><label htmlFor="fit-baseline">Baseline</label><output>{activeFit.baseline.toFixed(2)} a.u.</output></div><input id="fit-baseline" type="range" min="0" max="0.32" step="0.01" value={activeFit.baseline} onChange={(event) => updateFit("baseline", Number(event.target.value))} /></div>
              <button className="run-simulation" onClick={applyFit}><Play size={16} fill="currentColor" /> Apply spectrum fit</button><button className="fit-reset" onClick={resetFit}>คืนค่า target model</button>
            </div> : <><div className="instrument-slider"><div><label htmlFor="instrument-control">{selected.control.label}</label><output>{value} {selected.control.unit}</output></div><input id="instrument-control" type="range" min={selected.control.min} max={selected.control.max} step={selected.control.step} value={value} onChange={(event) => setSettings((previous) => ({ ...previous, [selected.id]: Number(event.target.value) }))} /><div className="range-ends"><span>{selected.control.min} {selected.control.unit}</span><span>{selected.control.max} {selected.control.unit}</span></div></div><button className="run-simulation" onClick={runSimulation}><Play size={16} fill="currentColor" /> Run conceptual scan</button></>}
            <p className="simulation-disclaimer"><CircleGauge size={15} /> {isSpectral ? "fit model ใช้ฝึกอ่านแนวโน้มเท่านั้น ไม่ใช่ผลวิเคราะห์เชิงปริมาณหรือ calibration จริง" : "สัญญาณนี้ออกแบบเพื่อฝึกอ่านแนวโน้มและเชื่อมโยงตัวแปรกับผลวัด"}</p>
          </aside>

          <article className="instrument-stage">
            <div className="instrument-stage-top"><span><Crosshair size={14} /> {isSpectral ? "SPECTRUM FITTING WORKBENCH" : "LIVE SIGNAL VIEWER"}</span><span>RUN {String(runCount).padStart(2, "0")}</span></div>
            <div className="signal-frame">{selectedSpectrumId && activeFit ? <div className="spectrum-frame"><SpectrumFitPlot instrument={selectedSpectrumId} parameters={activeFit} /><div className="spectrum-legend"><span><i className="raw" /> measured model</span><span><i className="fit" /> fitted envelope</span><span><i className="component" /> selected {activeFit.lineShape} component</span></div><ResidualPlot instrument={selectedSpectrumId} parameters={activeFit} /></div> : <InstrumentSignal instrument={selected} value={value} runCount={runCount} />}</div>
            <div className="signal-caption"><div><span>MODE</span><b>{selected.family}</b></div><div><span>{isSpectral ? "PEAK" : "CONTROL"}</span><b>{selectedSpectrum && activeFit ? `${activeFit.center.toFixed(selected.id === "xps" ? 1 : 0)} ${selectedSpectrum.unit}` : `${selected.control.label}: ${value} ${selected.control.unit}`}</b></div><div><span>{isSpectral ? "LINE SHAPE" : "OUTPUT"}</span><b>{activeFit ? activeFit.lineShape.toUpperCase() : selected.signals[2]}</b></div></div>
          </article>

          <aside className="instrument-metrics">
            <div className="instrument-panel-title"><span className="panel-index">B</span><div><p>READOUT</p><h2>สัญญาณที่สังเกต</h2><span>conceptual output</span></div></div>
            {selectedSpectrum && activeFit && residualMetrics ? <><div className="metric-highlight"><span>FIT MATCH SCORE</span><strong>{quality.toFixed(1)}<small>%</small></strong><i /></div><dl className="instrument-dl"><div><dt>Line shape</dt><dd>{activeFit.lineShape === "voigt" ? "pseudo-Voigt" : activeFit.lineShape}</dd></div><div><dt>{selectedSpectrum.peakLabel}</dt><dd>{activeFit.center.toFixed(selected.id === "xps" ? 1 : 0)} {selectedSpectrum.unit}</dd></div><div><dt>FWHM</dt><dd>{activeFit.fwhm.toFixed(selected.id === "xps" ? 1 : 0)} {selectedSpectrum.unit}</dd></div><div><dt>Baseline</dt><dd>{activeFit.baseline.toFixed(2)} a.u.</dd></div></dl><div className="residual-readout"><span>RESIDUAL SUMMARY</span><div><b>RMSE</b><strong>{residualMetrics.rmse.toFixed(3)}</strong></div><div><b>MAX |r|</b><strong>{residualMetrics.maxAbs.toFixed(3)}</strong></div></div><div className="student-prompt"><Binoculars size={17} /><p><b>สังเกต:</b> หาก residual เบี่ยงจากศูนย์เป็นรูปแบบชัดเจน ให้ทบทวน line shape หรือจำนวน component ก่อนสรุปผล</p></div></> : <><div className="metric-highlight"><span>{selected.signals[0]}</span><strong>{metrics[0]}</strong><i /></div><dl className="instrument-dl"><div><dt>{selected.signals[1]}</dt><dd>{metrics[1]}</dd></div><div><dt>Interpretation</dt><dd>{metrics[2]}</dd></div><div><dt>Confidence cue</dt><dd>{selected.id === "xrd" ? "peak width" : "contrast trend"}</dd></div></dl><div className="student-prompt"><Binoculars size={17} /><p><b>สังเกต:</b> ปรับค่าให้สุดช่วง แล้วบันทึกว่าสัญญาณใดเปลี่ยน และข้อสรุปใดที่ยังต้องยืนยันด้วยเครื่องมือชนิดอื่น</p></div></>}
          </aside>
        </section>

        <section className="interpretation-section">
          <div className="section-intro"><p className="section-kicker">MEASUREMENT LITERACY</p><h2>เครื่องมือหนึ่งชนิด ตอบคำถามได้ไม่ครบทุกมิติ</h2></div>
          <div className="calibration-strip warm-strip"><span>EVIDENCE / TRIANGULATION</span><i /><span>STRUCTURE</span><i /><span>COMPOSITION</span><i /><span>PROPERTY</span></div>
          <div className="triangulation-grid"><article><span>01</span><h3>Surface & morphology</h3><p>AFM และ SEM แสดงภูมิประเทศหรือรูปร่าง แต่ต้องตั้งคำถามต่อว่า contrast มีที่มาอย่างไร</p></article><article><span>02</span><h3>Structure & phase</h3><p>TEM และ XRD ให้ข้อมูลโครงสร้างคนละสเกล จึงใช้ตรวจสอบข้อสรุปร่วมกันได้</p></article><article><span>03</span><h3>Composition & properties</h3><p>XPS, Raman, EDS, Hall และ optical methods เป็นโมดูลเสริมที่เชื่อมองค์ประกอบกับสมบัติ</p></article></div>
        </section>

        <section className="catalog-section">
          <div className="catalog-heading"><div><p className="section-kicker catalog-kicker">EXPANDABLE LEARNING CATALOG</p><h2>เครื่องมือวัสดุศาสตร์นาโนที่เกี่ยวข้อง</h2><p>รายการต่อไปนี้จัดเป็นเส้นทางพัฒนาห้องทดลองเสมือนจริง ให้ครอบคลุมการวิเคราะห์ การสังเคราะห์ และการสร้างอุปกรณ์นาโน</p></div><span className="catalog-badge">{catalog.reduce((count, item) => count + item.tools.length, 0)} SUPPORTING TOOLS</span></div>
          <div className="calibration-strip catalog-strip"><span>INSTRUMENT RACK / 07</span><i /><span>METHOD → OBSERVABLE → EVIDENCE</span></div>
          <div className="catalog-grid">{catalog.map((section, index) => { const Icon = section.icon; return <article key={section.group} className="catalog-card"><div><Icon size={21} /><span>{section.group}</span><b>RACK / {String(index + 1).padStart(2, "0")}</b></div><p className="catalog-evidence">WHAT THIS RACK CAN PROVE</p><ul>{section.tools.map((tool) => <li key={tool}>{tool}</li>)}</ul><button onClick={() => toast(`วางแผนโมดูล ${section.group} ไว้ใน catalog แล้ว`)}>ดู workflow ที่จะเพิ่ม <MoveDiagonal2 size={14} /></button></article>; })}</div>
        </section>

        <section className="materials-protocol"><div><p className="section-kicker">CROSS-TECHNIQUE CHALLENGE</p><h2>ออกแบบชุดการวัด<br />ไม่ใช่แค่เลือกเครื่องมือ</h2></div><div className="challenge-flow"><span>Nanoparticle film</span><i>→</i><span>AFM: roughness</span><i>→</i><span>SEM: morphology</span><i>→</i><span>XRD: phase</span><i>→</i><span>TEM: lattice</span></div><p>คำถามสำหรับนักศึกษา: หลักฐานจากเครื่องมือใด “ยืนยัน” สมมติฐานได้ และหลักฐานใดเป็นเพียงข้อบ่งชี้?</p></section>
        <div className="materials-source-strip"><span>INSTRUMENT TAXONOMY / SOURCES</span><a href="https://imdd.ucsd.edu/facilities" target="_blank" rel="noreferrer">UCSD IMDD</a><a href="https://engineering.virginia.edu/NMCF" target="_blank" rel="noreferrer">UVA NMCF</a><a href="https://cns1.rc.fas.harvard.edu/nanofabrication/" target="_blank" rel="noreferrer">Harvard CNS</a></div>
      </main>
      <footer className="lab-footer"><span>NANO MATERIALS VIRTUAL LAB · core simulation models</span><span>AFM / MFM / SEM / TEM / XRD / RAMAN / XPS / UV-VIS</span><span>Use for conceptual learning, not experimental calibration</span></footer>
    </div>
  );
}
