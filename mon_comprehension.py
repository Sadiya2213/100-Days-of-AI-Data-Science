raw_temperature = [32.5, 18.0, 42.1, 15.4, 38.9, 22.3, 45.0]
print("1.Raw lab reading:" , raw_temperature)

high_temps = [temp for temp in raw_temperature if temp>30.0]
print("2. Filtered Critical Hot Zones (>30°C):", high_temps)

high_temps.sort()
print("3.Sorted critical temperature:" ,high_temps)

high_temps.sort(reverse=True)
print("4.Sorted critical temperature:" ,high_temps)
