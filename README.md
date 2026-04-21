# Air Quality Analysis Dashboard: Beijing Dataset

Proyek ini merupakan submission untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.
Analisis dilakukan untuk memahami pola **polusi PM2.5 di Beijing** berdasarkan data dari beberapa stasiun pemantauan kualitas udara.

Hasil analisis ditampilkan dalam bentuk **dashboard interaktif menggunakan Streamlit**.

---

# Dashboard Online

Dashboard dapat diakses secara langsung melalui link berikut:

https://air-quality-dashboardgit-3kbklstspjdyvm88p8gs5z.streamlit.app/

---

# Struktur Direktori

```text
.
├── dashboard/
│   ├── dashboard.py       # File utama aplikasi Streamlit
│   └── main_data.csv      # Dataset yang telah dibersihkan
├── data/
│   └── (Dataset mentah stasiun pemantau)
├── notebook.ipynb         # Proses analisis data
├── README.md              # Dokumentasi proyek
├── requirements.txt       # Library yang digunakan
└── url.txt                # Link dashboard online
```

---

# Setup Environment

Sebelum menjalankan dashboard secara lokal, buat environment baru agar tidak terjadi konflik library.

## Setup Environment - Anaconda

Buat environment baru:

```bash
conda create --name main-ds python=3.9
```

Aktifkan environment:

```bash
conda activate main-ds
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup Environment - Shell / Terminal

Buat folder proyek dan masuk ke direktori:

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
```

Buat virtual environment:

```bash
pipenv install
pipenv shell
```

Install library:

```bash
pip install -r requirements.txt
```

---

# Menjalankan Dashboard

Untuk menjalankan dashboard secara lokal gunakan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan berjalan pada alamat:

```
http://localhost:8501
```

---

# Dataset

Dataset yang digunakan adalah **Beijing Multi-Site Air Quality Dataset** yang berisi data kualitas udara dari beberapa stasiun pemantauan di Beijing.

Variabel utama yang dianalisis:

* **PM2.5** → Konsentrasi partikel polusi udara
* **TEMP** → Suhu udara
* **station** → Lokasi stasiun pemantau
* **month** → Bulan pengamatan

---

# Author

Submission untuk kelas **Belajar Analisis Data dengan Python – Dicoding**.
