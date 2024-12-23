#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:01 2020

@ygoats
"""

import telegram_send
from datetime import datetime
from time import sleep
    
def systemOne():
    
    f = open("dataSwing5M[M10][F].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass
  
    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemTwo():
    
    f = open("dataSwing15M[M10][F].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemThree():
    
    f = open("dataSwing1H[M10][F].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
      
def systemFour():
    
    f = open("dataSwing4H[M10][F].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemFive():
    
    f = open("dataSwing5M[M10][F][OI].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemSix():
    
    f = open("dataSwing15M[M10][F][OI].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemSeven():
    
    f = open("dataSwing1H[M10][F][OI].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemEight():
    
    f = open("dataSwing4H[M10][F][OI].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow
    
def systemNine():
    
    f = open("dataSwing5M[M10][F][4:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTen():
    
    f = open("dataSwing15M[M10][F][4:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemEleven():
    
    f = open("dataSwing1H[M10][F][4:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwelve():
    
    f = open("dataSwing4H[M10][F][4:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemThirteen():
    
    f = open("dataSwing5M[M10][F][10:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemFourteen():
    
    f = open("dataSwing15M[M10][F][10:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemFifteen():
    
    f = open("dataSwing1H[M10][F][10:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemSixteen():
    
    f = open("dataSwing4H[M10][F][10:1].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemSeventeen():
    
    f = open("dataSwing5M[M10][F][ATR62].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemEighteen():
    
    f = open("dataSwing15M[M10][F][ATR62].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemNineteen():
    
    f = open("dataSwing1H[M10][F][ATR62].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwenty():
    
    f = open("dataSwing4H[M10][F][ATR62].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentyOne():
    
    f = open("dataSwing5M[M10][F][ATR100].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentyTwo():
    
    f = open("dataSwing15M[M10][F][ATR100].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentyThree():
    
    f = open("dataSwing1H[M10][F][ATR100].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentyFour():
    
    f = open("dataSwing4H[M10][F][ATR100].txt", 'r')
    s = f.readlines()
    p = str(s)

    total = 0

    for line in s:
        #print(float(line))
        printnum = 0
        try: 
            printnum += float(line)
            total += printnum
            #print("Adding: ", printnum)
        except ValueError:
            pass

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def Main():
    
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    
    #print('System Growth Analyzer Connected ' + str(t))

    dataEntriesA = 0
    dataEntriesX = 0
        
    try:
        f = open('aGain.txt', 'r')
        dataEntriesA = len(f.readlines())
        #print("Data Entries = " + str(dataEntriesA))
        f.close() 
    except FileNotFoundError as e:
        print(str(e))
        
    try:
        f = open('xGain.txt', 'r')
        dataEntriesX = len(f.readlines())
        #print("Data Entries = " + str(dataEntriesX))
        f.close() 
    except FileNotFoundError as e:
        print(str(e))
    
    if dataEntriesA < 8 and dataEntriesX < 8:
        print('Algorithms require more data')
        sleep(10)
              
    if dataEntriesA >= 8 and dataEntriesX >= 8:
            
        now = datetime.now()
        t = now.strftime("%M:%S")
        #print(str(t))
        
        #print('Processessing A Gains')

        f = open('aGain.txt', 'r')
        lines = f.readlines()
        oneA = float(lines[-1]) - float(lines[-2])
        oneB = float(lines[-2]) - float(lines[-3])
        oneC = float(lines[-3]) - float(lines[-4])
        oneD = float(lines[-4]) - float(lines[-5])
        oneE = float(lines[-5]) - float(lines[-6])
        oneF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        oneSum = oneA + oneB + oneC + oneD + oneE + oneF
        oneAvg = oneSum / 6

        #print('Processessing B Gains')

        f = open('bGain.txt', 'r')
        lines = f.readlines()
        twoA = float(lines[-1]) - float(lines[-2])
        twoB = float(lines[-2]) - float(lines[-3])
        twoC = float(lines[-3]) - float(lines[-4])
        twoD = float(lines[-4]) - float(lines[-5])
        twoE = float(lines[-5]) - float(lines[-6])
        twoF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twoSum = twoA + twoB + twoC + twoD + twoE + twoF
        twoAvg = twoSum / 6             
 
        #print('Processessing C Gains')
        
        f = open('cGain.txt', 'r')
        lines = f.readlines()
        threeA = float(lines[-1]) - float(lines[-2])
        threeB = float(lines[-2]) - float(lines[-3])
        threeC = float(lines[-3]) - float(lines[-4])
        threeD = float(lines[-4]) - float(lines[-5])
        threeE = float(lines[-5]) - float(lines[-6])
        threeF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        threeSum = threeA + threeB + threeC + threeD + threeE + threeF
        threeAvg = threeSum / 6

        #print('Processessing E Gains')

        f = open('dGain.txt', 'r')
        lines = f.readlines()
        fourA = float(lines[-1]) - float(lines[-2])
        fourB = float(lines[-2]) - float(lines[-3])
        fourC = float(lines[-3]) - float(lines[-4])
        fourD = float(lines[-4]) - float(lines[-5])
        fourE = float(lines[-5]) - float(lines[-6])
        fourF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        fourSum = fourA + fourB + fourC + fourD + fourE + fourF
        fourAvg = fourSum / 6

        #print('Processessing E Gains')

        f = open('eGain.txt', 'r')
        lines = f.readlines()
        fiveA = float(lines[-1]) - float(lines[-2])
        fiveB = float(lines[-2]) - float(lines[-3])
        fiveC = float(lines[-3]) - float(lines[-4])
        fiveD = float(lines[-4]) - float(lines[-5])
        fiveE = float(lines[-5]) - float(lines[-6])
        fiveF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        fiveSum = fiveA + fiveB + fiveC + fiveD + fiveE + fiveF
        fiveAvg = fiveSum / 6

        #print('Processessing F Gains')

        f = open('fGain.txt', 'r')
        lines = f.readlines()
        sixA = float(lines[-1]) - float(lines[-2])
        sixB = float(lines[-2]) - float(lines[-3])
        sixC = float(lines[-3]) - float(lines[-4])
        sixD = float(lines[-4]) - float(lines[-5])
        sixE = float(lines[-5]) - float(lines[-6])
        sixF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        sixSum = sixA + sixB + sixC + sixD + sixE + sixF
        sixAvg = sixSum / 6

        #print('Processessing G Gains')

        f = open('gGain.txt', 'r')
        lines = f.readlines()
        sevenA = float(lines[-1]) - float(lines[-2])
        sevenB = float(lines[-2]) - float(lines[-3])
        sevenC = float(lines[-3]) - float(lines[-4])
        sevenD = float(lines[-4]) - float(lines[-5])
        sevenE = float(lines[-5]) - float(lines[-6])
        sevenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        sevenSum = sevenA + sevenB + sevenC + sevenD + sevenE + sevenF
        sevenAvg = sevenSum / 6

        #print('Processessing H Gains')

        f = open('hGain.txt', 'r')
        lines = f.readlines()
        eightA = float(lines[-1]) - float(lines[-2])
        eightB = float(lines[-2]) - float(lines[-3])
        eightC = float(lines[-3]) - float(lines[-4])
        eightD = float(lines[-4]) - float(lines[-5])
        eightE = float(lines[-5]) - float(lines[-6])
        eightF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        eightSum = eightA + eightB + eightC + eightD + eightE + eightF
        eightAvg = eightSum / 6

        #print('Processessing I Gains')

        f = open('iGain.txt', 'r')
        lines = f.readlines()
        nineA = float(lines[-1]) - float(lines[-2])
        nineB = float(lines[-2]) - float(lines[-3])
        nineC = float(lines[-3]) - float(lines[-4])
        nineD = float(lines[-4]) - float(lines[-5])
        nineE = float(lines[-5]) - float(lines[-6])
        nineF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        nineSum = nineA + nineB + nineC + nineD + nineE + nineF
        nineAvg = nineSum / 6

        #print('Processessing J Gains')

        f = open('jGain.txt', 'r')
        lines = f.readlines()
        tenA = float(lines[-1]) - float(lines[-2])
        tenB = float(lines[-2]) - float(lines[-3])
        tenC = float(lines[-3]) - float(lines[-4])
        tenD = float(lines[-4]) - float(lines[-5])
        tenE = float(lines[-5]) - float(lines[-6])
        tenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        tenSum = tenA + tenB + tenC + tenD + tenE + tenF
        tenAvg = tenSum / 6

        #print('Processessing K Gains')

        f = open('kGain.txt', 'r')
        lines = f.readlines()
        elevenA = float(lines[-1]) - float(lines[-2])
        elevenB = float(lines[-2]) - float(lines[-3])
        elevenC = float(lines[-3]) - float(lines[-4])
        elevenD = float(lines[-4]) - float(lines[-5])
        elevenE = float(lines[-5]) - float(lines[-6])
        elevenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        elevenSum = elevenA + elevenB + elevenC + elevenD + elevenE + elevenF
        elevenAvg = elevenSum / 6

        #print('Processessing L Gains')

        f = open('lGain.txt', 'r')
        lines = f.readlines()
        twelveA = float(lines[-1]) - float(lines[-2])
        twelveB = float(lines[-2]) - float(lines[-3])
        twelveC = float(lines[-3]) - float(lines[-4])
        twelveD = float(lines[-4]) - float(lines[-5])
        twelveE = float(lines[-5]) - float(lines[-6])
        twelveF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twelveSum = twelveA + twelveB + twelveC + twelveD + twelveE + twelveF
        twelveAvg = twelveSum / 6

        #print('Processessing M Gains')

        f = open('mGain.txt', 'r')
        lines = f.readlines()
        thirteenA = float(lines[-1]) - float(lines[-2])
        thirteenB = float(lines[-2]) - float(lines[-3])
        thirteenC = float(lines[-3]) - float(lines[-4])
        thirteenD = float(lines[-4]) - float(lines[-5])
        thirteenE = float(lines[-5]) - float(lines[-6])
        thirteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        thirteenSum = thirteenA + thirteenB + thirteenC + thirteenD + thirteenE + thirteenF
        thirteenAvg = thirteenSum / 6

        #print('Processessing N Gains')

        f = open('nGain.txt', 'r')
        lines = f.readlines()
        fourteenA = float(lines[-1]) - float(lines[-2])
        fourteenB = float(lines[-2]) - float(lines[-3])
        fourteenC = float(lines[-3]) - float(lines[-4])
        fourteenD = float(lines[-4]) - float(lines[-5])
        fourteenE = float(lines[-5]) - float(lines[-6])
        fourteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        fourteenSum = fourteenA + fourteenB + fourteenC + fourteenD + fourteenE + fourteenF
        fourteenAvg = fourteenSum / 6

        f = open('oGain.txt', 'r')
        lines = f.readlines()
        fifteenA = float(lines[-1]) - float(lines[-2])
        fifteenB = float(lines[-2]) - float(lines[-3])
        fifteenC = float(lines[-3]) - float(lines[-4])
        fifteenD = float(lines[-4]) - float(lines[-5])
        fifteenE = float(lines[-5]) - float(lines[-6])
        fifteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        fifteenSum = fifteenA + fifteenB + fifteenC + fifteenD + fifteenE + fifteenF
        fifteenAvg = fifteenSum / 6

        #print('Processessing P Gains')

        f = open('pGain.txt', 'r')
        lines = f.readlines()
        sixteenA = float(lines[-1]) - float(lines[-2])
        sixteenB = float(lines[-2]) - float(lines[-3])
        sixteenC = float(lines[-3]) - float(lines[-4])
        sixteenD = float(lines[-4]) - float(lines[-5])
        sixteenE = float(lines[-5]) - float(lines[-6])
        sixteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        sixteenSum = sixteenA + sixteenB + sixteenC + sixteenD + sixteenE + sixteenF
        sixteenAvg = sixteenSum / 6

        #print('Processessing Q Gains')

        f = open('qGain.txt', 'r')
        lines = f.readlines()
        seventeenA = float(lines[-1]) - float(lines[-2])
        seventeenB = float(lines[-2]) - float(lines[-3])
        seventeenC = float(lines[-3]) - float(lines[-4])
        seventeenD = float(lines[-4]) - float(lines[-5])
        seventeenE = float(lines[-5]) - float(lines[-6])
        seventeenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        seventeenSum = seventeenA + seventeenB + seventeenC + seventeenD + seventeenE + seventeenF
        seventeenAvg = seventeenSum / 6

        #print('Processessing R Gains')

        f = open('rGain.txt', 'r')
        lines = f.readlines()
        eighteenA = float(lines[-1]) - float(lines[-2])
        eighteenB = float(lines[-2]) - float(lines[-3])
        eighteenC = float(lines[-3]) - float(lines[-4])
        eighteenD = float(lines[-4]) - float(lines[-5])
        eighteenE = float(lines[-5]) - float(lines[-6])
        eighteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        eighteenSum = eighteenA + eighteenB + eighteenC + eighteenD + eighteenE + eighteenF
        eighteenAvg = eighteenSum / 6

        #print('Processessing S Gains')

        f = open('sGain.txt', 'r')
        lines = f.readlines()
        nineteenA = float(lines[-1]) - float(lines[-2])
        nineteenB = float(lines[-2]) - float(lines[-3])
        nineteenC = float(lines[-3]) - float(lines[-4])
        nineteenD = float(lines[-4]) - float(lines[-5])
        nineteenE = float(lines[-5]) - float(lines[-6])
        nineteenF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        nineteenSum = nineteenA + nineteenB + nineteenC + nineteenD + nineteenE + nineteenF
        nineteenAvg = nineteenSum / 6

        #print('Processessing T Gains')

        f = open('tGain.txt', 'r')
        lines = f.readlines()
        twentyA = float(lines[-1]) - float(lines[-2])
        twentyB = float(lines[-2]) - float(lines[-3])
        twentyC = float(lines[-3]) - float(lines[-4])
        twentyD = float(lines[-4]) - float(lines[-5])
        twentyE = float(lines[-5]) - float(lines[-6])
        twentyF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twentySum = twentyA + twentyB + twentyC + twentyD + twentyE + twentyF
        twentyAvg = twentySum / 6

        #print('Processessing U Gains')

        f = open('uGain.txt', 'r')
        lines = f.readlines()
        twentyoneA = float(lines[-1]) - float(lines[-2])
        twentyoneB = float(lines[-2]) - float(lines[-3])
        twentyoneC = float(lines[-3]) - float(lines[-4])
        twentyoneD = float(lines[-4]) - float(lines[-5])
        twentyoneE = float(lines[-5]) - float(lines[-6])
        twentyoneF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twentyoneSum = twentyoneA + twentyoneB + twentyoneC + twentyoneD + twentyoneE + twentyoneF
        twentyoneAvg = twentyoneSum / 6

        #print('Processessing V Gains')

        f = open('vGain.txt', 'r')
        lines = f.readlines()
        twentytwoA = float(lines[-1]) - float(lines[-2])
        twentytwoB = float(lines[-2]) - float(lines[-3])
        twentytwoC = float(lines[-3]) - float(lines[-4])
        twentytwoD = float(lines[-4]) - float(lines[-5])
        twentytwoE = float(lines[-5]) - float(lines[-6])
        twentytwoF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twentytwoSum = twentytwoA + twentytwoB + twentytwoC + twentytwoD + twentytwoE + twentytwoF
        twentytwoAvg = twentytwoSum / 6

        #print('Processessing W Gains')

        f = open('wGain.txt', 'r')
        lines = f.readlines()
        twentythreeA = float(lines[-1]) - float(lines[-2])
        twentythreeB = float(lines[-2]) - float(lines[-3])
        twentythreeC = float(lines[-3]) - float(lines[-4])
        twentythreeD = float(lines[-4]) - float(lines[-5])
        twentythreeE = float(lines[-5]) - float(lines[-6])
        twentythreeF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twentythreeSum = twentythreeA + twentythreeB + twentythreeC + twentythreeD + twentythreeE + twentythreeF
        twentythreeAvg = twentythreeSum / 6

        #print('Processessing W Gains')

        f = open('xGain.txt', 'r')
        lines = f.readlines()
        twentyfourA = float(lines[-1]) - float(lines[-2])
        twentyfourB = float(lines[-2]) - float(lines[-3])
        twentyfourC = float(lines[-3]) - float(lines[-4])
        twentyfourD = float(lines[-4]) - float(lines[-5])
        twentyfourE = float(lines[-5]) - float(lines[-6])
        twentyfourF = float(lines[-6]) - float(lines[-7])
        f.close()
        
        twentyfourSum = twentyfourA + twentyfourB + twentyfourC + twentyfourD + twentyfourE + twentyfourF
        twentyfourAvg = twentyfourSum / 6
        
        return oneAvg, twoAvg, threeAvg, fourAvg, fiveAvg, sixAvg, sevenAvg, eightAvg, nineAvg, tenAvg, \
            elevenAvg, twelveAvg, thirteenAvg, fourteenAvg, fifteenAvg, sixteenAvg, seventeenAvg, \
            eighteenAvg, nineteenAvg, twentyAvg, twentyoneAvg, twentytwoAvg, twentythreeAvg, twentyfourAvg
        

if __name__ == '__main__':
    Main()
