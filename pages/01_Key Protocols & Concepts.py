    # -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 2023

@author: Elvis Crypto
"""

import streamlit as st
import plost
import altair as alt

st.set_page_config(page_title='Perpetuals platform',layout='wide', initial_sidebar_state='expanded')

# Sidebar stuff
st.sidebar.header('DeFi Perpetuals Concepts ')


st.sidebar.markdown('''
---
Created with ❤️ by [@Elv1s_Crypto](https://twitter.com/Elv1s_Crypto/).
''')   

st.markdown('''
            # Key Platforms & Concepts
            '''
    )

st.markdown('''
            ## Platforms
            '''
    )

st.markdown('''
            #### dYdX
            dYdX perpetuals offer synthetic exposure to a variety tokens and coins.
            They use on-chain settlement together with off-chain matching.
            The centralized order matching enables superior execution speed and efficiency, 
            transaction data, results and proofs are kept on-chain to guarantee security.
            dYdX replicates the trading logic used on CEXs (orders are executed in thier matching engine as soon as they are recieved)
            and they offer similar conditional orders (limit, stop-limit) orders as CEXs. The main difference
            to CEXs is the dYdX's non-custodial fund handling model.
            dYdX uses oracles prices that are updated several times per second off-chain and are verified
            via STARK signatures, allowing execution without waiting for blocks. Collateral and liquidation
            prices are determined by the oracles. Remaining collateral is diverted to a risk reserve 
            that is used in case an overloss occurs during liquidation. dYdX also uses an Auto-deleverage
            mechanism to reduce margins in case of extreme fluctuations when no counterparties can be matched.
            dYdX uses index prices genrated from a list of exchanges to trigger stop-losses in timely manner
            to protect traders.
            '''
    )

st.markdown('''
            #### ApolloX
            ApolloX is a CEX and DEX hybrid exchange with on-chain settlement and custody and off-chain matching
            enabling users to use up to 150x leverage. As of 2023 January they have announced that they are
            winding down the CEX exchange and will continue as a pure DEX. Launched in 2021 the exchange achieved over 158.8 Billion USD
            trading volume in 2022 May and recieved funding from Binance Labs in 2022 June. The platform 
            allows for trading in both the spot and futures markets using a traditional off-chain order-book matching system.
            Their expanding line of products include predict-to-earn and DEX-as-a-service. The affiliates
            using their DEX infrastructure retain up to [70% of fees earned](https://apollox.zendesk.com/hc/en-us/articles/4405482780185).
            
            '''
    )

st.markdown('''
            #### GMX
            GMX is a decentralized, permissionless perpetual swap and spot exchange on the Arbitrum and 
            Avalanche networks. It was first launched on Arbitrum in September, 2021 and expanded to 
            Avalanche in January 2022.
            GMX perpetuals utilise on-chain self-custody of funds and enable trading
            with up to 50x leverage. GMX uses Chainlink oracles for price indexing.
            GMX uses multi-asset pool called GLP to facilitate trading. The pool is comprised of 50-55%
            stable coins, 25% ETH, 20% BTC and 5-10% altcoins. Liquidity providers can provide assets to
            this pool and, while traders deposit collateral to this pool. Liquidity provider fees are weighted 
            to maintain the intended composition of the pool. When traders deposit collateral
            to open a position their margin is fixed in USDC to prevent their margin from losing value.
            When liquidity providers deposit funds to the GLP they recieve GLP tokens.
            The GLP holders recieve 70% of the collected platform fees as well as esGMX tokens as incentives (see below),
            however any profit traders may realize will also be funded by the GLP exposing liquidity
            providers to synthetic counterparty risk. GLP tokens can also be staked to increase for an interest.
            
            Perpetuals trading on GMX is different from other platforms in the sense, that it does not create
            an independent market for a synthetic asset (No premium component in the funding rate, just an hourly borrowing fee).
            Rather, GMX enables leveraged betting on the price of an asset, allowing entry into positions 
            without directly affecting the price or causing slippage. Feedback to the price of the underlying
            asset is achieved through the fee rebalancing mechanism of the vault.
            
            GMX uses a partial liquidation system trigerred when the value of the position (including borrowing costs and losses) falls below
            1% of the margin value. Any remaining collateral after liquidation is returned to the account.
                                                                                                  
            
            GMX has native token called GMX. The token has governance as well as value accrue utility, as
            the token can be staked to earn a protion of the platforms trading fees (30% is distributed to
            stakers). Furthermore GMX stakers earn escrowed GMX esGMX tokens. These can be either staked
            or vested over 12 months to release GMX. Lastly, staked GMX tokens also earn Multiplier points
            that boost yields in GLP for long term holders.
            
            '''
    )

st.markdown('''
            #### Perpetual Protocol
            Introduced the fully decentralized virtual Automatic Market Maker (vAMM) model instead
            of order matching. See vAMM.
            v2 of Perpetual Protocol: Leverages Uniswap v3 contracts to make the AMM 'real'.
            This iteration introduced the maker role, enabling traders to mint vTokens and provide
            liquidity in the pools. As Uniswap does not allow negative tokens, therefore short positions
            are issued vETH tokens (in case of a ETH/USDC perpetual).
            Perpetual Protocol uses the Chainlink price as the index price and as the clearing price
            during liquidation. Liquidation is executed by a keeper bot. 50% of the remaining collateral
            is retained by the liquidator and 50% is directed to the risk reserve. The risk reserve 
            is used to cover over losses accrued due to untimely liquidations during extreme market 
            volatility. Perpetual Protocols also monitors market prices through off-chain robots and these
            prices are used to trigger stop-losses in a timely manner.
            
            '''
    )

st.markdown('''
            #### Injective
            A decentralized trading platform with it's own blockchain built on Tendermint
            with a 2.5 sec average block time. One of Injective's products is perpetual contracts.
            It uses a type of pooled bidding called Frequent Batch Auctions (FBA) for order matching.
            In a block order cancellations and liquidations are immediately processed, but creation
            requests are added to a trade queue. Order matching starts at the end of each block.
            First market orders are executed at a uniform price. Second matchable limit orders are matched
            and are also executed at a uniform clearing price. Remaining limit orders are carried over to
            the next block. This system is not constrained by network throughput and prevents order
            front-running. On the negative, the real-time price does not exist until the end of each
            block. This is usually not a concern, but during large market fluctuations it may cause
            large losses.   
            Injective also uses Chainlink as it's price oracle and clearing price during liquidations. 
            Liquidtion is handled by a bot which retains 50% of the liquidated funds and diverts 50%
            to a risk reserve which is used to cover over losses that cannot be recovered by normal liquidations
            during times of extreme market conditions.
            '''
    )

# st.markdown('''
#             #### On-chain trading models
#             early: 0x protocol, off-chain RFQ model
#             now> vAMM model, dYdX off-chain match, on-chain settle (hybrid model),
#             entirely on-chain model (on-chain match, on-chain settle)
#             '''
#             )
st.markdown('''
            ## Concepts
            '''
    )

# st.markdown('''
#             #### TVL
            
            
#             '''
#     )

st.markdown('''
            #### DEX
            [Decentralized Exchange](https://chain.link/education-hub/what-is-decentralized-exchange-dex) A DEX (decentralized exchange) is a peer-to-peer marketplace where users can trade cryptocurrencies in a non-custodial manner without the need for an intermediary to facilitate the transfer and custody of funds. DEXs substitute intermediaries—traditionally, banks, brokers, payment processors, or other institutions—with blockchain-based smart contracts that facilitate the exchange of assets. 
            
            '''
    )

st.markdown('''
            #### CEX
            Centralized Exchange
            
            '''
    )

# st.markdown('''
#             #### Futures Contract
#             dex exchange
            
#             '''
#     )

st.markdown('''
            #### Perpetual Futures Contract
            A Futures contract that automatically rolls over with no set expiration date.   
            The concept was proposed in its popular form in a [1993 NBER working paper by Nobel laurate Shiller](https://www.nber.org/system/files/working_papers/t0131/t0131.pdf).   
            Crypto perpetuals (a BTC perpetual) were first introduced by BitMEX in 2016.   
            Perpetual contracts are anchored to the underlying index price via the **Funding Rate** of the contract.   
            Contracts may be either **linear contracts**, settled in stable coins or **inverse contracts** settled in a crypto asset.  
            While **inverse contracts** may be more convient to open positions infor crypto holders, they magnify the risk of liquidation for long positions.
            '''
    )

st.markdown('''
            #### Funding Rate (Perpetual Futures Contract)
            Perpetual contracts are anchored to the underlying index price via the funding rate of the contract.
            Most CEXs and DEXs use the following formula:   
            `Funding Rate = Interest Rate + Premium Rate`   
            Interest Rate is the cost of holding a leveraged position, usually the difference of borrowing rates of between the undelying currency pair.   
            The Premium rate represents the risk of holding the position. It is proportional to the difference between the index and contract prices.   
            If the contract price is above the index price, contract buyers (long positions) pay sellers (short positions) and the other way around if the   
            contract price is below the index price.
            Perpetual Protocol uses the FTX formula:   
            `Funding Rate = Premium Rate`
            
            '''
    )

st.markdown('''
            #### AMM
            Automated Market Maker: A key innovation of decentralized exchanges introduced by UniSwap in 2020,
            AMMs allow trading against a pool of tokens, instead of requiring a counter-party like an orderbook based exchange does.
            Tokens are pooled in pairs and the pools exchange rate is set by a formula, usually `x * y = k`, where `x` and `y` are the quantity of the tokens and `k` is a constant.
            AMMs rely on arbitrage traders to couple the AMMs price to the wider market.
            AMMs allow anyone to post liquidity for a pair of tokens and thus enables trading of assets
            which would not have sufficient liquidity to be traded otherwise. Shallow liquidity pools
            will result in large changes in price after large transactions. As transactions are most 
            often executed in blocks, this leads to uncertainity in the exhange price. The slipping in 
            price between the posting and execution of a swap order is called slippage.
            '''
    )

st.markdown('''
            #### vAMM
            virtual Automated Market Maker: Introduced by the Perpetual Protocol.  
             * vAMM: A virtual AMM of virtual tokens is created by the protocol (eg. vUSDC and vETH) using the classic AMM equation (`x * y = k`). When a trader deposits collateral it is deposited to a vault address, while the user address is credited with either positive (long position) or negative (short position) vUSDC tokens in proportion to the leverage the user chose to use. An AMM Swap is executed with the virtual tokens to enter or exit a position.   
            After some time in operation two problems became apparent:  
            1. The value ok `k` is static and cannot react to market conditions. Too low values lead to large slippage in swaps, while larger values would make following the index price harder.  
            2. There is no counterparty to the transactions to fund the Premium part of the Funding Rate. The Premium rate could only be funded from an insurance fund. Depletion of this fund would lead to instability.             
            
            '''
    )