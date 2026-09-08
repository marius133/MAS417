import random
import time
def get_secret_number():
    for x in range(10):
        print(random.randint(0, 10))


def func(sensor_name):
    time_value = time.monotonic()
    random_measurement = random.uniform(0, 20)

    return time_value, sensor_name, random_measurement



measurement = func(sensor_name="temperature")
print(measurement)
func(sensor_name="humidity")


