import time
unix_time = int(input("Enter a unix time: "))

days_since_input = unix_time // (24 * 3600)
hours_since_input = unix_time % (24 * 3600) // 3600
minutes_since_input = (unix_time % 3600) // 60
seconds_since_input = unix_time % 60

print(f"That is {days_since_input} Days \n {hours_since_input} Hours \n {minutes_since_input} Minutes \n {seconds_since_input} Seconds")
print("Since midnight on jan 1st 1970.")
