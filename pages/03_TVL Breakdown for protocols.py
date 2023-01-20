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

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Sidebar stuff
st.sidebar.header('DeFi Perpetuals Dashboard ')
st.sidebar.subheader('Select protocol to explore.')
selected_protocol= st.sidebar.radio('Protocol Name',['GMX','dYdX','Perpetual Protocol','ApolloX'],index=0)
show_sanity = st.sidebar.checkbox('Show sanity check graphs',False)

st.sidebar.markdown('''
    ---
''')
st.sidebar.subheader('''
🗝️ Key takeaways 🗝️
''')

if (selected_protocol == 'GMX'):
    st.sidebar.markdown('''
    GMX, the dominant player in the space by TVL has around 40% of it's TVL in GMX tokens staked mostly on arbitrum. While their USDC TVL from their business is increasing this proportion is still very high compared to dYdX or Perpetual Protocol
    ''')
elif (selected_protocol == 'dYdX'):
    st.sidebar.markdown('''
    Compared to the others dYdX has the most stable business model. It has always converted deposits to USDC and this is the basis of settlement on the exchange. While they may be currently smaller than GMX with 393 M USD locked, any market fluctuations are more likely to strengthen their position as they are not directly exposed.
    ''')
elif (selected_protocol == 'Perpetual Protocol'):
    st.sidebar.markdown('''
    Perpetual Protocol used to have TVLs near 600 M USD before 2021 November, but most of this value was in PERP tokens staked on the ethereum chain. The staked token proportion of their TVL has collapsed by now (below 5%). What remains is 'real' business on their platform in the form of ~8.5 M locked USDC.
    ''')
elif (selected_protocol == 'ApolloX'):
    st.sidebar.markdown('''
    ApolloX's exposure to their own token remains limited around 25%. Most of their TVL (around 20 M USD) is from deposits locked with their exchange on BSC.
    ''')

st.sidebar.markdown('''
---
Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
---
Data📊 by [DefiLlama](https://defillama.com/).
''')   

current_test=protocol2Loader[selected_protocol]
test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total = readLlama(current_test)
processed = processLlamaIndiv(test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total)

st.markdown(f'''
Dataset Overview {processed['test_both']['Protocol'][0]}
---
''')

if(show_sanity):
    st.markdown(f'''
    #### Summed TVL Vs. DeFi Llama TVL for {processed['test_both']['Protocol'][0]}
    ''')
    plost.line_chart(
        processed['test_both'],
        x='Date',
        y=['TVL_summed','TVL_Llama'],
        height=600,
        title=processed['test_both']['Protocol'][0],
        pan_zoom='both'  # 👈 This is magic!
        )
    
    st.markdown(f'''
    ---
    #### Is DeFi Llama Total == Sum(Other origins) without staking?
    ''')
    plost.line_chart(
        processed['test_bothNoStake'],
        x='Date',
        y=['TVL_noStaking_shifted2prtc','TVL_Llama'],
        height=600,
        title=processed['test_both']['Protocol'][0],
        pan_zoom='both'  # 👈 This is magic!
        )

tSeriesLlamaBreakdown(Category='Origin', series_df=processed['test_origin'], isSubTotal=True)
tSeriesLlamaBreakdown(Category='Currency', series_df=processed['test_all'], isSubTotal=False)
tSeriesLlamaBreakdown(Category='Currency', series_df=processed['test_all'], isSubTotal=False, isStaking=True)
tSeriesLlamaBreakdown(Category='Origin', series_df=processed['test_all'], isSubTotal=False, isStaking=True)