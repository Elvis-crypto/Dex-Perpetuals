# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 2023

@author: Elvis Crypto
"""

import streamlit as st
import plost
import altair as alt
import pandas as pd
from functions.processLlama import paneltseriesLlamaSQL

def tSeriesLlamaBreakdown(Category, series_df, isSubTotal, isStaking=False, price_df=None, compareToken=None):
    tSeries_df, lastTVL, wOw_expanded = paneltseriesLlamaSQL(Category, series_df, isSubTotal, isStaking, price_df, compareToken)
    
    if(isStaking):
        AggLevel='Staking'
    else:
        AggLevel='TVL'
    
    st.markdown(f'''
    ---
    #### {AggLevel} breakdown by {Category}
    ''')
    if(tSeries_df.empty):
        st.markdown('''
        #### No Data
        ''')
    else:
        c1, c2 = st.columns((7,3))
        with c1:
            st.markdown(f'''
            ---
            #### {AggLevel} vs Time Composition by {Category}
            ''')
            if(isinstance(price_df, pd.DataFrame)):
                base = alt.Chart(tSeries_df).encode(
                    alt.X('Date:T', axis=alt.Axis(title=None))
                )
            
                line = base.mark_line().encode(
                    y=alt.Y('PRICE:Q',axis=alt.Axis(title=f'''{compareToken} price ($)''')),
                ).interactive()
                
                area = base.mark_area().encode(
                    alt.Y('TVL:Q',axis=alt.Axis(title='TVL ($)')),
                    color=Category+':N'
                ).interactive()
                
                
                c=alt.layer(area,line).resolve_scale(
                    y='independent'
                    )
                st.altair_chart(c, use_container_width=True)
            else:
                plost.area_chart(
                    tSeries_df,
                    x='Date:T',
                    y='TVL:Q',
                    color=Category,
                    stack=True,
                    height=400,
                    legend=None,
                    # title=series_df['Protocol'][0],
                    pan_zoom='both'  # 👈 This is magic!
                    )
        
        with c2:
            st.markdown('''
            ---
            #### Current Composition
            ''')
            plost.donut_chart(
                lastTVL,
                theta='TVL',
                color=Category
                )
        
        base = alt.Chart(wOw_expanded).encode(
            alt.X('Date:T', axis=alt.Axis(title=None))
        )
    
        line = base.mark_line().encode(
            y=alt.Y('TVL:Q',axis=alt.Axis(title='TVL')),
            color=alt.value('#F2F2F2')
        ).interactive()
        
        bar = base.mark_bar().encode(
            alt.Y('sum(TVL_change):Q',axis=alt.Axis(title='TVL Change ($)')),
            color=alt.Color(Category, legend=None)
        ).interactive()
        
        
        c=alt.layer(bar,line).resolve_scale(
            y='independent'
            )
        
        c3, c4 = st.columns((5,5))
        with c3:
            st.markdown(f'''
            #### Week over week change of TVL by {Category} 
            ''')
            st.altair_chart(c, use_container_width=True)
        with c4:
            st.markdown(f'''
            #### %Wise composition of TVL by {Category}
            ''')
            plost.area_chart(
                tSeries_df,
                x='Date:T',
                y='TVL:Q',
                color=Category,
                stack='normalize',
                height=400,
                title=series_df['Protocol'][0],
                pan_zoom='both'  # 👈 This is magic!
                )
    pass