import streamlit as st
from bbquote.lib import get_quote

quote = get_quote()

f"{quote}"
