import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

dataset = 'canada.xlsx'
df = pd.read_excel(dataset, header=20)

df = df.replace('..', 0)

df1 = df

df1.reset_index(inplace=True)
# df1.set_index(["AreaName", "RegName"], inplace=True)

data = df1.iloc[1:11, 4:]
barChartData = data.T
# barChartData.plot(kind='bar', layout=(5,2), subplots=True)

pieChartData = df1.iloc[1:11, 4:]
# pieChartData.plot.pie(subplots=True, figsize=(6,3))
# pieChartData.plot(kind='pie', y = 1990, subplots=True)



df2 = df
# Extract only the total from each continent
df2.set_index("index", inplace=True)
totalRegionPieChart = df2.loc[[6, 12, 17, 21, 22, 27, 28 ],]
df2.reset_index(inplace=True)
df2.set_index(["AreaName", "RegName"], inplace=True)
# totalRegionPieChart = totalRegionPieChart.T
print(totalRegionPieChart)
totalRegionPieChart.plot(kind='pie', y = 1990, subplots=True)
# print(df.index)


plt.show()
