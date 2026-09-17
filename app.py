import urllib.parse

import streamlit as st

st.set_page_config(
    page_title="EVOMAX | Global Mobility Simplified",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DESIGN
# =========================================================

st.markdown("""
<style>

#MainMenu, footer, header {
    visibility: hidden;
}

.stApp {
    background:
        radial-gradient(circle at 85% 10%, rgba(255,214,64,.20), transparent 25%),
        radial-gradient(circle at 10% 40%, rgba(37,99,235,.10), transparent 25%),
        #ffffff;
    color: #111111;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

/* ---------------- NAV ---------------- */

.nav {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:15px 0 25px;
}

.logo {
    font-size:38px;
    font-weight:900;
    letter-spacing:5px;
    color:#111111;
}

.logo span {
    color:#F2C94C;
}

.tagline {
    font-size:10px;
    letter-spacing:3px;
    color:#64748B;
    font-weight:700;
}


/* ---------------- HERO ---------------- */

.hero {
    position:relative;
    overflow:hidden;

    background:
        linear-gradient(
            125deg,
            #07111F 0%,
            #0B1F3B 55%,
            #123A70 100%
        );

    border-radius:30px;

    padding:
        clamp(55px,8vw,100px)
        clamp(30px,7vw,80px);

    margin-top:15px;

    box-shadow:
        0 25px 70px rgba(11,31,59,.20);

    animation:fadeUp .8s ease;
}


/* Yellow decorative light */

.hero:before {
    content:"";
    position:absolute;

    width:350px;
    height:350px;

    right:-100px;
    top:-130px;

    border-radius:50%;

    background:#F2C94C;

    filter:blur(5px);

    opacity:.95;
}


/* Blue glow */

.hero:after {
    content:"";

    position:absolute;

    width:350px;
    height:350px;

    right:100px;
    bottom:-250px;

    border-radius:50%;

    background:#2563EB;

    filter:blur(70px);

    opacity:.35;
}


.hero-content {
    position:relative;
    z-index:2;
    max-width:750px;
}


.hero-label {
    display:inline-block;

    background:rgba(255,255,255,.09);

    border:1px solid rgba(255,255,255,.15);

    color:#F7D84A;

    padding:9px 15px;

    border-radius:50px;

    font-size:11px;

    font-weight:700;

    letter-spacing:2px;
}


.hero h1 {

    color:white !important;

    font-size:
        clamp(45px,6vw,72px);

    line-height:1.03;

    letter-spacing:-2px;

    margin:
        25px 0 22px;

    font-weight:800;
}


.hero-highlight {
    color:#F7D84A;
}


.hero p {

    color:#CBD5E1 !important;

    font-size:18px;

    max-width:630px;

    line-height:1.7;
}


/* ---------------- FLOATING PLANE ---------------- */

.plane {

    position:absolute;

    right:12%;

    top:42%;

    z-index:3;

    font-size:55px;

    transform:rotate(-15deg);

    animation:
        fly 4s ease-in-out infinite;
}


/* ---------------- SECTION ---------------- */

.section {
    padding:75px 0 25px;
}


.section-label {

    color:#2563EB;

    font-size:11px;

    font-weight:800;

    letter-spacing:3px;

    text-align:center;
}


.section-title {

    color:#0B1F3B;

    text-align:center;

    font-size:40px;

    font-weight:800;

    margin-top:8px;
}


.section-text {

    color:#64748B;

    text-align:center;

    font-size:16px;

    max-width:650px;

    margin:10px auto 35px;
}


/* ---------------- SERVICES ---------------- */

.service-card {

    min-height:235px;

    background:white;

    border:
        1px solid #E2E8F0;

    border-radius:22px;

    padding:30px;

    box-shadow:
        0 8px 30px rgba(15,23,42,.06);

    transition:
        transform .3s ease,
        box-shadow .3s ease,
        border .3s ease;

    animation:
        fadeUp .8s ease;
}


.service-card:hover {

    transform:
        translateY(-10px);

    box-shadow:
        0 22px 50px rgba(15,23,42,.13);

    border-color:
        #F2C94C;
}


.service-icon {

    width:55px;

    height:55px;

    display:flex;

    align-items:center;

    justify-content:center;

    border-radius:16px;

    background:
        linear-gradient(
            135deg,
            #FFF7CC,
            #F7D84A
        );

    font-size:27px;

    margin-bottom:22px;
}


.service-card h3 {

    color:#0B1F3B;

    font-size:22px;

    margin-bottom:10px;
}


.service-card p {

    color:#64748B;

    line-height:1.6;

}


/* ---------------- PROCESS ---------------- */

.process {

    background:#F8FAFC;

    border-radius:30px;

    padding:50px;

    margin-top:65px;

    border:1px solid #E2E8F0;
}


.step-number {

    width:45px;

    height:45px;

    display:flex;

    align-items:center;

    justify-content:center;

    background:#0B1F3B;

    color:#F7D84A;

    border-radius:50%;

    font-weight:800;

    margin-bottom:15px;
}


.step-title {

    color:#0B1F3B;

    font-size:18px;

    font-weight:700;
}


.step-text {

    color:#64748B;

    font-size:14px;

    line-height:1.6;
}


/* ---------------- CTA ---------------- */

.cta {

    margin-top:80px;

    padding:55px 40px;

    text-align:center;

    border-radius:28px;

    background:
        linear-gradient(
            120deg,
            #F7D84A,
            #FFD93D
        );

    box-shadow:
        0 20px 50px rgba(242,201,76,.25);
}


.cta h2 {

    color:#0B1F3B;

    font-size:36px;

    font-weight:900;

    margin:0;
}


.cta p {

    color:#334155;

    font-size:16px;
}


/* ---------------- BUTTONS ---------------- */

.stLinkButton a {

    background:#0B1F3B !important;

    color:white !important;

    border:none !important;

    border-radius:50px !important;

    padding:
        12px 25px !important;

    font-weight:700 !important;

    transition:.25s !important;
}


.stLinkButton a:hover {

    background:#2563EB !important;

    transform:
        translateY(-2px);
}


/* ---------------- FOOTER ---------------- */

.footer {

    margin-top:70px;

    border-top:
        1px solid #E2E8F0;

    padding:35px 0;

    text-align:center;

    color:#64748B;

    font-size:13px;
}


/* ---------------- ANIMATIONS ---------------- */

@keyframes fadeUp {

    from {
        opacity:0;
        transform:
            translateY(25px);
    }

    to {
        opacity:1;
        transform:
            translateY(0);
    }
}


@keyframes fly {

    0%,100% {
        transform:
            translateY(0)
            rotate(-15deg);
    }

    50% {
        transform:
            translateY(-18px)
            translateX(12px)
            rotate(-10deg);
    }
}


/* Mobile */

@media(max-width:700px){

    .hero {
        border-radius:20px;
    }

    .plane {
        opacity:.25;
        right:5%;
    }

    .process {
        padding:30px 20px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="nav">

<div>

<div class="logo">
EVO<span>MAX</span>
</div>

<div class="tagline">
GLOBAL MOBILITY. SIMPLIFIED.
</div>

</div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-content">

<div class="hero-label">
GLOBAL VISA & MOBILITY
</div>

<h1>
Your Global Journey.<br>
<span class="hero-highlight">
Made Simpler.
</span>
</h1>

<p>
Professional visa processing and global mobility
support designed to make your international journey
clearer, easier and more organized.
</p>

</div>

<div class="plane">
✈
</div>

</div>
""", unsafe_allow_html=True)


st.write("")

# WhatsApp number in API format without spaces or plus sign
whatsapp_number = "917013193257"
whatsapp_message = "Hi EVOMAX, I want to start my visa process."

st.link_button(
    "💬 Chat with EVOMAX on WhatsApp",
    f"https://wa.me/{whatsapp_number}?text={urllib.parse.quote(whatsapp_message)}"
)


# =========================================================
# SERVICES
# =========================================================

st.markdown("""
<div class="section">

<div class="section-label">
WHAT WE DO
</div>

<div class="section-title">
Visa Services
</div>

<div class="section-text">
Professional support for your international
travel, study and career journey.
</div>

</div>
""", unsafe_allow_html=True)


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown("""
    <div class="service-card">

        <div class="service-icon">
        🎓
        </div>

        <h3>
        Student Visa
        </h3>

        <p>
        Support for students preparing
        for international education
        opportunities.
        </p>

    </div>
    """, unsafe_allow_html=True)


with c2:

    st.markdown("""
    <div class="service-card">

        <div class="service-icon">
        💼
        </div>

        <h3>
        Work Visa
        </h3>

        <p>
        Professional support for
        international employment and
        mobility requirements.
        </p>

    </div>
    """, unsafe_allow_html=True)


with c3:

    st.markdown("""
    <div class="service-card">

        <div class="service-icon">
        ✈️
        </div>

        <h3>
        Visitor Visa
        </h3>

        <p>
        Assistance for tourism,
        family visits and eligible
        short-term international travel.
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# PROCESS
# =========================================================

st.markdown("""
<div class="process">

<div class="section-label">
SIMPLE PROCESS
</div>

<div class="section-title">
How EVOMAX Works
</div>

</div>
""", unsafe_allow_html=True)


p1, p2, p3, p4 = st.columns(4)


with p1:

    st.markdown("""
    <div class="step-number">01</div>

    <div class="step-title">
    Contact Us
    </div>

    <div class="step-text">
    Start your conversation with
    EVOMAX through WhatsApp.
    </div>
    """, unsafe_allow_html=True)


with p2:

    st.markdown("""
    <div class="step-number">02</div>

    <div class="step-title">
    Consultation
    </div>

    <div class="step-text">
    Discuss your requirements,
    service and applicable fees.
    </div>
    """, unsafe_allow_html=True)


with p3:

    st.markdown("""
    <div class="step-number">03</div>

    <div class="step-title">
    Submit Details
    </div>

    <div class="step-text">
    Complete the secure client
    information form.
    </div>
    """, unsafe_allow_html=True)


with p4:

    st.markdown("""
    <div class="step-number">04</div>

    <div class="step-title">
    Case Support
    </div>

    <div class="step-text">
    EVOMAX assists with the
    agreed processing services.
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CTA
# =========================================================

st.markdown("""
<div class="cta">

<h2>
Ready to Go Global?
</h2>

<p>
Your next journey starts with one conversation.
</p>

</div>
""", unsafe_allow_html=True)


st.write("")

st.link_button(
    "💬 Start Your Journey",
    f"https://wa.me/{whatsapp_number}?text={urllib.parse.quote(whatsapp_message)}"
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<strong>
EVOMAX GLOBAL SOLUTIONS PVT LIMITED
</strong>

<br>

GLOBAL MOBILITY. SIMPLIFIED.

<br><br>

EVOMAX provides visa processing and
administrative support services.
Visa decisions are made by the relevant
government authorities.

</div>
""", unsafe_allow_html=True)