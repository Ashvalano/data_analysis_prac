import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('data/btc-eth-prices-outliers.csv', parse_dates=['Timestamp']) # Convert Date column to datetime



# data.plot(x='Timestamp')
# print(data.info())

# plt.show()

# print(data.isnull().sum()) # check for null values

# nan = data[data.isnull()]
# print(nan)


# data.loc['2017-10-21': '2017-12-15'].plot(x='Timestamp', y='Ether') # why wont this work?
# print(data.loc['2017-10-21':'2017-12-15'])

# data.loc[data['Ether'].isnull(), 'Ether']

# find the null values in the Ether column and print them 
# print(data.loc[data['Ether'].isnull(), ['Timestamp', 'Ether']])

# data.loc['2017-12-08':'2017-12-10', 'Ether'].fillna(data['Ether'].mean(), inplace=True)

# data['Ether'].loc['2017-12-08':'2017-12-10'].fillna(data['Ether'].mean(), inplace=True)

# data.loc['2017-12-06': '2017-12-12'].fillna(method='bfill', inplace=True)

# print(data.loc['2017-12-06': '2017-12-12'])

# data.plot(x='Timestamp',y='Ether')


# data.index = pd.to_datetime(data.index)

# data['2018-03-01': '2018-03-09'].plot()


# data.set_index('Timestamp', inplace=True)

# dataCleaned = data.drop(['2017-12-28', '2018-03-04'])
# dataCleaned = data.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))

# dataCleaned.plot(x='Timestamp')

# plt.show()