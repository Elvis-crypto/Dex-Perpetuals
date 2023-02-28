# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 2023

@author: Elvis Crypto
"""

from functions.sources import checkDatasets, protocol2Loader
import pandas as pd
from pandasql import sqldf


def paneltseriesGeneralSQL(series_df, Category, col2Sum, outName):
        
    q1 = f""" SELECT Date, {Category}, sum("{col2Sum}") as outName
                FROM series_df
                GROUP BY 1,2
               """
    tSeries_df = sqldf(q1)
        
    q2 = """ SELECT Date, sum({outName}) as {outName}
                FROM tSeries_df
                GROUP BY 1
               """
    total_df = sqldf(q2)
    
    
    q3 = f""" SELECT {Category}, AVG(col2Sum) as {outName}
               FROM series_df, (SELECT max(Date) as maxdate FROM series_df)
                 WHERE Date > date(maxdate, '-7 day')
               GROUP BY 1
              """
    
    last_df = sqldf(q3)
    
    q4 = f""" SELECT wk, {Category}, {outName} - LAG({outName}) OVER (PARTITION BY {Category} ORDER BY wk) AS {outName}_change
              FROM (
                SELECT date(strftime('%s', Date) - 86400 * ((strftime('%w', Date) + 6) % 7), 'unixepoch') as wk, {Category}, AVG({col2Sum}) as {outName}
                  FROM series_df
                  GROUP BY 1,2
                )
              """
                  
    wOw = sqldf(q4)
    q4p1 = f""" SELECT T.Date, T.{outName}, W.*
                 FROM total_df T LEFT JOIN wOw W ON T.Date = W.wk

    """
    wOw_expanded = sqldf(q4p1)
    wOw_expanded.dropna(inplace=True)
    
    return tSeries_df, last_df, wOw_expanded

def stateCompSQL(state_df, Category, col2Sum, outName):
    q3 = f""" SELECT {Category}, SUM({col2Sum}) as "{outName}"
               FROM state_df
               GROUP BY 1
               ORDER BY 2 DESC
              """
    comp_df = sqldf(q3)
    return comp_df