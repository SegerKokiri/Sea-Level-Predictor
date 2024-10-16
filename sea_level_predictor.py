import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df.head())

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)


    # Create first line of best fit
    slope, intercept, r_value, p_value, str_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_full = pd.Series(range(df['Year'].min(), 2051))
    y_fit = slope * x_full + intercept
    
    predicted_sea_level_2050 = slope * 2050 + intercept
    
    plt.plot(x_full, y_fit, color='blue')
    
    plt.scatter(2050, predicted_sea_level_2050)

    # Create second line of best fit
    df_filter = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, str_err2 = linregress(df_filter['Year'], df_filter['CSIRO Adjusted Sea Level'])
    x_fit_full2 = pd.Series(range(2000, 2051))
    y_fit_2 = slope2 * x_fit_full2 + intercept2
    predicted_sea_level_20502 = slope2 * 2050 + intercept2
    
    plt.plot(x_fit_full2, y_fit_2, color='red')
    
    plt.scatter(2050, predicted_sea_level_20502)
    

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    #plt.show()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


# draw_plot()