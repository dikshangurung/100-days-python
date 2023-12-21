from tkinter import *
window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)
#input
input_mile = Entry(width=15)
input_mile.insert(END,string="0")
input_mile.focus()
input_mile.grid(column=1,row=0)

font_spec = ("Arial",12,"normal")
#Function
def calculate_it():
    mile = float(input_mile.get())
    kilometers = round(mile * 1.60934,2)
    km_output.config(text= kilometers)
#label
miles = Label(text="Miles",font=font_spec)
miles.grid(column=2,row=0)
equal = Label(text="Is equal to ",font=font_spec)
equal.grid(column=0,row=1)
km_output = Label(text="0",font=font_spec)
km_output.grid(column=1,row=1)
km = Label(text="Km",font=font_spec)
km.grid(column=2,row=1)
calculate = Button(text="Calculate",font=font_spec,command=calculate_it)
calculate.grid(column=1,row=2)
# #Label
# my_label = Label(text="I am groot",font=("Arial",24,"bold"))
# my_label.grid(column=0,row=0)
# #Button
# def button_clicked():
#     print("ok")
#
# button1 = Button(text="Click Me",command=button_clicked)
# button1.grid(column=1,row=1)
#
# button2 = Button(text="Also Click Me",command=button_clicked)
# button2.grid(column=2,row=0)
# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3,row=3)
window.mainloop()