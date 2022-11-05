new_df = df[['Stock1', 'Stock2']]
new_df['ratios1'] = new_df['Stock1'].diff()
new_df['ratios2'] = new_df['Stock2'].diff()

ratios_df = new_df[['ratios1', 'ratios2']]
#ratios_df += 2
ratios_df = ratios_df.rolling(250).mean()
ratios_df = ratios_df.dropna()
ratios_df.plot()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = ratios_df[['ratios1']].to_numpy()
Y = ratios_df[['ratios2']].to_numpy()
model.fit(X, Y)

model.score(X, Y)
