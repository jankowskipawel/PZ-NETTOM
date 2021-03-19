import urllib.request
import statistics

url = "http://192.168.0.26/index.php"
number_of_tests = 5
times = []

for x in range(number_of_tests):
    print(f"Try {x} of {number_of_tests}")
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    str = mybytes.decode("utf8")
    fp.close()
    str_arr = str.split("<br>")

    script_execution_time_str = str_arr[-3][33:47]
    minutes_str = script_execution_time_str[0:2]
    seconds_str = script_execution_time_str[4:6]
    microseconds_str = script_execution_time_str[8:]

    seconds = float(seconds_str+"."+microseconds_str)
    for x in range(int(minutes_str)):
        seconds+=60
    times.append(seconds)


print(f"Testing succeded.")
print(f"Number of tests: {number_of_tests}")
print(f"Average time: {statistics.mean(times)}")
print(f"Minimum: {min(times)}")
print(f"Maximum: {max(times)}")
print(f"Variance: {statistics.variance(times)}")
print(f"Standard deviation: {statistics.stdev(times)}")
print(f"Median: {statistics.median(times)}")