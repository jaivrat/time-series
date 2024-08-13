import numpy as np
from statsmodels.tsa.stattools import adfuller
import plotly.express as px

def plotting(title, data, x, y, x_label, y_label):
    """General function to plot the passenger data."""
    fig = px.line(data, x=data[x], y=data[y], labels={x: x_label, y: y_label})

    fig.update_layout(template="simple_white", font=dict(size=18),
                      title_text=title, width=650,
                      title_x=0.5, height=400)

    fig.show()


def test_adf(sequence):
    res = adfuller(sequence)
    print('Statistic: ', res[0])
    print('p-value: ', res[1])
    print('critical values:')
    for threshold, statistic in res[4].items():
        print('\t%s: %.2f' % (threshold, statistic))

