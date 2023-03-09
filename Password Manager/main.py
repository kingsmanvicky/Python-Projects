from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for item in range(randint(8, 10))]
    password_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password_numbers = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    pw = "".join(password_list)
    password_entry.insert(0, pw)
    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    pw = password_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": pw
    }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any entry empty")
    else:
        try:
            with open("passwords.json","r") as pw_file:
                data = json.load(pw_file)


        except FileNotFoundError:
                with open("passwords.json","w") as pw_file:
                     json.dump(new_data, pw_file, indent=4)
                
        else:
            data.update(new_data)  

            with open("passwords.json", "w") as pw_file:
                json.dump(data, pw_file, indent=4)
        
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as pw_file:
            data = json.load(pw_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Passwords has been stored, \nKindly save some passwords to use the Functionality")
    else:        
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email} \nPassword: {password}")
        else:
             messagebox.showinfo(title="Error", message=f"The {website} hasn't stored yet")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "mm3343@srmist.edu.in")
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password",command=pw_generator)
generate_password_button.grid(row=3, column=3)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=3)
search_button = Button(text="Search" ,width=15,command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()