import streamlit as st
from app_pages.multi_page import MultiPage
from app_pages.page1 import page1_body
from app_pages.page2 import page2_body

app = MultiPage(app_name='This is my first multipage app')
app.app_page('Page 1', page1_body)




