from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

# try opening the file
try:
    data = pandas.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}
timer = None
SECONDS = 3


# timer
def count_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        flip_card()


def next_card():
    global current_card
    current_card_choice = random.choice(to_learn)
    french_word = current_card_choice["French"]
    english_word = current_card_choice["English"]
    current_card["French"] = french_word
    current_card["English"] = english_word
    canvas.itemconfig(tagOrId=card_title, text="French", fill="black")
    canvas.itemconfig(tagOrId=card_word, text=french_word, fill="black")
    canvas.itemconfig(tagOrId=card_image, image=card_front_image)
    count_down(SECONDS)


def flip_card():
    global current_card
    canvas.itemconfig(tagOrId=card_image, image=card_back_image)
    canvas.itemconfig(tagOrId=card_title, text="English", fill="white")
    canvas.itemconfig(tagOrId=card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------------- UI ----------------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Creating a picture
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Creating wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# Creating right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()
count_down(SECONDS)

window.mainloop()
