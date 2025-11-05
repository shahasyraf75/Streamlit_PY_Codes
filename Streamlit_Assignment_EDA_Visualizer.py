# ==============================================================
# 📘 Streamlit Application: Simple EDA & Visualization Tool
# Author: Muhammad Shah Asyraf
# Description: Interactive app for EDA where user uploads CSV,
# selects columns, and visualizes data (Line / Bar chart)
# ==============================================================

# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

# --------------------------------------------------------------
# 🏷️ Application Title & Page Config
# --------------------------------------------------------------
st.set_page_config(page_title="EDA Visualizer", layout="wide")
st.title("📊 Simple EDA Application")
st.caption("Developed by Muhammad Shah Asyraf — for assignment purpose.")
st.write("Upload your CSV file and visualize your data easily below 👇")

# --------------------------------------------------------------
# 📁 1. File Upload Section
# --------------------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=['csv'])

# Check if file uploaded
if uploaded_file is not None:
    # Read the CSV file into dataframe
    df = pd.read_csv(uploaded_file)
    
    st.success("✅ File uploaded successfully!")
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())  # show first few rows

    # ----------------------------------------------------------
    # 📈 2. Column Selection
    # ----------------------------------------------------------
    st.subheader("⚙️ Select Columns for Visualization")
    columns = df.columns.tolist()

    # Dropdown menus for selecting X and Y axes
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    # ----------------------------------------------------------
    # 🧭 3. Data Visualization Section
    # ----------------------------------------------------------
    st.subheader("🎨 Data Visualization")

    col1, col2 = st.columns(2)

    # Button 1: Line Graph
    with col1:
        if st.button("Click Here For Line Graph"):
            fig, ax = plt.subplots(figsize=(8,4))
            ax.plot(df[x_axis], df[y_axis], marker='o', linestyle='-', color='royalblue')
            ax.set_title(f"Line Graph: {y_axis} vs {x_axis}", fontsize=12)
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)

    # Button 2: Bar Chart
    with col2:
        if st.button("Click Here For Bar Chart"):
            fig, ax = plt.subplots(figsize=(8,4))
            ax.bar(df[x_axis], df[y_axis], color='darkorange')
            ax.set_title(f"Bar Chart: {y_axis} vs {x_axis}", fontsize=12)
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            st.pyplot(fig)

    # ----------------------------------------------------------
    # 📊 4. Optional: Summary Statistics
    # ----------------------------------------------------------
    if st.checkbox("📉 Show Summary Statistics"):
        st.subheader("📊 Data Summary")
        st.write(df.describe())

else:
    st.info("👆 Please upload a CSV file to begin your analysis.")