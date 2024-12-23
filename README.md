# advancedAutoTrader
This is an autotrader that can post signals to a telegram or autotrade them via binance futures. The autotrader will track 24 systems, when returns are generated the autotrader will trade the best performing systems.

pip3 install telegram-send

pip3 install python-binance

SETUP apiData file with your api keys from Binance

Although some of these systems do well in certain market conditions, I do not reccomend anyone try to run the AT version, use at your own risk. Capital loss can and will occur if you plan to run this.

Run pyLoader.py to run everything required to run the system

Run systemClear.py to erase the system PNL trackers

If none of the systems are making money it will eventually auto reset the PNL histories.

unhash alphaTraderV4AT.py in pyLoader.py to run the autoTrader on live Binance Futures --- I DO NOT RECCOMEND THIS

alphaTraderV4TG.py is the script that will post entries, exits, stops, and targets of the signals that the autotrader is trying to trade.

SETTING UP TELEGRAM

Go to @BotFather on telegram and setup an Bot with the easy to follow instructions.

Alternatively please use in the cli

telegram-send --configure

remove the conf = "user1.conf" from the telegram-send() portion of the code
