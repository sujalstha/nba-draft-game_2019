# NBA 2020 Draft
# 5/9/2020
# by Sujal Shrestha

# modules
from tkinter import *


def start():
    draft_win = Tk()
    draft_win.resizable(False, False)  # no resize for both directions
    draft_win.title('NBA 2020 Draft')  # window title
    draft_win.geometry("500x400")  # Define the size of the window.
    draft_win.iconbitmap(r'nba-logo.ico')  # window icon


def project_btn_pressed():
    espn_100 = open("espn.txt").read().splitlines()

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

    top.mainloop()


def picks_btn_pressed():
    espn_100 = open("espn.txt").read().splitlines()
    espn_100.sort()

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

    top.mainloop()


def gui():
    global win, fgColor, bgColor, text

    # window config
    win = Tk()  # Gui window
    win.resizable(False, False)  # no resize for both directions
    win.title('NBA 2020 Draft')  # window title
    fgColor = "#FFFFFF"  # font color
    bgColor = "#333333"  # background color
    text = ("Geneva", 20)
    text_2 = ("Geneva", 14)
    win.configure(bg='#f8f9fa')  # background color
    win.geometry('500x400')  # window size
    win.iconbitmap(r'nba-logo.ico')  # window icon

    titleFrame = Frame(win, bg="#333333")
    titleFrame.place(relwidth=1, relheight=0.08)

    Label(titleFrame,
          text='2020 NBA Draft',
          font=text,
          anchor=CENTER,
          fg=fgColor,
          bg=bgColor).place(relx=0.3, relheight=1)

    nbaLogo = PhotoImage(file=r"nba-logo.png")

    logo = Label(win,
                 image=nbaLogo,
                 bg="#f8f9fa",
                 compound=CENTER)
    logo.place(
        relx=.20,
        rely=.09,
        relwidth=0.55,
        relheight=0.7)

    projectedPicks = Button(font=text_2,
                            text='Projected Picks',
                            anchor=E,
                            fg=fgColor,
                            bg=bgColor,
                            borderwidth=0,
                            command=project_btn_pressed)

    projectedPicks.place(relx=0,
                         relheight=.2,
                         rely=.40,
                         relwidth=0.28)

    draftPicks = Button(font=text,
                        text='Draft Picks',
                        anchor=E,
                        fg=fgColor,
                        bg=bgColor,
                        borderwidth=0,
                        command=picks_btn_pressed)

    draftPicks.place(relx=0.72,
                     relheight=0.2,
                     rely=.40,
                     relwidth=0.28)

    start_game = Button(font=text,
                        text='Start',
                        fg=fgColor,
                        bg=bgColor,
                        borderwidth=0,
                        command=start)
    start_game.place(relx=0.35,
                     relheight=0.10,
                     rely=.80,
                     relwidth=0.28)

    win.mainloop()


# call functions
gui()
