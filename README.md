# Ethy (Easy) Prophet
---
## Project Description
### Ethereum Price Predictions
+++++++++++++++++\
\
**Overview:**\
Ethereum is a cryptocurrency that has historically been extremely volatile, whether federal governments are writing in new regulations or the latest update to the blockchain has been released, the predictability is fairly difficult. \
**Method**\
A time series analysis (TSA) on 6-weeks of Ethereum price historical data, create a model using Facebook Prophet algorithm. Predicting the price on a 4-hour basis using concurrent data.\
**Conclusion**\
Model was able to provide predictions better than baselines, varying results on selected frame of historical data & train/test split.

## Project Goals
---
- Sufficient exploration to learn more about ethereum price characteristics
- Create a tuned model that will be capable of predicting the price of Ethereum concurrently on a 4-hour basis.

## Initial Thoughts
--- 
Ethereum (cryptocurrencies) have inherintly a lot of volatility due to contraversy. There's constant new regulations and constant new developments that could be factors outside of available data. So coming into this project there is a degree of reluctance that the algorithm will be able to extrapolate accurate predictions. 

## Planning
--- 
1. Acquire data from yfinance (which retrieves from coinmarketcap)
2. Looking at sub-daily data - find best observations to accurately predict on this
    a. remap 'close' as y and datetime as 'ds'
3. Explore and analyze data for better insights for hypertuning model
    a. Determine our baseline prediction
        1. Last Observed value
        2. Simple Average
        3. Moving Average

## Data Dictionary
--- 
| Feature        | Definition                                   |
| ---            | ---                                          |
| open  | the price of currency at the start of the reported time frame |
| close | the price of currency at the end of reported time frame |
| high | the highest price of the reported time frame |
| low   | the lowest price of the reported time frame |
| volume  | a cumulation of trade volume data from the largest volume exchanges |
| month   | month of the year |
| weekday   | a text indicator of what day of the week it is |


## Reproducability Requirements
---
1. Clone repo
RUN OPTIONS:\
    2a. Local machine must have python 3.7 and prophet downloaded\
    2b. Using Google Colab drop wrangle into files
3. Run notebook

## Conclusions 
- Volatility of Ethereum makes it very hard to predict seasonality / trend on a macro scale but with the recent
consistency there's sufficient data to be able to make a fairly close prediction
- The nature of price is that is a quasi-schotastic value that has lots of factors even outside that of which\
can be seen on a time scale. Such as news, improvements and maybe even downtime

## Recommendation
- Utilize other models outside of a time series -- ex. utilizing trade volume, open, high and low for a regression model
- Cross validation to improve model accuracy