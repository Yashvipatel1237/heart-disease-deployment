### cmd ma ek ma python backend.py
### cmd ma streamlit run app.py


import requests
import streamlit as st
import pandas as pd


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(

    page_title="Cardio Risk",

    page_icon="❤️",

    layout="wide",

    initial_sidebar_state="collapsed"

)


# =========================================================
# SESSION STATE
# =========================================================

if "dark" not in st.session_state:

    st.session_state.dark = False


if "page" not in st.session_state:

    st.session_state.page = "Home"


# =========================================================
# BACKEND URL
# =========================================================

BACKEND_URL = "https://heart-disease-deployment-qq80.onrender.com"

# =========================================================
# MODEL METRICS
# =========================================================

ACCURACY = "78%"
ROC_AUC = "73%"
PRECISION = "85%"
RECALL = "88%"


# =========================================================
# THEME
# =========================================================

if st.session_state.dark:

    BG = "#080A14"

    CARD = "#111827"

    TEXT = "#F8F7FF"

    MUTED = "#C9C1DA"

    INPUT_TEXT = "#F3E8FF"

    PRIMARY = "#A78BFA"

    BORDER = "#40345F"

    SHADOW = "rgba(124,58,237,0.25)"

else:

    BG = "#F8F7FF"

    CARD = "#FFFFFF"

    TEXT = "#171426"

    MUTED = "#686276"

    INPUT_TEXT = "#211A35"

    PRIMARY = "#7C3AED"

    BORDER = "#E7DDFB"

    SHADOW = "rgba(124,58,237,0.13)"


# =========================================================
# CSS
# =========================================================

css = """

<style>

html,
body,
.stApp {

    background: __BG__ !important;

    color: __TEXT__ !important;

}


[data-testid="stHeader"] {

    display: none !important;

}


#MainMenu {

    visibility: hidden;

}


footer {

    visibility: hidden;

}


.block-container {

    max-width: 1400px !important;

    padding-top: 18px !important;

    padding-bottom: 50px !important;

    padding-left: 5vw !important;

    padding-right: 5vw !important;

}


/* =========================================================
   TOP LINE
========================================================= */

.top-line {

    height: 3px;

    width: 100%;

    border-radius: 20px;

    margin-bottom: 22px;

    background:
        linear-gradient(
            90deg,
            #7C3AED,
            #8B5CF6,
            #6366F1,
            #2563EB
        );

}


/* =========================================================
   BRAND
========================================================= */

.brand {

    font-size: 23px;

    font-weight: 850;

    color: __TEXT__;

    padding-top: 8px;

}


.brand-heart {

    color: #8B5CF6;

}


.brand-ai {

    color: __PRIMARY__;

}


/* =========================================================
   BUTTONS
========================================================= */

div.stButton > button {

    min-height: 43px !important;

    border-radius: 13px !important;

    border:
        1px solid __BORDER__ !important;

    background:
        __CARD__ !important;

    color:
        __TEXT__ !important;

    font-weight:
        650 !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border 0.25s ease;

}


div.stButton > button p {

    color:
        __TEXT__ !important;

}


div.stButton > button:hover {

    transform:
        translateY(-3px) !important;

    border-color:
        __PRIMARY__ !important;

    color:
        __PRIMARY__ !important;

    box-shadow:
        0 12px 30px
        __SHADOW__ !important;

}


div.stButton > button:hover p {

    color:
        __PRIMARY__ !important;

}


/* =========================================================
   HERO
========================================================= */

.hero {

    min-height:
        430px;

    padding:
        52px;

    border-radius:
        30px;

    overflow:
        hidden;

    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(255,255,255,0.20),
            transparent 27%
        ),

        linear-gradient(
            135deg,
            #3B0764,
            #6D28D9 48%,
            #2563EB
        );

    box-shadow:
        0 30px 75px
        rgba(79,70,229,0.25);

}


.hero-label {

    color:
        #DDD6FE;

    font-size:
        11px;

    font-weight:
        850;

    letter-spacing:
        2px;

    margin-bottom:
        22px;

}


.hero-title {

    color:
        white;

    font-size:
        46px;

    line-height:
        1.08;

    font-weight:
        850;

}


.hero-title span {

    color:
        #C4B5FD;

}


.hero-text {

    color:
        rgba(255,255,255,0.84);

    font-size:
        14px;

    line-height:
        1.8;

    max-width:
        650px;

    margin-top:
        22px;

}


/* =========================================================
   HEART IMAGE
========================================================= */

.heart-box {

    min-height:
        430px;

    border-radius:
        30px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    overflow:
        hidden;

    background:
        linear-gradient(
            145deg,
            #4C1D95,
            #7C3AED 50%,
            #2563EB
        );

}


.heart-image {

    width:
        220px;

    height:
        220px;

    object-fit:
        contain;

    filter:
        drop-shadow(
            0 18px 30px
            rgba(0,0,0,0.28)
        );

    animation:
        heartbeat 1.7s infinite;

}


@keyframes heartbeat {

    0% {
        transform:
            scale(1);
    }

    50% {
        transform:
            scale(1.07);
    }

    100% {
        transform:
            scale(1);
    }

}


/* =========================================================
   SECTIONS
========================================================= */

.section-label {

    margin-top:
        55px;

    color:
        __PRIMARY__;

    font-size:
        10px;

    font-weight:
        850;

    letter-spacing:
        2px;

}


.section-title {

    color:
        __TEXT__;

    font-size:
        34px;

    font-weight:
        850;

    margin-top:
        5px;

}


.section-text {

    color:
        __MUTED__;

    font-size:
        14px;

    line-height:
        1.8;

    max-width:
        800px;

}


/* =========================================================
   CARDS
========================================================= */

.card {

    background:
        __CARD__;

    border:
        1px solid __BORDER__;

    border-radius:
        22px;

    padding:
        28px;

    min-height:
        225px;

    box-shadow:
        0 12px 40px
        __SHADOW__;

    transition:
        0.28s ease;

}


.card:hover {

    transform:
        translateY(-9px);

    border-color:
        __PRIMARY__;

    box-shadow:
        0 25px 60px
        rgba(124,58,237,0.22);

}


.icon {

    width:
        58px;

    height:
        58px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        17px;

    font-size:
        27px;

    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.14),
            rgba(37,99,235,0.10)
        );

}


.card-title {

    color:
        __TEXT__;

    font-size:
        18px;

    font-weight:
        800;

    margin-top:
        17px;

}


.card-text {

    color:
        __MUTED__;

    font-size:
        13px;

    line-height:
        1.75;

    margin-top:
        8px;

}


/* =========================================================
   FORM
========================================================= */

.form-header {

    background:
        __CARD__;

    border:
        1px solid __BORDER__;

    border-radius:
        25px;

    padding:
        30px;

    margin-top:
        25px;

    box-shadow:
        0 20px 55px
        __SHADOW__;

}


.form-title {

    color:
        __TEXT__;

    font-size:
        25px;

    font-weight:
        850;

}


.form-subtitle {

    color:
        __MUTED__;

    font-size:
        13px;

}


.form-section-title {

    color:
        __PRIMARY__;

    font-size:
        11px;

    font-weight:
        850;

    letter-spacing:
        1.5px;

    margin-top:
        28px;

    margin-bottom:
        10px;

}


/* =========================================================
   INPUT LABELS
========================================================= */

[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label,
[data-testid="stNumberInput"] label p,
[data-testid="stSelectbox"] label p {

    color:
        __TEXT__ !important;

    -webkit-text-fill-color:
        __TEXT__ !important;

    font-weight:
        650 !important;

}


/* =========================================================
   NUMBER INPUT
========================================================= */

[data-testid="stNumberInput"] input {

    color:
        __INPUT_TEXT__ !important;

    -webkit-text-fill-color:
        __INPUT_TEXT__ !important;

    caret-color:
        __PRIMARY__ !important;

    font-weight:
        700 !important;

    opacity:
        1 !important;

    background:
        transparent !important;

}


[data-testid="stNumberInput"]
div[data-baseweb="input"] > div {

    background:
        __CARD__ !important;

    border:
        1px solid __BORDER__ !important;

    border-radius:
        12px !important;

}


[data-testid="stNumberInput"]
button {

    color:
        __INPUT_TEXT__ !important;

    background:
        __CARD__ !important;

    border-color:
        __BORDER__ !important;

}


[data-testid="stNumberInput"]
button svg {

    fill:
        __INPUT_TEXT__ !important;

}


/* =========================================================
   SELECTBOX
========================================================= */

[data-testid="stSelectbox"]
[data-baseweb="select"] {

    background:
        __CARD__ !important;

    color:
        __INPUT_TEXT__ !important;

}


[data-testid="stSelectbox"]
[data-baseweb="select"] > div {

    background:
        __CARD__ !important;

    border:
        1px solid __BORDER__ !important;

    border-radius:
        12px !important;

}


[data-testid="stSelectbox"]
[data-baseweb="select"] span,
[data-testid="stSelectbox"]
[data-baseweb="select"] p {

    color:
        __INPUT_TEXT__ !important;

    -webkit-text-fill-color:
        __INPUT_TEXT__ !important;

}


[data-testid="stSelectbox"]
[data-baseweb="select"] svg {

    fill:
        __INPUT_TEXT__ !important;

}


/* =========================================================
   DROPDOWN
========================================================= */

div[role="listbox"] {

    background:
        __CARD__ !important;

}


div[role="option"] {

    color:
        __INPUT_TEXT__ !important;

    background:
        __CARD__ !important;

}


div[role="option"]:hover {

    color:
        white !important;

    background:
        #312E81 !important;

}


/* =========================================================
   METRICS
========================================================= */

.metric {

    min-height:
        145px;

    padding:
        23px;

    border-radius:
        19px;

    background:
        linear-gradient(
            145deg,
            rgba(124,58,237,0.11),
            rgba(99,102,241,0.05)
        );

    border:
        1px solid
        rgba(124,58,237,0.15);

    transition:
        0.25s ease;

}


.metric:hover {

    transform:
        translateY(-7px);

    border-color:
        __PRIMARY__;

    box-shadow:
        0 18px 35px
        __SHADOW__;

}


.metric-name {

    color:
        __MUTED__;

    font-size:
        11px;

    font-weight:
        750;

}


.metric-value {

    color:
        __PRIMARY__;

    font-size:
        30px;

    font-weight:
        900;

    margin-top:
        5px;

}


/* =========================================================
   ABOUT
========================================================= */

.about {

    background:
        __CARD__;

    border:
        1px solid __BORDER__;

    border-radius:
        23px;

    padding:
        30px;

    min-height:
        300px;

    box-shadow:
        0 15px 45px
        __SHADOW__;

}


.about-title {

    color:
        __TEXT__;

    font-size:
        21px;

    font-weight:
        850;

    margin-bottom:
        15px;

}


.about-text {

    color:
        __MUTED__;

    font-size:
        14px;

    line-height:
        1.9;

}


/* =========================================================
   RESULT
========================================================= */

.result {

    margin-top:
        25px;

    padding:
        30px;

    text-align:
        center;

    border-radius:
        23px;

    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.10),
            rgba(37,99,235,0.08)
        );

    border:
        1px solid
        rgba(124,58,237,0.20);

}


.result-label {

    color:
        __PRIMARY__;

    font-size:
        11px;

    font-weight:
        850;

    letter-spacing:
        1.5px;

}


.result-text {

    color:
        __TEXT__;

    font-size:
        25px;

    font-weight:
        850;

}


/* =========================================================
   RECORDS
========================================================= */

.records-box {

    background:
        __CARD__;

    border:
        1px solid __BORDER__;

    border-radius:
        25px;

    padding:
        25px;

    margin-top:
        25px;

    box-shadow:
        0 18px 50px
        __SHADOW__;

}


.record-high {

    color:
        #EF4444;

    font-weight:
        800;

}


.record-low {

    color:
        #10B981;

    font-weight:
        800;

}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align:
        center;

    color:
        __MUTED__;

    font-size:
        12px;

    margin-top:
        70px;

    padding-top:
        25px;

    border-top:
        1px solid __BORDER__;

}

</style>

"""


# =========================================================
# APPLY CSS
# =========================================================

css = css.replace(
    "__BG__",
    BG
)

css = css.replace(
    "__CARD__",
    CARD
)

css = css.replace(
    "__TEXT__",
    TEXT
)

css = css.replace(
    "__MUTED__",
    MUTED
)

css = css.replace(
    "__INPUT_TEXT__",
    INPUT_TEXT
)

css = css.replace(
    "__PRIMARY__",
    PRIMARY
)

css = css.replace(
    "__BORDER__",
    BORDER
)

css = css.replace(
    "__SHADOW__",
    SHADOW
)


st.html(css)


# =========================================================
# TOP LINE
# =========================================================

st.html(
    """
    <div class="top-line"></div>
    """
)


# =========================================================
# NAVBAR
# =========================================================

n1, n2, n3, n4, n5, n6, n7 = st.columns(
    [2.4, 0.9, 1.15, 0.9, 0.9, 0.8, 0.55]
)


with n1:

    st.html(
        """
        <div class="brand">

            <span class="brand-heart">
                ♥
            </span>

            Cardio
            <span class="brand-ai">
                RISK
            </span>

        </div>
        """
    )


with n2:

    if st.button(
        "Home",
        use_container_width=True
    ):

        st.session_state.page = "Home"

        st.rerun()


with n3:

    if st.button(
        "Assessment",
        use_container_width=True
    ):

        st.session_state.page = "Assessment"

        st.rerun()


with n4:

    if st.button(
        "Features",
        use_container_width=True
    ):

        st.session_state.page = "Features"

        st.rerun()


with n5:

    if st.button(
        "Records",
        use_container_width=True
    ):

        st.session_state.page = "Records"

        st.rerun()


with n6:

    if st.button(
        "About",
        use_container_width=True
    ):

        st.session_state.page = "About"

        st.rerun()


with n7:

    if st.button(
        "☀️"
        if st.session_state.dark
        else "🌙",
        use_container_width=True
    ):

        st.session_state.dark = not st.session_state.dark

        st.rerun()


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "Home":

    left, right = st.columns(
        [1.25, 0.75],
        gap="medium"
    )


    with left:

        st.html(
            """
            <div class="hero">

                <div class="hero-label">
                    ✦ AI POWERED HEART HEALTH
                </div>

                <div class="hero-title">
                    Understand your heart.<br>

                    <span>
                        Predict with intelligence.
                    </span>

                </div>

                <div class="hero-text">

                    CardioAI combines machine learning
                    and healthcare data to analyze
                    cardiovascular parameters and
                    generate an intelligent prediction
                    through a simple interface.

                </div>

            </div>
            """
        )


    with right:

        st.html(
            """
            <div class="heart-box">

                <img

                    class="heart-image"

                    src="https://cdn-icons-png.flaticon.com/512/2966/2966486.png"

                    alt="Heart"

                >

            </div>
            """
        )


    st.html(
        """
        <div class="section-label">
            WHY CARDIOAI
        </div>

        <div class="section-title">
            Designed for smarter assessment
        </div>

        <div class="section-text">

            A complete machine-learning project
            with preprocessing, classification,
            prediction and patient records.

        </div>
        """
    )


    st.write("")


    c1, c2, c3 = st.columns(3)


    cards = [

        (
            "🧠",
            "Intelligent Prediction",
            "Uses a classification model to analyze "
            "patient parameters and generate a prediction."
        ),

        (
            "📊",
            "Health Data Analysis",
            "Analyzes age, blood pressure, cholesterol, "
            "glucose, weight and lifestyle parameters."
        ),

        (
            "🗂️",
            "Prediction Records",
            "Automatically stores completed assessments "
            "so previous predictions can be reviewed."
        )

    ]


    for column, item in zip(
        [c1, c2, c3],
        cards
    ):

        icon, title, text = item


        with column:

            st.html(
                f"""
                <div class="card">

                    <div class="icon">
                        {icon}
                    </div>

                    <div class="card-title">
                        {title}
                    </div>

                    <div class="card-text">
                        {text}
                    </div>

                </div>
                """
            )


    # MODEL STATISTICS

    st.html(
        """
        <div class="section-label">
            MODEL INSIGHTS
        </div>

        <div class="section-title">
            Model Statistics
        </div>

        <div class="section-text">

            Key evaluation metrics used to
            understand model performance.

        </div>
        """
    )


    st.write("")


    s1, s2, s3, s4 = st.columns(4)


    metrics = [

        ("🎯", "ACCURACY", ACCURACY),

        ("📈", "ROC-AUC SCORE", ROC_AUC),

        ("🔍", "PRECISION", PRECISION),

        ("🔄", "RECALL", RECALL)

    ]


    for column, item in zip(
        [s1, s2, s3, s4],
        metrics
    ):

        icon, name, value = item


        with column:

            st.html(
                f"""
                <div class="metric">

                    <div>
                        {icon}
                    </div>

                    <div class="metric-name">
                        {name}
                    </div>

                    <div class="metric-value">
                        {value}
                    </div>

                </div>
                """
            )


# =========================================================
# ASSESSMENT
# =========================================================

elif st.session_state.page == "Assessment":

    st.html(
        """
        <div class="section-label">
            HEART ASSESSMENT
        </div>

        <div class="section-title">
            Patient Health Profile
        </div>

        <div class="section-text">

            Enter the patient's health information
            below for heart disease assessment.

        </div>
        """
    )


    # IMAGE

    st.html(
        """
        <div style="
            margin-top:25px;
            border-radius:24px;
            overflow:hidden;
            border:1px solid rgba(124,58,237,0.18);
            box-shadow:0 15px 45px rgba(124,58,237,0.12);
        ">

            <img

                src="https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=1600&q=85"

                alt="Heart health"

                style="
                    width:100%;
                    height:220px;
                    object-fit:cover;
                    display:block;
                "

            >

        </div>
        """
    )


    st.html(
        """
        <div class="form-header">

            <div class="form-title">
                🫀 Health Information
            </div>

            <div class="form-subtitle">

                Complete the patient information
                before running the prediction.

            </div>

        </div>
        """
    )


    # BASIC INFORMATION

    st.html(
        """
        <div class="form-section-title">
            BASIC INFORMATION
        </div>
        """
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=50
        )


    with c2:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )


    with c3:

        height = st.number_input(
            "Height (cm)",
            min_value=50,
            max_value=250,
            value=165
        )


    # BODY

    st.html(
        """
        <div class="form-section-title">
            BODY & BLOOD PRESSURE
        </div>
        """
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=65.0
        )


    with c2:

        ap_hi = st.number_input(
            "Systolic BP",
            min_value=50,
            max_value=250,
            value=120
        )


    with c3:

        ap_lo = st.number_input(
            "Diastolic BP",
            min_value=30,
            max_value=150,
            value=80
        )


    # MEDICAL

    st.html(
        """
        <div class="form-section-title">
            MEDICAL PARAMETERS
        </div>
        """
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        cholesterol = st.selectbox(
            "Cholesterol",
            [1, 2, 3]
        )


    with c2:

        gluc = st.selectbox(
            "Glucose",
            [1, 2, 3]
        )


    with c3:

        smoke = st.selectbox(
            "Smoking",
            [0, 1]
        )


    # LIFESTYLE

    st.html(
        """
        <div class="form-section-title">
            LIFESTYLE
        </div>
        """
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        alco = st.selectbox(
            "Alcohol",
            [0, 1]
        )


    with c2:

        active = st.selectbox(
            "Physical Activity",
            [0, 1]
        )


    st.write("")


    # =====================================================
    # PREDICT
    # =====================================================

    if st.button(
        "❤️  Analyze Heart Health",
        use_container_width=True
    ):

        # Gender conversion

        if gender == "Female":

            gender_value = 1

        else:

            gender_value = 2


        # Data

        data = {

            "age":
                age,

            "gender":
                gender_value,

            "height":
                height,

            "weight":
                weight,

            "ap_hi":
                ap_hi,

            "ap_lo":
                ap_lo,

            "cholesterol":
                cholesterol,

            "gluc":
                gluc,

            "smoke":
                smoke,

            "alco":
                alco,

            "active":
                active

        }


        try:

            response = requests.post(

                f"{BACKEND_URL}/predict",

                json=data,

                timeout=10

            )


            result = response.json()


            if response.status_code == 200:

                prediction = result[
                    "prediction"
                ]

                risk = result[
                    "result"
                ]

                probability = result[
                    "probability"
                ]


                # HIGH RISK

                if prediction == 1:

                    st.html(
                        f"""
                        <div class="result"
                            style="
                            border:1px solid #F87171;
                            background:rgba(239,68,68,0.10);
                            ">

                            <div
                                class="result-label"
                                style="color:#F87171;"
                            >

                                ASSESSMENT RESULT

                            </div>

                            <div
                                class="result-text"
                                style="color:#FF6B6B;"
                            >

                                ❤️ {risk}

                            </div>

                            <div style="
                                margin-top:12px;
                                color:#C9C1DA;
                                font-size:15px;
                            ">

                                Estimated Risk:

                                <b style="color:#FF8A8A;">

                                    {probability}%

                                </b>

                            </div>

                            <div style="
                                margin-top:10px;
                                color:#C9C1DA;
                                font-size:12px;
                            ">

                                ✓ Record automatically saved

                            </div>

                        </div>
                        """
                    )


                # LOW RISK

                else:

                    st.html(
                        f"""
                        <div class="result"
                            style="
                            border:1px solid #34D399;
                            background:rgba(16,185,129,0.10);
                            ">

                            <div
                                class="result-label"
                                style="color:#34D399;"
                            >

                                ASSESSMENT RESULT

                            </div>

                            <div
                                class="result-text"
                                style="color:#34D399;"
                            >

                                💚 {risk}

                            </div>

                            <div style="
                                margin-top:12px;
                                color:#C9C1DA;
                                font-size:15px;
                            ">

                                Estimated Risk:

                                <b style="color:#6EE7B7;">

                                    {probability}%

                                </b>

                            </div>

                            <div style="
                                margin-top:10px;
                                color:#C9C1DA;
                                font-size:12px;
                            ">

                                ✓ Record automatically saved

                            </div>

                        </div>
                        """
                    )


            else:

                st.error(

                    "❌ Backend Error: "
                    + result.get(
                        "error",
                        "Prediction failed"
                    )

                )


        except requests.exceptions.ConnectionError:

            st.error(

                "❌ Backend is not connected. "
                "First run: python backend.py"

            )


        except requests.exceptions.Timeout:

            st.error(

                "⏳ Backend request timed out."

            )


        except Exception as e:

            st.error(

                f"❌ Error: {str(e)}"

            )


# =========================================================
# FEATURES
# =========================================================

elif st.session_state.page == "Features":

    st.html(
        """
        <div class="section-label">
            FEATURES
        </div>

        <div class="section-title">
            Everything inside CardioAI
        </div>

        <div class="section-text">

            Explore the major components of the
            heart disease prediction application.

        </div>
        """
    )


    st.write("")


    features = [

        (
            "🧠",
            "Machine Learning",
            "A classification model learns patterns "
            "from the prepared heart disease dataset."
        ),

        (
            "🧹",
            "Data Preprocessing",
            "Missing values, outliers, categorical "
            "values and numerical features can be processed."
        ),

        (
            "📈",
            "Model Evaluation",
            "Accuracy, ROC-AUC, precision and recall "
            "can be used to evaluate the model."
        ),

        (
            "⚡",
            "Fast Assessment",
            "Patient information can be entered through "
            "an organized interactive form."
        ),

        (
            "🗂️",
            "Prediction Records",
            "Every completed prediction is automatically "
            "stored for later review."
        ),

        (
            "🌙",
            "Light & Dark Mode",
            "A modern theme system provides a comfortable "
            "interface in both light and dark modes."
        )

    ]


    for i in range(
        0,
        len(features),
        2
    ):

        c1, c2 = st.columns(2)


        for column, item in zip(
            [c1, c2],
            features[i:i + 2]
        ):

            icon, title, text = item


            with column:

                st.html(
                    f"""
                    <div class="card">

                        <div class="icon">
                            {icon}
                        </div>

                        <div class="card-title">
                            {title}
                        </div>

                        <div class="card-text">
                            {text}
                        </div>

                    </div>
                    """
                )


        st.write("")


# =========================================================
# RECORDS
# =========================================================

elif st.session_state.page == "Records":

    st.html(
        """
        <div class="section-label">
            PATIENT RECORDS
        </div>

        <div class="section-title">
            Prediction History
        </div>

        <div class="section-text">

            View all heart disease assessments
            completed through CardioAI.

        </div>
        """
    )


    st.write("")


    try:

        response = requests.get(

            f"{BACKEND_URL}/records",

            timeout=10

        )


        result = response.json()


        if response.status_code == 200:

            records = result.get(
                "records",
                []
            )


            # -------------------------------------------------
            # NO RECORDS
            # -------------------------------------------------

            if len(records) == 0:

                st.html(
                    """
                    <div class="records-box">

                        <div class="card-title">
                            🗂️ No Records Yet
                        </div>

                        <div class="card-text">

                            Complete an assessment first.
                            Your prediction will automatically
                            appear here.

                        </div>

                    </div>
                    """
                )


            else:

                # -------------------------------------------------
                # SUMMARY
                # -------------------------------------------------

                total = len(records)

                high_count = sum(

                    1

                    for r in records

                    if "High Risk"
                    in str(
                        r.get(
                            "Prediction",
                            ""
                        )
                    )

                )

                low_count = total - high_count


                m1, m2, m3 = st.columns(3)


                with m1:

                    st.html(
                        f"""
                        <div class="metric">

                            <div>
                                📋
                            </div>

                            <div class="metric-name">
                                TOTAL ASSESSMENTS
                            </div>

                            <div class="metric-value">
                                {total}
                            </div>

                        </div>
                        """
                    )


                with m2:

                    st.html(
                        f"""
                        <div class="metric">

                            <div>
                                ❤️
                            </div>

                            <div class="metric-name">
                                HIGH RISK
                            </div>

                            <div
                                class="metric-value"
                                style="color:#EF4444;"
                            >
                                {high_count}
                            </div>

                        </div>
                        """
                    )


                with m3:

                    st.html(
                        f"""
                        <div class="metric">

                            <div>
                                💚
                            </div>

                            <div class="metric-name">
                                LOW RISK
                            </div>

                            <div
                                class="metric-value"
                                style="color:#10B981;"
                            >
                                {low_count}
                            </div>

                        </div>
                        """
                    )


                st.write("")


                # -------------------------------------------------
                # TABLE
                # -------------------------------------------------

                df = pd.DataFrame(
                    records
                )


                display_columns = [

                    "Date & Time",

                    "Age",

                    "Gender",

                    "Height",

                    "Weight",

                    "Systolic BP",

                    "Diastolic BP",

                    "Cholesterol",

                    "Glucose",

                    "Smoking",

                    "Alcohol",

                    "Physical Activity",

                    "Prediction",

                    "Risk Probability"

                ]


                existing_columns = [

                    col

                    for col in display_columns

                    if col in df.columns

                ]


                df = df[
                    existing_columns
                ]


                st.html(
                    """
                    <div class="records-box">

                        <div class="card-title">
                            📋 Assessment Records
                        </div>

                        <div class="card-text">

                            Every completed prediction
                            is automatically stored here.

                        </div>

                    </div>
                    """
                )


                st.dataframe(

                    df,

                    use_container_width=True,

                    hide_index=True

                )


                # -------------------------------------------------
                # DELETE
                # -------------------------------------------------

                st.write("")


                if st.button(

                    "🗑️ Clear All Records",

                    use_container_width=True

                ):

                    delete_response = requests.delete(

                        f"{BACKEND_URL}/records",

                        timeout=10

                    )


                    if delete_response.status_code == 200:

                        st.success(
                            "✅ All records deleted successfully."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "❌ Could not delete records."
                        )


        else:

            st.error(
                "❌ Could not load records."
            )


    except requests.exceptions.ConnectionError:

        st.error(

            "❌ Backend is not connected. "
            "Run python backend.py first."

        )


    except Exception as e:

        st.error(

            f"❌ Error: {str(e)}"

        )


# =========================================================
# ABOUT
# =========================================================

elif st.session_state.page == "About":

    st.html(
        """
        <div class="section-label">
            ABOUT CARDIOAI
        </div>

        <div class="section-title">
            About the project
        </div>

        <div class="section-text">

            A machine-learning based academic
            project for heart disease prediction.

        </div>
        """
    )


    st.write("")


    c1, c2 = st.columns(
        [1.35, 0.65]
    )


    with c1:

        st.html(
            """
            <div class="about">

                <div class="about-title">
                    🫀 What is CardioAI?
                </div>

                <div class="about-text">

                    CardioAI is a machine-learning
                    based heart disease prediction
                    project.

                    <br><br>

                    The application uses important
                    patient health parameters including
                    age, gender, height, weight,
                    blood pressure, cholesterol,
                    glucose and lifestyle information.

                    <br><br>

                    These values are prepared according
                    to the trained machine-learning model
                    and used to generate a prediction.

                    <br><br>

                    The application also maintains
                    prediction records so that previous
                    assessments can be reviewed easily.

                </div>

            </div>
            """
        )


    with c2:

        st.html(
            """
            <div class="about">

                <div class="about-title">
                    ⚙️ Technology Stack
                </div>

                <div class="card-text">

                    <b>Python</b><br>
                    Data processing and ML development.

                    <br><br>

                    <b>Pandas & NumPy</b><br>
                    Dataset and numerical operations.

                    <br><br>

                    <b>Scikit-learn</b><br>
                    Machine-learning model training.

                    <br><br>

                    <b>Streamlit</b><br>
                    Interactive frontend.

                    <br><br>

                    <b>Flask</b><br>
                    Backend prediction API.

                </div>

            </div>
            """
        )


    st.html(
        """
        <div class="section-label">
            PERFORMANCE
        </div>

        <div class="section-title">
            Model Performance Metrics
        </div>
        """
    )


    st.write("")


    p1, p2, p3, p4 = st.columns(4)


    performance = [

        ("🎯", "Accuracy", ACCURACY),

        ("📈", "ROC-AUC", ROC_AUC),

        ("🔎", "Precision", PRECISION),

        ("🔄", "Recall", RECALL)

    ]


    for column, item in zip(
        [p1, p2, p3, p4],
        performance
    ):

        icon, name, value = item


        with column:

            st.html(
                f"""
                <div class="metric">

                    <div>
                        {icon}
                    </div>

                    <div class="metric-name">
                        {name}
                    </div>

                    <div class="metric-value">
                        {value}
                    </div>

                </div>
                """
            )


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="footer">

        ❤️ <b>CardioAI</b>

        <br>

        Machine Learning Based
        Heart Disease Prediction

        <br>

        Academic Project • Python • Streamlit • Flask

    </div>
    """
)