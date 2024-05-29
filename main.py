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


def playlist(track):
    if track == "1":
        line1 = "I thought I heard"
    if track == "2":
        line1 = "They thought they heard"
    if track == "3":
        line1 = "We thought we heard"
    if track == "4":
        line 2
        1
        I
        thought
        I
        heard
        2
        They
        thought
        they
        heard
        3
        We
        thought
        we
        heard
        4
        The
        Old
        5
        The
        Tall
        6
        The
        Sad
        7
        Man
        say
        8
        Leave
        her
        1
        9
        Watch
        her
        1
        10
        Trust
        her
        1
        11
        Johnny
        1
        12
        Timmy
        1
        13
        Frodo
        14
        Leave
        her
        2
        15
        Watch
        her
        2
        16
        Trust
        her
        2
        17
        Tomorrow, ye
        will
        18
        Next
        Tuesday, ye
        will
        19
        On
        Friday, ye
        will
        20
        Get
        your
        pay
        21
        Get
        your
        bell
        22
        Get
        your
        fish
        23
        And
        it
        's time for us
        24
        To
        leave
        her
        25
        To
        watch
        her
        26
        To
        trust
        her
        27
        Oh, leave
        her
        28
        Oh, watch
        her
        29
        Oh, trust
        her
        30
        Johnny
        2
        31
        Timmy
        2
        32
        Frodo
        2
        33
        Leave
        her
        3
        34
        Watch
        her
        3
        35
        Trust
        her
        3
        36
        For
        the
        voyage is long
        37
        For
        the
        voyage is short
        38
        For
        the
        voyage is wild
        39
        And
        the
        winds
        don
        't blow
        40
        Oh, the
        wind
        was
        foul, and the
        sea
        ran
        high
        41
        Oh, the
        wind
        was
        cold, and the
        sea
        ran
        high
        42
        Oh, the
        wind
        was
        weird, and the
        sea
        ran
        high
        43
        She
        shipped
        it
        green, and none
        went
        by


def library(file):
    if file == "1":
        play1 = pygame.mixer.Sound("itih.mp3").play()
    if file == "2":
        play2 = pygame.mixer.Sound("ttth.mp3").play()
    if file == "3":
        play3 = pygame.mixer.Sound("wtwh.mp3").play()
    if file == "4":
        play4 = pygame.mixer.Sound("to.mp3").play()
    if file == "5":
        play5 = pygame.mixer.Sound("tt.mp3").play()
    if file == "6":
        play6 = pygame.mixer.Sound("ts.mp3").play()
    if file == "7":
        play7 = pygame.mixer.Sound("ms.mp3").play()
    if file == "8":
        play8 = pygame.mixer.Sound("lher_one.mp3").play()
    if file == "9":
        play9 = pygame.mixer.Sound("wher_one.mp3").play()
    if file == "10":
        play10 = pygame.mixer.Sound("trher_one.mp3").play()
    if file == "11":
        play11 = pygame.mixer.Sound("johnny_one.mp3").play()
    if file == "12":
        play12 = pygame.mixer.Sound("timmy_one.mp3").play()
    if file == "13":
        play13 = pygame.mixer.Sound("frodo_one.mp3").play()
    if file == "14":
        play14 = pygame.mixer.Sound("lher_two.mp3").play()
    if file == "15":
        play15 = pygame.mixer.Sound("wher_two.mp3").play()
    if file == "16":
        play16 = pygame.mixer.Sound("trher_two.mp3").play()
    if file == "17":
        play17 = pygame.mixer.Sound("tyw.mp3").play()
    if file == "18":
        play18 = pygame.mixer.Sound("ntyw.mp3").play()
    if file == "19":
        play19 = pygame.mixer.Sound("ofyw.mp3").play()
    if file == "20":
        play20 = pygame.mixer.Sound("getyp.mp3").play()
    if file == "21":
        play21 = pygame.mixer.Sound("getyb.mp3").play()
    if file == "22":
        play22 = pygame.mixer.Sound("getyf.mp3").play()
    if file == "23":
        play23 = pygame.mixer.Sound("aitfu.mp3").play()
    if file == "24":
        play24 = pygame.mixer.Sound("tlher_one.mp3").play()
    if file == "25":
        play25 = pygame.mixer.Sound("twher_one.mp3").play()
    if file == "26":
        play26 = pygame.mixer.Sound("ttrher_one.mp3").play()
    if file == "27":
        play27 = pygame.mixer.Sound("olher_one.mp3").play()
    if file == "28":
        play28 = pygame.mixer.Sound("owher_one.mp3").play()
    if file == "29":
        play29 = pygame.mixer.Sound("otrher_one.mp3").play()
    if file == "30":
        play30 = pygame.mixer.Sound("johnny_two.mp3").play()
    if file == "31":
        play31 = pygame.mixer.Sound("timmy_two.mp3").play()
    if file == "32":
        play32 = pygame.mixer.Sound("frodo_two.mp3").play()
    if file == "33":
        play33 = pygame.mixer.Sound("lher_three.mp3").play()
    if file == "34":
        play34 = pygame.mixer.Sound("wher_three.mp3").play()
    if file == "35":
        play35 = pygame.mixer.Sound("trher_three.mp3").play()
    if file == "36":
        play36 = pygame.mixer.Sound("ftvil.mp3").play()
    if file == "37":
        play37 = pygame.mixer.Sound("ftvis.mp3").play()
    if file == "38":
        play38 = pygame.mixer.Sound("ftviw.mp3").play()
    if file == "39":
        play39 = pygame.mixer.Sound("atwdb.mp3").play()
    if file == "40":
        play40 = pygame.mixer.Sound("otwwwatsrh.mp3").play()
    if file == "41":
        play41 = pygame.mixer.Sound("otwwcatsrh.mp3").play()
    if file == "42":
        play42 = pygame.mixer.Sound("otwwwatsrh.mp3").play()
    if file == "43":
        play43 = pygame.mixer.Sound("ssiganwb.mp3").play()


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
