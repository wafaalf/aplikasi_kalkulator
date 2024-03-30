import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('the first number is',angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('the second number is',angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")