#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:13:56 2022

@author: stanley
"""

"""
bot0: first attempt at reactive markets

"""

import random


def submit_market(state, my_history, period_history):
    """
    Given user defined state and history of the trades you executed
    last round, come up with a new market for this round.
    
    state is initially an empty dictionary
    
    Each trade in my_history is a dict of the format
    {
         "size": volume traded,
         "price": price traded at,
         "dir": either "buy" or "sell",
         "id_against": the type of party traded against, either "team"
                         or "customer"
    }
    
    Each trade in period_history is a dict of the format
    {
        "size": volume traded (will always be 1),
        "price": price traded at,
        "dir": either "buy" or "sell" depending on the team's action (not the customer's),
        "id_against": "customer",
    }
    """

    """
    One example of state you might want to keep track of are the last buy and sell prices
    you submitted to the market
    """
    state["k"]=0.1
    k = state["k"]
    if "bid" not in state:
        state["bid"]=k*500+(1-k)*1000
    if "sell" not in state:
        state["sell"]=k*1500+(1-k)*1000

    prices = [trade["price"] for trade in period_history]
    
    n_bid = 0
    n_ask = 0
    for trade in period_history:
        if trade["dir"]=="buy":
            n_bid += 1
        if trade["dir"]=="sell":
            n_ask += 1
    if "round" not in state:
        state["round"] = 0
    new_price = 1000
    if state["round"]>0:
        new_price = sum(prices)/len(prices)
    
    
    if len(my_history)>0:
        state["bid"] = k*500+(1-k)*new_price
        state["ask"] = k*1500 + (1-k)*new_price

    if n_ask>n_bid:
        isBid = True
    else:
        isBid = False
   
    state["round"] += 1
        
    if isBid:
        return {
            "buy": {
                    "price": state["bid"],
                    "size": 10
                    },
            "sell": {
                    "price": state["sell"],
                    "size": 0
                    },
            }
    else:
        return {
            "buy": {
                    "price": state["bid"],
                    "size": 0
                    },
            "sell": {
                    "price": state["sell"],
                    "size": 10
                    },
            }

    """
    May want to keep track of round number
    """
    
    

    
    

