# 🏙️ Analisis Segmentasi Ekonomi 40 Kecamatan di Kabupaten Bogor Berbasis K-Means Clustering

Aplikasi machine learning berbasis web untuk mengelompokkan 40 kecamatan di wilayah Kabupaten Bogor berdasarkan indikator stabilitas, ukuran pasar konsumen, dan laju pertumbuhan ekonomi rumah tangga. Proyek ini dibangun menggunakan Python, Scikit-Learn, dan di-deploy secara interaktif menggunakan Streamlit Community Cloud.

---

## 📌 Ringkasan Proyek

Pertumbuhan ekonomi dan konsentrasi pemukiman di Kabupaten Bogor memiliki disparitas antarwilayah yang signifikan. Proyek ini bertujuan untuk membantu pengambil keputusan, pelaku usaha, dan perencana wilayah dalam mengidentifikasi profil pasar kecamatan melalui teknik pembelajaran mesin tanpa pengawasan (*unsupervised learning*).

### Indikator Fitur yang Digunakan:
1. **Ukuran Pasar 2023 (`Ukuran_Pasar_2023`)**: Total estimasi jumlah rumah tangga terkini pada tahun 2023 (dalam ribuan unit).
2. **Rata-Rata Konsumen (`Rata_Rata_Konsumen`)**: Rata-rata populasi rumah tangga selama 4 tahun (2020–2023) sebagai tolok ukur stabilitas pasar.
3. **Laju Pertumbuhan Pasar (`Pertumbuhan_Pasar_Pct`)**: Persentase dinamika kenaikan atau penurunan rumah tangga dari tahun 2020 ke 2023.

---

## 🎯 Hasil Pengelompokan (K-Means $k=3$)

Berdasarkan pengujian evaluasi menggunakan *Elbow Method* dan *Silhouette Score*, nilai klaster optimal adalah **$k = 3$** (Silhouette Score: **0.325**):

| Klaster | Nama Segmen | Karakteristik Wilayah | Rekomendasi Strategis |
| :---: | :--- | :--- | :--- |
| **0** | **Hub Komersial & Pertumbuhan Agresif (Tier 1)** | Wilayah penyangga urban dengan lonjakan pertumbuhan tinggi dan basis konsumen masif. | Ekspansi ritel modern skala besar, fasilitas logistik/pergudangan, dan properti vertikal. |
| **1** | **Pusat Perdagangan Terbentuk / Skala Besar (Tier 2)** | Wilayah perkotaan matang dengan volume konsumen stabil dan daya beli mapan. | Distribusi produk FMCG harian, penguatan sentra grosir, dan perluasan jaringan minimarket. |
| **2** | **Pasar Perintis / Skala Terbatas (Tier 3)** | Wilayah bercorak agraris, eco-wisata, atau densitas populasi rendah hingga sedang. | Investasi agrowisata, rantai pasok komunitas lokal, dan pemenuhan infrastruktur primer. |

---

## 📁 Struktur Repositori

```text
├── Data_Rumah_Tangga_Rapi.csv            # Dataset mentah statistik rumah tangga 2020-2023
├── hasil_clustering_kecamatan_bogor.csv  # Dataset hasil segmentasi 40 kecamatan
├── model_kmeans_kecamatan.pkl            # Model K-Means hasil serialisasi joblib
├── scaler_kecamatan.pkl                  # Model StandardScaler hasil serialisasi joblib
├── app.py                                # Skrip aplikasi web interaktif Streamlit
├── requirements.txt                      # Daftar dependensi modul Python
├── Clustering_Kecamatan_Bogor.ipynb      # Notebook eksperimen & analisis data eksploratif
└── README.md                             # Dokumentasi proyek
