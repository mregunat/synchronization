# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:45:50 2018

@author: mregunat
"""
f1=20.1997 # downlink frequency
f2=42 # uplink frequency
a1=2.7 # downlink attenuation

ph2=f2*f2/(1+f2*f2*1e-4)
ph1=f1*f1/(1+f1*f1*1e-4)
H=1.12e-3*((ph2/ph1)**0.5)*((ph1*a1)**0.55)
g=1-H
a2=a1*(ph2/ph1)**g # uplink attenuation
print(a2)
