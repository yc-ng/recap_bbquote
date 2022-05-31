import streamlit as st
from bbquote.lib import get_quote

quote, author = get_quote()

st.write(f"{quote}", "\n- ", f"{author}")
