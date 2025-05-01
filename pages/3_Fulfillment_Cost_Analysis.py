import streamlit as st

st.title("Fulfillment Cost Analysis")

st.markdown("**Simulation of Order Consolidation**", unsafe_allow_html=True)
st.write(
    "This section estimates logistics cost savings if multiple orders are consolidated into one delivery. "
    "By comparing the original fulfillment costs with consolidated deliveries, we assess potential efficiency gains. "
)

# Display key results as metrics
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Estimated Savings Rate", value="26.5%")
with col2:
    st.metric(label="Avg Delivery Cost Reduction per Multi-Order", value="~27%")

st.markdown(
    "*Key Findings:* On average, consolidating multi-order deliveries can save approximately **26-27%** of fulfillment costs. "
    "Each customer segment sees substantial savings: for instance, one segment achieved about **27.5%** cost reduction, the highest relative savings among the clusters. "
    "These results imply significant logistics efficiency gains across different customer groups when adopting merged delivery strategies. "
)
