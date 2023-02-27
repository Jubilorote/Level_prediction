import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df=pd.read_csv('epa-sea-level.csv')
  

    # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
  result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  slope = result.slope
  intercept = result.intercept 
  x2 = list(range(1880, 2050))
  y2 = []
  for year in x2:
    y2.append(intercept + slope*year)
  plt.plot(x2,y2,'r',label = 'Bests Fit Line 1')
    # Create second line of best fit
  
  last_year=df["Year"].max()
  df_recent = df.loc[(df["Year"] >= 2000) & (df["Year"] <= last_year)]
  res2 = linregress(df_recent["Year"], df_recent['CSIRO Adjusted Sea Level'])
  df_recent = df_recent.append(
    [{"Year": y} for y in range(last_year + 1, 2050)]
    )
  plt.plot(
        df_recent["Year"],
        res2.intercept + res2.slope * df_recent["Year"],
        label="Bests Fit Line 2")
    # Add labels and title
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")
    
  plt.savefig('sea_level_plot.png')
  return plt.gca()
