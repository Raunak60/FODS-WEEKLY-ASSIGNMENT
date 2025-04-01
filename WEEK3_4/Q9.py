# Function to add daily temperatures.

def add_daily_temp(temps, day, temp):
    if day not in temps:
        temps[day] = temp
    return temps

temps = {}
day = input("Enter day: ")
temp = float(input("Enter temperature: "))
temps = add_daily_temp(temps, day, temp)
print("Updated Temperatures:", temps)