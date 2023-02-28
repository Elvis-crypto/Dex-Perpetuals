# -*- coding: utf-8 -*-
"""
Created on Sun Jan 08 2023

@author: Elvis Crypto
"""

# if __name__ == "__main__":
#     import os
    
#     os.chdir('C:\\Crypto_Analysis\\PalmSwap\\derivatives-dashboard\\heroku')
#     protocol2Loader = {
#         'GMX':'..\\tables\\gmx.csv',
#         'dYdX':'..\\tables\\dydx.csv',
#         'Perpetual Protocol':'..\\tables\\perpetual-protocol.csv',
#         'ApolloX':'..\\tables\\apollox.csv'
#         }

from functions.sources import checkDatasets, protocol2Loader, readJson, FS2Loader
from functions.readLlama import readMultiLlama
from functions.str_panels import tSeriesLlamaBreakdown
from functions.processLlama import processLlamaIndiv
import streamlit as st
import plost
import altair as alt


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Sidebar stuff
st.sidebar.header('DeFi Perpetuals Dashboard ')

st.sidebar.markdown('''
    ---
''')
st.sidebar.subheader('''
🗝️ Key takeaways 🗝️
''')


# st.sidebar.markdown('''
# GMX, the dominant player in the space by TVL has around 40% of it's TVL in GMX tokens staked mostly on arbitrum. While their USDC TVL from their business is increasing this proportion is still very high compared to dYdX or Perpetual Protocol
# ''')

st.sidebar.markdown('''
---
Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
---
Data📊 by [DefiLlama](https://defillama.com/).
''')   

test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total = readMultiLlama(protocol2Loader)
processed = processLlamaIndiv(test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total)
# prices_df = readFSjson(FS2Loader['prices'])


st.markdown(f'''
Total Perpetuals TVL and protocol Market shares
---
''')


tSeriesLlamaBreakdown(Category='Protocol', series_df=processed['test_Total'], isSubTotal=True)
tSeriesLlamaBreakdown(Category='Currency', series_df=processed['test_all'], isSubTotal=False)
# tSeriesLlamaBreakdown(Category='Currency', series_df=processed['test_all'], isSubTotal=False, isStaking=True)
# tSeriesLlamaBreakdown(Category='Origin', series_df=processed['test_all'], isSubTotal=False, isStaking=True)
tSeriesLlamaBreakdown(Category='Protocol', series_df=processed['test_all'], isSubTotal=False, isStaking=True)

# st.markdown(f'''
# This is a test, remove from production:
# ---
# ''')
# tSeriesLlamaBreakdown(Category='Protocol', series_df=processed['test_Total'], isSubTotal=True, price_df=prices_df, compareToken='bitcoin')