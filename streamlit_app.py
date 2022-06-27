import streamlit as st
from PIL import Image
import webbrowser

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')


st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', 26)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', 26)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', 26)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', 26)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', 26)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', 26)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', 26)
