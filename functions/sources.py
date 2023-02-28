# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2023

@author: Elvis Crypto
"""

import os
from pathlib import Path
from datetime import datetime, timedelta
from time import sleep
import requests
from urllib.request import urlopen
import json
import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

class Source():
    def __init__(self):
        pass



protocol2Loader = {
    'GMX':'./tables/gmx.csv',
    'dYdX':'./tables/dydx.csv',
    'Perpetual Protocol':'./tables/perpetual-protocol.csv',
    'ApolloX':'./tables/apollox.csv'
    }
protocol2URL = {
    'GMX':'https://api.llama.fi/dataset/gmx.csv',
    'dYdX':'https://api.llama.fi/dataset/dydx.csv',
    'Perpetual Protocol':'https://api.llama.fi/dataset/perpetual-protocol.csv',
    'ApolloX':'https://api.llama.fi/dataset/apollox.csv'
    } 

FS2Loader = {
    'protocol':'Flipside',
    'prices':'./tables/prices.json'
    }

FS2URL = {
    'prices':f'''https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1606262400&to={round(datetime.now().timestamp())}'''
    }

Gecko2Loader = {
    'protocol':'CoinGecko',
    'queries':['derivatives_exchanges'],
    'url':{'derivatives_exchanges':None},
    'derivatives_exchanges':'./tables/cg_derivatives_exchanges.json',
    }


# Implementation of an API loader reloading underlying tables regularly
def APILoader(protocol,protocol2URL, protocol2Loader, reloadInterval):
    # protocol is actually the protocol for the DEX list, otherwise it refers to the kind of data we wish to
    # load from the data-provider
    filename = protocol2Loader[protocol]
    url = protocol2URL[protocol]
    # if current file is older than the interval...
    ending = filename.split('.')[2]
    fileExists = os.path.exists(filename)
    if(fileExists):
        ImOld = os.path.getmtime(filename) < datetime.timestamp(datetime.now()-timedelta(hours=reloadInterval))
    else:
        Path(filename).touch(exist_ok=True)
        ImOld = True
    if(not(fileExists) or ImOld):
        sleep(0.25)
        if(ending == 'csv'):
            req = requests.get(url)
            with open(filename, mode='wb') as csv_file:
                csv_file.write(req.content)
        elif(ending == 'json'):
            if(protocol2Loader['protocol']=='CoinGecko'):
                if(protocol == 'derivatives_exchanges'):
                    data_json = cg.get_derivatives_exchanges(per_page=100)
            else:
                headers = {'Accept': 'application/json'}
                response = requests.get(url,headers=headers)
                #Response returns empty except for the column names. Gecko likely sensitive to headers, it worked in browser
                data_json = response.json()
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_json, f, ensure_ascii=False, indent=4)
            

def checkDatasets(reloadInterval):
    for protocol in protocol2Loader:
        APILoader(protocol,protocol2URL, protocol2Loader, reloadInterval)
    # for query in FS2Loader:
    #     APILoader(query,FS2URL, FS2Loader, reloadInterval)
    for query in Gecko2Loader['queries']:
        APILoader(query, Gecko2Loader['url'] , Gecko2Loader, reloadInterval)

def readJson(url):
    df = pd.read_json(url)
    return df

def readCGDerivatives():
    df = pd.read_json(Gecko2Loader['derivatives_exchanges'])
    defi = pd.read_json('./tables/cg_derivatives_exchanges_defi.json')
    df_out = pd.merge(df,defi[['id','DeFi']],on='id')
    return df_out


if __name__ == "__main__":
    os.chdir('C:/Crypto_Analysis/PalmSwap/derivatives-dashboard/heroku')
    reloadInterval = 24
    for query in Gecko2Loader['queries']:
        APILoader(query,Gecko2Loader['url'], Gecko2Loader, reloadInterval)
    df_test = readJson(Gecko2Loader['derivatives_exchanges'])