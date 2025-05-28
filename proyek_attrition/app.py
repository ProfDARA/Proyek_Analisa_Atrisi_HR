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

# --- Refactored INPUT USER ---
input_dict = {}

# Numeric inputs (continuous)
input_dict['Age'] = st.number_input("Umur", 18, 60, 30)
input_dict['DailyRate'] = st.number_input("Daily Rate", 100, 1500, 800)
input_dict['DistanceFromHome'] = st.number_input("Jarak dari rumah (km)", 0, 50, 10)
input_dict['HourlyRate'] = st.number_input("Hourly Rate", 30, 150, 60)
input_dict['MonthlyIncome'] = st.number_input("Monthly Income", 1000, 20000, 5000)
input_dict['MonthlyRate'] = st.number_input("Monthly Rate", 1000, 30000, 15000)
input_dict['NumCompaniesWorked'] = st.number_input("Jumlah Perusahaan Pernah Bekerja", 0, 10, 1)
input_dict['PercentSalaryHike'] = st.number_input("Kenaikan Gaji (%)", 0, 50, 15)
input_dict['TotalWorkingYears'] = st.number_input("Total Tahun Bekerja", 0, 40, 10)
input_dict['TrainingTimesLastYear'] = st.number_input("Jumlah Pelatihan Tahun Lalu", 0, 10, 2)
input_dict['YearsAtCompany'] = st.number_input("Tahun di Perusahaan", 0, 40, 5)
input_dict['YearsInCurrentRole'] = st.number_input("Tahun di Role Saat Ini", 0, 20, 3)
input_dict['YearsSinceLastPromotion'] = st.number_input("Tahun sejak Promosi Terakhir", 0, 15, 1)
input_dict['YearsWithCurrManager'] = st.number_input("Tahun dengan Manajer Saat Ini", 0, 15, 2)

# Ordinal categorical inputs (sliders)
input_dict['Education'] = st.slider("Tingkat Pendidikan", 1, 5, 3)
input_dict['EnvironmentSatisfaction'] = st.slider("Kepuasan Lingkungan", 1, 4, 3)
input_dict['JobInvolvement'] = st.slider("Job Involvement", 1, 4, 3)
input_dict['JobLevel'] = st.slider("Job Level", 1, 5, 2)
input_dict['JobSatisfaction'] = st.slider("Job Satisfaction", 1, 4, 3)
input_dict['PerformanceRating'] = st.slider("Rating Performa", 1, 4, 3)
input_dict['RelationshipSatisfaction'] = st.slider("Relationship Satisfaction", 1, 4, 3)
input_dict['StockOptionLevel'] = st.slider("Stock Option Level", 0, 3, 1)
input_dict['WorkLifeBalance'] = st.slider("Work-Life Balance", 1, 4, 3)

# Nominal categorical inputs (selectbox)
input_dict['BusinessTravel'] = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
input_dict['Department'] = st.selectbox("Department", ["Research & Development", "Sales", "Human Resources"])
input_dict['EducationField'] = st.selectbox("Education Field", [
    "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree", "Human Resources"])
input_dict['Gender'] = st.selectbox("Jenis Kelamin", ["Male", "Female"])
input_dict['JobRole'] = st.selectbox("Job Role", [
    "Human Resources", "Laboratory Technician", "Manager", "Manufacturing Director",
    "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"])
input_dict['MaritalStatus'] = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
input_dict['OverTime'] = st.selectbox("Lembur", ["Yes", "No"])

# Prediction trigger
if st.button("Prediksi"):
    input_df = pd.DataFrame([input_dict])
    prediksi, peluang = cek_peluang_attrisi(input_df)

    st.subheader("Hasil Prediksi")
    hasil = "Keluar" if prediksi == 1 else "Bertahan"
    st.write(f"Prediksi: **{hasil}**")
    st.write(f"Confidence attrition: **{peluang * 100:.2f}%**")