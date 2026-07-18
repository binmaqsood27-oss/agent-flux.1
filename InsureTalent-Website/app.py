import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Agent Flux",
    layout="wide"
)

with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()

components.html(
    html,
    height=2000,
    scrolling=True
)