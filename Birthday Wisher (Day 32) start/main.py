import random
import smtplib
with open(file="quotes.txt",mode="r") as file:
    file_list = file.readlines()
    send_this = random.choice(file_list)

email = "pythontest3967@gmail.com"
password = "ruevmynqbbpslzkk"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="dxngrg2058@gmail.com",msg=f"Subject: Today's Motivation \n\n {send_this}")







