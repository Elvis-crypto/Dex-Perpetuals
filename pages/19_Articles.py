# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 2023

@author: Elvis Crypto
"""

import streamlit as st
import plost
import altair as alt
import importlib
from functions.articles import getArticles

artNums2Names, artNames2FNames = getArticles()


st.set_page_config(page_title='Research articles',layout='wide', initial_sidebar_state='expanded')

# Sidebar stuff
st.sidebar.header('Research articles ')
# st.sidebar.markdown('''
# ---

# ''')   
selectedArticle = st.sidebar.selectbox('Please select an article to load', list(artNums2Names.values()),index=0)
modArticle = importlib.import_module('articles.'+artNames2FNames[selectedArticle])

modArticle.article()