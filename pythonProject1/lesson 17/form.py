import streamlit as st


with st.form(key="my_form", clear_on_submit=True):
    name = st.text_input("Name")

    age = st.slider("Age", min_value=0, max_value=100)

    email = st.text_input("Email")

    biography = st.text_area("Short bio")

    terms = st.checkbox("I agree to the Terms and Conditions")

    summbit_button = st.form_submit_button(label="Submit")

if summbit_button:
    st.write("Name of the person is:",name)
    st.write("Age of the person is:", age)
    st.write("Email of the person is:", email)
    st.write("Biography of the person is:", biography)

if terms:
    st.write("You agreed to the Terms and Conditions")
else:
    st.write("You did not agre to the Terms and Conditions")