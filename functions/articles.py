# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2023

@author: Elvis Crypto
"""

import os

# if __name__ == "__main__":
#     os.chdir('C:/Crypto_Analysis/PalmSwap/derivatives-dashboard/heroku')

ImHome = os.path.exists('C:/Crypto_Analysis/PalmSwap/derivatives-dashboard/heroku')    
dst = './readDir/actArticle.py'
dst2 = '.\\readDir\\actArticle.py'



def get_files():
    ret_list = []
    for file in os.listdir('./articles'):
        if '.' in file:
            if (file.split('.')[1] == 'py'):
                ret_list.append('./articles/'+file)
    return ret_list

def getArticles():
    # returns a dict of the article Titles and their path
    artNums2Names = {}
    artNames2FNames = {}
    artNames2Paths = {}
    for file in get_files():
        artNum = file.split('_',maxsplit=1)[0].split('/A')[1]
        artName = file.split('_',maxsplit=1)[1].split('.py')[0].replace('_',' ')
        artFName = file.split('/',maxsplit=1)[1].split('.py')[0]
        artNums2Names[artNum] = artName
        artNames2FNames[artName] = artFName
        artNames2Paths[artName] = file
        
    return artNums2Names, artNames2Paths

def prepArticle(src):
    # src is the source path for the actual article's python file
    if(ImHome):
        src2 = src.replace('/','\\')
        if(os.path.exists(dst2)):
            print()
            print(f'''del {dst2}''')
            os.system(f'''del {dst2}''')
        print()
        print(f'''copy {src2} {dst2} /Y''')
        os.system(f'''copy {src2} {dst2} /Y''')
    else:
        os.system(f'''cp {src} {dst}''')

# if __name__ == "__main__":
#     print(getArticles())
#     src = 'C:/Crypto_Analysis/PalmSwap/derivatives-dashboard/heroku/articles/"A01_Perpetuals in Crypto and DeFi.py"'
#     prepArticle(src)
