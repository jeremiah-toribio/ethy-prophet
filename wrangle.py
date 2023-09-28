import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import yfinance as yf

import warnings
warnings.filterwarnings("ignore")

def get_eth():
    '''
    Returns eth data that will be in csv format
    for not overdriving scraping.

    In order to cache data must run in Google Collab terminal
    ' !cp eth.csv "drive/My Drive/" '
    '''
    if os.path.isfile('eth.csv'):
        print('File exists, pulling from system.')
        eth = pd.read_csv('eth.csv')
        return eth
    else:
        print('File does not exist, extracting from Yahoo Finance.')

        eth = yf.Ticker("eth-usd")
        eth = eth.history(period='3mo',interval='1h')
        eth.to_csv('./eth.csv')
        return eth
    
def prepare_eth(eth):
    '''
    Cleans eth data to remove additional columns and organize 
    data to be explored.
    '''
    # irrelevant stock columns
    eth.drop(columns=['Dividends','Stock Splits'])
    # date information in columns
    eth['month'] = eth.index.month
    eth['year'] = eth.index.year
    eth['weekday'] = eth.index.dayofweek
    return eth
