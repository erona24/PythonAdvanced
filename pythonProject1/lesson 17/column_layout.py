import streamlit as st

col1,col2,col3,col4,col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("Kolona e Pare")
    st.write("Kjo eshte kolona e pare")
with col2:
    st.header("Kolona e Dyte")
    st.write("Kjo eshte kolona e dyte")
with col3:
    st.header("Kolona e Trete")
    st.write("Kjo eshte kolona e trete")
with col4:
    st.header("Kolona e Katert")
    st.write("Kjo eshte kolona e katert")
with col5:
    st.header("Kolona e Peste")
    st.write("Kjo eshte kolona e peste")
