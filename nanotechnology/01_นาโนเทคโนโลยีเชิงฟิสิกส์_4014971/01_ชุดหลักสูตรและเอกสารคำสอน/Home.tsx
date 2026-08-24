/**
 * Design: Instrument Garden — a lab-bench layout with amber controls, navy measurements, sage evidence, and an ivory field notebook surface.
 */
import { useMemo, useState } from "react";
import { Archive, Beaker, BookOpenCheck, ChevronRight, CircleHelp, ClipboardPlus, Download, FlaskConical, RotateCcw, ShieldCheck } from "lucide-react";
import { Lab2D } from "@/components/Lab2D";
import { Lab3D } from "@/components/Lab3D";

type Structure = "SC" | "BCC" | "FCC";

type Observation = {
  id: number;
  module: "2D" | "3D";
  parameter: string;
  result: string;
};

const HERO_IMAGE = "/manus-storage/nano_lab_hero_aa327b37.jpg";
const MICROSCOPY_IMAGE = "/manus-storage/nano_lab_microscopy_1954475a.jpg";
const LOGO_IMAGE = "/manus-storage/nano_lab_logo_90ca7400.png";

export default function Home() {
  const [activeLab, setActiveLab] = useState<"2d" | "3d">("2d");
  const [diameter, setDiameter] = useState(30);
  const [count, setCount] = useState(18);
  const [structure, setStructure] = useState<Structure>("FCC");
  const [latticeConstant, setLatticeConstant] = useState(4.05);
  const [observations, setObservations] = useState<Observation[]>([]);

  const ratio2D = useMemo(() => `${(6 / diameter).toFixed(3)} nm⁻¹`, [diameter]);
  const packing = structure === "SC" ? "0.52" : structure === "BCC" ? "0.68" : "0.74";

  const addObservation = () => {
    const item: Observation = activeLab === "2d"
      ? { id: Date.now(), module: "2D", parameter: `d = ${diameter} nm, n = ${count}`, result: `S/V = ${ratio2D}` }
      : { id: Date.now(), module: "3D", parameter: `${structure}, a = ${latticeConstant.toFixed(2)} Å`, result: `APF = ${packing}` };
    setObservations((current) => [item, ...current].slice(0, 8));
  };

  const exportCsv = () => {
    const rows = [["module", "parameter", "result"], ...observations.map((item) => [item.module, item.parameter, item.result])];
    const blob = new Blob([rows.map((row) => row.map((cell) => `"${cell}"`).join(",")).join("\n")], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob); const anchor = document.createElement("a");
    anchor.href = url; anchor.download = "nano-lab-observations.csv"; anchor.click(); URL.revokeObjectURL(url);
  };

  const resetLab = () => {
    setDiameter(30); setCount(18); setStructure("FCC"); setLatticeConstant(4.05); setObservations([]); setActiveLab("2d");
  };

  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="#top" aria-label="Nano Physics Interactive Lab">
          <span className="brand-mark"><img src={LOGO_IMAGE} alt="" /><i /><i /></span>
          <span><b>NANO / PHYSICS</b><small>interactive lab</small></span>
        </a>
        <div className="topbar-status"><span className="pulse-dot" /> ห้องปฏิบัติการพร้อมใช้งาน <span className="status-separator" /> v1.0 · learning simulation</div>
        <a className="course-link" href="#guide"><BookOpenCheck size={16} /> คู่มือกิจกรรม</a>
      </header>

      <main id="top" className="lab-layout">
        <aside className="lab-sidebar" aria-label="เส้นทางการเรียนรู้">
          <div className="sidebar-kicker">LAB ROUTE</div>
          <nav>
            <button className={activeLab === "2d" ? "route-link active" : "route-link"} onClick={() => setActiveLab("2d")}><span>01</span><i><CircleHelp size={17} /> มาตราส่วนและพื้นผิว</i></button>
            <button className={activeLab === "3d" ? "route-link active" : "route-link"} onClick={() => setActiveLab("3d")}><span>02</span><i><FlaskConical size={17} /> โครงสร้างผลึก 3D</i></button>
            <a className="route-link" href="#guide"><span>03</span><i><ShieldCheck size={17} /> ตีความอย่างรับผิดชอบ</i></a>
          </nav>
          <div className="sidebar-note">
            <Beaker size={19} />
            <p><strong>หลักปฏิบัติ</strong> เปลี่ยนทีละตัวแปร บันทึกสิ่งที่เห็น และแยก “แบบจำลอง” ออกจาก “ข้อมูลทดลอง”</p>
          </div>
        </aside>

        <div className="workbench">
          <section className="hero-panel instrument-hero" aria-label="แผงเริ่มต้นการทดลอง" style={{ backgroundImage: `linear-gradient(90deg, rgba(253,250,244,.97) 0%, rgba(253,250,244,.91) 48%, rgba(253,250,244,.20) 100%), url(${HERO_IMAGE})` }}>
            <div className="hero-content">
              <div className="eyebrow"><span /> WORKSTATION 01 · COURSE LAB</div>
              <h1>ปรับตัวแปร<br /><em>สังเกตหลักฐาน</em><br />อธิบายอย่างมีเหตุผล</h1>
              <p>ห้องปฏิบัติการเชิงโต้ตอบสำหรับสำรวจความสัมพันธ์ระหว่างขนาด พื้นผิว โครงสร้าง และข้อจำกัดของการสรุปผลในระดับนาโน</p>
              <div className="hero-steps"><span><b>01</b> ตั้งค่า</span><ChevronRight size={15} /><span><b>02</b> สังเกต</span><ChevronRight size={15} /><span><b>03</b> บันทึก</span></div>
            </div>
            <div className="hero-meter" aria-label="สถานะเครื่องมือจำลอง">
              <div><small>MODE</small><b>SIMULATION</b></div>
              <div><small>UNITS</small><b>nm · Å · APF</b></div>
              <div><small>OUTPUT</small><b>FIELD NOTE</b></div>
            </div>
            <div className="hero-stamp"><b>2D / 3D</b><span>learning models</span></div>
          </section>

          <section className="module-tabs" aria-label="เลือกห้องปฏิบัติการ">
            <button className={activeLab === "2d" ? "active" : ""} onClick={() => setActiveLab("2d")}><span>LAB 01</span> 2D · Surface-to-Volume</button>
            <button className={activeLab === "3d" ? "active" : ""} onClick={() => setActiveLab("3d")}><span>LAB 02</span> 3D · Crystal Viewer</button>
          </section>

          {activeLab === "2d" ? (
            <Lab2D diameter={diameter} count={count} onDiameterChange={setDiameter} onCountChange={setCount} />
          ) : (
            <Lab3D structure={structure} latticeConstant={latticeConstant} onStructureChange={setStructure} onLatticeConstantChange={setLatticeConstant} />
          )}

          <section id="guide" className="guide-strip" style={{ backgroundImage: `linear-gradient(90deg, rgba(17,44,66,.97), rgba(17,44,66,.90)), url(${MICROSCOPY_IMAGE})` }}>
            <div><span className="eyebrow light">EVIDENCE NOTE</span><h2>แบบจำลองที่ดีไม่ใช่คำตอบสุดท้าย</h2><p>ใช้ผลจากหน้าจอนี้เพื่อสร้างสมมติฐาน แล้วระบุข้อมูลทดลอง เครื่องมือวัด และความไม่แน่นอนที่ยังต้องตรวจสอบก่อนตัดสินใจ</p></div>
            <div className="guide-prompts"><span>“ตัวแปรใดคงที่?”</span><span>“หลักฐานใดยังขาด?”</span><span>“ข้อสรุปนี้เกินข้อมูลหรือไม่?”</span></div>
          </section>
        </div>

        <aside className="notebook" aria-label="สมุดบันทึกการทดลอง">
          <div className="notebook-heading"><div><span className="eyebrow">FIELD NOTES</span><h2>บันทึกการสังเกต</h2></div><Archive size={20} /></div>
          <p className="notebook-intro">กดบันทึกหลังปรับตัวแปรแต่ละครั้ง แล้วใช้ไฟล์ CSV เป็นหลักฐานประกอบใบงาน Data Lab</p>
          <button className="save-observation" onClick={addObservation}><ClipboardPlus size={17} /> บันทึกค่าปัจจุบัน</button>
          <div className="observation-list">
            {observations.length === 0 ? (
              <div className="empty-notes"><span>ยังไม่มีบันทึก</span><p>เริ่มจากปรับค่าหนึ่งตัวแปร แล้วบันทึกสิ่งที่เปลี่ยนแปลง</p></div>
            ) : observations.map((item) => (
              <article className="note-entry" key={item.id}><span>{item.module}</span><p>{item.parameter}</p><strong>{item.result}</strong></article>
            ))}
          </div>
          <div className="notebook-actions">
            <button onClick={exportCsv} disabled={!observations.length}><Download size={16} /> CSV</button>
            <button onClick={resetLab}><RotateCcw size={16} /> เริ่มใหม่</button>
          </div>
          <div className="safety-footer"><ShieldCheck size={17} /><p>ไม่มีผลลัพธ์ใดในหน้านี้ใช้แทน SOP, SDS, การประเมินความเสี่ยง หรือข้อมูลจากการทดลองจริง</p></div>
        </aside>
      </main>
    </div>
  );
}
