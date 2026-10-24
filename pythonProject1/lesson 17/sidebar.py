import streamlit as st

st.header("SideBar")

st.write("This is a sidebar")

st.sidebar.selectbox("chose an option",["Option 1","Option 2","Option 3"])
st.sidebar.radio("Go to",["Home","Settings"])