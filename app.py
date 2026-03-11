import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression

# PAGE CONFIG
st.set_page_config(page_title="UIDAI Aadhaar Enrolment Dashboard", layout="wide")

st.title("UIDAI Aadhaar Enrolment Analysis & Prediction")
st.markdown("Data-driven insights for inclusive Aadhaar service planning")

# LOAD DATA
@st.cache_data
def load_data():
    files = [
        "api_data_aadhar_enrolment_0_500000.csv",
        "api_data_aadhar_enrolment_500000_1000000.csv",
        "api_data_aadhar_enrolment_1000000_1006029.csv"
    ]
    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
    df['total_enrolment'] = df['age_0_5'] + df['age_5_17'] + df['age_18_greater']
    return df

df = load_data()

# SIDEBAR FILTER
st.sidebar.header("Filters")
states = ["All"] + sorted(df['state'].unique().tolist())
selected_state = st.sidebar.selectbox("Select State", states)

if selected_state != "All":
    df = df[df['state'] == selected_state]


# METRICS
col1, col2, col3 = st.columns(3)

col1.metric("Total Enrolments", f"{df['total_enrolment'].sum():,}")
col2.metric("Total Districts", df['district'].nunique())
col3.metric("Total PIN Codes", df['pincode'].nunique())

# AGE-WISE ENROLMENT
st.subheader("Age-wise Aadhaar Enrolment")

age_data = df[['age_0_5', 'age_5_17', 'age_18_greater']].sum()

fig1, ax1 = plt.subplots()
age_data.plot(kind='bar', ax=ax1)
ax1.set_ylabel("Enrolments")
ax1.set_title("Age-wise Distribution")

st.pyplot(fig1)


# STATE-WISE ENROLMENT

st.subheader("State-wise Enrolment")

state_data = df.groupby('state')['total_enrolment'].sum().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(8,4))
state_data.head(10).plot(kind='bar', ax=ax2)
ax2.set_ylabel("Enrolments")
ax2.set_title("Top 10 States")

st.pyplot(fig2)


# MONTHLY TREND
st.subheader("Monthly Enrolment Trend")

monthly_data = df.groupby(
    pd.Grouper(key='date', freq='ME')
)['total_enrolment'].sum().reset_index()

fig3, ax3 = plt.subplots(figsize=(10,4))
ax3.plot(monthly_data['date'], monthly_data['total_enrolment'])
ax3.set_title("Monthly Aadhaar Enrolment Trend")
ax3.set_ylabel("Enrolments")

st.pyplot(fig3)


# PREDICTION

st.subheader("Enrolment Forecast (Next 6 Months)")

monthly_data['month_index'] = np.arange(len(monthly_data))
X = monthly_data[['month_index']]
y = monthly_data['total_enrolment']

model = LinearRegression()
model.fit(X, y)

future_index = pd.DataFrame({
    'month_index': np.arange(len(monthly_data), len(monthly_data) + 6)
})

future_predictions = model.predict(future_index)

future_dates = pd.date_range(
    start=monthly_data['date'].iloc[-1] + pd.offsets.MonthEnd(1),
    periods=6,
    freq='ME'
)

fig4, ax4 = plt.subplots(figsize=(10,4))
ax4.plot(monthly_data['date'], y, label="Actual")
ax4.plot(future_dates, future_predictions, linestyle="--", marker="o", label="Predicted")
ax4.legend()
ax4.set_title("Aadhaar Enrolment Forecast")

st.pyplot(fig4)

