import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import joblib

with open('best_model.pkl', 'rb') as file_1:
  rfc = pickle.load(file_1)
def run():  
    # membuat title
    st.title('STROKE PREDICTION')
    st.subheader('Prediksi apakah patien mengalami stroke atau tidak')
    st.markdown('---')
    st.write("# Data Pasien")
    # Buat form
    with st.form(key='from_heart_failure'):
        Gender = st.radio('Jenis kelamin Pasien', ('Male', 'Female'), index=0)
        if Gender == 'Male':
            gender = 0
        else:
            gender = 1
        Age = st.number_input('Age', min_value=0, max_value=120, value=50, step=1, help="Umur Pasien")
        Hypertension = st.radio('Apakah pasien mengalami hipertensi?', ('No', 'Yes'), index=0)
        if Hypertension == 'No':
            hypertension = 0
        else:
            hypertension = 1
        Heart_disease = st.radio('Apakah pasien memiliki penyakit jantung?', ('No', 'Yes'), index=0)
        if Heart_disease == 'No':
            heart_disease = 0
        else:
            heart_disease = 1
        Ever_married = st.radio('Apakah pasien pernah menikah?', ('No', 'Yes'), index=0)
        if Ever_married == 'No':
            ever_married = 0
        else:
            ever_married = 1
        Work_type = st.radio('Apa pekerjaan pasien?', ('Bekerja di Pemerintahan', 'Tidak Pernah Kerja','Privasi','Wirausaha','anak-anak'), index=0)
        if Work_type == 'Bekerja di Pemerintahan':
            work_type = 0
        elif Work_type == 'Tidak Pernah Kerja':
            work_type = 1
        elif Work_type == 'Privasi':
            work_type = 2
        elif Work_type == 'Wirausaha':
            work_type = 3
        else:
            work_type = 4 
        Residence_type = st.radio('Daerah tinggal pasien', ('Perdesaan', 'Perkotaan'), index=0)
        if Residence_type == 'Perdesaan':
            residence_type = 0
        else:
            Residence_type = 1   
        Glukosa = st.number_input('Rata-rata glukosa', min_value=0, max_value=300, value=55, step=1, 
                                    help='Kadar glukosa pada pasian')
        BMI = st.number_input('Berat badan pasien',min_value=0,max_value=100,value=10,step=1)
        Smoking_status = st.radio('Apakah pasien merokok?', ('Tidak', 'Ya','Sebelumnya Merokok','Tidak Tau'), index=0)
        if Smoking_status == 'Tidak tau':
            smoking_status = 0
        elif Smoking_status == 'Sebelumnya Merokok':
            smoking_status = 1 
        elif Smoking_status == 'Tidak':
            smoking_status = 2
        else:
            smoking_status = 3
        
        

        submitted = st.form_submit_button('Predict')

        # dataframe
        st.write("# Patient's summary")
        data_inf = {
                    'gender': gender,
                    'age': Age,
                    'hypertension': hypertension,
                    'heart_disease': heart_disease,
                    'ever_married': ever_married,
                    'work_type': work_type,
                    'Residence_type': residence_type,
                    'avg_glucose_level': Glukosa,
                    'bmi': BMI,
                    'smoking_status': smoking_status,
                    
                    
                }

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf.T, width=800, height=495)
        data_inf
    if submitted:
            # Predict using Linear Regression
            y_pred_inf = rfc.predict(data_inf)
            if y_pred_inf == 0:
                pred = 'Tidak terkena stroke'
            else:
                pred = 'Terkena Stroke'
            st.markdown('---')
            st.write('# Prediksi : ', (pred))        
            
if __name__ == '__main__':
    run()