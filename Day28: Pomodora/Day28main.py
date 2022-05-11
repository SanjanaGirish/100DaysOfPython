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
LONG_BREAK_MIN = 10
reps = 0
timer = None
# ---------------------------- TIMER RESET ----------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    heading.config(text='Timer')
    check_label.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 ==0:
        heading.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        heading.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        heading.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM --------------------------- #


def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        completed_checks = "✔" * math.floor(reps / 2)
        check_label.config(text=completed_checks)
# ---------------------------- UI SETUP -------------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
heading.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white',
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=3, column=3)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
check_label.grid(row=4, column=2)

window.mainloop()

