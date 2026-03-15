import streamlit as st
from predict import predict_risk

st.set_page_config(
    page_title="TransactIQ Risk Engine",
    page_icon="💳",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .hero-card {
        background: linear-gradient(135deg, #111827 0%, #1e3a5f 100%);
        padding: 1.8rem 2rem;
        border-radius: 18px;
        border: 1px solid #243b5a;
        margin-bottom: 1.2rem;
    }

    .hero-title {
        color: white;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1rem;
    }

    .section-card {
        background: #081225;
        padding: 1.25rem;
        border-radius: 18px;
        border: 1px solid #1f3654;
        margin-bottom: 1rem;
    }

    .section-title {
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }

    .section-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
    }

    .note-text {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 0.75rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3rem;
        font-weight: 700;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-card">
    <div class="hero-title">TransactIQ Risk Engine</div>
    <div class="hero-subtitle">
        Credit default probability scoring for borrower risk assessment.
    </div>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1.2, 0.9], gap="large")

with left_col:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Borrower Information</div>
        <div class="section-subtitle">
            Enter applicant details below to estimate default probability and risk category.
        </div>
    </div>
    """, unsafe_allow_html=True)

    loan_amnt = st.number_input("Loan Amount", min_value=500.0, value=15000.0, step=500.0)
    term = st.selectbox("Loan Term (months)", [36, 60])
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=12.5, step=0.1)
    installment = st.number_input("Installment", min_value=0.0, value=450.0, step=10.0)
    annual_inc = st.number_input("Annual Income", min_value=0.0, value=65000.0, step=1000.0)

    col1, col2 = st.columns(2)
    with col1:
        dti = st.number_input("Debt-to-Income Ratio", min_value=0.0, value=18.0, step=0.1)
        delinq_2yrs = st.number_input("Delinquencies in Last 2 Years", min_value=0.0, value=0.0, step=1.0)
    with col2:
        revol_util = st.number_input("Revolving Utilization (%)", min_value=0.0, value=45.0, step=0.1)
        total_acc = st.number_input("Total Credit Accounts", min_value=1.0, value=12.0, step=1.0)

    predict_clicked = st.button("Predict Risk")

with right_col:
    st.markdown("""
    <div class="section-card">
        <div class="section-title">Prediction Summary</div>
        <div class="section-subtitle">
            The model output will appear here after running the risk assessment.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if predict_clicked:
        prob, risk = predict_risk(
            loan_amnt,
            term,
            int_rate,
            installment,
            annual_inc,
            dti,
            delinq_2yrs,
            revol_util,
            total_acc
        )

        if risk == "Low Risk":
            recommendation = "Approve / Low concern"
        elif risk == "Medium Risk":
            recommendation = "Manual review required"
        else:
            recommendation = "High caution / Reject or escalate"

        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("Default Probability", f"{prob:.2%}")
        with metric_col2:
            st.metric("Risk Category", risk)

        st.markdown("### Recommendation")
        st.info(recommendation)

        if risk == "Low Risk":
            st.success("Low default risk")
        elif risk == "Medium Risk":
            st.warning("Medium default risk")
        else:
            st.error("High default risk")

        st.markdown(
            '<div class="note-text">This output is intended for decision support and screening assistance only.</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("Fill in the borrower details and click 'Predict Risk' to view the assessment.")