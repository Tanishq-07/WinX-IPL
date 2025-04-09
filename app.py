import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("🏏 IPL Win Predictor")

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Gujarat Titans',
 'Lucknow Super Giants']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Lucknow', 'Guwahati', 'Mohali']

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted([team for team in teams if team != batting_team]))

city = st.selectbox('Select Host City', sorted(set(cities)))

target = st.number_input('Target', min_value=1)
score = st.number_input('Current Score', min_value=0, max_value=target)

overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1, format="%.1f")
wickets = st.number_input('Wickets Fallen', min_value=0, max_value=10)

if st.button('Predict Probability'):
    balls_bowled = overs * 6
    balls_left = 120 - balls_bowled
    wickets_left = 10 - wickets
    runs_left = target - score
    crr = score / overs if overs > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = {
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'target': [target],
        'crr': [crr],
        'rrr': [rrr]
    }

    import pandas as pd
    input_df = pd.DataFrame(input_df)

    prediction = pipe.predict_proba(input_df)
    loss_prob = np.round(prediction[0][0] * 100, 2)
    win_prob = np.round(prediction[0][1] * 100, 2)

    st.header("📊 Win Prediction")
    st.success(f"{batting_team} Win Probability: {win_prob}%")
    st.error(f"{bowling_team} Win Probability: {loss_prob}%")
