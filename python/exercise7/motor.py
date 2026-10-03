from python.exercise1.problem7 import maximum_angle


class Motor:
    supply_voltage_v = 24.0

    def __init__(self, name: str, max_speed_rpm: float):
        self.name = name
        self.max_speed_rpm = max_speed_rpm
        self._speed_rpm = 0.0

    def set_speed(self, speed_rpm: float) -> None:
        if not 0.0 <= speed_rpm <= self.max_speed_rpm:
            raise ValueError(f"speed must be between 0 and {self.max_speed_rpm} rpm")
        self._speed_rpm = speed_rpm

    def speed(self) -> float:
        return self._speed_rpm

    def __str__(self) -> str:
        return f"{self.name}: {self._speed_rpm:.0f} of {self.max_speed_rpm:.0f} rpm"


class ServoMotor(Motor):
    def __init__(self, name: str, max_speed_rpm: float, min_angle_deg, max_angle_deg):
        super().__init__(name, max_speed_rpm)
        self.min_angle_deg = min_angle_deg
        self.max_angle_deg = max_angle_deg
        self.angle_deg = 0.0

    def move_to(self,angle_deg):

        if not self.min_angle_deg <= angle_deg <= self.max_angle_deg:
            raise ValueError
        self.angle_deg = angle_deg

    def __str__(self) -> str:
        return f" {super().__str__()}, at {self.angle_deg:.0f} deg"

left = Motor("left wheel", 3000)
right = Motor("right wheel", 3000)
left.set_speed(1200)

print(left)
print(right)
print(Motor.supply_voltage_v, left.supply_voltage_v)

try:
    right.set_speed(3500)
except ValueError as error:
    print(f"Rejected: {error}")
print(right)

servo = ServoMotor("Gripper",60,-90,90)
servo.move_to(45)
print(servo)

print(isinstance(servo,Motor))
print(isinstance(left,ServoMotor))