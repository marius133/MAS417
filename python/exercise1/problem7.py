import math

measured_angle = -3*math.pi
minimum_angle = -2*math.pi
maximum_angle = 2*math.pi
def joint_angle_is_safe(measured_angle,minimum_angle,maximum_angle):
    safe =   maximum_angle >= measured_angle >=  minimum_angle
    return safe

print(joint_angle_is_safe(measured_angle,minimum_angle,maximum_angle))