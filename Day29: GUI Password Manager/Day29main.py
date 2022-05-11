from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR --------------- ------------ #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for ch in range(randint(2, 4))]
    password_list += [choice(numbers) for chars in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD --------------------------------- #
def click_add():
    website_data = website_entry.get()
    username_data = email_entry.get()
    pwd_data = pwd_entry.get()
    new_data = {website_data: {"email": username_data,
                               "password": pwd_data
                                }
                }
    # if len(website_data) or len(pwd_data) == 0:
    #     messagebox.showinfo(title='Oops', message="Please don't leave any "
    #                                               "fields empty")
    # else:
    is_ok = messagebox.askokcancel(title=website_data,
                                    message=f"These are the details entered:"
                                            f"\nEmail: {username_data} "
                                            f"\nPassword: {pwd_data} \nIs it"
                                            f" ok to save?")
    if is_ok:
        try:
            with open("pwd_data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data
                data.update(new_data)
        except FileNotFoundError:
            with open("pwd_data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("pwd_data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            pwd_entry.delete(0, END)

def click_search():
    website = website_entry.get()
    try:
        with open("pwd_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                       f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for "
                                                       f"{website} exists.")
# ---------------------------- UI SETUP -------------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=1, column=2)

website_label = Label(text="Website:")
website_label.grid(row=2, column=1)

website_entry = Entry(width=21)
website_entry.grid(row=2, column=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, 'sanjanagirish123@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

pwd_entry = Entry(width=21)
pwd_entry.grid(row=4, column=2)

generate_pwd_button = Button(text="Generate Password",
                             command=generate_password)
generate_pwd_button.grid(row=4, column=3)

add_button = Button(text="Add", width=36, command=click_add)
add_button.grid(row=5, column=2, columnspan=2)

search_button = Button(text="Search", width=13, command=click_search)
search_button.grid(row=2, column=3)

window.mainloop()
