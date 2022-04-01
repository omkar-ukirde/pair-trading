import pandas as pd
import pdb
import statsmodels.api as stat
import statsmodels.tsa.stattools as ts
import numpy as np

watchlist = ['HCLTECH','TECHM','SBILIFE','ASIANPAINT','WIPRO','ITC','INFY','TCS','RELIANCE','CIPLA','JSWSTEEL','HEROMOTOCO','NESTLEIND','HINDUNILVR','SHREECEM','BHARTIARTL','HDFCBANK','BRITANNIA','ICICIBANK','HDFCLIFE','TITAN','HINDALCO','BAJAJ-AUTO','DIVISLAB','SUNPHARMA','TATAMOTORS','UPL','TATASTEEL','BAJFINANCE','LT','SBIN','INDUSINDBK','TATACONSUM','COALINDIA','MARUTI','BPCL','ULTRACEMCO','HDFC','ADANIPORTS','DRREDDY','POWERGRID','BAJAJFINSV','AXISBANK','KOTAKBANK','IOC','M&M','ONGC','EICHERMOT','NTPC','GRASIM']

data = pd.DataFrame()
names = list()

for name in watchlist:
   df = pd.read_csv("C:\\Users\\omkin\\OneDrive\\Documents\\Algo Trading\\"+name+".csv", parse_dates=['date'], index_col='date')
   df = df.rename(columns={'close':name})
   data = pd.concat([data, df[name]],axis = 1)
   names.append(name)
   data.columns = names

corr_matrix = data.corr()
corr_matrix = corr_matrix.stack().reset_index().rename(columns={'level_0':'Stock1','level_1':'Stock2', 0:'Correlation'})
corr_matrix = corr_matrix[corr_matrix.Correlation != 1]
corr_matrix = corr_matrix.sort_values(by=['Correlation'], ascending=False)
corr_matrix = corr_matrix.drop_duplicates(subset='Correlation', keep='first')
pairs = corr_matrix[['Stock1','Stock2']].head(10).values.tolist()

def cointegration_test (x,y):
    result = stat.OLS(x['close'], y['close']).fit()
      
    return ts.adfuller(result.resid)

def zscore_cal(data1, data2, start, end):

    s1 = pd.Series(data1['Close'][start:end])
    s2 = pd.Series(data2['Close'][start:end])

    mvavg_old = np.mean(np.log(s1/s2))

    std_old = np.std(np.log(s1/s2))

    current_spread = np.log(
        data1['Close'][end]/data2['Close'][end])

    zscore = (current_spread - mvavg_old) / \
        std_old if std_old > 0 else 0

    return zscore

for index in range(len(pairs)):
    stock1, stock2 = pairs[index]
    df1 = pd.read_csv("C:\\Users\\omkin\\OneDrive\\Documents\\Algo Trading\\"+stock1+".csv")
    df2 = pd.read_csv("C:\\Users\\omkin\\OneDrive\\Documents\\Algo Trading\\"+stock2+".csv")
    res = cointegration_test(df1,df2)
    if res[0] <= res[4]['10%'] and res[1] <= 0.1:
        adftest = "Yes"
    else:
        adftest = "No"
        
