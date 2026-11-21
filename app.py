
import streamlit as st
import pandas as pd
import joblib
import json

# Configuration
st.set_page_config(
    page_title="Prédiction du rendement agricole",
    page_icon="🌱",
    layout="centered"
)

# Chargement du modèle
@st.cache_resource
def load_model():
    return joblib.load("modele_rendement_agricole.pkl")

model = load_model()

# Chargement des catégories
with open("categories.json", "r", encoding="utf-8") as f:
    categories = json.load(f)

# Titre
st.title("🌱 Prédiction du rendement agricole")
st.write(
    "Cette application estime le rendement agricole "
    "à partir des conditions climatiques et agricoles."
)

st.divider()

# Saisie des paramètres numériques
st.subheader("1. Conditions climatiques")

temperature = st.number_input(
    "Température (°C)",
    value=25.0
)

rainfall = st.number_input(
    "Précipitations (mm)",
    min_value=0.0,
    value=600.0
)

humidity = st.number_input(
    "Humidité (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# Saisie des paramètres catégoriels
st.subheader("2. Conditions agricoles")

soil_type = st.selectbox(
    "Type de sol",
    categories["Soil Type"]
)

weather = st.selectbox(
    "Conditions météorologiques",
    categories["Weather Condition"]
)

crop = st.selectbox(
    "Type de culture",
    categories["Crop Type"]
)

# Prédiction
if st.button("Prédire le rendement", type="primary"):

    input_data = pd.DataFrame([{
        "Temperature (°C)": temperature,
        "Rainfall (mm)": rainfall,
        "Humidity (%)": humidity,
        "Soil Type": soil_type,
        "Weather Condition": weather,
        "Crop Type": crop
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.success(
            f"Rendement estimé : {prediction:.2f} tonnes/hectare"
        )

        st.caption(
            "Cette valeur est une estimation expérimentale "
            "et ne constitue pas une garantie de rendement."
        )

    except Exception as e:
        st.error(f"Erreur pendant la prédiction : {e}")

st.divider()

st.caption(
    "Projet PFA – Prédiction du rendement agricole "
    "à partir de données climatiques et agricoles."
)