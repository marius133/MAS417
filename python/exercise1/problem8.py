

MINIMUM_OBSTACLE_DISTANCE_M = 0.200
obstacle_distances_m = [0.312, 0.190, 0.249]
obstacle_distances_m.append(0.200)
obstacle_distances_m.append(0.199)
obstacle_distances_m.append(0.201)

passing_samples = 0
for sample_number, distance_m in enumerate(obstacle_distances_m, start=1):

    if distance_m >= MINIMUM_OBSTACLE_DISTANCE_M:
        result = "PASS"
        passing_samples += 1
    else:
        result = "FAIL"
    print(f"Sample {sample_number}: {distance_m:.3f} m - {result}")


print(f"Number of passing samples: {passing_samples}")
print(f"Smallest sample: {min(obstacle_distances_m)}")
print(f"Largest sample: {max(obstacle_distances_m)}")