#write speed calc decorator function
import time

def speed_calculator(function):
    def wrapper_function():
        time_a = time.time()
        function()
        time_b = time.time()
        time_taken = time_b - time_a
        print(time_taken)
    return wrapper_function


@speed_calculator
def slow_func():
    for i in range(100000000):
        i * i


def fast_func():
    for i in range(10):
        i * i



slow_func()
