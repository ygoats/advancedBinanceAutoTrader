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
import systemClear

import symbol_listT

client = Client(apiData.APIKey, apiData.SecretKey)

#symbolLong = []   ### where symbol goes for aquiring fill order
#entryLong = []
#targetLong = []  ### if price goes above or equals this price place server side order
#stopLong = []  ## if price goes below or equals this price place server side order
#quantityLong = [] ## quantity based off 250MAX position controlled within alphaSignals

symbolLongT = []  
entryLongT = []
targetLongT = [] 
stopLongT = []  
quantityLongT = []

symbolLongActive = [] 
entryLongActive = []
targetLongActive = [] 
stopLongActive = []  
quantityLongActive = []

#symbolShort = []
#entryShort = []
#targetShort= []
#stopShort = [] 
#quantityShort = []

symbolShortT = []
entryShortT = []
targetShortT = []
stopShortT = [] 
quantityShortT = []

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
    
    #print('Checking For Signals')
    
    #######This is where sysGrowth will analyze systems pnl trajectory and
    #####apply the best system to trade into the autotrader
    ###### ie. alphaSignals.trade2() ###this would be running trade2 system
    
    for xr in range(24):  ####24 is amount of systems we have to get the sysGrowth calcs
        sysR = sysGrowth.Main()[xr]
        ##print(str(sysR))
        sysList.append(sysR)
    #print('System Growth Calculations Stated')
    
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

    #print('System Sum Calculations Stated')
    
    return sysList, sysTList

def checkSignal():
    lenBuy = 0
    lenSell = 0
    lenActive = 0
    sysMin = []
    sysList = []
    sysTList = []
    sysTrack = []
    sysTracker = []
    averageSystem = 0
    minSysTotal = 0
    
    checkSystem()
    sysList = checkSystem()[0] ###Trajectory
    sysTList = checkSystem()[1] ###Total System
    
    maxSys = max(sysList)  
    maxSysT = max(sysTList) 
    indexSys = sysList.index(maxSys) ##Trajectory
    indexSysT = sysTList.index(maxSysT) ##Total System
    
    averageSystem = float(sum(sysTList) / 24)
    
    if averageSystem <= -250:
        #print('Resetting Trade History Tracker')
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
    
    systemRun = False
    
    if maxSysT >= 1.11:
        if indexSysT == 0:
            #print('System 1 Is Canditate')
            sysTrack.append(sysTList[0])
            sysTracker.append(0)
            #print('Running System 1')
            alphaSignals.system1()
            systemRun = True
        elif indexSysT == 1:
            #print('System 2 Is Canditate')
            sysTrack.append(sysTList[1])
            sysTracker.append(1)
            #print('Running System 2')
            alphaSignals.system2()
            systemRun = True
        elif indexSysT == 2:
            #print('System 3 Is Canditate')
            sysTrack.append(sysTList[2])
            sysTracker.append(2)
            #print('Running System 3')
            alphaSignals.system3()
            systemRun = True
        elif indexSysT == 3:
            #print('System 4 Is Canditate')
            sysTrack.append(sysTList[3])
            sysTracker.append(3)
            #print('Running System 4')
            alphaSignals.system4()
            systemRun = True
        elif indexSysT == 4:
            #print('System 5 Is Canditate')
            sysTrack.append(sysTList[4])
            sysTracker.append(4)
            #print('Running System 5')
            alphaSignals.system5()
            systemRun = True            
        elif indexSysT == 5:
            #print('System 6 Is Canditate')
            sysTrack.append(sysTList[5])
            sysTracker.append(5)
            #print('Running System 6')
            alphaSignals.system6()
            systemRun = True            
        elif indexSysT == 6:
            #print('System 7 Is Canditate')
            sysTrack.append(sysTList[6])
            sysTracker.append(6)
            #print('Running System 7')
            alphaSignals.system7()
            systemRun = True            
        elif indexSysT == 7:
            #print('System 8 Is Canditate')
            sysTrack.append(sysTList[7])
            sysTracker.append(7)
            #print('Running System 8')
            alphaSignals.system8()
            systemRun = True            
        elif indexSysT == 8:
            #print('System 9 Is Canditate')
            sysTrack.append(sysTList[8])
            sysTracker.append(8)
            #print('Running System 9')
            alphaSignals.system9()
            systemRun = True            
        elif indexSysT == 9:
            #print('System 10 Is Canditate')
            sysTrack.append(sysTList[9])
            sysTracker.append(9)
            #print('Running System 10')
            alphaSignals.system10()
            systemRun = True            
        elif indexSysT == 10:
            #print('System 11 Is Canditate')
            sysTrack.append(sysTList[10])
            sysTracker.append(10)
            #print('Running System 11')
            alphaSignals.system11()
            systemRun = True                
        elif indexSysT == 11:
            #print('System 12 Is Canditate')
            sysTrack.append(sysTList[11])
            sysTracker.append(11)
            #print('Running System 12')
            alphaSignals.system12()
            systemRun = True 
        elif indexSysT == 12:
            #print('System 13 Is Canditate')
            sysTrack.append(sysTList[12])
            sysTracker.append(12)
            #print('Running System 13')
            alphaSignals.system13()
            systemRun = True
        elif indexSysT == 13:
            #print('System 14 Is Canditate')
            sysTrack.append(sysTList[13])
            sysTracker.append(13)
            #print('Running System 14')
            alphaSignals.system14()
            systemRun = True
        elif indexSysT == 14:
            #print('System 15 Is Canditate')
            sysTrack.append(sysTList[14])
            sysTracker.append(14)
            #print('Running System 15')
            alphaSignals.system15()
            systemRun = True            
        elif indexSysT == 15:
            #print('System 16 Is Canditate')
            sysTrack.append(sysTList[15])
            sysTracker.append(15)
            #print('Running System 16')
            alphaSignals.system16()
            systemRun = True            
        elif indexSysT == 16:
            #print('System 17 Is Canditate')
            sysTrack.append(sysTList[16])
            sysTracker.append(16)
            #print('Running System 17')
            alphaSignals.system17()
            systemRun = True            
        elif indexSysT == 17:
            #print('System 18 Is Canditate')
            sysTrack.append(sysTList[17])
            sysTracker.append(17)
            #print('Running System 18')
            alphaSignals.system18()
            systemRun = True            
        elif indexSysT == 18:
            #print('System 19 Is Canditate')
            sysTrack.append(sysTList[18])
            sysTracker.append(18)
            #print('Running System 19')
            alphaSignals.system19()
            systemRun = True            
        elif indexSysT == 19:
            #print('System 20 Is Canditate')
            sysTrack.append(sysTList[19])
            sysTracker.append(19)
            #print('Running System 20')
            alphaSignals.system20()
            systemRun = True
        elif indexSysT == 20:
            #print('System 21 Is Canditate')
            sysTrack.append(sysTList[20])
            sysTracker.append(20)
            #print('Running System 21')
            alphaSignals.system21()
            systemRun = True
        elif indexSysT == 21:
            #print('System 22 Is Canditate')
            sysTrack.append(sysTList[21])
            sysTracker.append(21)
            #print('Running System 22')
            alphaSignals.system22()
            systemRun = True            
        elif indexSysT == 22:
            #print('System 23 Is Canditate')
            sysTrack.append(sysTList[22])
            sysTracker.append(22)
            #print('Running System 23')
            alphaSignals.system23()
            systemRun = True
        elif indexSysT == 23:
            #print('System 24 Is Canditate')
            sysTrack.append(sysTList[23])
            sysTracker.append(23)
            #print('Running System 24')
            alphaSignals.system24()
            systemRun = True
    else:
        #print('Head To Fucking Lake Brother!')
        sleep(15)
        systemRun = False
            
    if systemRun == True: 
        symbActive = []
        symbActiveS = []
        symbActive = list(alphaSignals.symbol_listActiveBuy)
        symbActiveS = list(alphaSignals.symbol_listActiveSell)
        lenBuy = len(symbActive)
        lenSell = len(symbActiveS)
        lenBB = len(symbolLongT)
        lenSS = len(symbolShortT)
            
        if lenBuy > 0 and lenBB < 9:
            
            for aa in range(lenBuy):
                
                print('Signal Found ' + str(symbActive[aa]))
                symbolLongT.append(symbActive[aa])
                
                if alphaSignals.buy_PriceLong[aa] >= 1 and alphaSignals.buy_PriceLong[aa] < 10:
                    
                    entryLongT.append(str("{:.3f}".format(alphaSignals.buy_PriceLong[aa])))
                    targetLongT.append(str("{:.3f}".format(alphaSignals.target_PriceLong[aa])))
                    stopLongT.append(str("{:.3f}".format(alphaSignals.stop_PriceLong[aa])))
                    quantityLongT.append(int(alphaSignals.qty_Long[aa]))                
                    
                elif alphaSignals.buy_PriceLong[aa] >= 10 and alphaSignals.buy_PriceLong[aa] <= 250: 
                    
                    entryLongT.append(str("{:.2f}".format(alphaSignals.buy_PriceLong[aa])))
                    targetLongT.append(str("{:.2f}".format(alphaSignals.target_PriceLong[aa])))
                    stopLongT.append(str("{:.2f}".format(alphaSignals.stop_PriceLong[aa])))
                    quantityLongT.append(int(alphaSignals.qty_Long[aa])) 

                elif alphaSignals.buy_PriceLong[aa] > 250:
                    
                    entryLongT.append(str("{:.2f}".format(alphaSignals.buy_PriceLong[aa])))
                    targetLongT.append(str("{:.2f}".format(alphaSignals.target_PriceLong[aa])))
                    stopLongT.append(str("{:.2f}".format(alphaSignals.stop_PriceLong[aa])))
                    quantityLongT.append(str("{:.1f}".format(alphaSignals.qty_Long[aa])))
                    
                else:
                    
                    entryLongT.append(str("{:.4f}".format(alphaSignals.buy_PriceLong[aa])))
                    targetLongT.append(str("{:.4f}".format(alphaSignals.target_PriceLong[aa])))
                    stopLongT.append(str("{:.4f}".format(alphaSignals.stop_PriceLong[aa])))
                    quantityLongT.append(int(alphaSignals.qty_Long[aa]))
                
                telegram_send.send(disable_web_page_preview=True, conf='user1.conf',messages=["Buy Signal " + str(symbActive[aa]) + "\n" + \
                                                    "Entry: " + str("{:.4f}".format(float(alphaSignals.buy_PriceLong[aa]))) + "\n" + \
                                                    "Exit: " + str("{:.4f}".format(float(alphaSignals.stop_PriceLong[aa]))) + "\n" + \
                                                    "Target: " + str("{:.4f}".format(float(alphaSignals.target_PriceLong[aa]))) + "\n" + \
                                                    "Quantity: " + str("{:.4f}".format(float(alphaSignals.qty_Long[aa]))) + "\n" +
                                                    "https://www.binance.com/en/trade/" + str(symbActive[aa]) + "?type=perpetual"])
                
                alphaSignals.symbol_listActiveBuy.remove(symbActive[aa])
                symbActive.remove(symbActive[aa])
                alphaSignals.buy_PriceLong.remove(alphaSignals.buy_PriceLong[aa])
                alphaSignals.target_PriceLong.remove(alphaSignals.target_PriceLong[aa])
                alphaSignals.stop_PriceLong.remove(alphaSignals.stop_PriceLong[aa])
                alphaSignals.qty_Long.remove(alphaSignals.qty_Long[aa])
                break
            
        elif lenSell > 0 and lenSS < 9:
            
            for bb in range(lenSell):
                
                print('Signal Found ' + str(symbActiveS[bb]))
                symbolShortT.append(symbActiveS[bb])
                
                if alphaSignals.buy_PriceShort[bb] >= 1 and alphaSignals.buy_PriceShort[bb] < 10:
                    
                    entryShortT.append(str("{:.3f}".format(alphaSignals.buy_PriceShort[bb])))
                    targetShortT.append(str("{:.3f}".format(alphaSignals.target_PriceShort[bb])))
                    stopShortT.append(str("{:.3f}".format(alphaSignals.stop_PriceShort[bb])))
                    quantityShortT.append(int(alphaSignals.qty_Short[bb]))
                    
                elif alphaSignals.buy_PriceShort[bb] >= 10 and alphaSignals.buy_PriceShort[bb] <= 250:

                    entryShortT.append(str("{:.2f}".format(alphaSignals.buy_PriceShort[bb])))
                    targetShortT.append(str("{:.2f}".format(alphaSignals.target_PriceShort[bb])))
                    stopShortT.append(str("{:.2f}".format(alphaSignals.stop_PriceShort[bb])))
                    quantityShortT.append(int(alphaSignals.qty_Short[bb]))
                    
                elif alphaSignals.buy_PriceShort[bb] > 250:
                    
                    entryShortT.append(str("{:.2f}".format(alphaSignals.buy_PriceShort[bb])))
                    targetShortT.append(str("{:.2f}".format(alphaSignals.target_PriceShort[bb])))
                    stopShortT.append(str("{:.2f}".format(alphaSignals.stop_PriceShort[bb])))
                    quantityShortT.append(str("{:.1f}".format(alphaSignals.qty_Short[bb])))
                    
                else:  
                    
                    entryShortT.append(str("{:.4f}".format(alphaSignals.buy_PriceShort[bb])))
                    targetShortT.append(str("{:.4f}".format(alphaSignals.target_PriceShort[bb])))
                    stopShortT.append(str("{:.4f}".format(alphaSignals.stop_PriceShort[bb])))
                    quantityShortT.append(int(alphaSignals.qty_Short[bb]))  
                
                telegram_send.send(disable_web_page_preview=True, conf='user1.conf',messages=["Sell Signal " + str(symbActiveS[bb]) + "\n" + \
                                                    "Entry: " + str("{:.4f}".format(float(alphaSignals.buy_PriceShort[bb]))) + "\n" + \
                                                    "Exit: " + str("{:.4f}".format(float(alphaSignals.stop_PriceShort[bb]))) + "\n" + \
                                                    "Target: " + str("{:.4f}".format(float(alphaSignals.target_PriceShort[bb]))) + "\n" + \
                                                    "Quantity: " + str("{:.4f}".format(float(alphaSignals.qty_Short[bb]))) + "\n" +
                                                    "https://www.binance.com/en/trade/" + str(symbActiveS[bb]) + "?type=perpetual"])
                
                alphaSignals.symbol_listActiveSell.remove(symbActiveS[bb])
                symbActiveS.remove(symbActiveS[bb])
                alphaSignals.buy_PriceShort.remove(alphaSignals.buy_PriceShort[bb])
                alphaSignals.target_PriceShort.remove(alphaSignals.target_PriceShort[bb])
                alphaSignals.stop_PriceShort.remove(alphaSignals.stop_PriceShort[bb])
                alphaSignals.qty_Short.remove(alphaSignals.qty_Short[bb])
                break
        else:
            lenLen = float(lenBB) + float(lenSS)
            #print('Current Trades ' + str(lenLen))
            #sleep(5)
        
def localTracker():
    conNode = False
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    
    activeBuy = len(symbolLongT)
    if activeBuy > 0:
        for yx in range(activeBuy):
            pnl1 = 0
            pnlLongWin = 0
            pnl2 = 0
            pnlLongLose = 0
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines1 = client.futures_klines(symbol=symbolLongT[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
            except Exception as e:
                pd = open('pingData alphaData', 'a')
                pd.write("\n" + str(t) + str(e))
                pd.close()
                #print(str(e)) 
                sleep(60)
                conNode = True
                
            while conNode == True:
                try:
                    client = Client(apiData.APIKey, apiData.SecretKey)
                    klines1 = client.futures_klines(symbol=symbolLongT[yx],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    conNode = False
                except Exception as e:
                    #print(str(e))
                    sleep(60)
                    conNode = True
                
            currentPrice1 = float(klines1[0][4]) 
            
            if float(currentPrice1) >= float(targetLongT[yx]):
                #print(currentPrice1)
                #print(targetLongT[yx])
                #if long makes money
                pnl1 = float(currentPrice1) - float(entryLongT[yx])
                pnlLongWin = float(pnl1) * float(quantityLongT[yx])
            
                telegram_send.send(conf='user1.conf',messages=[ str(symbolLongT[yx]) + " Trade Closed @ PNL: " + str("{:.4f}".format(pnlLongWin))])

                f = open('deltaLong.txt', 'a')
                f.write("\n" + int(1))
                f.close()
                
                f = open('alphaData.txt', 'a')
                f.write("\n" + str("{:.4f}".format(pnlLongWin)))
                f.close()
                
                f = open('alphaLog.txt', 'a')
                f.write("\n" + str(t) + "    " + str(symbolLongT[yx]) + "    " + str("{:.4f}".format(float(entryLongT[yx]))) \
                + "    " +  str("{:.4f}".format(float(targetLongT[yx]))) + "    " +  str("{:.4f}".format(float(stopLongT[yx]))) + "    " \
                + "    " + str("{:.4f}".format(float(quantityLongT[yx])))   + "    " + str("{:.4f}".format(pnlLongWin)))
                f.close()
                
                alphaSignals.symbol_list.append(symbolLongT[yx])
                symbolLongT.remove(symbolLongT[yx])
                entryLongT.remove(entryLongT[yx])
                stopLongT.remove(stopLongT[yx])
                targetLongT.remove(targetLongT[yx])
                quantityLongT.remove(quantityLongT[yx])
                break
            
            if float(currentPrice1) <= float(stopLongT[yx]):
                #print(currentPrice1)
                #print(targetLongT[yx])
                #if long loses money
                pnl2 = float(entryLongT[yx]) - float(currentPrice1)
                pnlLongLose = float(pnl2) * float(quantityLongT[yx])
            
                telegram_send.send(conf='user1.conf',messages=[ str(symbolLongT[yx]) + " Trade Closed @ PNL: -" + str("{:.4f}".format(pnlLongLose))])

                f = open('deltaLong.txt', 'a')
                f.write("\n" + int(-1))
                f.close()

                f = open('alphaData.txt', 'a')
                f.write("\n" + "-" + str("{:.4f}".format(pnlLongLose)))
                f.close()
                
                f = open('alphaLog.txt', 'a')
                f.write("\n" + str(t) + "    " + str(symbolLongT[yx]) + "    " + str("{:.4f}".format(float(entryLongT[yx]))) \
                + "    " +  str("{:.4f}".format(float(targetLongT[yx]))) + "    " +  str("{:.4f}".format(float(stopLongT[yx]))) + "    " \
                + "    -" + str("{:.4f}".format(float(quantityLongT[yx]))) + "    -" + str("{:.4f}".format(pnlLongLose)))
                f.close()
                
                alphaSignals.symbol_list.append(symbolLongT[yx])
                symbolLongT.remove(symbolLongT[yx])
                entryLongT.remove(entryLongT[yx])
                stopLongT.remove(stopLongT[yx])
                targetLongT.remove(targetLongT[yx])
                quantityLongT.remove(quantityLongT[yx])
                break
            break
        
    activeSell = len(symbolShortT)
    if activeSell > 0:
        for yv in range(activeSell):
            pnl3 = 0
            pnlShortWin = 0
            pnl4 = 0
            pnlShortLose = 0
            #sleep(3)
            ##print(symbol_listActiveSell[yv])
            try:
                client = Client(apiData.APIKey, apiData.SecretKey)
                klines2 = client.futures_klines(symbol=symbolShortT[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
            except Exception as e:
                pd = open('pingData alphaData', 'a')
                pd.write("\n" + str(t) + str(e))
                pd.close()
                #print(str(e))
                sleep(60)
                conNode = True
            except MaxRetryError as e:
                pd = open('pingData alphaData', 'a')
                pd.write("\n" + str(t) + str(e))
                pd.close()
                #print(str(e))
                sleep(200)
                conNode = True
                
            while conNode == True:
                try:
                    client = Client(apiData.APIKey, apiData.SecretKey)
                    klines2 = client.futures_klines(symbol=symbolShortT[yv],interval=KLINE_INTERVAL_5MINUTE, limit=1)
                    conNode = False
                except Exception as e:
                    #print(str(e))
                    sleep(60)
                    conNode = True
                except MaxRetryError as e:
                    #print(str(e))
                    sleep(200)
                    conNode = True
                
            currentPrice2 = float(klines2[0][4])
            
            if float(currentPrice2) <= float(targetShortT[yv]): 
                #print(currentPrice2)
                #print(targetShortT[yv])
                #if short makes money
                pnl3 = float(entryShortT[yv]) - float(currentPrice2) #this is $amount trying to aquire on short
                pnlShortWin = float(pnl3) * float(quantityShortT[yv])
        
                telegram_send.send(conf='user1.conf',messages=[ str(symbolShortT[yv]) + " Trade Closed @ PNL: " + str("{:.4f}".format(pnlShortWin))])

                f = open('deltaShort.txt', 'a')
                f.write("\n" + int(1))
                f.close()
                
                f = open('alphaData.txt', 'a')
                f.write("\n" + str("{:.4f}".format(pnlShortWin)))
                f.close()
                
                f = open('alphaLog.txt', 'a')
                f.write("\n" + str(t) + "    " + str(symbolShortT[yv]) + "    " + str("{:.4f}".format(float(entryShortT[yv]))) \
                + "    " +  str("{:.4f}".format(float(targetShortT[yv]))) + "    " +  str("{:.4f}".format(float(stopShortT[yv]))) + "    " \
                + "    -" + str("{:.4f}".format(float(quantityShortT[yv]))) + "    " + str("{:.4f}".format(pnlShortWin)))
                f.close()
                
                alphaSignals.symbol_list.append(symbolShortT[yv])
                symbolShortT.remove(symbolShortT[yv])
                entryShortT.remove(entryShortT[yv])
                stopShortT.remove(stopShortT[yv])
                targetShortT.remove(targetShortT[yv])
                quantityShortT.remove(quantityShortT[yv])
                break
        
            if float(currentPrice2) >= float(stopShortT[yv]):
                #print(currentPrice2)
                #print(targetShortT[yv])                
                #if short loses money
                pnl4 = float(currentPrice2) - float(entryShortT[yv])
                pnlShortLose = float(pnl4) * float(quantityShortT[yv])
            
                telegram_send.send(conf='user1.conf',messages=[ str(symbolShortT[yv]) + " Trade Closed @ PNL: -" + str("{:.4f}".format(pnlShortLose))])

                f = open('deltaShort.txt', 'a')
                f.write("\n" + int(-1))
                f.close()
                                            
                f = open('alphaData.txt', 'a')
                f.write("\n" + "-" + str("{:.4f}".format(pnlShortLose)))
                f.close()
                
                f = open('alphaLog.txt', 'a')
                f.write("\n" + str(t) + "    " + str(symbolShortT[yv]) + "    " + str("{:.4f}".format(float(entryShortT[yv]))) \
                + "    " +  str("{:.4f}".format(float(targetShortT[yv]))) + "    " +  str("{:.4f}".format(float(stopShortT[yv]))) + "    " \
                + "    -" + str("{:.4f}".format(float(quantityShortT[yv]))) + "    -" + str("{:.4f}".format(pnlShortLose)))
                f.close()
                    
                alphaSignals.symbol_list.append(symbolShortT[yv])
                symbolShortT.remove(symbolShortT[yv])
                entryShortT.remove(entryShortT[yv])
                stopShortT.remove(stopShortT[yv])
                targetShortT.remove(targetShortT[yv])
                quantityShortT.remove(quantityShortT[yv])
                break
            break
def Main():
    
    initialProcessing = True
    
    now = datetime.now()
    tt = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    #print("[Connection Established Alpha Autotrader Live For Futures!]")
    telegram_send.send(conf='user1.conf',messages=["|||||autoTrader||||| Connection Established @ " + str(tt)])
    #print(str(tt))
    
    checkSystem()
    
    while initialProcessing == True:
        now = datetime.now()
        ttt = now.strftime("%M:%S")
        try:
            checkSystem()    
            checkSignal()
            localTracker()
        except Exception as e:
            #print(str(e))
            sleep(10)
            continue

if __name__ == '__main__':
    Main()
