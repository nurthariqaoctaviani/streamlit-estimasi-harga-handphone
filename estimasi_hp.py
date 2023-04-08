import pickle
import streamlit as st

model = pickle.load(open('estimasi_hanphone.sav', 'rb'))

st.title('Estimasi')
st.subheader('Kisaran Harga Handphone')


battery_power = st.number_input('Total kapasitas baterai (MaH)')
fc = st.number_input('Kamera depan (Mp)')
int_memory = st.number_input('Memori internal (GB)')
n_cores = st.number_input('jumlah core prosesor')
ram = st.number_input('RAM')

predict = ''

if st.button('Kisaran Harga'):
    predict = model.predict([[battery_power,fc,int_memory,n_cores,ram]])
    st.write('Estimasi Kisaran Harga Handphone Adalah :', predict)



