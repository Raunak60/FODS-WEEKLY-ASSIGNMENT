# Function to get daily temperatures.

def get_daily_temps():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return {day: float(input(f"Enter temperature for {day}: ")) for day in days}

temps = get_daily_temps()
print("Recorded Temperatures:", temps)