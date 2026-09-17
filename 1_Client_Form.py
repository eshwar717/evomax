import streamlit as st

st.set_page_config(
    page_title="Client Details | EVOMAX",
    page_icon="✈️",
    layout="centered"
)

st.markdown("""
<style>
.block-container {
    max-width: 760px;
    padding-top: 40px;
}

.form-header {
    background: linear-gradient(135deg, #0B1F3B, #123A70);
    padding: 35px;
    border-radius: 20px;
    margin-bottom: 25px;
}

.form-header h1 {
    color: white;
    margin: 0;
}

.form-header p {
    color: #CBD5E1;
    margin: 8px 0 0;
}

.brand {
    color: #F7D84A;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
}

.stButton button {
    background: #0B1F3B;
    color: white;
    border-radius: 30px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="form-header">
    <div class="brand">EVOMAX</div>
    <h1>Client Information</h1>
    <p>Please provide your details carefully. Our team will use this information to assist with your case.</p>
</div>
""", unsafe_allow_html=True)

with st.form("evomax_client_form"):

    st.subheader("Personal Details")

    full_name = st.text_input("Full Name *")
    email = st.text_input("Email Address *")
    phone = st.text_input("WhatsApp / Phone Number *")

    col1, col2 = st.columns(2)

    with col1:
        nationality = st.text_input("Nationality")

    with col2:
        residence = st.text_input("Country of Residence")

    st.divider()

    st.subheader("Visa Details")

    visa_type = st.selectbox(
        "Visa Type *",
        [
            "Select visa type",
            "Visitor Visa",
            "Student Visa",
            "Work Visa",
            "Business Visa",
            "Family Visa",
            "Other"
        ]
    )

    destination = st.selectbox(
        "Destination Country *",
        [
            "Select destination",
            "United States",
            "Canada",
            "United Kingdom",
            "Australia",
            "Germany",
            "UAE",
            "Other"
        ]
    )

    notes = st.text_area(
        "Additional Information",
        placeholder="Tell us anything important about your case...",
        height=120
    )

    st.divider()

    consent = st.checkbox(
        "I confirm that the information I provided is accurate and I consent to EVOMAX using it to assist with my requested service."
    )

    submit = st.form_submit_button(
        "Submit to EVOMAX",
        use_container_width=True
    )


if submit:

    if not full_name or not email or not phone:
        st.error("Please complete your name, email and phone number.")

    elif visa_type == "Select visa type":
        st.error("Please select your visa type.")

    elif destination == "Select destination":
        st.error("Please select your destination country.")

    elif not consent:
        st.error("Please confirm the consent box.")

    else:
        st.success("✓ Details submitted successfully.")
        st.info("Thank you. The EVOMAX team will review your information and contact you.")