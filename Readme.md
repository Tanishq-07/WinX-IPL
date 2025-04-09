# 🏏 WinX-IPL

**WinX-IPL** is an intelligent IPL match win predictor that calculates a team’s winning probability during the second innings of a match. It uses machine learning (Logistic Regression) trained on historical IPL data and offers a user-friendly web interface for real-time predictions and match progression visualization.

---

## 🚀 Features

- 📊 **Live Match Prediction**: Predicts win/loss probabilities dynamically during a match.
- 📈 **Over-by-Over Progression**: Visualizes team performance by tracking runs and wickets per over.
- 🏙️ **City & Venue Support**: Supports all IPL match venues, including international ones.
- 🏏 **Updated Team Mapping**:
  - Punjab Kings (formerly Kings XI Punjab)
  - Delhi Capitals (formerly Delhi Daredevils)
  - Sunrisers Hyderabad (formerly Deccan Chargers)
  - ✅ New Teams Supported: Gujarat Titans, Lucknow Super Giants

---

## 🧠 Model Details

- **Algorithm**: Logistic Regression (via `scikit-learn`)
- **Target Variable**: Match result (`Win` = 1, `Lose` = 0)
- **Features Used**:
  - Batting Team
  - Bowling Team
  - City
  - Runs Left
  - Balls Left
  - Wickets in Hand
  - Target
  - Current Run Rate (CRR)
  - Required Run Rate (RRR)

---

## 🗂️ Project Structure


---

## 🖥️ How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/WinX-IPL.git
cd WinX-IPL

pip install -r requirements.txt

streamlit run app.py
