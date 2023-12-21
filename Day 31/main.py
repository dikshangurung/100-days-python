import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *


def flip():
    canvas_top.itemconfig(old_img,image=card_back_img)
    canvas_top.itemconfig(language_txt, text="English",fill="white")
    canvas_top.itemconfig(text_txt, text=f"{current_card['English']}",fill="white")

def next_card():
    global timer_name,current_card,current_card
    window.after_cancel(timer_name)
    current_card = random.choice(data_dict)
    canvas_top.itemconfig(old_img, image=card_front_img)
    canvas_top.itemconfig(language_txt,text="French",fill="black")
    canvas_top.itemconfig(text_txt,text = f"{current_card['French']}",fill="black")
    timer_name = window.after(3000,flip)

def memorised():
    data_dict.remove(current_card)
    # data_dict.to_csv("words_to_learn.csv")
    dataFrame = pandas.DataFrame(data_dict)
    dataFrame.to_csv("./data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.configure(background=BACKGROUND_COLOR,padx=50,pady=50)

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
# print(data)


timer_name = window.after(3000,flip)
canvas_top = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
old_img = canvas_top.create_image(400,263,image=card_front_img)
canvas_top.config(background=BACKGROUND_COLOR,highlightthickness=0)
canvas_top.grid(row=0,column=0,columnspan=2,rowspan=2)

language_txt = canvas_top.create_text(400,150,text="French",font=("Ariel",40,"italic"))
text_txt = canvas_top.create_text(400,263,text="trouve",font=("Ariel",60,"bold"))

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=2,column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=memorised)
right_btn.grid(row=2,column=1)
next_card()
window.mainloop()