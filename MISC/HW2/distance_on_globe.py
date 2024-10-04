import math
radius_of_earth = 3958.8
print("Everything must be in degrees!!")
starting_lat = float(input("Enter starting latitude: "))
starting_lon = float(input("Enter starting longitude: "))

ending_lat = float(input("Enter ending latitude: "))
ending_lon = float(input("Enter ending longitude: "))

starting_lat = math.radians(starting_lat)
starting_lon = math.radians(starting_lon)
ending_lat = math.radians(ending_lat)
ending_lon = math.radians(ending_lon)



A = math.sin((ending_lat - starting_lat) / 2) ** 2 + math.cos(starting_lat) * math.cos(ending_lat) * math.sin((ending_lon - starting_lon) / 2) ** 2
d = 2 * radius_of_earth * math.atan2(math.sqrt(A), math.sqrt(1 - A))

print(f"The distance is {d:.2f} miles.")
