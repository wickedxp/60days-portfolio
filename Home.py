import streamlit as st
import pandas as pd

#st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)
    
with col2:
    st.title("Saul DeJesus")
    content = """Hello, my name is Saul DeJesus! I am a wanna-be Python programmer. Started this journey two years ago and started working 
    on multiple project since then. Love everything about Python programming"""
    
    st.write(content)

st.divider()
content2 = """Below you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=';')
    
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.markdown(f"""[source code]({row['url']})""")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.markdown(f"""[source code]({row['url']})""")