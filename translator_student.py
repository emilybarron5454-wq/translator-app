import streamlit as st
from googletrans import Translator

st.title("Language Translation App")

translator = Translator()

text = st.text_area("Enter text to translate")

languages = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh-cn"
}

target_language = st.selectbox("Select target language", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = translator.translate(text, dest=languages[target_language])
        st.write("Translated Text:")
        st.success(translated.text)
