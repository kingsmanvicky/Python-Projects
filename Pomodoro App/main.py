from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="LONG BREAK",fg = RED)
        count_down(long_break_sec)
    elif reps %2 == 0:
        title_label.config(text="BREAK",fg = PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="WORK",fg = GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 150,pady = 100,bg=YELLOW)


title_label = Label(text="Timer!!",fg = GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=2,row=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112,image = tomato_img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


start_button = Button(text="Start",highlightthickness=0,bg="white",font=(FONT_NAME,15,"bold"),command=start_timer)
start_button.grid(column=1,row=3)


check_marks = Label(bg = YELLOW,font=(20),fg=GREEN)
check_marks.grid(column=2,row=3)


reset_button = Button(text="Reset",font=(FONT_NAME,15,"bold"),highlightthickness=0,bg="white",command=reset_timer)
reset_button.grid(column=3,row=3)


window.mainloop()