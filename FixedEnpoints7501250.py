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
    state["buy_price"] = 750
    state["sell_price"] = 1250

    """
    May want to keep track of round number
    """
    if "round" not in state:
        state["round"] = 0
    state["round"] += 1
    

    """
    One quantity you may wish to look at are the number of buys and sells you
    executed last round
    """
    num_buys = 0
    num_sells = 0
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
            
    if total_buys > total_sells:
        to_buy, to_sell = 0, 10
    else:
        to_buy, to_sell = 10, 0
    
    return {
            "buy": {
                    "price": 750,
                    "size": to_buy
                    },
            "sell": {
                    "price": 1250,
                    "size": to_sell
                    },
            }
