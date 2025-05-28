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

# Business Travel
business_travel = st.selectbox("Business Travel", ["Sering Bepergian", "Jarang Bepergian", "Tidak Ada"])

input_dict = {
    'BusinessTravel_Travel_Frequently': 1 if business_travel == "Sering Bepergian" else 0,
    'BusinessTravel_Travel_Rarely': 1 if business_travel == "Jarang Bepergian" else 0
}

# Department
department = st.radio("Department", ["R&D", "Sales", "Lainnya"])

input_dict.update({
    'Department_Research & Development': 1 if department == "R&D" else 0,
    'Department_Sales': 1 if department == "Sales" else 0
})

# Gender
gender = st.radio("Gender", ["Laki-laki", "Perempuan"])

input_dict.update({
    'Gender_Male': 1 if gender == "Laki-laki" else 0
})

st.write(input_dict)

if st.button("Prediksi"):
    input_df = pd.DataFrame([input_dict])
    prediksi, peluang = cek_peluang_attrisi(input_df)

    st.subheader("Hasil Prediksi")
    hasil = "Keluar" if prediksi == 1 else "Bertahan"
    st.write(f"Prediksi: **{hasil}**")
    st.write(f"Confidence attrition: **{peluang * 100:.2f}%**")