import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    initial_sidebar_state="expanded",
    page_title="Sleep Quality",
    page_icon="💤",
    layout="wide"
)


st.sidebar.title("Zzz Factor 😴")
st.sidebar.divider()
st.sidebar.write("This app is prepared for insomniacs 😵‍💫")
st.sidebar.divider()
app_mode = st.sidebar.selectbox('Select Page', ["Sleep Well?", "Diagnosis", "About Project", "Presentation", "Team"])
if app_mode == 'Sleep Well?':
    st.title("Sleep Well?")
    st.image('./bebek.jpg')
    #st.write('This app is prepared for insomniacs 😵‍💫')
    st.divider()
    st.subheader('This project was prepared as a final project for Miuul&VBO Data Scientist Bootcamp, DSB13 semester.')


############## PREDICTION PAGE ##############

# TODO add an explanation and specify feature range and explain

elif app_mode == "Diagnosis":
    # st.balloons()

    container = st.container()
    col1, col2 = container.columns([1, 1])

    with col1:
        def main():
            style = """<div style='background-color:pink; padding:12px'>
                    <h1 style='color:black'>Sleep Disorder Analysis</h1>
            </div>"""
            st.markdown(style, unsafe_allow_html=True)
            st.header('How to make it?')
            st.write('You can make an approximate price estimate by updating the values you see below in accordance with the \
                    features of the house you are looking for - at the specified intervals. \
                    This will enable customers to make informed decisions when buying or selling properties.')

            st.divider()
            left, right = st.columns((2, 2))
            #BLOOD_PRESSURE_SYSTOLIC = left.number_input('Blood Pressure Systolic', step=5.00, format='%2f', value=120.00, min_value=80.00, max_value=160.00)
            #BLOOD_PRESSURE_DIASTOLIC = right.number_input('Blood Pressure Diastolic)', step=5.00, format='%2f', value=80.00, min_value=40.00, max_value=120.00)
            #BMI_CATEGORY_Overweight = left.checkbox('The BMI category of the person = Overweight', value=False)
            #AGE = left.number_input('Age', step=1.00, format='%2f', value=18.00, max_value=65.00)
            #SLEEP_DURATION = right.number_input('The number of hours the person sleeps per day.', step=0.10, format='%2f', value=0.00, min_value=0.00, max_value=24.00)

            # GENDER = 1
            # AGE = 41
            # SLEEP_DURATION = 7.7
            # PHYSICAL_ACTIVITY_LEVEL = 90
            # HEART_RATE = 70
            # DAILY_STEPS
            # BLOOD_PRESSURE_SYSTOLIC = 130
            # BLOOD_PRESSURE_DIASTOLIC = 85
            # BMI_CATEGORY_Obese = False
            # BMI_CATEGORY_Overweight = False
            GENDER_user = st.selectbox('Select Gender:', ['MALE', 'FEMALE'])
            GENDER = 1 if GENDER_user == 'MALE' else 0

            AGE = st.slider('Select your age:', min_value=18, max_value=80, step=1)

            SLEEP_DURATION = st.slider('Select your sleep duration (hours):', min_value=1.0, max_value=24.0, step=0.1)
            PHYSICAL_ACTIVITY_LEVEL = st.number_input('Physical Activity Level (minutes per day)', step=10, format='%d', value=10, min_value=0, max_value=600)
            HEART_RATE = st.number_input('Heart Rate (bpm)', step=5, format='%d', value=60, min_value=60, max_value=100)

            DAILY_STEPS = st.number_input('Daily Steps', step=500, format='%d', value=8000, min_value=0, max_value=20000)
            BLOOD_PRESSURE_SYSTOLIC = st.number_input('Blood Pressure Systolic', step=1, format='%d', value=120, min_value=50, max_value=200)
            BLOOD_PRESSURE_DIASTOLIC = st.number_input('Blood Pressure Diastolic', step=1, format='%d', value=80, min_value=40, max_value=100)

            QUALITY_OF_SLEEP_user = selected_value = st.slider('Select your quality of sleep level between 1 and 10:', min_value=1, max_value=10, step=1)
            # Diğer değişkenleri belirle

            QUALITY_OF_SLEEP_5 = False
            QUALITY_OF_SLEEP_6 = False
            QUALITY_OF_SLEEP_7 = False
            QUALITY_OF_SLEEP_8 = False
            QUALITY_OF_SLEEP_9 = False

            if QUALITY_OF_SLEEP_user <= 5:
                QUALITY_OF_SLEEP_5 = True
            elif QUALITY_OF_SLEEP_user == 6:
                QUALITY_OF_SLEEP_6 = True
            elif QUALITY_OF_SLEEP_user == 7:
                QUALITY_OF_SLEEP_7 = True
            elif QUALITY_OF_SLEEP_user == 8:
                QUALITY_OF_SLEEP_8 = True
            elif QUALITY_OF_SLEEP_user >= 9:
                QUALITY_OF_SLEEP_9 = True

            STRESS_LEVEL_user = st.slider('Select your stress level between 1 and 10:', min_value=1, max_value=10, step=1)
            # Diğer değişkenleri belirle

            STRESS_LEVEL_4 = False
            STRESS_LEVEL_5 = False
            STRESS_LEVEL_6 = False
            STRESS_LEVEL_7 = False
            STRESS_LEVEL_8 = False

            if STRESS_LEVEL_user <= 4:
                STRESS_LEVEL_4 = True
            elif STRESS_LEVEL_user >= 5:
                STRESS_LEVEL_5 = True
            elif STRESS_LEVEL_user == 6:
                STRESS_LEVEL_6 = True
            elif STRESS_LEVEL_user == 7:
                STRESS_LEVEL_7 = True
            elif STRESS_LEVEL_user >= 8:
                STRESS_LEVEL_8 = True

            KG = st.slider('Select your weight (kg)', min_value=45, max_value=200, step=1)
            HEIGH = st.slider('Select your height (cm)', min_value=150, max_value=200, step=1)
            # BMI = kg/metre^2
            BMI_CATEGORY_Obese = False
            BMI_CATEGORY_Overweight = False

            BMI_user_float = KG / ((HEIGH/100) * (HEIGH/100))
            BMI_user = int(BMI_user_float)
            if BMI_user >= 30:
                BMI_CATEGORY_Obese = True
            elif BMI_user < 29.9 and BMI_user >= 25:
                BMI_CATEGORY_Overweight = True
            else:
                BMI_CATEGORY_Obese = False
                BMI_CATEGORY_Overweight = False


            BP_CAT_Evre_2_HT = False
            BP_CAT_Normal = False

            # Kan basıncı kategorilerini belirle
            BP_CAT_Normal_user = (BLOOD_PRESSURE_SYSTOLIC < 120) and (BLOOD_PRESSURE_DIASTOLIC < 80)
            BP_CAT_Evre_1_HT_user = (130 <= BLOOD_PRESSURE_SYSTOLIC <= 139) or (80 <= BLOOD_PRESSURE_DIASTOLIC <= 89)
            BP_CAT_Evre_2_HT_user = (BLOOD_PRESSURE_SYSTOLIC >= 140) or (BLOOD_PRESSURE_DIASTOLIC >= 90)

            if BP_CAT_Normal_user:
                BP_CAT_Normal = True
            elif BP_CAT_Evre_1_HT_user:
                BP_CAT_Evre_2_HT = False
                BP_CAT_Normal = False
            else:
                BP_CAT_Evre_2_HT = True

            button = st.button('Predict')
            # if button is pressed
            if button:
                # make prediction
                result = predict(GENDER, AGE, SLEEP_DURATION, PHYSICAL_ACTIVITY_LEVEL, HEART_RATE, DAILY_STEPS, BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC, QUALITY_OF_SLEEP_5, QUALITY_OF_SLEEP_6, QUALITY_OF_SLEEP_7, QUALITY_OF_SLEEP_8, QUALITY_OF_SLEEP_9, STRESS_LEVEL_4, STRESS_LEVEL_5, STRESS_LEVEL_6, STRESS_LEVEL_7, STRESS_LEVEL_8, BMI_CATEGORY_Obese, BMI_CATEGORY_Overweight, BP_CAT_Evre_2_HT, BP_CAT_Normal)
                #st.success(f'result {result}')
                # if result == 0:
                #     st.success(f'You are healthy {result}')
                #     st.balloons()
                # elif result == 2:
                #     st.warning(f'Patient is probably has Insomnia {result}')
                # else:
                #     st.warning(f'Patient is probably has Sleep Apnea {result}')

           # BP_CAT_Evre_2_HT = left.number_input('BP Stage 2 HT', step=1.00, format='%2f', value=0.00, max_value=1.00)


        # load the train model
        # with open('./xgb_model.pkl', 'rb') as rf:
        model = pickle.load(open('D:\Egitimler\miuul_VB_yetistirme_bootcamp\Miuul_VB_Bootcamp\model_1.pkl', 'rb'))
        scaler = pickle.load(open('D:\Egitimler\miuul_VB_yetistirme_bootcamp\Miuul_VB_Bootcamp\model_1_scaler.pkl', 'rb'))

        def predict(GENDER, AGE, SLEEP_DURATION, PHYSICAL_ACTIVITY_LEVEL, HEART_RATE, DAILY_STEPS, BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC, QUALITY_OF_SLEEP_5, QUALITY_OF_SLEEP_6, QUALITY_OF_SLEEP_7, QUALITY_OF_SLEEP_8, QUALITY_OF_SLEEP_9, STRESS_LEVEL_4, STRESS_LEVEL_5, STRESS_LEVEL_6, STRESS_LEVEL_7, STRESS_LEVEL_8, BMI_CATEGORY_Obese, BMI_CATEGORY_Overweight, BP_CAT_Evre_2_HT, BP_CAT_Normal):
            #num_lists = [AGE, SLEEP_DURATION,PHYSICAL_ACTIVITY_LEVEL,HEART_RATE,DAILY_STEPS,BLOOD_PRESSURE_SYSTOLIC,BLOOD_PRESSURE_DIASTOLIC]
            num_list_str = ['AGE', 'SLEEP_DURATION', 'PHYSICAL_ACTIVITY_LEVEL', 'HEART_RATE', 'DAILY_STEPS', 'BLOOD_PRESSURE_SYSTOLIC', 'BLOOD_PRESSURE_DIASTOLIC']
            index_num_cols = [1,2,3,4,5,6,7]
            lists = [GENDER, AGE, SLEEP_DURATION, PHYSICAL_ACTIVITY_LEVEL, HEART_RATE, DAILY_STEPS, BLOOD_PRESSURE_SYSTOLIC, BLOOD_PRESSURE_DIASTOLIC, QUALITY_OF_SLEEP_5, QUALITY_OF_SLEEP_6, QUALITY_OF_SLEEP_7, QUALITY_OF_SLEEP_8, QUALITY_OF_SLEEP_9, STRESS_LEVEL_4, STRESS_LEVEL_5, STRESS_LEVEL_6, STRESS_LEVEL_7, STRESS_LEVEL_8, BMI_CATEGORY_Obese, BMI_CATEGORY_Overweight, BP_CAT_Evre_2_HT, BP_CAT_Normal]
            df = pd.DataFrame(lists).transpose()
            print(df.head())
            #print(df.columns())
            df[index_num_cols] = scaler.transform(df[index_num_cols])
            print(df.head())
            #     # scaling the data
            #    scaler.transform(df)
            # making predictions using the train model
            prediction = model.predict(df)
            result = int(prediction)
            #st.success(f'result {result}')
            if result is None:
                st.warning('Result is not available. Please check again.')
            elif result == 0:
                st.success('You are healthy.')
                st.balloons()
            elif result == 2:
                st.warning('Patient probably has Insomnia.')
            elif result == 1:
                st.warning('Patient probably has Sleep Apnea.')

            #return result


        if __name__ == '__main__':
            main()

    # Görsel
    with col2:
        image = st.image('./adam.jpg', caption="Let's Calculate")

# 'GENDER', 'AGE', 'SLEEP_DURATION', 'PHYSICAL_ACTIVITY_LEVEL', 'HEART_RATE', 'DAILY_STEPS', 'SLEEP_DISORDER', 'BLOOD_PRESSURE_SYSTOLIC', 'BLOOD_PRESSURE_DIASTOLIC', 'SLEEP_DISORDER_ENCODED', 'QUALITY_OF_SLEEP_5', 'QUALITY_OF_SLEEP_6', 'QUALITY_OF_SLEEP_7', 'QUALITY_OF_SLEEP_8', 'QUALITY_OF_SLEEP_9', 'STRESS_LEVEL_4', 'STRESS_LEVEL_5', 'STRESS_LEVEL_6', 'STRESS_LEVEL_7', 'STRESS_LEVEL_8', 'BMI_CATEGORY_Obese', 'BMI_CATEGORY_Overweight', 'BP_CAT_Evre_2_HT', 'BP_CAT_Normal'], dtype='object'

############## ABOUT  PROJECT ##############
elif app_mode == 'About Project':
    container = st.container()
    ap_col1, ap_col2 = container.columns([1, 1])

    with ap_col1:
        st.image('./uyku.jpg', caption="")

    with ap_col2:
        df = pd.read_csv("./archive/Sleep_health_and_lifestyle_dataset.csv")
        st.dataframe(df, height=450)  # Same as st.write(df)

    st.header('Dataset Overview')
    st.write('The Sleep Health and Lifestyle Dataset comprises 400 rows and 13 columns, covering a wide range of variables related to sleep and daily habits. \
    It includes details such as gender, age, occupation, sleep duration, quality of sleep, physical activity level, stress levels, BMI category, blood pressure, heart rate, daily steps, and the presence or absence of sleep disorders.')

    st.header('Key Features of the Dataset')
    st.write('Comprehensive Sleep Metrics: Explore sleep duration, quality, and factors influencing sleep patterns. \
             Lifestyle Factors: Analyze physical activity levels, stress levels, and BMI categories. \
             Cardiovascular Health: Examine blood pressure and heart rate measurements. \
             Sleep Disorder Analysis: Identify the occurrence of sleep disorders such as Insomnia and Sleep Apnea.')

    st.header('Dataset Features')
    st.markdown(
    """
    - **Person ID:** An identifier for each individual.
    - **Gender:** The gender of the person (Male/Female).
    - **Age:** The age of the person in years.
    - **Occupation:** The occupation or profession of the person.
    - **Sleep Duration (hours):** The number of hours the person sleeps per day.
    - **Quality of Sleep (scale: 1-10):** A subjective rating of the quality of sleep, ranging from 1 to 10.
    - **Physical Activity Level (minutes/day):** The number of minutes the person engages in physical activity daily.
    - **Stress Level (scale: 1-10):** A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
    - **BMI Category:** The BMI category of the person (e.g., Underweight, Normal, Overweight).
    - **Blood Pressure (systolic/diastolic):** The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
    - **Heart Rate (bpm):** The resting heart rate of the person in beats per minute.
    - **Daily Steps:** The number of steps the person takes per day.
    - **Sleep Disorder:** The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).
    """)

    st.subheader('Details about Sleep Disorder Feature')
    st.write('None: The individual does not exhibit any specific sleep disorder.\
    Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep. \
    Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.')


############## TEAM ##############

elif app_mode == 'Team':

    st.header("Educators 👨‍🔬")
    educators = {
        "Educator : Vahit Keskin": "https://www.linkedin.com/in/vahitkeskin",
        "Mentor Teacher : Yasemin Arslan": "https://www.linkedin.com/in/yaseminarslann"
    }

    for isim, profil_linki in educators.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")

    st.header(" ")
    st.divider()

    st.header("Team Members 👩‍💻‍👨‍💻")
    # Ekip üyelerinin isimleri ve LinkedIn profillerinin linkleri
    ekip_uyeleri = {
        "Elif Mavili": "https://www.linkedin.com/in/elifmavili",
        "Nimet Karagöz": "https://www.linkedin.com/in/nimet-karag%C3%B6z-34238390",
        "Birkan Çanakçıoğlu": "https://www.linkedin.com/in/birkancanakcioglu",
        "Halil İbrahim Erdoğan": "https://www.linkedin.com/in/hierdogan"

    }

    for isim, profil_linki in ekip_uyeleri.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [LinkedIn]({profil_linki})")

#####################################
    st.header(" ")
    st.divider()
    st.header("Education Platform 🏫")
    company = {

        "Miuul": "https://miuul.com",
        "Veri Bilimi Okulu": "https://www.veribilimiokulu.com"
    }

    for isim, profil_linki in company.items():
        # LinkedIn linki içeren butonu oluşturma
        st.subheader(f" {isim} | [Web Site]({profil_linki})")
