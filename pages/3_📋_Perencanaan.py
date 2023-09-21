#####################################################################################
# Source code: Dashboard Bukan Amel                                                 #
#-----------------------------------------------------------------------------------#
# Dashboard ini dibuat oleh:                                                        #
# Nama          : Kurnia Ramadhan, ST.,M.Eng                                        #
# Jabatan       : Sub Koordinator Pengelolaan Informasi LPSE                        #
# Instansi      : Biro Pengadaan Barang dan Jasa Setda Prov. Kalbar                 #
# Email         : kramadhan@gmail.com                                               #
# URL Web       : https://github.com/blogramadhan                                   #
#-----------------------------------------------------------------------------------#
# Hak cipta milik Allah SWT, source code ini silahkan dicopy, di download atau      #
# di distribusikan ke siapa saja untuk bahan belajar, atau untuk dikembangkan lagi  #
# lebih lanjut, btw tidak untuk dijual ya.                                          #
#                                                                                   #
# Jika teman-teman mengembangkan lebih lanjut source code ini, agar berkenan untuk  #
# men-share code yang teman-teman kembangkan lebih lanjut sebagai bahan belajar     #
# untuk kita semua.                                                                 #
#-----------------------------------------------------------------------------------#
# @ Pontianak, 2023                                                                 #
#####################################################################################

# Import Library
import duckdb
import streamlit as st
import pandas as pd
import plotly.express as px
# Import library currency
from babel.numbers import format_currency
# Import library Aggrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
# Import library Google Cloud Storage
from google.oauth2 import service_account
from google.cloud import storage
# Import fungsi pribadi
#from fungsi import *

# Konfigurasi variabel lokasi UKPBJ
daerah =    ["PROV. KALBAR"]

tahuns = [2023, 2022]

pilih = st.sidebar.selectbox("Pilih UKPBJ yang diinginkan :", daerah)
tahun = st.sidebar.selectbox("Pilih Tahun :", tahuns)

if pilih == "PROV. KALBAR":
    kodeFolder = "prov"

# Persiapan Dataset
con = duckdb.connect(database=':memory:')

## Akses file dataset format parquet dari Google Cloud Storage via URL public
DatasetRUPPP = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/sirup/RUPPaketPenyediaTerumumkan{tahun}.parquet"
DatasetRUPPS = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/sirup/RUPPaketSwakelolaTerumumkan{tahun}.parquet"
DatasetRUPSA = f"https://storage.googleapis.com/bukanamel/{kodeFolder}/sirup/RUPStrukturAnggaranPD{tahun}.parquet"

## Buat dataframe RUP
try:
    ### Baca file parquet dataset
    df_RUPPP = pd.read_parquet(DatasetRUPPP)

    ### Query RUP Paket Penyedia
    df_RUPPP_umumkan = con.execute("").df()

except Exception:
    st.error("Gagal baca dataset RUP Paket Penyedia.")