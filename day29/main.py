import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
#----------------------------Searching
def search_it():
    website_value = website_entry.get()
    try:

        with open("data.json",mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="File not found bro")
    else:
        if website_value in data:
            messagebox.showinfo(title="Ok chata",message=f"Your email is {data[website_value]['email']} "
                                                         f"and password is {data[website_value]['password']}")
        else:
            messagebox.showinfo(message="Website not found")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = "abcdefghijklmnopqrstuvwxyz"
    # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password = ''.join(password_letters)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    new_data = {website_value:{
        "email": email_value,
        "password": password_value,
    }}
    if len(website_value) != 0 and len(email_value) != 0 and len(password_value) != 0:


        bool = messagebox.askokcancel(title="ok",message=f"you entered email:{email_value},password:{password_value}\n"
                                                  f"Do you want to proceed?")
        if bool:
            try:
                with open("data.json",mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json",mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
               data.update(new_data)
               with open("data.json", mode="w") as data_file:
                   json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showinfo(title="Empty",message="You left a box empty")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:",font=("Arial",10,"bold"))
website_label.grid(column=0,row=1)
website_entry = Entry(width=50)
website_entry.grid(column=1,row=1)
website_entry.focus()

search_btn = Button(text="Search",command=search_it)
search_btn.grid(column=2,row=1)

email_label = Label(text="Email/Username:",font=("Arial",10,"bold"))
email_label.grid(column=0,row=2)
email_entry = Entry(width=50)
email_entry.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password:",font=("Arial",10,"bold"))
password_label.grid(column=0,row=3)
password_entry = Entry(width=32)
password_entry.grid(column=1,row=3)

generate_password_label = Button(text="Generate Password",command=generate_pass)
generate_password_label.grid(column=2,row=3)

add_btn = Button(text="Add",width=43,command=save)
add_btn.grid(column=1,row=4,columnspan=2)
window.mainloop()