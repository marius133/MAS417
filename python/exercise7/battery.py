class Battery:
    def __init__(self,capacity_wh, charge_percent=100.0):
        self.capacity_wh = capacity_wh
        self.charge_percent = charge_percent


    def discharge(self,energy_wh):
        remaining_energy_wh = self.capacity_wh * self.charge_percent/100

        if energy_wh > remaining_energy_wh:
            raise ValueError("Battery does not have enough charge left!")

        used_percent = energy_wh/self.capacity_wh * 100
        self.charge_percent -= used_percent

    def __str__(self) -> str:
        return f"Battery {self.capacity_wh} Wh at {self.charge_percent} %"


battery = Battery(500, 80)
battery2 = Battery(240)
print(battery)
print(battery2)

battery.discharge(100)
try:
    battery2.discharge(300)
except ValueError as error:
    print(f"Rejected: {error}")

print(battery)
print(battery2)
