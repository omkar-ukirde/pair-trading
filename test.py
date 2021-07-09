import pandas as pd
import pdb

watchlist = ['ACC','ALKEM','ASIANPAINT','BAJAJ-AUTO','BRITANNIA','CIPLA','COALINDIA','COLPAL','DABUR','DRREDDY','HCLTECH','HDFCBANK','HDFCLIFE','HEROMOTOCO','HINDUNILVR','ITC','IOC','INFY','KOTAKBANK','LT','MARICO','NTPC','NESTLEIND','PIDILITIND','POWERGRID','RELIANCE','TCS','TECHM','ULTRACEMCO','WIPRO']
data = pd.DataFrame()
names = list()

for name in watchlist:
   df15 = pd.read_csv("C:\\Users\\omkin\\Downloads\\Algo Trading\\Session 7\\mywork5\\15mins\\"+name+".csv", parse_dates=['date'], index_col='date')
   df15 = df15.rename(columns={'close':name})
   data = pd.concat([data, df15[name]],axis = 1)
   names.append(name)
   data.columns = names

corr_matrix = data.corr()
corr_matrix.to_csv('heatmap.csv')   
pdb.set_trace()