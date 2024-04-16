from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(text=password)


# ---------------------------- SEARCH WEBSITE ------------------------------ #
def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
        # searching for website:
        website = website_input.get()
        website_in_dict = data[website]
        messagebox.showinfo(title=website, message=f"Email: {website_in_dict['email']}\n"
                                                   f"Password: {website_in_dict['password']}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="There is no saved password!")
    except KeyError:
        messagebox.showerror(title="Error", message=f"There is no password for {website} yet!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Save password to file
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
                   website: {
                       "email": email,
                       "password": password,
                   }
               }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving old data
                json.dump(data, data_file, indent=4)
        finally:
            # Clear input areas
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating Canvas for image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Creating labels for information
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Creating entry labels
website_input = Entry(width=27)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=45)
username_input.insert(0, string="balint.karoly13@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=27)
password_input.grid(column=1, row=3)

# Creating buttons
generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()
