# ==============================================================
# 📘 Streamlit_mythirdapps --> Python Basic To Advanced
# Author: Muhammad Shah Asyraf
# Credit: Yash Sharma
# Artificial Intelligence & Machine Learning Course
# ==============================================================

import streamlit as st
# Page Setup
st.set_page_config(page_title='Colors and Layout')
st.title("Colors, Layouts & Charts")
st.write("Let's Make Our App Beautiful and Organized")
st.markdown("""
<div style="background-color: #E3E3A6">
<h3 style="color: #451108">HTML Style Using Markdown</h3> <p>This is HTML Paragraph Tag</p>
</div>
""",unsafe_allow_html=True)
# markdown
st.markdown("\n")
# display text in bold and italic
st.markdown("**Streamlit** is a python library for creating interactive *web apps*")

# Links
st.markdown("Visit For More Info: (https://streamlit.io/) *To Learn* **Streamlit**")
# code()
code1 = '''def hello():
print('Hi i am a python function')'''

st.code(code1, language="python")

# Latex()
st.latex('''
(a+b)^2 =a^2+b^2 + 2*a*b
''')

st.markdown ("\n")
st.markdown("**Sigmoid Function**")
st.latex(r'''
\frac {1}{1+e^-score}        
''')


# Layouts
coll, col2 = st.columns (2)

with coll:
    st.header("Left Side")
    name = st.text_input ('Enter Your Name ?') 
    st.write("Hello User ",name if name else "Guest")
    
with col2:
    st.header("Right Side")
    age = st.slider ("Pick A Number", 1,100,25)
    st.write(f"Next Year You Will Become {age+1} Year Old ")
    
# A sidebar is like a mini control panel on the left sidebar

with st.sidebar:
    st.header('Control Panel')
    user_color = st.color_picker('Pick Your Favorite Color','#000000')
    st.write('You Have Selected :',user_color)