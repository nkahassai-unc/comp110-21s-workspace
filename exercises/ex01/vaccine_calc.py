"""A vaccination calculator."""

__author__ = "730411124"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta

# Begin your solution here...
today: datetime = datetime.today()

prompt_populacion = input("Population: ") 
populacion = int(prompt_populacion) 
# Promp population figures.

prompt_doses_admin = input("Doses Administered: ") 
doses_admin = int(prompt_doses_admin) 
# Prompt doses adminstrated.

prompt_doses = input("Doses per day: ") 
doses_perday = int(prompt_doses) 
# Prompt doses per day.

prompt_percent = input("Target percent vaccinated: ") 
target_percent = int(prompt_percent) 
# Prompt target percentage.

ppl = populacion * (target_percent / 100)

doses_need = 2 * (ppl - doses_admin / 2)

days = round(doses_need // doses_perday)
number_days: timedelta = timedelta(days)
future: datetime = today + number_days
print_perc = str(target_percent)

print("We will reach " + print_perc + "% vaccination in", days, "days, which falls on", future.strftime("%B %d, %Y"))