import streamlit as st
import pandas as pd
import xgboost as xgb

st.title("Multi-Order Predictor")

st.write(
    "Input the order/customer features below to predict the probability that an order will be a **multi-order**. "
)

# Input fields for each feature
quantity = st.number_input("Quantity", min_value=1, value=1)
label_price = st.number_input("Label Price", min_value=0.0, value=100.0)
discount = st.number_input("Discount", min_value=0.0, value=0.0)
amount = st.number_input("Amount", min_value=0.0, value=100.0)
order_weekday = st.selectbox("Order Weekday", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], index=0)
order_hour = st.slider("Order Hour", min_value=0, max_value=23, value=12)
is_weekend = st.checkbox("Is Weekend?", value=False)
is_night = st.checkbox("Is Night?", value=False)
cluster_id = st.selectbox("Customer Cluster", [0, 1, 2], index=0)
member_level = st.selectbox("Member Level", ["A","B","C"], index=2)
customer_segment = st.selectbox("Customer Segment", ["Low","Medium","High"], index=2)
customer_group = st.selectbox("Customer Group ID", ["CustomerGroup_0","CustomerGroup_1"], index=0)
option_id_input = st.text_input("Option ID", value="Option_0")

# Convert inputs to proper types and encodings
weekday_map = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
order_weekday_num = weekday_map.get(order_weekday, 0)
# Convert booleans to 0/1
is_weekend_num = 1 if is_weekend else 0
is_night_num = 1 if is_night else 0
# Encode member_level and customer_segment to numeric codes for the model
member_map = {"A": 0, "B": 1, "C": 2}
segment_map = {"Low": 0, "Medium": 1, "High": 2}
member_level_num = member_map.get(member_level, 0)
customer_segment_num = segment_map.get(customer_segment, 0)
# Customer group: extract numeric part or map string to int
try:
    customer_group_num = int(customer_group.split('_')[-1])
except:
    customer_group_num = 0
# Option ID: if starts with non-numeric, extract number; otherwise use as int
try:
    option_num = int(option_id_input.split('_')[-1])
except:
    try:
        option_num = int(option_id_input)
    except:
        option_num = 0

# Prepare input DataFrame for model
input_features = pd.DataFrame([{
    "quantity": quantity,
    "label_price": label_price,
    "discount": discount,
    "amount": amount,
    "order_weekday": order_weekday_num,
    "order_hour": order_hour,
    "is_weekend": is_weekend_num,
    "is_night": is_night_num,
    "cluster": cluster_id,
    "member_level": member_level_num,
    "customer_segment": customer_segment_num,
    "customer_group_id": customer_group_num,
    "option_id": option_num
}])

# Load the trained XGBoost model
model = xgb.XGBClassifier()
model.load_model("models/xgb_model.json")

# Perform prediction when user clicks the button
if st.button("Predict"):
    # Get prediction probability for class 1 (multi-order)
    y_prob = model.predict_proba(input_features)[0][1]
    y_pred = model.predict(input_features)[0]
    # Display results
    st.write(f"**Predicted Probability of Multi-Order:** {y_prob*100:.2f}% "
             f"({'Yes' if y_pred==1 else 'No'} likelihood) "
    if y_pred == 1:
        st.success("The model predicts this order is likely to be a multi-order. )")
    else:
        st.info("The model predicts this order is not likely to be a multi-order. )")
