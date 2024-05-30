#   SETTING UP THE CODE
import pygame
from tkinter import *
import tkinter as tk
pygame.init()
fancyfont_header = ("Lucida Calligraphy", 20)
fancyfont_main = ("Courier New", 16)
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
textline1 = Label(window, text="", bg="black", fg="gold", font=fancyfont_header)
textline2 = Label(window, text="", bg="black", fg="gold", font=fancyfont_header)
textline3 = Label(window, text="", bg="black", fg="white", font=fancyfont_main)
textline4 = Label(window, text="", bg="black", fg="white", font=fancyfont_main)
textline5 = Label(window, text="", bg="black", fg="white", font=fancyfont_main)
choice1_option = Label(window, text="I", bg="gray14", fg="gold", font=fancyfont_header, width=8)
choice2_option = Label(window, text="They", bg="gray14", fg="gold", font=fancyfont_header, width=8)
choice3_option = Label(window, text="We", bg="gray14", fg="gold", font=fancyfont_header, width=8)
textline1.config(text="Lex Fridman")
textline1.grid(row=2, column=2, padx=75, pady=50, sticky=W)
# IMAGE DISPLAY AREAS
lex_image_display.grid(row=4, column=2, padx=75, pady=50, sticky=W)
textline2.config(text="Guido van Rossum")
textline2.grid(row=2, column=3, padx=450, pady=50, sticky=W)
textline3.grid(row=3, column=3, padx=75, pady=50, sticky=W)
textline4.grid(row=4, column=3, padx=75, pady=50, sticky=W)
textline5.grid(row=5, column=3, padx=75, pady=50, sticky=W)
guido_image_display.grid(row=6, column=4, padx=450, pady=50, sticky=W)


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
    continue_button3.grid(row=3, column=1, padx=50, pady=20)


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
    playlist("1", "1")


def choiceitw_t_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")
    playlist("1",  "2")


def choiceitw_w_button_clicked():
    choice_goodbye("itw")
    choice_hello("ots")
    textline1.config(text="Group 2")
    textline2.config(text="")
    playlist("1", "3")


def choiceots_o_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("2", "4")


def choiceots_t_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("2", "5")


def choiceots_s_button_clicked():
    choice_goodbye("ots")
    choice_hello("lwt")
    textline1.config(text="Group 3")
    textline2.config(text="")
    playlist("2", "6")


def choicelwt_l_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("3", "8")
    playlist("3", "14")
    playlist("3", "33")


def choicelwt_w_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("3", "9")
    playlist("3", "15")
    playlist("3", "34")


def choicelwt_t_button_clicked():
    choice_goodbye("lwt")
    choice_hello("jtf")
    textline1.config(text="Group 4")
    textline2.config(text="")
    playlist("3", "10")
    playlist("3", "16")
    playlist("3", "35")


def choicejtf_j_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("4", "11")
    playlist("4", "30")


def choicejtf_t_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("4", "12")
    playlist("4", "31")


def choicejtf_f_button_clicked():
    choice_goodbye("jtf")
    choice_hello("tntof")
    textline1.config(text="Group 5")
    textline2.config(text="")
    playlist("4", "13")
    playlist("4", "32")


def choicetntof_t_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("5", "17")


def choicetntof_nt_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("5", "18")


def choicetntof_of_button_clicked():
    choice_goodbye("tntof")
    choice_hello("pbf")
    textline1.config(text="Group 6")
    textline2.config(text="")
    playlist("5", "19")


def choicepbf_p_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("6", "20")


def choicepbf_b_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("6", "21")


def choicepbf_f_button_clicked():
    choice_goodbye("pbf")
    choice_hello("lsw")
    textline1.config(text="Group 7")
    textline2.config(text="")
    playlist("6", "22")


def choicelsw_l_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("7", "36")


def choicelsw_s_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("7", "37")


def choicelsw_w_button_clicked():
    choice_goodbye("lsw")
    choice_hello("fcw")
    textline1.config(text="Group 8")
    textline2.config(text="")
    playlist("7", "38")


def choicefcw_f_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline2.config(text="")
    playlist("8", "40")
    continue_button4.grid(row=3, column=1, padx=50, pady=20)


def choicefcw_c_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline2.config(text="")
    playlist("8", "41")
    continue_button4.grid(row=3, column=1, padx=50, pady=20)


def choicefcw_w_button_clicked():
    choice_goodbye("fcw")
    textline1.config(text="")
    textline1.config(text="")
    playlist("8", "42")
    continue_button4.grid(row=3, column=1, padx=20, pady=20)


def continue_button4_clicked():
    continue_button4.destroy()
    spinit("1", "")
    spinit("2", "")
    spinit("3", "")
    spinit("4", "")
    spinit("5", "")
    spinit("6", "")
    spinit("7", "")
    spinit("8", "")
    spinit("9", "")
    spinit("10", "")
    spinit("11", "")
    spinit("12", "")
    spinit("13", "")
    spinit("14", "")
    spinit("15", "")
    spinit("16", "")
    spinit("17", "")
    spinit("18", "")
    spinit("19", "")
    spinit("20", "")
    spinit("21", "")
    spinit("22", "")
    spinit("23", "")
    spinit("24", "")
    spinit("25", "")
    spinit("26", "")
    spinit("27", "")
    spinit("28", "")
    spinit("29", "")
    spinit("30", "")
    spinit("31", "")
    spinit("32", "")
    spinit("33", "")
    spinit("34", "")
    spinit("35", "")
    spinit("36", "")
    spinit("37", "")
    spinit("38", "")
    spinit("39", "")
    spinit("40", "")
    spinit("41", "")
    spinit("42", "")
    spinit("43", "")
    spinit("44", "")
    spinit("45", "")
    spinit("46", "")
    spinit("47", "")
    
    
def spinit(cue, track):
    #   I thought I heard
    if cue == "1":
        if track == "1":
            play = pygame.mixer.Sound("itih.mp3").play()
        if track == "2":
            play = pygame.mixer.Sound("ttth.mp3").play()
        if track == "3":
            play = pygame.mixer.Sound("wtwh.mp3").play()
        #   The Old
    if cue == "2":
        if track == "4":
            play = pygame.mixer.Sound("to.mp3").play()
        if track == "5":
            play = pygame.mixer.Sound("tt.mp3").play()
        if track == "6":
            play = pygame.mixer.Sound("ts.mp3").play()
        #   Man say
    if cue == "3":
        if track == "7":
            play = pygame.mixer.Sound("ms.mp3").play()
        #   Leave her
    if cue == "4":
        if track == "8":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "9":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "10":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        #   Johnny
    if cue == "5":
        if track == "11":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "12":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "13":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "6":
        if track == "14":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "15":
            play = pygame.mixer.Sound('wher_two.mp3').play()
        if track == "16":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        #   Tomorrow, ye will
    if cue == "7":
        if track == "17":
            play = pygame.mixer.Sound("tyw.mp3").play()
        if track == "18":
            play = pygame.mixer.Sound("ntyw.mp3").play()
        if track == "19":
            play = pygame.mixer.Sound("ofyw.mp3").play()
        #   Get your pay
    if cue == "8":
        if track == "20":
            play = pygame.mixer.Sound("getyp.mp3").play()
        if track == "21":
            play = pygame.mixer.Sound("getyb.mp3").play()
        if track == "22":
            play = pygame.mixer.Sound("getyf.mp3").play()
        #   And it's time for us
    if cue == "9":
        if track == "23":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        #   To leave her
    if cue == "10":
        if track == "24":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "25":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "26":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        #   Leave her
    if cue == "11":
        if track == "27":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "28":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "29":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        #   Johnny
    if cue == "12":
        if track == "30":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "31":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "32":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "13":
        if track == "33":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "34":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "35":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        #   Oh, leave her
    if cue == "14":
        if track == "36":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "37":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "38":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        #   Johnny
    if cue == "15":
        if track == "39":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "40":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "41":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "16":
        if track == "42":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "43":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "44":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        #   For the voyage is long
    if cue == "17":
        if track == "45":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "46":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "47":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        #   And the winds don't blow
    if cue == "18":
        if track == "48":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        #   And it's time for us
    if cue == "19":
        if track == "49":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        #   To leave her
    if cue == "20":
        if track == "50":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "51":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "52":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        #   Oh, the wind was wild, and the sea ran high
    if cue == "21":
        if track == "53":
            play = pygame.mixer.Sound("otwwwatsrh.mp3").play()
        if track == "54":
            play = pygame.mixer.Sound("otwwcatsrh.mp3").play()
        if track == "55":
            play = pygame.mixer.Sound("otwwcatsrh.mp3").play()
        #   Leave her
    if cue == "22":
        if track == "56":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "57":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "58":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        #   Johnny
    if cue == "23":
        if track == "59":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "60":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "61":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "24":
        if track == "62":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "63":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "64":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        #   She shipped it green, and none went by
    if cue == "25":
        if track == "65":
            play = pygame.mixer.Sound("ssiganwb.mp3").play()
        #   And it's time for us
    if cue == "26":
        if track == "66":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        #   To leave her
    if cue == "27":
        if track == "67":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "68":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "69":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        #   Leave her
    if cue == "28":
        if track == "70":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "71":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "72":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        #   Johnny
    if cue == "29":
        if track == "73":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "74":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "75":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "30":
        if track == "76":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "77":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "78":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        #   Oh, leave her
    if cue == "31":
        if track == "79":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "80":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "81":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        #   Johnny
    if cue == "32":
        if track == "82":
            play = pygame.mixer.Sound("johnny_two.mp3").play()
        if track == "83":
            play = pygame.mixer.Sound("timmy_two.mp3").play()
        if track == "84":
            play = pygame.mixer.Sound("frodo_two.mp3").play()
        #   Leave her
    if cue == "33":
        if track == "85":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "86":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "87":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        #   For the voyage is long
    if cue == "34":
        if track == "88":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "89":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "90":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        #   And the winds don't blow
    if cue == "35":
        if track == "91":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        #   And it's time for us
    if cue == "36":
        if track == "92":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        #   To leave her
    if cue == "37":
        if track == "93":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "94":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "95":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        #   Leave her
    if cue == "38":
        if track == "96":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "97":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "98":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        #   Johnny
    if cue == "39":
        if track == "99":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "100":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "101":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        #   Leave her
    if cue == "40":
        if track == "102":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "103":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "104":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        #   Oh, leave her
    if cue == "41":
        if track == "105":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "106":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "107":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        #   Johnny
    if cue == "42":
        if track == "108":
            play = pygame.mixer.Sound("johnny_two.mp3").play()
        if track == "109":
            play = pygame.mixer.Sound("timmy_two.mp3").play()
        if track == "110":
            play = pygame.mixer.Sound("frodo_two.mp3").play()
        #   Leave her
    if cue == "43":
        if track == "111":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "112":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "113":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        #   For the voyage is long
    if cue == "44":
        if track == "114":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "115":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "116":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        #   And the winds don't blow
    if cue == "45":
        if track == "117":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        #   And it's time for us
    if cue == "46":
        if track == "118":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        #   To leave her
    if cue == "47":
        if track == "119":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "120":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "121":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()


def playlist(cue, track):
    if cue == "1":
        if track == "1":
            cueit("1", "1")
        if track == "2":
            cueit("1", "2")
        if track == "3":
            cueit("1", "3")
    if cue == "2":
        if track == "4":
            cueit("2", "4")
        if track == "5":
            cueit("2", "5")
        if track == "6":
            cueit("2", "6")
    if cue == "3":
        if track == "7":
            cueit("3", "7")
    if cue == "4":
        if track == "8":
            cueit("4", "8")
        if track == "9":
            cueit("4", "9")
        if track == "10":
            cueit("4", "10")
    if cue == "5":
        if track == "11":
            cueit("5", "11")
        if track == "12":
            cueit("5", "12")
        if track == "13":
            cueit("5", "13")
    if cue == "6":
        if track == "14":
            cueit("6", "14")
        if track == "15":
            cueit("6", "15")
        if track == "16":
            cueit("6", "16")
    if cue == "7":
        if track == "17":
            cueit("7", "17")
        if track == "18":
            cueit("7", "18")
        if track == "19":
            cueit("7", "19")
    if cue == "8":
        if track == "20":
            cueit("8", "20")
        if track == "21":
            cueit("8", "21")
        if track == "22":
            cueit("8", "22")
    if cue == "9":
        if track == "23":
            cueit("9", "23")
    if cue == "10":
        if track == "24":
            cueit("10", "24")
        if track == "25":
            cueit("10", "25")
        if track == "26":
            cueit("10", "26")
    if cue == "11":
        if track == "27":
            cueit("11", "27")
        if track == "28":
            cueit("11", "28")
        if track == "29":
            cueit("11", "29")
    if cue == "12":
        if track == "30":
            cueit("12", "30")
        if track == "31":
            cueit("12", "31")
        if track == "32":
            cueit("12", "32")
    if cue == "13":
        if track == "33":
            cueit("13", "33")
        if track == "34":
            cueit("13", "34")
        if track == "35":
            cueit("13", "35")
    if cue == "14":
        if track == "36":
            cueit("14", "36")
        if track == "37":
            cueit("14", "37")
        if track == "38":
            cueit("14", "38")
    if cue == "15":
        if track == "39":
            cueit("15", "39")
        if track == "40":
            cueit("15", "40")
        if track == "41":
            cueit("15", "41")
    if cue == "16":
        if track == "42":
            cueit("16", "42")
        if track == "43":
            cueit("16", "43")
        if track == "44":
            cueit("16", "44")
    if cue == "17":
        if track == "45":
            cueit("17", "45")
        if track == "46":
            cueit("17", "46")
        if track == "47":
            cueit("17", "47")
    if cue == "18":
        if track == "48":
            cueit("18", "48")
    if cue == "19":
        if track == "49":
            cueit("19", "49")
    if cue == "20":
        if track == "50":
            cueit("20", "50")
        if track == "51":
            cueit("20", "51")
        if track == "52":
            cueit("20", "52")
    if cue == "21":
        if track == "53":
            cueit("21", "53")
        if track == "54":
            cueit("21", "54")
        if track == "55":
            cueit("21", "55")
    if cue == "22":
        if track == "56":
            cueit("22", "56")
        if track == "57":
            cueit("22", "57")
        if track == "58":
            cueit("22", "58")
    if cue == "23":
        if track == "59":
            cueit("23", "59")
        if track == "60":
            cueit("23", "60")
        if track == "61":
            cueit("23", "61")
    if cue == "24":
        if track == "62":
            cueit("24", "62")
        if track == "63":
            cueit("24", "63")
        if track == "64":
            cueit("24", "64")
    if cue == "25":
        if track == "65":
            cueit("25", "65")
    if cue == "26":
        if track == "66":
            cueit("26", "66")
    if cue == "27":
        if track == "67":
            cueit("27", "67")
        if track == "68":
            cueit("27", "68")
        if track == "69":
            cueit("27", "69")
    if cue == "28":
        if track == "70":
            cueit("28", "70")
        if track == "71":
            cueit("28", "71")
        if track == "72":
            cueit("28", "72")
    if cue == "29":
        if track == "73":
            cueit("29", "73")
        if track == "74":
            cueit("29", "74")
        if track == "75":
            cueit("29", "75")
    if cue == "30":
        if track == "76":
            cueit("30", "76")
        if track == "77":
            cueit("30", "77")
        if track == "78":
            cueit("30", "78")
    if cue == "31":
        if track == "79":
            cueit("31", "79")
        if track == "80":
            cueit("31", "80")
        if track == "81":
            cueit("31", "81")
    if cue == "32":
        if track == "82":
            cueit("32", "82")
        if track == "83":
            cueit("32", "83")
        if track == "84":
            cueit("32", "84")
    if cue == "33":
        if track == "85":
            cueit("33", "85")
        if track == "86":
            cueit("33", "86")
        if track == "87":
            cueit("33", "87")
    if cue == "34":
        if track == "88":
            cueit("34", "88")
        if track == "89":
            cueit("34", "89")
        if track == "90":
            cueit("34", "90")
    if cue == "35":
        if track == "91":
            cueit("35", "91")
    if cue == "36":
        if track == "92":
            cueit("36", "92")
    if cue == "37":
        if track == "93":
            cueit("37", "93")
        if track == "94":
            cueit("37", "94")
        if track == "95":
            cueit("37", "95")
    if cue == "38":
        if track == "96":
            cueit("38", "96")
        if track == "97":
            cueit("38", "97")
        if track == "98":
            cueit("38", "98")
    if cue == "39":
        if track == "99":
            cueit("39", "99")
        if track == "100":
            cueit("39", "100")
        if track == "101":
            cueit("39", "101")
    if cue == "40":
        if track == "102":
            cueit("40", "102")
        if track == "103":
            cueit("40", "103")
        if track == "104":
            cueit("40", "104")
    if cue == "41":
        if track == "105":
            cueit("41", "105")
        if track == "106":
            cueit("41", "106")
        if track == "107":
            cueit("41", "107")
    if cue == "42":
        if track == "108":
            cueit("42", "108")
        if track == "109":
            cueit("42", "109")
        if track == "110":
            cueit("42", "110")
    if cue == "43":
        if track == "111":
            cueit("43", "111")
        if track == "112":
            cueit("43", "112")
        if track == "113":
            cueit("43", "113")
    if cue == "44":
        if track == "114":
            cueit("44", "114")
        if track == "115":
            cueit("44", "115")
        if track == "116":
            cueit("44", "116")
    if cue == "45":
        if track == "117":
            cueit("45", "117")
    if cue == "46":
        if track == "118":
            cueit("46", "118")
    if cue == "47":
        if track == "119":
            cueit("47", "119")
        if track == "120":
            cueit("47", "120")
        if track == "121":
            cueit("47", "121")
            
            
def cueit(maintrack, subtrack):
    if maintrack == "1":
        if subtrack == "1":
            spinit("1", "1")
        if subtrack == "2":
            spinit("1", "2")
        if subtrack == "3":
            spinit("1", "3")
    if maintrack == "2":
        if subtrack == "4":
            spinit("2", "4")
        if subtrack == "5":
            spinit("2", "5")
        if subtrack == "6":
            spinit("2", "6")
    if maintrack == "3":
        if subtrack == "7":
            spinit("3", "7")
    if maintrack == "4":
        if subtrack == "8":
            spinit("4", "8")
        if subtrack == "9":
            spinit("4", "9")
        if subtrack == "10":
            spinit("4", "10")
    if maintrack == "5":
        if subtrack == "11":
            spinit("5", "11")
        if subtrack == "12":
            spinit("5", "12")
        if subtrack == "13":
            spinit("5", "13")
    if maintrack == "6":
        if subtrack == "14":
            spinit("6", "14")
        if subtrack == "15":
            spinit("6", "15")
        if subtrack == "16":
            spinit("6", "16")
    if maintrack == "7":
        if subtrack == "17":
            spinit("7", "17")
        if subtrack == "18":
            spinit("7", "18")
        if subtrack == "19":
            spinit("7", "19")
    if maintrack == "8":
        if subtrack == "20":
            spinit("8", "20")
        if subtrack == "21":
            spinit("8", "21")
        if subtrack == "22":
            spinit("8", "22")
    if maintrack == "9":
        if subtrack == "23":
            spinit("9", "23")
    if maintrack == "10":
        if subtrack == "24":
            spinit("10", "24")
        if subtrack == "25":
            spinit("10", "25")
        if subtrack == "26":
            spinit("10", "26")
    if maintrack == "11":
        if subtrack == "27":
            spinit("11", "27")
        if subtrack == "28":
            spinit("11", "28")
        if subtrack == "29":
            spinit("11", "29")
    if maintrack == "12":
        if subtrack == "30":
            spinit("12", "30")
        if subtrack == "31":
            spinit("12", "31")
        if subtrack == "32":
            spinit("12", "32")
    if maintrack == "13":
        if subtrack == "33":
            spinit("13", "33")
        if subtrack == "34":
            spinit("13", "34")
        if subtrack == "35":
            spinit("13", "35")
    if maintrack == "14":
        if subtrack == "36":
            spinit("14", "36")
        if subtrack == "37":
            spinit("14", "37")
        if subtrack == "38":
            spinit("14", "38")
    if maintrack == "15":
        if subtrack == "39":
            spinit("15", "39")
        if subtrack == "40":
            spinit("15", "40")
        if subtrack == "41":
            spinit("15", "41")
    if maintrack == "16":
        if subtrack == "42":
            spinit("16", "42")
        if subtrack == "43":
            spinit("16", "43")
        if subtrack == "44":
            spinit("16", "44")
    if maintrack == "17":
        if subtrack == "45":
            spinit("17", "45")
        if subtrack == "46":
            spinit("17", "46")
        if subtrack == "47":
            spinit("17", "47")
    if maintrack == "18":
        if subtrack == "48":
            spinit("18", "48")
    if maintrack == "19":
        if subtrack == "49":
            spinit("19", "49")
    if maintrack == "20":
        if subtrack == "50":
            spinit("20", "50")
        if subtrack == "51":
            spinit("20", "51")
        if subtrack == "52":
            spinit("20", "52")
    if maintrack == "21":
        if subtrack == "53":
            spinit("21", "53")
        if subtrack == "54":
            spinit("21", "54")
        if subtrack == "55":
            spinit("21", "55")
    if maintrack == "22":
        if subtrack == "56":
            spinit("22", "56")
        if subtrack == "57":
            spinit("22", "57")
        if subtrack == "58":
            spinit("22", "58")
    if maintrack == "23":
        if subtrack == "59":
            spinit("23", "59")
        if subtrack == "60":
            spinit("23", "60")
        if subtrack == "61":
            spinit("23", "61")
    if maintrack == "24":
        if subtrack == "62":
            spinit("24", "62")
        if subtrack == "63":
            spinit("24", "63")
        if subtrack == "64":
            spinit("24", "64")
    if maintrack == "25":
        if subtrack == "65":
            spinit("25", "65")
    if maintrack == "26":
        if subtrack == "66":
            spinit("26", "66")
    if maintrack == "27":
        if subtrack == "67":
            spinit("27", "67")
        if subtrack == "68":
            spinit("27", "68")
        if subtrack == "69":
            spinit("27", "69")
    if maintrack == "28":
        if subtrack == "70":
            spinit("28", "70")
        if subtrack == "71":
            spinit("28", "71")
        if subtrack == "72":
            spinit("28", "72")
    if maintrack == "29":
        if subtrack == "73":
            spinit("29", "73")
        if subtrack == "74":
            spinit("29", "74")
        if subtrack == "75":
            spinit("29", "75")
    if maintrack == "30":
        if subtrack == "76":
            spinit("30", "76")
        if subtrack == "77":
            spinit("30", "77")
        if subtrack == "78":
            spinit("30", "78")
    if maintrack == "31":
        if subtrack == "79":
            spinit("31", "79")
        if subtrack == "80":
            spinit("31", "80")
        if subtrack == "81":
            spinit("31", "81")
    if maintrack == "32":
        if subtrack == "82":
            spinit("32", "82")
        if subtrack == "83":
            spinit("32", "83")
        if subtrack == "84":
            spinit("32", "84")
    if maintrack == "33":
        if subtrack == "85":
            spinit("33", "85")
        if subtrack == "86":
            spinit("33", "86")
        if subtrack == "87":
            spinit("33", "87")
    if maintrack == "34":
        if subtrack == "88":
            spinit("34", "88")
        if subtrack == "89":
            spinit("34", "89")
        if subtrack == "90":
            spinit("34", "90")
    if maintrack == "35":
        if subtrack == "91":
            spinit("35", "91")
    if maintrack == "36":
        if subtrack == "92":
            spinit("36", "92")
    if maintrack == "37":
        if subtrack == "93":
            spinit("37", "93")
        if subtrack == "94":
            spinit("37", "94")
        if subtrack == "95":
            spinit("37", "95")
    if maintrack == "38":
        if subtrack == "96":
            spinit("38", "96")
        if subtrack == "97":
            spinit("38", "97")
        if subtrack == "98":
            spinit("38", "98")
    if maintrack == "39":
        if subtrack == "99":
            spinit("39", "99")
        if subtrack == "100":
            spinit("39", "100")
        if subtrack == "101":
            spinit("39", "101")
    if maintrack == "40":
        if subtrack == "102":
            spinit("40", "102")
        if subtrack == "103":
            spinit("40", "103")
        if subtrack == "104":
            spinit("40", "104")
    if maintrack == "41":
        if subtrack == "105":
            spinit("41", "105")
        if subtrack == "106":
            spinit("41", "106")
        if subtrack == "107":
            spinit("41", "107")
    if maintrack == "42":
        if subtrack == "108":
            spinit("42", "108")
        if subtrack == "109":
            spinit("42", "109")
        if subtrack == "110":
            spinit("42", "110")
    if maintrack == "43":
        if subtrack == "111":
            spinit("43", "111")
        if subtrack == "112":
            spinit("43", "112")
        if subtrack == "113":
            spinit("43", "113")
    if maintrack == "44":
        if subtrack == "114":
            spinit("44", "114")
        if subtrack == "115":
            spinit("44", "115")
        if subtrack == "116":
            spinit("44", "116")
    if maintrack == "45":
        if subtrack == "117":
            spinit("45", "117")
    if maintrack == "46":
        if subtrack == "118":
            spinit("46", "118")
    if maintrack == "47":
        if subtrack == "119":
            spinit("47", "119")
        if subtrack == "120":
            spinit("47", "120")
        if subtrack == "121":
            spinit("47", "121")
                    
                    
#   THE BUTTON LIBRARY
start_button = Button(window, text="Start", bg="gainsboro", fg="black", font=fancyfont_header, width=8,
                      command=start_button_clicked)
continue_button1 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont_header, width=8,
                          command=continue_button1_clicked)
continue_button2 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont_header, width=8,
                          command=continue_button2_clicked)
continue_button3 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont_header, width=8,
                          command=continue_button3_clicked)
continue_button4 = Button(window, text="Continue", bg="gainsboro", fg="black", font=fancyfont_header, width=8,
                          command=continue_button4_clicked)
choiceitw_i_button = Button(window, text="I", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceitw_i_button_clicked)
choiceitw_t_button = Button(window, text="They", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceitw_t_button_clicked)
choiceitw_w_button = Button(window, text="We", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceitw_w_button_clicked)
choiceots_o_button = Button(window, text="Old", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceots_o_button_clicked)
choiceots_t_button = Button(window, text="Tall", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceots_t_button_clicked)
choiceots_s_button = Button(window, text="Sad", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choiceots_s_button_clicked)
choicelwt_l_button = Button(window, text="Leave", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelwt_l_button_clicked)
choicelwt_w_button = Button(window, text="Watch", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelwt_w_button_clicked)
choicelwt_t_button = Button(window, text="Trust", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelwt_t_button_clicked)
choicejtf_j_button = Button(window, text="Johnny", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicejtf_j_button_clicked)
choicejtf_t_button = Button(window, text="Timmy", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicejtf_t_button_clicked)
choicejtf_f_button = Button(window, text="Frodo", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicejtf_f_button_clicked)
choicetntof_t_button = Button(window, text="Tomorrow", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                              command=choicetntof_t_button_clicked)
choicetntof_nt_button = Button(window, text="Next Tuesday", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                               command=choicetntof_nt_button_clicked)
choicetntof_of_button = Button(window, text="On Friday", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                               command=choicetntof_of_button_clicked)
choicepbf_p_button = Button(window, text="Pay", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicepbf_p_button_clicked)
choicepbf_b_button = Button(window, text="Bell", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicepbf_b_button_clicked)
choicepbf_f_button = Button(window, text="Fish", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicepbf_f_button_clicked)
choicelsw_l_button = Button(window, text="Long", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelsw_l_button_clicked)
choicelsw_s_button = Button(window, text="Short", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelsw_s_button_clicked)
choicelsw_w_button = Button(window, text="Wild", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicelsw_w_button_clicked)
choicefcw_f_button = Button(window, text="Foul", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicefcw_f_button_clicked)
choicefcw_c_button = Button(window, text="Cold", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicefcw_c_button_clicked)
choicefcw_w_button = Button(window, text="Weird", bg="gainsboro", fg="black", font=fancyfont_header, width=12,
                            command=choicefcw_w_button_clicked)

# DISPLAYING THE FIRST GUI BUTTON
start_button.grid(row=1, column=1, padx=50, pady=50)

# ENDING THE GUI CODE
window.mainloop()
