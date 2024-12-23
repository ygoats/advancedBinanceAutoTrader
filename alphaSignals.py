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

from time import sleep

from datetime import datetime

from requests import exceptions

import symbol_list

symbol_listActiveBuy = []
symbol_listActiveSell = []

buy_PriceLong = []
stop_PriceLong = []
target_PriceLong = []
qty_Long = []

buy_PriceShort = []
stop_PriceShort = []
target_PriceShort = []
qty_Short = []

symbol_list = symbol_list.symbol_list

############################################################
#####################PARSING SYSTEM 1#######################
############################################################
#ATC5M[M10][F]
def system1():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        print(str(symbol_list[s]))
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.005
        targetShort = float(currentPrice) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.995
        targetLong = float(currentPrice) + float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            print(str(symbol_list[s] + 'SignalFound'))
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            print(str(symbol_list[s] + 'SignalFound'))
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
            print(str(symbol_list[s] + 'SignalFound'))    
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
            print(str(symbol_list[s] + 'SignalFound'))    
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 2#######################
############################################################
#ATC15M[M10][F]
def system2():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.005
        targetShort = float(currentPrice) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.995
        targetLong = float(currentPrice) + float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 3#######################
############################################################
#ATC1H[M10][F]
def system3():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        #print(symbol_list[s])
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.005
        targetShort = float(currentPrice) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.995
        targetLong = float(currentPrice) + float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 4#######################
############################################################
#ATC4H[M10][F]
def system4():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.005
        targetShort = float(currentPrice) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.995
        targetLong = float(currentPrice) + float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 5#######################
############################################################
#ATC5M[M10][F][OI]       
def system5():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 6#######################
############################################################
#ATC15M[M10][F][OI]       
def system6():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 7#######################
############################################################
#ATC1H[M10][F][OI]       
def system7():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 8#######################
############################################################
#ATC4H[M10][F][OI]       
def system8():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            symbolLength = float(symbolLength) - 1
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            symbolLength = float(symbolLength) - 1
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 9#######################
############################################################
#ATC5M[M10][F][4:1]       
def system9():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 4) 
        riskTenS = (stopRiskRangeS * 4)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 10#######################
############################################################
#ATC15M[M10][F][4:1]       
def system10():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 4) 
        riskTenS = (stopRiskRangeS * 4)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 11#######################
############################################################
#ATC1H[M10][F][4:1]       
def system11():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
              
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 4) 
        riskTenS = (stopRiskRangeS * 4)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
            
############################################################
#####################PARSING SYSTEM 12#######################
############################################################
#ATC4H[M10][F][4:1]       
def system12():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 4) 
        riskTenS = (stopRiskRangeS * 4)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break

############################################################
#####################PARSING SYSTEM 13#######################
############################################################
#ATC5M[M10][F][10:1]       
def system13():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 10) 
        riskTenS = (stopRiskRangeS * 10)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 14#######################
############################################################
#ATC15M[M10][F][10:1]       
def system14():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
        
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
            
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 10) 
        riskTenS = (stopRiskRangeS * 10)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 15#######################
############################################################
#ATC1H[M10][F][10:1]       
def system15():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
              
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 10) 
        riskTenS = (stopRiskRangeS * 10)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
            
############################################################
#####################PARSING SYSTEM 16#######################
############################################################
#ATC4H[M10][F][10:1]       
def system16():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        currentPrice = float(klines[49][4])
        
        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        riskTenB = (stopRiskRangeB * 10) 
        riskTenS = (stopRiskRangeS * 10)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and targetRangeB > riskTenB:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and targetRangeS > riskTenS:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break

############################################################
#####################PARSING SYSTEM 17#######################
############################################################
#ATC5M[M10][F][ATR62]       
def system17():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday)  

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        atrAvg = float(atrAvg) * .625
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break

############################################################
#####################PARSING SYSTEM 18#######################
############################################################
#ATC15M[M10][F][ATR62]       
def system18():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        atrAvg = float(atrAvg) * .625
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
            
############################################################
#####################PARSING SYSTEM 19#######################
############################################################
#ATC1H[M10][F][ATR62]       
def system19():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        atrAvg = float(atrAvg) * .625
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
            
############################################################
#####################PARSING SYSTEM 20#######################
############################################################
#ATC4H[M10][F][ATR62]       
def system20():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        atrAvg = float(atrAvg) * .625
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 21#######################
############################################################
#ATC5M[M10][F][ATR100]       
def system21():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_5MINUTE, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday 

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break

############################################################
#####################PARSING SYSTEM 22#######################
############################################################
#ATC15M[M10][F][ATR100]       
def system22():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_15MINUTE, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday 

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
            
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
                
############################################################
#####################PARSING SYSTEM 23#######################
############################################################
#ATC1H[M10][F][ATR100]       
def system23():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1HOUR, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
        
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
############################################################
#####################PARSING SYSTEM 24#######################
############################################################
#ATC4H[M10][F][ATR100]       
def system24():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    lenList = len(symbol_list)
    LITR = True
    symbolLength = len(symbol_list)
    
    for s in range(lenList):
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
            klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
        except Exception as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e:
            pd = open('pingData alphaSignals', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
        while conNode == True:
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_4HOUR, limit=50)
                klines1 = client.futures_klines(symbol=symbol_list[s],interval=KLINE_INTERVAL_1DAY, limit=21)
                conNode = False
            except Exception as e:
                print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e: 
                print(str(e))
                sleep(200)
                conNode = True
                    
        swingLows = []
        swingHighs = []
        swingLowIndex = []
        swingHighIndex = []
        buyConditionMet = False
        sellConditionMet = False
        engulf = False
        atc = False
        engulfS = False
        atcS = False
        localHighLowList = []
        localLowHighList = []
        swingIsLower = False
        swingIsHigher = False
        targetLong = 0
        targetShort = 0
        checkCandlesBuy = False
        checkCandlesSell = False
        activeTrades = 0
        
        stopRiskRangeB = 0
        riskBuy = 0
        stopRiskRangeS = 0 
        riskSell = 0  
        
        targetRangeB = 0
        targetBuy = 0
        targetRangeS = 0
        targetSell = 0
                
        atrSum = 0
        atrAvg = 0
        atrToday = 0
    
        atrList = []
                
        currentPrice = float(klines[49][4])
        
        try:
            for b in range(21):
                pRise = float(klines1[b][2])-float(klines1[b][3])
                atrList.append(pRise)
                atrSum = sum(atrList)
                atrAvg = atrSum / 21
                atrToday = float(klines1[20][2])-float(klines1[20][3])
        except IndexError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        except KeyError as e:
            print(e)
            symbol_list.remove(symbol_list[s])
            continue
        
        #print(atrSum)
        #print(atrAvg)
        #print(atrToday

        for lh in range(6):
            localLowHigh = float(klines[49-lh][2])
            localLowHighList.append(localLowHigh)
        entryPointBuy = float(min(localLowHighList))
        
        for ll in range(6):
            localHighLow = float(klines[49-ll][3])
            localHighLowList.append(localHighLow)
        entryPointSell = float(max(localHighLowList))
        
        for vx in range(47):
           vxx = 47-vx
           checkLowIndex1 = float(klines[vxx][3])
           checkHighIndex1 = float(klines[vxx][2]) 
           
           checkLowBack1 = float(klines[vxx-1][3])
           checkLowBack2 = float(klines[vxx-2][3])
           checkLowFor1 = float(klines[vxx+1][3])
           checkLowFor2 = float(klines[vxx+2][3])
           
           checkHighBack1 = float(klines[vxx-1][2])
           checkHighBack2 = float(klines[vxx-2][2])
           checkHighFor1 = float(klines[vxx+1][2])
           checkHighFor2 = float(klines[vxx+2][2])
           
           if checkLowIndex1 < checkLowBack1 and checkLowIndex1 < checkLowBack2 and checkLowIndex1 < checkLowFor1 and checkLowIndex1 < checkLowFor2:
               swingLows.append(checkLowIndex1)
               swingLowIndex.append(vxx)
               
           if checkHighIndex1 > checkHighBack1 and checkHighIndex1 > checkHighBack2 and checkHighIndex1 > checkHighFor1 and checkHighIndex1 > checkHighFor2:
               swingHighs.append(checkHighIndex1)
               swingHighIndex.append(vxx)
        
        try:
            if float(swingLows[0]) < float(swingLows[1]):
                swingIsLower = True
        except IndexError as e:
            swingIsLower = False
            
        try:
            if float(swingHighs[0]) > float(swingHighs[1]):
                swingIsHigher = True
        except IndexError as e:
            swingIsHigher = False
               
        try:
            indexLow1 = swingLowIndex[0]
            indexLow2 = swingLowIndex[0] + 1
            indexHigh1 = swingHighIndex[0]
            indexHigh2 = swingHighIndex[0] + 1
        except IndexError as e:
            indexLow1 = 1
            indexLow2 = 1
            indexHigh1 = 1
            indexHigh2 = 1
        
        indexLowSignalOpen = float(klines[indexLow1][1])
        indexLowSignalHigh = float(klines[indexLow1][2])
        indexLowSignalLow = float(klines[indexLow1][3])
        indexLowSignalClose = float(klines[indexLow1][4])
        
        indexLowNextOpen = float(klines[indexLow2][1])
        indexLowNextHigh = float(klines[indexLow2][2])
        indexLowNextLow = float(klines[indexLow2][3])
        indexLowNextClose = float(klines[indexLow2][4])
        
        if indexLowSignalClose > indexLowSignalOpen:
            realBodySignal = indexLowSignalClose - indexLowSignalOpen
            topWickSignal = indexLowSignalHigh - indexLowSignalClose
        else: 
            realBodySignal = indexLowSignalOpen - indexLowSignalClose
            topWickSignal = indexLowSignalHigh - indexLowSignalOpen
                
        if indexLowNextClose > indexLowNextOpen:
            realBodyNext = indexLowNextClose - indexLowNextOpen
        else:
            realBodyNext = indexLowNextOpen - indexLowNextClose 
            
        if realBodyNext > topWickSignal and indexLowNextLow < indexLowSignalClose and indexLowNextClose > indexLowSignalHigh and indexLowNextClose > indexLowNextOpen:
            atc = True
            buyConditionMet = True
            
        if realBodyNext > realBodySignal and indexLowNextOpen <= indexLowSignalClose and indexLowNextClose > indexLowSignalOpen:
            engulf = True
            buyConditionMet = True 
        
        indexHighSignalOpen = float(klines[indexHigh1][1])
        indexHighSignalHigh = float(klines[indexHigh1][2])
        indexHighSignalLow = float(klines[indexHigh1][3])
        indexHighSignalClose = float(klines[indexHigh1][4])
        
        indexHighNextOpen = float(klines[indexHigh2][1])
        indexHighNextHigh = float(klines[indexHigh2][2])
        indexHighNextLow = float(klines[indexHigh2][3])
        indexHighNextClose = float(klines[indexHigh2][4])
                
        if indexHighSignalClose > indexHighSignalOpen:
            realBodySignalS = indexHighSignalClose - indexHighSignalOpen
            topWickSignalS = indexHighSignalHigh - indexHighSignalClose
        else: 
            realBodySignalS = indexHighSignalOpen - indexHighSignalClose
            topWickSignalS = indexHighSignalHigh - indexHighSignalOpen
                
        if indexHighNextClose > indexHighNextOpen:
            realBodyNextS = indexHighNextClose - indexHighNextOpen
        else:
            realBodyNextS = indexHighNextOpen - indexHighNextClose
        
        if realBodyNextS > topWickSignalS and indexHighNextOpen > indexHighSignalClose and indexHighNextClose < indexHighSignalLow and indexHighNextClose < indexHighNextOpen:
            atcS = True
            sellConditionMet = True
        if realBodyNextS > realBodySignalS and indexHighNextOpen >= indexHighSignalClose and indexHighNextClose < indexHighSignalOpen:
            engulfS = True
            sellConditionMet = True     
        
        apexS = (float(indexLowSignalHigh) - float(indexLowSignalLow)) * .50
        stopShort = float(indexHighSignalHigh) * 1.002
        targetShort = float(indexLowSignalHigh) - float(apexS)
        
        apexB = (float(indexHighSignalHigh) - float(indexHighSignalLow)) * .50
        stopLong = float(indexLowSignalLow) * 0.998
        targetLong = float(indexHighSignalHigh) - float(apexB)
            
        quantity = 1000 / float(currentPrice) #1000 is max position allocation in USDT           
        activeBuyStart = len(symbol_listActiveBuy)
        activeSellStart = len(symbol_listActiveSell)
        activeTrades = float(activeBuyStart) + float(activeSellStart)
        
        stopRiskRangeB = float(currentPrice) - float(stopLong) ###check if stop is not to large
        riskBuy = float(stopRiskRangeB) * float(quantity)
        
        stopRiskRangeS = float(stopShort) - float(currentPrice) ###check if stop is not to large
        riskSell = float(stopRiskRangeS) * (quantity) 
        
        targetRangeB = float(targetLong) - float(currentPrice)  #### check is the target is worth risk
        targetBuy = float(targetRangeB) * float(quantity)
        
        targetRangeS = float(currentPrice) - float(targetShort) #### check is the target is worth risk
        targetSell = float(targetRangeS) * float(quantity)
    
        if buyConditionMet == True and atc == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5 and atrToday < atrAvg:
            
            symbol_listActiveBuy.append(symbol_list[s])
            buy_PriceLong.append(float(currentPrice))
            stop_PriceLong.append(float(stopLong))
            target_PriceLong.append(float(targetLong))
            qty_Long.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
        
        if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5 and atrToday < atrAvg:
                
            symbol_listActiveSell.append(symbol_list[s])
            buy_PriceShort.append(float(currentPrice))
            stop_PriceShort.append(float(stopShort))
            target_PriceShort.append(float(targetShort))
            qty_Short.append(float(quantity))
            symbol_list.remove(symbol_list[s])
            break
