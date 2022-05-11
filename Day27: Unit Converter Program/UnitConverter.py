from tkinter import *


def calculate():
    miles = int(miles_input.get())
    km = round(1.609 * miles)
    km_output.config(text=km)


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(row=1, column=2)

miles_label = Label(text='Miles', font=("Arial", 16))
miles_label.grid(row=1, column=3)

equals_label = Label(text='is equal to', font=("Arial", 16))
equals_label.grid(row=2, column=1)

km_output = Label(text='', font=("Arial", 16))
km_output.grid(row=2, column=2)

km_label = Label(text='Km', font=("Arial", 16))
km_label.grid(row=2, column=3)

cal_button = Button(text="Calculate", command=calculate)
cal_button.grid(row=3, column=2)
window.mainloop()
