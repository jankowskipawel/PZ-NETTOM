from python import *
from php import *
import statistics
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

php_1_1 = [48.598351, 50.489828, 46.61536, 47.911028, 57.149568]
php_2_1 = [13.155872, 12.860295, 13.098183, 12.380478, 12.200476]
php_4_1 = [12.850316, 12.116081, 11.771937, 12.053196, 11.408492]

php_2_2 = [11.497576, 11.542073, 12.682181, 11.891146, 12.395079]


python_1_1 = [33.628501, 30.226008, 31.679491, 34.802327, 31.519581]
python_2_1 = [34.329012, 34.654868, 33.603926, 34.126776, 33.730298]
python_4_1 = [35.187991, 32.466086, 32.755128, 31.866335, 30.721493]

python_2_2 = [33.325747, 33.281406, 33.069684, 34.100468, 32.428239]


def plot_graph_one(python_data, php_data, d2):
    fig = plt.figure()
    php_mean = statistics.mean(php_data)
    python_mean = statistics.mean(python_data)
    d2_mean = statistics.mean(d2)
    zorder_less = 10
    zorder_more = 11
    if php_mean>python_mean:
        zorder_less=11
        zorder_more=10
    plt.plot(range(len(python_data)), python_data, label="1GB")
    plt.fill_between(range(len(python_data)), python_data, 0, zorder=zorder_less, alpha=0.85)
    plt.plot(range(len(php_data)), php_data, label="2GB")
    plt.plot(range(len(d2)), d2, label="4GB")
    plt.fill_between(range(len(php_data)), php_data, 0, color='orange',  zorder=zorder_more, alpha=0.85)
    plt.fill_between(range(len(php_data)), d2, 0, color='green',  zorder=zorder_more, alpha=0.65)
    plt.ylabel('Time [s]')
    plt.xlabel('Test number')
    plt.title('Python memory difference \n' +
              f"1GB avg = {round(python_mean, 2)}  2GB avg = {round(php_mean, 2)}  4GB avg = {round(d2_mean, 2)}  Diff = {round(((python_mean-php_mean)/php_mean)*100, 1)}%")
    plt.legend().set_zorder(100)
    plt.grid(True)
    plt.show()
    return fig

def plot_graph_CPU(python_data, php_data):
    fig = plt.figure()
    php_mean = statistics.mean(php_data)
    python_mean = statistics.mean(python_data)
    zorder_less = 10
    zorder_more = 11
    if php_mean>python_mean:
        zorder_less=11
        zorder_more=10
    plt.plot(range(len(python_data)), python_data, label="1CPU")
    plt.fill_between(range(len(python_data)), python_data, 0, zorder=zorder_less, alpha=0.85)
    plt.plot(range(len(php_data)), php_data, label="2CPUs")
    plt.fill_between(range(len(php_data)), php_data, 0, color='orange',  zorder=zorder_more, alpha=0.85)
    plt.ylabel('Time [s]')
    plt.xlabel('Test number')
    plt.title('PHP CPU difference \n' +
              f"1CPU avg = {round(python_mean, 2)}  2CPU avg = {round(php_mean, 2)}  Diff = {round(((python_mean-php_mean)/php_mean)*100, 1)}%")
    plt.legend().set_zorder(100)
    plt.grid(True)
    plt.show()
    return fig


plot_graph_CPU(php_2_1, php_2_2)