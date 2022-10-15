import streamlit as st
import pickle
import pandas as pd

st.title("Heart Disease Pridiction")

st.subheader("Enter details below")
def solve(new_data):
    loaded_model = pickle.load(open('model.sav', 'rb'))
    prediction = loaded_model.predict(new_data)
    if prediction[0] == 0:
        return 'No Heart Desease'
    else:
        return 'Heart Desease'

with st.form("form1", clear_on_submit=True):
    age = st.text_input("Enter age")
    sex = st.text_input("Enter sex")
    cp = st.text_input("Enter Cerebral palsy (CP)")
    trestbps = st.text_input("Patient's resting blood pressure(trestbps)")
    chol = st.text_input("cholestero(chol)")
    fbs = st.text_input("Fasting Blood Sugar(fbs)")
    restecg = st.text_input("resting electrocardiographic results(restecg)")
    thalanch = st.text_input("thalanch")
    exang = st.text_input("exang")
    oldpeak = st.text_input("oldpeak")
    slope = st.text_input("slope")
    ca = st.text_input("ca")
    thal = st.text_input("thal")

    new_data = pd.DataFrame({
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thal,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal,
    }, index=[0])

    submit=st.form_submit_button("Submit this form")
    if submit:
        st.write(solve(new_data))

