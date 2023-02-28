# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 2023

@author: Elvis Crypto
"""


import pandas as pd
from datetime import datetime
from pandasql import sqldf


# Correctional measures on the data
def correctLlama(df):
    def copyHeader(df_header, idx):
        header_temp = df_header.iloc[:,idx]
        return header_temp
    
    corr = df.copy()
    protocol = df.columns[1]
    df_body = df.iloc[5:,1:].copy()
    df_header = df.iloc[0:4,:].copy()
    df_body = df_body.astype(float)
    df_body.insert(0,'dummy',0)
    df_body = df_body.fillna(0)
    if(protocol=='Perpetual Protocol'):
        # Total staking is ethereum-staking but more complete
        corr.iloc[5:,2] = corr.iloc[5:,4]
        corr.iloc[5:,6] = corr.iloc[5:,8]
        corr.iloc[5:,10] = corr.iloc[5:,12]
        # Should be TVL on ETH not in staking (in USDC)
        offs=0
        value = df_body.iloc[:,3] - df_body.iloc[:,1]
        header = copyHeader(df_header, 3)
        header[1] = 'ethereum'
        value_ins = pd.concat([header,value], axis=0)
        corr.insert(2+offs,'Inserted1',value_ins)
        offs+=1
        
        header = copyHeader(df_header, 7)
        header[1] = 'ethereum'
        value_ins = pd.concat([header,value], axis=0)
        corr.insert(6+offs,'Inserted2',value_ins)
        offs+=1
        
        header = copyHeader(df_header, 11)
        header[1] = 'ethereum'
        value = df_body.iloc[:,11] - df_body.iloc[:,9]
        value_ins = pd.concat([header,value], axis=0)
        corr.insert(10+offs,'Inserted3',value_ins)
        offs+=1
    elif(protocol=='ApolloX'):
        # This is mostly fine except for some unncessary duplicates cols
        # corr.drop(columns=corr.columns[[3,6,13,14,29,30]],inplace=True)
        corr.drop(columns=corr.columns[[4,8,25,26,61,62]],inplace=True)
    elif(protocol=='dYdX'):
        # total same as ethereum where exists
        corr.iloc[5:,1] = corr.iloc[5:,2]
    return corr

# Read the data
def readLlama(url):
#    pysqldf = lambda q: sqldf(q, globals())
    
#    df = pd.read_csv(url, parse_dates=['Date'],dayfirst=True)
    df = pd.read_csv(url)
    df.drop(['Unnamed: 0','Timestamp'], axis=1, inplace = True)
    df = correctLlama(df)
#    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d %H:%M:%S.%f')
#    df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
    header = df.iloc[0:4,1:]
    body = df.iloc[4:,1:]
    body = body.astype(float).round(1)
    dates = df.iloc[4:,:1]
    dates['Date'] = dates['Date'].apply(lambda x: datetime.strptime(x,'%d/%m/%Y').date())
    new_set = []
    Llama_set =[]
    for column_name in header.iloc[2,:].unique():
        # Get columns indexes column name applies
        selected_cols = header.iloc[2,:] == column_name
        subheader = header.loc[:,selected_cols]
        subbody = body.loc[:,selected_cols]
        new_tall = pd.DataFrame(columns=['Date',column_name])
        new_Llama = pd.DataFrame(columns=['Date',column_name])
        # Stack all existing combos of 1,3 row
        for origin_idx in range(len(subheader.iloc[1,:])):
            origin = subheader.iloc[1,origin_idx]
            currency = subheader.iloc[3,origin_idx]
            new_df = pd.DataFrame(data=pd.concat([dates,subbody.iloc[:,origin_idx]], axis=1).rename(columns={subbody.columns[origin_idx]:column_name}))
            new_df['Currency'] = currency
            #if '-' not in origin:
            if 'Total' != origin: # This is not a Llama total
                new_df['Origin'] = origin
                new_tall = pd.concat([new_tall,new_df],ignore_index=True)
                new_tall['Category'] = header.iloc[0,0]
                new_tall['Protocol'] = header.columns[0]
            else: # This is a Llama Total
                new_Llama = pd.concat([new_Llama,new_df],ignore_index=True)
                new_Llama['Origin'] = 'NULL'
                new_Llama['Category'] = header.iloc[0,0]
                new_Llama['Protocol'] = header.columns[0]
        new_set.append(new_tall)
        Llama_set.append(new_Llama)
    q1 = """ SELECT *
              FROM df3 NATURAL LEFT OUTER JOIN df2
                WHERE Origin <> 'staking'
              """
    df1 = new_set[0]
    df1.drop('Currency', axis=1,inplace=True)
    df2 = new_set[1]
    df3 = new_set[2]
    TVL_all = sqldf(q1)
    TVL_origin = df1[df1['Origin']!='staking']
    q2 = """ SELECT Date, Protocol, sum(TVL) as TVL
              FROM df1
                WHERE Origin <> 'staking'
              GROUP BY Date
              """
    TVL_Total = sqldf(q2)
    Llama_TVL_Total = Llama_set[0]
    Llama_TVL_Total.drop('Currency', axis=1,inplace=True)
    df2 = Llama_set[1]
    df3 = Llama_set[2]
    Llama_TVL_Currency = sqldf(q1)
    Llama_TVL_Currency['Category'] = header.iloc[0,0]
    Llama_TVL_Currency['Protocol'] = header.columns[0]
    return TVL_all, TVL_origin, TVL_Total, Llama_TVL_Currency, Llama_TVL_Total

def readMultiLlama(protocol2Loader):
    isFirstKey = True
    for protocol, source in protocol2Loader.items():
        if(isFirstKey):
            out_all, out_origin, out_Total, out_Llama_TVL_Currency, out_Llama_TVL_Total = readLlama(source)
            isFirstKey = False
        else:
            test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total = readLlama(source)
            out_all = pd.concat([out_all,test_all],ignore_index=True)
            out_origin = pd.concat([out_origin,test_origin],ignore_index=True)
            # q2 = """ SELECT * FROM out_origin
            #          UNION ALL
            #          SELECT * FROM test_origin
            #           """
            # out_origin = sqldf(q2)
            out_Total = pd.concat([out_Total,test_Total],ignore_index=True)
            out_Llama_TVL_Currency = pd.concat([out_Llama_TVL_Currency,test_Llama_TVL_Currency],ignore_index=True)
            out_Llama_TVL_Total = pd.concat([out_Llama_TVL_Total,test_Llama_TVL_Total],ignore_index=True)
    
    return out_all, out_origin, out_Total, out_Llama_TVL_Currency, out_Llama_TVL_Total

if __name__ == "__main__":
    pass
