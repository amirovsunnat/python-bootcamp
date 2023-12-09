from tkinter import *
from tkinter import messagebox
import pyperclip

from password_generator import password_generator


def save_info():
    """Gets entries values, and save them into file."""
    website_name = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    # validate entered data
    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you have filled all the fields.")
    else:
        want_to_save = messagebox.askokcancel(title=website_name, message=f"Here is entered information:\n"
                                                                          f"Email: {email_username}\n"
                                                                          f"Password: {password}\nIs it okay to save?")
        if want_to_save:
            with open("passwords.txt", mode="a") as file:
                file.write(f"{website_name} | {email_username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def generate_and_write_password():
    """Generates random password and write it to password entry."""
    random_password = password_generator()
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


FONT_LABEL = ("Courier", 15, "bold")
FONT_ENTRY = ("Courier", 12, "bold")
FONT_BUTTON = ("Courier", 13, "bold")

window = Tk()
window.title("Password Manager App")
window.config(padx=60, pady=60)


# create canvas object
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# create labels
website_label = Label(text="Website:", font=FONT_LABEL)
website_label.grid(row=1, column=0)
website_label.config(padx=3, pady=3)

email_label = Label(text="Email/Username:", font=FONT_LABEL)
email_label.grid(row=2, column=0)
email_label.config(padx=3, pady=3)

password_label = Label(text="Password:", font=FONT_LABEL)
password_label.grid(row=3, column=0)
password_label.config(padx=3, pady=3)

# create entries
website_entry = Entry(width=50, font=FONT_ENTRY, highlightcolor="red", highlightthickness=2)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # focus on website entry when app is launched

email_entry = Entry(width=50, font=FONT_ENTRY, highlightcolor="red", highlightthickness=2)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@gmail.com")

password_entry = Entry(width=31, font=FONT_ENTRY, highlightcolor="red", highlightthickness=2)
password_entry.grid(row=3, column=1)

# create buttons
generate_pass_button = Button(text="Generate Password", font=FONT_BUTTON, command=generate_and_write_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=50, font=FONT_BUTTON, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
