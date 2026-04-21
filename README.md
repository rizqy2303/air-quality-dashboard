# Air Quality Analysis Dashboard: Beijing Dataset

Proyek ini merupakan **submission akhir** untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.
Tujuan proyek ini adalah menganalisis pola **polusi udara PM2.5 di Beijing** menggunakan data dari beberapa stasiun pemantauan kualitas udara, serta menyajikan hasil analisis dalam bentuk **dashboard interaktif menggunakan Streamlit**.

Dashboard ini membantu pengguna untuk:

* Mengidentifikasi **stasiun dengan tingkat polusi tertinggi**
* Melihat **tren polusi PM2.5 berdasarkan waktu**
* Memahami **hubungan antara suhu udara dan konsentrasi PM2.5**

---

# Dashboard Online

Dashboard dapat diakses secara langsung melalui tautan berikut:

https://air-quality-dashboardgit-3kbklstspjdyvm88p8gs5z.streamlit.app/

---

# Struktur Direktori

Berikut adalah struktur direktori proyek yang digunakan:

```
.
├── dashboard/
│   ├── dashboard.py       # File utama aplikasi Streamlit
│   └── main_data.csv      # Dataset hasil pembersihan data
├── data/
│   └── (Dataset mentah dari stasiun pemantau)
├── notebook.ipynb         # Notebook proses analisis data
├── README.md              # Dokumentasi proyek
├── requirements.txt       # Daftar library yang digunakan
└── url.txt                # Link dashboard online
```

---

# Setup Environment

Sebelum menjalankan dashboard secara lokal, disarankan untuk membuat **virtual environment** agar tidak terjadi konflik versi library.

## Setup Environment menggunakan Anaconda

Buat environment baru:

```
conda create --name main-ds python=3.9
```

Aktifkan environment:

```
conda activate main-ds
```

Install semua dependencies yang dibutuhkan:

```
pip install -r requirements.txt
```

---

## Setup Environment menggunakan Shell / Terminal (Pipenv)

Buat direktori proyek:

```
mkdir proyek_analisis_data
cd proyek_analisis_data
```

Buat dan aktifkan virtual environment:

```
pipenv install
pipenv shell
```

Install dependencies proyek:

```
pip install -r requirements.txt
```

---

# Menjalankan Dashboard

Setelah environment aktif dan semua library terinstal, jalankan aplikasi Streamlit dengan perintah berikut:

```
streamlit run dashboard/dashboard.py
```

Setelah perintah dijalankan, dashboard akan terbuka secara otomatis di browser pada alamat:

```
http://localhost:8501
```

---

# Dataset

Dataset yang digunakan adalah **Beijing Multi-Site Air Quality Dataset**, yang berisi data kualitas udara dari beberapa stasiun pemantauan di Beijing.

Beberapa variabel utama yang dianalisis dalam proyek ini antara lain:

* **PM2.5** : Konsentrasi partikel polusi udara berukuran kecil
* **TEMP** : Suhu udara
* **station** : Lokasi stasiun pemantau kualitas udara
* **month** : Bulan pengamatan data

Dataset ini digunakan untuk mengeksplorasi pola polusi udara serta faktor lingkungan yang memengaruhi tingkat konsentrasi PM2.5.

---

# Author

Proyek ini dibuat sebagai bagian dari submission pada kelas **Belajar Analisis Data dengan Python** di platform **Dicoding**.
