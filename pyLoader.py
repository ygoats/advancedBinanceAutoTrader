#@ygoats

import os
from subprocess import call
from subprocess import Popen
from time import sleep

# subprocess.call(['python', 'exampleScripts.py', somescript_arg1, somescript_val1,...]). 

#########################################################
###########LOAD ALPHATRADER CHANNEL CONTENT##############
#########################################################

Popen(['nohup', 'python3', 'systemClear.py'],
                   stdout=open('alphaSignals1', 'w'),
                   stderr=open('logfile.log', 'a'),
                   start_new_session=True )

##########################################################
##########################################################
##########################################################

Popen(['nohup', 'python3', 'alphaSignals1.py'],
                    stdout=open('alphaSignals1', 'w'),
                    stderr=open('logfile.log', 'a'),
                    start_new_session=True )

Popen(['nohup', 'python3', 'alphaSignals2.py'],
                    stdout=open('alphaSignals2', 'w'),
                    stderr=open('logfile.log', 'a'),
                    start_new_session=True ) 

Popen(['nohup', 'python3', 'alphaSignals3.py'],
                    stdout=open('alphaSignals3', 'w'),
                    stderr=open('logfile.log', 'a'),
                    start_new_session=True )

# =============================================================================
# Popen(['nohup', 'python3', 'alphaTraderV4AT.py'],
#                     #stdout=open('alphaTraderV4AT', 'w'),
#                     #stderr=open('logfile.log', 'a'),
#                     #start_new_session=True )
# =============================================================================

Popen(['nohup', 'python3', 'systemGrowth.py'],
                    stdout=open('systemGrowth', 'w'),
                    stderr=open('logfile.log', 'a'),
                    start_new_session=True )

#=============================================================================

sleep(20)  ###Let premables load before starting the autoTrader/Signaller

#=============================================================================
Popen(['nohup', 'python3', 'alphaTraderV4TG.py'],
                    stdout=open('alphaTraderV4TG', 'w'),
                    stderr=open('logfile.log', 'a'),
                    start_new_session=True )
#=============================================================================

##########################################################
##########################################################
##########################################################


