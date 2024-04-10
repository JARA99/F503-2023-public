import pandas as pd
import datetime as dt

# parser = lambda date: dt.datetime.strptime(date,'%Y-%m-%d')

data = pd.read_csv('data.csv',parse_dates=[1],date_format='%Y-%m-%d',header=None)
data.columns = ['index','date','simptoms','test','positive']
start_date = dt.datetime(2020,2,14)

print(data)

data['julian'] = (data['date'] - start_date).dt.days
data['julian_dt'] = (data['date'] - start_date)
print(data)

print(data['date'][0],type(data['date'][0]))
print(data['julian'][0],type(data['julian'][0]))

data[['date','julian','simptoms','test','positive']].to_csv('data.dat',sep='\t',index=False)



