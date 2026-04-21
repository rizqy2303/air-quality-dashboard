# Air Quality Analysis Dashboard: Beijing Dataset

Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** di platform Dicoding.
Tujuan proyek ini adalah melakukan analisis terhadap kualitas udara di Beijing dengan fokus pada **polusi PM2.5**, serta menyajikan hasil analisis dalam bentuk **dashboard interaktif menggunakan Streamlit**.

Dashboard menampilkan:

* Perbandingan rata-rata polusi antar stasiun pemantau
* Tren polusi PM2.5 dari waktu ke waktu
* Hubungan antara suhu udara dan konsentrasi PM2.5

---

# Struktur Direktori

Pastikan struktur folder proyek sebagai berikut agar dashboard dapat berjalan dengan baik.

```
.
├── dashboard/
│   ├── dashboard.py       # File utama aplikasi Streamlit
│   └── main_data.csv      # Dataset yang telah dibersihkan
├── data/
│   └── (Dataset mentah dari stasiun pemantau)
├── notebook.ipynb         # Notebook analisis data
├── README.md              # Dokumentasi proyek
├── requirements.txt       # Daftar library yang dibutuhkan
└── url.txt                # Link dashboard online
```

---

# Setup Environment

Sebelum menjalankan dashboard, disarankan untuk membuat **environment baru** agar tidak terjadi konflik versi library.

## Setup Environment - Anaconda

Buat environment baru:

```
conda create --name main-ds python=3.9
```

Aktifkan environment:

```
conda activate main-ds
```

Install semua library yang dibutuhkan:

```
pip install -r requirements.txt
```

---

## Setup Environment - Shell / Terminal (Pipenv)

Buat folder proyek dan masuk ke direktori tersebut:

```
mkdir proyek_analisis_data
cd proyek_analisis_data
```

Install pipenv:

```
pip install pipenv
```

Buat virtual environment:

```
pipenv install
```

Aktifkan environment:

```
pipenv shell
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Menjalankan Dashboard Streamlit

Setelah environment aktif dan library terinstal, jalankan dashboard dengan perintah berikut:

```
streamlit run dashboard/dashboard.py
```

Dashboard akan otomatis terbuka di browser pada alamat:

```
http://localhost:8501
```

---

# Dataset

Dataset yang digunakan berasal dari **Beijing Multi-Site Air Quality Dataset** yang berisi data kualitas udara dari beberapa stasiun pemantauan di Beijing.

Variabel utama yang dianalisis antara lain:

* **PM2.5** → Konsentrasi partikel polusi udara
* **TEMP** → Suhu udara
* **station** → Lokasi stasiun pemantau
* **month** → Bulan pengamatan

---

# Author

Proyek ini dibuat sebagai bagian dari submission kelas **Belajar Analisis Data dengan Python – Dicoding**.
