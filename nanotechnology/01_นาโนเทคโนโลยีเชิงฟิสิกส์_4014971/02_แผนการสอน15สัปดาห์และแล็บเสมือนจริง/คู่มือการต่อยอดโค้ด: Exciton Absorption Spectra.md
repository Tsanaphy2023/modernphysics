# คู่มือการต่อยอดโค้ด: Exciton Absorption Spectra

## แนวคิดสำคัญ

โค้ดเดิมคำนวณ effective band gap ของ quantum dot ด้วยสมการ Brus แต่การจำลอง **exciton absorption spectrum** ต้องเพิ่มองค์ประกอบอีกสามส่วน ได้แก่ ระดับพลังงานของ exciton, oscillator strength ของแต่ละ transition และรูปทรงของเส้นสเปกตรัมที่มี linewidth หรือ broadening

ใน quantum dot การกักขังของ electron และ hole ทำให้พลังงานของ continuum สูงขึ้นเมื่อขนาดอนุภาคลดลง ส่วนแรงดึงดูด Coulomb ระหว่าง electron กับ hole ทำให้เกิดสถานะ bound exciton ต่ำกว่าขอบ continuum แบบจำลองนี้สอดคล้องกับภาพรวมของ quantum well, quantum wire และ quantum dot ที่มี density of states และ optical transition แตกต่างกันตามมิติของระบบ [1]

> **ข้อควรย้ำในการบรรยาย:** โค้ดนี้เป็นแบบจำลองเชิงการสอนสำหรับแสดงแนวโน้ม ไม่ใช่การคำนวณ optical spectrum แบบ many-body ที่รวมทุก interaction ของวัสดุจริง

## 1. จาก band gap เดียวสู่ absorption spectrum

เดิมโค้ดให้ค่าพลังงานเพียงค่าเดียว คือ

```text
Eg(R) = Eg_bulk + Econf_e(R) + Econf_h(R) - Ecoul(R)
```

การสร้าง spectrum ต้องเปลี่ยนจาก “ค่าพลังงานจุดเดียว” เป็นฟังก์ชันของพลังงานโฟตอน โดยกำหนดตำแหน่งของ exciton peak และนำ line shape มาวางที่ตำแหน่งนั้น

แบบจำลองในไฟล์ใหม่ใช้พลังงานของ continuum ก่อนหัก exciton binding เป็น

```text
E_continuum(R) = Eg_bulk + Econf_e(R) + Econf_h(R)
```

จากนั้นใช้ exciton series แบบ hydrogenic อย่างง่าย

```text
E_n(R) = E_continuum(R) - E_binding(R)/n^2
```

โดย `n = 1` สอดคล้องกับสถานะ 1s ที่มีพลังงานต่ำสุด และแบบจำลองกำหนด oscillator strength อย่างง่ายเป็น `f_n proportional to 1/n^3` ดังนั้น peak ของ `n = 1` จึงเด่นที่สุด

## 2. การสร้างเส้น absorption peak

ในโค้ดใช้ Lorentzian line shape

```text
L(E) = [Gamma/pi] / [(E - E0)^2 + Gamma^2]
```

โดย `E0` คือพลังงานของ exciton transition และ `Gamma = FWHM/2` เป็นตัวแทนของ homogeneous broadening เช่น lifetime broadening หรือ interaction บางชนิดที่ทำให้เส้นไม่เป็น delta function

ในทางปฏิบัติ อาจใช้ Gaussian แทน Lorentzian เพื่อสาธิต broadening จากความไม่สม่ำเสมอของตัวอย่าง หรือใช้ Voigt profile หากต้องการรวมทั้ง homogeneous และ inhomogeneous broadening

## 3. ความหมายของฟังก์ชันหลักในไฟล์ใหม่

| ฟังก์ชัน | หน้าที่ |
|---|---|
| `single_particle_continuum_eV()` | คำนวณขอบพลังงานของ electron–hole continuum ก่อนหัก Coulomb correction |
| `coulomb_correction_eV()` | คำนวณ Coulomb correction แบบ Brus ซึ่งใช้เป็น effective binding/correction |
| `exciton_levels_eV()` | สร้างพลังงานของ exciton states เช่น 1s, 2s และ 3s |
| `lorentzian()` | สร้างรูปทรงของ absorption line ที่มี linewidth |
| `exciton_absorption_spectrum()` | รวม exciton peaks และ continuum tail เป็น spectrum ของ quantum dot เดี่ยว |
| `ensemble_absorption_spectrum()` | เฉลี่ย spectrum ของ quantum dots หลายขนาดเพื่อแสดง inhomogeneous broadening |
| `make_exciton_figure()` | สร้างกราฟ 4 แผงสำหรับใช้ในการบรรยาย |

## 4. การอ่านกราฟทั้ง 4 แผง

แผงซ้ายบนเปรียบเทียบ quantum dots หลายขนาด เมื่อรัศมีเล็กลง peak จะเลื่อนไปทางพลังงานสูงขึ้น ซึ่งเป็น blue shift จาก quantum confinement

แผงขวาบนแสดง exciton series สำหรับ quantum dot ขนาดเดียว โดยมี peak `n = 1` เด่นที่สุด ตามด้วยสถานะที่มี oscillator strength ลดลง และมีเส้นประสีแดงแสดง continuum onset

แผงซ้ายล่างแสดงผลของ size distribution หากตัวอย่างมีอนุภาคหลายขนาด peak จะกว้างขึ้นและรูปร่างไม่แหลมเท่าตัวอย่าง monodisperse การกระจายขนาดนี้เป็นตัวอย่างของ inhomogeneous broadening

แผงขวาล่างแสดงพร้อมกันว่า 1s exciton energy, continuum onset และ binding energy เปลี่ยนไปอย่างไรเมื่อขนาด quantum dot เปลี่ยน

## 5. วิธีใช้ในชั้นเรียน 60–75 นาที

| ช่วงเวลา | กิจกรรม |
|---|---|
| 10 นาที | ทบทวนว่า electron–hole pair และ exciton ต่างจาก free electron–hole continuum อย่างไร |
| 15 นาที | ให้นักศึกษาคำนวณ `E_continuum`, `E_binding` และ `E_1s` ด้วยมือสำหรับ `R = 2.5 nm` |
| 15 นาที | รันโค้ดและตรวจสอบว่าตำแหน่ง peak ตรงกับค่าที่คำนวณหรือไม่ |
| 15 นาที | เปลี่ยน `linewidth_meV` และอภิปรายความแตกต่างระหว่าง peak ที่แคบกับ peak ที่กว้าง |
| 10 นาที | เปลี่ยน `radius_sigma_nm` ใน ensemble spectrum เพื่อสาธิต inhomogeneous broadening |
| 10 นาที | วิเคราะห์ว่าข้อใดเป็นผลจาก quantum confinement และข้อใดเป็นผลจาก disorder ของตัวอย่าง |
| 5 นาที | เขียน exit ticket โดยแยก “ผลที่แบบจำลองทำนาย” กับ “ผลที่ต้องตรวจสอบด้วยการทดลอง” |

## 6. ตัวอย่างการปรับพารามิเตอร์

### เปลี่ยนขนาด quantum dot และ linewidth

```python
energy_grid = np.linspace(1.6, 3.6, 2600)

spectrum, metadata = exciton_absorption_spectrum(
    energy_grid_eV=energy_grid,
    radius_nm=2.5,
    material=MATERIAL,
    n_max=4,
    linewidth_meV=15.0,
    include_continuum=True,
)
```

เมื่อ `linewidth_meV` ลดลง peak จะคมขึ้น แต่ควรอธิบายว่านี่เป็นการปรับความละเอียดของแบบจำลอง ไม่ได้หมายความว่าตัวอย่างจริงมี lifetime ยาวขึ้นโดยอัตโนมัติ

### เปรียบเทียบตัวอย่างที่มีการกระจายขนาด

```python
spectrum, metadata = ensemble_absorption_spectrum(
    energy_grid_eV=energy_grid,
    mean_radius_nm=2.5,
    radius_sigma_nm=0.40,
    material=MATERIAL,
    n_dots=81,
    n_max=1,
    linewidth_meV=22.0,
    include_continuum=False,
)
```

ค่าของ `radius_sigma_nm` เป็นส่วนเบี่ยงเบนมาตรฐานของการกระจายรัศมีในแบบจำลอง หากเพิ่มค่านี้ peak จะกว้างขึ้นเนื่องจาก quantum dots แต่ละขนาดมี transition energy ต่างกัน

### ทดลองเปลี่ยนวัสดุ

```python
INP = {
    "name": "วัสดุตัวอย่าง",
    "Eg_bulk_eV": 1.42,
    "m_e_eff": 0.067,
    "m_h_eff": 0.50,
    "relative_permittivity": 12.4,
}

make_exciton_figure(INP, output_file="example_material_exciton.png")
```

ควรให้นักศึกษาค้นค่าพารามิเตอร์จากแหล่งอ้างอิงที่เหมาะสมก่อนใช้เปรียบเทียบกับข้อมูลจริง เพราะ effective mass และ dielectric constant ขึ้นกับวัสดุ โครงสร้างผลึก อุณหภูมิ และนิยามที่ใช้ในแบบจำลอง

## 7. คำถามเชิงลึกสำหรับการอภิปราย

1. เหตุใด `E_continuum` จึงสูงขึ้นเมื่อ quantum dot มีขนาดเล็กลง
2. เหตุใด exciton peak จึงอยู่ต่ำกว่า continuum onset
3. เมื่อ `R` ลดลง พลังงาน confinement มีแนวโน้มเปลี่ยนตาม `1/R^2` แต่ Coulomb correction มีแนวโน้มเปลี่ยนตาม `1/R` ผลนี้มีความหมายอย่างไร
4. ถ้าเพิ่ม dielectric constant ของวัสดุ binding energy จะเพิ่มหรือลดลง และเหตุใด
5. ทำไมการเพิ่ม size distribution จึงทำให้ peak กว้าง แม้ linewidth ของ quantum dot แต่ละอนุภาคจะคงเดิม
6. การใช้ Lorentzian หรือ Gaussian line shape แต่ละแบบเหมาะกับ broadening ประเภทใด
7. ข้อมูล absorption peak เพียงอย่างเดียวเพียงพอหรือไม่ที่จะยืนยัน quantum confinement ควรใช้ข้อมูลใดเสริม เช่น TEM, XRD, photoluminescence หรือ time-resolved spectroscopy

## 8. ข้อจำกัดและแนวทางต่อยอด

แบบจำลองนี้ใช้ effective-mass approximation และ Coulomb correction แบบง่าย จึงไม่รวม dielectric mismatch ระหว่าง quantum dot กับ ligand/matrix, surface polarization, finite confinement barrier, strain, alloy disorder, atomistic band structure, exchange interaction, phonon-assisted transitions และ many-body effects ในการทดลองจริง

หากต้องการยกระดับต่อไป สามารถเพิ่ม temperature-dependent band gap ด้วย Varshni equation, ใช้ Voigt profile, สร้าง absorption spectrum จากชุดข้อมูลจริง, เพิ่ม oscillator strength ที่ขึ้นกับขนาด และเปรียบเทียบ absorption กับ photoluminescence ซึ่งอาจมี Stokes shift และกลไก broadening ต่างกัน

สำหรับการสอนควรให้ผู้เรียนเปรียบเทียบสามระดับของแบบจำลอง ได้แก่ particle-in-a-box, Brus model และ exciton absorption spectrum แล้วอธิบายว่าแต่ละระดับเพิ่มฟิสิกส์ส่วนใดเข้ามาและยังละเลยอะไรอยู่

## เอกสารอ้างอิง

[1] Beard, M. C. et al. [*Quantum-confinement in Si and Ge nanostructures*](https://pubs.aip.org/aip/apr/article/1/1/011302/123949/Quantum-confinement-in-Si-and-Ge-nanostructures). *APL Materials*.

[2] Wolf, E. L. [*Nanophysics and Nanotechnology: An Introduction to Modern Concepts in Nanoscience*](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527618972). Wiley-VCH.

[3] nanoHUB. [*Simulation, Education, and Community for Nanotechnology*](https://nanohub.org/).
