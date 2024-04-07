from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = {}


def generate_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(image_displayed, image=card_front_image)
    canvas.itemconfig(language_label, text="French", fill="Black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="Black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(language_label, text="English", fill="White")
    canvas.itemconfig(word_label, text=current_card["English"], fill="White")
    canvas.itemconfig(image_displayed, image=card_back_image)


def remove_word():
    global current_card
    data_dict.remove(current_card)
    generate_random_word()
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv("data/To_learn.csv", index=False, encoding="utf-8")


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image_displayed = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_label = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
flip_timer = window.after(4000, func=flip_card)


tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=remove_word)
tick_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=generate_random_word)
cross_button.grid(row=1, column=0)

try:
    with open("data/To_learn.csv") as file:
        data = pandas.read_csv(file, encoding="utf-8")
        data_dict = data.to_dict(orient="records")
except FileNotFoundError:
    with open("data/french_words.csv") as file:
        data = pandas.read_csv(file)
        data_dict = data.to_dict(orient="records")

generate_random_word()








window.mainloop()

