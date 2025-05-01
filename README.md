# Multi-Order Analysis Dashboard

An interactive multi-page dashboard built with Streamlit for analyzing multi-order behavior and predicting multi-order likelihood using a trained XGBoost model.

## Features

- 📊 **Data Overview**: High-level summary of the order dataset.
- 📈 **Annual Statistics**: Time-series analysis of multi-order trends.
- 🕒 **Multi-Order Analysis**: Patterns by weekday, hour, and product options; includes a heatmap.
- 📦 **Fulfillment Cost Analysis**: Simulation of potential delivery cost savings via order consolidation.
- 👥 **Customer Segmentation**: Visualization of clustered customers by multi-order behavior.
- 🤖 **Model Predictor**: Input features to predict the likelihood of an order being a multi-order using XGBoost.

## Installation

To install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the App

From the project root directory, launch the app with:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Project Structure

```
my_streamlit_dashboard/
├── app.py                    # Main entry point
├── pages/                    # Subpages
│   ├── 1_Annual_Statistics.py
│   ├── 2_Multi_Order_Analysis.py
│   ├── 3_Fulfillment_Cost_Analysis.py
│   ├── 4_Customer_Segmentation.py
│   └── 5_Model_Predictor.py
├── data/                     # Data files (CSV/Excel)
├── model/                    # Trained XGBoost model file
├── requirements.txt          # Python dependencies
└── README.md                 # Project description and usage
```

## Deployment (Optional)

You can deploy this app for public access using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push the entire project folder to a GitHub repository.
2. Log into Streamlit Cloud and click **New app**.
3. Select your repo and set the main file to `app.py`.
4. Click **Deploy**.

Your dashboard will be live and shareable via a public link.

## License

This project is provided for educational and non-commercial use.
