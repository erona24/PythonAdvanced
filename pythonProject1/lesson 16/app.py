import streamlit as st

if st.button("cLiCk mE"):
    st.write("bUttOni eShTe kLiKuAr")

if st.checkbox("check me to show some text"):
    st.write("you're seeing this text bc you checked the checkbox")


user_input = st.text_input("Enter some text")
st.write("you entered: ", user_input)

age = st.number_input("enter age",min_value=0,max_value=100)
st.write(f"your age is{age}")

message3= st.text_area("Enter a message")

st.write("you have entered", message3)

choice = st.radio("Pick one",["ai","python adv","javascript"])

if st.button("Success"):
    st.success("Operation was successful")

try:
    1/0
except Exception as e:
    st.exception(e)