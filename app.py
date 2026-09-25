import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Clustering Ekonomi Kecamatan Kabupaten Bogor",
    page_icon="🏙️",
    layout="wide"
)

# Header Utama
st.title("🏙️ Dashboard Segmentasi Ekonomi Kecamatan Kabupaten Bogor")
st.markdown("""
Aplikasi analitik prediktif berbasis **K-Means Clustering** untuk mengelompokkan 40 kecamatan 
di Kabupaten Bogor berdasarkan indikator ekonomi pasar rumah tangga (Ukuran Pasar, Rata-Rata Konsumen, dan Laju Pertumbuhan).
""")

# Load Model dan Scaler
@st.cache_resource
def load_artifacts():
    model = joblib.load('model_kmeans_kecamatan.pkl')
    scaler = joblib.load('scaler_kecamatan.pkl')
    return model, scaler

@st.cache_data
def load_data():
    return pd.read_csv('hasil_clustering_kecamatan_bogor.csv')

try:
    model, scaler = load_artifacts()
    df_data = load_data()
    data_loaded = True
except Exception as e:
    st.warning(f"File model atau data belum siap: {e}. Pastikan notebook sudah dijalankan sampai sel terakhir.")
    data_loaded = False

if data_loaded:
    st.subheader("📝 Prediksi Klaster Wilayah / Kecamatan Baru:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        ukuran_pasar = st.number_input(
            "Ukuran Pasar Terkini (Jumlah RT dalam Ribuan):",
            min_value=1.0, max_value=300.0, value=75.0, step=1.0,
            help="Jumlah rumah tangga kecamatan pada tahun 2023 (contoh: 75.0 = 75.000 RT)"
        )
    with col2:
        rata_rata_konsumen = st.number_input(
            "Rata-Rata Rumah Tangga 4 Tahun Terakhir (Ribuan):",
            min_value=1.0, max_value=300.0, value=65.0, step=1.0,
            help="Rata-rata jumlah rumah tangga tahun 2020-2023"
        )
    with col3:
        pertumbuhan = st.number_input(
            "Laju Pertumbuhan Pasar (%):",
            min_value=-100.0, max_value=1000.0, value=120.0, step=5.0,
            help="Persentase pertumbuhan rumah tangga dari 2020 ke 2023"
        )

    if st.button("🚀 Prediksi Klaster Wilayah"):
        input_data = np.array([[ukuran_pasar, rata_rata_konsumen, pertumbuhan]])
        input_scaled = scaler.transform(input_data)
        pred_cluster = model.predict(input_scaled)[0]

        mapping_segmen = {
            0: {
                "nama": "Hub Komersial & Pertumbuhan Agresif (Tier 1)",
                "warna": "#d95f02",
                "deskripsi": "Kecamatan penyangga urban utama dengan lonjakan populasi ekstrem dan ukuran pasar sangat besar.",
                "rekomendasi": "Ekspansi ritel modern berskala besar, pusat logistik & pergudangan, properti residensial vertikal, serta kantor cabang perbankan."
            },
            1: {
                "nama": "Pusat Perdagangan Terbentuk / Skala Besar (Tier 2)",
                "warna": "#2b5c8f",
                "deskripsi": "Kecamatan dengan basis konsumen yang sudah matang, stabil, dan memiliki volume pasar tinggi.",
                "rekomendasi": "Distribusi barang konsumsi harian (FMCG), penguatan pasar grosir lokal, pembiayaan UMKM komersial, dan jaringan ritel minimarket."
            },
            2: {
                "nama": "Pasar Perintis / Skala Terbatas (Tier 3)",
                "warna": "#2ca02c",
                "deskripsi": "Kecamatan bercorak agraris, wisata alam, atau permukiman berkepadatan rendah hingga sedang.",
                "rekomendasi": "Fokus pada investasi agrowisata/eco-resort, jaringan logistik rantai pasok komunitas, dan fasilitas infrastruktur dasar."
            }
        }

        res = mapping_segmen.get(pred_cluster, {"nama": f"Klaster {pred_cluster}", "warna": "#333", "deskripsi": "", "rekomendasi": ""})

        st.success(f"### Hasil Prediksi: **{res['nama']}**")
        st.write(f"**Karakteristik Wilayah:** {res['deskripsi']}")
        st.info(f"**Rekomendasi Strategi Bisnis & Investasi:**\n\n{res['rekomendasi']}")

    st.markdown("---")
    st.subheader("📊 Database Hasil Clustering 40 Kecamatan di Kabupaten Bogor")

    pilihan_klaster = st.multiselect(
        "Filter berdasarkan Klaster:",
        options=list(df_data['Nama_Segmen'].unique()),
        default=list(df_data['Nama_Segmen'].unique())
    )

    filtered_df = df_data[df_data['Nama_Segmen'].isin(pilihan_klaster)]
    
    tampil_kolom = ['Kecamatan', 'Nama_Segmen', 'Ukuran_Pasar_2023', 'Rata_Rata_Konsumen', 'Pertumbuhan_Pasar_Pct', 'RT_2020', 'RT_2023']
    st.dataframe(filtered_df[tampil_kolom], use_container_width=True)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data Hasil Segmentasi (CSV)",
        data=csv_data,
        file_name='hasil_clustering_kecamatan_bogor.csv',
        mime='text/csv'
    )