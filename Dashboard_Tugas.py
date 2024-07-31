import streamlit as st
from streamlit_gsheets import GSheetsConnection

import pandas as pd
from ydata_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

st.set_page_config(
    page_title = "Data Pendapatan Dashboard",
    page_icon = "📝",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

# ----- Judul Dashboard
#st.title("Data Profiler")
st.markdown("<h1 style='text-align: center;'>Dashboard data Pendapatan</h1>",
            unsafe_allow_html=True)
st.markdown("---")

# ----- Sidebar
with st.sidebar:
    st.subheader("Data Pendapatan")
    st.markdown("----")

st.write("Silahkan isi profile anda terlebih dahulu :")
Namanya = st.text_input("Nama :")
Alamatnya = st.text_input("Alamat :")
Tanggalnya = st.date_input("Tanggal Lahir :")
Hobbynya = st.text_area("Ceritakan mengenai diri anda :")

tombol = st.button("Submit")
if tombol == True :
    st.write(f"Nama anda {Namanya}, anda bertempat tinggal di {Alamatnya}, dan lahir pada tanggal {Tanggalnya}. Anda kurang lebih seperti {Hobbynya}")
    st.write("Terima kasih untuk team Algoritma yang telah mengajari saya mengenai streamlit. Mohon maaf jika streamlit ini sederhana sekali, karena waktu untuk mengerjakannya terbatas")
    st.write("Namun minimal saya sudah mengerti konsepnya sehingga saya ada gambaran cara penerapan di tempat kerja.")
# ------ Buat Button
if st.sidebar.button("Start Profiling Data Pendapatan"):
    st.write("Report")
    ## read data
    conn = st.connection("gsheet", type = GSheetsConnection)

    df = conn.read(
        spreadsheet = st.secrets.gsheet_promotion["spreadsheet"],
        worksheet = st.secrets.gsheet_promotion["worksheet"]
    )
    
    ## Generated Report
    pr = ProfileReport(df)

    st_profile_report(pr)
else:
    st.info("Click bar sebelah kiri untuk melihat profiling data")


