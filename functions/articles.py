# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2023

@author: Elvis Crypto
"""

import os

if __name__ == "__main__":
    os.chdir('C:\\Crypto_Analysis\\PalmSwap\\derivatives-dashboard\\heroku')
    
dst = '.\\readDir\\actArticle.py'
ImHome = os.path.exists('C:\\Crypto_Analysis\\PalmSwap\\derivatives-dashboard\\heroku')


def get_files():
    ret_list = []
    for file in os.listdir('.\\articles'):
        if '.' in file:
            if (file.split('.')[1] == 'py'):
                ret_list.append('.\\articles\\'+file)
    return ret_list

def getArticles():
    # returns a dict of the article Titles and their path
    artNums2Names = {}
    artNames2FNames = {}
    artNames2Paths = {}
    for file in get_files():
        artNum = file.split('_',maxsplit=1)[0].split('\\A')[1]
        artName = file.split('_',maxsplit=1)[1].split('.py')[0]
        artFName = file.split('\\',maxsplit=1)[1].split('.py')[0]
        artNums2Names[artNum] = artName
        artNames2FNames[artName] = artFName
        artNames2Paths[artName] = file
        
    return artNums2Names, artNames2Paths

def prepArticle(src):
    # src is the source path for the actual article's python file
    if(ImHome):
        os.system(f'''copy {src} {dst}''')
    else:
        os.system(f'''cp {src} {dst}''')

if __name__ == "__main__":
    print(getArticles())