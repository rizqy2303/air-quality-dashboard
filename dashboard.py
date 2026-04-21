import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="darkgrid")

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.zip", compression="zip")

    df["datetime"] = pd.to_datetime(
        df[["year", "month", "day", "hour"]],
        errors="coerce"
    )

    df = df.dropna(subset=["datetime"])

    if "AQI_Category" not in df.columns:
        def category_pm25(x):
            if x <= 35:
                return "Baik"
            elif x <= 75:
                return "Sedang"
            elif x <= 150:
                return "Tidak Sehat"
            else:
                return "Sangat Tidak Sehat"

        df["AQI_Category"] = df["PM2.5"].apply(category_pm25)

    return df


main_df = load_data()

st.sidebar.header("Filter Data")

station_list = main_df["station"].unique()

selected_station = st.sidebar.selectbox(
    "Pilih Stasiun",
    station_list
)

filtered_df = main_df[main_df["station"] == selected_station]

st.title("Dashboard Kualitas Udara Beijing")

st.write(
    f"Menampilkan hasil analisis kualitas udara untuk stasiun: **{selected_station}**"
)

avg_pm25 = filtered_df["PM2.5"].mean()

st.metric(
    "Rata-rata Konsentrasi PM2.5",
    f"{avg_pm25:.2f} µg/m³"
)

st.markdown("---")

st.subheader("Tren Polusi PM2.5 Bulanan")

filtered_df = filtered_df.sort_values("datetime")

filtered_df["year_month"] = filtered_df["datetime"].dt.to_period("M")

monthly_trend = (
    filtered_df
    .groupby("year_month")["PM2.5"]
    .mean()
    .reset_index()
)

monthly_trend["year_month"] = monthly_trend["year_month"].astype(str)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    monthly_trend["year_month"],
    monthly_trend["PM2.5"],
    marker="o",
    linewidth=2
)

ax.set_title(
    f"Pergerakan PM2.5 2013-2017 ({selected_station})"
)

ax.set_xlabel("Bulan")
ax.set_ylabel("Rata-rata PM2.5")

plt.xticks(rotation=45)

st.pyplot(fig)

st.markdown("---")

st.subheader("Distribusi Kategori Kualitas Udara")

fig2, ax2 = plt.subplots(figsize=(8, 5))

sns.countplot(
    x="AQI_Category",
    data=filtered_df,
    palette="viridis",
    ax=ax2
)

ax2.set_title("Frekuensi Kategori Kualitas Udara")

ax2.set_xlabel("Kategori")
ax2.set_ylabel("Jumlah Data")

st.pyplot(fig2)

st.caption("Proyek Analisis Data - Rizqy")