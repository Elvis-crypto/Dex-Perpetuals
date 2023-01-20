# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 2023

@author: Elvis Crypto
"""

from functions.sources import checkDatasets, protocol2Loader
from functions.readLlama import readLlama
from functions.str_panels import tSeriesLlamaBreakdown
from functions.processLlama import processLlamaIndiv
import streamlit as st
import plost
import altair as alt

#Refresh Datasets as necessary
checkDatasets(reloadInterval=24)

st.set_page_config(page_title='Perpetuals platform',layout='wide', initial_sidebar_state='expanded')

# Sidebar stuff
st.sidebar.header('DeFi Perpetuals Dashboard ')


st.sidebar.markdown('''
---
Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
''')   

st.markdown('''
            # DeFi Perpetuals
            ### This is a Research Project by PalmSwap aimed at tracking and reviewing the current state of the Perpetuals market on Defi
            ## You'll be able to find charts and articles on the following topics:
            #### ☑️ TVL Distribution of GMX, dYdX, Perpetual Protocol and ApolloX based on DeFiLlama data  
            #### ☐ Current list of players and features in the DeFi & CeFi Perpetuals space   
            #### ☐ Contract to CEX flow metrics for on-chain Perpetual protocols   
            #### ☐ Cross-protocol and cross-chain flows for on-chain Perpetual protocols   
            #### ☐ User classification of on-chain Perpetual protocols address behaviour  
            #### ☐ Case studies of user actions on platforms    
            #### ☐ Outstanding Long/Short interest on platforms  
            
            '''
    )