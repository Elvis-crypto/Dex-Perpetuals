# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 2023

@author: Elvis Crypto
"""

from functions.sources import checkDatasets, protocol2Loader
import pandas as pd
from pandasql import sqldf

def processLlamaIndiv(test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total):
    arguments = locals()
    processed = arguments.copy()
    
    q1 = """ SELECT T.Date, L.Category, L.Protocol, T.TVL as 'TVL_summed', L.TVL as 'TVL_Llama'
              FROM test_Total T LEFT OUTER JOIN test_Llama_TVL_Total L USING (Date)
              """

    processed['test_both'] = sqldf(q1)
    
    q2 = """ SELECT T.Date, L.Category, L.Protocol, T.TVL*0.98 as 'TVL_noStaking_shifted2prtc', L.TVL as 'TVL_Llama'
              FROM (
                SELECT Date, Category, Protocol, sum(TVL) as TVL
                  FROM test_origin 
                    WHERE Origin not like '%staking%'
                  GROUP BY 1,2,3
              ) T          
              LEFT OUTER JOIN test_Llama_TVL_Total L USING (Date)
              """
    processed['test_bothNoStake'] = sqldf(q2)
    
    return processed

def paneltseriesLlamaSQL(Category, series_df, isSubTotal, isStaking=False, price_df=None, compareToken=None):
    
    
    if(isSubTotal):
        tSeries_df = series_df
    else:
        if (isStaking):
            q1 = f""" SELECT Date, {Category}, sum("Tokens(USD)") as TVL
                        FROM series_df
                          WHERE Origin LIKE '%-staking'
                        GROUP BY 1,2
                       """
        else:
            q1 = f""" SELECT Date, {Category}, sum("Tokens(USD)") as TVL
                        FROM series_df
                        GROUP BY 1,2
                       """
        tSeries_df = sqldf(q1)
        
    if(isinstance(price_df, pd.DataFrame)):
        qjoin = f""" SELECT T.*,P.price
                       FROM tSeries_df T LEFT OUTER JOIN price_df P ON T.Date = date(P.Date)
                         WHERE P.ID = '{compareToken}'
                       ORDER BY T.DATE
                    """
        tSeries_df = sqldf(qjoin)
    
    q2 = """ SELECT Date, sum(TVL) as TVL
                FROM tSeries_df
                GROUP BY 1
               """
    total_df = sqldf(q2)
    
    if(isSubTotal):
        q3 = f""" SELECT {Category}, AVG(TVL) as TVL
                   FROM series_df, (SELECT max(Date) as maxdate FROM series_df)
                     WHERE Date > date(maxdate, '-7 day')
                   GROUP BY 1
                  """
    else:
        if (isStaking):
            q3 = f""" SELECT {Category}, AVG("Tokens(USD)") as TVL
                       FROM series_df, (SELECT max(Date) as maxdate FROM series_df)
                         WHERE Date > date(maxdate, '-7 day')
                           AND Origin like '%staking%'
                       GROUP BY 1
                      """
        else:
            q3 = f""" SELECT {Category}, AVG("Tokens(USD)") as TVL
                       FROM series_df, (SELECT max(Date) as maxdate FROM series_df)
                         WHERE Date > date(maxdate, '-7 day')
                       GROUP BY 1
                      """
    lastTVL = sqldf(q3)
    
    if(isSubTotal):
        q4 = f""" SELECT wk, {Category}, TVL - LAG(TVL) OVER (PARTITION BY {Category} ORDER BY wk) AS TVL_change
                  FROM (
                    SELECT date(strftime('%s', Date) - 86400 * ((strftime('%w', Date) + 6) % 7), 'unixepoch') as wk, {Category}, AVG(TVL) as TVL
                      FROM series_df
                      GROUP BY 1,2
                    )
                  """
    else:
        if(isStaking):
            q4 = f""" SELECT wk, {Category}, TVL - LAG(TVL) OVER (PARTITION BY {Category} ORDER BY wk) AS TVL_change
                      FROM (
                        SELECT date(strftime('%s', Date) - 86400 * ((strftime('%w', Date) + 6) % 7), 'unixepoch') as wk, {Category}, AVG("Tokens(USD)") as TVL
                          FROM series_df
                            WHERE Origin like '%staking%'
                          GROUP BY 1,2
                        )
                      """
        else:
            q4 = f""" SELECT wk, {Category}, TVL - LAG(TVL) OVER (PARTITION BY {Category} ORDER BY wk) AS TVL_change
                      FROM (
                        SELECT date(strftime('%s', Date) - 86400 * ((strftime('%w', Date) + 6) % 7), 'unixepoch') as wk, {Category}, AVG("Tokens(USD)") as TVL
                          FROM series_df
                          GROUP BY 1,2
                        )
                      """
                  
    wOw = sqldf(q4)
    q4p1 = """ SELECT T.Date, T.TVL, W.*
                 FROM total_df T LEFT JOIN wOw W ON T.Date = W.wk

    """
    wOw_expanded = sqldf(q4p1)
    wOw_expanded.dropna(inplace=True)
    
    return tSeries_df, lastTVL, wOw_expanded

def paneltseriesSQL2(AggCol, Col2Sum, OutName, series_df, isSubTotal, isStaking=False):
    pass