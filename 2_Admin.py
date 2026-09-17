import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EVOMAX Admin",
    page_icon="✈️",
    layout="wide"
)

# --------------------------------------------------
# STYLE + ANIMATIONS
# --------------------------------------------------

st.markdown("""
<style>

/* Page */
.block-container {
    max-width: 1250px;
    padding-top: 35px;
}

/* Header */
.ev-label {
    color: #777;
    font-size: 12px;
    letter-spacing: 3px;
    font-weight: 600;
}

.ev-title {
    font-size: 36px;
    font-weight: 800;
    color: #111;
    margin-top: 5px;
}

.ev-subtitle {
    color: #777;
    margin-bottom: 30px;
}

/* Metric Cards */
.metric-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 25px;
    transition: 0.25s ease;
    animation: fadeUp 0.7s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
}

.metric-label {
    color: #777;
    font-size: 12px;
    letter-spacing: 1px;
}

.metric-number {
    font-size: 38px;
    font-weight: 800;
    color: #111;
    margin-top: 8px;
}

/* Sections */
.section-card {
    background: white;
    border: 1px solid #E5E7EB;
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
    animation: fadeUp 0.8s ease;
}

.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #111;
}

/* Pipeline */
.pipeline-row {
    margin-top: 22px;
}

.pipeline-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
}

.progress-bg {
    height: 9px;
    background: #EEEEEE;
    border-radius: 20px;
    overflow: hidden;
}

.progress-blue {
    height: 100%;
    background: #2563EB;
    border-radius: 20px;
    animation: growBar 1.5s ease;
}

.progress-yellow {
    height: 100%;
    background: #F5D547;
    border-radius: 20px;
    animation: growBar 1.7s ease;
}

.progress-black {
    height: 100%;
    background: #111111;
    border-radius: 20px;
    animation: growBar 1.9s ease;
}

/* Animation */
@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes growBar {

    from {
        width: 0%;
    }
}

/* Status */
.status-paid {
    background: #E8F7ED;
    color: #247A3D;
    padding: 5px 10px;
    border-radius: 20px;
}

.status-pending {
    background: #FFF5D6;
    color: #8A6500;
    padding: 5px 10px;
    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="ev-label">
EVOMAX • GLOBAL MOBILITY
</div>

<div class="ev-title">
Operations Dashboard
</div>

<div class="ev-subtitle">
Manage clients, payments and visa cases.
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SAMPLE DATA
# --------------------------------------------------

clients = [
    {
        "Client": "Aarav Sharma",
        "Visa": "US Visitor",
        "Payment": "Paid",
        "Status": "Document Review",
        "Updated": "Today"
    },
    {
        "Client": "Maya Reddy",
        "Visa": "Student Visa",
        "Payment": "Paid",
        "Status": "Appointment Booked",
        "Updated": "Today"
    },
    {
        "Client": "Noah Kumar",
        "Visa": "Work Visa",
        "Payment": "Pending",
        "Status": "Monitoring",
        "Updated": "Yesterday"
    },
    {
        "Client": "Sara Patel",
        "Visa": "Family Visa",
        "Payment": "Paid",
        "Status": "Details Received",
        "Updated": "Sep 14"
    }
]

df = pd.DataFrame(clients)


# --------------------------------------------------
# METRICS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">TOTAL CLIENTS</div>
        <div class="metric-number">128</div>
        <div style="color:#888;">All clients</div>
    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">ACTIVE CASES</div>
        <div class="metric-number">46</div>
        <div style="color:#888;">In progress</div>
    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">PAYMENT PENDING</div>
        <div class="metric-number">9</div>
        <div style="color:#888;">Need follow-up</div>
    </div>
    """, unsafe_allow_html=True)


with c4:

    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">APPOINTMENTS</div>
        <div class="metric-number">21</div>
        <div style="color:#888;">Successfully booked</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# VISA PIPELINE
# --------------------------------------------------

st.markdown("""
<div class="section-card">

<div class="section-title">
Visa Pipeline
</div>

<div style="color:#888;">
Current active workload
</div>


<div class="pipeline-row">

<div class="pipeline-info">
<span>Details Received</span>
<strong>18</strong>
</div>

<div class="progress-bg">
<div class="progress-blue" style="width:90%;"></div>
</div>

</div>


<div class="pipeline-row">

<div class="pipeline-info">
<span>Document Review</span>
<strong>12</strong>
</div>

<div class="progress-bg">
<div class="progress-yellow" style="width:65%;"></div>
</div>

</div>


<div class="pipeline-row">

<div class="pipeline-info">
<span>Appointment Monitoring</span>
<strong>10</strong>
</div>

<div class="progress-bg">
<div class="progress-black" style="width:50%;"></div>
</div>

</div>


<div class="pipeline-row">

<div class="pipeline-info">
<span>Appointment Booked</span>
<strong>6</strong>
</div>

<div class="progress-bg">
<div class="progress-blue" style="width:30%;"></div>
</div>

</div>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# CLIENT MANAGEMENT
# --------------------------------------------------

st.markdown("## Clients")

search = st.text_input(
    "Search clients",
    placeholder="Search name, visa type or status..."
)

status_filter = st.selectbox(
    "Case Status",
    [
        "All",
        "Details Received",
        "Document Review",
        "Monitoring",
        "Appointment Booked"
    ]
)

filtered_df = df.copy()

if search:

    mask = filtered_df.astype(str).apply(
        lambda row: row.str.contains(
            search,
            case=False
        ).any(),
        axis=1
    )

    filtered_df = filtered_df[mask]


if status_filter != "All":

    filtered_df = filtered_df[
        filtered_df["Status"] == status_filter
    ]


st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# RECENT ACTIVITY
# --------------------------------------------------

st.markdown("## Recent Activity")

st.write("🟢 **Maya Reddy** — Appointment booked")

st.write("🔵 **Aarav Sharma** — Documents received")

st.write("🟡 **Noah Kumar** — Payment pending")

st.write("⚫ **Sara Patel** — Client details submitted")