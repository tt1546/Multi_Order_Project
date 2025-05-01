import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Annual Statistics")

# Load daily multi-order statistics data
annual_stats = pd.read_csv("data/annual_stats.csv", parse_dates=["order_date"])
annual_stats.set_index("order_date", inplace=True)

# Plot multi-order ratio over time with moving average
fig = go.Figure()
# Original daily multi-order ratio line
fig.add_trace(go.Scatter(
    x = annual_stats.index, 
    y = annual_stats["multiorder_ratio"], 
    name = "Daily Multi-Order Ratio", 
    line=dict(color="lightskyblue", width=2), 
    mode="lines"
))
# 7-day moving average line
if "multiorder_ratio_smooth" in annual_stats.columns:
    fig.add_trace(go.Scatter(
        x = annual_stats.index, 
        y = annual_stats["multiorder_ratio_smooth"], 
        name = "7-Day Moving Avg", 
        line=dict(color="orange", width=3, dash="dash"), 
        mode="lines"
    ))

fig.update_layout(
    title = "Daily Multi-Order Ratio Over Time (每日多单率随时间的趋势)",
    xaxis_title = "Date (日期)",
    yaxis_title = "Multi-Order Ratio (多单率)",
    plot_bgcolor = "white",
    legend_title_text = "Legend (图例)"
)
st.plotly_chart(fig, use_container_width=True)

# Explanatory text for trends
st.markdown(
    "The chart above shows the daily **multi-order ratio** over time, along with a 7-day moving average to smooth out short-term fluctuations. "
    "We can observe overall trends in multi-order frequency across the year, identifying any seasonal patterns or significant changes. "
)
