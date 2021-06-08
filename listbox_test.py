from tkinter import *


espn_100 = open("espn_100.txt").read().splitlines()

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(top, height=10,
                  width=18,
                  bg="white",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="black")
scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT, fill=Y)

# Define the size of the window.
top.geometry("250x300")

# Define a label for the list.
label = Label(top, text=" Espn Draft 2020", font='bold', fg='blue')
listbox.insert(END, *espn_100)

# pack the widgets
label.pack()
listbox.pack()

# Display until User
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# exits themselves.
top.mainloop()