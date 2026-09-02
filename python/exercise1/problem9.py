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

    if (
        joint_angle_radians > MAXIMUM_JOINT_ANGLE_RADIANS
        or joint_angle_radians < MINIMUM_JOINT_ANGLE_RADIANS
    ):
        warnings.append("Joint angle is out of range")

    if obstacle_distance_m == INVALID_OBSTACLE_DISTANCE_M:
        warnings.append("Obstacle distance is invalid")
    elif obstacle_distance_m < MINIMUM_OBSTACLE_DISTANCE_M:
        warnings.append("Obstacle distance is less than minimum")

    if motor_temperature_degrees_celsius > MAXIMUM_MOTOR_TEMPERATURE_DEGREES_CELSIUS:
        warnings.append("Motor temperature is out of range")

    return warnings


def main():
    sample_results = []
    distances_m = []
    motor_temperatures_degrees_celsius = []

    robot_name = input("Enter robot name: ")
    number_of_test_samples = int(input("Enter number of test samples: "))

    while number_of_test_samples < 3:
        print("Must have at least 3 samples.")
        number_of_test_samples = int(input("Enter number of test samples: "))

    for i in range(number_of_test_samples):
        print(f"\nSample {i + 1}")

        joint_angle_radians = float(input("Insert joint angle [rad]: "))
        obstacle_distance_m = float(input("Insert obstacle distance [mm]: ")) / 1000
        motor_temperature_degrees_celsius = float(
            input("Insert motor temperature [deg C]: ")
        )

        warnings = check_sample(
            joint_angle_radians,
            obstacle_distance_m,
            motor_temperature_degrees_celsius,
        )

        distances_m.append(obstacle_distance_m)
        motor_temperatures_degrees_celsius.append(
            motor_temperature_degrees_celsius
        )

        if warnings == []:
            result = "PASS"
        else:
            result = "FAIL"

        sample_results.append(result)

        print(
            f"Sample {i + 1:2}: "
            f"angle={joint_angle_radians:7.3f} rad | "
            f"distance={obstacle_distance_m:6.3f} m | "
            f"motor={motor_temperature_degrees_celsius:6.2f} C | "
            f"{result}"
        )

        for warning in warnings:
            print(f"Warning: {warning}")

    number_of_passed_samples = sample_results.count("PASS")
    number_of_failed_samples = sample_results.count("FAIL")
    smallest_obstacle_distance_m = min(distances_m)
    highest_temperature_degrees_celsius = max(
        motor_temperatures_degrees_celsius
    )

    print("\nCommissioning summary:\n")
    print(f"Robot: {robot_name}")
    print(f"Passed samples: {number_of_passed_samples}")
    print(f"Failed samples: {number_of_failed_samples}")
    print(f"Smallest obstacle distance: {smallest_obstacle_distance_m:.3f} m")
    print(
        f"Highest motor temperature: "
        f"{highest_temperature_degrees_celsius:.2f} C"
    )

    if number_of_failed_samples == 0:
        print("Commissioning status: ACCEPTED")
    else:
        print("Commissioning status: NOT ACCEPTED")


if __name__ == "__main__":
    main()
