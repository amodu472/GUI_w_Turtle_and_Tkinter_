import pandas
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# Create our window and configurations
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Read and store our data
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def left_switch():
    # cancel previous timer
    global flip_timer
    window.after_cancel(flip_timer)
    word = choice(to_learn)
    french = word["French"]
    english = word["English"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{french}", fill="black")
    # initiate another card flip
    flip_timer = window.after(3000, switch_card, english)
    return word


def right_switch():
    to_be_removed = left_switch()
    to_learn.remove(to_be_removed)
    to_be_learned = pandas.DataFrame(to_learn)
    to_be_learned.to_csv("data/words_to_learn.csv")


def switch_card(to_english):
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{to_english}", fill="white")
    canvas.itemconfig(canvas_image, image=back_photo_image)


# ______________________________________________________ UI ____________________________________________________________

# required photo images
front_photo_image = PhotoImage(file="images/card_front.png")
back_photo_image = PhotoImage(file="images/card_back.png")
right_photo_image = PhotoImage(file="images/right.png")
wrong_photo_image = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(408, 286, image=front_photo_image)
title_text = canvas.create_text(400, 125, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# initial flip timer
flip_timer = window.after(3000, left_switch)

# buttons
right_button = Button(image=right_photo_image, highlightthickness=0, command=right_switch)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_photo_image, highlightthickness=0, command=left_switch)
wrong_button.grid(column=0, row=1)

window.mainloop()
