import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
import webbrowser

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

button_font_size = 24

st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', button_font_size)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', button_font_size)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', button_font_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', button_font_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', button_font_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', button_font_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', button_font_size)
