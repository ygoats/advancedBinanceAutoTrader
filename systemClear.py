#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:51:01 2020

@ygoats
"""

def clearGain():
    a = open('aGain.txt', 'w').close()
    b = open('bGain.txt', 'w').close()
    c = open('cGain.txt', 'w').close()
    d = open('dGain.txt', 'w').close()
    e = open('eGain.txt', 'w').close()
    f = open('fGain.txt', 'w').close()
    g = open('gGain.txt', 'w').close()
    h = open('hGain.txt', 'w').close()
    i = open('iGain.txt', 'w').close()
    j = open('jGain.txt', 'w').close()
    k = open('kGain.txt', 'w').close()
    l = open('lGain.txt', 'w').close()
    m = open('mGain.txt', 'w').close()
    n = open('nGain.txt', 'w').close()
    o = open('oGain.txt', 'w').close()
    p = open('pGain.txt', 'w').close()
    q = open('qGain.txt', 'w').close()
    r = open('rGain.txt', 'w').close()
    s = open('sGain.txt', 'w').close()
    t = open('tGain.txt', 'w').close()
    u = open('uGain.txt', 'w').close()
    v = open('vGain.txt', 'w').close()
    w = open('wGain.txt', 'w').close()
    x = open('xGain.txt', 'w').close()
    y = open('yGain.txt', 'w').close()
    z = open('zGain.txt', 'w').close()
    
    a = open('dataSwing5M[M10][F].txt', 'w').close()
    b = open('dataSwing15M[M10][F].txt', 'w').close()
    c = open('dataSwing1H[M10][F].txt', 'w').close()
    d = open('dataSwing4H[M10][F].txt', 'w').close()
    e = open('dataSwing5M[M10][F][OI].txt', 'w').close()
    f = open('dataSwing15M[M10][F][OI].txt', 'w').close()
    g = open('dataSwing1H[M10][F][OI].txt', 'w').close()
    h = open('dataSwing4H[M10][F][OI].txt', 'w').close()
    i = open('dataSwing5M[M10][F][4:1].txt', 'w').close()
    j = open('dataSwing15M[M10][F][4:1].txt', 'w').close()
    k = open('dataSwing1H[M10][F][4:1].txt', 'w').close()
    l = open('dataSwing4H[M10][F][4:1].txt', 'w').close()
    m = open('dataSwing5M[M10][F][10:1].txt', 'w').close()
    n = open('dataSwing15M[M10][F][10:1].txt', 'w').close()
    o = open('dataSwing1H[M10][F][10:1].txt', 'w').close()
    p = open('dataSwing4H[M10][F][10:1].txt', 'w').close()
    q = open('dataSwing5M[M10][F][ATR62].txt', 'w').close()
    r = open('dataSwing15M[M10][F][ATR62].txt', 'w').close()
    s = open('dataSwing1H[M10][F][ATR62].txt', 'w').close()
    t = open('dataSwing4H[M10][F][ATR62].txt', 'w').close()
    u = open('dataSwing5M[M10][F][ATR100].txt', 'w').close()
    v = open('dataSwing15M[M10][F][ATR100].txt', 'w').close()
    w = open('dataSwing1H[M10][F][ATR100].txt', 'w').close()
    x = open('dataSwing4H[M10][F][ATR100].txt', 'w').close()
    y = open('alphaData.txt', 'w').close()
    
    aa = open('logSwing5M[M10][F].txt', 'w').close()
    bb = open('logSwing15M[M10][F].txt', 'w').close()
    cc = open('logSwing1H[M10][F].txt', 'w').close()
    dd = open('logSwing4H[M10][F].txt', 'w').close()
    ee = open('logSwing5M[M10][F][OI].txt', 'w').close()
    ff = open('logSwing15M[M10][F][OI].txt', 'w').close()
    gg = open('logSwing1H[M10][F][OI].txt', 'w').close()
    hh = open('logSwing4H[M10][F][OI].txt', 'w').close()
    ii = open('logSwing5M[M10][F][4:1].txt', 'w').close()
    jj = open('logSwing15M[M10][F][4:1].txt', 'w').close()
    kk = open('logSwing1H[M10][F][4:1].txt', 'w').close()
    ll = open('logSwing4H[M10][F][4:1].txt', 'w').close()
    mm = open('logSwing5M[M10][F][10:1].txt', 'w').close()
    nn = open('logSwing15M[M10][F][10:1].txt', 'w').close()
    oo = open('logSwing1H[M10][F][10:1].txt', 'w').close()
    pp = open('logSwing4H[M10][F][10:1].txt', 'w').close()
    qq = open('logSwing5M[M10][F][ATR62].txt', 'w').close()
    rr = open('logSwing15M[M10][F][ATR62].txt', 'w').close()
    ss = open('logSwing1H[M10][F][ATR62].txt', 'w').close()
    tt = open('logSwing4H[M10][F][ATR62].txt', 'w').close()
    uu = open('logSwing5M[M10][F][ATR100].txt', 'w').close()
    vv = open('logSwing15M[M10][F][ATR100].txt', 'w').close()
    ww = open('logSwing1H[M10][F][ATR100].txt', 'w').close()
    xx = open('logSwing4H[M10][F][ATR100].txt', 'w').close()
    zz = open('alphaLog.txt', 'w').close()
        
def writeGain():
    s = 0 
    for s in range(10):
        pd = open('aGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('bGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()    
        
        pd = open('cGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()  
        
        pd = open('dGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()    
        
        pd = open('eGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
    
        pd = open('fGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('gGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('hGain.txt', 'a')       ####ADDED to run 4HR as Default
        pd.write("\n" + "0")             ####ADDED to run 4HR as Default
        pd.close()                        ####ADDED to run 4HR as Default
        
        #pd = open('dataSwing4H[M10][F][OI].txt', 'a') ####ADDED to run 4HR as Default
        #pd.write("\n" + "40")                         ####ADDED to run 4HR as Default
        #pd.close()                                    ####ADDED to run 4HR as Default
        
        pd = open('iGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('jGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('kGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('lGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('mGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('nGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('oGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('pGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('qGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('rGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('sGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('tGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('uGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('vGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('wGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
        pd = open('xGain.txt', 'a')
        pd.write("\n" + "0")
        pd.close()
        
def Main():
    clearGain()
    writeGain()
        
if __name__ == '__main__':
    Main()
