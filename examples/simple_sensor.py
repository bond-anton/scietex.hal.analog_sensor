"""Simple Linear Sensor example."""

from scietex.hal.analog_sensor import LinearSensor


if __name__ == "__main__":
    my_sensor = LinearSensor("LinearSensor", gain=2, offset=0)
    VOLTAGE = 3.3
    value = my_sensor.convert_voltage(VOLTAGE)

    print(f"Sensor reading {VOLTAGE} V. Sensor data: {value}.")
