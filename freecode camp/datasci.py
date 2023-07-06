import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('data/sales_data.csv'
                    , parse_dates=['Date']) # Convert Date column to datetime

# axis = 0 is row, axis = 1 is column
# convert string data types of date to datetime64

# sales['date'] = pd.to_datetime(sales['date'])

# print(sales.dtypes)   
# sales.set_index('Date', inplace=True)
# print(sales.isnull().sum()) # check for null values

# print(sales.columns)
# print(sales.index)

# print(sales.head())
# print(sales.loc['2015-11-26'])


# print(sales.info())

# pandas series
# a = pd.Series([1,2,3,4,5,6,7,8,9,10])

# a[1:-1] = 0


# df = pd.DataFrame({
#     'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
#     'GDP': [
#         1785387,
#         2833687,
#         3874437,
#         2167744,
#         4602367,
#         2950039,
#         17348075
#     ],
#     'Surface Area': [
#         9984670,
#         640679,
#         357114,
#         301336,
#         377930,
#         242495,
#         9525067
#     ],
#     'HDI': [
#         0.913,
#         0.888,
#         0.916,
#         0.873,
#         0.891,
#         0.907,
#         0.915
#     ],
#     'Continent': [
#         'America',
#         'Europe',
#         'Europe',
#         'Europe',
#         'Asia',
#         'Europe',
#         'America'
#     ]
# })



# df.index = [
#     'Canada',
#     'France',
#     'Germany',
#     'Italy',
#     'Japan',
#     'United Kingdom',
#     'United States',
# ]

# print(df.drop(columns=['Population', 'HDI']))






# handling nan values


# df = pd.DataFrame({
#     'Column A': [1, np.nan, 30, np.nan],
#     'Column B': [2, 8, 31, np.nan],
#     'Column C': [np.nan, 9, 32, 100],
#     'Column D': [5, 8, 34, 110],
# })


# print(df.isnull().sum() ) # check for null values
# # print(df.dropna(axis=1, thresh=3))  # drop columns with less than 3 non-NaN values

# # df.fillna(0, inplace=True) # fill NaN values with 0
# df.fillna(df.mean(), inplace=True) # fill NaN values with mean of column
# print(df.round(0)) 








# handling non nan values/ invalid values / duplicates

#invalid values 

# df = pd.DataFrame({
#     'Sex': ['M', 'F', 'F', 'D', '?'],
#     'Age': [29, 30, 24, 290, 250],
# })

# df.loc[df['Age'] > 100, 'Age'] /= 10

# print(df)


# duplicates

# ambassadors = pd.Series([
#     'France',
#     'United Kingdom',
#     'United Kingdom',
#     'Italy',
#     'Germany',
#     'Germany',
#     'Germany',
# ], index=[
#     'Gérard Araud',
#     'Kim Darroch',
#     'Peter Westmacott',
#     'Armando Varricchio',
#     'Peter Wittig',
#     'Peter Ammon',
#     'Klaus Scharioth '
# ])

# keep=false drops all duplicates, keep='last' keeps last duplicate
# print(ambassadors.drop_duplicates(keep='last')) 



# players = pd.DataFrame({
#     'Name': [
#         'Kobe Bryant',
#         'LeBron James',
#         'Kobe Bryant',
#         'Carmelo Anthony',
#         'Kobe Bryant',
#     ],
#     'Pos': [
#         'SG',
#         'SF',
#         'SG',
#         'SF',
#         'SF'
#     ]
# })

# print(players.drop_duplicates(subset=['Name'])) # drop duplicates based on name column



# text handling / splitting and replacing texts



# df = pd.DataFrame({
#     'Data': [
#         '1987_M_US _1',
#         '1990?_M_UK_1',
#         '1992_F_US_2',
#         '1970?_M_   IT_1',
#         '1985_F_I  T_2'
# ]})

# df[['Year', 'Sex', 'Country', 'No Children']] = df['Data'].str.split('_', expand=True)

# df.drop(columns=['Data'], inplace=True)

# df['Year'] = df['Year'].str.replace('?', '')  # replace ? with empty string
# # df['Country'] = df['Country'].str.strip() # remove white spaces
# df['Country'] = df['Country'].str.replace(' ', '') # replace white spaces with empty string

# print(df)




# visualization using matplotlib

# x = np.arange(-10, 11)

# plt.figure(figsize=(12, 6))

# plt.title('My Nice Plot')

# plt.scatter(x, x ** 2)
# plt.scatter(x, -1 * (x ** 2))

# plt.show()




