# Proyek Analisa Atrisi HR

Repository ini berisi proyek analisis attrition karyawan: mulai dari data mentah, proses analisis, model machine learning, sampai aplikasi Streamlit untuk prediksi peluang karyawan keluar.

## Tujuan Proyek

- Mengidentifikasi faktor utama yang mendorong attrition karyawan.
- Membangun model prediksi attrition untuk membantu intervensi dini tim HR.
- Menyediakan dashboard dan aplikasi sederhana untuk pengambilan keputusan berbasis data.

## Struktur Repository

```text
Proyek_Analisa_Atrisi_HR/
├── notebook.ipynb                    # Notebook analisis & eksperimen model
├── employee_data.csv                 # Data awal karyawan
├── cleaned_dataset.csv               # Data setelah pembersihan/preprocessing
├── hasil_prediksi_attrition.csv      # Hasil prediksi label attrition
├── prediksi_probabilitas.csv         # Hasil probabilitas prediksi
├── modelprediksi.pkl                 # Model terlatih (root)
├── requirements.txt                  # Dependensi umum proyek
├── proyek_attrition/
│   ├── app.py                        # Aplikasi Streamlit prediksi attrition
│   ├── modelprediksi.pkl             # Model untuk aplikasi Streamlit
│   └── requirements.txt              # Dependensi khusus aplikasi Streamlit
└── README.md
```

## Teknologi yang Digunakan

- Python
- Pandas, NumPy
- Scikit-learn, Imbalanced-learn
- Streamlit
- Matplotlib, Seaborn

## Cara Menjalankan Proyek

### 1) Setup environment

```bash
pip install -r requirements.txt
```

### 2) Menjalankan aplikasi Streamlit

```bash
cd proyek_attrition
pip install -r requirements.txt
streamlit run app.py
```

Aplikasi online: https://prediksiatrisi.streamlit.app/

## Dashboard Bisnis

Dashboard Looker Studio:  
https://lookerstudio.google.com/reporting/7a582316-1691-41cb-88e8-e9b4075ee39b

Dashboard membantu memantau pola attrition berdasarkan faktor seperti:
- overtime
- level jabatan
- kepuasan kerja
- status pernikahan
- usia dan lama bekerja

## Insight Utama

Berdasarkan hasil modeling, faktor yang paling berpengaruh terhadap attrition antara lain:
- **OverTime**
- **StockOptionLevel**
- **JobLevel**
- **EnvironmentSatisfaction**
- **JobSatisfaction**
- **JobInvolvement**

## Rekomendasi Singkat

- Kendalikan beban lembur karyawan.
- Perjelas jalur pengembangan karier.
- Tingkatkan kepuasan dan keterlibatan kerja.
- Gunakan model prediksi untuk deteksi risiko attrition lebih awal.
