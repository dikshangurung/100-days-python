from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel",16,"normal")
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.my_label = Label(text="Score: 0",font=FONT,bg=THEME_COLOR)
        self.my_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas_text = self.canvas.create_text(150,125,text="Amazion is ok ok ok ok ok ok ko ok ok ko ok ok ok ok",
                                                   width=280,
                                                   fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,rowspan=2,column=0,columnspan=2,pady=50)

        self.tick_img = PhotoImage(file="./images/true.png")
        self.tick_btn = Button(image=self.tick_img,bg=THEME_COLOR,highlightthickness=0,command=self.true_answer)
        self.tick_btn.grid(column=0,row=3,)
        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_btn = Button(image=self.wrong_img,bg=THEME_COLOR,command=self.false_answer)
        self.wrong_btn.grid(column=1,row=3)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_test = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=q_test)
        else:
            self.canvas.itemconfig(self.canvas_text,text="Question has ended bro")
            self.tick_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.my_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)