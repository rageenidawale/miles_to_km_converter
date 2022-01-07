from tkinter import *

# Creating a new window and configuration
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # adds padding to the window

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="This is new text")  # use .confing() to change pre-existing widgets
# need to use .pack() or .place(x=xcor, y=ycor) or .grid() to display the widget on the screen
# cannot use grid and pack in the same program
my_label.pack()  # cannot specify the position
my_label.place(x=0, y=0)  # requires very specific position
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)  # adds padding to the widget


# Button

def button_is_clicked():
    print("Button is clicked")
    my_label.config(text="Button is Clicked")  # changes the label text when the button is clicked
    new_text = entry.get()
    my_label.config(text=new_text)  # changes the label to the entry part when the button is clicked


button = Button(text="Click Me", command=button_is_clicked)
button.pack()

# Entry
entry = Entry(width=10)
entry.insert(END, string="Some text to begin with.")  # Add some text to begin with
print(entry.get())  # Gets text in the entry
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()  # Puts cursor in the textbox
text.insert(END, "Example of multi-line text entry.")  # Adds some text to begin with
print(text.get("1.0", END))  # Gets current value in textbox at line 1, character 0
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())  # gets the current value in spinbox


spinbox = Spinbox(from_=0, to=0, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):  # Called with current scale value
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())  # Prints 1 if On button checked, otherwise 0


checked_state = IntVar()  # variable to hold on to checked state - 0 is off, 1 is on
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


radio_state = IntVar()  # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used():
    print(listbox.get(listbox.curselection()))  # gets current selection from listbox


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
