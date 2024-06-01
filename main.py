import pygame
from tkinter import *
import tkinter as tk
pygame.init()
pycharm_default_font = ("JetBrains Mono", 13)
window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Digital Bard")
window.config(bg="black")
label = tk.Label(window, text="", bg="black")
label.grid(row=0, column=0)
office_backdrop = PhotoImage(file="computer_screen.png")
simulated_computer_frame = Label(window, image=office_backdrop, bg="black")
simulated_computer_frame.grid(row=0, column=0)
line1_print = Label(window, bg="pink", fg="purple", font=pycharm_default_font, text="print")
line1_print.grid(row=1, column=1)
line1_open_parentheses = Label(window, bg="white", font=pycharm_default_font, text="     (")
line1_open_parentheses.grid(row=1, column=1)
line1_text_in_quotes = Label(window, bg="white", fg="green",
                             text="      Lex Fridman: Do you have advice for a programming beginner "
                                  "on how to learn Python the right way?")
line1_text_in_quotes.grid(row=1, column=2)
line1_close_parentheses = Label(window, bg="white", text="                                          "
                                                          "                                           "
                                                          "                  )")
line1_close_parentheses.grid(row=1, column=2)
line2_print = Label(window, bg='white', fg="purple", text="print")
line2_print.grid(row=2, column=1)
line2_open_parentheses = Label(window, bg="white", text="     (")
line2_open_parentheses.grid(row=2, column=2)
line2_text_in_quotes = Label(window, bg="white", fg="green", text="Guido van Rossum: Find something "
                                                                   "you actually want to do with it."
                                                                   "If you say, \"I wanna learn skill X,\""
                                                                   "that's not enough motivation.  "
                                                                   "You need to pick something, "
                                                                   "and it can be a crazy problem you want"
                                                                   "to solve.  It can be completely"
                                                                   "unrealistic, but something that"
                                                                   "challenges you into actually learning"
                                                                   "coding in some language.")
line2_text_in_quotes.grid(row=2, column=1)
line2_close_parentheses = Label(window, bg="white", text="                                              "
                                                          "                                               "
                                                          "                                                "
                                                          "                                               "
                                                          "                                             "
                                                          "                                             "
                                                          "                                                    "
                                                          "     ')")
line2_close_parentheses.grid(row=2, column=1)
line3_terminal_output_line1 = Label(window, bg="black", text="Lex Fridman: Do you have advice for a programming"
                                                             "beginner on how to learn Python the right way?")
line3_terminal_output_line1.grid(row=2, column=1)
line4_terminal_output_line2 = Label(window, bg="black", text="Guido van Rossum: Find something you ac tually"
                                                             "want to do with it.  If you say, \"I wann learn"
                                                             "skill X,\" that's not enough motivation."
                                                             "You need to pick something, and it can be a crazy"
                                                             "problem you want to solve.  It can be completely"
                                                             "unrealistic, but something that challenges you"
                                                             "into actually learning coding in some language.")
line4_terminal_output_line2.grid(row=4, column=1)
window.mainloop()
