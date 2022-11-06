import random
import numpy as np 

def submit_market(state, my_history, period_history):
    
    prices = [x['price'] for x in period_history]
    p = np.mean(prices)
    
    for trade in my_history:
        if trade["dir"] == "buy":
            num_buys += 1
        elif trade["dir"] == "sell":
            num_sells += 1
            
    total_buys = 0 
    total_sells = 0
    for trade in period_history:
        if trade["dir"] == "buy":
            total_buys += 1
        elif trade["dir"] == "sell":
            total_sells += 1
            
    if total_buys - total_sells > 100:
        return {
                "buy": {
                        "price": p + 10,
                        "size": 10
                        },
                "sell": {
                        "price": p + 20,
                        "size": 0
                        },
                }
    elif total_sells - total_buys > 100:
        return {
                "buy": {
                        "price": p - 20,
                        "size": 0
                        },
                "sell": {
                        "price": p - 10,
                        "size": 10
                        },
                }
