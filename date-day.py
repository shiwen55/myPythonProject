import datetime

# Ask the user to input a date
date_str = input("Enter a date (YYYY-MM-DD): ")

# Convert the date string to a datetime object
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

# Get the day of the week as an integer (0 = Monday, 1 = Tuesday, etc.)
day_of_week = date_obj.weekday()

# Define a list of weekday names
weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Print the name of the weekday corresponding to the integer
print(f"The day of the week for {date_str} is {weekday_names[day_of_week]}.")