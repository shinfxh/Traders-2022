# Place any imports you need here!
# Helpful packages may include numpy, pandas, and sklearn.

import numpy as np

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
        max_hold = 1000000
        trades['Stock1'] = -1000
        m1 = 0.52524942 #based on stock1 prices
        b1 = 0.04248039
        
        if 'Stock1' in stock_prices: 
            diff1 = stock_prices['Stock1'] - stock_prices['Stock1_Delay']
            predict_diff2 = m1 * diff1 + b1
            #print(predict_diff2)
            if predict_diff2 > 0:
                trades['Stock2'] = 1000
            else:
                trades['Stock2'] = -1000
            
        total = 0
        for stock in trades:
            key = stock + '_Delay'
            total += np.abs(stock_prices[key] * trades[stock])
        scale = 0.9 * max_hold / total
        for stock in trades:
            trades[stock] *= scale
        #print(trades)
        return trades
