#   SETTING UP THE CODE
import pygame
from tkinter import *
import tkinter as tk
pygame.init()
fancyfont = ("Lucida Calligraphy", 20)
#   SETTING UP THE GUI
window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Digital Bard")
window.config(bg="black")
label = tk.Label(window, text="", bg="black")
label.grid(row=0, column=0)
lex = PhotoImage(file="LexFridman.png")
lex_image_display = Label(window, image=lex, bg="black")
guido = PhotoImage(file="GuidovanRossum.png")
guido_image_display = Label(window, image=guido, bg="black")
#   TEXT DISPLAY AREAS
textline1 = Label(window, text="", bg="black", fg="gold", font=fancyfont)
textline2 = Label(window, text="", bg="black", fg="gold", font=fancyfont)
choice1_option = Label(window, text="I", bg="gray14", fg="gold", font=fancyfont, width=8)
choice2_option = Label(window, text="They", bg="gray14", fg="gold", font=fancyfont, width=8)
choice3_option = Label(window, text="We", bg="gray14", fg="gold", font=fancyfont, width=8)
textline1.config(text="Lex Fridman")
textline1.grid(row=2, column=2, padx=75, pady=50, sticky=W)
# IMAGE DISPLAY AREAS
lex_image_display.grid(row=3, column=2, padx=75, pady=50, sticky=W)
textline2.config(text="Guido van Rossum")
textline2.grid(row=2, column=4, padx=450, pady=50, sticky=W)
guido_image_display.grid(row=3, column=4, padx=450, pady=50, sticky=W)


# THE BUTTON CLICK ACTIONS
def start_button_clicked():
    start_button.destroy()
    play = pygame.mixer.Sound("interview01.mp3").play()
    while play.get_busy():
        continue
    play = pygame.mixer.Sound("interview02.mp3").play()
        while play.get_busy():
        continue
    play = pygame.mixer.Sound("interview03.mp3").play()
    while play.get_busy():
        continue
    play = pygame.mixer.Sound("interview04.mp3").play()
    while play.get_busy():
        continue
    play = pygame.mixer.Sound("interview05.mp3").play()
    while play.get_busy():
        continue
    continue_button1.grid(row=1, column=1, padx=50, pady=50)


def continue_button1_clicked():
    continue_button1.destroy()
    guido_image_display.destroy()
    lex_image_display.destroy()
    textline1.config(text="Welcome to your free trial of Digital Bard.")
    textline1.grid(row=1, column=1, padx=20, pady=20)
    textline2.config(text="Please enjoy this sample from our sea shanty collection.")
    textline2.grid(row=2, column=1, padx=20, pady=20)
    pygame.mixer.music.load("scarborough_fair.mp3")
    pygame.mixer.music.play(-1)
    continue_button2.grid(row=3, column=1, padx=20, pady=20)


def continue_button2_clicked():
    continue_button2.destroy()
    textline1.config(text="You will have a total of eight lyric choices to make.")
    textline2.config(text="Choose one item from each group of three.")
    continue_button3.grid(row=3, column=1, padx=20, pady=20)


def continue_button3_clicked():
    continue_button3.destroy()


#   THE BUTTON LIBRARY
start_button = Button(window, text="Start", bg="gainsboro", fg="black", font=fancyfont, width=8,
                      command=start_button_clicked)
continue_button1 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button1_clicked)
continue_button2 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button2_clicked)
continue_button3 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button3_clicked)
# DISPLAYING THE FIRST GUI BUTTON
start_button.grid(row=1, column=1, padx=50, pady=50)

# ENDING THE GUI CODE
window.mainloop()
