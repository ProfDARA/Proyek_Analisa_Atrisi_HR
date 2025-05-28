# app.py
import streamlit as st
import pandas as pd
import joblib

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

# Numeric Inputs
input_dict.update({
    'Age': st.number_input("Umur", 18, 60, 30),
    'DailyRate': st.number_input("Daily Rate", 100, 1500, 800),
    'DistanceFromHome': st.number_input("Jarak dari rumah (km)", 0, 50, 10),
    'Education': st.selectbox("Tingkat Pendidikan", [1, 2, 3, 4, 5]),
    'EnvironmentSatisfaction': st.selectbox("Kepuasan Lingkungan", [1, 2, 3, 4]),
    'HourlyRate': st.number_input("Hourly Rate", 30, 150, 60),
    'JobInvolvement': st.selectbox("Job Involvement", [1, 2, 3, 4]),
    'JobLevel': st.selectbox("Job Level", [1, 2, 3, 4, 5]),
    'JobSatisfaction': st.selectbox("Job Satisfaction", [1, 2, 3, 4]),
    'MonthlyIncome': st.number_input("Monthly Income", 1000, 20000, 5000),
    'MonthlyRate': st.number_input("Monthly Rate", 1000, 30000, 15000),
    'NumCompaniesWorked': st.number_input("Jumlah Perusahaan Pernah Bekerja", 0, 10, 1),
    'PercentSalaryHike': st.number_input("Kenaikan Gaji (%)", 0, 50, 15),
    'PerformanceRating': st.selectbox("Rating Performa", [1, 2, 3, 4]),
    'RelationshipSatisfaction': st.selectbox("Relationship Satisfaction", [1, 2, 3, 4]),
    'StockOptionLevel': st.selectbox("Stock Option Level", [0, 1, 2, 3]),
    'TotalWorkingYears': st.number_input("Total Tahun Bekerja", 0, 40, 10),
    'TrainingTimesLastYear': st.number_input("Jumlah Pelatihan Tahun Lalu", 0, 10, 2),
    'WorkLifeBalance': st.selectbox("Work-Life Balance", [1, 2, 3, 4]),
    'YearsAtCompany': st.number_input("Tahun di Perusahaan", 0, 40, 5),
    'YearsInCurrentRole': st.number_input("Tahun di Role Saat Ini", 0, 20, 3),
    'YearsSinceLastPromotion': st.number_input("Tahun sejak Promosi Terakhir", 0, 15, 1),
    'YearsWithCurrManager': st.number_input("Tahun dengan Manajer Saat Ini", 0, 15, 2)
})

# Categorical One-Hot Encoding
business_travel = st.selectbox("Business Travel", ["Sering Bepergian", "Jarang Bepergian", "Tidak Ada"])
input_dict.update({
    'BusinessTravel_Travel_Frequently': 1 if business_travel == "Sering Bepergian" else 0,
    'BusinessTravel_Travel_Rarely': 1 if business_travel == "Jarang Bepergian" else 0,
    'BusinessTravel_Travel_No': 1 if business_travel == "Tidak Ada" else 0
})

department = st.radio("Department", ["R&D", "Sales", "Lainnya"])
input_dict.update({
    'Department_Research & Development': 1 if department == "R&D" else 0,
    'Department_Sales': 1 if department == "Sales" else 0,
    'Department_Other': 1 if department == "Lainnya" else 0
})

gender = st.radio("Gender", ["Laki-laki", "Perempuan"])
input_dict.update({
    'Gender_Male': 1 if gender == "Laki-laki" else 0,
    'Gender_Female': 1 if gender == "Perempuan" else 0
})

st.write(input_dict)

if st.button("Prediksi"):
    input_df = pd.DataFrame([input_dict])
    prediksi, peluang = cek_peluang_attrisi(input_df)

    st.subheader("Hasil Prediksi")
    hasil = "Keluar" if prediksi == 1 else "Bertahan"
    st.write(f"Prediksi: **{hasil}**")
    st.write(f"Confidence attrition: **{peluang * 100:.2f}%**")