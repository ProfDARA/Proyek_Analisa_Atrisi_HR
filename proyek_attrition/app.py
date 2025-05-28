# app.py
import streamlit as st
import pandas as pd
import joblib

# Fungsi prediksi peluang attrition
def cek_peluang_attrisi(input_data):
    model = joblib.load("modelprediksi.pkl")
    proba = model.predict_proba(input_data)[:, 1]
    pred = model.predict(input_data)
    return pred[0], proba[0]

st.title("Prediksi Peluang Attrition Karyawan")
st.write("Masukkan data karyawan untuk memprediksi apakah mereka berisiko keluar dari perusahaan.")

# --- INPUT USER ---
input_dict = {}

input_dict['Age'] = st.number_input("Umur", 18, 60, 30)
input_dict['DailyRate'] = st.number_input("Daily Rate", 100, 1500, 800)
input_dict['DistanceFromHome'] = st.number_input("Jarak dari rumah (km)", 0, 50, 10)
input_dict['Education'] = st.selectbox("Tingkat Pendidikan", [1, 2, 3, 4, 5])
input_dict['EnvironmentSatisfaction'] = st.selectbox("Kepuasan Lingkungan", [1, 2, 3, 4])
input_dict['HourlyRate'] = st.number_input("Hourly Rate", 30, 150, 60)
input_dict['JobInvolvement'] = st.selectbox("Job Involvement", [1, 2, 3, 4])
input_dict['JobLevel'] = st.selectbox("Job Level", [1, 2, 3, 4, 5])
input_dict['JobSatisfaction'] = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
input_dict['MonthlyIncome'] = st.number_input("Monthly Income", 1000, 20000, 5000)
input_dict['MonthlyRate'] = st.number_input("Monthly Rate", 1000, 30000, 15000)
input_dict['NumCompaniesWorked'] = st.number_input("Jumlah Perusahaan Pernah Bekerja", 0, 10, 1)
input_dict['PercentSalaryHike'] = st.number_input("Kenaikan Gaji (%)", 0, 50, 15)
input_dict['PerformanceRating'] = st.selectbox("Rating Performa", [1, 2, 3, 4])
input_dict['RelationshipSatisfaction'] = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
input_dict['StockOptionLevel'] = st.selectbox("Stock Option Level", [0, 1, 2, 3])
input_dict['TotalWorkingYears'] = st.number_input("Total Tahun Bekerja", 0, 40, 10)
input_dict['TrainingTimesLastYear'] = st.number_input("Jumlah Pelatihan Tahun Lalu", 0, 10, 2)
input_dict['WorkLifeBalance'] = st.selectbox("Work-Life Balance", [1, 2, 3, 4])
input_dict['YearsAtCompany'] = st.number_input("Tahun di Perusahaan", 0, 40, 5)
input_dict['YearsInCurrentRole'] = st.number_input("Tahun di Role Saat Ini", 0, 20, 3)
input_dict['YearsSinceLastPromotion'] = st.number_input("Tahun sejak Promosi Terakhir", 0, 15, 1)
input_dict['YearsWithCurrManager'] = st.number_input("Tahun dengan Manajer Saat Ini", 0, 15, 2)

# One-hot encoding pilihan kategori
input_dict['BusinessTravel_Travel_Frequently'] = st.checkbox("Sering Bepergian (Business Travel)")
input_dict['BusinessTravel_Travel_Rarely'] = st.checkbox("Jarang Bepergian (Business Travel)")
input_dict['Department_Research & Development'] = st.checkbox("Department: R&D")
input_dict['Department_Sales'] = st.checkbox("Department: Sales")
input_dict['EducationField_Life Sciences'] = st.checkbox("Education Field: Life Sciences")
input_dict['EducationField_Marketing'] = st.checkbox("Education Field: Marketing")
input_dict['EducationField_Medical'] = st.checkbox("Education Field: Medical")
input_dict['EducationField_Other'] = st.checkbox("Education Field: Other")
input_dict['EducationField_Technical Degree'] = st.checkbox("Education Field: Technical Degree")
input_dict['Gender_Male'] = st.checkbox("Laki-laki")
input_dict['JobRole_Human Resources'] = st.checkbox("Job Role: HR")
input_dict['JobRole_Laboratory Technician'] = st.checkbox("Job Role: Lab Technician")
input_dict['JobRole_Manager'] = st.checkbox("Job Role: Manager")
input_dict['JobRole_Manufacturing Director'] = st.checkbox("Job Role: Manufacturing Director")
input_dict['JobRole_Research Director'] = st.checkbox("Job Role: Research Director")
input_dict['JobRole_Research Scientist'] = st.checkbox("Job Role: Research Scientist")
input_dict['JobRole_Sales Executive'] = st.checkbox("Job Role: Sales Executive")
input_dict['JobRole_Sales Representative'] = st.checkbox("Job Role: Sales Representative")
input_dict['MaritalStatus_Married'] = st.checkbox("Sudah Menikah")
input_dict['MaritalStatus_Single'] = st.checkbox("Belum Menikah")
input_dict['OverTime_Yes'] = st.checkbox("Lembur")

if st.button("Prediksi"):
    input_df = pd.DataFrame([input_dict])
    prediksi, peluang = cek_peluang_attrisi(input_df)

    st.subheader("Hasil Prediksi")
    hasil = "Keluar" if prediksi == 1 else "Bertahan"
    st.write(f"Prediksi: **{hasil}**")
    st.write(f"Confidence attrition: **{peluang * 100:.2f}%**")