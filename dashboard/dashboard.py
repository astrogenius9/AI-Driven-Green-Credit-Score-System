import streamlit as st
import requests
import random
import pandas as pd
import plotly.graph_objects as go
from streamlit_extras.metric_cards import style_metric_cards
from datetime import datetime

st.set_page_config(
    page_title="Green Credit Score Dashboard",
    page_icon="🌱",
    layout="wide"
)

def random_sample():
    return {
        "energy_usage": round(random.uniform(50, 200), 2),
        "renewable_pct": round(random.uniform(0, 100), 2),
        "recycling_pct": round(random.uniform(0, 100), 2),
        "green_investments": round(random.uniform(1000, 500000), 2)
    }

def calculate_contributions(input_data):
    # Dummy weights - replace with your actual model logic if needed
    energy_contrib = 0.2 * (200 - input_data['energy_usage'])  # Lower is better
    renewable_contrib = 0.3 * input_data['renewable_pct']
    recycling_contrib = 0.3 * input_data['recycling_pct']
    investments_contrib = 0.00005 * input_data['green_investments']
    return {
        "Energy Usage": energy_contrib,
        "Renewable Energy": renewable_contrib,
        "Recycling Rate": recycling_contrib,
        "Green Investments": investments_contrib
    }

def save_to_history(input_data, green_score):
    record = input_data.copy()
    record['green_score'] = green_score
    record['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history_path = "dashboard/user_history.csv"
    try:
        df = pd.read_csv(history_path)
        df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([record])
    df.to_csv(history_path, index=False)

with st.sidebar:
    st.title("🌱 Green Score Inputs")
    if st.button("🎲 Random Sample Data"):
        data = random_sample()
    else:
        data = {}
    energy_usage = st.number_input(
        "🔌 Energy Usage (MWh/year)", min_value=0.0, max_value=1000.0,
        value=data.get('energy_usage', 100.0),
        help="Lower values are better for the environment."
    )
    renewable_pct = st.slider(
        "☀️ Renewable Energy Percentage (%)", 0, 100, int(data.get('renewable_pct', 40)),
        help="Higher percentages indicate cleaner energy sources."
    )
    recycling_pct = st.slider(
        "♻️ Recycling Rate (%)", 0, 100, int(data.get('recycling_pct', 30)),
        help="Higher percentages mean more waste recycling."
    )
    green_investments = st.number_input(
        "💰 Green Investments ($)", min_value=0.0, max_value=1000000.0,
        value=data.get('green_investments', 100000.0),
        help="Annual spending on green/sustainable projects."
    )

    # Button to switch to historical page (Streamlit multipage feature)
    if st.button("📈 View Score History"):
        st.switch_page("pages/historical.py")

input_data = {
    "energy_usage": energy_usage,
    "renewable_pct": renewable_pct,
    "recycling_pct": recycling_pct,
    "green_investments": green_investments
}

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("### ℹ️ How the Score Works")
    st.info(
        """
        **Green Credit Score** is calculated based on:
        - Lower energy usage (good)
        - Higher renewable energy use (good)
        - Higher recycling rate (good)
        - More green investments (good)
        """
    )
    st.markdown("#### Input Summary")
    # --- Changed to table instead of array/dict ---
    input_df = pd.DataFrame(list(input_data.items()), columns=["Input", "Value"])
    st.table(input_df)
    st.markdown("---")
    st.markdown("#### About This App")
    st.caption(
        "This AI-powered tool predicts a company's green credit score using your input. "
        "Powered by FastAPI, scikit-learn, and Streamlit."
    )

with col2:
    st.markdown("## 🌍 AI-Driven Green Credit Score Dashboard")
    predict_btn = st.button("🚦 Predict Green Credit Score", use_container_width=True)
    if predict_btn:
        with st.spinner("Predicting..."):
            try:
                response = requests.post("http://localhost:8000/predict", json=input_data)
                if response.status_code == 200:
                    green_score = response.json()["green_score"]
                    st.success(f"🌿 Predicted Green Credit Score: **{green_score}**")
                    save_to_history(input_data, green_score)
                    # Gauge visualization with dynamic gradient color
                    st.markdown("#### Green Score Gauge")

                    percent_width = min(max(green_score, 0), 100)
                    gradient_css = (
                        "linear-gradient(90deg, "
                        "#c0392b 0%, "
                        "#e67e22 50%, "
                        "#27ae60 100%)"
                    )
                    if green_score < 40:
                        emoji = "🛑"
                        font_color = "white"
                    elif green_score < 70:
                        emoji = "⚠️"
                        font_color = "white"
                    else:
                        emoji = "✅"
                        font_color = "white"

                    st.markdown(
                        f"""
                        <div style='width: 100%; background: #eee; border-radius: 10px;'>
                            <div style='
                                width: {percent_width}%;
                                background: {gradient_css};
                                padding: 12px 0;
                                border-radius: 10px;
                                text-align: center;
                                color: {font_color};
                                font-weight: bold;
                                font-size: 1.1em;
                                transition: width 0.5s;'>
                                {emoji} {green_score}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error(f"API Error: {response.text}")
            except Exception as e:
                st.error(f"Error connecting to AI backend: {e}")
    else:
        st.info("Enter company data and click 'Predict Green Credit Score'.")

    # --------- Visual Impact Simulator (Radar Chart) ---------
    st.markdown("#### 🕸️ Visual Impact Simulator: Score Contribution by Factor (Radar Chart)")
    contributions = calculate_contributions(input_data)
    radar_factors = list(contributions.keys())
    radar_values = list(contributions.values())

    # Repeat the first value at the end to close the radar chart, but
    # for better label visibility, add an empty string between last and first
    radar_factors_mod = radar_factors + [""] + [radar_factors[0]]
    radar_values_mod = radar_values + [None] + [radar_values[0]]

    fig = go.Figure(
        data=[
            go.Scatterpolar(
                r=radar_values_mod,
                theta=radar_factors_mod,
                fill="toself",
                marker=dict(color="#27ae60"),
                name="Score Contribution",
                hoverinfo="all"
            )
        ]
    )
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(40, max([v for v in radar_values if v is not None]))],
                showticklabels=True,
                tickfont=dict(color="#fff")
            ),
            angularaxis=dict(
                tickfont=dict(size=13, color="#fff"),
                rotation=90,
                direction="clockwise"
            ),
            bgcolor="#222"
        ),
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10),
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Developed by ALT F4. Feedback welcome!")

try:
    style_metric_cards(background_color="#272822", border_left_color="#00b894", border_color="#636e72")
except Exception:
    pass
