import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title = 'STROKE DATA SET',
    layout = 'wide',
    initial_sidebar_state= 'expanded'
)
def run():
    #Membuat title
    st.title('Stroke Prediction ')

    #membuat sub header
    st.subheader('EDA untuk analisis Stroke')

    #membuat gambar
    image = Image.open('stroke.jpeg')
    st.image(image ,caption = 'Stroke')

    #menambahkan deskripsi
    st.write('Page ini dibuat oleh **Novanska Aginta Ganesha**')
    #data yang diambil data yang sudah di encode dan scaling
    st.write('### Data ini diambil melalui kaggle.')
    data = pd.read_csv('data_final')
    st.dataframe(data)

    st.write('### Tingkat stroke berdasarkan gender')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x="gender", hue="stroke", data=data, palette="Blues")
    st.pyplot(fig)

    st.write('### Histogram tingkat terkena stroke berdasarkan umur')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x = 'age',hue='stroke',data=data)
    st.pyplot(fig)


    st.write('### Histrogram Umur')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(x='age',data=data)
    st.pyplot(fig)



    st.write('### Histogram tingkat terkena stroke berdasarkan penyakit jantung')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(x='heart_disease',hue='stroke',data=data,)
    st.pyplot(fig)
    st.write('### 0 (tidak punya penyakit jantung) 1 (punya penyakit jantung)')

    st.write('### Histrogram penyebab terkana stroke')
    pilihan = st.selectbox('Penyebab terkena stroke : ',('avg_glucose_level','bmi','smoking_status','work_type'))
    fig= plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan],bins=10,kde=True)
    st.pyplot(fig)
    
if __name__ == '__main__':
    run()