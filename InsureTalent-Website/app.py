from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Agent Flux",
    layout="wide"
)

html_path = Path(__file__).parent / "index.html"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=1200, scrolling=True)
