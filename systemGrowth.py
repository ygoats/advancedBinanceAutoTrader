#@ygoats

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
            print("Invalid Literal for Int() With Base 10:", ValueError)
  
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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

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
            print("Invalid Literal for Int() With Base 10:", ValueError)

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentyFive():
    
    f = open("alphaData.txt", 'r')
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
            print("Invalid Literal for Int() With Base 10:", ValueError)

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow


def systemTwentySix():
    
    f = open("deltaLong.txt", 'r')
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
            print("Invalid Literal for Int() With Base 10:", ValueError)

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def systemTwentySeven():
    
    f = open("deltaShort.txt", 'r')
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
            print("Invalid Literal for Int() With Base 10:", ValueError)

    totalNow = []
    totalNow.append(float(total))
    
    return totalNow

def Main():
        
    now = datetime.now()
    t = now.strftime("%H:%M:%S")
    
    print('System Growth Analyzer Connected ' + str(t))
    
    start = True
    dataEntries = 0
    
    while start == True:
        
        now = datetime.now()
        t = now.strftime("%M:%S")
        #print(str(t))
        
        try:
            f = open('aGain.txt', 'r')
            dataEntries = len(f.readlines())
            #print("Data Entries = " + str(dataEntries))
            f.close() 
        except FileNotFoundError as e:
            print(str(e))
        
        if t >= ("00:00") and t <="00:15" and dataEntries < 8:
            
            f = open('aGain.txt', 'a')
            f.write("\n" +  str(systemOne()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F] ' + str("{:.2f}".format(systemOne()[0]))])
            sleep(5)

            f = open('bGain.txt', 'a')
            f.write("\n" + str(systemTwo()[0]))
            f.close()   
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F] ' + str("{:.2f}".format(systemTwo()[0]))])
            sleep(5)            

            f = open('cGain.txt', 'a')
            f.write("\n" + str(systemThree()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F] ' + str("{:.2f}".format(systemThree()[0]))])
            sleep(5)
            
            f = open('dGain.txt', 'a')
            f.write("\n" + str(systemFour()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F] ' + str("{:.2f}".format(systemFour()[0]))])
            sleep(5)
            
            f = open('eGain.txt', 'a')
            f.write("\n" + str(systemFive()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][OI] ' + str("{:.2f}".format(systemFive()[0]))])
            sleep(5)
            
            f = open('fGain.txt', 'a')
            f.write("\n" + str(systemSix()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][OI] ' + str("{:.2f}".format(systemSix()[0]))])
            sleep(5)
            
            f = open('gGain.txt', 'a')
            f.write("\n" + str(systemSeven()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][OI] ' + str("{:.2f}".format(systemSeven()[0]))])
            sleep(5)
            
            f = open('hGain.txt', 'a')
            f.write("\n" + str(systemEight()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][OI] ' + str("{:.2f}".format(systemEight()[0]))])
            sleep(5)
            
            f = open('iGain.txt', 'a')
            f.write("\n" + str(systemNine()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][4:1] ' + str("{:.2f}".format(systemNine()[0]))])
            sleep(5)
            
            f = open('jGain.txt', 'a')
            f.write("\n" + str(systemTen()[0]))
            f.close()            
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][4:1] ' + str("{:.2f}".format(systemTen()[0]))])
            sleep(5)
            
            f = open('kGain.txt', 'a')
            f.write("\n" + str(systemEleven()[0]))
            f.close()   
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][4:1] ' + str("{:.2f}".format(systemEleven()[0]))])
            sleep(5)
            
            f = open('lGain.txt', 'a')
            f.write("\n" + str(systemTwelve()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][4:1] ' + str("{:.2f}".format(systemTwelve()[0]))])
            sleep(10)
            
            f = open('mGain.txt', 'a')
            f.write("\n" + str(systemThirteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][10:1] ' + str("{:.2f}".format(systemThirteen()[0]))])
            sleep(10)
            
            f = open('nGain.txt', 'a')
            f.write("\n" + str(systemFourteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][10:1] ' + str("{:.2f}".format(systemFourteen()[0]))])
            sleep(10)
            
            f = open('oGain.txt', 'a')
            f.write("\n" + str(systemFifteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][10:1] ' + str("{:.2f}".format(systemFifteen()[0]))])
            sleep(10)
            
            f = open('pGain.txt', 'a')
            f.write("\n" + str(systemSixteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][10:1] ' + str("{:.2f}".format(systemSixteen()[0]))])
            sleep(10)
            
            f = open('qGain.txt', 'a')
            f.write("\n" + str(systemSeventeen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][ATR62] ' + str("{:.2f}".format(systemSeventeen()[0]))])
            sleep(10)
            
            f = open('rGain.txt', 'a')
            f.write("\n" + str(systemEighteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][ATR62] ' + str("{:.2f}".format(systemEighteen()[0]))])
            sleep(10)
            
            f = open('sGain.txt', 'a')
            f.write("\n" + str(systemNineteen()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][ATR62] ' + str("{:.2f}".format(systemNineteen()[0]))])
            sleep(10)
            
            f = open('tGain.txt', 'a')
            f.write("\n" + str(systemTwenty()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][ATR62] ' + str("{:.2f}".format(systemTwenty()[0]))])
            sleep(10)
            
            f = open('uGain.txt', 'a')
            f.write("\n" + str(systemTwentyOne()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyOne()[0]))])
            sleep(10)
            
            f = open('vGain.txt', 'a')
            f.write("\n" + str(systemTwentyTwo()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyTwo()[0]))])
            sleep(10)
            
            f = open('wGain.txt', 'a')
            f.write("\n" + str(systemTwentyThree()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyThree()[0]))])
            sleep(10)
            
            f = open('xGain.txt', 'a')
            f.write("\n" + str(systemTwentyFour()[0]))
            f.close()
            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyFour()[0]))])
            sleep(10)
            
            ####ADD here the pnl that is the highest AVG to post like the alphaReturn to use for matching system#########
            listCheck = []
            listCheck.append(systemOne()[0])
            listCheck.append(systemTwo()[0])
            listCheck.append(systemThree()[0])
            listCheck.append(systemFour()[0])
            listCheck.append(systemFive()[0])
            listCheck.append(systemSix()[0])
            listCheck.append(systemSeven()[0])
            listCheck.append(systemEight()[0])
            listCheck.append(systemNine()[0])
            listCheck.append(systemTen()[0])
            listCheck.append(systemEleven()[0])
            listCheck.append(systemTwelve()[0])
            listCheck.append(systemThirteen()[0])
            listCheck.append(systemFourteen()[0])
            listCheck.append(systemFifteen()[0])
            listCheck.append(systemSixteen()[0])
            listCheck.append(systemSeventeen()[0])
            listCheck.append(systemEighteen()[0])
            listCheck.append(systemNineteen()[0])
            listCheck.append(systemTwenty()[0])
            listCheck.append(systemTwentyOne()[0])
            listCheck.append(systemTwentyTwo()[0])
            listCheck.append(systemTwentyThree()[0])
            listCheck.append(systemTwentyFour()[0])
            
            maxSys = max(listCheck)
            indexMaxSys = listCheck.index(maxSys)
            
            
            
            listCheck = []
            maxSys = 0
            indexMaxSys = 0
            
            f = open('yGain.txt', 'a')
            f.write("\n" + str(systemTwentyFour()[0]))
            f.close()
            
            delta = 0
            delta = float(systemTwentySix[0]) / float(systemTwentySeven[0])
            
            telegram_send.send(conf='user3.conf', messages=['Current Running System: ' + str(indexMaxSys) + ' Current PNL: ' + str(maxSys) + "/n" + \
                                                            'alphaTrader System Return ' + str("{:.2f}".format(systemTwentyFive()[0])) + "/n" + \
                                                            'Delta Long/Short Ratio ' + str(delta)])
            
            sleep(10)
              
        sleep(5)
                  
        if dataEntries >= 8:
            startProcess = True
            while startProcess == True:
                
                try:
                    now = datetime.now()
                    t = now.strftime("%M:%S")
                    #print(str(t))
                    
                    if t >= ("00:00") and t <="00:15":
                        print('Checking the Gains')
                    
                        #print('Processessing A Gains')
                        
                        f = open('aGain.txt', 'a')
                        f.write("\n" +  str(systemOne()[0]))
                        f.close()
                
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
                        
                        #if systemOne()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F] ' + str("{:.2f}".format(systemOne()[0])) + "\n" + \
                                                                        #'6H MA PNL Trajectory: ' + str("{:.2f}".format(oneAvg))])
                            #sleep(5)
                        
                        #print('Processessing B Gains')
                        
                        f = open('bGain.txt', 'a')
                        f.write("\n" +  str(systemTwo()[0]))
                        f.close()
                
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
                        
                        #if systemTwo()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F] ' + str("{:.2f}".format(systemTwo()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twoAvg))])
                            #sleep(5)                    
     
                        #print('Processessing C Gains')
                        
                        f = open('cGain.txt', 'a')
                        f.write("\n" +  str(systemThree()[0]))
                        f.close()
                
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
                        
                        #if systemThree()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F] ' + str("{:.2f}".format(systemThree()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(threeAvg))])
                            #sleep(5)
                       
                        #print('Processessing E Gains')
                        
                        f = open('dGain.txt', 'a')
                        f.write("\n" +  str(systemFour()[0]))
                        f.close()
                
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
                        
                        #if systemFour()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F] ' + str("{:.2f}".format(systemFour()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(fourAvg))])
                            #sleep(5) 
                        
                        #print('Processessing E Gains')
                        
                        f = open('eGain.txt', 'a')
                        f.write("\n" +  str(systemFive()[0]))
                        f.close()
                
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
                        
                        #if systemFive()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][OI] ' + str("{:.2f}".format(systemFive()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(fiveAvg))])
                            #sleep(5) 
                        
                        #print('Processessing F Gains')
                        
                        f = open('fGain.txt', 'a')
                        f.write("\n" +  str(systemSix()[0]))
                        f.close()
                
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
                        
                        #if systemSix()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][OI] ' + str("{:.2f}".format(systemSix()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(sixAvg))])
                            #sleep(5) 
                        
                        #print('Processessing G Gains')
                        
                        f = open('gGain.txt', 'a')
                        f.write("\n" +  str(systemSeven()[0]))
                        f.close()
                
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
                        
                        #if systemSeven()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][OI] ' + str("{:.2f}".format(systemSeven()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(sevenAvg))])
                            #sleep(5) 
                        
                        #print('Processessing H Gains')
                        
                        f = open('hGain.txt', 'a')
                        f.write("\n" +  str(systemEight()[0]))
                        f.close()
                
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
                        
                        #if systemEight()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][OI] ' + str("{:.2f}".format(systemEight()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(eightAvg))])
                            #sleep(5)
                        
                        #print('Processessing I Gains')
                        
                        f = open('iGain.txt', 'a')
                        f.write("\n" +  str(systemNine()[0]))
                        f.close()
                
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
                        
                        #if systemNine()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][4:1]' + str("{:.2f}".format(systemNine()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(nineAvg))])
                            #sleep(5)
                        
                        #print('Processessing J Gains')
                        
                        f = open('jGain.txt', 'a')
                        f.write("\n" +  str(systemTen()[0]))
                        f.close()
                
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
                        
                        #if systemTen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][4:1] ' + str("{:.2f}".format(systemTen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(tenAvg))])
                            #sleep(5)
                        
                        #print('Processessing K Gains')
                        
                        f = open('kGain.txt', 'a')
                        f.write("\n" +  str(systemEleven()[0]))
                        f.close()
                
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
                        
                        #if systemEleven()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][4:1] ' + str("{:.2f}".format(systemEleven()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(elevenAvg))])
                            #sleep(5)
                        
                        #print('Processessing L Gains')
                        
                        f = open('lGain.txt', 'a')
                        f.write("\n" +  str(systemTwelve()[0]))
                        f.close()
                
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
                        
                        #if systemTwelve()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][4:1] ' + str("{:.2f}".format(systemTwelve()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twelveAvg))])
                            #sleep(5)   
                        
                        #print('Processessing M Gains')
                        
                        f = open('mGain.txt', 'a')
                        f.write("\n" +  str(systemThirteen()[0]))
                        f.close()
                
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
                        
                        #if systemThirteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][10:1] ' + str("{:.2f}".format(systemThirteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(thirteenAvg))])
                            #sleep(5)
    
                        #print('Processessing N Gains')
                        
                        f = open('nGain.txt', 'a')
                        f.write("\n" +  str(systemFourteen()[0]))
                        f.close()
                
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
                        
                        #if systemFourteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][10:1] ' + str("{:.2f}".format(systemFourteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(fourteenAvg))])
                            #sleep(5)
    
                        #print('Processessing O Gains')
                        
                        f = open('oGain.txt', 'a')
                        f.write("\n" +  str(systemFifteen()[0]))
                        f.close()
                
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
                        
                        #if systemFifteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][10:1] ' + str("{:.2f}".format(systemFifteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(fifteenAvg))])
                            #sleep(5)
                        
                        #print('Processessing P Gains')
                        
                        f = open('pGain.txt', 'a')
                        f.write("\n" +  str(systemSixteen()[0]))
                        f.close()
                
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
                        
                        #if systemSixteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][10:1] ' + str("{:.2f}".format(systemSixteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(sixteenAvg))])
                            #sleep(5)                    
                        
                        #print('Processessing Q Gains')
                        
                        f = open('qGain.txt', 'a')
                        f.write("\n" +  str(systemSeventeen()[0]))
                        f.close()
                
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
                        
                        #if systemSeventeen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][ATR62] ' + str("{:.2f}".format(systemSeventeen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(seventeenAvg))])
                            #sleep(5)
    
                        #print('Processessing R Gains')
                        
                        f = open('rGain.txt', 'a')
                        f.write("\n" +  str(systemEighteen()[0]))
                        f.close()
                
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
                        
                        #if systemEighteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][ATR62] ' + str("{:.2f}".format(systemEighteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(eighteenAvg))])
                            #sleep(5)   
                        
                        #print('Processessing S Gains')
                        
                        f = open('sGain.txt', 'a')
                        f.write("\n" +  str(systemNineteen()[0]))
                        f.close()
                
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
                        
                        #if systemNineteen()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][ATR62] ' + str("{:.2f}".format(systemNineteen()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(nineteenAvg))])
                            #sleep(5)
                        
                        #print('Processessing T Gains')
                        
                        f = open('tGain.txt', 'a')
                        f.write("\n" +  str(systemTwenty()[0]))
                        f.close()
                
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
                        
                        #if systemTwenty()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][ATR62] ' + str("{:.2f}".format(systemTwenty()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twentyAvg))])
                            #sleep(5)
                        
                        #print('Processessing U Gains')
                        
                        f = open('uGain.txt', 'a')
                        f.write("\n" +  str(systemTwentyOne()[0]))
                        f.close()
                
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
                        
                        #if systemTwentyOne()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc5M[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyOne()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twentyoneAvg))])
                            #sleep(5)                    
    
                        #print('Processessing V Gains')
                        
                        f = open('vGain.txt', 'a')
                        f.write("\n" +  str(systemTwentyTwo()[0]))
                        f.close()
                
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
                        
                        #if systemTwentyTwo()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc15M[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyTwo()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twentytwoAvg))])
                            #sleep(5)
    
                        #print('Processessing W Gains')
                        
                        f = open('wGain.txt', 'a')
                        f.write("\n" +  str(systemTwentyThree()[0]))
                        f.close()
                
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
                        
                        #if systemTwentyThree()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc1H[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyThree()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twentythreeAvg))])
                            #sleep(5)
    
                        #print('Processessing W Gains')
                        
                        f = open('xGain.txt', 'a')
                        f.write("\n" +  str(systemTwentyFour()[0]))
                        f.close()
                
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
                        
                        #if systemTwentyFour()[0] > 0:
                            #telegram_send.send(conf='user3.conf', messages=['atc4H[M10][F][ATR100] ' + str("{:.2f}".format(systemTwentyFour()[0])) + "\n" + \
                                                                    #'6H MA PNL Trajectory: ' + str("{:.2f}".format(twentyfourAvg))])
                            
                            #sleep(5)

                        #print('Processessing Y Gains')
                        
                        f = open('yGain.txt', 'a')
                        f.write("\n" +  str(systemTwentyFive()[0]))
                        f.close()
                
                        f = open('yGain.txt', 'r')
                        lines = f.readlines()
                        twentyfiveA = float(lines[-1]) - float(lines[-2])
                        twentyfiveB = float(lines[-2]) - float(lines[-3])
                        twentyfiveC = float(lines[-3]) - float(lines[-4])
                        twentyfiveD = float(lines[-4]) - float(lines[-5])
                        twentyfiveE = float(lines[-5]) - float(lines[-6])
                        twentyfiveF = float(lines[-6]) - float(lines[-7])
                        f.close()
                        
                        twentyfiveSum = twentyfiveA + twentyfiveB + twentyfiveC + twentyfiveD + twentyfiveE + twentyfiveF
                        twentyfiveAvg = twentyfiveSum / 6
                        
                        ####ADD here the pnl that is the highest AVG to post like the alphaReturn to use for matching system#########
                        listCheck = []
                        listCheck.append(systemOne()[0])
                        listCheck.append(systemTwo()[0])
                        listCheck.append(systemThree()[0])
                        listCheck.append(systemFour()[0])
                        listCheck.append(systemFive()[0])
                        listCheck.append(systemSix()[0])
                        listCheck.append(systemSeven()[0])
                        listCheck.append(systemEight()[0])
                        listCheck.append(systemNine()[0])
                        listCheck.append(systemTen()[0])
                        listCheck.append(systemEleven()[0])
                        listCheck.append(systemTwelve()[0])
                        listCheck.append(systemThirteen()[0])
                        listCheck.append(systemFourteen()[0])
                        listCheck.append(systemFifteen()[0])
                        listCheck.append(systemSixteen()[0])
                        listCheck.append(systemSeventeen()[0])
                        listCheck.append(systemEighteen()[0])
                        listCheck.append(systemNineteen()[0])
                        listCheck.append(systemTwenty()[0])
                        listCheck.append(systemTwentyOne()[0])
                        listCheck.append(systemTwentyTwo()[0])
                        listCheck.append(systemTwentyThree()[0])
                        listCheck.append(systemTwentyFour()[0])
                        
                        maxSys = max(listCheck)
                        indexMaxSys = listCheck.index(maxSys)
                        
                        listCheck = []
                        maxSys = 0
                        indexMaxSys = 0                        
                        
                        delta = 0
                        delta = float(systemTwentySix[0]) / float(systemTwentySeven[0])
                        
                        telegram_send.send(conf='user3.conf', messages=['Current Running System: ' + str(indexMaxSys) + ' Current PNL: ' + str(maxSys) + "/n" + \
                                                                        'alphaTrader System Return ' + str("{:.2f}".format(systemTwentyFive()[0])) + "/n" + \
                                                                        'Delta Long/Short Ratio ' + str(delta)])

                        sleep(300) 
                        
                        continue
                except Exception as e:
                    print(e)
                    sleep(5)
                    continue
             
if __name__ == '__main__':
    Main()
