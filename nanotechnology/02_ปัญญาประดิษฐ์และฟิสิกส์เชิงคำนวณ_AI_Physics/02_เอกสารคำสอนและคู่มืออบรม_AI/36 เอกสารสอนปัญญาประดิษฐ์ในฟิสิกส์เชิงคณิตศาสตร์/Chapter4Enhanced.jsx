import React from 'react';
// Removed react-syntax-highlighter imports to fix build issues

const Chapter4Enhanced = () => {
    const codePCA = `
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
    `;

    const codeTSNE = `
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
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('t-SNE of Molecular Dynamics Simulation Data')
plt.colorbar(label='Artificial Group')
plt.grid(True)
plt.show()
    `;

    const codeKMeans = `
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
plt.scatter(X_cluster_scaled[:, 0], X_cluster_scaled[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, alpha=0.7, marker='X', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.legend()
plt.grid(True)

# 5. Apply Hierarchical Clustering (ตัวอย่าง)
agg_clustering = AgglomerativeClustering(n_clusters=4)
y_agg = agg_clustering.fit_predict(X_cluster_scaled)
plt.subplot(1, 2, 2)
plt.scatter(X_cluster_scaled[:, 0], X_cluster_scaled[:, 1], c=y_agg, s=50, cmap='viridis')
plt.title('Hierarchical Clustering')
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.grid(True)

plt.tight_layout()
plt.show()
    `;

    return (
        <div className="p-6 bg-gray-50 text-gray-800">
            <h1 className="text-3xl font-bold mb-4 text-center text-purple-600">บทที่ 4: การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning) และการค้นพบโครงสร้าง</h1>
            
            <div className="mb-8 p-4 border-l-4 border-purple-500 bg-purple-100">
                <h2 className="text-2xl font-semibold mb-2">วัตถุประสงค์การเรียนรู้</h2>
                <ul className="list-disc ml-6">
                    <li>เรียนรู้เทคนิคการลดมิติ (Dimensionality Reduction) และการจัดกลุ่ม (Clustering)</li>
                    <li>นำเทคนิคไปใช้ในการค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลฟิสิกส์</li>
                    <li>เข้าใจการประยุกต์ใช้ในการสำรวจและสร้างสมมติฐานจากข้อมูล</li>
                </ul>
            </div>

            {/* Section 4.1 */}
            <div className="mb-8">
                <h2 className="text-2xl font-bold mb-2 text-purple-700">4.1 การวิเคราะห์องค์ประกอบหลัก (Principal Component Analysis - PCA): ทฤษฎีและการประยุกต์ใช้</h2>
                <p className="mb-4">
                    <strong>Principal Component Analysis (PCA)</strong> เป็นเทคนิคการลดมิติข้อมูลที่ใช้กันอย่างแพร่หลาย โดยมีเป้าหมายเพื่อแปลงชุดข้อมูลที่มีมิติสูงให้เป็นชุดข้อมูลที่มีมิติที่ต่ำลง โดยยังคงรักษาข้อมูลที่สำคัญที่สุดไว้ให้ได้มากที่สุด หลักการของ PCA คือการหาแกนหลัก (principal components) ซึ่งเป็นทิศทางที่ข้อมูลมีการกระจายตัวมากที่สุด
                </p>
                <pre className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
                    <code>{codePCA}</code>
                </pre>
            </div>

            {/* Section 4.2 */}
            <div className="mb-8">
                <h2 className="text-2xl font-bold mb-2 text-purple-700">4.2 เทคนิคการลดมิติแบบไม่เชิงเส้น: t-SNE, UMAP และ Manifold Learning</h2>
                <p className="mb-4">
                    ในขณะที่ PCA เป็นเทคนิคการลดมิติแบบเชิงเส้น ที่มีประสิทธิภาพ แต่บางครั้งข้อมูลในโลกแห่งความเป็นจริงอาจมีโครงสร้างที่ไม่เชิงเส้น ซึ่ง PCA อาจไม่สามารถจับภาพได้ดีนัก ในกรณีเช่นนี้ เทคนิคการลดมิติแบบไม่เชิงเส้น เช่น t-SNE, UMAP และ Manifold Learning จะเข้ามามีบทบาทสำคัญ
                </p>
                <pre className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
                    <code>{codeTSNE}</code>
                </pre>
            </div>

            {/* Section 4.3 */}
            <div className="mb-8">
                <h2 className="text-2xl font-bold mb-2 text-purple-700">4.3 อัลกอริทึมการจัดกลุ่ม: K-Means, Hierarchical Clustering และ DBSCAN</h2>
                <p className="mb-4">
                    การจัดกลุ่ม (Clustering) เป็นเทคนิคการเรียนรู้แบบไม่มีผู้สอนที่สำคัญ ซึ่งมีเป้าหมายในการจัดระเบียบชุดข้อมูลให้เป็นกลุ่มย่อยๆ (clusters) โดยที่ข้อมูลภายในกลุ่มเดียวกันมีความคล้ายคลึงกันสูง และข้อมูลต่างกลุ่มกันมีความคล้ายคลึงกันต่ำ การจัดกลุ่มมีประโยชน์อย่างมากในการสำรวจข้อมูล และการค้นหารูปแบบที่ซ่อนอยู่ในข้อมูลฟิสิกส์
                </p>
                <pre className="bg-gray-900 text-green-400 p-4 rounded-lg overflow-x-auto">
                    <code>{codeKMeans}</code>
                </pre>
            </div>

            {/* Quiz for Chapter 4 */}
            <div className="mt-10 p-6 border-t-2 border-purple-300">
                <h3 className="text-xl font-bold mb-4">แบบทดสอบบทที่ 4</h3>
                <ul className="list-decimal ml-6 space-y-4">
                    <li>
                        <p>PCA มีวัตถุประสงค์หลักเพื่ออะไร?</p>
                        <ul className="list-disc ml-6 mt-2">
                            <li>a) เพิ่มจำนวนฟีเจอร์ในข้อมูล</li>
                            <li>b) ลดมิติข้อมูลโดยยังคงรักษาข้อมูลที่สำคัญ</li>
                            <li>c) จัดกลุ่มข้อมูลที่มีความคล้ายคลึงกัน</li>
                            <li>d) ทำนายค่าตัวแปรตาม</li>
                        </ul>
                    </li>
                    <li>
                        <p>ข้อใดคือข้อจำกัดหลักของ PCA เมื่อเทียบกับ t-SNE หรือ UMAP?</p>
                        <ul className="list-disc ml-6 mt-2">
                            <li>a) PCA ไม่สามารถจัดการกับข้อมูลที่มีมิติสูงได้</li>
                            <li>b) PCA ไม่สามารถรักษาโครงสร้างเชิงเส้นของข้อมูลได้</li>
                            <li>c) PCA มีประสิทธิภาพต่ำในการจับภาพโครงสร้างข้อมูลที่ไม่เชิงเส้น</li>
                            <li>d) PCA ใช้เวลาในการประมวลผลนานกว่า</li>
                        </ul>
                    </li>
                    <li>
                        <p>อัลกอริทึมการจัดกลุ่มใดที่ต้องการให้ผู้ใช้กำหนดจำนวนกลุ่ม (k) ล่วงหน้า?</p>
                        <ul className="list-disc ml-6 mt-2">
                            <li>a) DBSCAN</li>
                            <li>b) Hierarchical Clustering</li>
                            <li>c) K-Means</li>
                            <li>d) ทั้งหมดที่กล่าวมา</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    );
};

export default Chapter4Enhanced;

