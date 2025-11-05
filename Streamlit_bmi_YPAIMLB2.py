import streamlit as st # type: ignore
import pandas as pd # type: ignore
import altair as alt # type: ignore

st.set_page_config(page_title='BMI Calculator',layout='centered')

st.title('😁 BMI Calculator')
st.write("Let's calculate your **Body Mass Index [BMI]** and understand what it means")

st.header('😎 Enter Your Details')

height = st.number_input('Enter your height (in cm)',min_value=50,max_value=250,value=160)
weight = st.number_input('Enter your weight (in kg)',min_value=10,max_value=200,value=50)


st.write('🤝 Your Height :',height,'cm')
st.write('💪 Your Weight :',weight,'kg')

if st.button('Calculate BMI'):
    h_m = height / 100         # convert cm to meter
    bmi = weight / (h_m ** 2)
    st.success(f'YOUR BMI IS **{bmi:.2f}**')

    # BMI Category
    if bmi < 18.5:
        category = 'Underweight 😵'
        color = '#27F5EB'

    elif 18.5 <= bmi < 25:
        category = 'Normal 🤗'
        color = "#2DF33D"

    elif 25 <= bmi < 30:
        category = 'Overweight 😮‍💨'
        color = "#FFC504"
    
    else:
        category = 'Obese 😱'
        color = "#CC1204"
    
    st.markdown(
        f'''
        <div style='background-color:{color};padding:15px;border-radius:10px;test-allign:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        ''',
        unsafe_allow_html=True
    )

st.header("📊 BMI Range Chart")
 
# Data
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})
 
# Define custom colors for each category
color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=["#27F5EB", "#2DF33D", "#FFC504", "#CC1204"]
)
 
# Create chart
chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N", title="BMI Category"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=400)
)
 
st.altair_chart(chart, use_container_width=True)