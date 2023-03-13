from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient = "records")


def next_card():
    global current_card ,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French",fill= 'black')
    canvas.itemconfig(card_word, text= current_card["French"], fill= 'black')
    canvas.itemconfig(card_backgorund, image= card_front_img)
    flip_timer = window.after(3000, func= flip_card)


def flip_card():
    canvas.itemconfig(card_title, text= "English", fill= 'white')
    canvas.itemconfig(card_word, text= current_card["English"], fill ='white')
    canvas.itemconfig(card_backgorund, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index= False)
    next_card()


#Window Creation
window = Tk()
window.title("Flash Card")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)


#Canvas Creation
canvas = Canvas(width= 800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_backgorund = canvas.create_image(400, 263, image= card_front_img)
card_title = canvas.create_text(400, 158, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font=("Ariel", 60, "bold"))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row = 0, column= 0, columnspan = 2)


#Buttons
cross_image = PhotoImage(file = "images/wrong.png")
unknown_button = Button(image= cross_image, highlightthickness= 0, bg= BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row = 1, column = 0)
check_image = PhotoImage(file="images/right.png")
check_button = Button(image= check_image, highlightthickness= 0, bg= BACKGROUND_COLOR, command= is_known)
check_button.grid(row= 1, column = 1)


next_card()


window.mainloop()