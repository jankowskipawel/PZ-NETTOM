from python import *
from php import *
import statistics
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


def plotGraph(X, Y, title):
    fig = plt.figure()
    plt.plot(X,Y)
    plt.title(title)
    return fig


def plot_graph_one(python_data, php_data):
    fig = plt.figure()
    php_mean = statistics.mean(php_data)
    python_mean = statistics.mean(python_data)
    plt.plot(range(len(python_data)), python_data, label="Python")
    plt.fill_between(range(len(python_data)), python_data, 0, zorder=10)
    plt.plot(range(len(php_data)), php_data, label="PHP")
    plt.fill_between(range(len(php_data)), php_data, 0, color='orange',  zorder=11)
    plt.ylabel('Time [s]')
    plt.xlabel('Test number')
    plt.title('PHP VS PYTHON \n' +
              f"Python avg = {round(python_mean, 5)}  PHP avg = {round(php_mean, 5)}  Diff = {round((php_mean/python_mean) * 100, 3)}%")
    plt.legend().set_zorder(100)
    plt.grid(True)
    return fig


def plot_graph_two(Y, title):
    fig = plt.figure()
    plt.xlabel("Test number")
    plt.ylabel("Time [s]")
    mean = statistics.mean(Y)
    stdev = statistics.stdev(Y)
    avg_list = [statistics.mean(Y)]*len(Y)
    stdev_list_positive = [mean+stdev]*len(Y)
    stdev_list_negative = [mean-stdev]*len(Y)
    lines = plt.plot(Y, 'ro', avg_list)
    plt.plot(range(len(Y)), stdev_list_positive, linestyle=':', color='steelblue')
    plt.plot(range(len(Y)), stdev_list_negative, linestyle=':', color='steelblue')
    plt.title(f"{title}\n\u03C3 = {round(statistics.stdev(Y), 10)}")
    plt.legend(lines[:2], ['Values', 'Avg'])
    minimum = min(Y)
    maximum = max(Y)
    plt.ylim([mean-1.5*(maximum-minimum), mean+1.5*(maximum-minimum)])
    plt.grid(True)
    return fig


def replace_odd_values(data):
    mean = statistics.mean(data)
    result = [x if x < (mean*1.75) else mean for x in data]
    return result


python_url = "http://192.168.56.102/cgi-enabled/script1.py"
php_url = "http://192.168.56.103/script1.php"
number_of_tests = 500
ram = "1GB"
cpus = "1"
script_description = "Calculate average value of new covid cases for each country"

parameters = f"{ram}_RAM_{cpus}_CPUs"

python_speeds = replace_odd_values(speed_test_python(python_url, number_of_tests))
php_speeds = replace_odd_values(speed_test_php(php_url, number_of_tests))

php_plot = plot_graph_two(php_speeds, f"PHP {parameters}")
python_plot = plot_graph_two(python_speeds, f"PYTHON {parameters}")
both_plot = plot_graph_one(python_speeds, php_speeds)

pp = PdfPages(f"{parameters}_{number_of_tests}x.pdf")
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = f'Script description: {script_description}\n\n' \
      f'Number of tests: {number_of_tests}\n' \
      f'RAM: {ram}\n' \
      f'CPU(s): {cpus}\n\n\n' \
      f'Python:\n\nStandard deviation: {statistics.stdev(python_speeds)}\n' \
      f'Mean: {statistics.mean(python_speeds)}\n' \
      f'Min: {min(python_speeds)}\nMax: {max(python_speeds)}\n' \
      f'Total time: {sum(python_speeds)}s\n\n\n' \
      f'PHP:\n\nStandard deviation: {statistics.stdev(php_speeds)}\n' \
      f'Mean: {statistics.mean(php_speeds)}\n' \
      f'Min: {min(php_speeds)}\nMax: {max(php_speeds)}\n' \
      f'Total time: {sum(php_speeds)}s'
firstPage.text(0.5, 0.2, txt, transform=firstPage.transFigure, size=16, ha='center')
pp.savefig(firstPage)
pp.savefig(php_plot)
pp.savefig(python_plot)
pp.savefig(both_plot)
pp.close()

