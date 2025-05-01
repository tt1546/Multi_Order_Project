import streamlit as st

# Main App Title and Introduction
st.set_page_config(page_title="Multi-Order Dashboard", layout="wide")
st.title("Multi-Order Analysis Dashboard (多单分析仪表盘)")

st.markdown("""
This Streamlit app presents an interactive dashboard for multi-order analysis. 
Use the page navigation in the sidebar to explore:
- **Annual Statistics (年度统计)**: Yearly and time-series trends of multi-orders.
- **Multi-Order Analysis (多单分析)**: Patterns in multi-order behavior by day, hour, and product.
- **Fulfillment Cost Analysis (履约成本分析)**: Estimated cost savings from order consolidation.
- **Customer Segmentation (客户分群)**: Customer clusters and geographic distribution.
- **Model Predictor (模型预测器)**: Predict if an order will be a multi-order using the trained model.
""")
