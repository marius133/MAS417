MINIMUM_JOINT_ANGLE_RADIANS = -1.5
MAXIMUM_JOINT_ANGLE_RADIANS = 1.5
MINIMUM_OBSTACLE_DISTANCE_M = 0.200  # Requirement: 200 mm.
INVALID_OBSTACLE_DISTANCE_M = -0.001  # Interface sentinel: -1 mm.
MAXIMUM_MOTOR_TEMPERATURE_DEGREES_CELSIUS = 70.0


def check_sample(
    joint_angle_radians,
    obstacle_distance_m,
    motor_temperature_degrees_celsius,
):
    warnings = []

    # Add one specific warning for each invalid reading or failed limit.

    return warnings


def main():
    robot_name = input("Enter robot name: ")
    number_of_test_samples = int(input("Enter number of test samples: "))
    for i in range(number_of_test_samples):
        print(f"Sample {i+1}")
        joint_angle_radians = float(input("Insert joint angle [rad]: "))
        obstacle_distance_mm = float(input("Insert obstacle distance [mm]: "))
        motor_temperature = float(input("Insert motor_temperature [deg C]: "))



warnings = check_sample(0.0,0.350,45.0)
print(warnings)

if __name__ == "__main__":
    main()