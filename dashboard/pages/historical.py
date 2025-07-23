import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Green Score History", page_icon="📈", layout="wide")

history_path = "dashboard/user_history.csv"

st.title("📈 Your Green Credit Score History")
try:
    history_df = pd.read_csv(history_path)
    st.success(f"Loaded {len(history_df)} records!")
    st.dataframe(history_df, use_container_width=True)
    st.markdown("### Timeline of Green Credit Scores")
    fig = px.line(
        history_df, x="timestamp", y="green_score",
        markers=True, title="Green Credit Score Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.download_button("⬇️ Download History CSV", history_df.to_csv(index=False).encode('utf-8'), "green_credit_score_history.csv", mime="text/csv")
except FileNotFoundError:
    st.warning("No history found yet. Generate some scores on the dashboard page first!")

st.markdown("---")
st.caption("Developed by ALT F4. Feedback welcome!")