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

import symbol_list1 

symbol_list1 = symbol_list1.symbol_list   ####ALL BINANCE FUTURES

####SYSTEM 1 TF5M####
symbol_listActiveBuy1 = []
buy_PriceLong1 = []
stop_PriceLong1 = []
target_PriceLong1 = []
qty_Long1 = []

symbol_listActiveSell1 = []
buy_PriceShort1 = []
stop_PriceShort1 = []
target_PriceShort1 = []
qty_Short1 = []

####SYSTEM 1 TF15M####
symbol_listActiveBuy2 = []
buy_PriceLong2 = []
stop_PriceLong2 = []
target_PriceLong2 = []
qty_Long2 = []

symbol_listActiveSell2 = []
buy_PriceShort2 = []
stop_PriceShort2 = []
target_PriceShort2 = []
qty_Short2 = []

####SYSTEM 1 TF1H####
symbol_listActiveBuy3 = []
buy_PriceLong3 = []
stop_PriceLong3 = []
target_PriceLong3 = []
qty_Long3 = []

symbol_listActiveSell3 = []
buy_PriceShort3 = []
stop_PriceShort3 = []
target_PriceShort3 = []
qty_Short3 = []

####SYSTEM 1 TF4H####
symbol_listActiveBuy4 = []
buy_PriceLong4 = []
stop_PriceLong4 = []
target_PriceLong4 = []
qty_Long4 = []

symbol_listActiveSell4 = []
buy_PriceShort4 = []
stop_PriceShort4 = []
target_PriceShort4 = []
qty_Short4 = []

####SYSTEM 2 TF5M####
symbol_listActiveBuy5 = []
buy_PriceLong5 = []
stop_PriceLong5 = []
target_PriceLong5 = []
qty_Long5 = []

symbol_listActiveSell5 = []
buy_PriceShort5 = []
stop_PriceShort5 = []
target_PriceShort5 = []
qty_Short5 = []

####SYSTEM 2 TF15M####
symbol_listActiveBuy6 = []
buy_PriceLong6 = []
stop_PriceLong6 = []
target_PriceLong6 = []
qty_Long6 = []

symbol_listActiveSell6 = []
buy_PriceShort6 = []
stop_PriceShort6 = []
target_PriceShort6 = []
qty_Short6 = []

####SYSTEM 2 TF1H####
symbol_listActiveBuy7 = []
buy_PriceLong7 = []
stop_PriceLong7 = []
target_PriceLong7 = []
qty_Long7 = []

symbol_listActiveSell7 = []
buy_PriceShort7 = []
stop_PriceShort7 = []
target_PriceShort7 = []
qty_Short7 = []

####SYSTEM 2 TF4H####
symbol_listActiveBuy8 = []
buy_PriceLong8 = []
stop_PriceLong8 = []
target_PriceLong8 = []
qty_Long8 = []

symbol_listActiveSell8 = []
buy_PriceShort8 = []
stop_PriceShort8 = []
target_PriceShort8 = []
qty_Short8 = []

def getTF5M():
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    conNode = False
    
    try:
        client = Client(apiData.APIKey, apiData.SecretKey)
        klines1 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_5MINUTE, limit=50)
    except Exception as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(60)
        conNode = True
    except MaxRetryError as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(200)
        conNode = True
        
    while conNode == True:
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines1 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_5MINUTE, limit=50)
            conNode = False
        except Exception as e:
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e: 
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
    return klines1

def getTF15M():
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    conNode = False
    
    try:
        client = Client(apiData.APIKey, apiData.SecretKey)
        klines2 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_15MINUTE, limit=50)
    except Exception as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(60)
        conNode = True
    except MaxRetryError as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(200)
        conNode = True
        
    while conNode == True:
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines2 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_15MINUTE, limit=50)
            conNode = False
        except Exception as e:
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e: 
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
    return klines2

def getTF1H():
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    conNode = False
    
    try:
        client = Client(apiData.APIKey, apiData.SecretKey)
        klines3 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_1HOUR, limit=50)
    except Exception as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(60)
        conNode = True
    except MaxRetryError as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(200)
        conNode = True
        
    while conNode == True:
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines3 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_1HOUR, limit=50)
            conNode = False
        except Exception as e:
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e: 
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
    return klines3

def getTF4H():
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    conNode = False
    
    try:
        client = Client(apiData.APIKey, apiData.SecretKey)
        klines4 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_4HOUR, limit=50)
    except Exception as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(60)
        conNode = True
    except MaxRetryError as e:
        pd = open('pingData alphaSignals1', 'a')
        pd.write("\n" + str(t) + str(e))
        pd.close()
        print(str(e))
        sleep(200)
        conNode = True
        
    while conNode == True:
        try:
            client = Client(apiData.APIKey, apiData.SecretKey)
            klines4 = client.futures_klines(symbol=symbol_list1[0],interval=KLINE_INTERVAL_4HOUR, limit=50)
            conNode = False
        except Exception as e:
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(60)
            conNode = True
        except MaxRetryError as e: 
            pd = open('pingData alphaSignals1', 'a')
            pd.write("\n" + str(t) + str(e))
            pd.close()
            print(str(e))
            sleep(200)
            conNode = True
            
    return klines4
        
def Main():   
     
    now = datetime.now()
    t = now.strftime("%m/%d/%Y, %H:%M:%S")
    print('alphaSignals1 Running @ ' + str(t))
    
    qList1 = []
    conNode = False

    symbolLength = len(symbol_list1)
    
    while symbolLength > 0:
    
        klines1 = getTF5M()
        klines2 = getTF15M()
        klines3 = getTF1H()
        klines4 = getTF4H()
        
        ############################################################
        ###########PARSING SYSTEM 1 TF5M SIGNALS ##################
        ############################################################
        #ATC5M[M10][F]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy1 or \
            symbol_list1[0] in symbol_listActiveSell1:
                skipRun = True
                
        if skipRun == False:
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
                    
            currentPrice = float(klines1[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines1[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines1[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines1[vxx][3])
               checkHighIndex1 = float(klines1[vxx][2]) 
               
               checkLowBack1 = float(klines1[vxx-1][3])
               checkLowBack2 = float(klines1[vxx-2][3])
               checkLowFor1 = float(klines1[vxx+1][3])
               checkLowFor2 = float(klines1[vxx+2][3])
               
               checkHighBack1 = float(klines1[vxx-1][2])
               checkHighBack2 = float(klines1[vxx-2][2])
               checkHighFor1 = float(klines1[vxx+1][2])
               checkHighFor2 = float(klines1[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines1[indexLow1][1])
            indexLowSignalHigh = float(klines1[indexLow1][2])
            indexLowSignalLow = float(klines1[indexLow1][3])
            indexLowSignalClose = float(klines1[indexLow1][4])
        
            indexLowNextOpen = float(klines1[indexLow2][1])
            indexLowNextHigh = float(klines1[indexLow2][2])
            indexLowNextLow = float(klines1[indexLow2][3])
            indexLowNextClose = float(klines1[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines1[indexHigh1][1])
            indexHighSignalHigh = float(klines1[indexHigh1][2])
            indexHighSignalLow = float(klines1[indexHigh1][3])
            indexHighSignalClose = float(klines1[indexHigh1][4])
        
            indexHighNextOpen = float(klines1[indexHigh2][1])
            indexHighNextHigh = float(klines1[indexHigh2][2])
            indexHighNextLow = float(klines1[indexHigh2][3])
            indexHighNextClose = float(klines1[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy1)
            activeSellStart = len(symbol_listActiveSell1)
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
                
                symbol_listActiveBuy1.append(symbol_list1[0])
                buy_PriceLong1.append(float(currentPrice))
                stop_PriceLong1.append(float(stopLong))
                target_PriceLong1.append(float(targetLong))
                qty_Long1.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy1.append(symbol_list1[0])
                buy_PriceLong1.append(float(currentPrice))
                stop_PriceLong1.append(float(stopLong))
                target_PriceLong1.append(float(targetLong))
                qty_Long1.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                
                symbol_listActiveSell1.append(symbol_list1[0])
                buy_PriceShort1.append(float(currentPrice))
                stop_PriceShort1.append(float(stopShort))
                target_PriceShort1.append(float(targetShort))
                qty_Short1.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell1.append(symbol_list1[0])
                buy_PriceShort1.append(float(currentPrice))
                stop_PriceShort1.append(float(stopShort))
                target_PriceShort1.append(float(targetShort))
                qty_Short1.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 1 TF15M SIGNALS ##################
        ############################################################
        #ATC15M[M10][F]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy2 or \
            symbol_list1[0] in symbol_listActiveSell2:
                skipRun = True
            
        if skipRun == False:
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
                    
            currentPrice = float(klines2[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines2[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines2[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines2[vxx][3])
               checkHighIndex1 = float(klines2[vxx][2]) 
               
               checkLowBack1 = float(klines2[vxx-1][3])
               checkLowBack2 = float(klines2[vxx-2][3])
               checkLowFor1 = float(klines2[vxx+1][3])
               checkLowFor2 = float(klines2[vxx+2][3])
               
               checkHighBack1 = float(klines2[vxx-1][2])
               checkHighBack2 = float(klines2[vxx-2][2])
               checkHighFor1 = float(klines2[vxx+1][2])
               checkHighFor2 = float(klines2[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines2[indexLow1][1])
            indexLowSignalHigh = float(klines2[indexLow1][2])
            indexLowSignalLow = float(klines2[indexLow1][3])
            indexLowSignalClose = float(klines2[indexLow1][4])
        
            indexLowNextOpen = float(klines2[indexLow2][1])
            indexLowNextHigh = float(klines2[indexLow2][2])
            indexLowNextLow = float(klines2[indexLow2][3])
            indexLowNextClose = float(klines2[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines2[indexHigh1][1])
            indexHighSignalHigh = float(klines2[indexHigh1][2])
            indexHighSignalLow = float(klines2[indexHigh1][3])
            indexHighSignalClose = float(klines2[indexHigh1][4])
        
            indexHighNextOpen = float(klines2[indexHigh2][1])
            indexHighNextHigh = float(klines2[indexHigh2][2])
            indexHighNextLow = float(klines2[indexHigh2][3])
            indexHighNextClose = float(klines2[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy2)
            activeSellStart = len(symbol_listActiveSell2)
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
                
                symbol_listActiveBuy2.append(symbol_list1[0])
                buy_PriceLong2.append(float(currentPrice))
                stop_PriceLong2.append(float(stopLong))
                target_PriceLong2.append(float(targetLong))
                qty_Long2.append(float(quantity))
                buyConditionMet = False
                
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy2.append(symbol_list1[0])
                buy_PriceLong2.append(float(currentPrice))
                stop_PriceLong2.append(float(stopLong))
                target_PriceLong2.append(float(targetLong))
                qty_Long2.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell2.append(symbol_list1[0])
                buy_PriceShort2.append(float(currentPrice))
                stop_PriceShort2.append(float(stopShort))
                target_PriceShort2.append(float(targetShort))
                qty_Short2.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell2.append(symbol_list1[0])
                buy_PriceShort2.append(float(currentPrice))
                stop_PriceShort2.append(float(stopShort))
                target_PriceShort2.append(float(targetShort))
                qty_Short2.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 1 TF1H SIGNALS ###################
        ############################################################
        #ATC1H[M10][F]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy3 or \
            symbol_list1[0] in symbol_listActiveSell3:
                skipRun = True
            
        if skipRun == False:
        
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
                    
            currentPrice = float(klines3[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines3[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines3[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines3[vxx][3])
               checkHighIndex1 = float(klines3[vxx][2]) 
               
               checkLowBack1 = float(klines3[vxx-1][3])
               checkLowBack2 = float(klines3[vxx-2][3])
               checkLowFor1 = float(klines3[vxx+1][3])
               checkLowFor2 = float(klines3[vxx+2][3])
               
               checkHighBack1 = float(klines3[vxx-1][2])
               checkHighBack2 = float(klines3[vxx-2][2])
               checkHighFor1 = float(klines3[vxx+1][2])
               checkHighFor2 = float(klines3[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines3[indexLow1][1])
            indexLowSignalHigh = float(klines3[indexLow1][2])
            indexLowSignalLow = float(klines3[indexLow1][3])
            indexLowSignalClose = float(klines3[indexLow1][4])
        
            indexLowNextOpen = float(klines3[indexLow2][1])
            indexLowNextHigh = float(klines3[indexLow2][2])
            indexLowNextLow = float(klines3[indexLow2][3])
            indexLowNextClose = float(klines3[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines3[indexHigh1][1])
            indexHighSignalHigh = float(klines3[indexHigh1][2])
            indexHighSignalLow = float(klines3[indexHigh1][3])
            indexHighSignalClose = float(klines3[indexHigh1][4])
        
            indexHighNextOpen = float(klines3[indexHigh2][1])
            indexHighNextHigh = float(klines3[indexHigh2][2])
            indexHighNextLow = float(klines3[indexHigh2][3])
            indexHighNextClose = float(klines3[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy3)
            activeSellStart = len(symbol_listActiveSell3)
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
                
                symbol_listActiveBuy3.append(symbol_list1[0])
                buy_PriceLong3.append(float(currentPrice))
                stop_PriceLong3.append(float(stopLong))
                target_PriceLong3.append(float(targetLong))
                qty_Long3.append(float(quantity))
                buyConditionMet = False
                
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy3.append(symbol_list1[0])
                buy_PriceLong3.append(float(currentPrice))
                stop_PriceLong3.append(float(stopLong))
                target_PriceLong3.append(float(targetLong))
                qty_Long3.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell3.append(symbol_list1[0])
                buy_PriceShort3.append(float(currentPrice))
                stop_PriceShort3.append(float(stopShort))
                target_PriceShort3.append(float(targetShort))
                qty_Short3.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell3.append(symbol_list1[0])
                buy_PriceShort3.append(float(currentPrice))
                stop_PriceShort3.append(float(stopShort))
                target_PriceShort3.append(float(targetShort))
                qty_Short3.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 1 TF4H SIGNALS ###################
        ############################################################
        #ATC4H[M10][F]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy4 or \
            symbol_list1[0] in symbol_listActiveSell4:
                skipRun = True
            
        if skipRun == False:
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
                    
            currentPrice = float(klines4[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines4[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines4[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines4[vxx][3])
               checkHighIndex1 = float(klines4[vxx][2]) 
               
               checkLowBack1 = float(klines4[vxx-1][3])
               checkLowBack2 = float(klines4[vxx-2][3])
               checkLowFor1 = float(klines4[vxx+1][3])
               checkLowFor2 = float(klines4[vxx+2][3])
               
               checkHighBack1 = float(klines4[vxx-1][2])
               checkHighBack2 = float(klines4[vxx-2][2])
               checkHighFor1 = float(klines4[vxx+1][2])
               checkHighFor2 = float(klines4[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines4[indexLow1][1])
            indexLowSignalHigh = float(klines4[indexLow1][2])
            indexLowSignalLow = float(klines4[indexLow1][3])
            indexLowSignalClose = float(klines4[indexLow1][4])
        
            indexLowNextOpen = float(klines4[indexLow2][1])
            indexLowNextHigh = float(klines4[indexLow2][2])
            indexLowNextLow = float(klines4[indexLow2][3])
            indexLowNextClose = float(klines4[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines4[indexHigh1][1])
            indexHighSignalHigh = float(klines4[indexHigh1][2])
            indexHighSignalLow = float(klines4[indexHigh1][3])
            indexHighSignalClose = float(klines4[indexHigh1][4])
        
            indexHighNextOpen = float(klines4[indexHigh2][1])
            indexHighNextHigh = float(klines4[indexHigh2][2])
            indexHighNextLow = float(klines4[indexHigh2][3])
            indexHighNextClose = float(klines4[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy4)
            activeSellStart = len(symbol_listActiveSell4)
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
                
                symbol_listActiveBuy4.append(symbol_list1[0])
                buy_PriceLong4.append(float(currentPrice))
                stop_PriceLong4.append(float(stopLong))
                target_PriceLong4.append(float(targetLong))
                qty_Long4.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy4.append(symbol_list1[0])
                buy_PriceLong4.append(float(currentPrice))
                stop_PriceLong4.append(float(stopLong))
                target_PriceLong4.append(float(targetLong))
                qty_Long4.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell4.append(symbol_list1[0])
                buy_PriceShort4.append(float(currentPrice))
                stop_PriceShort4.append(float(stopShort))
                target_PriceShort4.append(float(targetShort))
                qty_Short4.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell4.append(symbol_list1[0])
                buy_PriceShort4.append(float(currentPrice))
                stop_PriceShort4.append(float(stopShort))
                target_PriceShort4.append(float(targetShort))
                qty_Short4.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 2 TF5M SIGNALS ##################
        ############################################################
        #ATC5M[M10][F][OI]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy5 or \
            symbol_list1[0] in symbol_listActiveSell5:
                skipRun = True
            
        if skipRun == False:
        
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
                    
            currentPrice = float(klines1[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines1[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines1[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines1[vxx][3])
               checkHighIndex1 = float(klines1[vxx][2]) 
               
               checkLowBack1 = float(klines1[vxx-1][3])
               checkLowBack2 = float(klines1[vxx-2][3])
               checkLowFor1 = float(klines1[vxx+1][3])
               checkLowFor2 = float(klines1[vxx+2][3])
               
               checkHighBack1 = float(klines1[vxx-1][2])
               checkHighBack2 = float(klines1[vxx-2][2])
               checkHighFor1 = float(klines1[vxx+1][2])
               checkHighFor2 = float(klines1[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines1[indexLow1][1])
            indexLowSignalHigh = float(klines1[indexLow1][2])
            indexLowSignalLow = float(klines1[indexLow1][3])
            indexLowSignalClose = float(klines1[indexLow1][4])
        
            indexLowNextOpen = float(klines1[indexLow2][1])
            indexLowNextHigh = float(klines1[indexLow2][2])
            indexLowNextLow = float(klines1[indexLow2][3])
            indexLowNextClose = float(klines1[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines1[indexHigh1][1])
            indexHighSignalHigh = float(klines1[indexHigh1][2])
            indexHighSignalLow = float(klines1[indexHigh1][3])
            indexHighSignalClose = float(klines1[indexHigh1][4])
        
            indexHighNextOpen = float(klines1[indexHigh2][1])
            indexHighNextHigh = float(klines1[indexHigh2][2])
            indexHighNextLow = float(klines1[indexHigh2][3])
            indexHighNextClose = float(klines1[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy5)
            activeSellStart = len(symbol_listActiveSell5)
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
                
                symbol_listActiveBuy5.append(symbol_list1[0])
                buy_PriceLong5.append(float(currentPrice))
                stop_PriceLong5.append(float(stopLong))
                target_PriceLong5.append(float(targetLong))
                qty_Long5.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy5.append(symbol_list1[0])
                buy_PriceLong5.append(float(currentPrice))
                stop_PriceLong5.append(float(stopLong))
                target_PriceLong5.append(float(targetLong))
                qty_Long5.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell5.append(symbol_list1[0])
                buy_PriceShort5.append(float(currentPrice))
                stop_PriceShort5.append(float(stopShort))
                target_PriceShort5.append(float(targetShort))
                qty_Short5.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell5.append(symbol_list1[0])
                buy_PriceShort5.append(float(currentPrice))
                stop_PriceShort5.append(float(stopShort))
                target_PriceShort5.append(float(targetShort))
                qty_Short5.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 2 TF15M SIGNALS ##################
        ############################################################
        #ATC15M[M10][F][OI]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy6 or \
            symbol_list1[0] in symbol_listActiveSell6:
                skipRun = True
            
        if skipRun == False:
        
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
                    
            currentPrice = float(klines2[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines2[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines2[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines2[vxx][3])
               checkHighIndex1 = float(klines2[vxx][2]) 
               
               checkLowBack1 = float(klines2[vxx-1][3])
               checkLowBack2 = float(klines2[vxx-2][3])
               checkLowFor1 = float(klines2[vxx+1][3])
               checkLowFor2 = float(klines2[vxx+2][3])
               
               checkHighBack1 = float(klines2[vxx-1][2])
               checkHighBack2 = float(klines2[vxx-2][2])
               checkHighFor1 = float(klines2[vxx+1][2])
               checkHighFor2 = float(klines2[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines2[indexLow1][1])
            indexLowSignalHigh = float(klines2[indexLow1][2])
            indexLowSignalLow = float(klines2[indexLow1][3])
            indexLowSignalClose = float(klines2[indexLow1][4])
        
            indexLowNextOpen = float(klines2[indexLow2][1])
            indexLowNextHigh = float(klines2[indexLow2][2])
            indexLowNextLow = float(klines2[indexLow2][3])
            indexLowNextClose = float(klines2[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines2[indexHigh1][1])
            indexHighSignalHigh = float(klines2[indexHigh1][2])
            indexHighSignalLow = float(klines2[indexHigh1][3])
            indexHighSignalClose = float(klines2[indexHigh1][4])
        
            indexHighNextOpen = float(klines2[indexHigh2][1])
            indexHighNextHigh = float(klines2[indexHigh2][2])
            indexHighNextLow = float(klines2[indexHigh2][3])
            indexHighNextClose = float(klines2[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy6)
            activeSellStart = len(symbol_listActiveSell6)
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
                
                symbol_listActiveBuy6.append(symbol_list1[0])
                buy_PriceLong6.append(float(currentPrice))
                stop_PriceLong6.append(float(stopLong))
                target_PriceLong6.append(float(targetLong))
                qty_Long6.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy6.append(symbol_list1[0])
                buy_PriceLong6.append(float(currentPrice))
                stop_PriceLong6.append(float(stopLong))
                target_PriceLong6.append(float(targetLong))
                qty_Long6.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell6.append(symbol_list1[0])
                buy_PriceShort6.append(float(currentPrice))
                stop_PriceShort6.append(float(stopShort))
                target_PriceShort6.append(float(targetShort))
                qty_Short6.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell6.append(symbol_list1[0])
                buy_PriceShort6.append(float(currentPrice))
                stop_PriceShort6.append(float(stopShort))
                target_PriceShort6.append(float(targetShort))
                qty_Short6.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 2 TF1H SIGNALS ###################
        ############################################################
        #ATC1H[M10][OI]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy7 or \
            symbol_list1[0] in symbol_listActiveSell7:
                skipRun = True
            
        if skipRun == False:
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
                    
            currentPrice = float(klines3[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines3[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines3[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines3[vxx][3])
               checkHighIndex1 = float(klines3[vxx][2]) 
               
               checkLowBack1 = float(klines3[vxx-1][3])
               checkLowBack2 = float(klines3[vxx-2][3])
               checkLowFor1 = float(klines3[vxx+1][3])
               checkLowFor2 = float(klines3[vxx+2][3])
               
               checkHighBack1 = float(klines3[vxx-1][2])
               checkHighBack2 = float(klines3[vxx-2][2])
               checkHighFor1 = float(klines3[vxx+1][2])
               checkHighFor2 = float(klines3[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines3[indexLow1][1])
            indexLowSignalHigh = float(klines3[indexLow1][2])
            indexLowSignalLow = float(klines3[indexLow1][3])
            indexLowSignalClose = float(klines3[indexLow1][4])
        
            indexLowNextOpen = float(klines3[indexLow2][1])
            indexLowNextHigh = float(klines3[indexLow2][2])
            indexLowNextLow = float(klines3[indexLow2][3])
            indexLowNextClose = float(klines3[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines3[indexHigh1][1])
            indexHighSignalHigh = float(klines3[indexHigh1][2])
            indexHighSignalLow = float(klines3[indexHigh1][3])
            indexHighSignalClose = float(klines3[indexHigh1][4])
        
            indexHighNextOpen = float(klines3[indexHigh2][1])
            indexHighNextHigh = float(klines3[indexHigh2][2])
            indexHighNextLow = float(klines3[indexHigh2][3])
            indexHighNextClose = float(klines3[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy7)
            activeSellStart = len(symbol_listActiveSell7)
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
                
                symbol_listActiveBuy7.append(symbol_list1[0])
                buy_PriceLong7.append(float(currentPrice))
                stop_PriceLong7.append(float(stopLong))
                target_PriceLong7.append(float(targetLong))
                qty_Long7.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy7.append(symbol_list1[0])
                buy_PriceLong7.append(float(currentPrice))
                stop_PriceLong7.append(float(stopLong))
                target_PriceLong7.append(float(targetLong))
                qty_Long7.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell7.append(symbol_list1[0])
                buy_PriceShort7.append(float(currentPrice))
                stop_PriceShort7.append(float(stopShort))
                target_PriceShort7.append(float(targetShort))
                qty_Short7.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell7.append(symbol_list1[0])
                buy_PriceShort7.append(float(currentPrice))
                stop_PriceShort7.append(float(stopShort))
                target_PriceShort7.append(float(targetShort))
                qty_Short7.append(float(quantity))
                sellConditionMet = False
            
        ############################################################
        ###########PARSING SYSTEM 2 TF4H SIGNALS ###################
        ############################################################
        #ATC4H[M10][F][OI]
        skipRun = False
        if symbol_list1[0] in symbol_listActiveBuy8 or \
            symbol_list1[0] in symbol_listActiveSell8:
                skipRun = True
            
        if skipRun == False:
        
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
                    
            currentPrice = float(klines4[49][4])
            
            for lh in range(6):
                localLowHigh = float(klines4[49-lh][2])
                localLowHighList.append(localLowHigh)
            entryPointBuy = float(min(localLowHighList))
            
            for ll in range(6):
                localHighLow = float(klines4[49-ll][3])
                localHighLowList.append(localHighLow)
            entryPointSell = float(max(localHighLowList))
            
            for vx in range(47):
               vxx = 47-vx
               checkLowIndex1 = float(klines4[vxx][3])
               checkHighIndex1 = float(klines4[vxx][2]) 
               
               checkLowBack1 = float(klines4[vxx-1][3])
               checkLowBack2 = float(klines4[vxx-2][3])
               checkLowFor1 = float(klines4[vxx+1][3])
               checkLowFor2 = float(klines4[vxx+2][3])
               
               checkHighBack1 = float(klines4[vxx-1][2])
               checkHighBack2 = float(klines4[vxx-2][2])
               checkHighFor1 = float(klines4[vxx+1][2])
               checkHighFor2 = float(klines4[vxx+2][2])
               
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
        
            indexLowSignalOpen = float(klines4[indexLow1][1])
            indexLowSignalHigh = float(klines4[indexLow1][2])
            indexLowSignalLow = float(klines4[indexLow1][3])
            indexLowSignalClose = float(klines4[indexLow1][4])
        
            indexLowNextOpen = float(klines4[indexLow2][1])
            indexLowNextHigh = float(klines4[indexLow2][2])
            indexLowNextLow = float(klines4[indexLow2][3])
            indexLowNextClose = float(klines4[indexLow2][4])
            
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
        
            indexHighSignalOpen = float(klines4[indexHigh1][1])
            indexHighSignalHigh = float(klines4[indexHigh1][2])
            indexHighSignalLow = float(klines4[indexHigh1][3])
            indexHighSignalClose = float(klines4[indexHigh1][4])
        
            indexHighNextOpen = float(klines4[indexHigh2][1])
            indexHighNextHigh = float(klines4[indexHigh2][2])
            indexHighNextLow = float(klines4[indexHigh2][3])
            indexHighNextClose = float(klines4[indexHigh2][4])
                    
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
            activeBuyStart = len(symbol_listActiveBuy8)
            activeSellStart = len(symbol_listActiveSell8)
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
                
                symbol_listActiveBuy8.append(symbol_list1[0])
                buy_PriceLong8.append(float(currentPrice))
                stop_PriceLong8.append(float(stopLong))
                target_PriceLong8.append(float(targetLong))
                qty_Long8.append(float(quantity))
                buyConditionMet = False
            
            if buyConditionMet == True and engulf == True and swingIsLower == True and currentPrice <= entryPointBuy and currentPrice > indexLowSignalLow and indexLow1 > indexHigh1 and activeTrades <= 9 and riskBuy <= 25 and targetBuy >= 5:
                
                symbol_listActiveBuy8.append(symbol_list1[0])
                buy_PriceLong8.append(float(currentPrice))
                stop_PriceLong8.append(float(stopLong))
                target_PriceLong8.append(float(targetLong))
                qty_Long8.append(float(quantity))
                buyConditionMet = False
            
            if sellConditionMet == True and atcS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell8.append(symbol_list1[0])
                buy_PriceShort8.append(float(currentPrice))
                stop_PriceShort8.append(float(stopShort))
                target_PriceShort8.append(float(targetShort))
                qty_Short8.append(float(quantity))
                sellConditionMet = False
            
            if sellConditionMet == True and engulfS == True and swingIsHigher == True and currentPrice >= entryPointSell and currentPrice < indexHighSignalHigh and indexHigh1 > indexLow1 and activeTrades <= 9 and riskSell <= 25 and targetSell >= 5:
                    
                symbol_listActiveSell8.append(symbol_list1[0])
                buy_PriceShort8.append(float(currentPrice))
                stop_PriceShort8.append(float(stopShort))
                target_PriceShort8.append(float(targetShort))
                qty_Short8.append(float(quantity))
                sellConditionMet = False
            
            now = datetime.now()
            t = now.strftime("%m/%d/%Y, %H:%M:%S")
            
        try:
            activeBuy1 = 0
            activeBuy1 = len(symbol_listActiveBuy1)
            if activeBuy1 > 0:
                for yx in range(activeBuy1):
                    print(symbol_listActiveBuy1[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy1[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing5M[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy1[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    
                    if float(currentPrice1) >= float(target_PriceLong1[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong1[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long1[yx])
                        
                        f = open('deltaLong.txt', 'a')
                        f.write("\n" + int(1))
                        f.close()
                        
                        f = open('dataSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy1[yx]) + "    " + str("{:.4f}".format(buy_PriceLong1[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong1[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong1[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long1[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong1.remove(buy_PriceLong1[yx])
                        stop_PriceLong1.remove(stop_PriceLong1[yx])
                        target_PriceLong1.remove(target_PriceLong1[yx])
                        qty_Long1.remove(qty_Long1[yx])
                        symbol_listActiveBuy1.remove(symbol_listActiveBuy1[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong1[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong1[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long1[yx])
                        
                        f = open('deltaLong.txt', 'a')
                        f.write("\n" + int(-1))
                        f.close()
                        
                        f = open('dataSwing5M[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy1[yx]) + "    " + str("{:.4f}".format(buy_PriceLong1[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong1[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong1[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long1[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong1.remove(buy_PriceLong1[yx])
                        stop_PriceLong1.remove(stop_PriceLong1[yx])
                        target_PriceLong1.remove(target_PriceLong1[yx])
                        qty_Long1.remove(qty_Long1[yx])
                        symbol_listActiveBuy1.remove(symbol_listActiveBuy1[yx])
                        break
                    
            activeSell1 = 0        
            activeSell1 = len(symbol_listActiveSell1)
            if activeSell1 > 0:
                for yv in range(activeSell1):
                    print(symbol_listActiveSell1[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell1[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing5M[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell1[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort1[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort1[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short1[yv])
                        
                        f = open('dataSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell1[yv]) + "    " + str("{:.4f}".format(buy_PriceShort1[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort1[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort1[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short1[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort1.remove(buy_PriceShort1[yv])
                        stop_PriceShort1.remove(stop_PriceShort1[yv])
                        target_PriceShort1.remove(target_PriceShort1[yv])
                        qty_Short1.remove(qty_Short1[yv])
                        symbol_listActiveSell1.remove(symbol_listActiveSell1[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort1[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort1[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short1[yv])
                                                    
                        f = open('dataSwing5M[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell1[yv]) + "    " + str("{:.4f}".format(buy_PriceShort1[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort1[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort1[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short1[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort1.remove(buy_PriceShort1[yv])
                        stop_PriceShort1.remove(stop_PriceShort1[yv])
                        target_PriceShort1.remove(target_PriceShort1[yv])
                        qty_Short1.remove(qty_Short1[yv])
                        symbol_listActiveSell1.remove(symbol_listActiveSell1[yv])
                        break
                    
            activeBuy2 = 0
            activeBuy2 = len(symbol_listActiveBuy2)
            if activeBuy2 > 0:
                for yx in range(activeBuy2):
                    print(symbol_listActiveBuy2[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy2[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing15M[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy2[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong2[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong2[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long2[yx])

                        f = open('dataSwing15M[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy2[yx]) + "    " + str("{:.4f}".format(buy_PriceLong2[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong2[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong2[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long2[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong2.remove(buy_PriceLong2[yx])
                        stop_PriceLong2.remove(stop_PriceLong2[yx])
                        target_PriceLong2.remove(target_PriceLong2[yx])
                        qty_Long2.remove(qty_Long2[yx])
                        symbol_listActiveBuy2.remove(symbol_listActiveBuy2[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong2[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong2[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long2[yx])
            
                        f = open('dataSwing15M[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy2[yx]) + "    " + str("{:.4f}".format(buy_PriceLong2[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong2[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong2[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long2[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong2.remove(buy_PriceLong2[yx])
                        stop_PriceLong2.remove(stop_PriceLong2[yx])
                        target_PriceLong2.remove(target_PriceLong2[yx])
                        qty_Long2.remove(qty_Long2[yx])
                        symbol_listActiveBuy2.remove(symbol_listActiveBuy2[yx])
                        break
                    
            activeSell2 = 0        
            activeSell2 = len(symbol_listActiveSell2)
            if activeSell2 > 0:
                for yv in range(activeSell2): 
                    print(symbol_listActiveSell2[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell2[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing15M[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell2[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort2[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort2[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short2[yv])

                        f = open('dataSwing15M[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing15M[10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell2[yv]) + "    " + str("{:.4f}".format(buy_PriceShort2[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort2[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort2[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short2[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort2.remove(buy_PriceShort2[yv])
                        stop_PriceShort2.remove(stop_PriceShort2[yv])
                        target_PriceShort2.remove(target_PriceShort2[yv])
                        qty_Short2.remove(qty_Short2[yv])
                        symbol_listActiveSell2.remove(symbol_listActiveSell2[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort2[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort2[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short2[yv])
                    
                        f = open('dataSwing15M[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell2[yv]) + "    " + str("{:.4f}".format(buy_PriceShort2[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort2[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort2[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short2[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort2.remove(buy_PriceShort2[yv])
                        stop_PriceShort2.remove(stop_PriceShort2[yv])
                        target_PriceShort2.remove(target_PriceShort2[yv])
                        qty_Short2.remove(qty_Short2[yv])
                        symbol_listActiveSell2.remove(symbol_listActiveSell2[yv])
                        break
                    
            activeBuy3 = 0                
            activeBuy3 = len(symbol_listActiveBuy3)
            if activeBuy3 > 0:
                for yx in range(activeBuy3):
                    print(symbol_listActiveBuy3[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy3[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing1H[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy3[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong3[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong3[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long3[yx])

                        f = open('dataSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy3[yx]) + "    " + str("{:.4f}".format(buy_PriceLong3[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong3[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong3[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long3[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong3.remove(buy_PriceLong3[yx])
                        stop_PriceLong3.remove(stop_PriceLong3[yx])
                        target_PriceLong3.remove(target_PriceLong3[yx])
                        qty_Long3.remove(qty_Long3[yx])
                        symbol_listActiveBuy3.remove(symbol_listActiveBuy3[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong3[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong3[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long3[yx])

                        f = open('dataSwing1H[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy3[yx]) + "    " + str("{:.4f}".format(buy_PriceLong3[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong3[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong3[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long3[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong3.remove(buy_PriceLong3[yx])
                        stop_PriceLong3.remove(stop_PriceLong3[yx])
                        target_PriceLong3.remove(target_PriceLong3[yx])
                        qty_Long3.remove(qty_Long3[yx])
                        symbol_listActiveBuy3.remove(symbol_listActiveBuy3[yx])
                        break
                    
            activeSell3 = 0        
            activeSell3 = len(symbol_listActiveSell3)
            if activeSell3 > 0:
                for yv in range(activeSell3): 
                    print(symbol_listActiveSell3[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell3[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing1H[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell3[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort3[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort3[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short3[yv])

                        f = open('dataSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell3[yv]) + "    " + str("{:.4f}".format(buy_PriceShort3[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort3[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort3[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short3[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort3.remove(buy_PriceShort3[yv])
                        stop_PriceShort3.remove(stop_PriceShort3[yv])
                        target_PriceShort3.remove(target_PriceShort3[yv])
                        qty_Short3.remove(qty_Short3[yv])
                        symbol_listActiveSell3.remove(symbol_listActiveSell3[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort3[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort3[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short3[yv])
               
                        f = open('dataSwing1H[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell3[yv]) + "    " + str("{:.4f}".format(buy_PriceShort3[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort3[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort3[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short3[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort3.remove(buy_PriceShort3[yv])
                        stop_PriceShort3.remove(stop_PriceShort3[yv])
                        target_PriceShort3.remove(target_PriceShort3[yv])
                        qty_Short3.remove(qty_Short3[yv])
                        symbol_listActiveSell3.remove(symbol_listActiveSell3[yv])
                        break
                    
            activeBuy4 = 0                
            activeBuy4 = len(symbol_listActiveBuy4)
            if activeBuy4 > 0:
                for yx in range(activeBuy4):
                    print(symbol_listActiveBuy4[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy4[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing4H[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy4[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong4[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong4[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long4[yx])

                        f = open('dataSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy4[yx]) + "    " + str("{:.4f}".format(buy_PriceLong4[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong4[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong4[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long4[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong4.remove(buy_PriceLong4[yx])
                        stop_PriceLong4.remove(stop_PriceLong4[yx])
                        target_PriceLong4.remove(target_PriceLong4[yx])
                        qty_Long4.remove(qty_Long4[yx])
                        symbol_listActiveBuy4.remove(symbol_listActiveBuy4[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong4[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong4[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long4[yx])

                        f = open('dataSwing4H[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy4[yx]) + "    " + str("{:.4f}".format(buy_PriceLong4[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong4[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong4[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long4[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong4.remove(buy_PriceLong4[yx])
                        stop_PriceLong4.remove(stop_PriceLong4[yx])
                        target_PriceLong4.remove(target_PriceLong4[yx])
                        qty_Long4.remove(qty_Long4[yx])
                        symbol_listActiveBuy4.remove(symbol_listActiveBuy4[yx])
                        break
                    
            activeSell4 = 0        
            activeSell4 = len(symbol_listActiveSell4)
            if activeSell4 > 0:
                for yv in range(activeSell4):
                    print(symbol_listActiveSell4[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell4[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing4H[M10][F]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell4[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort4[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort4[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short4[yv])

                        f = open('dataSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell4[yv]) + "    " + str("{:.4f}".format(buy_PriceShort4[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort4[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort4[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short4[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort4.remove(buy_PriceShort4[yv])
                        stop_PriceShort4.remove(stop_PriceShort4[yv])
                        target_PriceShort4.remove(target_PriceShort4[yv])
                        qty_Short4.remove(qty_Short4[yv])
                        symbol_listActiveSell4.remove(symbol_listActiveSell4[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort4[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort4[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short4[yv])
                     
                        f = open('dataSwing4H[M10][F].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell4[yv]) + "    " + str("{:.4f}".format(buy_PriceShort4[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort4[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort4[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short4[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort4.remove(buy_PriceShort4[yv])
                        stop_PriceShort4.remove(stop_PriceShort4[yv])
                        target_PriceShort4.remove(target_PriceShort4[yv])
                        qty_Short4.remove(qty_Short4[yv])
                        symbol_listActiveSell4.remove(symbol_listActiveSell4[yv])
                        break
                    
            activeBuy5 = 0
            activeBuy5 = len(symbol_listActiveBuy5)
            if activeBuy5 > 0:
                for yx in range(activeBuy5):
                    print(symbol_listActiveBuy5[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy5[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing5M[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy5[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong5[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong5[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long5[yx])

                        f = open('dataSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy5[yx]) + "    " + str("{:.4f}".format(buy_PriceLong5[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong5[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong5[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long5[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong5.remove(buy_PriceLong5[yx])
                        stop_PriceLong5.remove(stop_PriceLong5[yx])
                        target_PriceLong5.remove(target_PriceLong5[yx])
                        qty_Long5.remove(qty_Long5[yx])
                        symbol_listActiveBuy5.remove(symbol_listActiveBuy5[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong5[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong5[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long5[yx])

                        f = open('dataSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy5[yx]) + "    " + str("{:.4f}".format(buy_PriceLong5[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong5[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong5[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long5[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong5.remove(buy_PriceLong5[yx])
                        stop_PriceLong5.remove(stop_PriceLong5[yx])
                        target_PriceLong5.remove(target_PriceLong5[yx])
                        qty_Long5.remove(qty_Long5[yx])
                        symbol_listActiveBuy5.remove(symbol_listActiveBuy5[yx])
                        break
                    
            activeSell5 = 0        
            activeSell5 = len(symbol_listActiveSell5)
            if activeSell5 > 0:
                for yv in range(activeSell5):
                    print(symbol_listActiveSell5[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell5[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing5M[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell5[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort5[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort5[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short5[yv])

                        f = open('dataSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell5[yv]) + "    " + str("{:.4f}".format(buy_PriceShort5[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort5[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort5[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short5[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort5.remove(buy_PriceShort5[yv])
                        stop_PriceShort5.remove(stop_PriceShort5[yv])
                        target_PriceShort5.remove(target_PriceShort5[yv])
                        qty_Short5.remove(qty_Short5[yv])
                        symbol_listActiveSell5.remove(symbol_listActiveSell5[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort5[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort5[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short5[yv])
       
                        f = open('dataSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing5M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell5[yv]) + "    " + str("{:.4f}".format(buy_PriceShort5[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort5[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort5[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short5[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort5.remove(buy_PriceShort5[yv])
                        stop_PriceShort5.remove(stop_PriceShort5[yv])
                        target_PriceShort5.remove(target_PriceShort5[yv])
                        qty_Short5.remove(qty_Short5[yv])
                        symbol_listActiveSell5.remove(symbol_listActiveSell5[yv])
                        break
                    
            activeBuy6 = 0            
            activeBuy6 = len(symbol_listActiveBuy6)
            if activeBuy6 > 0:
                for yx in range(activeBuy6):
                    print(symbol_listActiveBuy6[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy6[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing15M[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy6[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong6[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong6[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long6[yx])

                        f = open('dataSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy6[yx]) + "    " + str("{:.4f}".format(buy_PriceLong6[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong6[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong6[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long6[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong6.remove(buy_PriceLong6[yx])
                        stop_PriceLong6.remove(stop_PriceLong6[yx])
                        target_PriceLong6.remove(target_PriceLong6[yx])
                        qty_Long6.remove(qty_Long6[yx])
                        symbol_listActiveBuy6.remove(symbol_listActiveBuy6[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong6[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong6[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long6[yx])

                        f = open('dataSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy6[yx]) + "    " + str("{:.4f}".format(buy_PriceLong6[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong6[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong6[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long6[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong6.remove(buy_PriceLong6[yx])
                        stop_PriceLong6.remove(stop_PriceLong6[yx])
                        target_PriceLong6.remove(target_PriceLong6[yx])
                        qty_Long6.remove(qty_Long6[yx])
                        symbol_listActiveBuy6.remove(symbol_listActiveBuy6[yx])
                        break
                    
            activeSell6 = 0        
            activeSell6 = len(symbol_listActiveSell6)
            if activeSell6 > 0:
                for yv in range(activeSell6):
                    print(symbol_listActiveSell6[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell6[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing15M[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell6[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort6[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort6[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short6[yv])

                        f = open('dataSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell6[yv]) + "    " + str("{:.4f}".format(buy_PriceShort6[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort6[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort6[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short6[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort6.remove(buy_PriceShort6[yv])
                        stop_PriceShort6.remove(stop_PriceShort6[yv])
                        target_PriceShort6.remove(target_PriceShort6[yv])
                        qty_Short6.remove(qty_Short6[yv])
                        symbol_listActiveSell6.remove(symbol_listActiveSell6[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort6[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort6[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short6[yv])
                      
                        f = open('dataSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing15M[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell6[yv]) + "    " + str("{:.4f}".format(buy_PriceShort6[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort6[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort6[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short6[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort6.remove(buy_PriceShort6[yv])
                        stop_PriceShort6.remove(stop_PriceShort6[yv])
                        target_PriceShort6.remove(target_PriceShort6[yv])
                        qty_Short6.remove(qty_Short6[yv])
                        symbol_listActiveSell6.remove(symbol_listActiveSell6[yv])
                        break
                    
            activeBuy7 = 0
            activeBuy7 = len(symbol_listActiveBuy7)
            if activeBuy7 > 0:
                for yx in range(activeBuy7):
                    print(symbol_listActiveBuy7[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy7[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing1H[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy7[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong7[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong7[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long7[yx])
                        
                        f = open('dataSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy7[yx]) + "    " + str("{:.4f}".format(buy_PriceLong7[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong7[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong7[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long7[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong7.remove(buy_PriceLong7[yx])
                        stop_PriceLong7.remove(stop_PriceLong7[yx])
                        target_PriceLong7.remove(target_PriceLong7[yx])
                        qty_Long7.remove(qty_Long7[yx])
                        symbol_listActiveBuy7.remove(symbol_listActiveBuy7[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong7[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong7[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long7[yx])

                        f = open('dataSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy7[yx]) + "    " + str("{:.4f}".format(buy_PriceLong7[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong7[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong7[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long7[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong7.remove(buy_PriceLong7[yx])
                        stop_PriceLong7.remove(stop_PriceLong7[yx])
                        target_PriceLong7.remove(target_PriceLong7[yx])
                        qty_Long7.remove(qty_Long7[yx])
                        symbol_listActiveBuy7.remove(symbol_listActiveBuy7[yx])
                        break
                    
            activeSell7 = 0       
            activeSell7 = len(symbol_listActiveSell7)
            if activeSell7 > 0:
                for yv in range(activeSell7):  
                    print(symbol_listActiveSell7[yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell7[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing1H[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell7[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort7[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort7[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short7[yv])

                        f = open('dataSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell7[yv]) + "    " + str("{:.4f}".format(buy_PriceShort7[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort7[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort7[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short7[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort7.remove(buy_PriceShort7[yv])
                        stop_PriceShort7.remove(stop_PriceShort7[yv])
                        target_PriceShort7.remove(target_PriceShort7[yv])
                        qty_Short7.remove(qty_Short7[yv])
                        symbol_listActiveSell7.remove(symbol_listActiveSell7[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort7[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort7[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short7[yv])
                
                        f = open('dataSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing1H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell7[yv]) + "    " + str("{:.4f}".format(buy_PriceShort7[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort7[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort7[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short7[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort7.remove(buy_PriceShort7[yv])
                        stop_PriceShort7.remove(stop_PriceShort7[yv])
                        target_PriceShort7.remove(target_PriceShort7[yv])
                        qty_Short7.remove(qty_Short7[yv])
                        symbol_listActiveSell7.remove(symbol_listActiveSell7[yv])
                        break
                    
            activeBuy8 = 0
            activeBuy8 = len(symbol_listActiveBuy8)
            if activeBuy8 > 0:
                for yx in range(activeBuy8):
                    print(symbol_listActiveBuy8[yx] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveBuy8[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing4H[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveBuy8[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])

                    if float(currentPrice1) >= float(target_PriceLong8[yx]):
                        #if long makes money
                        pnl1 = float(currentPrice1) - float(buy_PriceLong8[yx])
                        pnlLongWin = float(pnl1) * float(qty_Long8[yx])

                        f = open('dataSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy8[yx]) + "    " + str("{:.4f}".format(buy_PriceLong8[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong8[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong8[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long8[yx])) + "    " + str("{:.4f}".format(pnlLongWin)))
                        f.close()
                        
                        buy_PriceLong8.remove(buy_PriceLong8[yx])
                        stop_PriceLong8.remove(stop_PriceLong8[yx])
                        target_PriceLong8.remove(target_PriceLong8[yx])
                        qty_Long8.remove(qty_Long8[yx])
                        symbol_listActiveBuy8.remove(symbol_listActiveBuy8[yx])
                        break
                    
                    if float(currentPrice1) <= float(stop_PriceLong8[yx]):
                        #if long loses money
                        pnl2 = float(buy_PriceLong8[yx]) - float(currentPrice1)
                        pnlLongLose = float(pnl2) * float(qty_Long8[yx])

                        f = open('dataSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveBuy8[yx]) + "    " + str("{:.4f}".format(buy_PriceLong8[yx])) \
                        + "    " +  str("{:.4f}".format(target_PriceLong8[yx])) + "    " +  str("{:.4f}".format(stop_PriceLong8[yx])) + "    " \
                        + "    " + str("{:.4f}".format(qty_Long8[yx])) + "    -" + str("{:.4f}".format(pnlLongLose)))
                        f.close()
                        
                        buy_PriceLong8.remove(buy_PriceLong8[yx])
                        stop_PriceLong8.remove(stop_PriceLong8[yx])
                        target_PriceLong8.remove(target_PriceLong8[yx])
                        qty_Long8.remove(qty_Long8[yx])
                        symbol_listActiveBuy8.remove(symbol_listActiveBuy8[yx])
                        break
                    
            activeSell8 = 0        
            activeSell8 = len(symbol_listActiveSell8)
            if activeSell8 > 0:
                for yv in range(activeSell8):
                    print(symbol_listActiveSell8 [yv] + ' Calculating Close')
                    try:
                        client = Client(apiData.APIKey, apiData.SecretKey)
                        klines1 = client.futures_klines(symbol=symbol_listActiveSell8[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    except Exception as e:
                        pd = open('pingData Swing4H[M10][F][OI]', 'a')
                        pd.write("\n" + str(t) + str(e))
                        pd.close()
                        print(str(e)) 
                        sleep(60)
                        conNode = True
                    
                    while conNode == True:
                        try:
                            client = Client(apiData.APIKey, apiData.SecretKey)
                            klines1 = client.futures_klines(symbol=symbol_listActiveSell8[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                            conNode = False
                        except Exception as e:
                            print(str(e))
                            sleep(60)
                            conNode = True
                        
                    currentPrice1 = float(klines1[0][4])
                    if float(currentPrice1) <= float(target_PriceShort8[yv]): 
                        #if short makes money
                        pnl3 = float(buy_PriceShort8[yv]) - float(currentPrice1) #this is $amount trying to aquire on short
                        pnlShortWin = float(pnl3) * float(qty_Short8[yv])

                        f = open('dataSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell8[yv]) + "    " + str("{:.4f}".format(buy_PriceShort8[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort8[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort8[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short8[yv])) + "    " + str("{:.4f}".format(pnlShortWin)))
                        f.close()
                    
                        buy_PriceShort8.remove(buy_PriceShort8[yv])
                        stop_PriceShort8.remove(stop_PriceShort8[yv])
                        target_PriceShort8.remove(target_PriceShort8[yv])
                        qty_Short8.remove(qty_Short8[yv])
                        symbol_listActiveSell8.remove(symbol_listActiveSell8[yv])
                        break
                
                    if float(currentPrice1) >= float(stop_PriceShort8[yv]):
                        #if short loses money
                        pnl4 = float(currentPrice1) - float(buy_PriceShort8[yv])
                        pnlShortLose = float(pnl4) * float(qty_Short8[yv])
                     
                        f = open('dataSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                        
                        f = open('logSwing4H[M10][F][OI].txt', 'a')
                        f.write("\n" + str(t) + "    " + str(symbol_listActiveSell8[yv]) + "    " + str("{:.4f}".format(buy_PriceShort8[yv])) \
                        + "    " +  str("{:.4f}".format(target_PriceShort8[yv])) + "    " +  str("{:.4f}".format(stop_PriceShort8[yv])) + "    " \
                        + "    -" + str("{:.4f}".format(qty_Short8[yv])) + "    -" + str("{:.4f}".format(pnlShortLose)))
                        f.close()
                            
                        buy_PriceShort8.remove(buy_PriceShort8[yv])
                        stop_PriceShort8.remove(stop_PriceShort8[yv])
                        target_PriceShort8.remove(target_PriceShort8[yv])
                        qty_Short8.remove(qty_Short8[yv])
                        symbol_listActiveSell8.remove(symbol_listActiveSell8[yv])
                        break
        
        except IndexError as e:
            print(str(e))
            #print(symbol_list1[0] + ' Parsed!') 
        
            qList1.append(symbol_list1[0])
            symbol_list1.remove(symbol_list1[0])
            
            symbolLength = len(symbol_list1)
            continue
        
            if symbolLength == 0:
                
                print('Adding QLISTS BACK TO ORIGIN MINUS SIGNALS')
                qLength1 = len(qList1)
                for a in range(qLength1):
                    symbol_list1.append(qList1[a])
                    
                print('Symbol List is Reset')
                
                symbolLength = len(symbol_list1)
                
                qList1 = []
                
                now = datetime.now() 
                t = now.strftime("%m/%d/%Y, %H:%M:%S")
                print('alphaSignals1 Running @ ' + str(t))
                continue
                
        #print(symbol_list1[0] + ' Parsed!') 
        
        qList1.append(symbol_list1[0])
        symbol_list1.remove(symbol_list1[0])
        
        symbolLength = len(symbol_list1)

        if symbolLength == 0:
            
            print('Adding QLISTS BACK TO ORIGIN MINUS SIGNALS')
            qLength1 = len(qList1)
            for a in range(qLength1):
                symbol_list1.append(qList1[a])
                
            print('Symbol List is Reset')
            
            symbolLength = len(symbol_list1)
            
            qList1 = []
            
            now = datetime.now() 
            t = now.strftime("%m/%d/%Y, %H:%M:%S")
            print('alphaSignals1 Running @ ' + str(t))
            
if __name__ == '__main__':
    Main()
