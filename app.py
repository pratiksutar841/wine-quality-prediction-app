import streamlit as st
import joblib
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Wine Quality Prediction", page_icon="🍷", layout="wide")
st.title("🍷 Wine Quality Prediction App")
st.markdown("Adjust the values below and click **Predict** to see wine quality score.")

# -----------------------------
# 1️⃣ INPUT SLIDERS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    fixed_acidity = st.slider("Fixed Acidity", 4.0, 15.0, 7.4)
    volatile_acidity = st.slider("Volatile Acidity", 0.1, 1.5, 0.7)
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, 0.3)
    residual_sugar = st.slider("Residual Sugar", 0.5, 15.0, 2.5)

with col2:
    chlorides = st.slider("Chlorides", 0.01, 0.2, 0.08)
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1.0, 72.0, 15.0)
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 6.0, 289.0, 46.0)
    density = st.slider("Density", 0.990, 1.005, 0.996)

with col3:
    pH = st.slider("pH", 2.5, 4.0, 3.2)
    sulphates = st.slider("Sulphates", 0.3, 2.0, 0.6)
    alcohol = st.slider("Alcohol %", 8.0, 15.0, 10.0)

# -----------------------------
# 2️⃣ PREDICTION + VISUALS
# -----------------------------
if st.button("🔍 Predict Quality"):

    input_data = [[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                   chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                   density, pH, sulphates, alcohol]]

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.subheader("📌 Prediction Result")
    if prediction[0] >= 7:
        st.success(f"🌟 High Quality Wine (Score: {prediction[0]})")
    else:
        st.warning(f"⚠️ Average/Low Quality Wine (Score: {prediction[0]})")

    # -----------------------------
    # 3️⃣ RADAR CHART (add here)
    # -----------------------------
    features = ['Fixed Acidity', 'Volatile Acidity', 'Citric Acid', 'Residual Sugar',
                'Chlorides', 'Free SO2', 'Total SO2', 'Density', 'pH', 'Sulphates', 'Alcohol']
    values = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
              chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
              density, pH, sulphates, alcohol]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=features,
        fill='toself',
        name='Wine Features'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False,
        title="📈 Your Wine Features Profile"
    )
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # 4️⃣ GAUGE METER (add here)
    # -----------------------------
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction[0],
        title={'text': "Predicted Quality"},
        gauge={'axis': {'range': [0, 10]},
               'bar': {'color': "green" if prediction[0] >= 7 else "red"}}
    ))
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 5️⃣ OPTIONAL SIDEBAR HISTOGRAM
# -----------------------------
if st.sidebar.checkbox("Show Quality Distribution"):
    data = pd.read_csv("winequality.csv")
    fig3, ax = plt.subplots()
    ax.hist(data['quality'], bins=7, color='purple', edgecolor='black')
    ax.set_xlabel("Quality")
    ax.set_ylabel("Count")
    ax.set_title("Wine Quality Distribution")
    st.sidebar.pyplot(fig3)
