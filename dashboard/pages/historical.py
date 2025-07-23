import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Green Score History", page_icon="📈", layout="wide")

history_path = "dashboard/user_history.csv"

def generate_recommendation(row):
    """Generate a personalized recommendation based on values in a row."""
    recs = []
    if row["energy_usage"] > 120:
        recs.append("Reduce energy usage for a better score.")
    if row["renewable_pct"] < 50:
        recs.append("Increase renewable energy percentage above 50%.")
    if row["recycling_pct"] < 40:
        recs.append("Improve recycling rate for greater sustainability.")
    if row["green_investments"] < 100000:
        recs.append("Invest more in green projects.")
    if not recs:
        recs.append("Excellent performance! Keep it up.")
    return " | ".join(recs)

st.title("📈 Your Green Credit Score History")
try:
    history_df = pd.read_csv(history_path)
    st.success(f"Loaded {len(history_df)} records!")

    # Add recommendations column for CSV/download and for personalized feedback
    history_df_with_recs = history_df.copy()
    history_df_with_recs["recommendations"] = history_df_with_recs.apply(generate_recommendation, axis=1)

    # Display table WITHOUT recommendations column
    st.dataframe(history_df, use_container_width=True)

    st.markdown("### Timeline of Green Credit Scores")
    fig = px.line(
        history_df, x="timestamp", y="green_score",
        markers=True, title="Green Credit Score Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.download_button(
        "⬇️ Download History CSV",
        history_df_with_recs.to_csv(index=False).encode('utf-8'),
        "green_credit_score_history.csv",
        mime="text/csv"
    )

    st.markdown("### Personalized Recommendations for Each Entry")
    for idx, row in history_df_with_recs.iterrows():
        st.markdown(f"**{row['timestamp']}** — {row['recommendations']}")

except FileNotFoundError:
    st.warning("No history found yet. Generate some scores on the dashboard page first!")

st.markdown("---")
st.caption("Developed by ALT F4. Feedback welcome!")
