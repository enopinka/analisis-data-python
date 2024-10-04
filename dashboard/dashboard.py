import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from babel.numbers import format_currency


def create_rentals_per_month(df):
  rentals_per_month = df.groupby("mnth_x")["cnt_y"].count().reset_index()
  return rentals_per_month

def create_rentals_per_season(df):
  rentals_per_season = df.groupby("season_x").count()
  return rentals_per_season

def create_rentals_per_year(df):
  return df.groupby("yr_x").count()

all_df = pd.read_csv("all_df.csv")


with st.sidebar:
  all_df["dteday"] = pd.to_datetime(all_df["dteday"])
  min_date = all_df["dteday"].min()
  max_date = all_df["dteday"].max()

  # Logo perusahaan
  st.image("https://png.pngtree.com/template/20200713/ourmid/pngtree-modern-bicycle-logo-template-image_390986.jpg")

  #rentang waktu
  start_date, end_date = st.date_input(
    label="Rentang Waktu",
    min_value=min_date, 
    max_value=max_date,
    value=[min_date, max_date],
    help="Pilih rentang waktu dari data yang ingin Anda tinjau"
  )

filtered_df = all_df[(all_df["dteday"] >= pd.Timestamp(start_date)) & (all_df["dteday"] <= pd.Timestamp(end_date))]


st.header("Peminjaman Sepeda Dicoding :sparkles:")

# Peminjaman Sepeda Per Bulan
st.subheader("Peminjaman Sepeda per Bulan")
rent_per_month = create_rentals_per_month(filtered_df)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="mnth_x",
    y="cnt_y",
    data=rent_per_month,
    ax=ax
)

plt.title("Peminjaman Sepeda Per Bulan", loc="center", fontsize=15)
plt.xlabel("Bulan")
plt.xticks(ticks=range(0, 12), 
           labels=["Januari", "Februari", "Maret","April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"],
           rotation=45)

for p in ax.patches:
   ax.annotate(f'{p.get_height():,}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=12)
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Peminjaman Sepeda Per Musim
st.subheader("Peminjaman Sepeda per Musim")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="season_x",
    y="cnt_y",
    data=create_rentals_per_season(filtered_df),
    ax=ax
)

plt.title("Peminjaman Sepeda Per Musim", loc="center", fontsize=15)
plt.xlabel("Bulan")
for p in ax.patches:
   ax.annotate(f'{p.get_height():,}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=12)

plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Peminjaman sepeda per tahun
st.subheader("Peminjaman Sepeda Per Tahun")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x="yr_x",
    y="cnt_y",
    data=create_rentals_per_year(filtered_df),
    ax=ax
)

plt.title("Peminjaman Sepeda Per Musim", loc="center", fontsize=15)
plt.xlabel("Tahun")
plt.xticks(ticks=[0, 1], labels=['2011', '2012'])

for p in ax.patches:
   ax.annotate(f'{p.get_height():,}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=12)

plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig)