import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iterations = 10
theta_list = []
lamb_list=[]
min_list = []
max_list = []

data = []
for buy_price in range(500, 1600, 10):
    for sell_price in range(buy_price, 1600, 10):

        pnl_list=[]
        for _ in range(100):
            isBuy = True
            pnl = 0
            holdings = 0

            for _ in range(iterations):
                
                theta = 500+1000*np.random.random_sample()
                
                theta_list.append(theta)
                lamb = 50 + 150*np.random.random_sample()
                
                lamb_list.append(lamb)
                num_c = np.random.normal(500, 30, 1)
                num = int(np.floor(num_c[0]))
                
                
                max_price = lamb + theta - 1
                min_price = theta - lamb + 1
                
                
                if isBuy and buy_price>min_price:
                    isBuy = False
                    #print("bought at ", buy_price)
                    holdings += 1
                else:
                    if sell_price<max_price and holdings>0:
                        pnl += sell_price - buy_price
                        holdings -= 1
                        #print("sold at ", sell_price)
                    
                    isBuy = True

            pnl_list.append(pnl)

        ##min_np = np.array(min_list)
        ##max_np = np.array(max_list)
        ##plt.hist(max_np, bins=50)
        ##plt.show()

        ave = sum(pnl_list)/len(pnl_list)
        data.append((ave, buy_price, sell_price))


data.sort()
print(data[-5:])


