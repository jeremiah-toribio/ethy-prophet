# Ethy (Easy) Prophet
---
## Project Description 
Can the price of Ethereum be predicted? 

## Project Goals
---
- Discover independence of features within data
- Utilizing said features to develop machine learning models that will determine the quality of wine 
- Determine the drivers of quality
- The insights discovered will be used to estimate quality and provide a more robust understanding of the attributes of a the wine and it's associated quality

## Initial Thoughts
--- 
The drivers will likely have an equal weight when determining the quality -- this will be due to the quality likely scored by a professional who is cognizant of their biasis and would like to score on an objective scale. There will still likely be clusters based on data for the wines, since different wines will share qualities. 

## Planning
--- 
1. Acquire data from yfinance (which retrieves from coinmarketcap)
2. Prepare data accordingly for exploration & machine learning needs
    a. Assign date time to index
    b. removing unneeded columns & add helpful columns
    c. snake case columns
    d. remap weekday values
    e. feat engineer high-low diff col
3. Explore data for assocations with quality (correlation tests)
    a. Determine our baseline prediction
    b. Determine which features would be best to cluster
    c. Create new column of clustered data
4. Develop a model to further understand churn
    a. Use various models to determine what algorithm are best for the data
    b. Select best model based on evaluation metrics
    c. Evaluate all models on respective test data
    d. Tune hyperparameters

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
2. Run notebook

## Conclusions 
- Volatility of Ethereum makes it very hard to predict seasonality / trend on a micro scale
- The nature of price is that is a quasi-schotastic value that has lots of factors even outside that of which\
can be seen on a time scale

## Recommendation
- Downsampling to a more granular measure of time to compare results
- Utilize other models outside of a time series -- ex. utilizing trade volume, open, high and low for a regression model