import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Solar Power",
    page_icon="☀️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* ==========================
   GLOBAL STYLING
========================== */

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #0f172a
    );
    color:white !important;
}

html, body, [class*="css"]{
    color:white !important;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* ==========================
   TITLES
========================== */

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #FFD700,
        #FFA500,
        #FF6B00
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.sub-title{
    text-align:center;
    color:#e5e7eb !important;
    font-size:20px;
}

/* ==========================
   GLASS CARD
========================== */

.glass{
    background: rgba(17,24,39,0.88);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius:20px;
    padding:25px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 8px 32px rgba(0,0,0,0.3);
}

/* ==========================
   INPUT LABELS
========================== */

label{
    color:white !important;
    font-weight:600 !important;
}

/* Number Inputs */

.stNumberInput input{
    background: rgba(255,255,255,0.08) !important;
    color:white !important;
    border-radius:10px !important;
    border:1px solid rgba(255,255,255,0.2) !important;
}

/* Placeholder */

input::placeholder{
    color:#d1d5db !important;
}

/* ==========================
   BUTTON
========================== */

.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:linear-gradient(
        90deg,
        #f59e0b,
        #ea580c
    );
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0 0 20px rgba(249,115,22,0.5);
}

/* ==========================
   METRICS
========================== */

[data-testid="stMetricValue"]{
    color:white !important;
    font-size:28px !important;
    font-weight:700 !important;
}

[data-testid="stMetricLabel"]{
    color:#e5e7eb !important;
    font-size:16px !important;
}

/* ==========================
   SIDEBAR
========================== */

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* ==========================
   INFO BOXES
========================== */

[data-testid="stInfo"]{
    background:rgba(17,24,39,0.9);
    color:white !important;
    border-radius:12px;
}

/* ==========================
   HEADINGS
========================== */

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

/* ==========================
   RESULT CARD
========================== */

.result-card{
    background:linear-gradient(
        135deg,
        #22c55e,
        #16a34a
    );
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0 0 25px rgba(34,197,94,0.5);
}

/* ==========================
   EXPANDERS
========================== */

.streamlit-expanderHeader{
    color:white !important;
}

/* ==========================
   TABLES
========================== */

table{
    color:white !important;
}

/* ==========================
   MARKDOWN TEXT
========================== */

p, span, div{
    color:white;
}

</style>


""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("solar_power_model.pkl")

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/869/869869.png",
        width=120
    )

    st.title("☀️ Solar")

    st.success("Machine Learning Dashboard")

    st.metric("Model Status", "Active")
    st.metric("Input Features", "9")
    st.metric("Prediction Type", "Regression")

    st.markdown("---")
    st.write("### Features")
    st.write("✅ Real-time Prediction")
    st.write("✅ Weather Analytics")
    st.write("✅ AI Forecasting")
    st.write("✅ Renewable Energy")

# ---------------- HEADER ---------------- #

st.markdown(
    "<h1 class='main-title'>SOLAR POWER FORECASTING</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>AI-Powered Solar Energy Generation Prediction System</p>",
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200",
    use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FEATURE CARDS ---------------- #

c1, c2, c3 = st.columns(3)

with c1:
    st.info("⚡ Real-Time Power Prediction")

with c2:
    st.info("🤖 Machine Learning Powered")

with c3:
    st.info("🌍 Renewable Energy Analytics")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT FORM ---------------- #

st.markdown("<div class='glass'>", unsafe_allow_html=True)

st.subheader("🌤 Weather Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    distance_to_solar_noon = st.number_input(
        "☀ Distance to Solar Noon",
        value=0.0
    )

    temperature = st.number_input(
        "🌡 Temperature",
        value=0.0
    )

    wind_direction = st.number_input(
        "🧭 Wind Direction",
        value=0.0
    )

with col2:
    wind_speed = st.number_input(
        "💨 Wind Speed",
        value=0.0
    )

    sky_cover = st.number_input(
        "☁ Sky Cover",
        value=0.0
    )

    visibility = st.number_input(
        "👁 Visibility",
        value=0.0
    )

with col3:
    humidity = st.number_input(
        "💧 Humidity",
        value=0.0
    )

    avg_wind_speed = st.number_input(
        "🌪 Avg Wind Speed",
        value=0.0
    )

    avg_pressure = st.number_input(
        "📊 Avg Pressure",
        value=0.0
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIVE WEATHER METRICS ---------------- #

st.markdown("<br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

m1.metric("Temperature", f"{temperature}")
m2.metric("Humidity", f"{humidity}")
m3.metric("Wind Speed", f"{wind_speed}")
m4.metric("Visibility", f"{visibility}")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- PREDICTION ---------------- #

if st.button("🔮 Predict Power Generation"):

    features = np.array([[
        distance_to_solar_noon,
        temperature,
        wind_direction,
        wind_speed,
        sky_cover,
        visibility,
        humidity,
        avg_wind_speed,
        avg_pressure
    ]])

    prediction = model.predict(features)

    st.markdown(
        f"""
        <div class='result-card'>
        <h2>⚡ Predicted Solar Power Generation</h2>
        <h1>{prediction[0]:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Gauge Chart

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=float(prediction[0]),
        title={"text":"Predicted Output"},
        gauge={
            "axis":{"range":[0,1000]},
            "bar":{"color":"orange"},
            "steps":[
                {"range":[0,300],"color":"lightgray"},
                {"range":[300,700],"color":"gray"},
                {"range":[700,1000],"color":"darkgray"}
            ]
        }
    ))

    fig.update_layout(
        height=400,
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color":"white"}
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- FOOTER ---------------- #

st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown(
    """
    <center>
    <h4>☀️ Solar AI Forecasting Platform</h4>
    <p>Powered by Machine Learning | Renewable Energy Analytics</p>
    </center>
    """,
    unsafe_allow_html=True
)

