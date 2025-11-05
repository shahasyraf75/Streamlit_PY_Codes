import streamlit as st
import numpy as np
import pandas as pd
import io

st.set_page_config(page_title='Analyze Your Data',layout='wide',page_icon='🧔‍♂️')

st.title('📊 Analyze Your Data')
st.write('Upload a CSV File and explore your data interactively!')

# for uploading csv file
uploaded_file = st.file_uploader('📁 Upload Your CSV File ',type=['csv'])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        # converting bool column as str
        bool_cols = df.select_dtypes(include=['bool']).columns
        df[bool_cols] = df[bool_cols].astype(str)
    except Exception as e:
        st.error('Could Not Read The CSV. Please Check The File Format')
        st.exception(e)
        st.stop()

    st.success('✅ File Uploaded Successfully !')
    st.write('### Preview Of Data')
    st.dataframe(df.head())

    st.write('### 🔎 Data Overview')
    st.write('Number Of Rows :',df.shape[0])
    st.write('Number Of Columns :',df.shape[1])
    st.write('Number Of Missing Values :',int(df.isnull().sum().sum()))
    st.write('Number Of Duplicate Records :',df.duplicated().sum())

    st.subheader('ℹ️ Complete Summary Of Dataset')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
    st.write('### 📈 Statistical Summary')
    st.dataframe(df.describe())

    st.write('### 📈 Statistical Summary for Non Numerical Features')
    st.dataframe(df.describe(include='object'))

    st.subheader('✨ Select The Desired Columns For Analysis')

    # Multiselect box
    columns = st.multiselect('Choose Columns',df.columns.tolist())

    st.subheader('💻 Preview')

    if columns:  # if user selected one or more column
        st.dataframe(df[columns].head())
    else:
        st.info('No Columns Selected. Showing Full Dataset.')
        st.dataframe(df.head())

    st.subheader('😣 Showing 10 Records Where Customer Service Calls > 4')
    filtered_df = df[df['customer service calls'] > 4]
    result = filtered_df[['phone number','customer service calls', 'churn']]
    st.dataframe(result.head(10))

    st.subheader('📊 International Plan Usage')
    count = df['international plan'].value_counts()
    st.bar_chart(count)

else:
    st.info('Please Upload a CSV File to get started')