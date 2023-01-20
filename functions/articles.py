# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2023

@author: Elvis Crypto
"""

import os
import glob

if __name__ == "__main__":
    os.chdir('C:\\Crypto_Analysis\\PalmSwap\\derivatives-dashboard\\heroku')
    

def getArticles():
    # returns a dict of the article Titles and their path
    artNums2Names = {}
    artNames2FNames = {}
    for file in glob.glob('articles\\A[0-9][0-9]_*.py'):
        artNum = file.split('_',maxsplit=1)[0].split('\\A')[1]
        artName = file.split('_',maxsplit=1)[1].split('.py')[0]
        artFName = file.split('\\',maxsplit=1)[1].split('.py')[0]
        artNums2Names[artNum] = artName
        artNames2FNames[artName] = artFName
        
    return artNums2Names, artNames2FNames

if __name__ == "__main__":
    getArticles()