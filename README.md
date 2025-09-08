# Heart Disease Prediction App

This is a Streamlit web application that predicts the likelihood of heart disease based on user input features.

## Features

- User-friendly web interface for inputting patient data
- Predicts heart disease using a trained machine learning model (`model.pkl`)
- Displays prediction results instantly

## Requirements

- Python 3.7+
- See `requirements.txt` for required Python packages

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure `model.pkl` is present in the project directory.

## Usage

Run the app with:

```
streamlit run app.py
```

Then open the provided local URL in your browser.

## Input Fields

- Age
- Chest pain type
- Heart pain (numeric value)
- Exercise pain
- Oldpeak
- Number of blood vessels
- Blood disorder

## Output

- Displays whether heart disease is detected or not based on the input.

---
**Note:** The accuracy and reliability of predictions depend on the quality and scope of the trained model (`model.pkl`).
