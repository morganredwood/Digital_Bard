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
    continue_button1.grid(row=1, column=1, padx=20, pady=50)


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
    continue_button2.grid(row=3, column=1, padx=10, pady=20)


def continue_button2_clicked():
    continue_button2.destroy()
    textline1.config(text="You will have a total of eight lyric choices to make.")
    textline2.config(text="Choose one item from each group of three.")
    continue_button3.grid(row=3, column=1, padx=10, pady=20)


def continue_button3_clicked():
    continue_button3.destroy()
    textline1.config(text="Group 1")
    textline2.config(text="")
    choice_hello("itw")


def choice_hello(group):
    if group == "itw":
        choiceitw_i_button.grid(row=3, column=1, padx=20, pady=20)
        choiceitw_t_button.grid(row=4, column=1, padx=20, pady=20)
        choiceitw_w_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "ots":
        choiceots_o_button.grid(row=3, column=1, padx=20, pady=20)
        choiceots_t_button.grid(row=4, column=2, padx=20, pady=20)
        choiceots_s_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "lwt":
        choicelwt_l_button.grid(row=3, column=1, padx=20, pady=20)
        choicelwt_w_button.grid(row=4, column=2, padx=20, pady=20)
        choicelwt_t_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "jtf":
        choicejtf_j_button.grid(row=3, column=1, padx=20, pady=20)
        choicejtf_t_button.grid(row=4, column=2, padx=20, pady=20)
        choicejtf_f_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "tntof":
        choicetntof_t_button.grid(row=3, column=1, padx=20, pady=20)
        choicetntof_nt_button.grid(row=4, column=2, padx=20, pady=20)
        choicetntof_of_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "pbf":
        choicepbf_p_button.grid(row=3, column=1, padx=20, pady=20)
        choicepbf_b_button.grid(row=4, column=2, padx=20, pady=20)
        choicepbf_f_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "lsw":
        choicelsw_l_button.grid(row=3, column=1, padx=20, pady=20)
        choicelsw_s_button.grid(row=4, column=2, padx=20, pady=20)
        choicelsw_w_button.grid(row=5, column=3, padx=20, pady=20)
    if group == "fcw":
        choicefcw_f_button.grid(row=3, column=1, padx=20, pady=20)
        choicefcw_c_button.grid(row=4, column=2, padx=20, pady=20)
        choicefcw_w_button.grid(row=5, column=3, padx=20, pady=20)


def choice_goodbye(group):
    if group == "itw":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "ots":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "lwt":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "jtf":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "tntof":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "pbf":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "lsw":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "fcw":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()


def choiceitw_i_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")


def choiceitw_t_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")


def choiceitw_w_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")


def choiceots_o_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")


def choiceots_t_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")


def choiceots_s_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")


def choicelwt_l_button_clicked():
    choice_goodbye("lwt")
    choice_hello("tntof")
    textline1.config(text="Group 4")
    textline2.config(text="")


def choicelwt_w_button_clicked():
    choice_goodbye("lwt")
    choice_hello("tntof")
    textline1.config(text="Group 4")
    textline2.config(text="")


def choicelwt_t_button_clicked():
    choice_goodbye("lwt")
    choice_hello("tntof")
    textline1.config(text="Group 4")
    textline2.config(text="")


def choice_tntof_t_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 5")
    textline2.config(text="")


def choice_tntof_nt_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")




def continue_button4_clicked():
    continue_button4.destroy()


#   THE BUTTON LIBRARY
start_button = Button(window, text="Start", bg="gainsboro", fg="black", font=fancyfont, width=8,
                      command=start_button_clicked)
continue_button1 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button1_clicked)
continue_button2 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button2_clicked)
continue_button3 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button3_clicked)
continue_button4 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont, width=8,
                          command=continue_button4_clicked)
choiceitw_i_button = Button(window, text="I", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceitw_i_button_clicked)
choiceitw_t_button = Button(window, text="They", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceitw_t_button_clicked)
choiceitw_w_button = Button(window, text="We", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceitw_w_button_clicked)
choiceots_o_button = Button(window, text="Old", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceots_o_button_clicked)
choiceots_t_button = Button(window, text="Tall", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceots_t_button_clicked)
choiceots_s_button = Button(window, text="Sad", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choiceots_s_button_clicked)
choicelwt_l_button = Button(window, text="Leave", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelwt_l_button_clicked)
choicelwt_w_button = Button(window, text="Watch", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelwt_w_button_clicked)
choicelwt_t_button = Button(window, text="Trust", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelwt_t_button_clicked)
choicepbf_p_button = Button(window, text="")
choicepbf_b_button =
choicepbf_f_button =
choicelsw_l_button =
choicelsw_s_button =
choicelsw_w_button =
choicefcw_f_button =
choicefcw_c_button =
choicefcw_w_button =

# DISPLAYING THE FIRST GUI BUTTON
start_button.grid(row=1, column=1, padx=50, pady=50)

# ENDING THE GUI CODE
window.mainloop()
