# StreamLit Interface for Project:
import streamlit as st
from scrape import *
from parser import parse_content_llama

# set OLLAMA_NO_GPU=1

st.title("marfiiAI Web Scraper")
url = st.text_input("Enter the website URL to scrape:")

if st.button("Scrape Site",type="primary"):
    st.write("Scraping the website...")
    result = scrape_website(url)
    # Extract body content
    body_content = extract_body_content(result)
    # Clean HTMl style and script tags:
    cleaned_content = clean_html_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    description = st.text_area("What you want to parse?")
    if st.button("Parse Content",type="secondary"):
        if description:
            # LLM Parsing:
            st.write("Parsing the content...")
            dom_chunks = separate_into_tokens(st.session_state.dom_content)
            result = parse_content_llama(dom_chunks, description)
            st.write(result)