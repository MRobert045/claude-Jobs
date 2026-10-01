import pandas as pd, numpy as np
fx=pd.read_csv('https://raw.githubusercontent.com/datasets/exchange-rates/main/data/daily.csv',parse_dates=['Date']).pivot(index='Date',columns='Country',values='Exchange rate')
m={'Euro':'EUR','United Kingdom':'GBP','Australia':'AUD','New Zealand':'NZD','Japan':'JPY','Switzerland':'CHF','Canada':'CAD'}
fx=fx[list(m)].rename(columns=m).apply(pd.to_numeric,errors='coerce').dropna()
usd=1/fx  # USD value of 1 unit of currency
usd['USD']=1.0
pairs=['EURUSD','GBPUSD','AUDUSD','NZDUSD','USDJPY','USDCHF','USDCAD','EURGBP','EURJPY','GBPJPY','AUDJPY','NZDJPY','CADJPY','CHFJPY','EURCHF','GBPCHF','EURAUD','GBPAUD','AUDNZD','AUDCAD','EURCAD','GBPCAD','EURNZD']
P=pd.DataFrame({p:usd[p[:3]]/usd[p[3:]] for p in pairs})
print(P.tail(1).T.round(4))
def C(start,freq=None):
    x=P[P.index>=start]
    if freq: x=x.resample(freq).last()
    return np.log(x).diff().corr()
res={'1y':C('2025-09-25'),'3m':C('2026-06-25'),'5y':C('2021-09-25','W')}
for k,v in res.items(): v.round(2).to_csv(f'results/corr_{k}.csv')
# gold monthly
g=pd.read_csv('https://raw.githubusercontent.com/datasets/gold-prices/main/data/monthly.csv'); g['Date']=pd.to_datetime(g['Date'])+pd.offsets.MonthEnd(0); g=g.set_index('Date')['Price']
Pm=P.resample('ME').mean(); gm=g[g.index>='2021-08-01']
J=pd.concat([Pm,gm.rename('XAUUSD')],axis=1).dropna()
gc=np.log(J).diff().corr()['XAUUSD'].drop('XAUUSD').sort_values()
gc.round(2).to_csv('results/gold_corr.csv'); print(gc.round(2)); print(len(J),J.index[0],J.index[-1])
for k in ['1y','3m']:
  v=res[k]; s=v.where(np.triu(np.ones(v.shape),1).astype(bool)).stack().sort_values()
  print(k,'MOST NEGATIVE\n',s.dropna().head(12).round(2)); print(k,'MOST POSITIVE\n',s.dropna().tail(20).round(2))
