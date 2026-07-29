import streamlit as st
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("models/gradient_boosting_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(
    page_title="E-Commerce Purchase Prediction",
    page_icon="🛒",
    layout="wide"
)

col1, col2 = st.columns([2, 1])

with col1:
    st.title("🛒 E-Commerce Purchase Prediction")
    st.write(
        "Predict whether a customer is likely to complete a purchase based on their browsing session."
    )

with col2:
    st.metric("Model", "Gradient Boosting")
    st.metric("Project", "ML Internship")

st.sidebar.header("Customer Session Details")

# Numerical Inputs
Administrative = st.sidebar.number_input("Administrative", min_value=0)

Administrative_Duration = st.sidebar.number_input(
    "Administrative Duration",
    min_value=0.0
)

Informational = st.sidebar.number_input(
    "Informational",
    min_value=0
)

Informational_Duration = st.sidebar.number_input(
    "Informational Duration",
    min_value=0.0
)

ProductRelated = st.sidebar.number_input(
    "Product Related",
    min_value=0
)

ProductRelated_Duration = st.sidebar.number_input(
    "Product Related Duration",
    min_value=0.0
)

BounceRates = st.sidebar.number_input(
    "Bounce Rates",
    min_value=0.0,
    format="%.4f"
)

ExitRates = st.sidebar.number_input(
    "Exit Rates",
    min_value=0.0,
    format="%.4f"
)

PageValues = st.sidebar.number_input(
    "Page Values",
    min_value=0.0
)

SpecialDay = st.sidebar.number_input(
    "Special Day",
    min_value=0.0
)

# Categorical Inputs
Month = st.sidebar.selectbox(
    "Month",
    [
        "Feb",
        "Mar",
        "Apr",
        "May",
        "June",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]
)

OperatingSystems = st.sidebar.number_input(
    "Operating Systems",
    min_value=1
)

Browser = st.sidebar.number_input(
    "Browser",
    min_value=1
)

Region = st.sidebar.number_input(
    "Region",
    min_value=1
)

TrafficType = st.sidebar.number_input(
    "Traffic Type",
    min_value=1
)

VisitorType = st.sidebar.selectbox(
    "Visitor Type",
    [
        "Returning_Visitor",
        "New_Visitor",
        "Other"
    ]
)

Weekend = st.sidebar.selectbox(
    "Weekend",
    [False, True]
)

# Manual Encoding
month_mapping = {
    "Apr": 0,
    "Aug": 1,
    "Dec": 2,
    "Feb": 3,
    "Jul": 4,
    "June": 5,
    "Mar": 6,
    "May": 7,
    "Nov": 8,
    "Oct": 9,
    "Sep": 10
}

visitor_mapping = {
    "New_Visitor": 0,
    "Other": 1,
    "Returning_Visitor": 2
}

Month = month_mapping[Month]
VisitorType = visitor_mapping[VisitorType]
Weekend = int(Weekend)

# Prediction
# Prediction
if st.button("Predict Purchase"):

    features = np.array([[
        Administrative,
        Administrative_Duration,
        Informational,
        Informational_Duration,
        ProductRelated,
        ProductRelated_Duration,
        BounceRates,
        ExitRates,
        PageValues,
        SpecialDay,
        Month,
        OperatingSystems,
        Browser,
        Region,
        TrafficType,
        VisitorType,
        Weekend
    ]])

    # Scale Features
    features = scaler.transform(features)

    # Predict
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    purchase_probability = probability[0][1]

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("🟢 Customer is likely to purchase.")
    else:
        st.error("🔴 Customer is NOT likely to purchase.")

    st.write(f"Confidence: **{purchase_probability*100:.2f}%**")

    st.progress(float(purchase_probability))

    st.subheader("Customer Session Summary")

    st.write(f"Administrative: {Administrative}")
    st.write(f"Product Related: {ProductRelated}")
    st.write(f"Bounce Rate: {BounceRates}")
    st.write(f"Exit Rate: {ExitRates}")
    st.write(f"Page Values: {PageValues}")
    st.write(f"Visitor Type: {VisitorType}")
    st.write(f"Month: {Month}")
    st.write(f"Weekend: {bool(Weekend)}")

st.divider()

st.caption("Developed by Shiva Gupta | Data Science Internship Project")