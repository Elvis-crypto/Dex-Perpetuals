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
            ### [DEX](#dex)s
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
            enabling users to use up to 200x leverage. As of 2023 January they have announced that they are
            winding down the CEX exchange and will continue as a pure DEX. Launched in 2021 the exchange achieved over 158.8 Billion USD
            trading volume in 2022 May and recieved funding from Binance Labs in 2022 June. The platform 
            allows for trading in both the spot and futures markets using a traditional off-chain order-book matching system.
            They charge a competitive trading fee of 0.02% for makers and 0.07% for takers. 
            Their expanding line of products include predict-to-earn and DEX-as-a-service. The affiliates
            using their DEX infrastructure retain up to [70% of fees earned](https://apollox.zendesk.com/hc/en-us/articles/4405482780185).
            
            '''
    )

# st.markdown('''
#             #### PalmSwap
#             PalmSwap is a DEX on BSC with a two-tier product offer for Perpetuals. Building on ApolloX infrastucture
#             PalmSwap is a hybrid system with decentralized on-chain custody of funds and off-chain, orderbook based
#             order matching. The hybrid system became operational in 
            
#             '''
#     )


st.markdown('''
            #### GMX
            GMX is a decentralized, permissionless perpetual swap and spot exchange on the Arbitrum and 
            Avalanche networks. It was first launched on Arbitrum in September, 2021 and expanded to 
            Avalanche in January 2022.
            GMX perpetuals utilise on-chain self-custody of funds and enable trading
            with up to 50x leverage. GMX uses Chainlink oracles for price indexing.
            The protocol uses multi-asset pool called GLP to facilitate trading. The pool is comprised of 50-55%
            stable coins, 25% ETH, 20% BTC and 5-10% altcoins. Liquidity providers can provide assets to
            this pool and, while traders deposit collateral to this pool. Liquidity provider fees are weighted 
            to maintain the intended composition of the pool (swap fees range between 0.2-0.8%). When traders deposit collateral
            to open a position their margin is fixed in USDC to prevent their margin from losing value.
            When liquidity providers deposit funds to the GLP they recieve GLP tokens.
            The GLP holders recieve 70% of the collected platform fees as well as esGMX tokens as incentives (see below),
            however any profit traders may realize will also be funded by the GLP exposing liquidity
            providers to synthetic counterparty risk. GLP tokens can also be staked to further increase yields.
            Staking GLP is possible with the platforms own staking contract or with external protocols as well.
            
            Perpetuals trading on GMX is different from many other platforms in the sense, that it does not create
            an independent market for a synthetic asset (No premium component in the funding rate, just an hourly borrowing fee).
            Rather, GMX enables leveraged betting on the price of an asset, allowing entry into positions 
            without directly affecting the price or causing slippage. Feedback to the price of the underlying
            asset is achieved through the fee rebalancing mechanism of the vault, meaning that fees for swaps and
            deposits that reduce imbalance are lowered and fees for operations that increase it are increased.
            
            Trading is possible with market and limit orders, with limit orders being posted on-chain and being 
            executed by keeper bots. Payment for such execution neccesitates a fee for these bots. Managing risk
            by using take profit/ stop loss orders is possible, but only after a position is already taken.
            Openening or closing a position incurs a 0.1% trading fee and maintaining it maximum of 0.01%/hour
            borrowing fee paid in proportion to the amount of assets a trader borrowed for his position relative
            to the amount of those assets in the GLP pool. Trading profit is payed in the same asset as being 
            traded for long and in stable coins for shorts. If the inappropriate collateral is posted it will
            be converted using the GMXs relevant swap fees (0.2-0.8%).
            
            GMX uses a partial liquidation system trigerred when the value of the position (including borrowing costs and losses) falls below
            1% of the margin value. Any remaining collateral after liquidation is returned to the account.
                                                                                                  
            GMX has native token called GMX. The token is used in governance as well as utility value, as
            the token can be staked to earn a protion of the platforms trading fees (30% is distributed to
            stakers as ETH or AVAX). Furthermore GMX stakers earn escrowed GMX esGMX tokens. These can be either staked
            or vested over 12 months to release GMX. Lastly, staked GMX tokens also earn Multiplier points
            that boost yields in GLP for long term holders.
            
            '''
    )

st.markdown('''
            #### Perpetual Protocol
            Introduced the fully decentralized virtual Automatic Market Maker (vAMM) model instead
            of order matching. See vAMM. The protocol originally launched in 2019 as Strike Protocol, until
            the PERP token was released 2020, after which they rebranded to Perpetual Protocol.            
            v2 of Perpetual Protocol: Leverages Uniswap v3 contracts to make the AMM 'real'.
            This iteration introduced the maker role, enabling traders to mint vTokens and provide
            liquidity in the pools. As Uniswap does not allow negative tokens, therefore short positions
            are issued vETH tokens (in case of a ETH/USDC perpetual). Leverage is capped at 10x.
            Perpetual Protocol uses the Chainlink price as the index price and as the clearing price
            during liquidation. Liquidation is executed by a keeper bot. 50% of the remaining collateral
            is retained by the liquidator and 50% is directed to the risk reserve. The risk reserve 
            is used to cover over losses accrued due to untimely liquidations during extreme market 
            volatility. Perpetual Protocol also monitors market prices through off-chain robots and these
            prices are used to trigger stop-losses in a timely manner.
            The PERP token is used as a governance token and it is also used by the protocol in an auction 
            mechanism to cover over losses in liquidations. PERP can be staked for staking rewards with a 6 month
            vesting period.
            
            
            '''
    )

st.markdown('''
            #### Helix (fromerly Injective)
            A decentralized trading platform with it's own blockchain built on Tendermint
            with a 2.5 sec average block time. One of Injective's products is perpetual contracts.
            It uses a type of pooled bidding called Frequent Batch Auctions (FBA) for order matching.
            In a block order cancellations and liquidations are immediately processed, but creation
            requests are added to a trade queue. Order matching starts at the end of each block.
            First, market orders are executed at a uniform price. Second, matchable limit orders are matched
            and are also executed at a uniform clearing price. Remaining limit orders are carried over to
            the next block. This system is not constrained by network throughput and prevents order
            front-running. On the negative, the real-time price does not exist until the end of each
            block. This is usually not a concern, but during large market fluctuations it may cause
            large losses.   
            Injective uses Chainlink as it's price oracle and clearing price during liquidations. 
            Liquidtion is handled by a bot which retains 50% of the liquidated funds and diverts 50%
            to a risk reserve which is used to cover over losses that cannot be recovered by normal liquidations
            during times of extreme market conditions.
            '''
    )

st.markdown('''
            #### MUX protocol (formerly MCDEX)
            The name of the protocol comes from liquidity multiplexing also known as 'muxing'. The protocol preferentially
            reserve assets across multiple chains (Arbitrum, BNB Chain, Avalanche, Fantom) to cover potential wins
            of traders negaged in leveraged margin trading and use the remaining assets in liquidity mining in selected other DEXes.
            Moreover, assets can be multipurposed and be used to cover mining and covering trades simultaniously, but
            the overlap is capped at 80%. MUXLP is the pool serving as counterparty for traders, but earning trading fees
            for depositors. The protocol ensures that there is no counterparty risk for traders.
            The protocols docs describe the risk of long positions for the pool to be delta-neutral, because
            as the price of the underlying asset rises (the long position trader is winning), the rise
            in value of the collateral [offsets the loss of value for the pool](https://docs.mux.network/protocol/mechanisms#multi-asset-pool).
            This is only true if the ratio of net assets (long-short margin/collateral value) remains below 50%.
            MUX uses a Dark Oracle to aggregate price feeds from multiple sources such as (Binance, Coinbase, Bitfinex).
            The oracle is private to prevent front running.
            The universal liquidityt pool gathers assets in a targeted ratio, issueing MUXLP tokens for depositors
            (buyers) of the token and burning them when they sell MUXLP. Buying MUXLP is completed after a set pending time of 18 minutes.
            The target ratio of assets is enforced by adjusting the buying/selling fees. To ensure the protocol gradually becomes
            self sufficient, 30% of protocol income is diverted to the POL (Protocol Owned Liquidity). Besides the 
            MUXLP this is a source of independent and available liquidity.
            MUXLP may be staked to earn MUX rewards, which may be sold on exchanges 
            '''
    )

st.markdown('''
            #### Drift Protocol
            Drift is relatively new fully decentralized (on-chain custody, on-chain matching logic) perpetual DEX built on Solana,
            offrering perpetuals in 3 markets, BTC, SOL and ETH. They aim to solve the problem of limited liquidity and
            slow order fills plaguing most fully on-chain perpetual DEXs with a 3 layer approach to on-chain matching:
            1. an order is first attempted to be matched in a Just-in-Time (JIT) auction held every 5s.
                This is a Dutch auction for markert makers where the auction starts at a higher than given price,
                but will not go lower than the requested price.
            2. vAMM: If no bid is submitted form MMs in the auction or if there is a remainder of the order after MMs bids
                a virtual Automated Market Maker (vAMM) steps in. The vAMM works with a constant product formula and 
                the price at which the AMM is accapting a bid from a particular aution is predetermined before the 
                auction and constitutes the guranteed price for the submitter of the take order.
            3. Order book. The limit orders are placed by users on chain. A version of the limit order book is kept by Keeper bots off-chain.
                When the trigger condition for the limit order is met the keeper bots will try to match the order
                against an available taker order, however if there is none available, they will fulfill the order against
                the AMM.
            The v2 vAMM of Drift updates the value of the AMMs k value based on wether the protocol had to pay funding rates
            (long/short postions were out of balance and the mark-index price did not reflect their relation). If the protocol
            had to pay, it will decrease k (and remove liquidity, the same transaction will move the price more) and increase
            k if it recieved net payment. The rate of change for k is capped at .1%. The withdrwable profit a trader can make
            is limited by the collateral pool. If a trader achieves a win not offset by other losses in the pool he has to wait
            before withdrawing. Winners may be offered a discounted margin on their unrealized gains.
            '''
    )

st.markdown('''
            #### Gains Protocol
            Gains is not a perpetual platform per se but similarly to GMX allows users to bet on various price movements
            with high leverage. It offers 37 Crypto pairs, 10 Forx pairs, 23 US Stock 4 US indices + 2 commodities, Gold
            and Silver. Traders can use up to 150x leverage for crypto and 1000x leverage on FOREX pairs, while paying only trading fees
            of 0.08% for makers and 0.06% for takers (makers need to pay Keeper bots to execute limit orders). Even though there is no price impact of trades, the platform still applies funding
            fees between short and long positions and a rollover fee based on the position size. They calculate the spread of a price (difference between the market price and the ask or brid price)
            based on the current open interest on the platform and the 1% depth of Binance of the releveant coin. The platform has a lower and upper bound
            on the size of the trades you can execute. The lower bound of a positions is 1500 DAI (=1500 USD), and the upper bound is set by the condition of the pool.
            The protocol allows for setting stop loss and take profit order at the creation of an order and stop losses are guaranteed to execute even though they are stored on 
            the on-chain. Gains is operating on the Polygon and Arbitrum networks.
            Gains protocol, similarly GMX or MUX does not trade anything when a position is opened or closed, so there is no price impact, but allows traders
            to make leveraged bets against a pool of assets in a vault that are reserved while the positions are open.
            If the protocol does not have enough collateral to cover the position of a particular high-leverage trade
            it mints GNS tokens and exchanges them in the GNS/DAI pool. If (when) more people are loosing trades, than
            winning, excess DAI is removed from the pool and exchanged for GNS in the GNS/DAI pool and burned (the process is reversed)
            Since this is the dominant process GNX is largely defaltionary.
            The index price of a crypto asset is requested from Chainlink (slow, but gold-standard) as well as the median
            of 7 price-feed APIs. Trades are only executed if the difference between these price feeds is less than 1.5%.
            They also have a 5 tiered NFT program (Bronze to Diamond). Holders of the NFTs can claim higher rewards from the
            DAI/NFT pool on their investments, trade with reduced spread and are eligible to run Liquidator bots or Limit order 
            Keeper bots.
            Gains Protocol was audited by Certik and has a B security rating with CERtified. They are not registered with 
            any of the insurance protocols.
            '''
    )
    
st.markdown('''
            #### CAP Protocol
            CAP protocol is a decentralized synthetic contract provider. They use an AMM to simulate liquidity
            available for their trades by observing the index price of the quoted asset and skewing the mid-market price. [whitepaper](https://www.cap.finance/whitepaper_mm.pdf).
            Traders can use up to 50x to trade BTC or ETH while paying a 0.1% fee. It is possible to participate in the
            USDC or ETH pools and and act a as counterparty to the traders, and profit from their losses. It is
            also possible to stake CAP, the protocol token to recieve some of the protocol's fees.
            While a position is open it incurs a funding fee dependent on the skew of positions on the market.
            v3 of the protocol uses dark oracles for index price feeds and can only execute market orders,
            while v3.1 uses Chainlink and can execute Limit and Stop Loss and Limit orders as well using keeper bots.
            Hence v3 of the protocol has centralized execution and v3.1 is fully decentralized.
            Liquidation on the protocol occurs after a position loses 80% of the initial margin value.
            While the protocol is fully permissionless, the terms of service restrict usage for citizens of US, Canada, Switzerland,
            Côte d’Ivoire, Cuba, Belarus, Iran, Iraq, Liberia, North Korea, Sudan, and Syria
            
            '''
    )

st.markdown('''
            #### Rage Trade 
            Rage trade is Perpetuals platform selling ETH-USDC perpetuals on Arbitrum with a maximum of 5x leverage.
            They us PerP v2 style vAMM on Uniswap v3, meaning that they create virtual USDC and ETH tokens for users
            when they deposit to their Rage wallet and (5x the collateral), that the protocol than swaps in a UniSwap v3
            pool to open or close a position.
            They use a funding rate mechanism called forward guidance to keep the mark price of positions close to
            the index price of ETH. The mechanism toggles between 3 methods: 
                1. The classic mark - index proportional calculation,
                2. A Chainlink Oracle feeding the funding rate of Binance
                3. A rate given by multisig with a governance vote.
            The express intent of this design was to enable stable coin issuers to build on top of the protocol and 
            open delta-neutral position short positions, while earning yield.
            The protocol also offers a '80-20' vaults, where 80% of the provided liquidity is deployed to external yield
            earning protocols and 20% provides concentrated liquidity for the UniSwap v3 contract. The protocol rebalances
            available liquidity daily (so the platform tokens remain under the 20% limit) and resets liquidity if the proportion
            of platform tokens would reach 50% after rebalance (for a more in dpth explanation plase visit their [mechanism page](https://docs.rage.trade/operations)).
            Currently only Curve's tricrypto LP tokens can be deposited into the 80-20 vault to provide liquidity, but
            the protocol has plans to expand it's vaults to AMMs(Curve, Balancer, Sushi), Money Market LPs(Aave, Rari, Euler)
            and Derivative LPs (GMX, Ribbon) on Arbitrum, Avalanche, Ethereum and Fantom, using Layer Zero to connect the protocols
            and bridge the LP tokens.  
            The protocol has a Delta Neutral vault which has two sections, a 'risk-on' and 'risk-off' vault. The principal idea
            is to earn yield from a BTC-ETH exposure in the GPL pool, while neutralising the impermanent loss exposure to BTC/ETH (the possible loss of value acrued if the USD value of these assets changes)
            by creating short positions for the equivalent amounts. The Risk-off vault accepts USDC which serves as collateral for a short created on Aave
            and the Risk-on accepts sGLP (GMX liquidity pool token) or USDC (which is converted to sGLP). The protocol then
            opens and updates short positions on GMX based on the current ratio and amount of BTC/ETH held by the risk-on pool.
            The short is constructed with a flash loan taken from Balancer in BTC/ETH as follows.
             * The BTC/ETH is sold for USDC on Uniswap
             * USDC is deposited in Aave
             * USDC is taken form the risk-off pool to maintain a 1.5 health factor for the loan in the nex step (and deposted on Aave along with USDC in the previous step)
             * ETH/BTC is borrowed from Aave
             * ETH/BTC is repayed to Balancer, completing the falsh loan
            The net effect of the described transaction is the creation or maintanence of a short ETH/BTC position with 1.5 health factor.
            The risk-off vault will be earning liquidity supplier APY from Aave, because some of the ETH rewards earned from GMX are sold for USDC and invested.
            The risk-on vault recieves rewards from the GLP vault in esGMX and ETH, and is exposed to GMX trader counterparty risk/reward.
            It also pays for the maintanence of the short. The protocol harvests fees and rebalances the position every 12 hours.
            Since GLP rewards its holders with both esGMX and ETH rewards, the Risk-On Vault is able to provide an extra boost in yield.
            Trading fee for ETH Perps is (0.15%). 
            '''
    )

    
st.markdown('''
            #### Mummy Finance
            Mummy Finance is a fork of GMX on Fantom launched on 2022 December. Similarly to GMX staked MMY tokens earn
            esMMY, multiplier points, and FTM rewards. The supply of MMY is capped at 10,000,000 ([tokenomics](https://docs.mummy.finance/tokenomics)). 
            Multiplier points reward long term users, 1000 MMY staked for 1 year earns 1000 MPs. MPs can be used to boost rewards on staking and are 
            burned if MMY or esMMY is unstaked (but staked tokens can be transfered without unstaking them). esMMY can be staked similarly to MMY
            or it can be vested to become MMY after a year. Vesting tokens requires reserving the same amount of MMY or MLP tokens as were used to earn the tokens.
            The vesting process is continuous, MMY tokens will time-proportionally become available every second. Vesting can be paused for esMMY and locked
            MMY or MLP tokens can be accessed.  
            MLP is the platforms liquidity pool token. Depositing in the pool earns esMMY and 60% of the platform fees in FTM tokens (Fantom native currency).
            Any token indexed by the platform can be deposited and any of them can be redeemed, after a minimum of 15 minutes cooldown. The fees for either
            operation depends on the targeted proportion of underlying assets for the platform. At the moment the Mummy supports BTC, ETH, FTM and stablecoin tokens.
            The MLP tokens recieved will automatically be staked and start earning esMMY. The pool serves as the counterparty for traders on the platform
            and will lose value when traders win and vica-versa.
            Traders can open a max 50x leveraged positions for BTC, ETH or FTM perpetuals, all quoted in USD. Profits are paid out in the same token the trader
            posted his collateral in, shorts will be paid in the stablecoin used to open the position. Trades are quoted in USD and the margin's (collateral) value is
            fixed after deposition in USD and there is a 0.3% fee on swapping the collateral to it's USD equivalent for longs (but not shorts). Traders pay a trading
            fee of 0.1% when either opening or closing a position and they pay an hourly borrow fee proportional to the portion of the asset they borrowed compared to
            the size of the pool. (There is no funding rate between longs and shorts). As there are no tokens bought or sold, there is no price impact when 
            entering the position, however there may be slippage (difference between ordered and executed price) due to the time it takes for the network to execute
            the transaction. The amount of accaptable slippage can be capped in the order (the order will fail if the price moved too much).  
            At the moment Mummy accepts market and limit orders. Take profit and stop loss orders can be set after a position is opened.
            The community also has a Mummy NFT, used to raise additional funds for the Treasury. Mummy minters have recieved esMMY as an incentive, but Mummy NFTs
            can also be staked to recieve periodic WFTM (Wrapped FTM) rewards.
            
            
            '''
    )

st.markdown('''
            #### Metavault.Trade
            Metavault is a fork of GMX on Polygon started in 2022 March. It's parameters are very similar to the ones of GMX or Mummy Finance. The platforms counterparty 
            pool holds Matic, BTC, ETH, LINK, UNI, AAVE and stable coins Depositors recieve MVLP tokens. MVLP tokens share in the platforms trading fees (presumably 70% of fees).
            MVLP tokens earn rewards in the form of esMVX and MATIC (Polygon native token). MVX is the platforms token used for rewards and marketing purposes. 
            Staking MVX or esMVX tokens earns rewards as esMVX (escrowed) which can be vested over a period of 1 year. Vesting is continous. Staked tokens also recieve MATIC rewards from 30% of
            the platform trading fees as well as multiplier points that can also be staked to further increase yield.
            Traders can use 50x leverage and all positions incur a trading fee proportional to size of the position. There is also a trading fee of 0.1%. 
            The site uses an integrated TradingView charting tool. Traders can use Market and Limit orders to open positions, but Stop Loss/ Take Profit 
            orders can only be added after the position is already open.
            The protocol uses an audited fork of GMX, but has since been independently audited by Techrate. The app is available on backup IPs and on the IPFS to provide continous service.
            
            '''
    )
    
    
st.markdown('''
            #### OPX Finance
            OPX is a GMX fork on Optimism started in 2022 November by the DarkCrypto Foundation DAO. Traded perpetuals: OP/USD, BTC/USD, ETH/USD. Protocol token: OPX, Pool token: OPL.
            35% of the protocol fees are sent to the DAO Treasury. Staking OPX yields veOPX rewards which is both a vesting token and a governance token for the OPX DAO. Holders vote on
            the distribution rewards from protocol income. The protocol has a buyback and burn program, making OPX deflationary. 60-70% of platform fees are distributed to stakers in WETH.
            As in other GMX forks, depositing funds in the OLP pool exposes the user to trader counterparty risks/rewards.
            Trading open/close position fee: 0.1% borrowing fee: up to 0.01%/hour.
            Fianlly they are working on a betting game, where one may stake collateral and bet on the price movement of ETH in the next 5 minutes. Payout is inversly proportional
            to relative volume of each side (up, down) to the total volume.
            '''
    )

st.markdown('''
            #### FutureSwap
            FutureSwap is a straightforward platform for creating leveraged positions using UniSwap v3 (not a perpetual). It consists of a pair of assets,
            currently 6 pairs are available on 3 chains (Ethereum, Avalanche, Arbitrum). The leveraged amount from the pools holdings is swapped and trader gains short or long exposure,
            while paying fees. 
            To avoid over-losses the protocol auto-deleverages positions within itself (to avoid delays). If a long(short) position need to be closed
            it forces an equivalent amount of short(long) positions to be closed at the same time. While this is not ideal for the force-closed positions
            they are compensated by getting a better-than-market quoted price on the position. This is possible because the liquidated position gets liquidated
            at 4% over the bankruptcy price and the remaining collateral is used to compensate the force-closed trader.A fee of 0.05% is charged on every trade.
            A funding rate dependent on the long/short open interest ratio is affected on positions.
            '''
    )


st.markdown('''
            #### Deri Protocol
            Deri was started in 2021 February specifically for on-chain derivative trading. It is currently in v3 with major
            upgrades in funds handling and product offering compared to previous versions. It operates on the BNB Chain and Arbitrum.
            Deri has 3 major categories of perpetual-like derivatives: Perpetual Futures, Everlasting Options and 
            Power Perpetuals. Positions are organized into transferable NFTs, integratable with the broader DeFi
            ecosystem. The protocol supports opening pools for any token pairs (on paper, could not find the technical options to execute this).
            Deri uses external custody of funds, ie.: funds are only locked as needed, funds not in use are deposited to
            external protocols such as Compound, Ethereum and Venus to increase yield. When a user (LPer or trader)
            first deposits funds to the protocol it creates a Vault for each user. The Vault will send any non-reserved
            funds to a money market protocol and hold receipt tokens for the funds. The protocol then uses the Borrow Limit
            function of the money market protocols to calculate the dynamic effective value of the funds.
            Deri's AMM Mechanism ([whitepaper](https://github.com/deri-protocol/whitepaper/blob/master/deri_v3_whitepaper.pdf)), called DPMM (Deri Proactive MM) involeves a common pool for for all derivatives where Liquidity Providers (LPs)
            act as a common counterparty to the individually settled traders. Besides winnings and fees of the pool,
            LPers benefit from DERI awards for providing liquidity. With Deri's AMM implementation any trade pushes the
            price linearly (there *is* a price impact when buying) and the relative price difference to the index price is proportional to the net
            long-short position of the derivative.   
            After deposition traders may use up to 25x leverage for perpetuals and in-the-money everlasting future options and 
            200x leverage for out-of-money options, while allowing only 12.5x leverage for power perpetuals. All maintanance margins are at
            50% of the initial margin except for out-of-money options (which are generally much lower). *Margin requirements
            are evaluated dynamically*, if the value of the collateral changes, a position may become liquidated even if the
            price doesn't move against it. Positions may be closed partially, the platform supports reduce only orders.
            There are no limit orders are stop losses availble for DERI protocol, positions need to be managed manually.
            trading fees are 0.1 or 0.2% for perpetuals (0.1 for BTC/ETH). 
            The stability of positions are ensured by on-chain liquidator bots, that anyone may run. Once the liquidate()
            function is successfully called on a position the liquidator closes the position and recieves a portion of the
            remaining margin (2% of the margin in most cases). This portion is 50% of the remaining margin or 1000 USD
            whichever is smaller.
            
            '''
    )

st.markdown('''
            #### Mycellium Perpetual Swaps
            Originally depolyed as Tracer DAO in 2021 September, Mycelium Perpetual Swaps is a decentralised derivative exchange, which allows users to open leveraged long and/or
            short positions on crypto-assets. Though not explicitly stated, the construction All traders trade against the Mycelium Liquidity Pool (MLP).
            Traders on the platform can enjoy trading leveraged positions with extremely low entry and exit fees
            (0.09% of notional value) with no price impact on a range of assets: BTC, ETH, LINK, BAL, FXS, & CRV!
            The Mycelium Liquidity Pool also doubles as an AMM, allowing traders to swap between any two assets in
            the pool (including stablecoins).
            The MLP pool earns 70% of fees generated from swaps and leveraged trading. These fees are converted to ETH
            and are continously ditributed to MLP stakers. MLP stakers also earn esMYC tokens which may be vested into MYC tokens,
            in the esMYC vault over a period of a year.
            There is no price impact for trades on the Mycellium Protocol, however there is a small spread applied to assets
            other than BTC or ETH. Traders may use market, limit and conditional stop loss/take profit orders, however these
            can not be set before entering the position and cannot be set in an one-cancels-tht-other (OCO) manner.
            Conditional (Limit, stop) orders are executed by keeper bots and are converted to market orders. Even though there is
            no price impact for orders, price slippage may still occur between the quoted and executed price. This can be limited with the
            slippage tolarance parameter of the order. Market orders pay a fee of 0.09% on position entry and exit,
            but this may be lowered in a tiered manner down to 0.072% for users trading at least 20 M USD/month.
            Levered long positions require the asset they are leveraging as margin. If a position with the incorrect asset
            as margin is opened, the collateral will be swapped and swap fee of 0.2% will be applied. Traders also need to
            pay a borrowing fee on the asset they are using in proportion to the utilization of the assets in the pool. (up to a maximum of 0.005%/hour).
            There is also a bid-ask spread applied to cryptos other than BTC, ETH: 0.44% for LINK and UNI, 0.88% for all others.
            Profits from the spread are left in the pool.
            The liquidation leverage of Mycelium Perpetual Swaps is 100x (minus borrowing fees). The liquidation fee is 5 USDC.
            Mycelium uses its own price keeper that takes the median of 3 CEX prices. Any time this price is more than 5 minutes old,
            the Chainlink oracle pricefeed is used instead. If at any time the keeper-chainlink pricespread exceeds 2.5%, a 2.5% spread will
            be added to the Chainlink price between bids and asks.  
            5% of trading fees are awarded to the top 5% of traders by volume every 2 weeks.  
            Restricted territories: China, the United States, Antigua and Barbuda, Algeria, Australia, Bangladesh, Bolivia, Belarus, Burundi, Myanmar (Burma), Cote D'Ivoire (Ivory Coast), Crimea and Sevastopol, Cuba, Democratic Republic of Congo, Ecuador, Iran, Iraq, Liberia, Libya, Magnitsky, Mali, Morocco, Nepal, North Korea, Somalia, Sudan, Syria, Venezuela, Yemen, Zimbabwe
            
            '''
    )

st.markdown('''
            #### handle.fi
            handle.fi is a decentralised multi currency stablecoin protocol. The handle protocol allows users to leverage trade, swap, borrow and earn from multi-currency stablecoins; called fxTokens.
            fxTokens are collateral backed stablecoins representing, and soft pegged to, a range of currencies.
            The protocols native token FOREX may be exhanged in the apps pool or at balancer or at Uniswap or traded at Gate.io.
            fxToken and FOREX holders are able to stake tokens across governance, liquidity and fxkeeper functions to earn a portion of fees and rewards in FOREX.
            The fxtokens themselves are created by separate vaults (called CDP vaults) holding collateral for the minted tokens.
            The synthetic fxtokens may be minted against and redeemed for ETH or FOREX collateral as well being used to trade with a 50x leverage. 
            handle.fi only supports market orders and therefore there is no possibility to limit risk by stop loss or take profit orders.
            There seems to be no price impact or funding rate for trading, however there is an hourly borrow rate, but its quantity is not displayed.
            As per docs the protocol charges 2.5% interest on loans.
            handle.fi also provides a UI for a bridge to transport tokens between abitrum, polygon and ethereum.
            The protocol uses a keeper bot system to handle liquidations and the capital used to repay liquidated 
            accounts is communal and anyone can contribute to this for recieving a portion of the liquidated margins.
            Rewards are boosted based on users veFOREX amounts. Users can lock FOREX/fxUSD (80/20) Balancer Pool Token (BPT) into the handle.fi governance pool to receive veFOREX - 'vote escrowed FOREX'
            For perpetual trading, handle.fi uses the H2SO (handle high speed oracles) system which allows the end user to update the price directly on an oracle aggregator contract by submitting a trusted signature.
            The platform uses a community incentive system called PIE to issue bounties for marketing the platform
            and has released a limited NFT program called t0-Troopers to its supporters, granting access to swaps and trading free of platform fees to its owners.
            
            '''
    )

st.markdown('''
            #### Kwenta
            Kwenta is a decentralized trading platform on Optimism offering synthetic assets minted by the Synthetix staking contract. It's first version was started in 2022 November.
            Kwenta gains its oracle prices from the Synthetix exhachange rate contract, whose stored prices are frequently updated.
            SNX holders take on counterparty risk when open positions in the futures market is skewed. To compensate for this a funding rate 
            and a skewed price impact function is used.
            The online UI only allows positions to be opened by market orders. v1 of the protocol had limit and stop loss orders implemented,
            however at the time of writing only market orders were visible without depositing with the protocol.
            While v1 of the protocol is still online and available, it is being depricated and new positions cannot be opened on it.
            Kwenta imposes a fixed execution fee of 2 sUSD per order as well as a varaible fee for makers and takers. 
            The protocol uses the term maker in a non-orthodox sense. They refer to makers as traders that reduce the minority contractual position (eg. traders going short, while the majority is going long)
            The initial configuration for maker/taker fees are 0.1/0.3%, but in practice these values vary market by market.
            Off-chain oracles provided by Pyth Network allow perps fees to be reduced to 5-10bps. They save prices off-chain
            and are provided to traders by keepers when a trade is initiated, with an 8-sec delay due to block times.
            The on-chain validation process includes staleness checks, key-threshold confirm, and a final check against on-chain oracles.
            
            As a side product Kwenta offers integrated 1inch swaps on the platform.
            '''
    )


st.markdown('''
            #### LEVEL Finance
            
            Level Finance launched in January 2023 and in month managed to reach over 15M USD TVL and 200 M USD daily traded volume,
            substantial numbers in the DeFi space. Their order matching/liquidity provision model is innovative. It resembles the GMX
            family of AMMs in so far as having a pool being the trade counterparty and having 0 price impact when trading, but they have
            created Tranches from the pools underlying collateral types. This Tradfi term means, that their assets (BTC, ETH, BNB, CAKE and stablecoins) are
            organized in three groups of risk seniority (called tranches). A tranche defines how much of the constituent assets PnL will the
            tranche absorb. The most senior tranche draws most of its PnL form the least risky assets(BTC,ETH), while the most junior draws most
            PnL from the most risky asset (CAKE). Correspondingly potential and realized yields/risks are higher for the junior tranches.
            The LVL utility token is earned by trading or LPing, or refering users, whereas the LGO governance token is earned only by staking
            LVL. LGO is reddemeble pro rata against treasury assets. For every 1 USD traded in swaps or closed positions you get 1 lyLVL (loyalty LVL), which
            turn into LVL after a 24 h vesting period. (Caveat: swapping between stable coins earns 1/20th of this reward). Not one to one though. Each day 16000LVL is distributed proprotionally to every trader
            who earned lyLVL in the past 24 hours.
            Trading is possible once the user deposits collateral in one of the pool tokens. Traders may us up to 30x leverage, the maintanence margin is 1%.
            Using Limit orders are possible, but stop orders are not, risk has to be managed manually or via bot.
            There is a 0.1% fee for opening or closing postions and a 0.01% maximum hourly borrowing fee for using the pool assets (maximum when using 100% of a given asset).
            Similar GMX swapping pool asssets is also supported with swapping fees ranging from 0 to 0.6% favoring transactions raising the
            amount of underrepresented assets in the pool.
            There is a fixed liquiodation fee of 5 USD (which means that 1% maintanence margin is only applicable to positions over 500 USD)
            
            '''
    )

st.markdown('''
            ### CEXs
            '''
    )

st.markdown('''
            #### BTCEX
            Launched in July, 2021, BTCEX is a full-category digital asset trading platform, providing both spot and derivatives trading
            options. The site sports a fast response user interface with Tradingview charting and an integrated order book - depth chart.
            Users can execute conditional and trailing stop orders and mitigatte risk by setting up stop-loss and take profit orders before
            they enter a position. BTCX offers using up to 125x leverage with a capped position size of 50,000 USDT.
            Fees for makers and takers are 0.02 and 0.05%.   
            The exchange has an A cybersecurity rating with CoinGecko and has completed 3rd party penetration tests, proof of funds and has a bug bounty program.
            Some restrictions in using the platform apply to citizens of the US and Japan.
            
            '''
    )

st.markdown('''
            #### Binance
            Following it's launch in June, 2017 Binance grew into the largest cryptoexchanage on the planet in less then 180 days.
            Binance come swith a whole ecosystem of products beyond spot and derivatives trading, including it's own peer-2-peer exchange,
            inhouse NFT market, FIAT card payment system, launchpad etc.   
            From the perpetual perspective Binance offers two main lines of products: USD-M Futures (settled in USDT or BUSD) and COIN-M Futures (settled in USD).
            With 220 perpetual markets Binance covers all coin and token use-cases.
            Users can use up to 125x leverage with a capped position size of 50,000 USD. Fees for makers and takers range up to 0.02 and 0.04%,
            but are dependent on the trader tier (which is a function of the past month's volume and the amount of BNB a trader holds in his spot account).
            All fees are reducable by 10% if a user is willing pay them in BNB.   
            The site has its own charting interface as well as an integrated Tradingview charting tool and an integrated order book - depth chart.
            Users can execute conditional and trailing stop orders and mitigatte risk by setting up stop-loss and take profit orders before
            they enter a position.  
            Automated grid trading is also available on Binance Futures.
            The exchange has an AAA cybersecurity rating with CoinGecko and has completed 3rd party penetration tests, proof of funds and has a bug bounty program.
            Binance itself was hacked once, in May 2019, when attackers were able to steal 7000 BTC (worth 40 M USD at the time), as well as 2FA and API keys. All user losses were covered by Binance.
            More recently, in October 2022, 2 million BNB (570 M USD at the time) were minted from cross-chain bridge leading to Binance requesting a temporary stop
            to BSC from the BSC validators.
            Binance Futures are not available to the citiyens of the US, Singapore, Canada, China, Malaysia, Japan, UK, Thailand, Germany, Italy and the Netherlands.
            
            
            '''
    )

st.markdown('''
            #### BTCC
            BTCC is one of the longest operating cryptoexchanges still in operation. Originally started as Bitcoin China
            in June 2011 the platform is still among highest volume exchanges in the futures and perpetuals market.
            The Tradingview interface is clean and simple, but still supports stop-loss/ take-profit type conditional
            orders and these may be set before entering a trade as well. Users may use up to 150x leverage. Contracts are mostly
            settled in USDT, but there are markets available in USD for BTC, ETH and XRP.
            The selection of available contracts is competitive with 75 perpetual contracts covering even some minor and meme coins
            as well as providing perpetual contracts for stocks like Tesla or Microsoft.
            The fees are somewhat higher than most exchanges use, 0.065% for both makers and takers, but this may be lowered to
            0.055% with a realtively modest amount of volume and on-exchange deposits.   
            BTCC does not have a recognized security rating by Coingecko, but they do claim to perform regular
            penetration testing. Over 11 years of operations the exchange hasn't been hacked.
            '''
    )

st.markdown('''
            #### Deepcoin
            Deepcoin is Singapore based CEX estabilished in November 2018 offering both spot and futures products.
            Trades are settled in USDT for most tokens and coins (62), but they offer reverse contracts for 7 of the
            large market cap coins. Their user interface has both a legacy and Tradingview options and their app comes
            with extra features such as K-line quick trading for 'Pro' contracts. This enables users to set up triggered market orders
            by tapping the price and setting the amount to be traded. Once in position users can add trailing stops or
            take-profit/stop-loss limit orders to the position. In nortmal mode users do have the option to pre-set 
            limit orders with stop-loss take-profit orders, as well as set up conditional SL / TP orders. The platform
            supports hedged positions, users can enter up to 20 positions in the same contract with different leverage,
            these positions can then be merged again if needed to avoid their individual liquidation.  
            Deepcoin supports trading with up-to 125x leverage, with a capped but very high amount of contracts (32 BTC for the BTCUSDT pair)
            Platform fees are 0.02 and 0.04% for makers and takers with no option to reduce them.
            Deepcoin does not have a security rating from Coingecko or calims of security audits. However, to their 
            credit, there is no record of them ever being hacked either.
            Getting open positions data on this exchange is difficult as they do not make it publicly available and
            only 3rd party aggregators provide it.
            '''
    )

st.markdown('''
            #### BingX
            Estabilished in May 2018, BingX has been trading spot and derivative products through several crashes bull cycles.
            In general BingX focuses on providing automated tools for trading. They are integrated with Metatrader 5 and 
            are able to execute trades from the signal trading platform, but they also provide a signal trading option for
            their users to set-up their own bots without programming or APIs. They also provide the option of grid trading
            as well as copy trading for a simpler experience. They use a version of the Tradingview UI complete with an
            order book meaningfully animated with the depth chart. They offer Take Profit/ Stop Loss orders as well as 
            Trailing stops, but SL / TP cannot be set when setting up the trade. Traders dealing Perpetuals may use leverage
            up to 100x (cap data not provided). The platform supports hedging and opening multiple orders on the same currency
            and merges new orders into the same position when executed. Maker and taker fees are 0.02 and 0.05% reducible with
            *very* high trading volumes to 0.0015% and 0.035% respectively.
            BingX has an A security rating at Coingecko, and have reported to have performed penteration tests and posts bug bounties.
            BingX also provides a Merkle Tree of their proof of reserves on the 1th and 15th of every month and a thrid
            party audit of said reserves by Mazars. To date, no major hack of the exchange has been reported.
            '''
    )

st.markdown('''
            #### Bitget
            Bitget was estabilished at the end of 2018 with the idea of putting community trading at the center of their
            business. To this end the exchange's app makes copy trading very simple with their One-click copy trade feature.
            They also support grid trading with the parameters either filled in by a Machine Learning model or entered manually.
            The exchange mostly settles trades in USDT (80 contracts), but large cap tokens (9) may be traded in USD and the 
            big two, BTC & ETH in USDC as well. Trades up to 125x leverage are supported (no data on caps). Their user interface
            is based on Tradingview and the exchange supports Take Profit / Stop Loss orders and trailing stop orders and any order
            may be paired with TP/SL that activates once the order executes. The platform charges 0.02% for makers and 0.06% for 
            takers, but this may be lowered to 0.0015% and 0.035% for traders over 200M USDT in mothly volume.
            Bitgets Coingecko Security rating is BBB though they do have penetration testing provide proofs of reserves and offer
            a bug bounty. Bitget has not been hacked to date.
            '''
    )

st.markdown('''
            #### MEXC
            Started in April 2018 MEXC offers spot and perpetual trading as well as leveraged ETFs. They have one of the 
            widest selection of perpetuals on the market with 180 contracts settled in USDT and 6 large caps settled in USD.
            Traders may use up to 200x leverage with positions capped at 52.5 BTC (for the BTCUSDT pair). Better yet, at the time
            of writing, all maker fees on exchange were 0, while taker fees started at 0.06%, but were reducible to 0.042%.
            The exchange supports copy trading, grid trading. Traders may use triggered Take Profit / Stop Loss orders as well as
            trailing stop orders, but TP/LS cannot be set for an order before it executes.   
            MEXC has an A Security rating listed at Coingecko, and are presenting penetration test, proofs of funds and have  bug bounty.
            No hack of the exchange has been reported to this point.
            MEXC does not offer services to citizens of North Korea, Cuba, Sudan, Syria, Iran, Yemen, Zimbabwe, Myanmar, Lebanon, Libya, Bolivia, Ecuador, Bangladesh, Somalia, Iraq, Congo Democratic Republic (Golden), Central African Republic, Kyrgyzstan, Burundi, Afghanistan, Macedonia, Ethiopia, Guinea-Bissau, Guinea, Liberia, Trinidad and Tobago, Venezuela, Serbia, Crimea, China, Singapore and Italy.
            '''
    )

st.markdown('''
            #### OKX
            Founded in January 2017 as OKeX the exchange has grown to be one of the largest crypto markets.
            Besides perpetuals they also offer spot, margined, DeFi, lending and mining services.  They 
            offer 130 contracts with USDT settlement, 33 contracts with USD and 2 with USDC settlement.
            Their original charting system is very nice, coplete with a projected depth chart on the right side 
            of the price chart, which would be pretty useful if the sticker for the price didn't cover the immediate
            vicinity of the actual price. They also provide the standard Tradingview interface as well. 
            Their fees for makers and takers are 0.02% and 0.05% but this is reducible to 0.015 and 0.03% by holding
            the exhanges OKB token. It may be reduced even further for VIP users, however accesing this tier requires
            at a minimum 100,000 USD in assets held at the platform or 50 M USD in monthly volume.
            It is possible to use copy trading and grid trading on the site (and even copy other people's grid trading strategies!).
            Users may use up to 125x leverage on the platform capped at 2000 contracts, which equates to 200,000 USD.
            OKX has an A Security rating listed at Coingecko, and are presenting penetration test, proofs of funds and have  bug bounty.
            No hack of the exchange has been reported to this point.
            OKX is not accessible for US citizens, they can use the sister exchange, OKCoin with limited features.
            '''
    )


st.markdown('''
            #### Bybit
            Bybit started operation in March 2018 and became one of the best know exchanges offering perpetuals.
            The company ran high profile ads was the principal sponsor of the Formula-1 Oracle Red Bull Racing team,
            who won both the drivers and contructors championships.
            Bybit is offering 184 USDT perpetual contracts, 9 inverse contracts and 21 USDC setteld contracts. The
            maximum leverage is 125x, but the position cap is not specified. They offer their own trading interface
            as well as a Tradingview interface. Users may set Limit or conditional orders (Take profit and Stop loss orders),
            but TP/SL orders may not be preset for other orders. Makers need to pay very generous 0.01% fee, while
            takers have to pay 0.06%. Both are reducible by having a large trade volume and holding sufficient assets on
            the exchange (maker fees to 0 and taker fees to 0.04%). Traders have the option to use copy trading and/or
            grid trading bots and use AI parametrization to help set up the bots.
            Bybit has an A security rating with Coingecko and they have performed penetration test and presented prrof of funds for the exhange
            and have a bug bounty.
            There has been no security breaches of the exchange reported to this point.
            Bybit does not offer it's services to citzens of the US, Singapore, Cuba, Crimea, Sevastopol, Iran, Syria, North Korea, Sudan and Mainland China.
            '''
    )

# st.markdown('''
#             #### BTSE
            
#             '''
#     )

st.markdown('''
            #### Gate.io
            Gate.io is the earliest crypto-to-crypto exchange from China. The company is located in the Cayman Islands. 
            It was launched in 2013 under the name Bter or Bter.com, then in the fall of 2017 the exchange was taken over by Gate Technology Inc. and has been renamed.
            '''
    )

# st.markdown('''
#             #### Phemex
#             Offers Perpetuals with 100x leverage.
#             '''
#     )
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
            #### Perpetual Futures Contract
            A Futures contract that automatically rolls over with no set expiration date.   
            The concept was proposed in its popular form in a [1993 NBER working paper by Nobel laurate Shiller](https://www.nber.org/system/files/working_papers/t0131/t0131.pdf).   
            Crypto perpetuals (a BTC perpetual) were first introduced by BitMEX in 2016. A differen t name for the
            concpet is CFDs ContractsFfor Difference.   
            Perpetual contracts are anchored to the underlying index price via the **Funding Rate** of the contract.   
            Contracts may be either **linear contracts**, settled in stable coins or **inverse contracts** settled in a crypto asset.  
            While **inverse contracts** may be more convient to open positions infor crypto holders, they magnify the risk of liquidation for long positions.
            In early 2022 Perpetual trading volume has [surpassed](https://phemex.com/academy/what-is-perpetual-protocol-perp) spot trading volume.
            Perperuals in general are *the* most traded asset in finance with daily trading volume in the tens of trillions.
            '''
    )

st.markdown('''
            #### Everlasting Options
            Everlasting Options are a DeFi innovation ([whitepaper](https://github.com/deri-protocol/whitepaper/blob/master/deri_everlasting_options_whitepaper.pdf)) offered by the [Deri Protocol](),
            that share the properties of Perpetual Futures Options. Like Perpetuals, they do not have an expiration date and their price is governed by a funding rate,
            but like Options they do have a stike price. Their funding rate does not converge the mark price to an index price, but it is proportional to the degree
            the mark price differs from the option payoff (the amount the holder would recieve), if the option is in the money. If the option is out of the money it's
            price will drop near zero (depending on how far out of the money it is), but compared to the price it will still retain a substantial funding rate for contract 
            sellers. The out-of money margin maintanence margins are also unique. They are .5%-to 5% whereas in-the-money options have a 5% maintanence margin on Deri.
            
            '''
    )


st.markdown('''
            #### Power Perpetuals
            Power perpetuals ([whitepaper](https://www.paradigm.xyz/2021/08/power-perpetuals)) are perpetuals with a mark price that scales non-linearly with the 
            index price. For example if the BTC's index price doubles a BTC^2 price quadruples. Similarly to regular perpetuals, power perpetualss mark price is
            kept in line with a funding fee, proportional to $(MARK-INDEX^p), where p is the power of the perpetual. 
            
            '''
    )


st.markdown('''
            #### Arbitragers
            In a general sense a special kind of trader that takes advantage of price differences between markets, earning a low risk profit in the process and
            equilibrating the market. For perpetual futures this means a trader who deliberately takes the side (long or short) that is undersubscribed earning
            a funding fee in the process. For short perpetual positions the arbitrager may make the position delta neutral (the positions value does not change withthe underlying price),
            by buying and quivalent amount of underlying asset on the spot market. The profit or loss from price change will cancel out, while he retains the 
            funding arbitrage.
            
            
            '''
    )

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

st.markdown('''
            #### Crypto-synthetics
            Crypto-synthetics are cryptocurrency backed instruments that track the value
            of an underlying asset (e.g. a stock). They allow investors to gain exposure to
            an asset without needing to own it or interacting with the traditional financial
            system, saving time and money.
            
            '''
    )

st.markdown('''
            #### Open Interest
            Refers to the amount of contracts open at any given moment, meaning that someone purchased the contract,
            -opened a position- but did not close it yet. Both long and short positions are counted in this metric.
            Significant open interest for a contract signals a lively secondary market and traders can expect contract prices
            to have a narrow spread.
            '''
    )

st.markdown('''
            #### Volume
            A contracts volume is the amount of positions that were closed in a given period (both long and short positions).
            
            '''
    )

# st.markdown('''
#             #### Futures Contract
#             dex exchange
            
#             '''
#     )

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