import numpy as np
def submit_market(state, my_history, period_history):
            
    to_buy, to_sell = 500 / p * 10, 0
    prices = [x['price'] for x in period_history]
    p = np.mean(prices)
    buy_price, sell_price = p + 1, p + 2
    
    return {
            "buy": {
                    "price": buy_price,
                    "size": to_buy
                    },
            "sell": {
                    "price": sell_price,
                    "size": to_sell
                    },
            }
