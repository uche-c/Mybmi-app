import streamlit as st
from PIL import Image

st.header( "MY BMI APP")

img = Image.open( "Bmifile.jpg")
st.image(img)

weight = st.number_input( "Input your weight (kg)", step = 0.1)
height = st.number_input( "Input your height (m)")

def bmi_calc(w,h):
    bmi = round(w/h**2, 2)
    return bmi

def bmi_rating(b):
    if b > 25:
        st.write("Please see a doctor!")
    elif 18.4 < b < 25.1:
        st.write("You are doing great!")
    else:
        st.write("You are underweight! Please see a doctor.")
        

if st.button( "Calculate"):
    score = bmi_calc(weight, height)
    st.write(score)
    bmi_rating(score)
