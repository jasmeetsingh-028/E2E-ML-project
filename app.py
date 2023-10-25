import joblib
import numpy as np
import pandas as pd
import streamlit as st
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction



def main():
    st.title("Enter Values to predict wine quality")

    st.sidebar.header("Wine Quality Prediction App")
    st.sidebar.markdown("This is a Streamlit app that predicts the quality of wine based on various features.")
    fixed_acidity = st.number_input("Fixed Acidity")
    volatile_acidity = st.number_input("Volatile Acidity")
    citric_acid = st.number_input("Citric Acid")
    residual_sugar = st.number_input("Residual Sugar")
    chlorides = st.number_input("Chlorides")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide")
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide")
    density = st.number_input("Density")
    pH = st.number_input("pH")
    sulphates = st.number_input("Sulphates")
    alcohol = st.number_input("Alcohol")

    if st.button("Predict"):
        data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
        data = [float(feats) for feats in data]
        data = np.array(data).reshape(1, 11)
        
        obj = PredictionPipeline()
        prediction = obj.predict(data)
        
        st.subheader("Prediction")
        st.write(f"The predicted Wine quality is: {prediction}")
    
    st.sidebar.markdown("Project GitHub Repository: [GitHub Repository](https://github.com/jasmeetsingh-028/E2E-ML-project)")
    
if __name__ == "__main__":
    main()
