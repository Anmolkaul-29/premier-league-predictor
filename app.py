import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('epl_model.pkl')

# Title and intro
st.title("🏟️ Premier League Match Outcome Predictor")
st.write("Enter match statistics below to predict the result (Home Win / Draw / Away Win).")

# Input fields
home_shots = st.number_input("Home Shots", min_value=0)
away_shots = st.number_input("Away Shots", min_value=0)
home_shots_on_target = st.number_input("Home Shots on Target", min_value=0)
away_shots_on_target = st.number_input("Away Shots on Target", min_value=0)
home_corners = st.number_input("Home Corners", min_value=0)
away_corners = st.number_input("Away Corners", min_value=0)
home_fouls = st.number_input("Home Fouls", min_value=0)
away_fouls = st.number_input("Away Fouls", min_value=0)
home_yellow = st.number_input("Home Yellow Cards", min_value=0)
away_yellow = st.number_input("Away Yellow Cards", min_value=0)
home_red = st.number_input("Home Red Cards", min_value=0)
away_red = st.number_input("Away Red Cards", min_value=0)

# Predict button
if st.button("Predict Outcome"):
    input_data = pd.DataFrame([[home_shots, away_shots, home_shots_on_target, away_shots_on_target,
                                home_corners, away_corners, home_fouls, away_fouls,
                                home_yellow, away_yellow, home_red, away_red]],
                              columns=['HomeShots', 'AwayShots', 'HomeShotsOnTarget', 'AwayShotsOnTarget',
                                       'HomeCorners', 'AwayCorners', 'HomeFouls', 'AwayFouls',
                                       'HomeYellowCards', 'AwayYellowCards', 'HomeRedCards', 'AwayRedCards'])

    result = model.predict(input_data)[0]
    st.success(f"🏆 Predicted Match Result: **{result}**")
