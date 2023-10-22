import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(2, 4))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    random_password = "".join(password_list)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Alert!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            website = data[website_entry.get()]
            email = website["email"]
            password = website["password"]
            messagebox.showinfo(title="Credentials",
                                message=f"Website: {website_entry.get()}\nEmail: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message="No Details For Website Exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass: Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Calibre", 14))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=("Calibre", 14))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Calibre", 14))
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sarveshmhatre213@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()