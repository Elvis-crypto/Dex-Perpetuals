# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 2023

@author: Elvis Crypto
"""

if(__name__ == "__main__"):
    import os
    os.chdir('C:/Crypto_Analysis/PalmSwap/derivatives-dashboard/heroku')
    protocol2Loader = {
        'GMX':'../tables/gmx.csv',
        'dYdX':'../tables/dydx.csv',
        'Perpetual Protocol':'../tables/perpetual-protocol.csv',
        'ApolloX':'../tables/apollox.csv'
        }

import streamlit as st
#import plost
#import altair as alt


def article():
    from functions.sources import protocol2Loader#, readJson, FS2Loader
    from functions.readLlama import readMultiLlama
    from functions.str_panels import tSeriesLlamaBreakdown
    from functions.processLlama import processLlamaIndiv
    
    test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total = readMultiLlama(protocol2Loader)
    processed = processLlamaIndiv(test_all, test_origin, test_Total, test_Llama_TVL_Currency, test_Llama_TVL_Total)
    # prices_df = readFSjson(FS2Loader['prices'])
    
    
    st.markdown('''
                # Perpetuals in Crypto and DeFi
                ---
                #### A Brief History 
                Perpetuals have been reported to be origins of the next wave of [innovation and growth](https://beincrypto.com/defi-and-crypto-options-breaking-out-in-2023-says-report/) 
                in Decentralized Finance (DeFi), but what are they?   
                Perpetuals allow users to take a leveraged positions (up to 150x leveraged) on an asset while
                posting collateral. They have existed in traditional finance since the early 90s. Their 
                full name is perpetual futures contracts - since they are a special type of futures contract,
                one that never gets settled. A traditional futures contract allows traders to fix the price of
                a stock or a commodity in advance to be settled on a set expiration date. This has been useful 
                for both hedging against price swings and for speculation on the future price. As the expiration
                date draws closer the price of a futures contract inevitably converges with the market price of
                the asset, so traders who would want to keep a bet going have to get out of their futures contract
                and purchase new ones in time. [Perpetual futures contracts](/Key_Protocols_&_Concepts#perpetual-futures-contract) - as their name suggests - don't have 
                an obligatory settlement date and make this process much simpler. What keeps their price tethered
                to the underlying asset's price instead is their funding rate. As they are bought on the margin
                (with borrowed money against posted collateral), the funding rate is comprised of two parts, the 
                borrowing rate and premium rate. The premium rate is paid by the contract buyers (long positions)
                to the contract sellers (short positions) if the contract's market price is above underlying asset's
                index price and the other way-around if the market price is below the index price. The premium 
                rate reflects the risk of holding the position.
                
                Perpetuals have first been introduced to the crypto-space in 2016 by BitMex and have soon spread to
                all the major centralised exchanges (CEXs). Most of the outstanding interest in the space has
                been on BTC and ETH contracts.  
                As perpetuals are traded on the margin and often with very high leverage, the processing speed
                of market and index prices by the exchange can determine the fate of positions in volatile
                market conditions. This does not pose a limitation for CEXs as both 
                prices are 'in-house' on their servers, however until recently block execution times posed the
                major obstacle to the proliferation of perpetuals in DeFi.
                
                #### Perpetuals in DeFi
                Different protocols operating partially or fully on-chain adapted to the challenge with different
                approaches. [dYdX](/Key_Protocols_&_Concepts#dydx), one of the first partially on-chain exchanges opted for a hybrid method, settling 
                funds on-chain, but keeping the time sensitive order book matching off-chain. dYdX operates on Ethereum.
                [ApolloX](/Key_Protocols_&_Concepts#apollox) is new exchange on the Binance Smart Chain (BSC) operating with a similar hybrid principle,
                but leveraging the much shorter block-time of BSC (BSC has a 3 sec block-time while ethereum has 13.7 block-time on average).
                The [Perpetual Protocol](/Key_Protocols_&_Concepts#perpetual-protocol) introduced the concept of virtual Automated Market Makers ([vAMM](/Key_Protocols_&_Concepts#vamm))
                on the Optimism Layer2 rollup of Ethereum. The pool concept allows for fully decentralized settling and 
                execution of perpetual contracts trading, eliminating the need for an order book and an explicit counter
                party. [GMX](/Key_Protocols_&_Concepts#perpetual-protocol) is also a fully decentralized protocol operating on Arbitrum and Avalanche that enables
                perpetual margin trading against a large pool of assets and entering positions without the risk of price
                slippage. The protocol achieves this by avoiding the creation of a contract market and evaluating positions
                purely based on price feeds.   
                We will analyse the relative market position of these 4 protocols based on their Total Value Locked (TVL)
                as retrieved from [DefiLlama](https://defillama.com/).
                '''
        )
    
    # tSeriesLlamaBreakdown(Category='Protocol', series_df=processed['test_Total'], isSubTotal=True, price_df=prices_df, compareToken='bitcoin')
    tSeriesLlamaBreakdown(Category='Protocol', series_df=processed['test_Total'], isSubTotal=True)
    
    st.markdown('''
                The collective growth of the 4 perpetual trading DEXs have broadly followed the price of Bitcoin and
                the change in market capitalization of the broader crypto market. Between November 2020 and February
                2021 the price of BTC had risen from 18,000 to 56,000 USD. In the same period dYdX increased its TVL 
                from 38 M USD to 230 M USD. When BTC revisited the 30,000 range in May dYdX's TVL also shrank to 140 
                M USD. Once BTC took off again in July, the DeFi perpetual market cap also doubled again, this time
                due to the Perpetual Protocol, which reached 260 M USD in TVL in merely 20 days. By the end of August
                Perpetual Protocols TVL had reached 546 M USD, while BTC had recaptured the range between 40 and 50,000 USD.
                Growth through September continued to be explosive with GMX blowing up from nothing to 127 M USD in just
                3 weeks. Starting in August dYdX also started increasing it's TVL, after the successful launch of the 
                dYdX token the protocol more than doubled its TVL by the end of September. After holding a trading 
                competition for with a price pool of 250,000 USD at the end of September dYdX rocketed to over a Billion
                USD in TVL by the end of October. As it later turned out this was the highest point of the bull run both for
                DEX perpetuals and crypto-market as a whole. The 3 DEXs together constituted nearly 2 billion in total
                locked funds at the turn of November 2021. Bitcoin has entered a bear-market trend after November, 
                holding the 40,000 USD support until the Terra-Luna collapse in May 2022. The value of the DEX perpetuals
                market continued sideways in this period with dYdX holding it's TVL value, the Perpetual Protocol
                continually losing and GMX gaining market share. GMX's growth in April was strong enough to produce a
                new peak for the perpetual aggregate DEX market. The real shift in positions occured after the Terra-
                Luna collapse. While all market participants lost value in May, GMX has rebounded quickly managing to grow
                its TVL despite the bearish conditions. dYdX keeps slowly losing market share since May, while the 
                Perpetuals Protocol, which once commanded over 50% of DEX perpetuals market, is now fading into obscurity.
                ApolloX, while managing to grow it's assets since the end of 2021, could not push past 2-3% market
                share due to the strong competition from GMX.   
                As of January 2023 GMX has become the dominant decentralized trading platform with 65% TVL market share
                , while dYdX has retained 31%. The rest of the decentralized exchanges with perpetual products 
                (not all of them were shown in this analysis) retain a few 10s of millions USD in controlled funds.
                
                ''')
                
    st.sidebar.markdown('''
        ---
    ''')
    st.sidebar.subheader('''
    🗝️ Key takeaways 🗝️
      * The decentralized market for perpetual contracts trading controls over a billion USD in locked funds (it has come a very long way in 2 years), while protocols are entering with key innovations
      * The TVL of Perpetual DEXs broadly followed the general trend of bitcoin's price and the crypto market cap, but the perpetual exchanges have retained a much larger proportion of their capital in the bear-market than crypto in general.
      * GMX, the largest Perpetual DEX, continues to grow and attract liquidity. As of January 2023 it controls aprx. 2/3s of the decentralized perpetuals market.
      * dYdX, the largest Perpetual DEX during the bull-market, has lost it's near 2/3 market share after the Terra-Luna collapse in May and have gradually converged to a 1/3 market share in terms of controlled value.
    ''')
    st.sidebar.markdown('''
                        ---
                        Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
                        ''')   

if(__name__ == "__main__"):
    article()