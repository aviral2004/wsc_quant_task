# recognise bearish engulfing pattern
def bearish_engulfing(df):
    if df['Close'].iloc[-1] < df['Open'].iloc[-1]:
        if df['Close'].iloc[-2] > df['Open'].iloc[-2]:
            if df['Open'].iloc[-1] > df['Close'].iloc[-2]:
                if df['Close'].iloc[-1] < df['Open'].iloc[-2]:
                    return True
    return False

# recognise bullish engulfing pattern
def bullish_engulfing(df):
    if df['Close'].iloc[-1] > df['Open'].iloc[-1]:
        if df['Close'].iloc[-2] < df['Open'].iloc[-2]:
            if df['Open'].iloc[-1] < df['Close'].iloc[-2]:
                if df['Close'].iloc[-1] > df['Open'].iloc[-2]:
                    return True
    return False

# recognise bearish harami pattern
def bearish_harami(df):
    if df['Close'].iloc[-1] < df['Open'].iloc[-1]:
        if df['Close'].iloc[-2] > df['Open'].iloc[-2]:
            if df['Open'].iloc[-1] < df['Close'].iloc[-2]:
                if df['Close'].iloc[-1] > df['Open'].iloc[-2]:
                    return True
    return False

# recognise bullish harami pattern
def bullish_harami(df):
    if df['Close'].iloc[-1] > df['Open'].iloc[-1]:
        if df['Close'].iloc[-2] < df['Open'].iloc[-2]:
            if df['Open'].iloc[-1] > df['Close'].iloc[-2]:
                if df['Close'].iloc[-1] < df['Open'].iloc[-2]:
                    return True
    return False