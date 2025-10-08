#student name -Ujjawal Mishra
#Roll No-2024UG3021
#Course: CS-2101/CD-2101 -Python Programming Lab
#Experiment No-3 - Task 3: : Import the datetime module. Define a function get_day_of_week that takes a date string in YYYY-MM-DD format. 
# Use datetime.strptime() to convert the date string into a datetime object and then use strftime('%A') to get the day of the week. 
# Test the function with various dates.

from datetime import datetime
def get_day_of_week(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.strftime('%A')

# Test the function with various dates
print(get_day_of_week('2023-10-01'))     