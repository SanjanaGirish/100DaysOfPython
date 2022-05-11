from tkinter import *
import pandas
from random import choice
# ---------------------------- CONSTANTS ------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
COUNT_SECONDS = 3
curr_word = {}
data_dict = {}
# --------------------------- FLIP CARDS ------------------------------------- #
def flip_cards():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, fill="white", text=curr_word["English"])


# --------------------------- SAVE PROGRESS ---------------------------------- #
def is_known():
    data_dict.remove(curr_word)
    pandas.DataFrame(data_dict).to_csv(path_or_buf='data/words_to_learn.csv',
                                       index=False)
    generate_new_word()

# --------------------------- WORDS IN FLASHCARDS ---------------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
finally:
    data_dict = data.to_dict(orient="records")


def generate_new_word():
    global curr_word, flip
    window.after_cancel(flip)
    curr_word = choice(data_dict)
    french_word = curr_word["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    flip = window.after(3000, flip_cards)
# ---------------------------- UI SETUP -------------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, flip_cards)

# Front flashcard Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0,
                bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Text on Canvas
card_title = canvas.create_text(400, 150, text="French",
                                font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word",
                               font=("Ariel", 60, "bold"))

# Wrong-button (❌)
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0,
                      command=generate_new_word)
wrong_button.grid(row=1, column=0)

# Correct-Button (✅)
right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0,
                      command=is_known)
right_button.grid(row=1, column=1)

generate_new_word()

window.mainloop()
