import streamlit as st
import requests

"""
# Zoologist : Identify your penguin !
"""

st.markdown(
    """
    ## What does your penguin look like ?

    ### Select your parameters !
    """
)

island = st.radio('Select an island', ('Dream', 'Torgersen', 'Biscoe'))

bill_length = st.slider('Select bill length', 25, 70, 35, 2)

bill_depth = st.slider('Select bill depth', 10, 25, 15, 1)

flipper_length = st.slider('Select flipper length', 160, 240, 200, 5)

body_mass = st.number_input("Insert the penguin's body mass", 1000, 8000, 3000)

sex = st.radio("Select penguin's sex", ('Male', 'Female'))


api_url = st.secrets['API_URL']

params = {
    'island': island,
    'bill_length_mm': bill_length,
    'bill_depth_mm': bill_depth,
    'flipper_length_mm': flipper_length,
    'body_mass_g': body_mass,
    'sex': sex
}
response = requests.get(api_url, params=params).json()

st.markdown(f"## Your penguin is a ....... \n # {response['species']} !!!")
