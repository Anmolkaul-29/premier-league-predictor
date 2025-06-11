import streamlit as st
import pandas as pd
import joblib

# Load the trained model
try:
    model = joblib.load('epl_model.pkl')
except:
    st.error("❌ Failed to load the model. Make sure 'epl_model.pkl' is in the repo.")
    st.stop()

# Sidebar info
st.sidebar.markdown("### 👤 Made by Anmol Kaul")
st.sidebar.markdown("[🔗 GitHub Repo](https://github.com/your-repo-link)")
st.sidebar.markdown("[💼 LinkedIn](https://linkedin.com/in/your-link)")
st.sidebar.markdown("📧 anmolkaul123@gmail.com")

# Main Title
st.title("🏟️ Premier League Match Outcome Predictor")
st.write("Enter match statistics below to predict the result (Home Win / Draw / Away Win).")

# Inputs with default values
home_shots = st.number_input("Home Shots", min_value=0, value=12)
away_shots = st.number_input("Away Shots", min_value=0, value=10)
home_shots_on_target = st.number_input("Home Shots on Target", min_value=0, value=5)
away_shots_on_target = st.number_input("Away Shots on Target", min_value=0, value=4)
home_corners = st.number_input("Home Corners", min_value=0, value=6)
away_corners = st.number_input("Away Corners", min_value=0, value=5)
home_fouls = st.number_input("Home Fouls", min_value=0, value=10)
away_fouls = st.number_input("Away Fouls", min_value=0, value=11)
home_yellow = st.number_input("Home Yellow Cards", min_value=0, value=2)
away_yellow = st.number_input("Away Yellow Cards", min_value=0, value=2)
home_red = st.number_input("Home Red Cards", min_value=0, value=0)
away_red = st.number_input("Away Red Cards", min_value=0, value=0)

# Prediction
if st.button("Predict Outcome"):
    input_data = pd.DataFrame([[home_shots, away_shots, home_shots_on_target, away_shots_on_target,
                                home_corners, away_corners, home_fouls, away_fouls,
                                home_yellow, away_yellow, home_red, away_red]],
                              columns=['HomeShots', 'AwayShots', 'HomeShotsOnTarget', 'AwayShotsOnTarget',
                                       'HomeCorners', 'AwayCorners', 'HomeFouls', 'AwayFouls',
                                       'HomeYellowCards', 'AwayYellowCards', 'HomeRedCards', 'AwayRedCards'])

    result = model.predict(input_data)[0]

    if result == "HomeWin":
        st.success("✅ Predicted Result: Home Team is likely to win!")
    elif result == "AwayWin":
        st.warning("⚠️ Predicted Result: Away Team might take the win!")
    else:
        st.info("🤝 Predicted Result: Looks like a Draw!")

    st.markdown("🔍 **Model Accuracy**: 78% (on test data)")

# Footer
st.markdown("---")
st.caption("📌 This is a project for learning sports analytics using Python, Machine Learning, and Streamlit.")
