# สถาปัตยกรรม Nano Materials Virtual Laboratory

> เอกสารนี้กำหนดขอบเขตเชิงการสอนของแพลตฟอร์ม ไม่ใช่คู่มือปฏิบัติการจริงหรือข้อกำหนดด้านความปลอดภัยของห้องปฏิบัติการ

## หลักการจัดกลุ่ม

ศูนย์เครื่องมือวัสดุศาสตร์จริงมักจัดเครื่องมือเป็นชุดที่ตอบคำถามต่างชนิดกัน ได้แก่ **โครงสร้าง ผลึก องค์ประกอบ เคมีพื้นผิว สัณฐาน/ภูมิประเทศ สมบัติทางแสง ไฟฟ้า แม่เหล็ก และกระบวนการสร้างวัสดุ** [1] [2] แพลตฟอร์มนี้จึงแยกประสบการณ์เรียนรู้ออกเป็น “วิเคราะห์” และ “สร้าง” เพื่อให้นักศึกษาตามเส้นทาง specimen → process → measurement → interpretation ได้ครบวงจร

| กลุ่มโมดูล | เครื่องมือหลักในแพลตฟอร์ม | คำถามเชิงวัสดุศาสตร์ | ระดับการจำลอง |
| --- | --- | --- | --- |
| Surface & probe microscopy | AFM, MFM, STM, profilometer | ผิวขรุขระเพียงใด โดเมนแม่เหล็กอยู่ที่ใด | Interactive core สำหรับ AFM/MFM; catalog สำหรับเครื่องมืออื่น |
| Electron & ion microscopy | SEM, TEM, STEM, FIB-SEM, EDS, EELS, EBSD | อนุภาคมีขนาด รูปร่าง defect และองค์ประกอบอย่างไร | Interactive core สำหรับ SEM/TEM; guided catalog สำหรับส่วนขยาย |
| Diffraction & scattering | XRD, GI-XRD, SAXS/WAXS, electron diffraction | phase, lattice spacing และ crystallite size คืออะไร | Interactive core สำหรับ XRD |
| Spectroscopy & composition | Raman, FTIR, XPS, ToF-SIMS, UV-Vis, PL | มีพันธะ ธาตุ สถานะเคมี และ optical transition อะไร | Guided catalog + route สำหรับโมดูลถัดไป |
| Electrical, magnetic & mechanical | four-point probe, Hall, I–V, nanoindenter, VSM/PPMS, SQUID | การนำไฟฟ้า carrier, hysteresis และ modulus เปลี่ยนอย่างไร | Guided catalog + route สำหรับโมดูลถัดไป |
| Particle, porosity & thermal | DLS, zeta potential, BET, TGA/DSC | ขนาดในสารแขวนลอย ประจุผิว พื้นที่ผิว และ thermal stability เป็นอย่างไร | Guided catalog + route สำหรับโมดูลถัดไป |
| Synthesis, film growth & fabrication | wet synthesis, CVD/PECVD, ALD, PVD/sputter, evaporation, MBE/MOCVD, electrospinning, ball milling | จะสร้าง nanostructure และ thin film แบบใด | Guided process simulator/catalog |
| Patterning & post-processing | photolithography, EBL, nanoimprint, FIB milling, RIE/ICP, wet etch, lift-off, CMP, annealing | จะนิยาม pattern และถ่ายโอนลวดลายอย่างไร | Guided process simulator/catalog |

## โมดูลหลักของรุ่นนี้

| โมดูล | ตัวควบคุมที่จำลอง | ผลลัพธ์ทางการสอน | สิ่งที่ไม่ควรตีความเกินแบบจำลอง |
| --- | --- | --- | --- |
| AFM | scan size, feedback setpoint, roughness | height map, line profile, RMS roughness | ไม่ใช่ force field หรือ calibration ของ cantilever จริง |
| MFM | lift height, polarity, domain scale | magnetic contrast map และ line profile | ไม่ใช่ quantitative magnetic moment หรือ field inversion |
| SEM | accelerating voltage, working distance, magnification | particle image, edge/contrast proxy, size reading | ไม่ใช่ Monte Carlo electron–matter interaction |
| TEM | sample thickness, contrast, lattice spacing | transmission image, diffraction proxy, defect cue | ไม่ใช่ multislice simulation หรือ electron dose model |
| XRD | crystallite size, phase, background | diffractogram, peak position, FWHM trend | ไม่ใช่ Rietveld refinement หรือ instrument calibration |

## การอ้างอิงสำหรับ taxonomy

[1] [UC San Diego Institute for Materials Discovery and Design — Facilities and Instrumentation](https://imdd.ucsd.edu/facilities): ระบุการใช้ XRD, XPS, Hall, UV-Vis, AFM/MFM และ SEM เพื่อวัดสมบัติผลึก แม่เหล็ก พื้นผิว การขนส่ง และเชิงแสง

[2] [University of Virginia Nanoscale Materials Characterization Facility — Instrumentation](https://engineering.virginia.edu/NMCF): ระบุการวิเคราะห์โครงสร้าง องค์ประกอบ และ defect ด้วย XRD, XPS, AFM, FT-IR/Raman, SEM และ HR-S/TEM

[3] [Harvard Center for Nanoscale Systems — Nanofabrication](https://cns1.rc.fas.harvard.edu/nanofabrication/): ระบุกลุ่มเทคโนโลยี lithography, CVD/ALD/PVD, etching และ metrology สำหรับสร้างและตรวจวัดโครงสร้างนาโน

[4] [Notre Dame Nanofabrication Facility — Equipment](https://nanofabrication.nd.edu/facilities/equipment/): แสดงตัวอย่างการจัดกลุ่มอุปกรณ์ lithography, deposition, etching, thermal process, planarization และ characterization ใน cleanroom

## ส่วนขยาย: โมดูล Spectrum Fitting

โมดูล Raman, XPS และ UV-Vis ใช้เพื่อฝึกแยกความหมายของ **peak position, line width, amplitude และ baseline** จากกัน โดยให้ผู้เรียนเห็นว่าเส้น fit ไม่ใช่หลักฐานอัตโนมัติหากสมมติฐานของแบบจำลองไม่เหมาะสม คู่มือ XPS เชิงปฏิบัติชี้ว่า peak fitting ต้องพิจารณาคุณภาพข้อมูลและสมมติฐานอย่างระมัดระวัง [5] ดังนั้น UI จะแสดงคำเตือนว่าเป็น *conceptual spectrum model* และไม่ใช่ผลการวิเคราะห์เพื่อรายงานค่าจริง

| โมดูล | แกน x เชิงการสอน | จุดเน้นของ fit | ขอบเขตที่ตั้งใจไม่จำลอง |
| --- | --- | --- | --- |
| Raman | Raman shift (cm⁻¹) | peak position, FWHM, relative intensity | calibration ของ laser, fluorescence correction และ deconvolution แบบวิจัยจริง |
| XPS | binding energy (eV) | chemical-state peak, baseline และ component area | charge correction, spin-orbit constraints, satellite structure และ quantification จริง |
| UV-Vis | wavelength (nm) | absorption maximum, linewidth และ absorbance baseline | instrument response, scattering correction และ Tauc fitting เชิงปริมาณ |

[5] [Practical Guides for X-Ray Photoelectron Spectroscopy (XPS)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6774202/): แหล่งอ้างอิงเกี่ยวกับการวิเคราะห์ XPS และประเด็น peak fitting (หน้าบทความอาจต้องผ่านการตรวจสอบเบราว์เซอร์)

[6] [UT Austin Materials Analysis and Spectroscopy Facility](https://tmi.utexas.edu/facilities/materials-analysis-and-spectroscopy-facility): ตัวอย่างศูนย์เครื่องมือที่ให้บริการ absorption/fluorescence spectrometers, Raman spectroscopy, FTIR และการวิเคราะห์วัสดุร่วมกัน
