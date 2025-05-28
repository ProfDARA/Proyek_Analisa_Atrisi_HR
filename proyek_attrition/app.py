import streamlit as st
import pandas as pd
import joblib
from streamlit_extras.let_it_rain import rain
from streamlit_extras.mention import mention
# Custom Page Config
st.set_page_config(
    page_title="Prediksi Attrition Karyawan",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Background Styling
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background: url("https://images.unsplash.com/photo-1519389950473-47ba0277781c") no-repeat center center fixed;
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


# Model Prediction Function
def cek_peluang_attrisi(input_data):
    model = joblib.load("modelprediksi.pkl")
    proba = model.predict_proba(input_data)[:, 1]
    pred = model.predict(input_data)
    return pred[0], proba[0]

# One-Hot Encoding Helper
def one_hot_encode_input(input_dict):
    encoded = {}
    for key in input_dict:
        if key not in [
            'BusinessTravel', 'Department', 'EducationField', 'Gender',
            'JobRole', 'MaritalStatus', 'OverTime']:
            encoded[key] = input_dict[key]

    for cat in ["Travel_Frequently", "Travel_Rarely"]:
        encoded[f"BusinessTravel_{cat}"] = (input_dict['BusinessTravel'] == cat)

    for cat in ["Research & Development", "Sales"]:
        encoded[f"Department_{cat}"] = (input_dict['Department'] == cat)

    for cat in ["Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"]:
        encoded[f"EducationField_{cat}"] = (input_dict['EducationField'] == cat)

    encoded['Gender_Male'] = (input_dict['Gender'] == 'Male')

    for cat in ["Human Resources", "Laboratory Technician", "Manager",
                "Manufacturing Director", "Research Director", "Research Scientist",
                "Sales Executive", "Sales Representative"]:
        encoded[f"JobRole_{cat}"] = (input_dict['JobRole'] == cat)

    for cat in ["Married", "Single"]:
        encoded[f"MaritalStatus_{cat}"] = (input_dict['MaritalStatus'] == cat)

    encoded['OverTime_Yes'] = (input_dict['OverTime'] == 'Yes')

    return encoded

# Streamlit UI
st.title("\ud83d\udcca Prediksi Peluang Attrition Karyawan")
st.markdown("""
<style>
    .big-font {
        font-size:24px !important;
        color: white;
        font-weight: bold;
    }
</style>
<span class="big-font">Masukkan data karyawan untuk melihat peluang mereka mengundurkan diri.</span>
""", unsafe_allow_html=True)

input_dict = {}

# Numeric and ordinal inputs
input_dict['Age'] = st.slider("Umur", 18, 60, 30)
input_dict['DailyRate'] = st.slider("Daily Rate", 100, 1500, 800)
input_dict['DistanceFromHome'] = st.slider("Jarak dari rumah (km)", 0, 50, 10)
input_dict['Education'] = st.selectbox("Tingkat Pendidikan", [1, 2, 3, 4, 5])
input_dict['EnvironmentSatisfaction'] = st.selectbox("Kepuasan Lingkungan", [1, 2, 3, 4])
input_dict['HourlyRate'] = st.slider("Hourly Rate", 30, 150, 60)
input_dict['JobInvolvement'] = st.selectbox("Job Involvement", [1, 2, 3, 4])
input_dict['JobLevel'] = st.selectbox("Job Level", [1, 2, 3, 4, 5])
input_dict['JobSatisfaction'] = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
input_dict['MonthlyIncome'] = st.slider("Monthly Income", 1000, 20000, 5000)
input_dict['MonthlyRate'] = st.slider("Monthly Rate", 1000, 30000, 15000)
input_dict['NumCompaniesWorked'] = st.slider("Jumlah Perusahaan Pernah Bekerja", 0, 10, 1)
input_dict['PercentSalaryHike'] = st.slider("Kenaikan Gaji (%)", 0, 50, 15)
input_dict['PerformanceRating'] = st.selectbox("Rating Performa", [1, 2, 3, 4])
input_dict['RelationshipSatisfaction'] = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
input_dict['StockOptionLevel'] = st.selectbox("Stock Option Level", [0, 1, 2, 3])
input_dict['TotalWorkingYears'] = st.slider("Total Tahun Bekerja", 0, 40, 10)
input_dict['TrainingTimesLastYear'] = st.slider("Jumlah Pelatihan Tahun Lalu", 0, 10, 2)
input_dict['WorkLifeBalance'] = st.selectbox("Work-Life Balance", [1, 2, 3, 4])
input_dict['YearsAtCompany'] = st.slider("Tahun di Perusahaan", 0, 40, 5)
input_dict['YearsInCurrentRole'] = st.slider("Tahun di Role Saat Ini", 0, 20, 3)
input_dict['YearsSinceLastPromotion'] = st.slider("Tahun sejak Promosi Terakhir", 0, 15, 1)
input_dict['YearsWithCurrManager'] = st.slider("Tahun dengan Manajer Saat Ini", 0, 15, 2)

# Categorical inputs
input_dict['BusinessTravel'] = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
input_dict['Department'] = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
input_dict['EducationField'] = st.selectbox("Education Field", ["Life Sciences", "Marketing", "Medical", "Other", "Technical Degree", "Human Resources"])
input_dict['Gender'] = st.selectbox("Jenis Kelamin", ["Male", "Female"])
input_dict['JobRole'] = st.selectbox("Job Role", ["Human Resources", "Laboratory Technician", "Manager", "Manufacturing Director", "Research Director", "Research Scientist", "Sales Executive", "Sales Representative"])
input_dict['MaritalStatus'] = st.selectbox("Status Pernikahan", ["Married", "Single", "Divorced"])
input_dict['OverTime'] = st.selectbox("Lembur", ["Yes", "No"])

if st.button("\u2728 Prediksi"):
    try:
        encoded_input = one_hot_encode_input(input_dict)
        input_df = pd.DataFrame([encoded_input])
        prediksi, peluang = cek_peluang_attrisi(input_df)

        hasil = "Keluar" if prediksi == 1 else "Bertahan"
        rain(emoji="\ud83c\udf1f" if prediksi == 1 else "\ud83c\udf3f", font_size=36, falling_speed=5, animation_length="medium")

        st.success(f"Prediksi: {hasil}")
        st.info(f"Peluang Mengundurkan Diri: {peluang * 100:.2f}%")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")