from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from password_generator import password_generator


def save_info():
    """Gets entries values, and save them into file."""
    website_name = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    data = {
        website_name: {
            "email": email_username,
            "password": password,
        }
    }

    # validate entered data
    if len(website_name) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you have filled all the fields.")
    else:
        try:
            with open("data.json", "r") as file:
                # read data
                data_dict = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        else:
            # update data
            data_dict.update(data)
            want_to_save = messagebox.askokcancel(title=website_name, message=f"Here is entered details:\n"
                                                                              f"Email/Username: {email_username}\n"
                                                                              f"Password: {password}\n\n"
                                                                              f"Are you sure you want to save it ?")
            if want_to_save:
                with open("data.json", "w") as file:
                    # write data
                    json.dump(data_dict, file, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


def generate_and_write_password():
    """Generates random password and write it to password entry."""
    random_password = password_generator()
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)


def search_data():
    """Search user data by website name, and returns if it is existed, otherwise file data file not found."""
    website_name = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Something happened.",
                             message=f"File data does not exist. Please save some data first.")
    else:
        if len(website_name) == 0:
            messagebox.showerror(title="Error", message=f"Please make sure you have entered website name.")
        elif website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not found", message=f"{website_name} does not exist database.")


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
website_entry = Entry(width=31, font=FONT_ENTRY, highlightcolor="red", highlightthickness=2)
website_entry.grid(row=1, column=1)
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

search_button = Button(text="Search", width=16, font=FONT_BUTTON, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()
