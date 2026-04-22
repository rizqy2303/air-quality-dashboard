# Air Quality Analysis Dashboard: Beijing Dataset

Proyek ini merupakan **submission akhir** untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.  
Tujuan proyek ini adalah menganalisis pola **polusi udara PM2.5 di Beijing** menggunakan data dari beberapa stasiun pemantauan kualitas udara dan menampilkan hasil analisis dalam bentuk **dashboard interaktif menggunakan Streamlit**.

Dashboard ini memungkinkan pengguna untuk:

- Mengidentifikasi **stasiun dengan tingkat polusi PM2.5 tertinggi**
- Melihat **tren perubahan polusi PM2.5 dari waktu ke waktu**
- Menganalisis **hubungan antara suhu udara dan konsentrasi PM2.5**

---

# Dashboard Online

Dashboard dapat diakses melalui link berikut:

https://air-quality-dashboardgit-3kbklstspjdyvm88p8gs5z.streamlit.app/

---

## Struktur Direktori

Berikut struktur direktori dari proyek ini:

```
.
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   └── dataset mentah stasiun pemantau
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

# Setup Environment

Sebelum menjalankan dashboard secara lokal, buat **virtual environment** terlebih dahulu untuk menghindari konflik versi library.

## Setup Environment - Anaconda


conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt


---

## Setup Environment - Shell/Terminal


mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt


---

# Run Streamlit App

Jalankan aplikasi Streamlit dengan perintah berikut:


streamlit run dashboard/dashboard.py


Setelah perintah dijalankan, dashboard akan berjalan pada alamat:


http://localhost:8501


---

# Dataset

Dataset yang digunakan adalah **Beijing Multi-Site Air Quality Dataset** yang berisi data kualitas udara dari beberapa stasiun pemantauan di Beijing.

Variabel utama yang digunakan dalam analisis antara lain:

- **PM2.5** : Konsentrasi partikel polusi udara
- **TEMP** : Suhu udara
- **station** : Lokasi stasiun pemantauan
- **month** : Bulan pengamatan

Dataset ini digunakan untuk mengeksplorasi pola polusi udara serta faktor lingkungan yang memengaruhi konsentrasi PM2.5.

---

# Requirements

Library yang digunakan dalam proyek ini:


pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
streamlit==1.31.1


---

# Author

Submission untuk kelas **Belajar Analisis Data dengan Python – Dicoding**.
