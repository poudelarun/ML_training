import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pickle", "rb") as f:
    model = pickle.load(f)

# Load the label encoder
with open("label_encoder.pickle", "rb") as f:
    label_encoder = pickle.load(f)

# Function to predict hepatitis based on user inputs
def predict_hepatitis(age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot):
    # Create a DataFrame from user inputs
    input_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ALB": [alb],
        "ALP": [alp],
        "ALT": [alt],
        "AST": [ast],
        "BIL": [bil],
        "CHE": [che],
        "CHOL": [chol],
        "CREA": [crea],
        "GGT": [ggt],
        "PROT": [prot]
    })

    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    prediction_label = label_encoder.inverse_transform(prediction)[0]
    return prediction_label

# Streamlit app starts here
def main():
    st.title("Hepatitis Detection")

    # Sidebar inputs
    age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
    sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
    alb = st.sidebar.number_input("ALB")
    alp = st.sidebar.number_input("ALP")
    alt = st.sidebar.number_input("ALT")
    ast = st.sidebar.number_input("AST")
    bil = st.sidebar.number_input("BIL")
    che = st.sidebar.number_input("CHE")
    chol = st.sidebar.number_input("CHOL")
    crea = st.sidebar.number_input("CREA")
    ggt = st.sidebar.number_input("GGT")
    prot = st.sidebar.number_input("PROT")

    # Predict button
    if st.sidebar.button("Predict"):
        # Convert categorical inputs to numerical
        sex = 1 if sex == "Male" else 2

        # Get prediction
        result = predict_hepatitis(age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot)
        st.write(f"Prediction: {result}")

if __name__ == "__main__":
    main()
