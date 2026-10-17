import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Downloading the Data from Yahoo Finance for AMD and INTC
ko = "KO"
pep = "PEP"
ko_data = yf.download(ko, start="2000-01-01", end="2026-10-16", group_by='ticker')[ko]["Close"] #Data is from the 2000s onwards
pep_data = yf.download(pep, start="2000-01-01", end="2026-10-16", group_by='ticker')[pep]["Close"]






#Creating the Graphs - Coco Cola - Creates graph of stock price for KO since 2000s
plt.figure(figsize=(10,5))
plt.plot(
   ko_data.index,       # Closing price for KO
   ko_data,
   label="KO Stock Price",     # Labeling
   color='red', 
   linewidth=2,         
)


#Creating the Graphs - Pepsi. Co - Creates graph of stock price for PEP since 2000s
plt.plot(
   pep_data.index,       # Closing price for PEP
   pep_data,
   label="PEP Stock Price",     # Labeling
   color='blue', 
   linewidth=2,         
)


#Adding Correlation
tickers = ("KO", "PEP")
data = yf.download(tickers, start="2000-01-01", end="2026-10-16")["Close"]


#Daily percentage returns
returns = data.pct_change().dropna()




rolling_corr = returns["KO"].rolling(30).corr(returns["PEP"]) #Use rolling correlation instead of 1 number so we can plot it, helps us see if more or less correlated over time.


ax1 = plt.gca() #Retrieving the already made axis'
ax2 = ax1.twinx() #Creates a second axis on the same graph


#Since the two stock prices are already on an axis we use the new axis for the rolling correlation since it is from -1 to +1 instead of in the hundreds
#Drawing correlation line
ax2.plot(
   rolling_corr.index,
   rolling_corr,
   label="30-Day Rolling Correlation",
   color="green",
   linewidth=2,
)


#Formatting


plt.title(f"KO and PEP stocks", fontsize=14)
plt.xlabel("Date", fontsize=11)
plt.ylabel("Stock", fontsize=11)
ax2.set_ylabel("Correlation")
ax2.set_ylim(-1, 1)
plt.grid(True, linestyle="--", alpha=0.6)


#Combining the two legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()


ax1.legend(lines1 + lines2, labels1 + labels2)




#Display the plot
plt.tight_layout()


plt.show()

