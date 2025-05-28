import streamlit as st
import pandas as pd
import joblib

# Model Prediction Function
def cek_peluang_attrisi(input_data):
    model = joblib.load("modelprediksi.pkl")
    proba = model.predict_proba(input_data)[:, 1]
    pred = model.predict(input_data)
    return pred[0], proba[0]

# One-Hot Encoding Helper 
def one_hot_encode_input(input_dict):
    encoded = {}

    # Salin numerik dan ordinal
    for key in input_dict:
        if key not in [
            'BusinessTravel', 'Department', 'EducationField', 'Gender',
            'JobRole', 'MaritalStatus', 'OverTime']:
            encoded[key] = input_dict[key]

    # One-hot BusinessTravel
    bt = input_dict['BusinessTravel']
    for cat in ["Travel_Frequently", "Travel_Rarely"]:
        encoded[f"BusinessTravel_{cat}"] = (bt == cat)

    # One-hot Department
    dept = input_dict['Department']
    for cat in ["Research & Development", "Sales"]:
        encoded[f"Department_{cat}"] = (dept == cat)

    # One-hot EducationField
    field = input_dict['EducationField']
    for cat in ["Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"]:
        encoded[f"EducationField_{cat}"] = (field == cat)

    # One-hot Gender
    encoded['Gender_Male'] = (input_dict['Gender'] == 'Male')

    # One-hot JobRole
    role = input_dict['JobRole']
    for cat in ["Human Resources", "Laboratory Technician", "Manager",
                "Manufacturing Director", "Research Director", "Research Scientist",
                "Sales Executive", "Sales Representative"]:
        encoded[f"JobRole_{cat}"] = (role == cat)

    # One-hot MaritalStatus
    ms = input_dict['MaritalStatus']
    for cat in ["Married", "Single"]:
        encoded[f"MaritalStatus_{cat}"] = (ms == cat)

    # One-hot OverTime
    encoded['OverTime_Yes'] = (input_dict['OverTime'] == 'Yes')

    return encoded

# Streamlit UI
st.title("Prediksi Peluang Attrition Karyawan")
st.write("Masukkan data karyawan untuk memprediksi apakah mereka berisiko keluar dari perusahaan.")

input_dict = {}

# Numeric and ordinal inputs
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

# Categorical inputs (selectbox)
input_dict['BusinessTravel'] = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
input_dict['Department'] = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
input_dict['EducationField'] = st.selectbox("Education Field", ["Life Sciences", "Marketing", "Medical", "Other", "Technical Degree", "Human Resources"])
input_dict['Gender'] = st.selectbox("Jenis Kelamin", ["Male", "Female"])
input_dict['JobRole'] = st.selectbox("Job Role", ["Human Resources", "Laboratory Technician", "Manager", "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"])
input_dict['MaritalStatus'] = st.selectbox("Status Pernikahan", ["Married", "Single", "Divorced"])
input_dict['OverTime'] = st.selectbox("Lembur", ["Yes", "No"])

# Bagian untuk memprediksi
if st.button("Prediksi"):
    try:
        encoded_input = one_hot_encode_input(input_dict)
        input_df = pd.DataFrame([encoded_input])
        prediksi, peluang = cek_peluang_attrisi(input_df)

        st.subheader("Hasil Prediksi")
        hasil = "Keluar" if prediksi == 1 else "Bertahan"
        st.write(f"Prediksi: **{hasil}**")
        st.write(f"Peluang Mengundurkan Diri: **{peluang * 100:.2f}%**")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")