from cProfile import label
from cgitb import text
from tkinter import *
from turtle import onclick, width

from pip import main

main_window = Tk()

# Labels

Label(main_window, text="Web scrapping").grid(row=0, column=0)

# #Label(main_window, text=" how many unique words").grid(row=4, column=0)

# Label(main_window, text=" Count how many stories are retrieved").grid(
#     row=5, column=0)

# Label(main_window, text=" Count how many stories are retrieved").grid(
#     row=6, column=0)

# Label(main_window, text="Max and min length story.").grid(
#     row=7, column=0)


# Text fill
scrapeDataFromSite = Entry(main_window, width=50,
                           borderwidth=5).grid(row=1, column=1)


# Button
Button(main_window, text="Scrape Web", command=onclick).grid(row=2, column=1)

Button(main_window, text="how many unique words").grid(row=8, column=1)

Button(main_window, text="Count how many stories are retrieved").grid(
    row=16, column=1)

Button(main_window, text="Max and min length story").grid(row=24, column=1)

Button(main_window, text="Top 10 words in terms of frequency.").grid(
    row=32, column=1)

Button(main_window, text="Plot a bar-graph").grid(
    row=40, column=1)


def onclick():
    print({scrapeDataFromSite})


main_window.mainloop()
