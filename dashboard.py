import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set tema seaborn
sns.set(style="darkgrid")

# 1. Load Data
@st.cache_data
def load_data():
    # Pastikan file ini ada di GitHub kamu dengan nama yang sama
    df = pd.read_csv("main_data.zip") 

    # Konversi datetime
    df["datetime"] = pd.to_datetime(
        df[["year", "month", "day", "hour"]],
        errors="coerce"
    )
    df = df.dropna(subset=["datetime"])

    # Binning Kualitas Udara (Sesuai dengan Notebook)
    if "quality_category" not in df.columns:
        bins = [0, 35, 75, 150, 500]
        labels = ["Baik", "Sedang", "Tidak Sehat", "Sangat Tidak Sehat"]
        df["quality_category"] = pd.cut(df["PM2.5"], bins=bins, labels=labels)

    return df

main_df = load_data()

# --- SIDEBAR ---
st.sidebar.header("Filter Dashboard")
station_list = main_df["station"].unique()
selected_station = st.sidebar.selectbox("Pilih Stasiun Pemantau", station_list)

# Filter Data Berdasarkan Stasiun
filtered_df = main_df[main_df["station"] == selected_station]

# --- MAIN PAGE ---
st.title("📊 Air Quality Dashboard: Beijing")
st.markdown(f"Analisis kualitas udara untuk stasiun: **{selected_station}**")

# Row 1: Metrics
avg_pm25 = filtered_df["PM2.5"].mean()
max_pm25 = filtered_df["PM2.5"].max()

col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata PM2.5", f"{avg_pm25:.2f} µg/m³")
with col2:
    st.metric("PM2.5 Tertinggi", f"{max_pm25:.2f} µg/m³")

st.divider()

# Row 2: Tren Bulanan (Menjawab Pertanyaan 1)
st.subheader("1. Tren Konsentrasi PM2.5 Bulanan")
filtered_df["year_month"] = filtered_df["datetime"].dt.to_period("M").astype(str)
monthly_trend = filtered_df.groupby("year_month")["PM2.5"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.lineplot(x="year_month", y="PM2.5", data=monthly_trend, marker="o", color="red", ax=ax1)
plt.xticks(rotation=45)
ax1.set_xlabel("Periode")
ax1.set_ylabel("Rata-rata PM2.5")
st.pyplot(fig1)

st.divider()

# Row 3: Korelasi Cuaca (Menjawab Pertanyaan 2)
st.subheader("2. Hubungan Suhu (TEMP) terhadap Polusi")
fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.scatterplot(x="TEMP", y="PM2.5", data=filtered_df, alpha=0.3, color="orange", ax=ax2)
ax2.set_xlabel("Suhu (°C)")
ax2.set_ylabel("Konsentrasi PM2.5")
st.pyplot(fig2)
st.info("Visualisasi ini menunjukkan bagaimana polusi meningkat saat suhu udara menurun (musim dingin).")

st.divider()

# Row 4: Distribusi Kategori
st.subheader("3. Distribusi Kategori Kualitas Udara")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.countplot(x="quality_category", data=filtered_df, palette="Reds_r", ax=ax3)
ax3.set_xlabel("Kategori")
ax3.set_ylabel("Jumlah Data")
st.pyplot(fig3)

st.caption(f"Copyright © 2026 - {selected_station} Air Quality Analysis - Rizqy")
