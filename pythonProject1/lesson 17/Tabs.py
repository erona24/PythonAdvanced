import streamlit as st

tab1, tab2, tab3 = st.tabs(["tab 1", "tab2", "tab3"])

with tab1:
    st.header("content of tab 1")
    st.button("click")

with tab2:
    st.header("kontenti i tabit te 2te")
    st.write("welcome")

with tab3:
    st.header("jemi ne tab 3")
    st.write("hello there")