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

st.markdown("""
<a href='https://www.youtube.com/dataprofessor' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"/></svg> Data Professor YouTube channel</a>
<a href='https://www.youtube.com/codingprofessor' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Coding Professor YouTube channel</a>
<a href='https://data-professor.medium.com/' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Read my Blogs</a>
<a href='https://twitter.com/thedataprof' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Follow me on Twitter</a>
<a href='https://www.linkedin.com/in/chanin-nantasenamat/' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Follow me on LinkedIn</a>
<a href='https://sendfox.com/dataprofessor' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Sign up for my Newsletter</a>
<a href='https://www.buymeacoffee.com/dataprofessor' class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">Buy me a Coffee</a>
""", unsafe_allow_html=True)
