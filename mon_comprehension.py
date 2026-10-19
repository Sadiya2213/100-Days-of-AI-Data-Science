raw_temperature = [32.5, 18.0, 42.1, 15.4, 38.9, 22.3, 45.0]
print("1.Raw lab reading:" , raw_temperature)

high_temps = [temp for temp in raw_temperature if temp>30.0]
print("2. Filtered Critical Hot Zones (>30°C):", high_temps)

high_temps.sort()
print("3.Sorted critical temperature:" ,high_temps)

high_temps.sort(reverse=True)
print("4.Sorted critical temperature:" ,high_temps)

backup_temperatures = high_temps.copy()
print("5. Safe Data Backup Created:", backup_temperatures)

sensor_two_data = [48.2, 51.0]
combined_report = high_temps + sensor_two_data
print("6. Final Combined Lab Report:", combined_report)