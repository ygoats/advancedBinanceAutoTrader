#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:01 2020

@ygoats
"""

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

import apiData

import telegram_send

from time import sleep

from datetime import datetime

from requests import exceptions

import alphaSignals
import sysGrowth

import symbol_list

client = Client(apiData.APIKey, apiData.SecretKey)

symbolLong = []   ### where symbol goes for aquiring fill order
entryLong = []
targetLong = []  ### if price goes above or equals this price place server side order
stopLong = []  ## if price goes below or equals this price place server side order
quantityLong = [] ## quantity based off 250MAX position controlled within alphaSignals

symbolLongActive = [] 
entryLongActive = []
targetLongActive = [] 
stopLongActive = []  
quantityLongActive = []

symbolShort = []
entryShort = []
targetShort= []
stopShort = [] 
quantityShort = []

symbolShortActive = []
entryShortActive = []
targetShortActive = []
stopShortActive = [] 
quantityShortActive = []

sysList = []
sysTList = []

##SYSTEM 1 ATC5M[O]
##SYSTEM 2 ATC15M[O]
##SYSTEM 3 ATC1H[O]
##SYSTEM 4 ATC4H[O]
##SYSTEM 5 ATC5M[OI]
##SYSTEM 6 ATC15M[OI]
##SYSTEM 7 ATC1H[OI]
##SYSTEM 8 ATC4H[OI]
##SYSTEM 9 ATC5M[4:1]
##SYSTEM 10 ATC15M[4:1]
##SYSTEM 11 ATC1H[4:1]
##SYSTEM 12 ATC4H[4:1]
##SYSTEM 13 ATC5M[10:1]
##SYSTEM 14 ATC15M[10:1]
##SYSTEM 15 ATC1H[10:1]
##SYSTEM 16 ATC4H[10:1]
##SYSTEM 17 ATC5M[ATR62]
##SYSTEM 18 ATC15M[ATR62]
##SYSTEM 19 ATC1H[ATR62]
##SYSTEM 20 ATC4H[ATR62]
##SYSTEM 21 ATC5M[ATR100]
##SYSTEM 22 ATC15M[ATR100]
##SYSTEM 23 ATC1H[ATR100]
##SYSTEM 24 ATC4H[ATR100]
def checkSystem():
    lenSell = 0
    lenBuy = 0
    sysR = 0
    sysList = []
    sysTList = []
    
    print('Checking For Signals')
    
    #######This is where sysGrowth will analyze systems pnl trajectory and
    #####apply the best system to trade into the autotrader
    ###### ie. alphaSignals.trade2() ###this would be running trade2 system
    
    for xr in range(24):  ####24 is amount of systems we have to get the sysGrowth calcs
        sysR = sysGrowth.Main()[xr]
        #print(str(sysR))
        sysList.append(sysR)
    print('System Growth Calculations Stated')
    
    sysTList.append(sysGrowth.systemOne()[0])
    sysTList.append(sysGrowth.systemTwo()[0])
    sysTList.append(sysGrowth.systemThree()[0])
    sysTList.append(sysGrowth.systemFour()[0])
    sysTList.append(sysGrowth.systemFive()[0])
    sysTList.append(sysGrowth.systemSix()[0])
    sysTList.append(sysGrowth.systemSeven()[0])
    sysTList.append(sysGrowth.systemEight()[0])
    sysTList.append(sysGrowth.systemNine()[0])
    sysTList.append(sysGrowth.systemTen()[0])
    sysTList.append(sysGrowth.systemEleven()[0])
    sysTList.append(sysGrowth.systemTwelve()[0])
    sysTList.append(sysGrowth.systemThirteen()[0])
    sysTList.append(sysGrowth.systemFourteen()[0])
    sysTList.append(sysGrowth.systemFifteen()[0])
    sysTList.append(sysGrowth.systemSixteen()[0])
    sysTList.append(sysGrowth.systemSeventeen()[0])
    sysTList.append(sysGrowth.systemEighteen()[0])
    sysTList.append(sysGrowth.systemNineteen()[0])
    sysTList.append(sysGrowth.systemTwenty()[0])
    sysTList.append(sysGrowth.systemTwentyOne()[0])
    sysTList.append(sysGrowth.systemTwentyTwo()[0])
    sysTList.append(sysGrowth.systemTwentyThree()[0])
    sysTList.append(sysGrowth.systemTwentyFour()[0])

    print('System Sum Calculations Stated')
    
    return sysList, sysTList
            
def checkSignal():
    sysMin = []
    sysList = []
    sysTList = []
    sysTrack = []
    sysTracker = []
    averageSystem = 0
    minSysTotal = 0
    
    checkSystem()
    sysMin = checkSystem()[0] ###For Getting Top 7 PNL
    sysList = checkSystem()[0] ###Trajectory
    sysTList = checkSystem()[1] ###Total System
    
    maxSys = max(sysList)  
    maxSysT = max(sysTList) 
    indexSys = sysList.index(maxSys)
    indexSysT = sysTList.index(maxSysT)
    
    averageSystem = float(sum(sysTList) / 24)
    print('Average System Return: ' + str(averageSystem))
    if averageSystem <= -250:
        print('Resetting Trade History Tracker')
        telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| Resetting PNL Trackers Wait 6 Hours To Confirm Structure"])
        systemClear.Main()
        sleep(10)
        averageSystem = 0
        checkSystem()
        sysList = checkSystem()[0] ###Trajectory
        sysTList = checkSystem()[1] ###Total System
        
        maxSys = max(sysList)  
        maxSysT = max(sysTList) 
        indexSys = sysList.index(maxSys)
        indexSysT = sysTList.index(maxSysT)
        
    sysMin.sort()
    minSysTotal = sysMin[17]
    
    systemRun = False
    
    if maxSys >= 5 and maxSysT >= 10:
        if sysList[0] >= 1.11 and sysTList[0] >= minSysTotal:
            print('System 1 Is Canditate')
            sysTrack.append(sysTList[0])
            sysTracker.append(0)
        if sysList[1] >= 1.11 and sysTList[1] >= minSysTotal:
            print('System 2 Is Canditate')
            sysTrack.append(sysTList[1])
            sysTracker.append(1)
        if sysList[2] >= 1.11 and sysTList[2] >= minSysTotal:
            print('System 3 Is Canditate')
            sysTrack.append(sysTList[2])
            sysTracker.append(2)
        if sysList[3] >= 1.11 and sysTList[3] >= minSysTotal:
            print('System 4 Is Canditate')
            sysTrack.append(sysTList[3])
            sysTracker.append(3)
        if sysList[4] >= 1.11 and sysTList[4] >= minSysTotal:
            print('System 5 Is Canditate')
            sysTrack.append(sysTList[4])
            sysTracker.append(4)
        if sysList[5] >= 1.11 and sysTList[5] >= minSysTotal:
            print('System 6 Is Canditate')
            sysTrack.append(sysTList[5])
            sysTracker.append(5)
        if sysList[6] >= 1.11 and sysTList[6] >= minSysTotal:
            print('System 7 Is Canditate')
            sysTrack.append(sysTList[6])
            sysTracker.append(6)
        if sysList[7] >= 1.11 and sysTList[7] >= minSysTotal:
            print('System 8 Is Canditate')
            sysTrack.append(sysTList[7])
            sysTracker.append(7)
        if sysList[8] >= 1.11 and sysTList[8] >= minSysTotal:
            print('System 9 Is Canditate')
            sysTrack.append(sysTList[8])
            sysTracker.append(8)
        if sysList[9] >= 1.11 and sysTList[9] >= minSysTotal:
            print('System 10 Is Canditate')
            sysTrack.append(sysTList[9])
            sysTracker.append(9)
        if sysList[10] >= 1.11 and sysTList[10] >= minSysTotal:
            print('System 11 Is Canditate')
            sysTrack.append(sysTList[10])
            sysTracker.append(10)
        if sysList[11] >= 1.11 and sysTList[11] >= minSysTotal:
            print('System 12 Is Canditate')
            sysTrack.append(sysTList[11])
            sysTracker.append(11)
        if sysList[12] >= 1.11 and sysTList[12] >= minSysTotal:
            print('System 13 Is Canditate')
            sysTrack.append(sysTList[12])
            sysTracker.append(12)
        if sysList[13] >= 1.11 and sysTList[13] >= minSysTotal:
            print('System 14 Is Canditate')
            sysTrack.append(sysTList[13])
            sysTracker.append(13)
        if sysList[14] >= 1.11 and sysTList[14] >= minSysTotal:
            print('System 15 Is Canditate')
            sysTrack.append(sysTList[14])
            sysTracker.append(14)
        if sysList[15] >= 1.11 and sysTList[15] >= minSysTotal:
            print('System 16 Is Canditate')
            sysTrack.append(sysTList[15])
            sysTracker.append(15)
        if sysList[16] >= 1.11 and sysTList[16] >= minSysTotal:
            print('System 17 Is Canditate')
            sysTrack.append(sysTList[16])
            sysTracker.append(16)
        if sysList[17] >= 1.11 and sysTList[17] >= minSysTotal:
            print('System 18 Is Canditate')
            sysTrack.append(sysTList[17])
            sysTracker.append(17)
        if sysList[18] >= 1.11 and sysTList[18] >= minSysTotal:
            print('System 19 Is Canditate')
            sysTrack.append(sysTList[18])
            sysTracker.append(18)
        if sysList[19] >= 1.11 and sysTList[19] >= minSysTotal:
            print('System 20 Is Canditate')
            sysTrack.append(sysTList[19])
            sysTracker.append(19)
        if sysList[20] >= 1.11 and sysTList[20] >= minSysTotal:
            print('System 21 Is Canditate')
            sysTrack.append(sysTList[20])
            sysTracker.append(20)
        if sysList[21] >= 1.11 and sysTList[21] >= minSysTotal:
            print('System 22 Is Canditate')
            sysTrack.append(sysTList[21])
            sysTracker.append(21)
        if sysList[22] >= 1.11 and sysTList[22] >= minSysTotal:
            print('System 23 Is Canditate')
            sysTrack.append(sysTList[22])
            sysTracker.append(22)
        if sysList[23] >= 1.11 and sysTList[23] >= minSysTotal:
            print('System 24 Is Canditate')
            sysTrack.append(sysTList[23])
            sysTracker.append(23)
        print(sysTrack)
        print(sysTracker)
        lenSysTracker = len(sysTracker) 
        if lenSysTracker > 0: 
            maxTrack = max(sysTrack)
            indexTrack = sysTrack.index(maxTrack)
            indexUsed = sysTracker[indexTrack]
            if indexUsed == 0 and sysList[0] > -11.11: 
                print('Running System 1')
                alphaSignals.system1()
                systemRun = True
            if indexUsed == 1 and sysList[1] > -11.11: 
                print('Running System 2')
                alphaSignals.system2()
                systemRun = True
            if indexUsed == 2 and sysList[2] > -11.11: 
                print('Running System 3')
                alphaSignals.system3()
                systemRun = True
            if indexUsed == 3 and sysList[3] > -11.11: 
                print('Running System 4')
                alphaSignals.system4()
                systemRun = True
            if indexUsed == 4 and sysList[4] > -11.11: 
                print('Running System 5')
                alphaSignals.system5()
                systemRun = True
            if indexUsed == 5 and sysList[5] > -11.11: 
                print('Running System 6')
                alphaSignals.system6()
                systemRun = True
            if indexUsed == 6 and sysList[6] > -11.11: 
                print('Running System 7')
                alphaSignals.system7()
                systemRun = True
            if indexUsed == 7 and sysList[7] > -11.11: 
                print('Running System 8')
                alphaSignals.system8()
                systemRun = True
            if indexUsed == 8 and sysList[8] > -11.11: 
                print('Running System 9')
                alphaSignals.system9()
                systemRun = True
            if indexUsed == 9 and sysList[9] > -11.11: 
                print('Running System 10')
                alphaSignals.system10()
                systemRun = True
            if indexUsed == 10 and sysList[10] > -11.11: 
                print('Running System 11')
                alphaSignals.system11()
                systemRun = True
            if indexUsed == 11 and sysList[11] > -11.11: 
                print('Running System 12')
                alphaSignals.system12()
                systemRun = True
            if indexUsed == 12 and sysList[12] > -11.11: 
                print('Running System 13')
                alphaSignals.system13()
                systemRun = True
            if indexUsed == 13 and sysList[13] > -11.11: 
                print('Running System 14')
                alphaSignals.system14()
                systemRun = True
            if indexUsed == 14 and sysList[14] > -11.11: 
                print('Running System 15')
                alphaSignals.system15()
                systemRun = True
            if indexUsed == 15 and sysList[15] > -11.11: 
                print('Running System 16')
                alphaSignals.system16()
                systemRun = True
            if indexUsed == 16 and sysList[16] > -11.11: 
                print('Running System 17')
                alphaSignals.system17()
                systemRun = True
            if indexUsed == 17 and sysList[17] > -11.11: 
                print('Running System 18')
                alphaSignals.system18()
                systemRun = True
            if indexUsed == 18 and sysList[18] > -11.11: 
                print('Running System 19')
                alphaSignals.system19()
                systemRun = True
            if indexUsed == 19 and sysList [19] > -11.11: 
                print('Running System 20')
                alphaSignals.system20()
                systemRun = True
            if indexUsed == 20 and sysList[20] > -11.11: 
                print('Running System 21')
                alphaSignals.system21()
                systemRun = True
            if indexUsed == 21 and sysList[21] > -11.11: 
                print('Running System 22')
                alphaSignals.system22()
                systemRun = True
            if indexUsed == 22 and sysList[22] > -11.11: 
                print('Running System 23')
                alphaSignals.system23()
                systemRun = True
            if indexUsed == 23 and sysList[23] > -11.11: 
                print('Running System 24')
                alphaSignals.system24()
                systemRun = True                
        else:
            print('Head To Fucking Lake Brother!')
            sleep(15)
            systemRun = False
            
        if systemRun == True:
                
            lenBuy = len(alphaSignals.symbol_listActiveBuy)
            lenSell = len(alphaSignals.symbol_listActiveSell)
            lenActive = len(symbolLong) + len(symbolShort) #### changed because T si always in saved live state
            
            if lenBuy > 0 and lenActive <= 9:
                
                print('Signal Found ' + str(alphaSignals.symbol_listActiveBuy[0]))
                symbolLong.append(alphaSignals.symbol_listActiveBuy[0])
                
                if alphaSignals.buy_PriceLong[0] >= 1 and alphaSignals.buy_PriceLong[0] < 10:
                    entryLong.append(str("{:.3f}".format(alphaSignals.buy_PriceLong[0])))
                    targetLong.append(str("{:.3f}".format(alphaSignals.target_PriceLong[0])))
                    stopLong.append(str("{:.3f}".format(alphaSignals.stop_PriceLong[0])))
                    quantityLong.append(int(alphaSignals.qty_Long[0]))              
                    
                elif alphaSignals.buy_PriceLong[0] >= 10 and alphaSignals.buy_PriceLong[0] <= 250:
                    entryLong.append(str("{:.2f}".format(alphaSignals.buy_PriceLong[0])))
                    targetLong.append(str("{:.2f}".format(alphaSignals.target_PriceLong[0])))
                    stopLong.append(str("{:.2f}".format(alphaSignals.stop_PriceLong[0])))
                    quantityLong.append(int(alphaSignals.qty_Long[0])) 
    
                elif alphaSignals.buy_PriceLong[0] > 250:
                    entryLong.append(str("{:.2f}".format(alphaSignals.buy_PriceLong[0])))
                    targetLong.append(str("{:.2f}".format(alphaSignals.target_PriceLong[0])))
                    stopLong.append(str("{:.2f}".format(alphaSignals.stop_PriceLong[0])))
                    quantityLong.append(str("{:.1f}".format(alphaSignals.qty_Long[0])))
                    
                else:
                    entryLong.append(str("{:.4f}".format(alphaSignals.buy_PriceLong[0])))
                    targetLong.append(str("{:.4f}".format(alphaSignals.target_PriceLong[0])))
                    stopLong.append(str("{:.4f}".format(alphaSignals.stop_PriceLong[0])))
                    quantityLong.append(int(alphaSignals.qty_Long[0]))
                    
                alphaSignals.symbol_listActiveBuy.remove(alphaSignals.symbol_listActiveBuy[0])
                alphaSignals.buy_PriceLong.remove(alphaSignals.buy_PriceLong[0])
                alphaSignals.target_PriceLong.remove(alphaSignals.target_PriceLong[0])
                alphaSignals.stop_PriceLong.remove(alphaSignals.stop_PriceLong[0])
                alphaSignals.qty_Long.remove(alphaSignals.qty_Long[0])
    
            if lenSell > 0 and lenActive <= 9:
                
                print('Signal Found ' + str(alphaSignals.symbol_listActiveSell[0]))
                symbolShort.append(alphaSignals.symbol_listActiveSell[0])
                
                if alphaSignals.buy_PriceShort[0] >= 1 and alphaSignals.buy_PriceShort[0] < 10:
                    entryShort.append(str("{:.3f}".format(alphaSignals.buy_PriceShort[0])))
                    targetShort.append(str("{:.3f}".format(alphaSignals.target_PriceShort[0])))
                    stopShort.append(str("{:.3f}".format(alphaSignals.stop_PriceShort[0])))
                    quantityShort.append(int(alphaSignals.qty_Short[0]))
                    
                elif alphaSignals.buy_PriceShort[0] >= 10 and alphaSignals.buy_PriceShort[0] <= 250:
                    entryShort.append(str("{:.2f}".format(alphaSignals.buy_PriceShort[0])))
                    targetShort.append(str("{:.2f}".format(alphaSignals.target_PriceShort[0])))
                    stopShort.append(str("{:.2f}".format(alphaSignals.stop_PriceShort[0])))
                    quantityShort.append(int(alphaSignals.qty_Short[0]))
                    
                elif alphaSignals.buy_PriceShort[0] > 250:
                    entryShort.append(str("{:.2f}".format(alphaSignals.buy_PriceShort[0])))
                    targetShort.append(str("{:.2f}".format(alphaSignals.target_PriceShort[0])))
                    stopShort.append(str("{:.2f}".format(alphaSignals.stop_PriceShort[0])))
                    quantityShort.append(str("{:.1f}".format(alphaSignals.qty_Short[0])))
                    
                else:
                    entryShort.append(str("{:.4f}".format(alphaSignals.buy_PriceShort[0])))
                    targetShort.append(str("{:.4f}".format(alphaSignals.target_PriceShort[0])))
                    stopShort.append(str("{:.4f}".format(alphaSignals.stop_PriceShort[0])))
                    quantityShort.append(int(alphaSignals.qty_Short[0]))
                
                alphaSignals.symbol_listActiveSell.remove(alphaSignals.symbol_listActiveSell[0])
                alphaSignals.buy_PriceShort.remove(alphaSignals.buy_PriceShort[0])
                alphaSignals.target_PriceShort.remove(alphaSignals.target_PriceShort[0])
                alphaSignals.stop_PriceShort.remove(alphaSignals.stop_PriceShort[0])
                alphaSignals.qty_Short.remove(alphaSignals.qty_Short[0])
                
    else:
        print('No Trajectory PNLS are above threshhold, please go to the lake.')
        sleep(5)

def enterLongSignals():
    
    lenTickerLong = len(symbolLong)
    
    if lenTickerLong > 0:
        for bb in range(lenTickerLong):
            
            waitingLongEntry = False
            longFilled = False
            y = 0
            
            print('Place Buy Limit Order ' + str(symbolLong[bb]))
            startOrder = client.futures_create_order(
            symbol=symbolLong[bb],
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantityLong[bb],
            price=entryLong[bb])
            
            waitingLongEntry = True
            
            while waitingLongEntry == True:
                
                try:
                    positionLong = client.futures_position_information(symbol = symbolLong[bb])
                    positionLongL = float(positionLong[0]['positionAmt'])
                    
                    openOrder = client.futures_get_open_orders(symbol = symbolLong[bb])
                    positionL = float(openOrder[0]['executedQty'])
                    
                    lenOrderLong = len(openOrder)
                    
                    y = y + 1
                    if lenOrderLong == 0:
                        print('Position Filled')
                        waitingLongEntry = False
                        longFilled = True
                    if y == 15 and positionL > 0:
                        print('Position is partially filled')
                        openOrder = client.futures_get_open_orders(symbol = symbolLong[bb])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolLong[bb])
                        print('Cancelling rest of order')
                        waitingLongEntry = False
                        longFilled = True
                    if y == 15 and positionLongL == 0:
                        print('Cannot fill order in time')
                        openOrder = client.futures_get_open_orders(symbol = symbolLong[bb])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolLong[bb])
                        print('Cancelling rest of order')
                        waitingLongEntry = False
                        longFilled = False
                        print('Moving on to next signal')
                        symbolLong.remove(symbolLong[bb])
                        entryLong.remove(entryLong[bb])
                        targetLong.remove(targetLong[bb])
                        stopLong.remove(stopLong[bb])
                        quantityLong.remove(quantityLong[bb])
                        break    
                    sleep(1)
                
                except IndexError as e:
                    print(e)
                    print('Position Filled Instantly')
                    waitingLongEntry = False
                    longFilled = True
            
            if longFilled == True:
                
                ####REMOVE IF TG FUCKS
                telegram_send.send(disable_web_page_preview=True, conf='user1.conf',messages=["|||||AlphaTrader Buy||||| " + str(symbolLong[bb]) + "\n" + \
                                                    "Entry: " + str("{:.4f}".format(float(positionLong[0]['entryPrice']))) + "\n" + \
                                                    "Exit: " + str("{:.4f}".format(float(stopLong[bb]))) + "\n" + \
                                                    "Target: " + str("{:.4f}".format(float(targetLong[bb]))) + "\n" + \
                                                    "Quantity: " + str("{:.4f}".format(float(positionLong[0]['positionAmt']))) + "\n" +
                                                    "https://www.binance.com/en/trade/" + str(symbolLong[bb]) + "?type=perpetual"])
                    
                positionLong = client.futures_position_information(symbol = symbolLong[bb])
                
                symbolLongActive.append(symbolLong[bb])
                entryLongActive.append(positionLong[0]['entryPrice'])
                targetLongActive.append(targetLong[bb])
                stopLongActive.append(stopLong[bb])
                quantityLongActive.append(positionLong[0]['positionAmt'])
                
                symbolLong.remove(symbolLong[bb])
                entryLong.remove(entryLong[bb])
                targetLong.remove(targetLong[bb])
                stopLong.remove(stopLong[bb])
                quantityLong.remove(quantityLong[bb])
                
                break
            break
        
def enterShortSignals():
    
    lenTickerShort = len(symbolShort)
           
    if lenTickerShort > 0:
        for ss in range(lenTickerShort):
            
            waitingShortEntry = True
            shortFilled = False
            y = 0            
            
            print('Place Sell Limit Order ' + str(symbolShort[ss]))
            startOrder = client.futures_create_order(
            symbol=symbolShort[ss],
            side=SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantityShort[ss],
            price=entryShort[ss])
            
            while waitingShortEntry == True:
                
                try:
                    positionShort = client.futures_position_information(symbol = symbolShort[ss])
                    positionShortS = float(positionShort[ss]['positionAmt'])
                    
                    openOrder = client.futures_get_open_orders(symbol = symbolShort[ss])
                    positionS = float(openOrder[ss]['executedQty'])
                    
                    lenOrderShort = len(openOrder)
                    
                    
                    y = y + 1
                    if lenOrderShort == 0:
                        print('Position Filled')
                        waitingShortEntry = False
                        shortFilled = True
                    if y == 15 and positionS < 0:
                        print('Position is partially filled')
                        openOrder = client.futures_get_open_orders(symbol = symbolShort[ss])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolShort[ss])
                        print('Cancelling rest of order')
                        waitingShortEntry = False
                        shortFilled = True
                    if y == 15 and positionShortS == 0:
                        print('Cannot fill order in time')
                        openOrder = client.futures_get_open_orders(symbol = symbolShort[ss])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolShort[ss])
                        print('Cancelling rest of order')
                        waitingShortEntry = False
                        print('Moving on to next signal')
                        shortFilled = False
                        symbolShort.remove(symbolShort[ss])
                        entryShort.remove(entryShort[ss])
                        targetShort.remove(targetShort[ss])
                        stopShort.remove(stopShort[ss])
                        quantityShort.remove(quantityShort[ss])
                        break
                    sleep(1)
            
                except IndexError as e:
                    print(e)
                    print('Position Filled Instantly')
                    waitingShortEntry = False  
                    shortFilled = True
            
            if shortFilled == True:
                
                ####REMOVE IF TG FUCKS
                telegram_send.send(disable_web_page_preview=True, conf='user1.conf',messages=["|||||AlphaTrader Sell||||| " + str(symbolShort[ss]) + "\n" + \
                                                                    "Entry: " + str("{:.4f}".format(float(positionShort[0]['entryPrice']))) + "\n" + \
                                                                    "Exit: " + str("{:.4f}".format(float(stopShort[ss]))) + "\n" + \
                                                                    "Target: " + str("{:.4f}".format(float(targetShort[ss]))) + "\n" + \
                                                                    "Quantity: " + str("{:.4f}".format(float(positionShort[0]['positionAmt']))) + "\n" +
                                                                    "https://www.binance.com/en/trade/" + str(symbolShort[ss]) + "?type=perpetual"])
                
                positionShort = client.futures_position_information(symbol = symbolShort[ss])
                    
                symbolShortActive.append(symbolShort[ss])
                entryShortActive.append(positionShort[0]['entryPrice'])
                targetShortActive.append(targetShort[ss])
                stopShortActive.append(stopShort[ss])
                quantityShortActive.append(positionShort[0]['positionAmt'])
                
                symbolShort.remove(symbolShort[ss])
                entryShort.remove(entryShort[ss])
                targetShort.remove(targetShort[ss])
                stopShort.remove(stopShort[ss])
                quantityShort.remove(quantityShort[ss])
                break
            break
            
def exitLongSignals():
    lengthActiveBuy = len(symbolLongActive)
    
    if lengthActiveBuy > 0:
        
        for eb in range(lengthActiveBuy):
            pnlB = 0
            waitingLongEntry = False
            y = 0
    
            print('Checking ' + str(symbolLongActive[eb]) + ' For exit!')
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbolLongActive[eb],interval=KLINE_INTERVAL_5MINUTE, limit=1)
            currentPrice = float(klines[0][4])
            
            print('currentPrice: ' + str(currentPrice))
            print('target: ' + str(targetLongActive[eb]))
            print('stop: ' + str(stopLongActive[eb]))
            
            if currentPrice >= float(targetLongActive[eb]) or currentPrice <= float(stopLongActive[eb]):

                positionLongE = client.futures_position_information(symbol = symbolLongActive[eb])
                positionLongLE = float(positionLongE[0]['positionAmt'])               
                try:
                    
                    print('Exit Long Limit Order ' + str(symbolLongActive[eb]))
                    startOrder = client.futures_create_order(
                    symbol=symbolLongActive[eb],
                    side=SIDE_SELL,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=positionLongLE,
                    price=targetLongActive[eb])
                    waitingLongEntry = True
                except BinanceAPIException as e:
                    pnlB = (float(currentPrice) - float(entryLongActive[eb])) * float(quantityLongActive[eb])
                
                    telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolLongActive[eb]) + " Closing Long Trade, PNL: " + str("{:.4f}".format(float(pnlB)))])
                    
                    f = open('alphaData.txt', 'a')
                    f.write("\n" + str("{:.4f}".format(pnlB)))
                    f.close()
                    
                    f = open('alphaLog.txt', 'a')
                    f.write("\n" + str(t) + "    " + str(symbolLongActive[eb]) + "    " + str("{:.4f}".format(float(entryLongActive[eb]))) \
                    + "    " +  str("{:.4f}".format(float(targetLongActive[eb]))) + "    " +  str("{:.4f}".format(float(stopLongActive[eb]))) + "    " \
                    + "    " + str("{:.4f}".format(float(quantityLongActive[eb])))   + "    " + str("{:.4f}".format(pnlB)))
                    f.close()                    
    
                    alphaSignals.symbol_list.append(symbolLongActive[eb])
                    symbolLongActive.remove(symbolLongActive[eb])
                    entryLongActive.remove(entryLongActive[eb])
                    targetLongActive.remove(targetLongActive[eb])
                    stopLongActive.remove(stopLongActive[eb])
                    quantityLongActive.remove(quantityLongActive[eb])
                    waitingLongEntry = False
                    break
                
                while waitingLongEntry == True:
                    
                    positionLongActive = client.futures_position_information(symbol = symbolLongActive[eb])
                    positionLA = float(positionLongActive[0]['positionAmt'])
                    y = y + 1
                    
                    if positionLA == 0:
                        print(str(symbolLongActive[eb]) + ' Long Trade Closed!')
                        pnlB = (float(currentPrice) - float(entryLongActive[eb])) * float(quantityLongActive[eb])
                
                        telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolLongActive[eb]) + " Closing Long Trade, PNL: " + str("{:.4f}".format(float(pnlB)))])
                    
                        f = open('alphaData.txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlB)))
                        f.close()
                        
                        f = open('alphaLog.txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbolLongActive[eb]) + "    " + str("{:.4f}".format(float(entryLongActive[eb]))) \
                        + "    " +  str("{:.4f}".format(float(targetLongActive[eb]))) + "    " +  str("{:.4f}".format(float(stopLongActive[eb]))) + "    " \
                        + "    " + str("{:.4f}".format(float(quantityLongActive[eb])))   + "    " + str("{:.4f}".format(pnlB)))
                        f.close()
        
                        alphaSignals.symbol_list.append(symbolLongActive[eb])
                        symbolLongActive.remove(symbolLongActive[eb])
                        entryLongActive.remove(entryLongActive[eb])
                        targetLongActive.remove(targetLongActive[eb])
                        stopLongActive.remove(stopLongActive[eb])
                        quantityLongActive.remove(quantityLongActive[eb])
                        break
                    if y == 15 and positionLA > 0:
                        print('Position is partially filled Flatten The rest ' + str(symbolLongActive[eb]))
                        openOrder = client.futures_get_open_orders(symbol = symbolLongActive[eb])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolLongActive[eb])
                        print('Cancelling rest of order')
                        ####FLATTENTRADE HERE*******
                        
                        positionLongActive = client.futures_position_information(symbol = symbolLongActive[eb])
                        
                        print('Exit Long Market Order ' + str(symbolLongActive[eb]))
                        startOrder = client.futures_create_order(
                        symbol=symbolLongActive[eb],
                        side=SIDE_SELL,
                        type=ORDER_TYPE_MARKET,
                        quantity=positionLongActive[0]['positionAmt'])
                        
                        print(str(symbolLongActive[eb]) + ' Long Trade Closed!')
                        pnlB = (float(currentPrice) - float(entryLongActive[eb])) * float(quantityLongActive[eb])
                
                        telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolLongActive[eb]) + " Closing Long Trade, PNL: " + str("{:.4f}".format(float(pnlB)))])
                        
                        f = open('alphaData.txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlB)))
                        f.close()
                        
                        f = open('alphaLog.txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbolLongActive[eb]) + "    " + str("{:.4f}".format(float(entryLongActive[eb]))) \
                        + "    " +  str("{:.4f}".format(float(targetLongActive[eb]))) + "    " +  str("{:.4f}".format(float(stopLongActive[eb]))) + "    " \
                        + "    " + str("{:.4f}".format(float(quantityLongActive[eb])))   + "    " + str("{:.4f}".format(pnlB)))
                        f.close()                        
        
                        alphaSignals.symbol_list.append(symbolLongActive[eb])
                        symbolLongActive.remove(symbolLongActive[eb])
                        entryLongActive.remove(entryLongActive[eb])
                        targetLongActive.remove(targetLongActive[eb])
                        stopLongActive.remove(stopLongActive[eb])
                        quantityLongActive.remove(quantityLongActive[eb])
                        break
                    sleep(1)
    else:
        print('No Long Trades Active')
        
def exitShortSignals(): 
    lengthActiveSell = len(symbolShortActive)
         
    if lengthActiveSell > 0:
        for es in range(lengthActiveSell):
            pnlS = 0
            waitingShortEntry = False
            y = 0
            
            print('Checking ' + str(symbolShortActive[es]) + ' For exit!')
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbolShortActive[es],interval=KLINE_INTERVAL_5MINUTE, limit=1)
            currentPrice = float(klines[0][4])
            
            print('currentPrice: ' + str(currentPrice))
            print('target: ' + str(targetShortActive[es]))
            print('stop: ' + str(stopShortActive[es]))           
            
            if currentPrice <= float(targetShortActive[es]) or currentPrice >= float(stopShortActive[es]):
                
                positionShortE = client.futures_position_information(symbol = symbolShortActive[es])
                positionShortSE = float(positionShortE[0]['positionAmt'])                
                
                print('Exit Short Limit Order ' + str(symbolShortActive[es]))
                try:
                    startOrder = client.futures_create_order(
                    symbol=symbolShortActive[es],
                    side=SIDE_BUY,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=abs(positionShortSE),
                    price=targetShortActive[es])
                    waitingShortEntry = True
                except BinanceAPIException as e:
                    print(e)
                    pnlS = (float(currentPrice) - float(entryShortActive[es])) * float(quantityShortActive[es])
                
                    telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolShortActive[es]) + " Closing Short Trade, PNL: " + str("{:.4f}".format(float(pnlS)))])
                    
                    f = open('alphaData.txt', 'a')
                    f.write("\n" + str("{:.4f}".format(pnlS)))
                    f.close()
                    
                    f = open('alphaLog.txt', 'a')
                    f.write("\n" + str(t) + "    " + str(symbolShortActive[es]) + "    " + str("{:.4f}".format(float(entryShortActive[es]))) \
                    + "    " +  str("{:.4f}".format(float(targetShortActive[es]))) + "    " +  str("{:.4f}".format(float(stopShortActive[es]))) + "    " \
                    + "    " + str("{:.4f}".format(float(quantityShortActive[es])))   + "    " + str("{:.4f}".format(pnlS)))
                    f.close()                    
                        
                    alphaSignals.symbol_list.append(symbolShortActive[es])
                    symbolShortActive.remove(symbolShortActive[es])
                    entryShortActive.remove(entryShortActive[es])
                    targetShortActive.remove(targetShortActive[es])
                    stopShortActive.remove(stopShortActive[es])
                    quantityShortActive.remove(quantityShortActive[es])
                    waitingShortEntry = False
                    break

                while waitingShortEntry == True:
                    
                    positionShortActive = client.futures_position_information(symbol = symbolShortActive[es])
                    positionSA = float(positionShortActive[0]['positionAmt'])
                    y = y + 1
                    
                    if positionSA == 0:
                        print(str(symbolShortActive[es]) + ' Short Closed Trade!')
                        pnlS = (float(currentPrice) - float(entryShortActive[es])) * float(quantityShortActive[es])
                
                        telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolShortActive[es]) + " Closing Short Trade, PNL: " + str("{:.4f}".format(float(pnlS)))])
                        
                        f = open('alphaData.txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlS)))
                        f.close()
                        
                        f = open('alphaLog.txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbolShortActive[es]) + "    " + str("{:.4f}".format(float(entryShortActive[es]))) \
                        + "    " +  str("{:.4f}".format(float(targetShortActive[es]))) + "    " +  str("{:.4f}".format(float(stopShortActive[es]))) + "    " \
                        + "    " + str("{:.4f}".format(float(quantityShortActive[es])))   + "    " + str("{:.4f}".format(pnlS)))
                        f.close()                        
                        
                        alphaSignals.symbol_list.append(symbolShortActive[es])
                        symbolShortActive.remove(symbolShortActive[es])
                        entryShortActive.remove(entryShortActive[es])
                        targetShortActive.remove(targetShortActive[es])
                        stopShortActive.remove(stopShortActive[es])
                        quantityShortActive.remove(quantityShortActive[es]) 
                        break
                    if y == 15 and positionSA < 0:
                        print('Position is partially filled Flatten The rest ' + str(symbolShortActive[es]))
                        openOrder = client.futures_get_open_orders(symbol = symbolShortActive[es])
                        orderID = openOrder[0]['orderId']  ##### returns the orderID
                        cancelOrder = client.futures_cancel_order(orderId=orderID, symbol= symbolShortActive[es])
                        print('Cancelling rest of order')
                        ####FLATTENTRADE HERE*******
                        
                        print('Exit Short Market Order ' + str(symbolShortActive[es]))
                        startOrder = client.futures_create_order(
                        symbol=symbolShortActive[es],
                        side=SIDE_BUY,
                        type=ORDER_TYPE_MARKET,
                        quantity=abs(positionSA))
                        
                        print(str(symbolShortActive[es]) + ' Short Closed Trade!')
                        pnlS = (float(currentPrice) - float(entryShortActive[es])) * float(quantityShortActive[es])
                
                        telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| " + str(symbolShortActive[es]) + " Closing Short Trade, PNL: " + str("{:.4f}".format(float(pnlS)))])
                        
                        f = open('alphaData.txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlS)))
                        f.close()
                        
                        f = open('alphaLog.txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbolShortActive[es]) + "    " + str("{:.4f}".format(float(entryShortActive[es]))) \
                        + "    " +  str("{:.4f}".format(float(targetShortActive[es]))) + "    " +  str("{:.4f}".format(float(stopShortActive[es]))) + "    " \
                        + "    " + str("{:.4f}".format(float(quantityShortActive[es])))   + "    " + str("{:.4f}".format(pnlS)))
                        f.close()                        
                        
                        alphaSignals.symbol_list.append(symbolShortActive[es])
                        symbolShortActive.remove(symbolShortActive[es])
                        entryShortActive.remove(entryShortActive[es])
                        targetShortActive.remove(targetShortActive[es])
                        stopShortActive.remove(stopShortActive[es])
                        quantityShortActive.remove(quantityShortActive[es])                                     
                        break
                    sleep(1)
    else:
        print('No Short Trades Active')
        
def Main():
    
    initialProcessing = True
    
    now = datetime.now()
    tt = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    print("[Connection Established Alpha Autotrader Live For Futures!]")
    print(str(tt))
    telegram_send.send(conf='user1.conf',messages=["|||||alphaTrader||||| Connection Established @ " + str(tt)])
    
    checkSystem()
    
    while initialProcessing == True:
        lenActive = 0
        now = datetime.now()
        ttt = now.strftime("%M:%S")
        try:
            if ttt >= "05:00" and ttt <= "05:15":
                checkSystem()
            if ttt >= "30:00" and ttt <= "30:15":
                checkSystem()
                
            lenActive = float(len(symbolLongActive) + len(symbolShortActive))
            print('Current Systems Open: ' + str(lenActive))
            if lenActive <= 7:
                checkSignal()
    
            enterLongSignals()
            enterShortSignals()
            exitLongSignals()
            exitShortSignals()
        except Exception as e:
            print(str(e))
            sleep(10)
            continue
        
    
if __name__ == '__main__':
    Main()
