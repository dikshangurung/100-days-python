# class NotificationManager:
#     #This class is responsible for sending notifications with the deal flight details.
#     pass

from datetime import datetime,timedelta
curr_date = datetime.now()
date_after_6months = curr_date + timedelta(days=6*30)
print(curr_date.strftime("%d/%m/%Y"))
print(date_after_6months.strftime("%d/%m/%Y"))