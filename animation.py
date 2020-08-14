#!/usr/bin/env python3

import csv
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from itertools import count
from matplotlib.animation import FuncAnimation


resize_window = False
max_window_width = 200
initial_data_points = 250
huge_int = 999999999999999999999999999999

index = count()

x_arr = []
y_arr = []
sma20_arr = []
sma50_arr = []
sma200_arr = []


def populate_data():
  global x_arr
  global y_arr
  global index
  global sma20_arr
  global sma50_arr
  global sma200_arr

  # TODO: fetch from source & use caching
  df = pd.read_csv("amd-1y.csv")
  sma20_arr = df.y.rolling(window=20).mean().tolist()
  sma50_arr = df.y.rolling(window=50).mean().tolist()
  sma200_arr = df.y.rolling(window=200).mean().tolist()

  y_arr = df["y"].tolist()
  index = count(len(y_arr))
  x_arr = list(range(len(y_arr)))


def check_resize_window(x):
  global resize_window
  global max_window_width

  if not resize_window:
    if x > max_window_width:
      resize_window = True


def animate(i):
  x = next(index)
  x_arr.append(x)

  # TODO: get ticker data here
  y = 85 + random.randint(0, 5) + (10 * np.sin(x/50)) + (5 * np.sin(x/10))

  y_arr.append(y)
  y_df = pd.DataFrame(y_arr, columns=["y"])

  sma20_arr = y_df.y.rolling(window=20).mean().tolist()
  sma50_arr = y_df.y.rolling(window=50).mean().tolist()
  sma200_arr = y_df.y.rolling(window=200).mean().tolist()

  check_resize_window(x)
  if resize_window:
    x_arr.pop(0)
    y_arr.pop(0)
    sma20_arr.pop(0)
    sma50_arr.pop(0)
    sma200_arr.pop(0)
    plt.cla()

  plt.plot(x_arr, y_arr,     "b")
  plt.plot(x_arr, sma20_arr, "c")
  plt.plot(x_arr, sma50_arr, "y")
  plt.plot(x_arr, sma200_arr, "g")

  ax.legend(["Stock", "SMA20", "SMA50", "SMA200"])
  ax.set_xlabel("cnt")
  ax.set_ylabel("$")


populate_data()
fig, ax = plt.subplots()
ani = FuncAnimation(plt.gcf(), animate, huge_int, interval=100)
plt.tight_layout()
plt.show()
