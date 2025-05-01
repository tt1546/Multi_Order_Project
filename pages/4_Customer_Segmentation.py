import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customer Segmentation (客户分群)")

# Load customer cluster/segment data
customers = pd.read_csv("data/hotzone_customers.csv")
# Assume hotzone_customers.csv contains columns: address_lat, address_lon, customer_segment
# If cluster IDs are present instead of names, map them to segment names
if "cluster" in customers.columns and "customer_segment" not in customers.columns:
    # Map cluster IDs to segment labels if needed (example mapping: 0->High,1->Low,2->Medium)
    id_to_seg = {0: "High", 1: "Low", 2: "Medium"}
    customers["customer_segment"] = customers["cluster"].map(id_to_seg)

# Plot geographic distribution of customers colored by segment
fig = px.scatter(
    customers, x="address_lon", y="address_lat", 
    color="customer_segment", 
    color_discrete_map={"Low": "blue", "Medium": "green", "High": "orange"},
    labels={"address_lon": "Longitude (经度)", "address_lat": "Latitude (纬度)"},
    title="Customer Geographic Distribution by Segment (按客户分段的地理分布)"
)
fig.update_layout(plot_bgcolor="white", legend_title_text="Customer Segment (客户分段)")
st.plotly_chart(fig, use_container_width=True)

st.markdown(
    "Customers have been clustered into three groups based on their multi-order behavior and location. "
    "(根据多单行为和地理位置，将客户聚类为三个群组。) "
    "We label these segments as **Low**, **Medium**, and **High** engagement segments. "
    "(我们将这些簇标记为多单参与度**低**、**中**、**高**的客户群。) "
)
st.markdown(
    "- **High Segment (高段)** (orange points): Customers with the highest multi-order frequency or value. (多单频率或金额最高的客户，橙色点)"
    "\n- **Medium Segment (中段)** (green points): Customers with moderate multi-order behavior. (多单行为适中的客户，绿色点)"
    "\n- **Low Segment (低段)** (blue points): Customers with the least multi-order involvement. (多单参与度最低的客户，蓝色点)"
)
st.markdown(
    "All three segments show a heavy concentration in the central region, indicating most multi-order customers are geographically clustered in core service areas. "
    "(这三类客户都高度集中在中心区域，表明大多数多单客户在核心服务区域内。) "
    "Despite similar locations, their multi-order engagement levels differ, which helps tailor marketing and fulfillment strategies for each group. "
    "(尽管地理位置相近，他们的多单参与程度不同，这有助于针对每一群体定制营销和履约策略。)"
)
