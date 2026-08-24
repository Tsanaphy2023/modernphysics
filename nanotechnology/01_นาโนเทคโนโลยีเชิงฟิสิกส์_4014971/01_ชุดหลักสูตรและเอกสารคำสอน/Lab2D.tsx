/**
 * Design: Instrument Garden — scientific instrument panel with warm ivory, amber controls, navy data, and sage evidence.
 */
import { useMemo } from "react";
import { CircleDot, Gauge, Sparkles } from "lucide-react";

type Lab2DProps = {
  diameter: number;
  count: number;
  onDiameterChange: (value: number) => void;
  onCountChange: (value: number) => void;
};

export function Lab2D({ diameter, count, onDiameterChange, onCountChange }: Lab2DProps) {
  const ratio = 6 / diameter;
  const normalized = Math.min(100, Math.round(ratio * 1000));
  const particleSize = Math.max(18, Math.min(78, 86 - diameter * 0.62));
  const particles = useMemo(() => Array.from({ length: Math.min(count, 36) }, (_, index) => index), [count]);

  return (
    <section className="lab-module" aria-labelledby="lab-2d-title">
      <div className="module-heading">
        <div>
          <p className="eyebrow">02D / สำรวจอัตราส่วนพื้นผิว</p>
          <h2 id="lab-2d-title">อนุภาคทรงกลมและพื้นที่ผิวต่อปริมาตร</h2>
        </div>
        <div className="model-chip"><Sparkles size={15} /> แบบจำลองเชิงการเรียนรู้</div>
      </div>

      <div className="lab-grid two-d-grid">
        <div className="control-stack" aria-label="ตัวควบคุมการทดลอง 2D">
          <div className="control-block">
            <div className="control-label"><span>เส้นผ่านศูนย์กลาง</span><strong>{diameter} nm</strong></div>
            <input aria-label="เส้นผ่านศูนย์กลางอนุภาค" type="range" min="10" max="100" value={diameter} onChange={(event) => onDiameterChange(Number(event.target.value))} />
            <div className="range-caption"><span>10 nm</span><span>100 nm</span></div>
          </div>
          <div className="control-block">
            <div className="control-label"><span>จำนวนอนุภาคที่แสดง</span><strong>{count}</strong></div>
            <input aria-label="จำนวนอนุภาคที่แสดง" type="range" min="4" max="36" value={count} onChange={(event) => onCountChange(Number(event.target.value))} />
            <div className="range-caption"><span>4</span><span>36</span></div>
          </div>
          <div className="equation-note">
            <span className="equation-mark">S/V</span>
            <p>สำหรับทรงกลม <strong>S/V = 6/d</strong> เมื่อ <em>d</em> ใช้หน่วยเดียวกับค่า S/V</p>
          </div>
        </div>

        <div className="surface-view" aria-label="ภาพจำลองอนุภาค 2 มิติ">
          <div className="microscope-scale"><span>100 nm</span><i /></div>
          <div className="particle-stage">
            {particles.map((index) => (
              <span
                className="particle-2d"
                key={index}
                style={{
                  width: `${particleSize}px`, height: `${particleSize}px`,
                  left: `${8 + (index % 6) * 15 + ((index * 11) % 5)}%`,
                  top: `${10 + Math.floor(index / 6) * 17 + ((index * 7) % 4)}%`,
                  opacity: 0.62 + (index % 4) * 0.09,
                }}
              />
            ))}
            <div className="stage-caption">ภาพขยายเชิงแนวคิด — ไม่ใช่ภาพจากกล้องจุลทรรศน์จริง</div>
          </div>
        </div>

        <aside className="readout-panel" aria-label="ค่าที่คำนวณจากแบบจำลอง 2D">
          <div className="readout-title"><Gauge size={17} /> อ่านค่าจากแบบจำลอง</div>
          <div className="metric-main">
            <span>อัตราส่วน S/V</span>
            <strong>{ratio.toFixed(3)}</strong>
            <small>nm⁻¹</small>
          </div>
          <div className="indicator">
            <div className="indicator-top"><span>แนวโน้มพื้นที่ผิวจำเพาะ</span><b>{normalized}%</b></div>
            <div className="indicator-track"><span style={{ width: `${normalized}%` }} /></div>
          </div>
          <div className="inference-card">
            <CircleDot size={17} />
            <p><strong>ข้อสังเกต:</strong> เมื่อเส้นผ่านศูนย์กลางลดลง อัตราส่วน S/V เพิ่มขึ้น จึงอาจส่งผลต่อการแลกเปลี่ยนที่ผิว แต่ยังไม่เพียงพอที่จะสรุปอัตราการเกิดปฏิกิริยาจริงโดยไม่มีข้อมูลทดลอง</p>
          </div>
        </aside>
      </div>
    </section>
  );
}
