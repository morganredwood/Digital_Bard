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
    continue_button1.grid(row=1, column=1, padx=20, pady=20)


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
        choiceots_t_button.grid(row=4, column=1, padx=20, pady=20)
        choiceots_s_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "lwt":
        choicelwt_l_button.grid(row=3, column=1, padx=20, pady=20)
        choicelwt_w_button.grid(row=4, column=1, padx=20, pady=20)
        choicelwt_t_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "jtf":
        choicejtf_j_button.grid(row=3, column=1, padx=20, pady=20)
        choicejtf_t_button.grid(row=4, column=1, padx=20, pady=20)
        choicejtf_f_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "tntof":
        choicetntof_t_button.grid(row=3, column=1, padx=20, pady=20)
        choicetntof_nt_button.grid(row=4, column=1, padx=20, pady=20)
        choicetntof_of_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "pbf":
        choicepbf_p_button.grid(row=3, column=1, padx=20, pady=20)
        choicepbf_b_button.grid(row=4, column=1, padx=20, pady=20)
        choicepbf_f_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "lsw":
        choicelsw_l_button.grid(row=3, column=1, padx=20, pady=20)
        choicelsw_s_button.grid(row=4, column=1, padx=20, pady=20)
        choicelsw_w_button.grid(row=5, column=1, padx=20, pady=20)
    if group == "fcw":
        choicefcw_f_button.grid(row=3, column=1, padx=20, pady=20)
        choicefcw_c_button.grid(row=4, column=1, padx=20, pady=20)
        choicefcw_w_button.grid(row=5, column=1, padx=20, pady=20)


def choice_goodbye(group):
    if group == "itw":
        choiceitw_i_button.destroy()
        choiceitw_t_button.destroy()
        choiceitw_w_button.destroy()
    if group == "ots":
        choiceots_o_button.destroy()
        choiceots_t_button.destroy()
        choiceots_s_button.destroy()
    if group == "lwt":
        choicelwt_l_button.destroy()
        choicelwt_w_button.destroy()
        choicelwt_t_button.destroy()
    if group == "jtf":
        choicejtf_j_button.destroy()
        choicejtf_t_button.destroy()
        choicejtf_f_button.destroy()
    if group == "tntof":
        choicetntof_t_button.destroy()
        choicetntof_nt_button.destroy()
        choicetntof_of_button.destroy()
    if group == "pbf":
        choicepbf_p_button.destroy()
        choicepbf_b_button.destroy()
        choicepbf_f_button.destroy()
    if group == "lsw":
        choicelsw_l_button.destroy()
        choicelsw_s_button.destroy()
        choicelsw_w_button.destroy()
    if group == "fcw":
        choicefcw_f_button.destroy()
        choicefcw_c_button.destroy()
        choicefcw_w_button.destroy()


def choiceitw_i_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")
    playlist("1")


def choiceitw_t_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")
    playlist("2")

def choiceitw_w_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")
    playlist("3")

def choiceots_o_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("4")

def choiceots_t_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("5")

def choiceots_s_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("6")

def choicelwt_l_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("8")
    playlist("14")
    playlist("33")

def choicelwt_w_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("9")
    playlist("15")
    playlist("34")

def choicelwt_t_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("10")
    playlist("16")
    playlist("35")

def choicejtf_j_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("11")
    playlist("30")

def choicejtf_t_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("12")
    playlist("31")

def choicejtf_f_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("13")
    playlist("32")

def choicetntof_t_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("17")

def choicetntof_nt_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("18")

def choicetntof_of_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("19")

def choicepbf_p_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("20")

def choicepbf_b_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("21")

def choicepbf_f_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("22")

def choicelsw_l_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("36")

def choicelsw_s_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("37")

def choicelsw_w_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("38")

def choicefcw_f_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline2.config(text="")
    playlist("40")


def choicefcw_c_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline2.config(text="")
    playlist("41")


def choicefcw_w_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline1.config(text="")
    playlist("42")


def continue_button4_clicked():
    continue_button4.destroy()


def playlist(number):
    #   Playlist 1 "I thought I heard"
        #   Track 1 "I thought I heard"
        #   Track 2 "They thought they heard"
        #   Track 3 "We thought we heard"
    #   Playlist 2 "The Old"
        #   Track 4 "The Old"
        #   Track 5 "The Tall"
        #   Track 6 "The Sad"
    #   Playlist 3 "Man say"
        #   Track 7 "Man say"
    #   Playlist 4 "Leave her"
        #   Track 8 "Leave her 1"
        #   Track 9 "Watch her 1"
        #   Track 10 "Trust her 1"
    #   Playlist 5 "Johnny"
        #   Track 11 "Johnny 1"
        #   Track 12 "Timmy 1"
        #   Track 13 "Frodo 1"
    #   Playlist 6 "Leave her"
        #   Track 14 "Leave her 2"
        #   Track 15 "Watch her 2"
        #   Track 16 "Trust her 2"
    #   Playlist 7 "Tomorrow, ye will"
        #   Track 17 "Tomorrow, ye will"
        #   Track 18 "Next Tuesday, ye will"
        #   Track 19 "On Friday, ye will"
    #   Playlist 8 "Get your pay"
        #   Track 20 "Get your pay"
        #   Track 21 "Get your bell"
        #   Track 22 "Get your fish"
    #   Playlist 9 "And it's time for us"
        # Track 23 "And it's time for us"
    #   Playlist 10 "To leave her"
        #   Track 24 "To leave her"
        #   Track 25 "To watch her"
        #   Track 26 "To trust her"
    #   Playlist 11 "Leave her"
        #   Track 27 "Leave her 1"
        #   Track 28 "Watch her 1"
        #   Track 29 "Trust her 1"
    #   Playlist 12 "Johnny"
        #   Track 30 "Johnny 1"
        #   Track 31 "Timmy 1"
        #   Track 32 "Frodo 1"
    #   Playlist 13 "Leave her"
        #   Track 33 "Leave her 2"
        #   Track 34 "Watch her 2"
        #   Track 35 "Trust her 2"
    #   Playlist 14 "Oh, leave her"
        #   Track 36 "Oh, leave her"
        #   Track 37 "Oh, watch her"
        #   Track 38 "Oh, trust her"
    #   Playlist 15 "Johnny"
        #   Track 39 "Johnny 2"
        #   Track 40 "Timmy 2"
        #   Track 41 "Frodo 2"
    #   Playlist 16 "Leave her"
        #   Track 42 "Leave her 3"
        #   Track 43 "Watch her 3"
        #   Track 44 "Trust her 3"
    #   Playlist 17 "For the voyage is long"
        #   Track 45 "For the voyage is long"
        #   Track 46 "For the voyage is short"
        #   Track 47 "For the voyage is wild"
    #   Playlist 18 "And the winds don't blow"
        #   Track 48 "And the winds don't blow"
    #   Playlist 19 "And it's time for us"
        #   Track 49 "And it's time for us"
    #   Playlist 20 "To leave her"
        #   Track 50 "To leave her"
        #   Track 51 "To watch her"
        #   Track 52 "To trust her"
    #   Playlist 21 "Oh, the wind was foul, and the sea ran high"
        #   Track 53 "Oh, the wind was foul, and the sea ran high"
        #   Track 54 "Oh, the wind was cold, and the sea ran high"
        #   Track 55 "Oh, the wind was weird, and the sea ran high"
    #   Playlist 22 "Leave her"
        #   Track 56 "Leave her 1"
        #   Track 57 "Watch her 1"
        #   Track 58 "Trust her 1"
    #   Playlist 23 "Johnny"
        #   Track 59 "Johnny 1"
        #   Track 60 "Timmy 1"
        #   Track 61 "Frodo 1"
    #   Playlist 24 "Leave her"
        #   Track 62 "Leave her 2"
        #   Track 63 "Watch her 2"
        #   Track 64 "Trust her 2"
    #   Playlist 25 "She shipped it green, and none went by"
        #   Track 65 "She shipped it green, and none went by"
    #   Playlist 26 "And it's time for us"
        #   Track 66 "And it's time for us"
    #   Playlist 27 "To leave her"
        #   Track 67 "To leave her"
        #   Track 68 "To watch her"
        #   Track 69 "To trust her"
    #   Playlist 28 "Leave her"
        #   Track 70 "Leave her 1"
        #   Track 71 "Watch her 1"
        #   Track 72 "Trust her 1"
    #   Playlist 29 "Johnny"
        #   Track 73 "Johnny 1"
        #   Track 74 "Timmy 1"
        #   Track 75 "Frodo 1"
    #   Playlist 30 "Leave her"
        #   Track 76 "Leave her"
        #   Track 77 "Watch her"
        #   Track 78 "Trust her"
    #   Playlist 31 "Oh, leave her"
        #   Track 79 "Oh, leave her"
        #   Track 80 "Oh, watch her"
        #   Track 81 "Oh, trust her"
    #   Playlist 32 "Johnny"
        #   Track 82 "Johnny 2"
        #   Track 83 "Timmy 2"
        #   Track 84 "Frodo 2"
    #   Playlist 33 "Leave her"
        #   Track 85 "Leave her 3"
        #   Track 86 "Watch her 3"
        #   Track 87 "Trust her 3"
    #   Playlist 34 "For the voyage is long"
        #   Track 88 "For the voyage is long"
        #   Track 89 "For the voyage is short"
        #   Track 90 "For the voyage is wild"
    #   Playlist 35 "And the winds don't blow"
        #   Track 91 "And the winds don't blow'
    #   Playlist 36 "And it's time for us"
        #   Track 92 "And it's time for us"
    #   Playlist 37 "To leave her"
        #   Track 93 "To leave her"
        #   Track 94 "To watch her"
        #   Track 95 "To trust her"
    #   Playlist 38 "Leave her"
        #   Track 96 "Leave her"
        #   Track 97 "Watch her"
        #   Track 98 "Trust her"
    #   Playlist 39 "Johnny"
        #   Track 99 "Johnny 1"
        #   Track 100 "Timmy 1"
        #   Track 101 "Frodo 1"
    #   Playlist 40 "Leave her"
        #   Track 102 "Leave her 2"
        #   Track 103 "Watch her 2"
        #   Track 104 "Trust her 2"
    #   Playlist 41 "Oh, leave her"
        #   Track 105 "Oh, leave her"
        #   Track 106 "Oh, watch her"
        #   Track 107 "Oh, trust her"
    #   Playlist 42 "Johnny"
        #   Track 108 "Johnny 2"
        #   Track 109 "Timmy 2"
        #   Track 110 "Frodo 2"
    #   Playlist 43 "Leave her"
        #   Track 111 "Leave her"
        #   Track 112 "Watch her"
        #   Track 113 "Trust her"
    #   Playlist 44 "For the voyage is long"
        #   Track 114 "For the voyage is long"
        #   Track 115 "For the voyage is short"
        #   Track 116 "For the voyage is wild"
    #   Playlist 45 "And the winds don't blow"
        #   Track 117 "And the winds don't blow"
    #   Playlist 46 "And it's time for us"
        #   Track 118 "And it's time for us"
    #   Playlist 47 "To leave her"
        #   Track 119 "To leave her"
        #   Track 120 "To watch her"
        #   Track 121 "To trust her"

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
choicejtf_j_button = Button(window, text="Johnny", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicejtf_j_button_clicked)
choicejtf_t_button = Button(window, text="Timmy", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicejtf_t_button_clicked)
choicejtf_f_button = Button(window, text="Frodo", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicejtf_f_button_clicked)
choicetntof_t_button = Button(window, text="Tomorrow", bg="gainsboro", fg="black", font=fancyfont, width=12,
                              command=choicetntof_t_button_clicked)
choicetntof_nt_button = Button(window, text="Next Tuesday", bg="gainsboro", fg="black", font=fancyfont, width=12,
                               command=choicetntof_nt_button_clicked)
choicetntof_of_button = Button(window, text="On Friday", bg="gainsboro", fg="black", font=fancyfont, width=12,
                               command=choicetntof_of_button_clicked)
choicepbf_p_button = Button(window, text="Pay", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicepbf_p_button_clicked)
choicepbf_b_button = Button(window, text="Bell", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicepbf_b_button_clicked)
choicepbf_f_button = Button(window, text="Fish", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicepbf_f_button_clicked)
choicelsw_l_button = Button(window, text="Long", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelsw_l_button_clicked)
choicelsw_s_button = Button(window, text="Short", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelsw_s_button_clicked)
choicelsw_w_button = Button(window, text="Wild", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicelsw_w_button_clicked)
choicefcw_f_button = Button(window, text="Foul", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicefcw_f_button_clicked)
choicefcw_c_button = Button(window, text="Cold", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicefcw_c_button_clicked)
choicefcw_w_button = Button(window, text="Weird", bg="gainsboro", fg="black", font=fancyfont, width=12,
                            command=choicefcw_w_button_clicked)

# DISPLAYING THE FIRST GUI BUTTON
start_button.grid(row=1, column=1, padx=50, pady=50)

# ENDING THE GUI CODE
window.mainloop()
