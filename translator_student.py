import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator")

st.write("Enter text and choose a language to translate.")

text = st.text_area("Enter text to translate")

language = st.selectbox(
    "Select target language",
    [
        "es",  # Spanish
        "fr",  # French
        "de",  # German
        "it",  # Italian
        "pt",  # Portuguese
        "hi",  # Hindi
        "zh-cn",  # Chinese
        "ja"   # Japanese
    ]
)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(target=language).translate(text)
        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter text to translate.")
    
