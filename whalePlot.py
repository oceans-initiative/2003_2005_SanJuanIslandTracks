#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:41:24 2020

@author: val
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import WhaleBoatObj

mc = mcolors.TABLEAU_COLORS  # color palette for potting
  
def plotPassby(whale, boats, delta):
  plt.rcParams["figure.figsize"] = [16,16]
  theDate = WhaleBoatObj.getDateFromJulian(whale.jDay[0])
  plotTitle = "%d_%d_%d_%d_%d_%d -" % (theDate)
  plotTitle += " passby number %d" % whale.trackID
  plt.title(plotTitle)
  ax = plt.axes()
  ## list(mc) ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown','tab:pink','tab:gray', 'tab:olive', 'tab:cyan']
  xMean = np.mean(whale.xMod)
  yMean = np.mean(whale.yMod)
  if xMean > 600000:
    print(plotTitle)
    print(xMean,whale.xMod)
    input("in whalePlot with large mean")
    return
  nHalf = len(whale.xMod)//2
#  print(len(whale.xMod), nHalf)
#  print("in plotPassby: N of whale points", len(whale.xMod), "x mean", int(xMean), "y mean", int(yMean), "speed at center",whale.vMod[nHalf])
  plt.xlim(xMean-delta,xMean+delta)
  plt.ylim(yMean-delta,yMean+delta)

  dx = whale.xMod[nHalf + 1] - whale.xMod[nHalf]
  dy = whale.yMod[nHalf + 1] - whale.yMod[nHalf]
  plt.text(whale.xMod[nHalf], whale.yMod[nHalf], whale.whaleID)
  
  plt.plot(whale.xMod, whale.yMod, color = 'black')   # plot whale track

  plt.scatter(whale.utmE, whale.utmN, s=100, c='black')
  
#  if DEBUG == 1:
#    print("OBS ARE", whale.xObs,"y obs",whale.yObs)
#    print(whale.x[nHalf], dx, whale.y[nHalf], dy, whale.x[nHalf] + whale.v[nHalf]*dx, whale.y[nHalf] + whale.v[nHalf]*dy)

  ax.arrow(whale.xMod[nHalf], whale.yMod[nHalf],  10*dx, 10*dy, linewidth = 3, head_width=10, head_length=10)  # plot whale velocity vector at midpath point
  clr = 1
  for b in boats:
    i = 0
    thisClr = mc[list(mc)[clr]]
    clr = clr + 1
    if clr == len(list(mc)):
      clr = 0
    while i < len(b.xMod):   ## plot synchronous lines from boats to whale 
      plt.plot([b.xMod[i],whale.xMod[i]],[b.yMod[i],whale.yMod[i]], linewidth = 0.5, color = thisClr)
      plt.scatter(b.utmE, b.utmN, s=100, c=thisClr)
      if b.xMod[0] == b.xMod[-1]:
        plt.text(b.xMod[0],b.yMod[0],b.boatID, color = thisClr)  # this is a stationary boat
      else:
        dx = b.xMod[nHalf + 1] - b.xMod[nHalf]
        dy = b.yMod[nHalf + 1] - b.yMod[nHalf]
        ax.arrow(b.xMod[nHalf],b.yMod[nHalf], 10*dx, 10*dy, linewidth = 2, head_width=10, head_length=10)
      i = i+10
    plt.plot(b.xMod,b.yMod, color = thisClr)
  plotDirectory = "analysisResults"
  filename = "%s/passby%s_%d_%s.png" % (plotDirectory, whale.trackID, delta, whale.whaleID)
  plt.savefig(filename)
  plt.show(block=False)  # force plot to write out  