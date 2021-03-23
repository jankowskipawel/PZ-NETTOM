import urllib.request
import statistics

# url = "http://192.168.56.103/script1.php"
# number_of_tests = 500
def speed_test_php(url, number_of_tests):
    execution_times = []

    for x in range(number_of_tests):
        print(f"Try {x+1} of {number_of_tests}")
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
        execution_times.append(seconds)
    print(f"Testing succeded.")
    print(f"Number of tests: {number_of_tests}")
    print(f"Average time: {statistics.mean(execution_times)}")
    print(f"Minimum: {min(execution_times)}")
    print(f"Maximum: {max(execution_times)}")
    print(f"Variance: {statistics.variance(execution_times)}")
    print(f"Standard deviation: {statistics.stdev(execution_times)}")
    print(f"Median: {statistics.median(execution_times)}")
    return execution_times
