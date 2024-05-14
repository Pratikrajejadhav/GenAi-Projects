import streamlit as st
import google.generativeai as genai
from PIL import Image
import matplotlib.pyplot  as plt 

api_key = "AIzaSyC_L3-d181ibSultwSEuGm6P4XwE8HIsEQ"
genai.configure(api_key=api_key)

# st.title ("Application")
# st.text("streamlit application")
# st.write("hello im creating an app")
# st.text_input("name"," ")
# st.button("click")

st.header("Image Analytics")
upload_file = st.file_uploader("Upload image", type=["png","jpg","jpeg"])

if upload_file is not None:
    st.image(Image.open(upload_file))


prompt = st.text_input("Enter the text")


if st.button("GET RESPONSE"):
    img = Image.open(upload_file)
    model=genai.GenerativeModel("gemini-1.0-pro-vision-latest")
    response=model.generate_content([prompt,img])
    st.markdown(response.text)