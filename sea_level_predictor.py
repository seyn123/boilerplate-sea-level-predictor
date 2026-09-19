import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    intercept = lr.intercept
    slope = lr.slope
    intercept_range = np.linspace(df['Year'].min(), 2050, df.shape[0]+37)
    bestfit = slope * intercept_range + intercept
    ax.plot(intercept_range, bestfit, color="red", label="line of best fit 1")

    # Create second line of best fit
    lr = linregress(df.loc[(df['Year'] >= 2000)]['Year'], df.loc[(df['Year'] >= 2000)]['CSIRO Adjusted Sea Level'])
    intercept = lr.intercept
    slope = lr.slope
    intercept_range = np.linspace(2000, 2050, 51)
    bestfit = slope * intercept_range + intercept
    ax.plot(intercept_range, bestfit, color="orange", label="line of best fit 2")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()