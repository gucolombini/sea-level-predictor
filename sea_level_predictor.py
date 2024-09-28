import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Gráfico de dispersão do nível do mar de 1880 até 2013
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c='blue')

    # Regressão linear para descobrir a linha de tendência inicial
    reg = linregress(x,y)
    # Range da previsão (2051 pois o número de stop é omitido)
    x_pred = pd.Series([i for i in range(1880,2051)])
    # Fórmula da reta usando coeficiente angular e linear (slope & intersect).
    # (y = mx + n)
    y_pred = reg.slope*x_pred + reg.intercept
    plt.plot(x_pred, y_pred, 'lime')

    # Ditto, mas agora apenas a partir do ano 2000
    reg_2 = linregress(x[x >= 2000],y[x >= 2000])
    x_pred_2 = pd.Series([i for i in range(2000,2051)])
    y_pred_2 = reg_2.slope*x_pred_2 + reg_2.intercept
    plt.plot(x_pred_2, y_pred_2, 'red')

    # Legenda
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()