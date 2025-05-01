import streamlit as st

# Main App Title and Introduction
st.set_page_config(page_title="Multi-Order Dashboard", layout="wide")
st.title("Multi-Order Analysis Dashboard")

st.markdown("""
This Streamlit app presents an interactive dashboard for multi-order analysis. 
Use the page navigation in the sidebar to explore:
- **Multi-Order Analysis**: Patterns in multi-order behavior by day, hour, and product.
- **Time Statistics**: Time-series trends of multi-orders.
- **Customer Segmentation**: Customer clusters and geographic distribution.
- **Fulfillment Cost Analysis**: Estimated cost savings from order consolidation.
- **Model Predictor**: Predict if an order will be a multi-order using the trained model.
""")