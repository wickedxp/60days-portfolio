import streamlit as st

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)
    
with col2:
    st.title("Saul DeJesus")
    content = """Hello, my name is Saul DeJesus! I am a wanna-be Python programmer. Started this journey two years ago and started working 
    on multiple project since then. Love everything about Python programming"""
    
    st.write(content)

content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)