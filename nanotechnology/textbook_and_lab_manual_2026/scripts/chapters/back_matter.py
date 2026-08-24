# -*- coding: utf-8 -*-
"""
Back Matter: Appendices, Physical Constants, Glossary, and References
"""

def get_back_matter():
    return r"""
    <!-- APPENDIX A -->
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">APPENDIX A • REFERENCE CONSTANTS</div>
        <h1 class="chapter-title">ภาคผนวก ก: ค่าคงที่สากลทางฟิสิกส์และตารางแปลงหน่วย</h1>
        <p class="chapter-subtitle">Fundamental Physical Constants &amp; Unit Conversion Factors in Nanophysics</p>
      </div>

      <table>
        <thead>
          <tr>
            <th>ปริมาณทางฟิสิกส์ (Physical Quantity)</th>
            <th>สัญลักษณ์ (Symbol)</th>
            <th>ค่าในระบบหน่วย SI (Value in SI Units)</th>
            <th>ค่าในระบบหน่วยนาโน (Nanoscale Units)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td>ค่าคงที่พลังค์ (Planck Constant)</td><td>$h$</td><td>$6.62607015 \times 10^{-34}\text{ J}\cdot\text{s}$</td><td>$4.135667 \times 10^{-15}\text{ eV}\cdot\text{s}$</td></tr>
          <tr><td>ค่าคงที่พลังค์ลดรูป (Reduced Planck Constant)</td><td>$\hbar = h/2\pi$</td><td>$1.05457182 \times 10^{-34}\text{ J}\cdot\text{s}$</td><td>$6.582119 \times 10^{-16}\text{ eV}\cdot\text{s}$</td></tr>
          <tr><td>ประจุของอิเล็กตรอน (Elementary Charge)</td><td>$e$</td><td>$1.60217663 \times 10^{-19}\text{ C}$</td><td>$1\text{ e}$</td></tr>
          <tr><td>มวลนิ่งของอิเล็กตรอน (Electron Rest Mass)</td><td>$m_0$</td><td>$9.10938370 \times 10^{-31}\text{ kg}$</td><td>$0.5109989\text{ MeV}/c^2$</td></tr>
          <tr><td>ค่าคงที่โบลต์ซมันน์ (Boltzmann Constant)</td><td>$k_B$</td><td>$1.380649 \times 10^{-23}\text{ J/K}$</td><td>$8.617333 \times 10^{-5}\text{ eV/K}$</td></tr>
          <tr><td>ความเร็วแสงในสุญญากาศ (Speed of Light)</td><td>$c$</td><td>$2.99792458 \times 10^8\text{ m/s}$</td><td>$0.2998\text{ nm/fs}$</td></tr>
          <tr><td>สภาพยอมของสุญญากาศ (Vacuum Permittivity)</td><td>$\varepsilon_0$</td><td>$8.85418781 \times 10^{-12}\text{ F/m}$</td><td>$5.5263 \times 10^{-2}\text{ e}^2/(\text{eV}\cdot\text{nm})$</td></tr>
          <tr><td>รัศมีโบร์ของไฮโดรเจน (Bohr Radius)</td><td>$a_0$</td><td>$5.29177211 \times 10^{-11}\text{ m}$</td><td>$0.0529177\text{ nm} = 0.529\text{ Å}$</td></tr>
          <tr><td>พลังงานความร้อนที่อุณหภูมิห้อง ($300\text{ K}$)</td><td>$k_B T_{300}$</td><td>$4.142 \times 10^{-21}\text{ J}$</td><td>$25.85\text{ meV} \approx 1/40\text{ eV}$</td></tr>
          <tr><td>ความต้านทานควอนตัมของคลิตซิง (von Klitzing Constant)</td><td>$R_K = h/e^2$</td><td>$25,812.807\text{ }\Omega$</td><td>$25.813\text{ k}\Omega$</td></tr>
          <tr><td>การนำไฟฟ้าควอนตัม (Quantum Conductance)</td><td>$G_0 = 2e^2/h$</td><td>$7.74809173 \times 10^{-5}\text{ S}$</td><td>$(12.906\text{ k}\Omega)^{-1}$</td></tr>
        </tbody>
      </table>
    </div>

    <!-- APPENDIX B -->
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">APPENDIX B • MATHEMATICAL APPARATUS</div>
        <h1 class="chapter-title">ภาคผนวก ข: บทพิสูจน์คณิตศาสตร์และสมการชเรอดิงเงอร์ในพิกัดทรงกลม</h1>
        <p class="chapter-subtitle">Mathematical Proofs, Spherical Harmonics &amp; Bessel Functions in Quantum Dots</p>
      </div>

      <h2>ข.1 การแยกตัวแปรในสมการชเรอดิงเงอร์สำหรับควอนตัมดอททรงกลม</h2>
      <p>สมการชเรอดิงเงอร์อิสระจากเวลาในพิกัดทรงกลม ($r, \theta, \phi$) ภายใต้ศักย์แบบสมมาตรทรงกลม $V(r)$ เขียนได้ดังนี้:</p>
      <div class="formula-box">
        <div class="formula-math">$$\left[ -\frac{\hbar^2}{2m^*} \left( \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2}{\partial\phi^2} \right) + V(r) \right] \psi(r,\theta,\phi) = E\psi$$</div>
      </div>
      <p>เมื่อแยกตัวแปร $\psi(r,\theta,\phi) = R_{nl}(r) Y_{lm}(\theta,\phi)$ จะได้สมการในแนวรัศมี:</p>
      <div class="formula-box">
        <div class="formula-math">$$\frac{d^2 R}{dr^2} + \frac{2}{r}\frac{dR}{dr} + \left[ \frac{2m^*}{\hbar^2}(E - V(r)) - \frac{l(l+1)}{r^2} \right] R = 0$$</div>
      </div>
      <p>สำหรับบ่อศักย์ลึกอนันต์รัศมี $R_0$ ผลเฉลยคือฟังก์ชันเบสเซลทรงกลม (Spherical Bessel Functions, $j_l(kr)$) โดยที่ $k_{n,l} = \alpha_{n,l} / R_0$ เมื่อ $\alpha_{n,l}$ คือรากที่ $n$ ของ $j_l(x) = 0$ ระดับพลังงานจึงกำหนดโดย:</p>
      <div class="formula-box">
        <div class="formula-math">$$E_{n,l} = \frac{\hbar^2 \alpha_{n,l}^2}{2 m^* R_0^2}$$</div>
      </div>
    </div>

    <!-- GLOSSARY -->
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">GLOSSARY • THAI-ENGLISH</div>
        <h1 class="chapter-title">อภิธานศัพท์นาโนฟิสิกส์ (Glossary of Nanophysics Terms)</h1>
        <p class="chapter-subtitle">Comprehensive Bilingual Vocabulary and Physical Definitions</p>
      </div>

      <table>
        <thead>
          <tr>
            <th>คำศัพท์ภาษาไทย</th>
            <th>คำศัพท์ภาษาอังกฤษ</th>
            <th>คำนิยามและความหมายทางฟิสิกส์</th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>การกักขังเชิงควอนตัม</strong></td><td>Quantum Confinement</td><td>ปรากฏการณ์ที่ฟังก์ชันคลื่นของอนุภาคถูกบีบอัดในมิติที่เล็กกว่าความยาวคลื่นเดอบรอยล์ ทำให้ระดับพลังงานไม่ต่อเนื่อง</td></tr>
          <tr><td><strong>กรวยดิแรก</strong></td><td>Dirac Cones</td><td>ความสัมพันธ์การกระจายตัวของพลังงานรูปกรวยเชิงเส้นในกราฟีนที่พาหะมีพฤติกรรมเสมือนอนุภาคไร้มวล</td></tr>
          <tr><td><strong>ความดันลาปลาซ</strong></td><td>Laplace Pressure</td><td>ผลต่างความดันข้ามผิวโค้งของอนุภาคนาโนเนื่องจากพลังงานพื้นผิว $\Delta P = 2\gamma/R$</td></tr>
          <tr><td><strong>ควอนตัมดอท</strong></td><td>Quantum Dot (0D)</td><td>ผลึกสารกึ่งตัวนำขนาดนาโนเมตรที่มีระดับพลังงานแยกขาดจากกันเสมือนอะตอมเดี่ยวประดิษฐ์</td></tr>
          <tr><td><strong>คูลอมบ์บล็อกเคด</strong></td><td>Coulomb Blockade</td><td>การยับยั้งการไหลของกระแสทันเนลลิ่งในตัวนำขนาดจิ๋วเนื่องจากพลังงานชาร์จประจุ $e^2/2C > k_B T$</td></tr>
          <tr><td><strong>พลาสมอนเรโซแนนซ์</strong></td><td>LSPR</td><td>การสั่นพ้องร่วมของอิเล็กตรอนอิสระในอนุภาคโลหะนาโนกับสนามไฟฟ้าของคลื่นแสง</td></tr>
          <tr><td><strong>ลิพิดนาโนพาร์ติเคิล</strong></td><td>Lipid Nanoparticle (LNP)</td><td>อนุภาคไขมันระดับนาโนเมตรที่ใช้เป็นระบบห่อหุ้มและนำส่งยาหรือวัคซีน mRNA เข้าสู่เซลล์</td></tr>
          <tr><td><strong>ออสวอลด์ไรเปนนิง</strong></td><td>Ostwald Ripening</td><td>กระบวนการเติบโตของผลึกที่อนุภาคขนาดเล็กละลายตัวไปพอกพูนบนผิวของอนุภาคขนาดใหญ่กว่า</td></tr>
          <tr><td><strong>เอ็กซิตอน</strong></td><td>Exciton</td><td>คู่อนุภาคเทียมระหว่างอิเล็กตรอนและโฮลที่ยึดเหนี่ยวกันด้วยแรงดึงดูดคูลอมบ์ในสารกึ่งตัวนำ</td></tr>
          <tr><td><strong>ฮีเทอโรสตรัคเจอร์</strong></td><td>Heterostructure</td><td>โครงสร้างที่ประกอบขึ้นจากการประกบซ้อนวัสดุที่มีช่องว่างแถบพลังงานแตกต่างกัน</td></tr>
        </tbody>
      </table>
    </div>

    <!-- REFERENCES -->
    <div class="chapter-container">
      <div class="chapter-hero">
        <div class="chapter-badge">BIBLIOGRAPHY &amp; REFERENCES</div>
        <h1 class="chapter-title">เอกสารอ้างอิงและบรรณานุกรมวิชาการ</h1>
        <p class="chapter-subtitle">Authoritative Academic References, Standard Textbooks &amp; Seminal Papers</p>
      </div>

      <ol style="margin-left:25px; font-size:9.5pt; color:#334155; line-height:1.8;">
        <li>Wolf, E. L. (2015). <em>Nanophysics and Nanotechnology: An Introduction to Modern Concepts in Nanoscience</em> (3rd ed.). Wiley-VCH.</li>
        <li>Kittel, C. (2005). <em>Introduction to Solid State Physics</em> (8th ed.). John Wiley &amp; Sons.</li>
        <li>Ashcroft, N. W., &amp; Mermin, N. D. (1976). <em>Solid State Physics</em>. Saunders College Publishing.</li>
        <li>Datta, S. (2005). <em>Quantum Transport: Atom to Transistor</em>. Cambridge University Press.</li>
        <li>Brus, L. E. (1984). Electron–electron and electron-hole interactions in small semiconductor crystallites: The size dependence of the lowest excited electronic state. <em>Journal of Chemical Physics</em>, 80(9), 4403–4409.</li>
        <li>Novoselov, K. S., Geim, A. K., Morozov, S. V., Jiang, D., Zhang, Y., Dubonos, S. V., Grigorieva, I. V., &amp; Firsov, A. A. (2004). Electric field effect in atomically thin carbon films. <em>Science</em>, 306(5696), 666–669.</li>
        <li>Iijima, S. (1991). Helical microtubules of graphitic carbon. <em>Nature</em>, 354(6348), 56–58.</li>
        <li>Bohren, C. F., &amp; Huffman, D. R. (1983). <em>Absorption and Scattering of Light by Small Particles</em>. John Wiley &amp; Sons.</li>
        <li>Israelachvili, J. N. (2011). <em>Intermolecular and Surface Forces</em> (3rd ed.). Academic Press.</li>
        <li>LaMer, V. K., &amp; Dinegar, R. H. (1950). Theory, production and mechanism of formation of monodispersed hydrosols. <em>Journal of the American Chemical Society</em>, 72(11), 4847–4854.</li>
        <li>Sze, S. M., &amp; Ng, K. K. (2007). <em>Physics of Semiconductor Devices</em> (3rd ed.). John Wiley &amp; Sons.</li>
        <li>Feynman, R. P. (1959). There's plenty of room at the bottom: An invitation to enter a new field of physics. <em>Engineering and Science</em>, 23(5), 22–36.</li>
        <li>ชีวะ ทัศนา และ จิรพัศ จันทมาลี. (2026). <em>ฟิสิกส์ของแข็งและวัสดุศาสตร์ระดับนาโน</em>. มหาวิทยาลัยราชภัฏรำไพพรรณี.</li>
      </ol>

      <div style="margin-top:40px; padding:25px; border:2px dashed #cbd5e1; border-radius:12px; background:#f8fafc; text-align:center;">
        <h3 style="color:#0f172a; margin:0 0 10px 0;">🎉 สิ้นสุดเล่มตำราวิชาการ: นาโนเทคโนโลยีเชิงฟิสิกส์ (Masterclass Edition)</h3>
        <p style="font-size:9.5pt; color:#64748b; margin:0; line-height:1.6;">
          ลิขสิทธิ์ทางวิชาการ © พ.ศ. 2569 ผู้ช่วยศาสตราจารย์ ดร.ชีวะ ทัศนา (Asst. Prof. Dr. Chewa Thassana)<br>
          สาขาวิชาฟิสิกส์ คณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยราชภัฏรำไพพรรณี (RBRU)<br>
          จัดทำและเรนเดอร์ตามมาตรฐาน Modern Academic Textbook Publishing System (Cambridge / Springer Style)
        </p>
      </div>
    </div>
    """
