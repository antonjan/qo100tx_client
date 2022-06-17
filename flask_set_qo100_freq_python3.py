#!/usr/bin/env python

import time
import random
#import xmlrpclib
import http.client
import xmlrpc.client
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    s = xmlrpc.client.ServerProxy('http://192.168.10.96:8080')
    print(s.get_TX_Freq())
    # Print list of available methods
    #print(s.system.listMethods())

    freq = s.get_TX_Freq()
    print(freq)
    new_freq_up = freq + 1000
    new_freq_down = freq - 1000
    #set new values
    time.sleep(1)
    print(new_freq_up)
    s.set_TX_Freq(new_freq_up)
    time.sleep(1)
    #    s.set_ampl(new_ampl)
    time.sleep(1)
    #    s.set_offset(new_offset)
    freq = s.get_TX_Freq()
    print(freq)
    freqstr = str(freq)
    return freqstr

if __name__ == '__main__':
    app.run()









