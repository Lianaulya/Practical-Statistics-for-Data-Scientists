# 📊 Practical Statistics for Data Scientists

Kode Python yang mereproduksi konsep, algoritma, dan contoh dari buku **Practical Statistics for Data Scientists** karya Peter Bruce, Andrew Bruce, dan Peter Gedeck (O'Reilly).

Repositori ini dibuat sebagai pemenuhan **Tugas 1 (Enrichment for Machine Learning and Deep Learning Classes) – Individual Task**.

---

## 👤 Identitas Mahasiswa

| Informasi | Keterangan |
|---|---|
| **Nama** | **Muammar Yaldi Fadhil** |
| **NIM** | **101032300019** |
| **Kelas** | **TK-47-03** |
| **Mata Kuliah** | **Machine Learning** |
| **Institusi** | **Telkom University** |

<a href="https://www.amazon.com/Practical-Statistics-Data-Scientists-Essential/dp/149207294X">
<img alt="Practical Statistics for Data Scientists Cover" src="./cover.jpeg" style="width: 200px; height: auto; padding: 10px;">
</a>

---

## 🗓️ Status Milestone Deadline

| Milestone | Cakupan Bab | Batas Waktu | Status |
|---|---|---|---|
| **Milestone 1** | **Chapter 1 – 4** | 3 Oktober 2026 (23:59) |  **SELESAI (100%)** |
| **Milestone 2** | **Chapter 5 – 6** | 17 Oktober 2026 (23:59) |  **SELESAI (100%)** |
| **Milestone 3** | **Chapter 7** | 24 Oktober 2026 (23:59) |  **SELESAI (100%)** |

---

## 📖 Daftar Notebook & Akses Google Colab

Setiap bab dapat dibuka dan dijalankan langsung di Google Colab dengan satu klik melalui tombol badge di bawah ini:

| # | Chapter | Topik Utama | Akses Colab |
|---|---------|-------------|-------------|
| 1 | [Chapter 1 – Exploratory Data Analysis](./Chapter1_EDA.ipynb) | Mean, Median, Trimmed Mean, Std Dev, IQR, Histogram, KDE, Korelasi, Scatterplot | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter1_EDA.ipynb) |
| 2 | [Chapter 2 – Data and Sampling Distributions](./Chapter2_SamplingDistributions.ipynb) | Central Limit Theorem (CLT), Bootstrap, Confidence Interval, Distribusi Normal/t/Binomial/Poisson | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter2_SamplingDistributions.ipynb) |
| 3 | [Chapter 3 – Statistical Experiments and Significance Testing](./Chapter3_StatisticalExperiments.ipynb) | A/B Testing, p-value, Uji Hipotesis, Permutation Test, t-Test, ANOVA, Chi-Square, Power & Sample Size | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter3_StatisticalExperiments.ipynb) |
| 4 | [Chapter 4 – Regression and Prediction](./Chapter4_Regression.ipynb) | Simple OLS, Multiple Linear Regression, R², RMSE, Cross-Validation, Dummy Variables, VIF, Polinomial | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter4_Regression.ipynb) |
| 5 | [Chapter 5 – Classification](./Chapter5_Classification.ipynb) | Naive Bayes, Linear Discriminant Analysis (LDA), Logistic Regression, Odds Ratio, ROC-AUC, Imbalanced Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter5_Classification.ipynb) |
| 6 | [Chapter 6 – Statistical Machine Learning](./Chapter6_StatisticalMachineLearning.ipynb) | K-Nearest Neighbors (KNN), Decision Tree (CART), Gini Impurity, Bagging, Random Forest, Boosting (AdaBoost, XGBoost) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter6_StatisticalMachineLearning.ipynb) |
| 7 | [Chapter 7 – Unsupervised Learning](./Chapter7_UnsupervisedLearning.ipynb) | Principal Component Analysis (PCA), K-Means Clustering, Elbow Method, Hierarchical Clustering (Dendrogram) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lianaulya/Practical-Statistics-for-Data-Scientists/blob/main/Chapter7_UnsupervisedLearning.ipynb) |

---

## 💻 Cara Menjalankan

### Opsi 1: Google Colab (Direkomendasikan — Tanpa Instalasi Lokal)
Klik tombol **"Open in Colab"** pada tabel di atas. Seluruh dependensi dan dataset akan termuat secara otomatis.

### Opsi 2: Lokal

```bash
# 1. Clone repository
git clone https://github.com/Lianaulya/Practical-Statistics-for-Data-Scientists.git
cd Practical-Statistics-for-Data-Scientists

# 2. Buat virtual environment (opsional)
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan Jupyter Notebook / Lab
jupyter notebook
```

---

## 📦 Requirements

```
matplotlib
pandas
scikit-learn
scipy
statsmodels
wquantiles
seaborn
pygam
dmba
pydotplus
imblearn
xgboost
prince
numpy
adjustText
```

Seluruh 19 dataset resmi tersimpan secara lokal di folder `data/` dan dapat pula diakses langsung melalui raw URL repositori resmi buku.

---

## 🔬 Ringkasan Materi Lengkap Setiap Bab

### Chapter 1 – Exploratory Data Analysis (EDA)
Teknik eksplorasi data untuk menemukan pola, anomali, dan hubungan antar variabel:
- **Estimasi Lokasi**: Mean, Trimmed Mean, Weighted Mean, Median.
- **Estimasi Variabilitas**: Standard Deviation, Variance, Mean Absolute Deviation (MAD), Interquartile Range (IQR).
- **Percentile & Boxplot**: Deteksi outlier menggunakan kuartil ($Q_1$, $Q_2$, $Q_3$) dan whiskers ($1.5 \times \text{IQR}$).
- **Histogram & Density Plot**: Visualisasi estimasi kepadatan probabilitas (Kernel Density Estimation / KDE).
- **Korelasi**: Koefisien korelasi Pearson $r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{(n-1) s_x s_y}$ dan heatmap korelasi.

### Chapter 2 – Data and Sampling Distributions
Distribusi statistik dan prinsip pengambilan sampel:
- **Central Limit Theorem (CLT)**: Distribusi rata-rata sampel mendekati distribusi normal seiring membesarnya ukuran sampel $n$.
- **Bootstrap**: Resampling dengan pengembalian untuk mengestimasi distribusi sampling tanpa asumsi parametrik.
- **Confidence Interval (CI)**: Interval kepercayaan 95% ($x̄ \pm 1.96 \cdot \text{SE}$).
- **Distribusi Teoretis**: Distribusi Normal, Distribusi $t$-Student (heavy-tailed), Distribusi Binomial, dan Distribusi Poisson.

### Chapter 3 – Statistical Experiments and Significance Testing
Desain eksperimen, pengujian hipotesis, dan inferensi kausal:
- **A/B Testing**: Membandingkan efektivitas dua perlakuan (Control vs. Treatment).
- **Uji Hipotesis & p-value**: Hipotesis Nol ($H_0$), Hipotesis Alternatif ($H_a$), tingkat signifikansi $\alpha = 0.05$.
- **Permutation Test**: Uji non-parametrik berbasis resampling acak untuk menguji signifikansi perbedaan kelompok.
- **ANOVA (Analysis of Variance)**: Uji beda rata-rata untuk $\ge 3$ kelompok menggunakan statistik $F$.
- **Chi-Square Test**: Uji independensi dan goodness-of-fit variabel kategorik.
- **Power & Sample Size**: Penentuan ukuran sampel minimum untuk mencapai daya uji (*statistical power*) yang memadai.

### Chapter 4 – Regression and Prediction
Pemodelan hubungan linier dan evaluasi prediksi:
- **Simple Linear Regression (OLS)**: Meminimalkan jumlah kuadrat residual $\hat{y} = b_0 + b_1 x$.
- **Multiple Regression**: Memodelkan target dengan banyak prediktor $\hat{y} = b_0 + b_1 x_1 + \dots + b_p x_p$.
- **Evaluasi Model**: $R^2$ (koefisien determinasi) dan RMSE (*Root Mean Squared Error*).
- **Cross-Validation**: $k$-fold cross-validation untuk estimasi generalisasi out-of-sample.
- **Variabel Kategorik**: One-hot / dummy encoding ($k-1$ kolom).
- **Multikolinieritas**: Deteksi korelasi antar prediktor dengan *Variance Inflation Factor* (VIF).
- **Polynomial & Spline Regression**: Menangkap hubungan non-linier.

### Chapter 5 – Classification
Prediksi kategori target biner maupun multikelas:
- **Naive Bayes**: Pengklasifikasi berbasis probabilitas posterior dengan asumsi independensi fitur kondisional.
- **Discriminant Analysis (LDA & QDA)**: Memaksimalkan separabilitas antar-kelas di ruang proyeksi linier.
- **Logistic Regression**: Memodelkan log-odds (*logit*) sebagai fungsi linier dari prediktor:
  $$\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$$
- **Evaluasi Klasifikasi**: Confusion matrix, Sensitivity/Recall, Specificity, Precision, ROC Curve, dan AUC (*Area Under Curve*).
- **Strategi Imbalanced Data**: Undersampling, oversampling (SMOTE), dan penyesuaian threshold.

### Chapter 6 – Statistical Machine Learning
Algoritma pembelajaran mesin modern dan metode ensemble:
- **K-Nearest Neighbors (KNN)**: Prediksi berbasis mayoritas tetangga terdekat dalam ruang fitur terstandarisasi.
- **Decision Trees (CART)**: Partisi ruang fitur berbasis metrik kemurnian Gini Impurity ($I_G = 1 - \sum p_i^2$) atau Information Gain.
- **Bagging & Random Forest**: Ensemble pohon keputusan independen dengan *bootstrap sampling* dan *random feature subspace selection* untuk mereduksi variansi.
- **Boosting**: Pembelajaran ensemble sekuensial (AdaBoost, Gradient Boosting, XGBoost) yang mengoreksi residual iterasi sebelumnya.

### Chapter 7 – Unsupervised Learning
Pembelajaran tanpa label untuk ekstraksi struktur laten dan pengelompokan:
- **Principal Components Analysis (PCA)**: Reduksi dimensi ortogonal untuk menangkap variansi maksimum data multivariat.
- **K-Means Clustering**: Pengelompokan data ke dalam $K$ klaster dengan meminimalkan *within-cluster sum of squares* (WCSS).
- **Evaluasi Klaster**: Penentuan $K$ optimal menggunakan *Elbow Method* dan *Silhouette Score*.
- **Hierarchical Clustering**: Pengelompokan bertingkat (*agglomerative*) dengan visualisasi pohon relasi (*Dendrogram*).

---

## 🔗 Referensi & Sumber Rujukan

- **Buku Utama:** Bruce, Peter, Andrew Bruce, and Peter Gedeck. *Practical Statistics for Data Scientists: 50+ Essential Concepts Using R and Python* (2nd ed.). O'Reilly Media, 2020.
- **Tautan Buku (Google Drive):** [Google Drive - Practical Statistics for Data Scientists](https://drive.google.com/file/d/1dR9228_PRCN5_Hjs9ClxYgKe5zmifkmb/view?usp=sharing)
- **Repositori Resmi Buku:** [gedeck/practical-statistics-for-data-scientists](https://github.com/gedeck/practical-statistics-for-data-scientists)
- **Repositori Rujukan Tugas:** [farrelrassya/Practical-Statistics-for-Data-Scientist-Books](https://github.com/farrelrassya/Practical-Statistics-for-Data-Scientist-Books)
