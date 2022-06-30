# Welcome to Streamlit `links page`

> A Streamlit app that you can build for free to store all your personal links similar in functionality to that of [Linktr.ee](https://linktr.ee/).

# Getting started

Getting your own Streamlit `links page` up and running is really easy, just follow the following steps:
1. [Click here](https://github.com/dataprofessor/links/generate) to generate a copy of this repository. Next, name your new repository to anything you'd like except for `your username`.github.io
2. Customize the contents of the newly generated `links page` by editing the `streamlit_app.py` file:
```python
import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Chanin Nantasenamat, Ph.D.')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

icon_size = 20

st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/chanin-nantasenamat/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
```

There are 3 key information that you can modify:
1. `st.header(A)` is used for specifying your name in place of **A**.
2. `st.info(B)` is used for speciying a quick description about who you are, what you do, etc. in place of **B**.
3. `st.button(A, B, C, D)` is a custom function for creating link buttons where **A** represents the icon to display (use `youtube` if the play button is to be displayed), **B** represents the URL, **C** represents the message to display on the clickable button and **D** represents the icon size.
