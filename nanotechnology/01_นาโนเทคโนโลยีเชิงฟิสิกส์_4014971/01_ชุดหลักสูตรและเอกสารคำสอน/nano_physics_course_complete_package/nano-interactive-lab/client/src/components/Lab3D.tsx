/**
 * Design: Instrument Garden — measured 3D lattice viewer with navy data, amber atoms, and sage evidence labels.
 */
import { useEffect, useMemo, useRef, useState } from "react";
import { Box, Move3D, Rotate3D } from "lucide-react";

type Structure = "SC" | "BCC" | "FCC";

type Lab3DProps = {
  structure: Structure;
  latticeConstant: number;
  onStructureChange: (structure: Structure) => void;
  onLatticeConstantChange: (value: number) => void;
};

const STRUCTURE_DETAILS: Record<Structure, { name: string; coordination: number; packing: number; points: [number, number, number][] }> = {
  SC: { name: "Simple Cubic", coordination: 6, packing: 0.52, points: [[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1]] },
  BCC: { name: "Body-Centered Cubic", coordination: 8, packing: 0.68, points: [[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1],[0,0,0]] },
  FCC: { name: "Face-Centered Cubic", coordination: 12, packing: 0.74, points: [[-1,-1,-1],[-1,-1,1],[-1,1,-1],[-1,1,1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,1],[0,0,-1],[0,0,1],[0,-1,0],[0,1,0],[-1,0,0],[1,0,0]] },
};

function projectPoint([x, y, z]: [number, number, number], angleX: number, angleY: number, scale: number) {
  const cy = Math.cos(angleY); const sy = Math.sin(angleY);
  const cx = Math.cos(angleX); const sx = Math.sin(angleX);
  const x1 = x * cy - z * sy;
  const z1 = x * sy + z * cy;
  const y1 = y * cx - z1 * sx;
  const z2 = y * sx + z1 * cx;
  const perspective = 1 / (3.2 - z2 * 0.5);
  return { x: x1 * scale * perspective, y: y1 * scale * perspective, z: z2 };
}

export function Lab3D({ structure, latticeConstant, onStructureChange, onLatticeConstantChange }: Lab3DProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const drag = useRef({ active: false, x: 0, y: 0 });
  const [rotation, setRotation] = useState({ x: -0.48, y: 0.7 });
  const [autoRotate, setAutoRotate] = useState(true);
  const details = STRUCTURE_DETAILS[structure];
  const visiblePoints = useMemo(() => details.points, [details.points]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const context = canvas.getContext("2d");
    if (!context) return;
    let frame = 0;
    const render = () => {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      if (canvas.width !== Math.round(rect.width * dpr) || canvas.height !== Math.round(rect.height * dpr)) {
        canvas.width = Math.round(rect.width * dpr); canvas.height = Math.round(rect.height * dpr);
      }
      context.setTransform(dpr, 0, 0, dpr, 0, 0);
      context.clearRect(0, 0, rect.width, rect.height);
      const midpoint = { x: rect.width / 2, y: rect.height / 2 };
      const scale = Math.min(rect.width, rect.height) * 0.72;
      const projected = visiblePoints.map((point) => projectPoint(point, rotation.x, rotation.y, scale));
      const sorted = projected.map((point, index) => ({ ...point, index })).sort((a, b) => a.z - b.z);

      context.strokeStyle = "rgba(16, 44, 66, 0.20)";
      context.lineWidth = 1;
      for (let i = 0; i < projected.length; i += 1) {
        for (let j = i + 1; j < projected.length; j += 1) {
          const a = visiblePoints[i]; const b = visiblePoints[j];
          const distance = Math.hypot(a[0] - b[0], a[1] - b[1], a[2] - b[2]);
          if (distance <= 2.05) {
            context.beginPath(); context.moveTo(midpoint.x + projected[i].x, midpoint.y + projected[i].y);
            context.lineTo(midpoint.x + projected[j].x, midpoint.y + projected[j].y); context.stroke();
          }
        }
      }
      sorted.forEach((point) => {
        const radius = Math.max(7, 13 + point.z * 2.4);
        const gradient = context.createRadialGradient(midpoint.x + point.x - radius * 0.35, midpoint.y + point.y - radius * 0.4, 1, midpoint.x + point.x, midpoint.y + point.y, radius);
        gradient.addColorStop(0, "#fff3d9"); gradient.addColorStop(0.42, "#e88a2a"); gradient.addColorStop(1, "#9f4e0d");
        context.fillStyle = gradient; context.beginPath(); context.arc(midpoint.x + point.x, midpoint.y + point.y, radius, 0, Math.PI * 2); context.fill();
        context.strokeStyle = "rgba(255,255,255,0.62)"; context.stroke();
      });
      if (autoRotate && !drag.current.active) setRotation((current) => ({ ...current, y: current.y + 0.006 }));
      frame = requestAnimationFrame(render);
    };
    frame = requestAnimationFrame(render);
    return () => cancelAnimationFrame(frame);
  }, [visiblePoints, rotation, autoRotate]);

  const dragStart = (clientX: number, clientY: number) => { drag.current = { active: true, x: clientX, y: clientY }; };
  const dragMove = (clientX: number, clientY: number) => {
    if (!drag.current.active) return;
    const dx = clientX - drag.current.x; const dy = clientY - drag.current.y;
    drag.current = { active: true, x: clientX, y: clientY };
    setRotation((current) => ({ x: current.x + dy * 0.012, y: current.y + dx * 0.012 }));
  };
  const dragEnd = () => { drag.current.active = false; };

  return (
    <section className="lab-module" aria-labelledby="lab-3d-title">
      <div className="module-heading">
        <div>
          <p className="eyebrow">03D / สำรวจโครงสร้างผลึก</p>
          <h2 id="lab-3d-title">มองโครงข่ายผลึกจากหลายมุม</h2>
        </div>
        <div className="model-chip"><Box size={15} /> หมุนภาพจำลองด้วยการลาก</div>
      </div>

      <div className="lab-grid three-d-grid">
        <div className="control-stack">
          <div className="control-block">
            <div className="control-label"><span>โครงสร้างตัวอย่าง</span><strong>{structure}</strong></div>
            <div className="structure-tabs" role="group" aria-label="เลือกโครงสร้างผลึก">
              {(Object.keys(STRUCTURE_DETAILS) as Structure[]).map((item) => (
                <button className={structure === item ? "active" : ""} key={item} onClick={() => onStructureChange(item)}>{item}</button>
              ))}
            </div>
            <p className="control-hint">{details.name}</p>
          </div>
          <div className="control-block">
            <div className="control-label"><span>ค่าคงที่โครงผลึก</span><strong>{latticeConstant.toFixed(2)} Å</strong></div>
            <input aria-label="ค่าคงที่โครงผลึก" type="range" min="2.5" max="5.5" step="0.05" value={latticeConstant} onChange={(event) => onLatticeConstantChange(Number(event.target.value))} />
            <div className="range-caption"><span>2.50 Å</span><span>5.50 Å</span></div>
          </div>
          <button className="motion-toggle" onClick={() => setAutoRotate((value) => !value)}><Rotate3D size={16} /> {autoRotate ? "หยุดการหมุนอัตโนมัติ" : "เริ่มการหมุนอัตโนมัติ"}</button>
        </div>

        <div className="crystal-view" aria-label="ภาพจำลองผลึกสามมิติ">
          <div className="axis-label x">x</div><div className="axis-label y">y</div><div className="axis-label z">z</div>
          <canvas
            ref={canvasRef}
            onPointerDown={(event) => { event.currentTarget.setPointerCapture(event.pointerId); dragStart(event.clientX, event.clientY); }}
            onPointerMove={(event) => dragMove(event.clientX, event.clientY)}
            onPointerUp={dragEnd}
            onPointerCancel={dragEnd}
          />
          <div className="canvas-legend"><Move3D size={14} /> ลากเพื่อเปลี่ยนมุมมอง</div>
        </div>

        <aside className="readout-panel">
          <div className="readout-title"><Box size={17} /> พารามิเตอร์โครงสร้าง</div>
          <dl className="structure-data">
            <div><dt>จำนวนเพื่อนบ้านใกล้สุด</dt><dd>{details.coordination}</dd></div>
            <div><dt>Atomic packing factor</dt><dd>{details.packing.toFixed(2)}</dd></div>
            <div><dt>lattice constant</dt><dd>{latticeConstant.toFixed(2)} Å</dd></div>
          </dl>
          <div className="inference-card sage">
            <p><strong>คำถามทดลอง:</strong> โครงสร้างใดบรรจุอะตอมได้หนาแน่นกว่า และคุณต้องมีข้อมูลใดเพิ่มจึงจะอธิบายสมบัติทางกลหรือไฟฟ้าได้อย่างน่าเชื่อถือ?</p>
          </div>
        </aside>
      </div>
    </section>
  );
}
