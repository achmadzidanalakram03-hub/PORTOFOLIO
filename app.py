import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi tampilan halaman Streamlit
st.set_page_config(
    page_title="Adinara Savero — Portofolio Koas Kedokteran Gigi",
    page_icon="??",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hilangkan padding default dan header/footer bawaan Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Baca file HTML portofolio Anda
with open("Adinara Savero — Portofolio Koas Kedokteran Gigi.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML di dalam Streamlit
components.html(html_content, height=2000, scrolling=True)