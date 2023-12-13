import streamlit as st
from PIL import Image

image = Image.open('Assets/arcane.jpeg')
st.image(image)

st.write("## For more information visit: [Github](https://github.com/CoulsonZhang/6893BigData)")
st.write("## Team: Song Wen, Zheyu Zhang")

