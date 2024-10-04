starting_num = int(input("Starting number: "))
avg_increase = int(input("Average increase: "))
num_days = int(input("Number of days: "))
population = starting_num
print(f"Day \tApproximate Population")
for i in range(num_days):
    print(f"{i+1} \t \t {population:.2f}")
    population += population * (avg_increase /100)


