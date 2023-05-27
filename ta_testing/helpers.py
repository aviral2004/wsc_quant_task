import numpy as np
import yfinance as yf
from tqdm import tqdm
from ta_funcs import *
import pickle as pkl

# checking accuracy for any pattern for any window size
def check(df, window, bearish, func, verbose=False): # bearish = True for bearish, False for bullish
    lst = []
    if bearish:
        for i in range(2, len(df) - window):
            if func(df.iloc[i-2:i+1]):
                if df.iloc[i+window]['Close'] < df.iloc[i]['Close']:
                    if verbose:
                        print("Bearish engulfing day: ", df.index[i], " is actually bearish")
                    lst.append(1)
                lst.append(0)
    else:
        for i in range(2, len(df) - window):
            if func(df.iloc[i-2:i+1]):
                if df.iloc[i+window]['Close'] > df.iloc[i]['Close']:
                    if verbose:
                        print("Bullish engulfing day: ", df.index[i], " is actually bullish")
                    lst.append(1)
                lst.append(0)

    return np.mean(lst) if len(lst) != 0 else 1


# downloading data for any number of stocks
def get_data(stocks, start="2022-01-01", end="2023-04-30", interval="1d"):
    filename = f"data/{start}_{end}_{interval}.pkl"

    # if data already exists, load it, else download it
    try:
        with open(filename, "rb") as f:
            stock_data = pkl.load(f)
        
        print("Data loaded from file")
    except:
        stock_data = {}
        print("Downloading data")

        for i, stock in tqdm(enumerate(stocks)):
            df = yf.download(stock, start=start, end=end, interval=interval, progress=False)
            stock_data[stock] = df

        with open(filename, "wb") as f:
            pkl.dump(stock_data, f)

    return stock_data

# checking accuracy for any pattern for any window size for any number of stocks
def get_accuracies(stock_data):
    data = {}
    for func in [bullish_engulfing, bearish_engulfing, bullish_harami, bearish_harami]:
        print(f"Function: {func.__name__}")

        curr_data = {}
        for stock in tqdm(stock_data.keys()):
            accuracies = []
            df = stock_data[stock]
            for window in range(1, 11):
                accuracy = check(df, window, False, func)
                accuracies.append(accuracy)

            curr_data[stock] = accuracies
                
        data[func.__name__] = curr_data

    return data