import pandas as pd
import pdb

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
print(corr_matrix.head(10))
