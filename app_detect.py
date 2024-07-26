import streamlit as st
import joblib
import numpy as np

# Charger le modèle
model = joblib.load('random_forest_model.joblib')

# Titre de l'application
st.title('Détection de Fraude dans les Transactions')

# Entrées utilisateur
time = st.number_input('Time', min_value=0)
amount = st.number_input('Amount', min_value=0.0)
v4 = st.number_input('V4')

# Prédiction
if st.button('Prédire'):
    input_data = np.array([[time, amount, v4]])
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f'Transaction Frauduleuse avec une probabilité de {prediction_proba[0][1]*100:.2f}%')
    else:
        st.success(f'Transaction Légitime avec une probabilité de {prediction_proba[0][0]*100:.2f}%')

# Instructions d'exécution
st.write("""
### Instructions
1. Entrez les valeurs pour **Time**, **Amount** et **V4**.
2. Cliquez sur **Prédire** pour voir le résultat de la prédiction.
""")
