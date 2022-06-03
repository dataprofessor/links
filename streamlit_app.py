import streamlit as st
from PIL import Image
import webbrowser

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.title('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

st.markdown("""
<a href='https://www.youtube.com/dataprofessor' class="btn btn-primary btn-lg btn-block active" role="button" aria-pressed="true">Data Professor YouTube channel</a>
<a href='https://www.youtube.com/codingprofessor' class="btn btn-primary btn-lg btn-block active" role="button" aria-pressed="true">Coding Professor YouTube channel</a>
<a href='https://data-professor.medium.com/' class="btn btn-primary btn-lg btn-block active" role="button" aria-pressed="true">Read my Blogs</a>
<a href='https://twitter.com/thedataprof' class="btn btn-primary btn-lg btn-block active" role="button" aria-pressed="true">Follow me on Twitter</a>
<a href='https://www.linkedin.com/in/chanin-nantasenamat/' class="btn btn-primary btn-lg btn-block active" role="button" aria-pressed="true">Follow me on LinkedIn</a>
""", unsafe_allow_html=True)
