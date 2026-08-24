# บทที่ 4: การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning) และการค้นพบโครงสร้าง

## วัตถุประสงค์การเรียนรู้
เมื่อสิ้นสุดบทเรียนนี้ ผู้เรียนจะสามารถ:
- เรียนรู้เทคนิคการลดมิติ (Dimensionality Reduction) และการจัดกลุ่ม (Clustering)
- นำเทคนิคไปใช้ในการค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลฟิสิกส์
- เข้าใจการประยุกต์ใช้ในการสำรวจและสร้างสมมติฐานจากข้อมูล

## 4.1 การวิเคราะห์องค์ประกอบหลัก (Principal Component Analysis - PCA): ทฤษฎีและการประยุกต์ใช้

**Principal Component Analysis (PCA)** เป็นเทคนิคการลดมิติข้อมูลที่ใช้กันอย่างแพร่หลาย โดยมีเป้าหมายเพื่อแปลงชุดข้อมูลที่มีมิติสูงให้เป็นชุดข้อมูลที่มีมิติที่ต่ำลง โดยยังคงรักษาข้อมูลที่สำคัญที่สุดไว้ให้ได้มากที่สุด หลักการของ PCA คือการหาแกนหลัก (principal components) ซึ่งเป็นทิศทางที่ข้อมูลมีการกระจายตัวมากที่สุด [1].

### ทฤษฎีเบื้องต้นของ PCA
PCA ทำงานโดยการคำนวณเวกเตอร์ลักษณะเฉพาะ (eigenvectors) และค่าลักษณะเฉพาะ (eigenvalues) ของเมทริกซ์ความแปรปรวนร่วม (covariance matrix) ของข้อมูล. เวกเตอร์ลักษณะเฉพาะเหล่านี้คือแกนหลัก และค่าลักษณะเฉพาะที่สอดคล้องกันจะบ่งบอกถึงปริมาณความแปรปรวนของข้อมูลตามแกนนั้นๆ [2].

**ขั้นตอนหลักของ PCA:**
1. **การปรับข้อมูลให้เป็นศูนย์กลาง (Centering the data):** ลบค่าเฉลี่ยของแต่ละฟีเจอร์ออกจากข้อมูล.
2. **การคำนวณเมทริกซ์ความแปรปรวนร่วม (Covariance Matrix):** คำนวณเมทริกซ์ที่แสดงความสัมพันธ์ระหว่างคู่ของฟีเจอร์ต่างๆ.
3. **การคำนวณเวกเตอร์ลักษณะเฉพาะและค่าลักษณะเฉพาะ (Eigenvectors and Eigenvalues):** หาเวกเตอร์และค่าลักษณะเฉพาะของเมทริกซ์ความแปรปรวนร่วม.
4. **การเลือกแกนหลัก (Selecting Principal Components):** จัดเรียงแกนหลักตามลำดับของค่าลักษณะเฉพาะจากมากไปน้อย และเลือกจำนวนแกนหลักที่ต้องการเพื่อลดมิติ.
5. **การแปลงข้อมูล (Transforming the data):** ฉายข้อมูลเดิมลงบนแกนหลักที่เลือกไว้.

### การประยุกต์ใช้ PCA ในฟิสิกส์
ในสาขาฟิสิกส์ PCA มีประโยชน์อย่างมากในการวิเคราะห์ข้อมูลที่มีมิติสูง เช่น ข้อมูลจากการทดลองฟิสิกส์อนุภาค, ข้อมูลทางดาราศาสตร์, หรือข้อมูลจากการจำลองวัสดุศาสตร์ [3].

**ตัวอย่าง:**
- **ฟิสิกส์อนุภาค:** ลดมิติข้อมูลจากเครื่องตรวจจับอนุภาคเพื่อระบุลักษณะของเหตุการณ์ชนกัน.
- **ดาราศาสตร์:** วิเคราะห์สเปกตรัมของกาแล็กซีเพื่อจัดกลุ่มตามคุณสมบัติทางกายภาพ.
- **วัสดุศาสตร์:** ลดมิติข้อมูลคุณสมบัติของวัสดุเพื่อค้นหารูปแบบและทำนายพฤติกรรม.

### ตัวอย่างโค้ด: PCA สำหรับข้อมูลการทดลองฟิสิกส์

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# สร้างข้อมูลตัวอย่าง: คุณสมบัติของวัสดุ (เช่น อุณหภูมิ, ความดัน, สนามแม่เหล็ก, ความหนาแน่น)
# และผลลัพธ์การทดลอง (เช่น ค่าการนำไฟฟ้า, ค่าความต้านทาน)
# สมมติว่ามี 5 ฟีเจอร์และ 100 ตัวอย่าง
np.random.seed(42)
X = np.random.rand(100, 5) * 100  # 5 ฟีเจอร์, 100 ตัวอย่าง

# เพิ่มความสัมพันธ์บางอย่างในข้อมูลเพื่อแสดงให้เห็นถึงประโยชน์ของ PCA
X[:, 0] = X[:, 0] + np.random.normal(0, 5, 100)
X[:, 1] = X[:, 1] * 0.5 + X[:, 0] * 0.3 + np.random.normal(0, 3, 100)
X[:, 2] = X[:, 2] * 0.8 - X[:, 1] * 0.2 + np.random.normal(0, 4, 100)

print("Original data shape:", X.shape)

# 1. Standardize the data (สำคัญสำหรับ PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Apply PCA
pca = PCA(n_components=2)  # ลดเหลือ 2 องค์ประกอบหลัก
X_pca = pca.fit_transform(X_scaled)

print("Reduced data shape (2 principal components):", X_pca.shape)

# 3. Explained variance ratio
explained_variance = pca.explained_variance_ratio_
print("Explained variance ratio by each component:", explained_variance)
print("Total explained variance by 2 components:", sum(explained_variance))

# 4. Plot the 2 principal components
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.8)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Physics Experimental Data')
plt.grid(True)
plt.show()

# 5. Access the principal components (eigenvectors)
print("Principal Components (Eigenvectors):")
print(pca.components_)

# 6. Reconstruct data (optional, for understanding information loss)
X_reconstructed = pca.inverse_transform(X_pca)
print("\nReconstructed data shape:", X_reconstructed.shape)
```

### แบบทดสอบ 4.1
1. PCA มีวัตถุประสงค์หลักเพื่ออะไร?
   a) เพิ่มจำนวนฟีเจอร์ในข้อมูล
   b) ลดมิติข้อมูลโดยยังคงรักษาข้อมูลที่สำคัญ
   c) จัดกลุ่มข้อมูลที่มีความคล้ายคลึงกัน
   d) ทำนายค่าตัวแปรตาม

2. ข้อใดคือขั้นตอนแรกที่สำคัญในการทำ PCA?
   a) การคำนวณเมทริกซ์ความแปรปรวนร่วม
   b) การเลือกแกนหลัก
   c) การปรับข้อมูลให้เป็นศูนย์กลาง (Standardization/Centering)
   d) การแปลงข้อมูล

3. ค่าลักษณะเฉพาะ (eigenvalues) ใน PCA บ่งบอกถึงอะไร?
   a) จำนวนของแกนหลัก
   b) ปริมาณความแปรปรวนของข้อมูลตามแกนหลักนั้นๆ
   c) ความสัมพันธ์ระหว่างฟีเจอร์ต่างๆ
   d) ค่าเฉลี่ยของข้อมูล

4. ในฟิสิกส์อนุภาค PCA สามารถนำไปประยุกต์ใช้เพื่ออะไรได้บ้าง?
   a) การทำนายอุณหภูมิของดาวฤกษ์
   b) การลดมิติข้อมูลจากเครื่องตรวจจับอนุภาคเพื่อระบุลักษณะของเหตุการณ์ชนกัน
   c) การจำลองการเคลื่อนที่ของดาวเคราะห์
   d) การคำนวณแรงโน้มถ่วง

## 4.2 เทคนิคการลดมิติแบบไม่เชิงเส้น: t-SNE, UMAP และ Manifold Learning

ในขณะที่ PCA เป็นเทคนิคการลดมิติแบบเชิงเส้น (linear dimensionality reduction) ที่มีประสิทธิภาพ แต่บางครั้งข้อมูลในโลกแห่งความเป็นจริงอาจมีโครงสร้างที่ไม่เชิงเส้น (non-linear structure) ซึ่ง PCA อาจไม่สามารถจับภาพได้ดีนัก ในกรณีเช่นนี้ เทคนิคการลดมิติแบบไม่เชิงเส้น เช่น t-SNE, UMAP และ Manifold Learning จะเข้ามามีบทบาทสำคัญ [4].

### t-Distributed Stochastic Neighbor Embedding (t-SNE)
t-SNE เป็นอัลกอริทึมที่ใช้สำหรับการแสดงภาพข้อมูลที่มีมิติสูงในพื้นที่มิติที่ต่ำกว่า (มักจะเป็น 2 หรือ 3 มิติ) โดยเฉพาะอย่างยิ่งในการรักษาโครงสร้างของข้อมูลในท้องถิ่น (local structure) หรือความคล้ายคลึงกันระหว่างจุดข้อมูลที่อยู่ใกล้กัน [5].

**หลักการทำงาน:**
- t-SNE สร้างการแจกแจงความน่าจะเป็นบนคู่ของจุดข้อมูลในพื้นที่มิติสูงและพื้นที่มิติที่ต่ำกว่า.
- พยายามลดความแตกต่างระหว่างการแจกแจงความน่าจะเป็นทั้งสองนี้ โดยใช้ Kullback-Leibler divergence.
- เหมาะสำหรับการแสดงภาพข้อมูลเพื่อระบุกลุ่มหรือโครงสร้างที่ซ่อนอยู่.

### Uniform Manifold Approximation and Projection (UMAP)
UMAP เป็นเทคนิคการลดมิติที่ไม่เชิงเส้นอีกชนิดหนึ่งที่ได้รับความนิยมอย่างรวดเร็ว เนื่องจากมีความเร็วในการประมวลผลที่สูงกว่า t-SNE และยังคงรักษาโครงสร้างทั้งในท้องถิ่นและโครงสร้างโดยรวม (global structure) ของข้อมูลได้ดี [6].

**หลักการทำงาน:**
- UMAP สร้างกราฟของข้อมูลในพื้นที่มิติสูงและพยายามสร้างกราฟที่คล้ายกันในพื้นที่มิติที่ต่ำกว่า.
- ใช้แนวคิดจากทฤษฎี Manifold Learning และ Topological Data Analysis.
- มีพารามิเตอร์ที่สามารถปรับแต่งได้เพื่อควบคุมสมดุลระหว่างการรักษาโครงสร้างท้องถิ่นและโครงสร้างโดยรวม.

### Manifold Learning
Manifold Learning เป็นกลุ่มของอัลกอริทึมที่สมมติว่าข้อมูลที่มีมิติสูงที่เราสังเกตเห็นนั้นจริงๆ แล้วอยู่บน 

แมนิโฟลด์ (manifold) ที่มีมิติที่ต่ำกว่าในพื้นที่มิติสูงนั้น [7].

**หลักการทำงาน:**
- Manifold Learning พยายามค้นหาโครงสร้างที่แท้จริงของข้อมูล (intrinsic dimensionality) ที่ซ่อนอยู่.
- ตัวอย่างอัลกอริทึมในกลุ่มนี้ ได้แก่ Isomap, Locally Linear Embedding (LLE) และ Laplacian Eigenmaps.
- มีประโยชน์ในการเปิดเผยความสัมพันธ์ที่ซับซ้อนในข้อมูลที่ PCA ไม่สามารถทำได้.

### การประยุกต์ใช้เทคนิคการลดมิติแบบไม่เชิงเส้นในฟิสิกส์
เทคนิคเหล่านี้มีประโยชน์อย่างยิ่งในการวิเคราะห์ข้อมูลฟิสิกส์ที่แสดงพฤติกรรมที่ไม่เชิงเส้นหรือมีความซับซ้อนสูง เช่น การศึกษาการเปลี่ยนสถานะของสสาร, การวิเคราะห์ข้อมูลจากระบบควอนตัม, หรือการทำความเข้าใจโครงสร้างของวัสดุที่ซับซ้อน [8].

### ตัวอย่างโค้ด: t-SNE สำหรับข้อมูลการจำลองพลศาสตร์โมเลกุล

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# สร้างข้อมูลตัวอย่าง: ข้อมูลการจำลองพลศาสตร์โมเลกุล (เช่น ตำแหน่งและความเร็วของอนุภาค)
# สมมติว่ามี 10 ฟีเจอร์ (x, y, z, vx, vy, vz, energy, pressure, density, temperature) และ 500 ตัวอย่าง
np.random.seed(42)
X_md = np.random.rand(500, 10) * 100

# สร้างกลุ่มข้อมูลที่แตกต่างกันเพื่อแสดงให้เห็นถึงความสามารถของ t-SNE
X_md[:100, :3] += 50  # Group 1
X_md[100:200, 3:6] += 30 # Group 2
X_md[200:300, 6:9] -= 20 # Group 3

print("Original MD data shape:", X_md.shape)

# 1. Standardize the data
scaler_md = StandardScaler()
X_md_scaled = scaler_md.fit_transform(X_md)

# 2. Apply t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=300)
X_md_tsne = tsne.fit_transform(X_md_scaled)

print("Reduced MD data shape (2 dimensions with t-SNE):", X_md_tsne.shape)

# 3. Plot the t-SNE results
plt.figure(figsize=(8, 6))
plt.scatter(X_md_tsne[:, 0], X_md_tsne[:, 1], alpha=0.8, c=np.concatenate([
    np.zeros(100), np.ones(100), np.full(100, 2), np.full(200, 3)
])) # Color by artificial groups
plt.xlabel(\'t-SNE Component 1\')
plt.ylabel(\'t-SNE Component 2\')
plt.title(\'t-SNE of Molecular Dynamics Simulation Data\')
plt.colorbar(label=\'Artificial Group\')
plt.grid(True)
plt.show()
```

### แบบทดสอบ 4.2
1. ข้อใดคือข้อจำกัดหลักของ PCA เมื่อเทียบกับ t-SNE หรือ UMAP?
   a) PCA ไม่สามารถจัดการกับข้อมูลที่มีมิติสูงได้
   b) PCA ไม่สามารถรักษาโครงสร้างเชิงเส้นของข้อมูลได้
   c) PCA มีประสิทธิภาพต่ำในการจับภาพโครงสร้างข้อมูลที่ไม่เชิงเส้น
   d) PCA ใช้เวลาในการประมวลผลนานกว่า

2. t-SNE เหมาะสมที่สุดสำหรับการใช้งานประเภทใด?
   a) การทำนายค่าตัวแปรตามในข้อมูลเชิงเส้น
   b) การลดมิติข้อมูลเพื่อการจัดกลุ่มในพื้นที่มิติสูง
   c) การแสดงภาพข้อมูลที่มีมิติสูงเพื่อระบุกลุ่มหรือโครงสร้างที่ซ่อนอยู่
   d) การสร้างแบบจำลองเชิงสถิติ

3. UMAP มีข้อดีอย่างไรเมื่อเทียบกับ t-SNE?
   a) UMAP ใช้เวลาในการประมวลผลนานกว่า
   b) UMAP สามารถรักษาโครงสร้างทั้งในท้องถิ่นและโครงสร้างโดยรวมของข้อมูลได้ดีกว่า
   c) UMAP ไม่สามารถจัดการกับข้อมูลที่ไม่เชิงเส้นได้
   d) UMAP มีพารามิเตอร์ที่ปรับแต่งได้น้อยกว่า

4. Manifold Learning มีสมมติฐานพื้นฐานเกี่ยวกับข้อมูลอย่างไร?
   a) ข้อมูลทั้งหมดมีการแจกแจงแบบปกติ
   b) ข้อมูลที่มีมิติสูงจริงๆ แล้วอยู่บนแมนิโฟลด์ที่มีมิติที่ต่ำกว่า
   c) ข้อมูลมีความสัมพันธ์เชิงเส้นตรงเท่านั้น
   d) ข้อมูลไม่มีโครงสร้างที่ซ่อนอยู่

## 4.3 อัลกอริทึมการจัดกลุ่ม: K-Means, Hierarchical Clustering และ DBSCAN

การจัดกลุ่ม (Clustering) เป็นเทคนิคการเรียนรู้แบบไม่มีผู้สอนที่สำคัญ ซึ่งมีเป้าหมายในการจัดระเบียบชุดข้อมูลให้เป็นกลุ่มย่อยๆ (clusters) โดยที่ข้อมูลภายในกลุ่มเดียวกันมีความคล้ายคลึงกันสูง และข้อมูลต่างกลุ่มกันมีความคล้ายคลึงกันต่ำ [9]. การจัดกลุ่มมีประโยชน์อย่างมากในการสำรวจข้อมูล (exploratory data analysis) และการค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลฟิสิกส์.

### K-Means Clustering
K-Means เป็นหนึ่งในอัลกอริทึมการจัดกลุ่มที่ได้รับความนิยมและเข้าใจง่ายที่สุด โดยมีเป้าหมายในการแบ่งข้อมูลออกเป็น k กลุ่ม โดยที่ k คือจำนวนกลุ่มที่กำหนดไว้ล่วงหน้า [10].

**หลักการทำงาน:**
1. **การกำหนดจุดศูนย์กลางเริ่มต้น (Initialization):** สุ่มเลือกจุดข้อมูล k จุดเป็นจุดศูนย์กลางของแต่ละกลุ่ม.
2. **การกำหนดกลุ่ม (Assignment Step):** กำหนดจุดข้อมูลแต่ละจุดให้กับกลุ่มที่มีจุดศูนย์กลางที่ใกล้ที่สุด.
3. **การปรับปรุงจุดศูนย์กลาง (Update Step):** คำนวณจุดศูนย์กลางใหม่ของแต่ละกลุ่มโดยการหาค่าเฉลี่ยของจุดข้อมูลทั้งหมดในกลุ่มนั้นๆ.
4. **การทำซ้ำ (Iteration):** ทำซ้ำขั้นตอนที่ 2 และ 3 จนกว่าจุดศูนย์กลางจะไม่เปลี่ยนแปลงหรือเปลี่ยนแปลงน้อยมาก.

**ข้อดี:** เข้าใจง่าย, รวดเร็วสำหรับชุดข้อมูลขนาดใหญ่.
**ข้อเสีย:** ต้องกำหนดจำนวนกลุ่ม k ล่วงหน้า, ไวต่อจุดเริ่มต้น, ไม่เหมาะกับกลุ่มที่มีรูปร่างซับซ้อน.

### Hierarchical Clustering
Hierarchical Clustering สร้างลำดับชั้นของกลุ่มข้อมูล โดยสามารถแบ่งออกเป็นสองประเภทหลักคือ Agglomerative (จากล่างขึ้นบน) และ Divisive (จากบนลงล่าง) [11]. Agglomerative Clustering เป็นที่นิยมมากกว่า.

**หลักการทำงาน (Agglomerative):**
1. **เริ่มต้น:** แต่ละจุดข้อมูลเป็นหนึ่งกลุ่มของตัวเอง.
2. **รวมกลุ่ม:** รวมกลุ่มที่ใกล้ที่สุดเข้าด้วยกัน.
3. **ทำซ้ำ:** ทำซ้ำขั้นตอนที่ 2 จนกว่าจะเหลือเพียงกลุ่มเดียว.

ผลลัพธ์จะแสดงในรูปแบบของ Dendrogram ซึ่งเป็นแผนภาพต้นไม้ที่แสดงลำดับชั้นของการรวมกลุ่ม.

**ข้อดี:** ไม่ต้องกำหนดจำนวนกลุ่มล่วงหน้า, แสดงโครงสร้างลำดับชั้นของข้อมูล.
**ข้อเสีย:** ใช้ทรัพยากรมากสำหรับชุดข้อมูลขนาดใหญ่, การตัดสินใจรวมกลุ่มที่ระดับต่ำอาจส่งผลต่อระดับสูง.

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
DBSCAN เป็นอัลกอริทึมการจัดกลุ่มที่สามารถค้นหากลุ่มที่มีรูปร่างตามอำเภอใจ (arbitrary shapes) และสามารถระบุจุดข้อมูลที่เป็นจุดรบกวน (noise) ได้ [12].

**หลักการทำงาน:**
1. **กำหนดจุดหลัก (Core Points):** จุดข้อมูลที่มีจำนวนเพื่อนบ้าน (ภายในรัศมี epsilon) มากกว่าหรือเท่ากับ min_samples.
2. **กำหนดจุดขอบ (Border Points):** จุดข้อมูลที่อยู่ภายในรัศมี epsilon ของจุดหลัก แต่มีจำนวนเพื่อนบ้านน้อยกว่า min_samples.
3. **กำหนดจุดรบกวน (Noise Points):** จุดข้อมูลที่ไม่ใช่ทั้งจุดหลักและจุดขอบ.

**ข้อดี:** ค้นหากลุ่มที่มีรูปร่างตามอำเภอใจได้ดี, สามารถระบุจุดรบกวนได้, ไม่ต้องกำหนดจำนวนกลุ่มล่วงหน้า.
**ข้อเสีย:** ประสิทธิภาพลดลงเมื่อความหนาแน่นของข้อมูลแตกต่างกันมาก, การเลือกพารามิเตอร์ epsilon และ min_samples อาจทำได้ยาก.

### การประยุกต์ใช้การจัดกลุ่มในฟิสิกส์
การจัดกลุ่มมีบทบาทสำคัญในการวิเคราะห์ข้อมูลฟิสิกส์เพื่อค้นหารูปแบบที่ซ่อนอยู่และจัดหมวดหมู่ปรากฏการณ์ต่างๆ [13].

**ตัวอย่าง:**
- **ฟิสิกส์ดาราศาสตร์:** จัดกลุ่มกาแล็กซีตามคุณสมบัติทางสเปกตรัม.
- **ฟิสิกส์อนุภาค:** จัดกลุ่มเหตุการณ์ชนกันเพื่อระบุประเภทของอนุภาค.
- **วัสดุศาสตร์:** จัดกลุ่มวัสดุตามคุณสมบัติทางโครงสร้างหรืออิเล็กทรอนิกส์.

### ตัวอย่างโค้ด: K-Means Clustering สำหรับข้อมูลการทดลองฟิสิกส์

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# สร้างข้อมูลตัวอย่าง: ข้อมูลการทดลองฟิสิกส์ที่มีกลุ่มที่ชัดเจน
# เช่น การวัดพลังงานของอนุภาคที่มาจากแหล่งกำเนิดที่แตกต่างกัน
X_cluster, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

print("Original clustering data shape:", X_cluster.shape)

# 1. Standardize the data
scaler_cluster = StandardScaler()
X_cluster_scaled = scaler_cluster.fit_transform(X_cluster)

# 2. Apply K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10) # กำหนด 4 กลุ่ม
kmeans.fit(X_cluster_scaled)
y_kmeans = kmeans.predict(X_cluster_scaled)

# 3. Plot K-Means results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_cluster_scaled[:, 0], X_cluster_scaled[:, 1], c=y_kmeans, s=50, cmap=\'viridis\')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c=\'red\', s=200, alpha=0.7, marker=\'X\', label=\'Centroids\')
plt.title(\'K-Means Clustering\')
plt.xlabel(\'Feature 1 (Scaled)\')
plt.ylabel(\'Feature 2 (Scaled)\')
plt.legend()
plt.grid(True)

# 4. Apply DBSCAN Clustering (ตัวอย่าง)
# dbscan = DBSCAN(eps=0.3, min_samples=5)
# y_dbscan = dbscan.fit_predict(X_cluster_scaled)
# plt.subplot(1, 2, 2)
# plt.scatter(X_cluster_scaled[:, 0], X_cluster_scaled[:, 1], c=y_dbscan, s=50, cmap=\'viridis\')
# plt.title(\'DBSCAN Clustering\')
# plt.xlabel(\'Feature 1 (Scaled)\')
# plt.ylabel(\'Feature 2 (Scaled)\')
# plt.grid(True)

# 5. Apply Hierarchical Clustering (ตัวอย่าง)
agg_clustering = AgglomerativeClustering(n_clusters=4)
y_agg = agg_clustering.fit_predict(X_cluster_scaled)
plt.subplot(1, 2, 2)
plt.scatter(X_cluster_scaled[:, 0], X_cluster_scaled[:, 1], c=y_agg, s=50, cmap=\'viridis\')
plt.title(\'Hierarchical Clustering\')
plt.xlabel(\'Feature 1 (Scaled)\')
plt.ylabel(\'Feature 2 (Scaled)\')
plt.grid(True)

plt.tight_layout()
plt.show()
```

### แบบทดสอบ 4.3
1. อัลกอริทึมการจัดกลุ่มใดที่ต้องการให้ผู้ใช้กำหนดจำนวนกลุ่ม (k) ล่วงหน้า?
   a) DBSCAN
   b) Hierarchical Clustering
   c) K-Means
   d) ทั้งหมดที่กล่าวมา

2. ข้อใดคือข้อดีหลักของ DBSCAN เมื่อเทียบกับ K-Means?
   a) DBSCAN ทำงานได้เร็วกว่าสำหรับชุดข้อมูลขนาดใหญ่
   b) DBSCAN สามารถค้นหากลุ่มที่มีรูปร่างตามอำเภอใจและระบุจุดรบกวนได้
   c) DBSCAN ไม่ไวต่อจุดเริ่มต้น
   d) DBSCAN ให้ผลลัพธ์เป็น Dendrogram

3. Dendrogram เป็นผลลัพธ์ที่ได้จากอัลกอริทึมการจัดกลุ่มใด?
   a) K-Means
   b) DBSCAN
   c) Hierarchical Clustering
   d) PCA

4. ในการวิเคราะห์ข้อมูลฟิสิกส์อนุภาค การจัดกลุ่มสามารถช่วยในเรื่องใดได้บ้าง?
   a) การทำนายวิถีการเคลื่อนที่ของอนุภาค
   b) การจัดกลุ่มเหตุการณ์ชนกันเพื่อระบุประเภทของอนุภาค
   c) การคำนวณพลังงานจลน์ของอนุภาค
   d) การสร้างแบบจำลองทางทฤษฎีใหม่


## 4.4 การวิเคราะห์องค์ประกอบอิสระ (Independent Component Analysis - ICA)

**Independent Component Analysis (ICA)** เป็นเทคนิคการประมวลผลสัญญาณเชิงคำนวณที่ใช้ในการแยกสัญญาณหลายสัญญาณที่ผสมกันอยู่ (mixed signals) ออกเป็นองค์ประกอบอิสระที่มาจากการแจกแจงที่ไม่ใช่แบบเกาส์เซียน (non-Gaussian distributions) [14]. ICA แตกต่างจาก PCA ตรงที่ PCA มุ่งเน้นไปที่การลดความสัมพันธ์เชิงเส้น (linear decorrelation) และการหาทิศทางที่มีความแปรปรวนสูงสุด ในขณะที่ ICA มุ่งเน้นไปที่การหาองค์ประกอบที่เป็นอิสระทางสถิติ (statistically independent components).

### หลักการทำงานของ ICA
สมมติว่าเรามีสัญญาณต้นฉบับ (source signals) หลายสัญญาณที่อิสระต่อกัน และสัญญาณเหล่านี้ถูกผสมรวมกันด้วยเมทริกซ์การผสม (mixing matrix) ที่ไม่ทราบค่า. ICA พยายามที่จะหาเมทริกซ์การแยก (unmixing matrix) ที่สามารถแยกสัญญาณผสมกลับไปเป็นสัญญาณต้นฉบับที่เป็นอิสระได้ [15].

**ตัวอย่างคลาสสิก:** ปัญหา 'Cocktail Party Problem' ที่ต้องการแยกเสียงพูดของแต่ละบุคคลออกจากเสียงผสมที่บันทึกโดยไมโครโฟนหลายตัว.

### การประยุกต์ใช้ ICA ในฟิสิกส์
ICA มีประโยชน์ในการวิเคราะห์ข้อมูลฟิสิกส์ที่เกิดจากการผสมผสานของกระบวนการทางกายภาพหลายอย่าง [16].

**ตัวอย่าง:**
- **ฟิสิกส์ดาราศาสตร์:** แยกสัญญาณจากแหล่งกำเนิดรังสีคอสมิกที่แตกต่างกันออกจากข้อมูลที่บันทึกโดยกล้องโทรทรรศน์.
- **ฟิสิกส์พลาสมา:** แยกองค์ประกอบของสัญญาณพลาสมาที่ซับซ้อนเพื่อทำความเข้าใจกระบวนการพื้นฐาน.
- **การวิเคราะห์สัญญาณ:** แยกสัญญาณรบกวนออกจากสัญญาณฟิสิกส์ที่ต้องการศึกษา.

### ตัวอย่างโค้ด: ICA สำหรับการแยกสัญญาณฟิสิกส์

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from sklearn.decomposition import FastICA

# สร้างสัญญาณต้นฉบับ (สมมติว่าเป็นสัญญาณฟิสิกส์ 2 ชนิด)
np.random.seed(0)
n_samples = 2000
t = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * t)  # สัญญาณไซน์
s2 = np.sign(np.sin(3 * t)) # สัญญาณคลื่นสี่เหลี่ยม

S = np.c_[s1, s2] # รวมสัญญาณต้นฉบับ
S += 0.2 * np.random.normal(size=S.shape) # เพิ่มสัญญาณรบกวนเล็กน้อย

# สร้างเมทริกซ์การผสมแบบสุ่ม
A = np.array([[1, 1], [0.5, 2]])  # Mixing matrix
X_mixed = S @ A.T  # สัญญาณผสม

print("Original source signals shape:", S.shape)
print("Mixed signals shape:", X_mixed.shape)

# 1. Apply FastICA
ica = FastICA(n_components=2, random_state=0, max_iter=500)
S_recovered = ica.fit_transform(X_mixed)  # แยกสัญญาณ

# 2. Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, s1, label=\'Source 1 (Sine)\
plt.plot(t, s2, label=\'Source 2 (Square)\
plt.title(\'Original Source Signals\
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, X_mixed[:, 0], label=\'Mixed Signal 1\
plt.plot(t, X_mixed[:, 1], label=\'Mixed Signal 2\
plt.title(\'Mixed Signals\
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, S_recovered[:, 0], label=\'Recovered Signal 1\
plt.plot(t, S_recovered[:, 1], label=\'Recovered Signal 2\
plt.title(\'Recovered Signals by ICA\
plt.legend()

plt.tight_layout()
plt.show()
```

### แบบทดสอบ 4.4
1. ICA แตกต่างจาก PCA อย่างไรในหลักการพื้นฐาน?
   a) ICA มุ่งเน้นการลดความสัมพันธ์เชิงเส้น, PCA มุ่งเน้นความเป็นอิสระทางสถิติ
   b) ICA มุ่งเน้นความเป็นอิสระทางสถิติ, PCA มุ่งเน้นการลดความสัมพันธ์เชิงเส้น
   c) ICA ใช้สำหรับการจัดกลุ่ม, PCA ใช้สำหรับการลดมิติ
   d) ICA ใช้สำหรับการทำนาย, PCA ใช้สำหรับการจำแนกประเภท

2. ปัญหา 'Cocktail Party Problem' เป็นตัวอย่างคลาสสิกของการประยุกต์ใช้เทคนิคใด?
   a) PCA
   b) K-Means
   c) ICA
   d) t-SNE

3. ข้อใดคือคุณสมบัติสำคัญของสัญญาณที่ ICA พยายามแยกออกมา?
   a) มีการแจกแจงแบบเกาส์เซียน
   b) มีความสัมพันธ์เชิงเส้นสูง
   c) เป็นอิสระทางสถิติและมาจากการแจกแจงที่ไม่ใช่แบบเกาส์เซียน
   d) มีความแปรปรวนต่ำ

4. ในฟิสิกส์ดาราศาสตร์ ICA สามารถนำไปใช้เพื่ออะไรได้บ้าง?
   a) การทำนายการโคจรของดาวเคราะห์
   b) การแยกสัญญาณจากแหล่งกำเนิดรังสีคอสมิกที่แตกต่างกัน
   c) การจำลองการก่อตัวของกาแล็กซี
   d) การคำนวณมวลของหลุมดำ

## 4.5 การประยุกต์ใช้ในการวิเคราะห์แผนภาพสถานะ (Phase Diagrams) และการเปลี่ยนสถานะ

แผนภาพสถานะ (Phase Diagrams) เป็นเครื่องมือสำคัญในฟิสิกส์และวัสดุศาสตร์ที่แสดงถึงสภาวะทางกายภาพของสสารภายใต้เงื่อนไขต่างๆ เช่น อุณหภูมิ ความดัน หรือสนามแม่เหล็ก [17]. การเปลี่ยนสถานะ (Phase Transitions) เป็นปรากฏการณ์ที่สสารเปลี่ยนจากสถานะหนึ่งไปอีกสถานะหนึ่ง ซึ่งมักจะเกี่ยวข้องกับการเปลี่ยนแปลงคุณสมบัติทางกายภาพอย่างรวดเร็ว.

### การใช้ Unsupervised Learning ในการวิเคราะห์แผนภาพสถานะ
เทคนิค Unsupervised Learning โดยเฉพาะการลดมิติและการจัดกลุ่ม สามารถช่วยในการวิเคราะห์และทำความเข้าใจแผนภาพสถานะและการเปลี่ยนสถานะได้อย่างมีประสิทธิภาพ โดยเฉพาะอย่างยิ่งเมื่อข้อมูลมีมิติสูงและซับซ้อน [18].

**ตัวอย่างการประยุกต์ใช้:**
- **การลดมิติ:** ใช้ PCA, t-SNE หรือ UMAP เพื่อลดมิติของข้อมูลคุณสมบัติทางกายภาพ (เช่น การจัดเรียงสปิน, ค่าพารามิเตอร์อันดับ) ที่ได้จากการจำลองหรือการทดลอง เพื่อสร้างภาพแผนภาพสถานะใน 2D หรือ 3D.
- **การจัดกลุ่ม:** ใช้ K-Means, Hierarchical Clustering หรือ DBSCAN เพื่อระบุขอบเขตของสถานะต่างๆ ในแผนภาพสถานะ โดยการจัดกลุ่มจุดข้อมูลที่มีคุณสมบัติคล้ายคลึงกันเข้าด้วยกัน.
- **การระบุจุดวิกฤต:** การเปลี่ยนแปลงอย่างรวดเร็วในโครงสร้างของกลุ่มข้อมูลที่ลดมิติแล้วสามารถบ่งชี้ถึงจุดวิกฤตของการเปลี่ยนสถานะได้.

### ตัวอย่างโค้ด: การใช้ PCA เพื่อสร้างแผนภาพสถานะแบบง่าย

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# สร้างข้อมูลตัวอย่าง: คุณสมบัติของวัสดุที่อุณหภูมิต่างๆ (สมมติ 3 สถานะ: ของแข็ง, ของเหลว, แก๊ส)
# แต่ละสถานะมีคุณสมบัติทางกายภาพที่แตกต่างกัน (เช่น ความหนาแน่น, ความร้อนจำเพาะ, การนำไฟฟ้า)
np.random.seed(42)
n_samples_per_phase = 100

# Phase 1 (Solid-like)
phase1_data = np.random.normal(loc=[10, 2, 0.1], scale=[1, 0.2, 0.02], size=(n_samples_per_phase, 3))

# Phase 2 (Liquid-like)
phase2_data = np.random.normal(loc=[5, 5, 0.5], scale=[0.5, 0.5, 0.1], size=(n_samples_per_phase, 3))

# Phase 3 (Gas-like)
phase3_data = np.random.normal(loc=[1, 8, 0.9], scale=[0.2, 1, 0.05], size=(n_samples_per_phase, 3))

X_phases = np.vstack((phase1_data, phase2_data, phase3_data))
y_phases = np.array([0]*n_samples_per_phase + [1]*n_samples_per_phase + [2]*n_samples_per_phase)

print("Original phase data shape:", X_phases.shape)

# 1. Standardize the data
scaler_phases = StandardScaler()
X_phases_scaled = scaler_phases.fit_transform(X_phases)

# 2. Apply PCA to reduce to 2 dimensions for visualization
pca_phases = PCA(n_components=2)
X_phases_pca = pca_phases.fit_transform(X_phases_scaled)

print("Reduced phase data shape (2 principal components):", X_phases_pca.shape)

# 3. Plot the phase diagram in reduced dimension
plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_phases_pca[:, 0], X_phases_pca[:, 1], c=y_phases, cmap=\'viridis\', alpha=0.8)
plt.xlabel(\'Principal Component 1\
plt.ylabel(\'Principal Component 2\
plt.title(\'Simplified Phase Diagram using PCA\
plt.colorbar(scatter, ticks=[0, 1, 2], label=\'Phase (0=Solid, 1=Liquid, 2=Gas)\
plt.grid(True)
plt.show()
```

### แบบทดสอบ 4.5
1. แผนภาพสถานะ (Phase Diagrams) ใช้แสดงอะไรในฟิสิกส์?
   a) การเคลื่อนที่ของอนุภาค
   b) สภาวะทางกายภาพของสสารภายใต้เงื่อนไขต่างๆ
   c) ความสัมพันธ์ระหว่างแรงและการเร่ง
   d) การเปลี่ยนแปลงพลังงานในระบบ

2. เทคนิค Unsupervised Learning ใดที่สามารถช่วยในการระบุขอบเขตของสถานะต่างๆ ในแผนภาพสถานะได้?
   a) Linear Regression
   b) Logistic Regression
   c) Clustering (เช่น K-Means)
   d) Support Vector Machines

3. การเปลี่ยนแปลงอย่างรวดเร็วในโครงสร้างของกลุ่มข้อมูลที่ลดมิติแล้วสามารถบ่งชี้ถึงอะไร?
   a) การเพิ่มขึ้นของอุณหภูมิ
   b) จุดวิกฤตของการเปลี่ยนสถานะ
   c) การลดลงของความดัน
   d) การเพิ่มขึ้นของปริมาตร

4. การลดมิติข้อมูลด้วย PCA, t-SNE หรือ UMAP มีประโยชน์อย่างไรในการวิเคราะห์แผนภาพสถานะ?
   a) ช่วยเพิ่มความซับซ้อนของข้อมูล
   b) ช่วยให้สามารถสร้างภาพแผนภาพสถานะใน 2D หรือ 3D ได้
   c) ช่วยในการทำนายค่าตัวแปรตาม
   d) ช่วยในการคำนวณค่าเฉลี่ยของข้อมูล

## 4.6 การค้นหารูปแบบในข้อมูลอนุกรมเวลา (Time Series) จากการจำลองทางฟิสิกส์

ข้อมูลอนุกรมเวลา (Time Series Data) เป็นข้อมูลที่ถูกเก็บรวบรวมตามลำดับเวลา ซึ่งพบได้บ่อยในการจำลองทางฟิสิกส์และการทดลอง เช่น การวัดอุณหภูมิของระบบที่เปลี่ยนแปลงตามเวลา, การติดตามตำแหน่งของอนุภาค, หรือการบันทึกสัญญาณจากเครื่องตรวจจับ [19]. การค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลอนุกรมเวลาเป็นสิ่งสำคัญในการทำความเข้าใจพลวัตของระบบ.

### การใช้ Unsupervised Learning สำหรับ Time Series
เทคนิค Unsupervised Learning สามารถนำมาประยุกต์ใช้เพื่อค้นหารูปแบบ, ความผิดปกติ (anomalies), หรือจัดกลุ่มพฤติกรรมที่คล้ายคลึงกันในข้อมูลอนุกรมเวลา [20].

**ตัวอย่างการประยุกต์ใช้:**
- **การลดมิติ:** ลดมิติของฟีเจอร์ที่สกัดจากอนุกรมเวลา (เช่น ค่าเฉลี่ย, ความแปรปรวน, ค่าสัมประสิทธิ์ฟูเรียร์) เพื่อให้สามารถแสดงภาพหรือจัดกลุ่มได้ง่ายขึ้น.
- **การจัดกลุ่ม:** จัดกลุ่มอนุกรมเวลาที่มีพฤติกรรมคล้ายคลึงกัน เช่น การจัดกลุ่มการสั่นของโมเลกุล หรือการจัดกลุ่มสัญญาณจากแหล่งกำเนิดเดียวกัน.
- **การตรวจจับความผิดปกติ:** ระบุอนุกรมเวลาที่มีพฤติกรรมแตกต่างจากปกติ ซึ่งอาจบ่งชี้ถึงเหตุการณ์ทางฟิสิกส์ที่น่าสนใจหรือข้อผิดพลาดในการทดลอง.

### ตัวอย่างโค้ด: K-Means Clustering สำหรับ Time Series Data

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from tslearn.clustering import TimeSeriesKMeans
from tslearn.datasets import utils

# สร้างข้อมูลอนุกรมเวลาตัวอย่าง (สมมติว่าเป็นการวัดอุณหภูมิจาก 3 การทดลองที่แตกต่างกัน)
np.random.seed(42)
n_ts = 30  # Number of time series
sz = 50  # Length of each time series

# Group 1: Sine wave with noise
ts1 = np.sin(np.linspace(0, 10, sz)) + np.random.normal(0, 0.2, sz)

# Group 2: Cosine wave with noise
ts2 = np.cos(np.linspace(0, 10, sz)) + np.random.normal(0, 0.2, sz)

# Group 3: Linear trend with noise
ts3 = np.linspace(0, 1, sz) + np.random.normal(0, 0.1, sz)

X_ts = np.vstack([
    np.tile(ts1, (n_ts // 3, 1)),
    np.tile(ts2, (n_ts // 3, 1)),
    np.tile(ts3, (n_ts // 3, 1))
])

# Add some random variations to each time series within its group
X_ts += np.random.normal(0, 0.1, X_ts.shape)

print("Original time series data shape:", X_ts.shape)

# 1. Standardize the data (optional, but good practice)
scaler_ts = StandardScaler()
X_ts_scaled = scaler_ts.fit_transform(X_ts)

# 2. Apply TimeSeriesKMeans (using a library like tslearn for time series specific clustering)
# Note: For simple cases, standard KMeans on raw time series can work, but tslearn is better for complex patterns
km = TimeSeriesKMeans(n_clusters=3, metric=\

"'dtw'", random_state=42, n_init=10)
km.fit(X_ts_scaled)
y_ts_kmeans = km.predict(X_ts_scaled)

# 3. Plot the results
plt.figure(figsize=(12, 8))
for i in range(3):
    plt.subplot(3, 1, i + 1)
    for j in range(n_ts):
        if y_ts_kmeans[j] == i:
            plt.plot(X_ts_scaled[j], alpha=0.6)
    plt.title(f\'Cluster {i+1}\' )
    plt.ylabel(\'Scaled Value\')
plt.xlabel(\'Time Point\')
plt.tight_layout()
plt.show()
```

### แบบทดสอบ 4.6
1. ข้อมูลอนุกรมเวลา (Time Series Data) คืออะไร?
   a) ข้อมูลที่ไม่มีลำดับเวลา
   b) ข้อมูลที่ถูกเก็บรวบรวมตามลำดับเวลา
   c) ข้อมูลที่มีเพียงสองมิติ
   d) ข้อมูลที่ใช้สำหรับการจำแนกประเภทเท่านั้น

2. เทคนิค Unsupervised Learning สามารถนำมาประยุกต์ใช้กับข้อมูลอนุกรมเวลาเพื่อวัตถุประสงค์ใดบ้าง?
   a) การทำนายค่าในอนาคต
   b) การค้นหารูปแบบ, ความผิดปกติ, หรือจัดกลุ่มพฤติกรรมที่คล้ายคลึงกัน
   c) การสร้างแบบจำลองเชิงเส้น
   d) การคำนวณค่าเฉลี่ยเคลื่อนที่

3. การจัดกลุ่มอนุกรมเวลาที่มีพฤติกรรมคล้ายคลึงกันมีประโยชน์อย่างไร?
   a) ช่วยให้สามารถทำนายค่าได้อย่างแม่นยำ
   b) ช่วยในการระบุแหล่งกำเนิดของสัญญาณที่แตกต่างกัน
   c) ช่วยในการทำความเข้าใจพลวัตของระบบและจัดหมวดหมู่ปรากฏการณ์
   d) ช่วยในการลดสัญญาณรบกวน

4. ในการตรวจจับความผิดปกติในข้อมูลอนุกรมเวลา เทคนิค Unsupervised Learning สามารถบ่งชี้ถึงอะไรได้บ้าง?
   a) การเปลี่ยนแปลงตามฤดูกาล
   b) เหตุการณ์ทางฟิสิกส์ที่น่าสนใจหรือข้อผิดพลาดในการทดลอง
   c) แนวโน้มของข้อมูล
   d) ความสัมพันธ์เชิงเส้นระหว่างตัวแปร

## 4.7 การค้นพบโครงสร้างในข้อมูลทางฟิสิกส์ด้วย Autoencoders

**Autoencoders** เป็นโครงข่ายประสาทเทียม (neural networks) ชนิดหนึ่งที่ได้รับการออกแบบมาเพื่อเรียนรู้การเข้ารหัส (encoding) ข้อมูลที่มีประสิทธิภาพในรูปแบบที่ไม่มีผู้สอน (unsupervised manner) [21]. หลักการทำงานคือการบีบอัดข้อมูลอินพุตให้เป็นตัวแทนที่มีมิติที่ต่ำกว่า (latent space representation) และจากนั้นก็พยายามสร้างข้อมูลอินพุตเดิมกลับคืนมาให้ได้มากที่สุด.

### สถาปัตยกรรมของ Autoencoder
Autoencoder ประกอบด้วยสองส่วนหลัก:
1. **Encoder:** ทำหน้าที่แปลงข้อมูลอินพุตที่มีมิติสูงให้เป็นตัวแทนที่มีมิติที่ต่ำกว่า (latent space).
2. **Decoder:** ทำหน้าที่สร้างข้อมูลอินพุตเดิมกลับคืนมาจากตัวแทนใน latent space.

เป้าหมายคือการลดความแตกต่างระหว่างข้อมูลอินพุตและข้อมูลเอาต์พุตที่สร้างขึ้นใหม่ ซึ่งบังคับให้ encoder เรียนรู้การจับคุณสมบัติที่สำคัญที่สุดของข้อมูล [22].

### การประยุกต์ใช้ Autoencoders ในฟิสิกส์
Autoencoders มีประโยชน์อย่างมากในการวิเคราะห์ข้อมูลฟิสิกส์ โดยเฉพาะอย่างยิ่งในการลดมิติ, การตรวจจับความผิดปกติ, และการเรียนรู้คุณสมบัติที่ซ่อนอยู่ในข้อมูล [23].

**ตัวอย่าง:**
- **ฟิสิกส์อนุภาค:** ลดมิติข้อมูลจากเครื่องตรวจจับเพื่อค้นหาเหตุการณ์ใหม่ๆ หรือตรวจจับความผิดปกติ.
- **วัสดุศาสตร์:** เรียนรู้ตัวแทนที่มีประสิทธิภาพของโครงสร้างผลึกหรือคุณสมบัติของวัสดุ.
- **ฟิสิกส์ดาราศาสตร์:** ตรวจจับความผิดปกติในข้อมูลทางดาราศาสตร์ เช่น ซูเปอร์โนวา หรือการปะทุของรังสีแกมมา.

### ตัวอย่างโค้ด: Autoencoder สำหรับการลดมิติข้อมูลฟิสิกส์

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

# สร้างข้อมูลตัวอย่าง: ข้อมูลการทดลองฟิสิกส์ที่มีมิติสูง (เช่น การวัดจากเซ็นเซอร์หลายตัว)
np.random.seed(42)
X_ae = np.random.rand(1000, 30)  # 1000 ตัวอย่าง, 30 ฟีเจอร์

# เพิ่มความสัมพันธ์บางอย่างในข้อมูล
X_ae[:, 0] = X_ae[:, 1] * 2 + np.random.normal(0, 0.1, 1000)
X_ae[:, 5] = X_ae[:, 10] * 0.5 - X_ae[:, 15] * 0.3 + np.random.normal(0, 0.2, 1000)

print("Original Autoencoder data shape:", X_ae.shape)

# 1. Standardize the data
scaler_ae = StandardScaler()
X_ae_scaled = scaler_ae.fit_transform(X_ae)

# 2. Build the Autoencoder model
input_dim = X_ae_scaled.shape[1]
encoding_dim = 2  # ลดมิติเหลือ 2 สำหรับการแสดงภาพ

input_layer = Input(shape=(input_dim,))
encoder = Dense(16, activation=\'relu\')(input_layer)
encoder = Dense(8, activation=\'relu\')(encoder)
encoder_output = Dense(encoding_dim, activation=\'relu\')(encoder) # Latent space

decoder = Dense(8, activation=\'relu\')(encoder_output)
decoder = Dense(16, activation=\'relu\')(decoder)
decoder_output = Dense(input_dim, activation=\'linear\')(decoder)

autoencoder = Model(inputs=input_layer, outputs=decoder_output)

# 3. Compile and train the Autoencoder
autoencoder.compile(optimizer=\'adam\', loss=\'mse\')
autoencoder.fit(X_ae_scaled, X_ae_scaled, epochs=50, batch_size=32, shuffle=True, verbose=0)

# 4. Extract the encoded (reduced dimension) representation
encoder_model = Model(inputs=input_layer, outputs=encoder_output)
X_ae_encoded = encoder_model.predict(X_ae_scaled)

print("Reduced Autoencoder data shape (2 dimensions):", X_ae_encoded.shape)

# 5. Plot the reduced dimension data
plt.figure(figsize=(8, 6))
plt.scatter(X_ae_encoded[:, 0], X_ae_encoded[:, 1], alpha=0.8)
plt.xlabel(\'Latent Dimension 1\')
plt.ylabel(\'Latent Dimension 2\')
plt.title(\'Autoencoder Latent Space Representation of Physics Data\')
plt.grid(True)
plt.show()
```

### แบบทดสอบ 4.7
1. Autoencoder มีส่วนประกอบหลักกี่ส่วนและทำหน้าที่อะไรบ้าง?
   a) 1 ส่วน: Encoder ทำหน้าที่ลดมิติข้อมูล
   b) 2 ส่วน: Encoder ลดมิติ, Decoder สร้างข้อมูลกลับคืน
   c) 3 ส่วน: Input, Hidden, Output
   d) 2 ส่วน: Input, Output

2. เป้าหมายหลักของ Autoencoder คืออะไร?
   a) การจำแนกประเภทข้อมูล
   b) การทำนายค่าตัวแปรตาม
   c) การเรียนรู้การเข้ารหัสข้อมูลที่มีประสิทธิภาพและสร้างข้อมูลอินพุตเดิมกลับคืน
   d) การจัดกลุ่มข้อมูล

3. ในฟิสิกส์อนุภาค Autoencoder สามารถนำไปประยุกต์ใช้เพื่ออะไรได้บ้าง?
   a) การคำนวณมวลของอนุภาค
   b) การลดมิติข้อมูลจากเครื่องตรวจจับเพื่อค้นหาเหตุการณ์ใหม่ๆ หรือตรวจจับความผิดปกติ
   c) การจำลองการชนกันของอนุภาค
   d) การสร้างอนุภาคใหม่

4. Latent space representation ใน Autoencoder คืออะไร?
   a) ข้อมูลอินพุตเดิม
   b) ข้อมูลเอาต์พุตที่สร้างขึ้นใหม่
   c) ตัวแทนข้อมูลที่มีมิติที่ต่ำกว่าที่ Encoder สร้างขึ้น
   d) สัญญาณรบกวนในข้อมูล

## 4.8 การประยุกต์ใช้ Unsupervised Learning ในการสร้างแบบจำลองทางฟิสิกส์เชิงกำเนิด (Generative Physics Models)

**Generative Models** เป็นแบบจำลองที่เรียนรู้การแจกแจงข้อมูล (data distribution) และสามารถสร้างข้อมูลใหม่ที่คล้ายกับข้อมูลต้นฉบับได้ [24]. ในบริบทของฟิสิกส์, Generative Physics Models สามารถใช้เพื่อสร้างข้อมูลการทดลองจำลอง, สร้างการกำหนดค่าของระบบทางฟิสิกส์, หรือสำรวจพื้นที่พารามิเตอร์ที่ซับซ้อน.

### Generative Adversarial Networks (GANs) และ Variational Autoencoders (VAEs)
สองประเภทหลักของ Generative Models ที่ใช้กันอย่างแพร่หลายคือ GANs และ VAEs.

**Generative Adversarial Networks (GANs):**
- ประกอบด้วยสองโครงข่ายประสาทเทียมที่แข่งขันกัน: Generator และ Discriminator.
- **Generator:** สร้างข้อมูลใหม่จาก noise.
- **Discriminator:** พยายามแยกแยะระหว่างข้อมูลจริงกับข้อมูลที่ Generator สร้างขึ้น.
- ทั้งสองโครงข่ายจะได้รับการฝึกฝนไปพร้อมกัน โดย Generator พยายามสร้างข้อมูลที่หลอก Discriminator ได้ และ Discriminator พยายามแยกแยะให้ถูกต้อง [25].

**Variational Autoencoders (VAEs):**
- เป็นส่วนขยายของ Autoencoder ที่เพิ่มความสามารถในการสร้างข้อมูล.
- Encoder จะเรียนรู้ที่จะแมปข้อมูลอินพุตไปยังการแจกแจงความน่าจะเป็น (เช่น การแจกแจงแบบปกติ) ใน latent space แทนที่จะเป็นจุดเดียว.
- Decoder จะสุ่มตัวอย่างจาก latent space นี้เพื่อสร้างข้อมูลใหม่ [26].

### การประยุกต์ใช้ Generative Physics Models
Generative Models มีศักยภาพในการปฏิวัติการวิจัยทางฟิสิกส์โดยการสร้างข้อมูลที่ซับซ้อนและสำรวจพื้นที่พารามิเตอร์ที่กว้างขวาง [27].

**ตัวอย่าง:**
- **ฟิสิกส์อนุภาค:** สร้างข้อมูลการชนกันของอนุภาคจำลองเพื่อฝึกฝนเครื่องมือตรวจจับหรือสำรวจฟิสิกส์ใหม่ๆ.
- **วัสดุศาสตร์:** สร้างโครงสร้างวัสดุใหม่ที่มีคุณสมบัติที่ต้องการ.
- **ฟิสิกส์ดาราศาสตร์:** สร้างภาพกาแล็กซีหรือการจำลองการก่อตัวของโครงสร้างขนาดใหญ่.

### ตัวอย่างโค้ด: VAE สำหรับการสร้างข้อมูลฟิสิกส์แบบง่าย

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Lambda
from tensorflow.keras import backend as K
from tensorflow.keras.losses import mse

# สร้างข้อมูลตัวอย่าง: ข้อมูลการทดลองฟิสิกส์แบบง่าย (เช่น การวัด 2 มิติ)
np.random.seed(42)
X_gen = np.random.normal(loc=[0, 0], scale=[1, 1], size=(1000, 2))
X_gen = np.vstack((X_gen, np.random.normal(loc=[5, 5], scale=[0.5, 0.5], size=(500, 2))))

print("Original Generative data shape:", X_gen.shape)

# 1. Standardize the data
scaler_gen = StandardScaler()
X_gen_scaled = scaler_gen.fit_transform(X_gen)

# 2. Build the VAE model
original_dim = X_gen_scaled.shape[1]
latent_dim = 2

# Encoder
inputs = Input(shape=(original_dim,))
x = Dense(8, activation=\'relu\')(inputs)
z_mean = Dense(latent_dim, name=\'z_mean\')(x)
z_log_var = Dense(latent_dim, name=\'z_log_var\')(x)

# Reparameterization trick
def sampling(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

z = Lambda(sampling, output_shape=(latent_dim,), name=\'z\')([z_mean, z_log_var])

encoder = Model(inputs, [z_mean, z_log_var, z], name=\'encoder\')

# Decoder
latent_inputs = Input(shape=(latent_dim,), name=\'z_sampling\')
x = Dense(8, activation=\'relu\')(latent_inputs)
outputs = Dense(original_dim, activation=\'linear\')(x)

decoder = Model(latent_inputs, outputs, name=\'decoder\')

# VAE
outputs = decoder(encoder(inputs)[2])
vae = Model(inputs, outputs, name=\'vae_mlp\')

# VAE loss = mse_loss + kl_loss
reconstruction_loss = mse(inputs, outputs)
reconstruction_loss *= original_dim
kl_loss = 1 + z_log_var - K.square(z_mean) - K.exp(z_log_var)
kl_loss = K.sum(kl_loss, axis=-1)
kl_loss *= -0.5
vae_loss = K.mean(reconstruction_loss + kl_loss)
vae.add_loss(vae_loss)
vae.compile(optimizer=\'adam\')

# 3. Train the VAE
vae.fit(X_gen_scaled, epochs=50, batch_size=32, verbose=0)

# 4. Generate new data from the trained VAE
# Sample points in the latent space
np.random.seed(42)
latent_samples = np.random.normal(size=(500, latent_dim))

# Decode to generate new data
X_generated_scaled = decoder.predict(latent_samples)
X_generated = scaler_gen.inverse_transform(X_generated_scaled)

print("Generated data shape:", X_generated.shape)

# 5. Plot original and generated data
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_gen[:, 0], X_gen[:, 1], alpha=0.8)
plt.title(\'Original Physics Data\')
plt.xlabel(\'Feature 1\')
plt.ylabel(\'Feature 2\')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(X_generated[:, 0], X_generated[:, 1], alpha=0.8, c=\'red\')
plt.title(\'Generated Physics Data (VAE)\' )
plt.xlabel(\'Feature 1\')
plt.ylabel(\'Feature 2\')
plt.grid(True)

plt.tight_layout()
plt.show()
```

### แบบทดสอบ 4.8
1. Generative Models มีเป้าหมายหลักในการทำอะไร?
   a) การจำแนกประเภทข้อมูล
   b) การทำนายค่าตัวแปรตาม
   c) การเรียนรู้การแจกแจงข้อมูลและสามารถสร้างข้อมูลใหม่ที่คล้ายกับข้อมูลต้นฉบับได้
   d) การลดมิติข้อมูล

2. GANs ประกอบด้วยโครงข่ายประสาทเทียมกี่ส่วนและทำหน้าที่อะไรบ้าง?
   a) 1 ส่วน: Generator สร้างข้อมูล
   b) 2 ส่วน: Generator สร้างข้อมูล, Discriminator แยกแยะข้อมูลจริง/ปลอม
   c) 3 ส่วน: Input, Hidden, Output
   d) 2 ส่วน: Encoder, Decoder

3. VAEs แตกต่างจาก Autoencoders ทั่วไปอย่างไร?
   a) VAEs ไม่มี Decoder
   b) VAEs เรียนรู้ที่จะแมปข้อมูลอินพุตไปยังการแจกแจงความน่าจะเป็นใน latent space
   c) VAEs ไม่สามารถสร้างข้อมูลใหม่ได้
   d) VAEs ใช้สำหรับการจัดกลุ่มเท่านั้น

4. ในฟิสิกส์อนุภาค Generative Physics Models สามารถนำไปประยุกต์ใช้เพื่ออะไรได้บ้าง?
   a) การคำนวณพลังงานของอนุภาค
   b) การสร้างข้อมูลการชนกันของอนุภาคจำลองเพื่อฝึกฝนเครื่องมือตรวจจับ
   c) การวิเคราะห์สเปกตรัมของอนุภาค
   d) การวัดความเร็วของอนุภาค

## 4.9 สรุปและแนวโน้มในอนาคต

บทนี้ได้สำรวจเทคนิคการเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning) ที่หลากหลายและทรงพลัง รวมถึงการลดมิติ (PCA, t-SNE, UMAP, Autoencoders), การจัดกลุ่ม (K-Means, Hierarchical, DBSCAN), และการแยกองค์ประกอบอิสระ (ICA) นอกจากนี้ยังได้กล่าวถึง Generative Models (GANs, VAEs) ซึ่งเป็นแนวทางที่น่าตื่นเต้นในการสร้างแบบจำลองทางฟิสิกส์เชิงกำเนิด.

### แนวโน้มในอนาคต
- **การรวมกันของเทคนิค:** การรวม Unsupervised Learning เข้ากับ Supervised Learning (Semi-supervised Learning) เพื่อใช้ประโยชน์จากข้อมูลที่มีป้ายกำกับน้อยและข้อมูลที่ไม่มีป้ายกำกับจำนวนมาก.
- **การค้นพบทางฟิสิกส์อัตโนมัติ:** การใช้ Unsupervised Learning เพื่อค้นพบกฎทางฟิสิกส์ใหม่ๆ หรือสมการที่ซ่อนอยู่ในข้อมูล.
- **การสร้างแบบจำลองที่ซับซ้อน:** การพัฒนา Generative Models ที่สามารถสร้างข้อมูลการจำลองทางฟิสิกส์ที่มีความสมจริงและซับซ้อนมากขึ้น.
- **การวิเคราะห์ข้อมูลขนาดใหญ่:** การปรับปรุงประสิทธิภาพของอัลกอริทึม Unsupervised Learning เพื่อจัดการกับชุดข้อมูลขนาดใหญ่และมีความหลากหลายสูงที่มาจากเครื่องทดลองฟิสิกส์ยุคใหม่.

### แหล่งอ้างอิง
[1] Jolliffe, I. T. (2002). *Principal Component Analysis*. Springer.
[2] Shlens, J. (2014). A tutorial on principal component analysis. *arXiv preprint arXiv:1404.1100*.
[3] Baldi, P., & Sadowski, P. (2014). Understanding the bottleneck in deep autoencoders. *arXiv preprint arXiv:1301.7401*.
[4] Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. *Journal of Machine Learning Research, 9*(Nov), 2579-2605.
[5] Wattenberg, M., Viégas, F., & Johnson, I. (2018). How to use t-SNE effectively. *Distill, 3*(10), e2.
[6] McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction. *arXiv preprint arXiv:1802.03426*.
[7] Tenenbaum, J. B., De Silva, V., & Langford, J. C. (2000). A global geometric framework for nonlinear dimensionality reduction. *Science, 290*(5500), 2319-2323.
[8] Wang, L., & Li, X. (2020). Manifold learning for materials science. *npj Computational Materials, 6*(1), 1-10.
[9] Jain, A. K. (2010). Data clustering: 50 years beyond K-means. *Pattern Recognition Letters, 31*(8), 651-666.
[10] MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. *Proceedings of the fifth Berkeley symposium on mathematical statistics and probability, 1*(14), 281-297.
[11] Johnson, S. C. (1967). Hierarchical clustering schemes. *Psychometrika, 32*(3), 241-254.
[12] Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996, August). A density-based algorithm for discovering clusters in large spatial databases with noise. In *KDD* (Vol. 96, No. 34, pp. 226-231).
[13] Mehta, P., Bukov, M., Wang, X., Day, A. G. R., Seshadri, C., Green, D., ... & Schwab, D. J. (2019). A high-bias, low-variance introduction to Machine Learning for physicists. *Physics Reports, 810*, 1-124.
[14] Comon, P. (1994). Independent component analysis, A new concept?. *Signal processing, 36*(3), 287-314.
[15] Hyvärinen, A., & Oja, E. (2000). Independent component analysis: algorithms and applications. *Neural networks, 13*(4-5), 411-430.
[16] Stone, J. V. (2004). *Independent component analysis: a tutorial introduction*. MIT press.
[17] Callen, H. B. (1985). *Thermodynamics and an introduction to thermostatistics*. John Wiley & Sons.
[18] Carrasquilla, J., & Melko, R. G. (2017). Machine learning phases of matter. *Nature Physics, 13*(5), 431-434.
[19] Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: forecasting and control*. John Wiley & Sons.
[20] Fu, T. (2011). A review on time series data mining. *Transactions on Computational Science, 12*, 1-22.
[21] Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks. *Science, 313*(5786), 504-507.
[22] Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT press.
[23] Carleo, G., Cirac, I., Cranmer, K., Daudet, L., Schuld, M., Tishby, N., ... & Zdeborová, L. (2019). Machine learning and the physical sciences. *Reviews of Modern Physics, 91*(4), 045002.
[24] Kingma, D. P., & Welling, M. (2013). Auto-encoding variational Bayes. *arXiv preprint arXiv:1312.6114*.
[25] Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., ... & Bengio, Y. (2014). Generative adversarial nets. *Advances in neural information processing systems, 27*.
[26] Rezende, D. J., Mohamed, S., & Wierstra, D. (2014). Stochastic backpropagation and variational autoencoders. *arXiv preprint arXiv:1401.4082*.
[27] Stoudenmire, E. M., & Schwab, D. J. (2017). Supervised learning with quantum-inspired tensor networks. *Advances in neural information processing systems, 30*.

