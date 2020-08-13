#!/usr/bin/env python3

# Make sure IEX_TOKEN is exported
import os.path
import pyEX as p
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from os import path
from datetime import datetime

if not path.exists("amd-1y.csv"):
  print("fetching fresh data")
  ticker = 'AMD'
  timeframe = '1y'
  c = p.Client()
  df = c.chartDF(ticker, timeframe)
  df = df[['close']]
  df.reset_index(level=0, inplace=True)
  df.columns=['ds','y']

if path.exists("amd-1y.csv"):
  print("using csv")
  df = pd.read_csv("amd-1y.csv")

sma_20 = df.y.rolling(window=20).mean()
sma_50 = df.y.rolling(window=50).mean()
sma_200 = df.y.rolling(window=200).mean()
plt.plot(df.ds, df.y, label='AMD')
plt.plot(df.ds, sma_20, label='AMD 20 Day SMA', color='orange')
plt.plot(df.ds, sma_50, label='AMD 50 Day SMA', color='magenta')
plt.plot(df.ds, sma_200, label='AMD 200 Day SMA', color='blue')
plt.legend(loc='upper left')
plt.show()

if not path.exists("amd-1y.csv"):
  df.to_csv("amd-1y.csv")
