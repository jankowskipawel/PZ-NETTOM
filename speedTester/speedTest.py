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

python_url = "http://192.168.56.102/cgi-enabled/script1.py"
php_url = "http://192.168.56.103/script1.php"
number_of_tests = 200
ram="1GB"
cpus = "1"

parameters = f"{ram}_RAM_{cpus}_CPUs"

python_speeds = speed_test_python(python_url, number_of_tests)
php_speeds = speed_test_php(php_url, number_of_tests)

php_plot = plotGraph(range(len(php_speeds)), php_speeds, f"PHP {parameters}")
python_plot = plotGraph(range(len(python_speeds)), python_speeds, f"PYTHON {parameters}")

pp = PdfPages(f"{parameters}_{number_of_tests}x.pdf")
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = f'Number of tests: {number_of_tests}\n' \
      f'RAM: {ram}\n' \
      f'CPU(s): {cpus}\n\n\n' \
      f'Python:\n\nStandard deviation: {statistics.stdev(python_speeds)}\n' \
      f'Mean: {statistics.mean(python_speeds)}\n' \
      f'Min: {min(python_speeds)}\nMax: {max(python_speeds)}\n\n\n' \
      f'PHP:\n\nStandard deviation: {statistics.stdev(php_speeds)}\n' \
      f'Mean: {statistics.mean(php_speeds)}\n' \
      f'Min: {min(php_speeds)}\nMax: {max(php_speeds)}'
firstPage.text(0.5, 0.25, txt, transform=firstPage.transFigure, size=16, ha='center')
pp.savefig(firstPage)
pp.savefig(php_plot)
pp.savefig(python_plot)
pp.close()

