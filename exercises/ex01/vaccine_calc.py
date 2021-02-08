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

today: datetime = datetime.today()

# Begin your solution here...

pop = input("Population: ") 
populacion = int(pop) 

do_ad = input("Doses Administered: ") 
doses_admin = int(do_ad) 

do_pe = input("Doses per day: ") 
doses_perday = int(do_pe) 

tar = input("Target percent vaccinated: ") 
target_percent = int(tar) 

ladate = today.strftime("%B %d, %Y")

ppl = populacion * (target_percent / 100)

ppl_need = (ppl - doses_admin / 2)

doses_needed = ppl_need * 2

numero_days = doses_needed // doses_perday

number_days: timedelta = timedelta(numero_days)
future: datetime = today + number_days

print(numero_days)
print(target_percent)

print("We will reach" ,  target_percent , "% vaccination in" , numero_days , "days, which falls on" , future.strftime("%B %d, %Y"))