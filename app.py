import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Student Performance Prediction", page_icon="🎓")

st.title("🎓 Student Performance Prediction")
st.write("Enter the student's grades to check whether extra attention is needed.")


@st.cache_resource
def load_model():
    return joblib.load("student_performance_model.pkl")


try:
    model = load_model()
except FileNotFoundError:
    st.error("student_performance_model.pkl not found. Run the notebook once to save "
             "the model, and keep the file in the same folder as app.py.")
    st.stop()

# Grade inputs
col1, col2 = st.columns(2)
g1 = col1.slider("Period 1 Grade (G1)", 0, 20, 10)
g2 = col2.slider("Period 2 Grade (G2)", 0, 20, 10)

# Prediction (DataFrame keeps the feature names the model was trained with)
if st.button("Predict"):
    student = pd.DataFrame([{'G1': g1, 'G2': g2}])
    result = model.predict(student)[0]

    if result == 1:
        st.success("✅ Good performance expected. No special attention required. "
                   "Keep up the consistent study routine!")
    else:
        st.warning("⚠️ Attention required. This student is at risk of low performance. "
                   "Suggested steps: revise weak topics, attend extra classes, "
                   "and meet the teacher for guidance.")