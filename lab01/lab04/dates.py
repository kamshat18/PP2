# Write a Python program to subtract five days from current date.

# Write a Python program to print yesterday, today, tomorrow.

# Write a Python program to drop microseconds from datetime.

# Write a Python program to calculate two date difference in seconds.


 #TASK 1
from datetime import datetime , timedelta
today = datetime.now() 
substract_days= timedelta(days=5)
print(today-substract_days)

#TASK 2
from datetime import datetime , timedelta
today = datetime.now() 
days= timedelta(days=1)
print(today-days)
print(today)
print(today+days)

#TASK 3 
from datetime import datetime
today = datetime.now()
microseconds = today.replace(microsecond=0)
print("дата и время:", today)
print("без микросекунд:", microseconds)

#TASK 4
from datetime import datetime
date1 = datetime(2025, 3, 10, 12, 0, 0)  
date2 = datetime(2025, 2, 13, 14, 30, 0)  
difference= abs((date2 - date1).total_seconds())

print("Difference:", difference)
