robot_name = input("Robot name: ")
payload_mass_kg = float(input("Payload mass [kg]: "))
joint_angle_radians = float(input("Joint angle [rad]: "))



MILLIMETRES_PER_METRE = 1000.0
obstacle_distance_m = (
    float(input("Obstacle distance [mm]: ")) / MILLIMETRES_PER_METRE
)
operation_text = input("Start operation [yes/no]: ")
operation_requested = operation_text.lower() == "yes"

print(f"{'Robot:':<20} {robot_name}")
print(f"{'Payload:':<20} {payload_mass_kg:.2f} kg")
print(f"{'Joint angle':20} {joint_angle_radians:.3f} rad")
print(f"{'Obstacle distance':<20} {obstacle_distance_m:.3f} m")
print(f"{'Operation requested:':<20} {operation_requested}")