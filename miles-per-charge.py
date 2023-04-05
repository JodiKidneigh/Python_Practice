charge_range = 21.71
kWh = 7.235
miles_per_kWh = kWh /charge_range 
cost_per_kWh = 189.90/1170

cost_per_mile = cost_per_kWh * miles_per_kWh

cost_per_full_charge = cost_per_mile * 95

print(f"miles per kWh: {miles_per_kWh}")
print(f"cost per kWh: {cost_per_kWh}")
print(f"cost per ev mile: {cost_per_mile}")
print(f"cost per full charge: {cost_per_full_charge}")

mpg = 33
tank_gallons = 11
tank_range = mpg * tank_gallons
cost_per_gallon = 2.99
cost_per_full_tank = cost_per_gallon * tank_gallons
cost_per_gas_mile = cost_per_gallon / tank_range

print(f"tank range: {tank_range}")
print(f"cost per gallon: {cost_per_gallon}")
print(f"cost per gas mile: {cost_per_gas_mile}")
print(f"cost per full tank: {cost_per_full_tank}")

print(363 / 95)
print(3.82 * 5.1386)