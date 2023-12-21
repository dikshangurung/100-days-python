import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0

# FONT = ("Arial",16,"normal")

def start_timer():
    global reps
    reps +=1
    work_sec = 30
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        reps += 1
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0 and reps % 8 == 0:
        reps += 1
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

    else:
        reps += 1
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        window.after(1000,count_down,count-1)
    else:
        tick_mark_signs = "✔"
        if reps%2 == 0:
            tick_mark_signs += "✔"
        canvas.itemconfig(tick_mark,text = "✔")
        # for tick in tick_mark_signs:
        #     tick_mark = Label(text=f"{tick}", font=("Arial", 16, "bold"), fg=GREEN, bg=YELLOW)
        #     tick_mark.grid(column=1, row=3)
        start_timer()

# ---------------------------- TIMER RESET ------------------------------- #
def reset_it():
    start_timer()
#
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.gif")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_btn = Button(text="Start",font=("Arial",10,"normal"),command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset",font=("Arial",10,"normal"),command=reset_it)
reset_btn.grid(column=2,row=2)

tick_mark = Label(text="✔",font=("Arial",16,"bold"),fg=GREEN,bg=YELLOW)
tick_mark.grid(column=1,row=3)
window.mainloop()