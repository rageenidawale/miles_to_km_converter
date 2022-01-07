from tkinter import *


def button_is_clicked():
    miles = float(entry.get())
    km = float(miles * 1.609344)
    km = round(km, 2)
    km_label.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=50)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=20, pady=5)

km_label = Label(text="0")
km_label.grid(column=1, row=1)
km_label.config(padx=20, pady=5)

miles_text = Label(text="miles")
miles_text.grid(column=2, row=0)
miles_text.config(padx=20, pady=5)

km_text = Label(text="km")
km_text.grid(column=2, row=1)
km_text.config(padx=20, pady=5)

entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text="Convert", command=button_is_clicked)
button.grid(column=1, row=2)
button.config(padx=20, pady=5)
window.mainloop()
