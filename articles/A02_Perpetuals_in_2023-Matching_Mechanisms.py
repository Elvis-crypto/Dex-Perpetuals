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
                # Comparing the Crypto Perpetual markets in 2023 - Matching Mechanisms
                ---
                In this series of articles we are examining the markets offering perpetuals at the moment in crypto,
                both Centralized Exchanges (CEX) as well as Decentralized Exchanges (DEX).  
                In this section we will be looking at the mechanisms perpetual markets use to match buyer and seller orders
                or otherwise make assets (liquidity) available to facilitate trading.
                
                #### Overview
                
                [Perpetuals]((/Key_Protocols_&_Concepts#Perpetual)) are a special kind of futures contract that do not expire and there is no necessary
                settlement date assigned to them. They are used to get exposure to the price of an asset, often with
                high leverage, without owning the asset to either speculate on the price action or hedge against it.
                In most cases a perpetual contracts market is independent from the underlying indexed asset, meaning
                that trading moves the mark price of the contract independent from the indexed assets price. What 
                keeps the mark price moored to the index price, then? The funding rate of the contract. In almost all
                implementations of perpetuals holders of the contracts (longs) pay a fee periodically to the sellers
                of the contract (shorts) *if* the index price is above the mark price, in proportion to the difference.
                However, if the mark price is below the index price, it goes the other way around, shorts pay longs.
                This mechanism ensures, that the mark and index prices stay close as the majority sides positions continualy
                lose some value to the majority.
                
                #### How do exchanges make trades happen in DeFi and CeFi crypto perp trading?
                
                Markets in crypto have devised several mechanism for matching the buyer and seller side of futures contracts
                as well as for providing liquidity for these trades.   
                
                ##### The 3 main approaches
                
                **Order books**
                
                The classical mechanism for matching trades in either the spot or the futures market is using order books.
                Order books record the unmatched bid and ask orders of market makers. Market orders are executed against 
                these offers. While anyone can provide liquidity, exchanges use bots or external companies to ensure some 
                liquidity is provided for trading near the last price. The advantage of order book based systems is that
                they provide some transparency for the buyers and sellers intentions on the market. The disadvantage is
                that it requires the participation of at least one active market maker with substantial liquidity.
                Failing this, the price of the asset would become volatile with very large breakouts, resulting in mass 
                liquidations on one side or the other. Centralized exchanges and hybrid DEXes such as [dYdX](/Key_Protocols_&_Concepts#dydx), [ApolloX](/Key_Protocols_&_Concepts#apollox) and ApolloX forks
                rely on server based matching engines to implement order book based trading. This results in quick and cheap execution
                and competitive fees at the cost of centralization. Most DeFi protocols allow limit orders to be placed on-chain,
                but need keeper bots to submit the limit orders as market orders (they do not provide liquidity), liquidity and order
                matching is provided by another mechanism of the protocol.
                
                **Automated Market Makers ([AMM](/Key_Protocols_&_Concepts#amm)s)**
                
                AMMs are smart contracts exchanging two or more assets in a pool 
                with a formula constraining the trade, most commonly, the constant product formula. This mechanism
                enables the decentralized, permissionless creation of markets for any asset even with low liquidity.
                The issue with the simple concept of AMMs is slippage, the movement of the offered price due to prior
                transactions in the same block.
                
                **Virtual AMMs ([vAMM](/Key_Protocols_&_Concepts#vamm)s)**
                                       
                Virtual AMMs trade tokens isolated from the rest of the crypto ecosystem, minted and 
                traded only by their contract. vAMMs were used in the original implementation of perpetuals in DeFi,
                the v1 [Perpetual Protocol](/Key_Protocols_&_Concepts#perpetual-protocol). A trader would deposit collateral in the protocol pool and mint virtual tokens with
                a fixed leverage to enter a position by swapping with the vAMM. The system is also a classic AMM for 
                the collateral tokens, enabling swaps between the assets. Liquidity providers may deposit funds to the protocol
                pool and receive income from swaps as well as act as a counterparty to the traders, because the virtual tokens are
                redeemable form the pool. When traders win, the pool loses funds and vica versa. The business model relies on
                the observation that over time and on average, traders lose.   
                **v2 of Perpetual Protocol** relies on Uniswap v3 to manage pools for the virtual tokens.
                Uniswap v3 allows for concentrating liquidity in specified price ranges instead of accepting the
                pools composition for the provided tokens. This feature introduces the role of makers to the protocol
                allowing some traders to provide liquidity in the virtual pool. Besides [Perpetual protocol](/Key_Protocols_&_Concepts#perpetual-protocol), [Rage trade](/Key_Protocols_&_Concepts#rage-trade) and [Drift protocol](/Key_Protocols_&_Concepts#drift-protocol)
                also uses the vAMM concept for providing liquidity.   
                The upside of vAMMs is that they realise a floating priced market for the perpetual contracts,
                allowing funding rates to flow as the mark price moves relative to the index price. The downside is that
                large orders may create significant volatility in the mark price. Furthermore they rely on feedback
                mechanism to adjust the mark price to the index price, which is necessarily delayed.
                
                **GMX style AMMs** 
                
                A different concept AMMs was pioneered by [GMX](/Key_Protocols_&_Concepts#gmx). They retained the aspect of pooling collateral
                in an AMM swap pool, however there is no floating market created for contracts. Instead when a trader 
                enters a deposits collateral it's current USD value will be recorded by the contract. The trader can
                then take a leveraged position (recorded by the contract on-chain) without buying anything and hence without
                any price impact. With this construct there is no funding payment, however traders still need to pay
                a fee for the funds they are using in the pool
                (funds get reserved to cover potential trade profits until the position is closed).  
                The positive aspect of this approach is that it avoids large trades having price impacts and potential
                frontrunning of these orders. On the other hand as there are no funding payments this type of contract
                cannot be used for hedging positions with a profit (delta neutral hedging strategies).  
                The GMX type of perpetuals got enormously popular and have been replicated on all chains with many
                variations. Besides [GMX](/Key_Protocols_&_Concepts#gmx), [MUX](/Key_Protocols_&_Concepts#mux-protocol-formerly-mcdex), [Gains Network](/Key_Protocols_&_Concepts#gains-protocol), [Mummy Finance](/Key_Protocols_&_Concepts#mummy-finance), [MetaVault](/Key_Protocols_&_Concepts#metavault-trade), [OPX](/Key_Protocols_&_Concepts#opx), [Mycelium](/Key_Protocols_&_Concepts#mycellium-perpetual-swaps) and [Level Finance](/Key_Protocols_&_Concepts#level-finance)
                also uses this approach.
                ''')
                
    st.image('./Images/MatchMechanisms.png')
                
    st.markdown('''
                ##### Proactive Market Makers
                
                The main problem with classic and virtual AMMs as well as orderbook based exchanges is that they require trading to
                update their mark price. This is inefficient from the liquidity providers point of view as they have to pay
                arbitragers profit for the information. UniSwap v3 type pools have ameliorated the problem by allowing 
                liquidity providers to concentrate and target their liquidity in select price ranges. An alternative
                way for incorporating the price information is to establish a programmatic relationship between the mark price
                (and offered liquidity) and the index price. 
                
                **Deri Proactive Martket Maker (DPMM)** 
                
                [Deri protocol](/Key_Protocols_&_Concepts#deri-protocol) represents a special case for several reasons. While they offer everlasting options and
                specially priced power perpetuals, the underlying matching mechanism is also a special kind of vAMM that
                takes into account the index price. The price increase for a given size purchase is proportional
                to the net long-short position of the pool. The coefficient of the linear relationship is a 
                function of pool liquidity and parameters. This model does not solely rely on external actors
                (arbitragers) to update the price like classical AMMs, but changes both the price and liquidity
                offered for trades based on the index price movement.   
                
                **AMM for simulated liquidity**
                
                [CAP Protocol](/Key_Protocols_&_Concepts#cap-protocol) uses a special vAMM that uses the quoted asset's index
                price as basis and offers a mid-market contract mark price skewed based on the long/short position
                skew at the platform. The available liquidity for bids and asks is modeled as two Gaussians with heights
                proportional to the position skew and center proportional to the quoted assets recent volatility.
                This mechanism allows for correcting the mark price of the contract without using funding fees
                (the simulated price impact corrects the mark price). The price skew may be advantageous to traders
                depending on the market conditions and pool's state and the size of the order they wish to execute.
                
                **Synthetic tokens**
                
                Both [Synthetix protocol](/Key_Protocols_&_Concepts#kwenta) and [handle.fi](/Key_Protocols_&_Concepts#handle-fi) enables the creation of synthetic tokens (crypto or forex synth tokens)
                based on overcollateralized loans (this step is similar to GMX as there is no price impact). 
                The created sUSD can be used in the Synthetix perpetual system as collateral to trade synth perpetuals,
                however matching and liquidity are provided by a vAMM that skews both the index price and the offered
                liquidity based on the position balance between longs and shorts. (Similar to DPMM). Synthetix created two
                similar frontend protocols to facilitate accessing their ecosystem, [Kwenta](/Key_Protocols_&_Concepts#kwenta) and [Decentrex](/Key_Protocols_&_Concepts#kwenta).
                [Handle.fi](/Key_Protocols_&_Concepts#handle-fi) on the other hand keeps synth and perpetual contract creation under the hood and offers
                exposure to the created synth forex perps with a GMX style AMM, without contract price impact or
                requiring a position balancing funding fee.                
                
                ##### Alternate Approaches
                
                **Frequent Batch Auctions**
                
                The [Helix protocol](/Key_Protocols_&_Concepts#helix-fromerly-injective) built on top of the Injective blockchain was created to
                facilitate auction trading. In every block (~2.5 seconds) orders are executed in two phases: First,
                market orders are executed at a uniform price, based on the previously existing limit orders. Second,
                new limit orders are matched against each other and executed at uniform price. New limit orders are
                sealed, the offers are only posted to the block-chain after a block auction is concluded. This approach
                removes the incentive for high frequency traders to frontrun market maker orders and allows market 
                makers to provide liquidity closer to the market price. The drawback of the method is that the real-time
                market price for assets does not exist, which may cause losses when market conditions are volatile.
                
                **Dutch Auctions** 
                
                An auction (held within 5 seconds on [Drift Protocol](/Key_Protocols_&_Concepts#drift-protocol) after submitting a market order),
                where market makers may bid on incoming market orders. The auction starts at the mid-market oracle
                index price (the best option for the taker) and ends with the guaranteed Drift vAMM price. This setup
                allows market makers to compete for orders without the risk of forerunning, incentivising them to
                provide liquidity close to the index price.
                                
                **Direct position realization**
                
                [FutureSwap](/Key_Protocols_&_Concepts#futureswap) enables users to directly realize a leveraged positions 
                by borrowing funds from their pool and creating overcollateralized long or short positions on Aave
                through flash loans. While this method doesn't involve the creation of a perpetual contract, it also allows
                for leveraged trading on crypto assets without a fixed settlement date. While this option avoids
                positional funding fees and isn't impacted by mark price volatility, it has to cover borrowing fees both with FutureSwap and Aave.
                Therefore realizing the position is achieved at a higher cost than with GMX style AMMs.
                
                #### Conclusion
                
                Perpetual futures contracts aggregate information on an assets future prospects more so than the spot market
                itself as there is no direct feedback to the spot price and the settlement currency is different from
                the quoted asset in most cases. The use of leverage precludes the sustainability of incorrect predictions.   
                Besides expectations of the future prospects of the indexed price, perpetual prices are also driven
                by a mechanism forcing the mark price to return to the index price. The listed methods differ in the
                way index price information is relayed to the mark price and the participants required to or allowed to
                profit from doing so. 
                  * vAMM type systems require arbitragers to correct the mark price toward the index price and pay a funding fee for taking the minority side. They also allow for higher volatility which may be desirable.
                  * GMX style AMMs directly fix the mark price to the index price cutting out the possibility for funding fees and mark-index volatility.
                  * Proactive vAMMs represent a middle ground, mixing position and index price information programmatically reducing, but not eliminating the opportunity for arbitrage and mark-index volatility
                ''')
                
    st.sidebar.markdown('''
        ---
    ''')
    st.sidebar.subheader('''
    🗝️ Key takeaways 🗝️
      * Perpetual implementations differ in index-to-mark price information flow
      * vAMM types rely on arbitragers to take the minority side, but allow for more mark-index volatility
      * GMX style AMMs eliminate both arbitrage and mark-index volatility by fixing the mark to the index price
      * Proactive vAMMs include the index price in the mark price, reducing but not eliminating arbitrage and mark-index volatility
    ''')
    st.sidebar.markdown('''
                        ---
                        Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
                        ''')   

if(__name__ == "__main__"):
    article()