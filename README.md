# Proyek Analisis Data: Kualitas Udara Beijing (Air Quality Dataset)

Proyek ini merupakan submission akhir untuk kelas **Belajar Analisis Data dengan Python** di platform Dicoding.  
Tujuan dari proyek ini adalah melakukan analisis terhadap dataset kualitas udara dari berbagai stasiun pemantau di Beijing.

Proses analisis yang dilakukan meliputi:

- Data Wrangling (pembersihan dan penggabungan data)
- Exploratory Data Analysis (EDA)
- Visualisasi data
- Pembuatan dashboard interaktif

Hasil analisis kemudian divisualisasikan dalam bentuk **dashboard interaktif menggunakan Streamlit** sehingga pengguna dapat melihat tren polusi udara dengan lebih mudah.

---

# Dashboard Online

Dashboard dapat diakses melalui link berikut:

https://air-quality-dashboardgit-3kbklstspjdyvm88p8gs5z.streamlit.app/

Dashboard ini menampilkan:

- Rata-rata konsentrasi PM2.5
- Tren polusi udara per bulan
- Distribusi kategori kualitas udara
- Filter berdasarkan stasiun pemantau

---

# Struktur Direktori

submission
│
├── dashboard
│   ├── dashboard.py
│   └── main_data.zip
│
├── data
│   └── dataset mentah dari berbagai stasiun pemantau
│
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt

Penjelasan:

dashboard/  
Berisi file utama dashboard Streamlit (dashboard.py) serta dataset yang telah dibersihkan.

data/  
Berisi dataset mentah CSV dari berbagai stasiun pemantau kualitas udara.

notebook.ipynb  
Berisi seluruh proses analisis data mulai dari data wrangling, exploratory data analysis (EDA), hingga visualisasi.

requirements.txt  
Daftar library Python yang dibutuhkan untuk menjalankan proyek.

url.txt  
Berisi link dashboard yang telah di-deploy.

---

# Setup Environment (Menjalankan Dashboard di Lokal)

Jika ingin menjalankan dashboard di komputer lokal, lakukan langkah berikut:

1. Clone repository

git clone https://github.com/username/air-quality-dashboard.git

2. Masuk ke folder proyek

cd air-quality-dashboard

3. Install semua dependency

pip install -r requirements.txt

4. Jalankan aplikasi Streamlit

streamlit run dashboard/dashboard.py

Setelah dijalankan, dashboard akan terbuka di browser pada alamat:

http://localhost:8501

---

# Library yang Digunakan

Beberapa library utama yang digunakan dalam proyek ini:

- pandas
- matplotlib
- seaborn
- streamlit

---

# Kesimpulan

Berdasarkan analisis yang dilakukan, data kualitas udara menunjukkan bahwa beberapa stasiun pemantau memiliki tingkat PM2.5 yang cukup tinggi, yang dapat berdampak pada kualitas udara dan kesehatan masyarakat.

Melalui dashboard interaktif ini, pengguna dapat dengan mudah:

- memantau tren kualitas udara
- membandingkan antar stasiun pemantau
- memahami distribusi kategori kualitas udara
