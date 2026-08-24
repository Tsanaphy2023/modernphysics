# คู่มือการจำลอง Temperature-dependent Exciton Broadening

## วัตถุประสงค์การเรียนรู้

หลังทำกิจกรรม นักศึกษาควรสามารถอธิบายได้ว่าอุณหภูมิส่งผลต่อ exciton absorption spectrum อย่างน้อยสองทาง ได้แก่ **การเลื่อนตำแหน่งพลังงานของ peak** จาก temperature-dependent band gap และ **การเพิ่มความกว้างของ peak** จากการกระเจิงกับ phonons นอกจากนี้ควรแยกผลดังกล่าวออกจาก inhomogeneous broadening ที่เกิดจาก quantum dots มีขนาดไม่เท่ากัน

> **ประเด็นสำคัญ:** peak ที่เลื่อนไปกับอุณหภูมิและ peak ที่กว้างขึ้นเป็นคนละ observable ทางฟิสิกส์ การ fit spectrum ควรพิจารณาทั้ง peak position และ linewidth ไม่ใช่ดูเฉพาะความสูงของ peak

## 1. แบบจำลองที่เพิ่มเข้ามา

### 1.1 Temperature-dependent band gap

สคริปต์ใช้ Varshni-type model ในรูปแบบที่กำหนดให้ค่า band gap ที่อุณหภูมิอ้างอิงตรงกับค่าที่กำหนดไว้

```text
Eg(T) = Eg(Tref) + alpha*Tref^2/(Tref + beta)
                       - alpha*T^2/(T + beta)
```

เมื่ออุณหภูมิเพิ่มขึ้น แบบจำลองนี้ทำให้ band gap ลดลง และทำให้ exciton peak เลื่อนไปยังพลังงานต่ำลงหรือความยาวคลื่นยาวขึ้น

### 1.2 Temperature-dependent linewidth

ใช้แบบจำลองเชิงการสอน

```text
FWHM(T) = Gamma_res
          + a_acoustic*T
          + Gamma_LO*n_LO(T)
```

โดย

```text
n_LO(T) = 1/[exp(E_LO/(k_B*T)) - 1]
```

`Gamma_res` แทน broadening ที่เหลืออยู่เมื่ออุณหภูมิต่ำมาก เช่น disorder หรือ instrumental contribution ส่วน `a_acoustic*T` ใช้แทนแนวโน้ม broadening จาก acoustic phonons และเทอม `Gamma_LO*n_LO(T)` ใช้แทนการเพิ่มขึ้นของ optical-phonon population

แบบจำลองนี้เป็น phenomenological model สำหรับสาธิตแนวโน้ม ไม่ควรตีความว่าเป็น scattering theory ที่ครบถ้วนสำหรับ CdSe ทุกสภาวะ

## 2. ฟังก์ชันสำคัญในไฟล์

| ฟังก์ชัน | บทบาท |
|---|---|
| `varshni_term_eV()` | คำนวณเทอม Varshni |
| `bulk_bandgap_temperature_eV()` | คำนวณ band gap ของ bulk ตามอุณหภูมิ |
| `phonon_broadening_components_meV()` | แยก residual, acoustic และ optical-phonon contributions |
| `temperature_dependent_exciton_levels_eV()` | สร้าง exciton levels ที่รวมการเปลี่ยนของ band gap |
| `temperature_dependent_absorption_spectrum()` | สร้าง spectrum ที่ตำแหน่ง peak และ linewidth ขึ้นกับอุณหภูมิ |
| `make_temperature_figure()` | สร้างกราฟ 4 แผงสำหรับการบรรยาย |

## 3. การรันโค้ด

วางไฟล์ `quantum_confinement_exciton_spectra.py` และ `quantum_confinement_temperature_exciton.py` ไว้ในโฟลเดอร์เดียวกัน แล้วรัน

```bash
pip install numpy matplotlib
python quantum_confinement_temperature_exciton.py
```

สคริปต์จะสร้างไฟล์ `quantum_confinement_temperature_exciton.png` และพิมพ์ตารางค่า `Eg_bulk`, `1s peak`, `FWHM` และ wavelength ที่อุณหภูมิต่าง ๆ

## 4. การอ่านกราฟ 4 แผง

แผงซ้ายบนแสดง spectrum ที่อุณหภูมิต่างกัน เมื่ออุณหภูมิเพิ่มขึ้น peak จะเลื่อนไปทางพลังงานต่ำลงและกว้างขึ้น แผงขวาบนแยกองค์ประกอบของ linewidth เพื่อให้นักศึกษาเห็นว่า total FWHM ไม่ได้มาจาก phonon term เพียงอย่างเดียว

แผงซ้ายล่างเปรียบเทียบ 1s exciton peak, continuum onset และ bulk band gap ตามอุณหภูมิ ความแตกต่างระหว่าง exciton peak กับ continuum onset ในโค้ดนี้เป็น effective Coulomb correction ที่ถือว่าคงที่ตามอุณหภูมิ ส่วนแผงขวาล่างเป็น temperature–energy map ซึ่งเหมาะสำหรับอธิบายว่า spectral ridge เลื่อนและขยายตัวอย่างไร

## 5. กิจกรรมในชั้นเรียน 60–75 นาที

| เวลา | กิจกรรม |
|---|---|
| 10 นาที | ให้นักศึกษาทำนายทิศทางการเลื่อนของ peak และการเปลี่ยน linewidth เมื่ออุณหภูมิเพิ่ม |
| 15 นาที | คำนวณ `Eg(T)` และ `FWHM(T)` สำหรับ 10, 100 และ 300 K ด้วยมือหรือ spreadsheet |
| 15 นาที | รันโค้ดและเปรียบเทียบค่าที่คำนวณกับตารางผลลัพธ์ |
| 15 นาที | เปลี่ยน `acoustic_slope_meV_per_K`, `LO_phonon_energy_meV` และ `LO_coupling_meV` ทีละตัว แล้วอภิปรายผล |
| 10 นาที | ปิด temperature-dependent linewidth โดยกำหนด `linewidth_meV` คงที่ เพื่อแยก peak shift ออกจาก peak broadening |
| 10 นาที | ให้นักศึกษาอธิบายว่า broadening จากอุณหภูมิต่างจาก broadening จาก size distribution อย่างไร |
| 5 นาที | เขียน exit ticket พร้อมระบุ parameter ที่ควร fit จากข้อมูลทดลอง |

## 6. ตัวอย่างการปรับพารามิเตอร์

### เปลี่ยนความแรงของ acoustic-phonon broadening

```python
MATERIAL_T["acoustic_slope_meV_per_K"] = 0.050
```

ค่าที่มากขึ้นจะทำให้ FWHM เพิ่มเกือบเชิงเส้นกับอุณหภูมิในช่วงที่ acoustic term เด่น

### เปลี่ยน optical-phonon contribution

```python
MATERIAL_T["LO_phonon_energy_meV"] = 30.0
MATERIAL_T["LO_coupling_meV"] = 50.0
```

`LO_phonon_energy_meV` ควบคุมพลังงาน phonon ใน Bose occupation ส่วน `LO_coupling_meV` ควบคุมขนาดของ broadening ที่เกิดจากเทอมนี้

### แยกผลของ peak shift กับ thermal broadening

```python
spectrum, metadata = temperature_dependent_absorption_spectrum(
    energy_grid_eV=energy_grid,
    radius_nm=2.5,
    temperature_K=300.0,
    linewidth_meV=20.0,       # ค่าคงที่: ปิด phonon-dependent linewidth
    include_continuum=False,
)
```

เปรียบเทียบผลลัพธ์นี้กับกรณี `linewidth_meV=None` ซึ่งใช้ FWHM จาก phonon model โดยตรง

## 7. คำถามอภิปรายเชิงลึก

1. เหตุใด Varshni model จึงทำให้ exciton peak เลื่อนไปยังพลังงานต่ำลงเมื่ออุณหภูมิเพิ่มขึ้น
2. เหตุใด residual linewidth จึงไม่หายไปแม้ที่อุณหภูมิต่ำมาก
3. ในช่วงอุณหภูมิใด acoustic term มีแนวโน้มสำคัญกว่า optical-phonon term และดูได้จากกราฟใด
4. ถ้า peak เลื่อนไปแต่ไม่กว้างขึ้น จะสรุปได้หรือไม่ว่า phonon coupling ไม่มีอยู่
5. ถ้า peak กว้างขึ้นแต่ตำแหน่งไม่เลื่อน ควรตรวจสอบสาเหตุใดบ้าง
6. ข้อมูล absorption spectrum เพียงชุดเดียวที่ 300 K สามารถแยก homogeneous กับ inhomogeneous broadening ได้หรือไม่
7. หากต้อง fit ข้อมูลจริง ควร fit peak position และ FWHM แยกกันหรือใช้ global fit หลายอุณหภูมิ เพราะเหตุใด

## 8. ข้อจำกัดของแบบจำลอง

โค้ดนี้ใช้ Varshni equation และ linewidth model แบบ phenomenological โดยถือว่า effective mass, dielectric constant และ exciton binding correction ไม่เปลี่ยนตามอุณหภูมิ นอกจากนี้ยังไม่รวม temperature-dependent dielectric screening, exciton–phonon self-energy, carrier population, phonon sidebands, non-radiative channels, spectral asymmetry, Stokes shift และ phase transition ของวัสดุ

หากนำไปวิเคราะห์ข้อมูลจริง ควรใช้ค่าพารามิเตอร์จากวัสดุและ sample ที่สนใจ รวมถึงตรวจสอบหน่วย `eV`, `meV`, `K` ให้ชัดเจน ควร fit หลายอุณหภูมิพร้อมกัน และรายงาน uncertainty ของ `alpha`, `beta`, `Gamma_res`, acoustic slope และ LO coupling

## เอกสารอ้างอิง

[1] Beard, M. C. et al. [*Quantum-confinement in Si and Ge nanostructures*](https://pubs.aip.org/aip/apr/article/1/1/011302/123949/Quantum-confinement-in-Si-and-Ge-nanostructures). *APL Materials*.

[2] Wolf, E. L. [*Nanophysics and Nanotechnology: An Introduction to Modern Concepts in Nanoscience*](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527618972). Wiley-VCH.

[3] nanoHUB. [*Simulation, Education, and Community for Nanotechnology*](https://nanohub.org/).
