import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iterations = 10

n_teams = 50



for _ in range(100):
    price = 1000

    pnl = 0
    
    holding = 0
    
    k = 0.5
    bid = k*500+(1-k)*price
    ask = (1-k)*price+k*1500
    isBid = True
    theta = 500+1000*np.random.random(1)[0]
    
    lamb = 50+150*np.random.random(1)[0]
    #print(theta, lamb)


    c_pnl = 0
    c_holding = 0
    for i in range(50):
        
        n_asks = 0
        n_bids = 0
        std = max(price-500, 1500-price)/2
        prices = []
        ask_prices = []
        bid_prices = []
            
        for _ in range(n_teams):
            v = np.random.normal(price, std, 1)[0]
            if v>price*1.2 and v<1500:
                n_asks += 1
                ask_prices.append((v, 0))
                prices.append((v, 0))
            elif v<price*0.8 and v>500:
                n_bids += 1
                bid_prices.append((v, 0))
                prices.append((v, 0))
            elif 500<v and v<1500:
                t = np.random.random(1)[0]
                if t>0.5:
                    n_bids += 1
                    bid_prices.append((v, 0))
                    prices.append((v, 0))
                else:
                    n_asks += 1
                    ask_prices.append((v, 0))
                    prices.append((v, 0))
            

        price = sum([i[0] for i in prices])/len(prices)

        if n_asks>n_bids:
            isBid = True
        else:
            isBid = False
        if isBid:

            bid_prices.append((bid, 1))
            bid_prices.append((750, 2))
        else:
            ask_prices.append((ask, 1))
            ask_prices.append((1250, 2))

        
        bid_prices.sort()
        ask_prices.sort()
        count = 0
        fulfilled_bid = False
        
        fulfilled_ask = False

        c_bid = False
        c_ask = False
        c_bid_price = None
        c_transaction_done = False
        isMatch = True
        while isMatch:
            if bid_prices[-count-1][1]==1:
                fulfilled_bid = True
                
            if ask_prices[count][1]==1:
                fulfilled_ask = True
            if bid_prices[-count-1][1]==2:
                c_bid = True
            if ask_prices[count][1]==2:
                c_ask = True
                c_bid_price = bid_prices[-count-1][1]
            
            if bid_prices[-count-1]>ask_prices[count]:
                count += 1
            else:
                isMatch = False

        ave = (bid_prices[-count][0]+ask_prices[count-1][0])/2
        new_bids = []
        new_asks = []
        
        for _ in range(500):
            t = np.random.random(1)[0]
            if t>0.5:
                new_bids.append(theta-lamb+2*lamb*np.random.random(1)[0])
            else:
                new_asks.append(theta-lamb+2*lamb*np.random.random(1)[0])

        
        if isBid:
            if fulfilled_bid:
                ## if exists ask_price less than bid, yay
                
                holding += 1
                pnl -= ave
                hasBought = True
                bid = k*500+(1-k)*price
                ask = (1-k)*price+k*1500
                if n_asks >= n_bids:
                    isBid = True
            else:
                
                done = False
                for i in new_asks:
                    if i<bid and not done:
                        holding += 1
                        pnl -= i
                        done = True
                        bid = k*500+(1-k)*price
                        ask = (1-k)*price+k*1500
                        if n_asks >= n_bids:
                            isBid = True
                        #print("customer success", i)
                    if i<750 and not c_bid and not c_transaction_done:
                        c_holding += 1
                        c_pnl -= 750
                        c_transaction_done=True
                        
            if c_bid and not c_transaction_done:
                c_holding += 1
                c_pnl -= 750
                c_transaction_done=True
                
        else:       
            if fulfilled_ask and holding>0:
                
                
                holding -= 1
                pnl += ave
                hasSold = True
                bid = k*500+(1-k)*price
                ask = (1-k)*price+k*1500
                if n_asks >= n_bids:
                    isBid = True
            elif holding>0:
                
                done = False
                for i in new_bids:
                    if i>ask and not done:
                        holding -= 1
                        pnl += i
                        done = True
                        bid = k*500+(1-k)*price
                        ask = (1-k)*price+k*1500
                        if n_asks >= n_bids:
                            isBid = True
                        #print("customer success", i)

                    if i>1250 and not c_ask and not c_transaction_done:
                        c_holding -= 1
                        c_pnl += 1250
                        c_transaction_done=True
            if c_ask and not c_transaction_done:
                c_holding -= 1
                c_pnl += c_bid_price
                c_transaction_done=True
                
##        if fulfilled_ask or fulfilled_bid:
##            print("match")
##            
##        else:
##            print("no match")
##
##        print(ask_prices)
##        print(bid_prices)
##        print(bid)
##        print(ask)
##        print(price)
##        print(pnl)
##        print(holding)
##        print(isBid)
##        print(n_asks, n_bids)
##        print("\n \n \n")  
        
        
    print(theta, lamb)          
    pnl = pnl+theta*holding
    print("method 2:", pnl)
    c_pnl = c_pnl+theta*c_holding
    print("method 1:", c_pnl)
    
    if pnl>c_pnl:
        print("2 wins")
    else:
        print("1 wins")
    print("\n \n \n")
