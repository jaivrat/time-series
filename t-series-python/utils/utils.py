import numpy as np
from statsmodels.tsa.stattools import adfuller
import plotly.express as px
import pandas as pd


def get_data(data_label, **kwargs):
    # Create a datafactory later
    if data_label == "airlines":
        # Raw data from somewhere on internet! Thanks selva86!
        data = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv")
        data  = data.rename(columns = {"value": "passengers"})
        data["month"] = [str(x) for x in pd.to_datetime(data.date).dt.to_period('m')]
        return data
    raise Exception(f"You requested unknown data_label={data_label}")

def plotting(title, data, x, y, x_label, y_label):
    """General function to plot the passenger data."""
    fig = px.line(data, x=data[x], y=data[y], labels={x: x_label, y: y_label})

    fig.update_layout(template="simple_white", font=dict(size=18),
                      title_text=title, width=650,
                      title_x=0.5, height=400)

    fig.show()


#### Augmented Dickey-Fuller (ADF) test
# H0: Series is non-stationary

def test_adf(sequence):
    # H0: Series is non-stationary
    res = adfuller(sequence)
    print('Statistic: ', res[0])
    print('p-value: ', res[1])
    print('critical values:')
    for threshold, statistic in res[4].items():
        print('\t%s: %.2f' % (threshold, statistic))

