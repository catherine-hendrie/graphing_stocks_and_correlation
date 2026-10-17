import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Downloading the Data from Yahoo Finance for AMD and INTC
amd = "AMD"
intc = "INTC"
amd_data = yf.download(amd, start="2022-11-01", end="2026-10-16", group_by='ticker')[amd]["Close"] #Data is from Start of November 2022 up untill recently.
intc_data = yf.download(intc, start="2022-11-01", end="2026-10-16", group_by='ticker')[intc]["Close"]






#Creating the Graphs - AMD - Creates graph of stock price for AMD for past 4 ish years since the month before ChatGPT released
plt.figure(figsize=(10,5))
plt.plot(
   amd_data.index,       # Closing price for AMD
   amd_data,
   label="AMD Stock Price",     # Labeling
   color='red', 
   linewidth=2,         
)


#Creating the Graphs - INTC - Creates graph of stock price for AMD for past 4 ish years since the month before ChatGPT released
plt.plot(
   intc_data.index,       # Closing price for INTC
   intc_data,
   label="INTC Stock Price",     # Labeling
   color='blue', 
   linewidth=2,         
)
