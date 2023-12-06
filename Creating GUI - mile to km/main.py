from tkinter import *


FONT = ("Arial", 12, "bold")


# create function convert miles to km
def mile_to_km():
    """Converts mile to km."""
    mile = float(text_entry.get())
    km = round(mile * 1.609)
    text3.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

# create labels
text1 = Label(text="is equal to", font=FONT)
text1.grid(column=0, row=1)

text2 = Label(text="Miles", font=FONT, padx=10, pady=10)
text2.grid(column=2, row=0)


text3 = Label(text="0", font=FONT)
text3.grid(column=1, row=1)

text4 = Label(text="Km", font=FONT)
text4.grid(column=2, row=1)

# create text entry
text_entry = Entry(width=13)
text_entry.grid(column=1, row=0)

# create button
button = Button(text="Calculate", width=8, font=FONT, command=mile_to_km)
button.grid(column=1, row=2)


window.mainloop()
