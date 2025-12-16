import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # -------- First line of best fit (all data) --------
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred)

    # -------- Second line of best fit (from year 2000) --------
    df_2000 = df[df["Year"] >= 2000]

    res_2000 = linregress(
        df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"]
    )

    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000)

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot
    plt.savefig("sea_level_plot.png")

    return plt.gca()
