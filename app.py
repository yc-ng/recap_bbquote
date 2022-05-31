import streamlit as st
from bbquote.lib import get_quote

st.markdown(f'''
Who said what?

{get_quote()}
''')
