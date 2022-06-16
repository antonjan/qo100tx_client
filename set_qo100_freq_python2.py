#!/usr/bin/env python

import time
import random
import xmlrpclib

#create server object
s = xmlrpclib.Server("http://192.168.10.96:8080")

#randomly change parameters of the sinusoid
for i in range(10):
    #generate random values
    freq = s.get_TX_Freq()
    new_freq_up = freq + 1000
    new_freq_down = freq - 1000
    new_ampl = random.uniform(0, 2)
    new_offset = random.uniform(-1, 1)
    #set new values
    time.sleep(1)
    s.set_TX_Freq(new_freq_up)
    time.sleep(1)
#    s.set_ampl(new_ampl)
    time.sleep(1)
#    s.set_offset(new_offset)
    freq = s.get_TX_Freq()
    print(freq)

