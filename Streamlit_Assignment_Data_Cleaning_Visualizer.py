# ==============================================================
# 📘 Streamlit Application: Data Cleaning & Visualization Tool
# Author: Muhammad Shah Asyraf
# Description: Interactive app for D.C where user uploads CSV,
# selects columns, and visualizes data (Bar / Pie chart)
# ==============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------------------------
# 🌿 App Setup
# ---------------------------------
st.set_page_config(page_title="Data Cleaning & Visualization App", page_icon="🧹", layout="wide")
st.title("🧹 Data Cleaning & Visualization App")
st.markdown("""
This Streamlit application helps you clean and visualize your dataset with **clarity and honesty**.  
You can upload a CSV or Excel file, review the summary, handle missing or duplicate values,  
and visualize your data in a simple, interactive way.
""")
st.divider()

# ---------------------------------
# 📂 File Upload
# ---------------------------------
uploaded_file = st.file_uploader("📁 Please upload your CSV or Excel file:", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"❌ Unable to read the file. Please check the file structure. Error: {e}")
        st.stop()

    # Initialize session state
    if "cleaned_data" not in st.session_state:
        st.session_state.cleaned_data = data.copy()

    # ---------------------------------
    # 📊 Data Summary (Before Cleaning)
    # ---------------------------------
    st.subheader("📋 Data Summary (Before Cleaning)")
    st.write("**Rows:**", data.shape[0])
    st.write("**Columns:**", data.shape[1])
    st.write("**Total Missing Values:**", data.isnull().sum().sum())
    st.write("**Duplicate Records:**", data.duplicated().sum())
    st.dataframe(data.head())

    st.divider()

    # ---------------------------------
    # 🧩 Cleaning Options
    # ---------------------------------
    st.subheader("🛠️ Choose a Cleaning Operation")

    col1, col2, col3 = st.columns(3)

    # Remove Missing Values
    with col1:
        if st.button("🧽 Remove Missing Values"):
            cleaned = data.dropna()
            st.session_state.cleaned_data = cleaned
            st.success("✅ All rows with missing values have been removed.")

    # Handle Missing Values (fillna/interpolate)
    with col2:
        if st.button("🔧 Handle Missing Values (fillna/interpolate)"):
            cleaned = data.copy()
            for col in cleaned.columns:
                if cleaned[col].dtype == "object":
                    cleaned[col] = cleaned[col].fillna("Unknown")
                else:
                    cleaned[col] = cleaned[col].interpolate()
            st.session_state.cleaned_data = cleaned
            st.success("✅ Missing values handled with fillna/interpolate method.")

    # Remove Duplicates
    with col3:
        if st.button("🗑️ Remove Duplicate Rows"):
            cleaned = data.drop_duplicates()
            st.session_state.cleaned_data = cleaned
            st.success("✅ Duplicate records have been removed.")

    st.divider()

    # ---------------------------------
    # 📊 Summary After Cleaning
    # ---------------------------------
    cleaned_data = st.session_state.cleaned_data

    st.subheader("📋 Data Summary (After Cleaning)")
    st.write("**Rows:**", cleaned_data.shape[0])
    st.write("**Columns:**", cleaned_data.shape[1])
    st.write("**Total Missing Values:**", cleaned_data.isnull().sum().sum())
    st.write("**Duplicate Records:**", cleaned_data.duplicated().sum())
    st.dataframe(cleaned_data.head())

    st.divider()

    # ---------------------------------
    # 📈 Visualization
    # ---------------------------------
    st.subheader("📊 Data Visualization (After Cleaning)")

    col_x, col_y = st.columns(2)
    x_axis = col_x.selectbox("Select X-axis:", options=cleaned_data.columns)
    y_axis = col_y.selectbox("Select Y-axis:", options=cleaned_data.columns)

    c1, c2 = st.columns(2)

    # Bar Chart
    with c1:
        if st.button("📊 Show Bar Chart"):
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(cleaned_data[x_axis].astype(str), cleaned_data[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Bar Chart")
            st.pyplot(fig)

    # Pie Chart
    with c2:
        if st.button("🥧 Show Pie Chart"):
            fig, ax = plt.subplots(figsize=(6, 6))
            cleaned_data[y_axis].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
            ax.set_ylabel('')
            st.pyplot(fig)

    st.divider()

    # ---------------------------------
    # 💾 Download Cleaned File
    # ---------------------------------
    cleaned_csv = cleaned_data.to_csv(index=False).encode('utf-8')
    filename = f"cleaned_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    st.download_button(
        label="⬇️ Download Cleaned CSV File",
        data=cleaned_csv,
        file_name=filename,
        mime="text/csv"
    )

else:
    st.info("👆 Please upload a CSV or Excel file to begin the data cleaning process.")