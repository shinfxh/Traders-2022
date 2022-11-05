# Place any imports you need here!
# Helpful packages may include numpy, pandas, and sklearn.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_trader(data):
    trader = Trader()
    total = 0
    for i in range(len(data) - 1):
        prices = df.iloc[i].to_dict()
        next_prices = df.iloc[i + 1].to_dict()
        trades = trader.MakeTrades(i, prices)
        pnl = 0
        for stock in trades:
            pnl += trades[stock] * (next_prices[stock] - prices[stock])
        total += pnl
    return total

class Trader:
    def __init__(self):
        self.team_id = '71e18vZcweB0w0F' # TODO: CHANGE TO YOUR TEAM'S PASSWORD.
        # Add any additional info you want

    def MakeTrades(self, time, stock_prices):
        """ 
        Grader will call this once per timestep to determine your buys/sells.
        Args: 
            time: int
            stock_prices: dict[string -> float]
        Returns: 
            trades: dict[string -> float] of your trades (quantity) for this timestep.
                Positive is buy/long and negative is sell/short.
        """

        trades = {}

        # TODO: PICK HOW TO MAKE TRADES.
        trades['Stock1'] = -1000 
        #if 'Stock2' in stock_prices: 
         #   if stock_prices['Stock2'] > 123:
           #     trades['Stock2'] = 1000
          #  else:
            #    trades['Stock2'] = -1000

        total = 0
        for stock in trades:
            total += np.abs(stock_prices[stock] * trades[stock])
        scale = max_hold / total
        for stock in trades:
            trades[stock] *= scale

        return trades
