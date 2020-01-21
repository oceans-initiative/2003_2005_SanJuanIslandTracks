#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 5:26:24 2020

@author: val
"""
from jdcal import gcal2jd, jd2gcal
import pickle as pickle
import os

##########################################################  helper functions
    
def getDate(jDay):
  jd = (2400000.5, jDay)  #  Note:  This is a tuple, not a list (i.e. ordered and unchangeable)
  dt = jd2gcal(*jd)
  yr = dt[0]
  mo = dt[1]
  day = int(dt[2])
  dayFrac = dt[3]
  hr = int(dayFrac * 24)
  mins = int((dayFrac * 24 - hr)*60)
  sec = int((dayFrac * 24 - hr - mins/60)*3600)
  return (yr,mo,day,hr,mins,sec)    

def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    print("Working directory is ",os.getcwd())
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)  


