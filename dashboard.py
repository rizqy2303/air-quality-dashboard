import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    
    if 'datetime' not in df.columns:
        df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    else:
        df['datetime'] = pd.to_datetime(df['datetime'])
        
    if 'AQI_Category' not in df.columns:
        def category_pm25(value):
            if value <= 35: return "Baik"
            elif value <= 75: return "Sedang"
            elif value <= 150: return "Tidak Sehat"
            else: return "Sangat Tidak Sehat"
        df['AQI_Category'] = df['PM2.5'].apply(category_pm25)
        
    return df

main_df = load_data()

st.sidebar.header("Filter Data ")

station_list = main_df['station'].unique()

selected_station = st.sidebar.selectbox("Pilih Stasiun Pemantau:", station_list)

filtered_df = main_df[main_df['station'] == selected_station]

st.title("Dashboard Kualitas Udara Beijing ")
st.write(f"Menampilkan hasil analisis kualitas udara untuk stasiun: **{selected_station}**")

avg_pm25 = filtered_df['PM2.5'].mean()
st.metric("Rata-rata Konsentrasi PM2.5", f"{avg_pm25:.2f} µg/m³")

st.markdown("---")

st.subheader("Tren Polusi PM2.5 Bulanan")

monthly_trend = filtered_df.resample('M', on='datetime')['PM2.5'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_trend['datetime'], monthly_trend['PM2.5'], marker='o', color='#E63946', linewidth=2)
ax.set_title(f"Pergerakan PM2.5 dari 2013 - 2017 ({selected_station})", fontsize=14)
ax.set_xlabel("Waktu", fontsize=12)
ax.set_ylabel("Rata-rata PM2.5", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

st.markdown("---")

st.subheader("Distribusi Kategori Kualitas Udara")
st.write("Berdasarkan pengelompokan (Binning) nilai PM2.5")

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.countplot(
    x='AQI_Category', 
    data=filtered_df, 
    palette='viridis',
    order=['Baik', 'Sedang', 'Tidak Sehat', 'Sangat Tidak Sehat'], 
    ax=ax2
)

ax2.set_title("Frekuensi Kategori Kualitas Udara", fontsize=14)
ax2.set_xlabel("Kategori", fontsize=12)
ax2.set_ylabel("Jumlah Catatan (Jam)", fontsize=12)
st.pyplot(fig2)

st.caption("Proyek Analisis Data Dicoding - Dibuat oleh [Isi Nama Kamu]")