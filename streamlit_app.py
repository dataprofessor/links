import streamlit as st
from PIL import Image
import webbrowser

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.title('Chanin Nantasenamat, Ph.D.')

st.write('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

if st.button('YouTube channel'):
    webbrowser.open_new_tab('https://youtube.com/dataprofessor')
