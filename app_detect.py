import streamlit as st
import pickle
import numpy as np

# Charger le modèle pré-entraîné
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Titre de l'application
st.title('Détection de Fraude Transactionnelle')

# Instructions
st.write('Veuillez entrer les détails de la transaction pour vérifier si elle est frauduleuse.')

# Inputs utilisateur
time = st.number_input('Temps (Time)', min_value=0)
amount = st.number_input('Montant (Amount)', min_value=0.0)
v4 = st.number_input('V4', min_value=-100.0, max_value=100.0)

# Bouton de prédiction
if st.button('Vérifier la transaction'):
    # Préparation des données d'entrée pour le modèle
    input_data = np.array([[time, amount, v4]])
    
    # Prédiction
    prediction = model.predict(input_data)
    
    # Affichage du résultat
    if prediction[0] == 1:
        st.error('La transaction est frauduleuse.')
    else:
        st.success('La transaction est non frauduleuse.')
