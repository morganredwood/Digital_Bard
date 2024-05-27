import pygame
from tkinter import *
pygame.init()
win = Tk()
win.geometry("972x565")
bardwithlute = PhotoImage(file="digitalbardbg.png")
lex = PhotoImage(file="LexFridman.png")
guido = PhotoImage(file="GuidovanRossum.png")
image_spot = Label(win, text="", width=972, height=565, bg="black")
image_spot.place(x=0, y=0)
background_image = Label(image_spot, image=bardwithlute, bg="black")
guido_image = Label(image_spot, image=guido, bg="black")
lex_image = Label(image_spot, image=lex, bg="black")
background_image.grid(row=1, column=1)
digitalbard_font = ("Lucida Calligraphy", 14)
selection1 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection2 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection3 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection4 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection5 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection6 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection7 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
selection8 = Label(win, bg="gray14", fg="gold", text="", width=12, font=digitalbard_font)
header1 = Label(win, bg="black", fg="gold", text="", font=digitalbard_font)
itw_i = Label(win, text="I", bg="black", fg="gold", font=digitalbard_font, justify="left")
itw_t = Label(win, text="They", bg="black", fg="gold", font=digitalbard_font, justify="left")
itw_w = Label(win, text="We", bg="black", fg="gold", font=digitalbard_font, justify="left")
ots_o = Label(win, text="Old", bg="black", fg="gold", font=digitalbard_font, justify="left")
ots_t = Label(win, text="Tall", bg="black", fg="gold", font=digitalbard_font, justify="left")
ots_s = Label(win, text="Sad", bg="black", fg="gold", font=digitalbard_font, justify="left")
lwt_l = Label(win, text="Leave", bg="black", fg="gold", font=digitalbard_font, justify="left")
lwt_w = Label(win, text="Watch", bg="black", fg="gold", font=digitalbard_font, justify="left")
lwt_t = Label(win, text="Trust", bg="black", fg="gold", font=digitalbard_font, justify="left")
jtf_j = Label(win, text="Johnny", bg="black", fg="gold", font=digitalbard_font, justify="left")
jtf_t = Label(win, text="Timmy", bg="black", fg="gold", font=digitalbard_font, justify="left")
jtf_f = Label(win, text="Frodo", bg="black", fg="gold", font=digitalbard_font, justify="left")
tntof_t = Label(win, text="Tomorrow", bg="black", fg="gold", font=digitalbard_font, justify="left")
tntof_nt = Label(win, text="Next Tuesday", bg="black", fg="gold", font=digitalbard_font, justify="left")
tntof_of = Label(win, text="On Friday", bg="black", fg="gold", font=digitalbard_font, justify="left")
pbf_p = Label(win, text="pay", bg="black", fg="gold", font=digitalbard_font, justify="left")
pbf_b = Label(win, text="bell", bg="black", fg="gold", font=digitalbard_font, justify="left")
pbf_f = Label(win, text="fish", bg="black", fg="gold", font=digitalbard_font, justify="left")
lsw_l = Label(win, text="long", bg="black", fg="gold", font=digitalbard_font, justify="left")
lsw_s = Label(win, text="short", bg="black", fg="gold", font=digitalbard_font, justify="left")
lsw_w = Label(win, text="wild", bg="black", fg="gold", font=digitalbard_font, justify="left")
fcw_f = Label(win, text="foul", bg="black", fg="gold", font=digitalbard_font, justify="left")
fcw_c = Label(win, text="cold", bg="black", fg="gold", font=digitalbard_font, justify="left")
fcw_w = Label(win, text="weird", bg="black", fg="gold", font=digitalbard_font, justify="left")


def gimme_my_song():
    button_gimme_my_song.destroy()
    playlist3("7")
    playlist9("23")
    playlist18("48")
    playlist25("65")
    playlist26("49")
    playlist35("91")
    playlist36("66")
    playlist45("117")
    playlist46("118")


def instructions():
    start.destroy()
    digitalbard_messages.config(text="You will be shown various song options in groups of three items.")
    digitalbard_messagesline2.config(text="You may choose one item from each group.")
    proceed.grid(row=1, column=1, padx=10, pady=10, sticky=W)


def letschoose_itw():
    proceed.destroy()
    digitalbard_messages.destroy()
    digitalbard_messagesline2.destroy()
    button_display("itw")


def button_display(name):
    if name == "itw":
        button_itw_i.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        itw_i.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_itw_t.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        itw_t.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_itw_w.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        itw_w.grid(row=3, column=3, padx=3, pady=3, sticky=W)
    if name == "ots":
        button_ots_o.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        ots_o.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_ots_t.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        ots_t.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_ots_s.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        ots_s.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "lwt":
        button_lwt_l.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        lwt_l.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_lwt_w.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        lwt_w.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_lwt_t.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        lwt_t.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "jtf":
        button_jtf_j.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        jtf_j.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_jtf_t.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        jtf_t.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_jtf_f.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        jtf_f.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "tntof":
        button_tntof_t.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        tntof_t.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_tntof_nt.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        tntof_nt.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_tntof_of.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        tntof_of.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "pbf":
        button_pbf_p.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        pbf_p.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_pbf_b.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        pbf_b.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_pbf_f.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        pbf_f.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "lsw":
        button_lsw_l.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        lsw_l.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_lsw_s.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        lsw_s.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_lsw_w.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        lsw_w.grid(row=3, column=3, padx=10, pady=10, sticky=W)
    if name == "fcw":
        button_fcw_f.grid(row=1, column=2, padx=10, pady=10, sticky=W)
        fcw_f.grid(row=1, column=3, padx=10, pady=10, sticky=W)
        button_fcw_c.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        fcw_c.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        button_fcw_w.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        fcw_w.grid(row=3, column=3, padx=10, pady=10, sticky=W)


def button_boom(name):
    if name == "itw":
        button_itw_i.destroy()
        button_itw_t.destroy()
        button_itw_w.destroy()
        itw_i.destroy()
        itw_t.destroy()
        itw_w.destroy()
    if name == "ots":
        button_ots_o.destroy()
        button_ots_t.destroy()
        button_ots_s.destroy()
        ots_o.destroy()
        ots_t.destroy()
        ots_s.destroy()
    if name == "lwt":
        button_lwt_l.destroy()
        button_lwt_w.destroy()
        button_lwt_t.destroy()
        lwt_l.destroy()
        lwt_w.destroy()
        lwt_t.destroy()
    if name == "jtf":
        button_jtf_j.destroy()
        button_jtf_t.destroy()
        button_jtf_f.destroy()
        jtf_j.destroy()
        jtf_t.destroy()
        jtf_f.destroy()
    if name == "pbf":
        button_pbf_p.destroy()
        button_pbf_b.destroy()
        button_pbf_f.destroy()
        pbf_p.destroy()
        pbf_b.destroy()
        pbf_f.destroy()
    if name == "tntof":
        button_tntof_t.destroy()
        button_tntof_nt.destroy()
        button_tntof_of.destroy()
        tntof_t.destroy()
        tntof_nt.destroy()
        tntof_of.destroy()
    if name == "lsw":
        button_lsw_l.destroy()
        button_lsw_s.destroy()
        button_lsw_w.destroy()
        lsw_l.destroy()
        lsw_s.destroy()
        lsw_w.destroy()
    if name == "fcw":
        button_fcw_f.destroy()
        button_fcw_c.destroy()
        button_fcw_w.destroy()
        fcw_f.destroy()
        fcw_c.destroy()
        fcw_w.destroy()
    if name == "thegrid":
        header1.destroy()
        selection1.destroy()
        selection2.destroy()
        selection3.destroy()
        selection4.destroy()
        selection5.destroy()
        selection6.destroy()
        selection7.destroy()
        selection8.destroy()
        button_heresyoursong.destroy()


def letschoose_itw_i():
    button_boom("itw")
    button_display("ots")
    selection1.config(text="I")
    cue1("I")


def letschoose_itw_t():
    button_boom("itw")
    button_display("ots")
    selection1.config(text="They")
    cue1("They")


def letschoose_itw_w():
    button_boom("itw")
    button_display("ots")
    selection1.config(text="We")
    cue1("We")


def letschoose_ots_o():
    button_boom("ots")
    button_display("lwt")
    selection2.config(text="Old")
    cue2("Old")


def letschoose_ots_t():
    button_boom("ots")
    button_display("lwt")
    selection2.config(text="Tall")
    cue2("Tall")


def letschoose_ots_s():
    button_boom("ots")
    button_display("lwt")
    selection2.config(text="Sad")
    cue2("Sad")


def letschoose_lwt_l():
    button_boom("lwt")
    button_display("jtf")
    selection3.config(text="Leave")
    cue3("Leave")


def letschoose_lwt_w():
    button_boom("lwt")
    button_display("jtf")
    selection3.config(text="Watch")
    cue3("Watch")


def letschoose_lwt_t():
    button_boom("lwt")
    button_display("jtf")
    selection3.config(text="Trust")
    cue3(choice="Trust")


def letschoose_jtf_j():
    button_boom("jtf")
    button_display("tntof")
    selection4.config(text="Johnny")
    cue4(choice="Johnny")


def letschoose_jtf_t():
    button_boom("jtf")
    button_display("tntof")
    selection4.config(text="Timmy")
    cue4(choice="Timmy")


def letschoose_jtf_f():
    button_boom("jtf")
    button_display("tntof")
    selection4.config(text="Frodo")
    cue4(choice="Frodo")


def letschoosetntof_t():
    button_boom("tntof")
    button_display("pbf")
    selection5.config(text="Tomorrow")
    cue5(choice="Tomorrow")


def letschoosetntof_nt():
    button_boom("tntof")
    button_display("pbf")
    selection5.config(text="Next Tuesday")
    cue5(choice="Next Tuesday")


def letschoosetntof_of():
    button_boom("tntof")
    button_display("pbf")
    selection5.config(text="On Friday")
    cue5(choice="On Friday")


def letschoosepbf_p():
    button_boom("pbf")
    button_display("lsw")
    selection6.config(text="Pay")
    cue6(choice="Pay")


def letschoosepbf_b():
    button_boom("pbf")
    button_display("lsw")
    selection6.config(text="Bell")
    cue6(choice="Bell")


def letschoosepbf_f():
    button_boom("pbf")
    button_display("lsw")
    selection6.config(text="Fish")
    cue6(choice="Fish")


def letschooselsw_l():
    button_boom("lsw")
    button_display("fcw")
    selection7.config(text="Long")
    cue7(choice="Long")


def letschooselsw_s():
    button_boom("lsw")
    button_display("fcw")
    selection7.config(text="Short")
    cue7(choice="Short")


def letschooselsw_w():
    button_boom("lsw")
    button_display("fcw")
    selection7.config(text="Wild")
    cue7(choice="Short")


def letschoosefcw_f():
    button_boom("fcw")
    selection8.config(text="Foul")
    cue8(choice="Foul")
    herewego()


def interview():
    int1 = pygame.mixer.Sound("interview01.mp3").play()
    while True:
        if not int1.get_busy():
            break
        else:
            continue
    int2 = pygame.mixer.Sound("interview02.mp3").play()
    while True:
        if not int2.get_busy():
            break
        else:
            continue
    int3 = pygame.mixer.Sound("interview03.mp3").play()
    while True:
        if not int3.get_busy():            
            break
        else:
            continue
    int4 = pygame.mixer.Sound("interview04.mp3").play()
    while True:
        if not int4.get_busy():            
            break
        else:
            continue
    int5 = pygame.mixer.Sound("interview05.mp3").play()
    while True:
        if not int5.get_busy():            
            break
        else:
            continue
    button_gimme_my_song.grid(row=1, column=1, padx=10, pady=10, sticky=W)


def letschoosefcw_c():
    button_boom("fcw")
    selection8.config(text="Cold")
    cue8(choice="Cold")
    herewego()


def herewego():
    header1.config(text="Here are the selections you made:")
    header1.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    selection1.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    selection2.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    selection3.grid(row=5, column=1, padx=10, pady=10, sticky=W)
    selection4.grid(row=6, column=1, padx=10, pady=10, sticky=W)
    selection5.grid(row=7, column=1, padx=10, pady=10, sticky=W)
    selection6.grid(row=8, column=1, padx=10, pady=10, sticky=W)
    selection7.grid(row=9, column=1, padx=10, pady=10, sticky=W)
    selection8.grid(row=10, column=1, padx=10, pady=10, sticky=W)
    button_heresyoursong.grid(row=2, column=0, padx=10, pady=10, sticky=W)


def letschoosefcw_w():
    button_boom("fcw")
    selection8.config(text="Weird")
    cue8(choice="Weird")
    herewego()


def playlist1(track):
    if track == "1":
        bigfinale("I thought I heard")
    if track == "2":
        bigfinale("They thought they heard")
    if track == "3":
        bigfinale("We thought we heard")


def playlist2(track):
    if track == "4":
        bigfinale("The Old")
    if track == "5":
        bigfinale("The Tall")
    if track == "6":
        bigfinale("The Sad")


def playlist3(track):
    if track == "7":
        bigfinale("Man say")


def playlist4(track):
    if track == "8":
        bigfinale("Leave her 1")
    if track == "9":
        bigfinale("Watch her 1")
    if track == "10":
        bigfinale("Trust her 1")


def playlist5(track):
    if track == "11":
        bigfinale("Johnny 1")
    if track == "12":
        bigfinale("Timmy 1")
    if track == "13":
        bigfinale("Frodo 1")


def playlist6(track):
    if track == "14":
        bigfinale("Leave her 2")
    if track == "15":
        bigfinale("Watch her 2")
    if track == "16":
        bigfinale("Trust her 2")


def playlist7(track):
    if track == "17":
        bigfinale("Tomorrow, ye will")
    if track == "18":
        bigfinale("Next Tuesday, ye will")
    if track == "19":
        bigfinale("On Friday, ye will")


def playlist8(track):
    if track == "20":
        bigfinale("Get your pay")
    if track == "21":
        bigfinale("Get your bell")
    if track == "22":
        bigfinale("Get your fish")


def playlist9(track):
    if track == "23":
        bigfinale("And it's time for us")


def playlist10(track):
    if track == "24":
        bigfinale("To leave her")
    if track == "25":
        bigfinale("To watch her")
    if track == "26":
        bigfinale("To trust her")


def playlist11(track):
    if track == "27":
        bigfinale("Leave her 1")
    if track == "28":
        bigfinale("Watch her 1")
    if track == "29":
        bigfinale("Trust her 1")


def playlist12(track):
    if track == "30":
        bigfinale("Johnny 1")
    if track == "31":
        bigfinale("Timmy 1")
    if track == "32":
        bigfinale("Frodo 1")


def playlist13(track):
    if track == "33":
        bigfinale("Leave her 2")
    if track == "34":
        bigfinale("Watch her 2")
    if track == "35":
        bigfinale("Trust her 2")


def playlist14(track):
    if track == "36":
        bigfinale("Oh, leave her")
    if track == "37":
        bigfinale("Oh, watch her")
    if track == "38":
        bigfinale("Oh, trust her")


def playlist15(track):
    if track == "39":
        bigfinale("Johnny 2")
    if track == "40":
        bigfinale("Timmy 2")
    if track == "41":
        bigfinale("Frodo 2")


def playlist16(track):
    if track == "42":
        bigfinale("Leave her 3")
    if track == "43":
        bigfinale("Watch her 3")
    if track == "44":
        bigfinale("Trust her 3")


def playlist17(track):
    if track == "45":
        bigfinale("For the voyage is long")
    if track == "46":
        bigfinale("For the voyage is short")
    if track == "47":
        bigfinale("For the voyage is weird")


def playlist18(track):
    if track == "48":
        bigfinale("And the winds don't blow")


def playlist19(track):
    if track == "49":
        bigfinale("And it's time for us")


def playlist20(track):
    if track == "50":
        bigfinale("To leave her")
    if track == "51":
        bigfinale("To watch her")
    if track == "52":
        bigfinale("To trust her")


def playlist21(track):
    if track == "53":
        bigfinale("Oh, the wind was foul, and the sea ran high")
    if track == "54":
        bigfinale("Oh, the wind was cold, and the sea ran high")
    if track == "55":
        bigfinale("Oh, the wind was weird, and the sea ran high")


def playlist22(track):
    if track == "56":
        bigfinale("Leave her 1")
    if track == "57":
        bigfinale("Watch her 1")
    if track == "58":
        bigfinale("Trust her 1")


def playlist23(track):
    if track == "59":
        bigfinale("Johnny 1")
    if track == "60":
        bigfinale("Timmy 1")
    if track == "61":
        bigfinale("Frodo 1")


def playlist24(track):
    if track == "62":
        bigfinale("Leave her 2")
    if track == "63":
        bigfinale("Watch her 2")
    if track == "64":
        bigfinale("Trust her 2")


def playlist25(track):
    if track == "65":
        bigfinale("She shipped it green, and none went by")


def playlist26(track):
    if track == "66":
        bigfinale("And it's time for us")


def playlist27(track):
    if track == "67":
        bigfinale("To leave her")
    if track == "68":
        bigfinale("To watch her")
    if track == "69":
        bigfinale("To trust her")


def playlist28(track):
    if track == "70":
        bigfinale("Leave her 1")
    if track == "71":
        bigfinale("Watch her 1")
    if track == "72":
        bigfinale("Trust her 1")


def playlist29(track):
    if track == "73":
        bigfinale("Johnny 1")
    if track == "74":
        bigfinale("Timmy 1")
    if track == "75":
        bigfinale("Frodo 1")


def playlist30(track):
    if track == "76":
        bigfinale("Leave her 2")
    if track == "77":
        bigfinale("Watch her 2")
    if track == "78":
        bigfinale("Trust her 2")


def playlist31(track):
    if track == "79":
        bigfinale("Oh, leave her")
    if track == "80":
        bigfinale("Oh, watch her")
    if track == "81":
        bigfinale("Oh, trust her")


def playlist32(track):
    if track == "82":
        bigfinale("Johnny 2")
    if track == "83":
        bigfinale("Timmy 2")
    if track == "84":
        bigfinale("Frodo 2")


def playlist33(track):
    if track == "85":
        bigfinale("Leave her 3")
    if track == "86":
        bigfinale("Watch her 3")
    if track == "87":
        bigfinale("Trust her 3")


def playlist34(track):
    if track == "88":
        bigfinale("For the voyage is long")
    if track == "89":
        bigfinale("For the voyage is short")
    if track == "90":
        bigfinale("For the voyage is wild")


def playlist35(track):
    if track == "91":
        bigfinale("And the winds don't blow")


def playlist36(track):
    if track == "92":
        bigfinale("And it's time for us")


def playlist37(track):
    if track == "93":
        bigfinale("To leave her")
    if track == "94":
        bigfinale("To watch her")
    if track == "95":
        bigfinale("To trust her")


def playlist38(track):
    if track == "96":
        bigfinale("Leave her 1")
    if track == "97":
        bigfinale("Watch her 1")
    if track == "98":
        bigfinale("Trust her 1")


def playlist39(track):
    if track == "99":
        bigfinale("Johnny 1")
    if track == "100":
        bigfinale("Timmy 1")
    if track == "101":
        bigfinale("Frodo 1")


def playlist40(track):
    if track == "102":
        bigfinale("Leave her 2")
    if track == "103":
        bigfinale("Watch her 2")
    if track == "104":
        bigfinale("Trust her 2")


def playlist41(track):
    if track == "105":
        bigfinale("Oh, leave her")
    if track == "106":
        bigfinale("Oh, watch her")
    if track == "107":
        bigfinale("Oh, trust her")


def playlist42(track):
    if track == "108":
        bigfinale("Johnny 2")
    if track == "109":
        bigfinale("Timmy 2")
    if track == "110":
        bigfinale("Frodo 2")


def playlist43(track):
    if track == "111":
        bigfinale("Leave her 3")
    if track == "112":
        bigfinale("Watch her 3")
    if track == "113":
        bigfinale("Trust her 3")


def playlist44(track):
    if track == "114":
        bigfinale("For the voyage is long")
    if track == "115":
        bigfinale("For the voyage is short")
    if track == "116":
        bigfinale("For the voyage is wild")


def playlist45(track):
    if track == "117":
        bigfinale("And the winds don't blow")


def playlist46(track):
    if track == "118":
        bigfinale("And it's time for us")


def playlist47(track):
    if track == "119":
        bigfinale("To leave her")
    if track == "120":
        bigfinale("To watch her")
    if track == "121":
        bigfinale("To watch her")


def bigfinale(track="I thought I heard",
              track="They they they heard",
              track ="We thought we heard",
              track="The Old",
              track="The Tall",
              track="The Sad",
              track="Man say",
              track="Leave her 1",
              track="Watch her 1",
              track="Trust her 1",
              track="Johnny 1",
              track="Timmy 1",
              track="Frodo 1",
              track="Leave her 2",
              track="Watch her 2",
              track="Trust her 2",
              track="Tomorrow, ye will",
              track="Next Tuesday, ye will",
              track="On Friday, ye will",
              track="Get your pay",
              track="Get your bell",
              track="Get your fish",
              track="And it's time for us",
              track="To leave her",
              track="To watch her",
              track="To trust her",
              track="Oh, leave her",
              track="Oh, watch her",
              track="Oh, trust her",
              track="For the voyage is long",
              track="For the voyage is short",
              track="For the voyage is wild",
              track="Oh, the wind was foul, and the sea ran high",
              track="Oh, the wind was cold, and the sea ran high",
              track="Oh, the wind was weird, and the sea ran high",
              track="She shipped it green, and none went by"):
    if track == "I thought I heard":
        part("1")
    if track == "They thought they heard":
        part("2")
    if track

def part(track):
    if part == "1":
        pygame.mixer.music.load("itih.mp3")
        pygame.mixer.music.play()
    if part == "2":
        pygame.mixer.music.load("ttth.mp3")
        pygame.mixer.music.play()
    if part == "3":
        pygame.mixer.music.load("wtwh.mp3")
        pygame.mixer.music.play()
    if part == "4":
        pygame.mixer.music.queue("to.mp3")
    if part == "5":
        pygame.mixer.music.queue("tt.mp3")
    if part == "6":
        pygame.mixer.music.load("ts.mp3")
    if part == "7":
        pygame.mixer.music.queue("ms.mp3")
    if part == "8":
        pygame.mixer.music.queue("lher_one.mp3")
    if part == "9":
        pygame.mixer.music.queue("wher_one.mp3")
    if part == "10":
        pygame.mixer.music.queue("trher_one.mp3")
    if part == "11":
        pygame.mixer.music.queue("johnny_one.mp3")
    if part == "12":
        pygame.mixer.music.queue("timmy_one.mp3")
    if part == "13":
        pygame.mixer.music.queue("frodo_one.mp3")            
    if part == "14":
        pygame.mixer.music.queue("lher_two.mp3")            
    if part == "15":
        pygame.mixer.music.queue("wher_two.mp3")            
    if part == "16":
        pygame.mixer.music.queue("trher_two.mp3")            
    if track == "Tomorrow, ye will":
        pygame.mixer.music.queue("tyw.mp3")            
    if track == "Next Tuesday, ye will":
        pygame.mixer.music.queue("ntyw.mp3")            
    if track == "On Friday, ye will":
        pygame.mixer.music.queue("ofyw.mp3")            
    if track == "Get your pay":
        pygame.mixer.music.queue("getyp.mp3")            
    if track == "Get your bell":
        pygame.mixer.music.queue("getyb.mp3")            
    if track == "Get your fish":
        pygame.mixer.music.queue("getyf.mp3")            
    if track == "And it's time for us":
        pygame.mixer.music.queue("aitfu.mp3")            
    if track == "To leave her":
        pygame.mixer.music.queue("tlher_one.mp3")            
    if track == "To watch her":
        pygame.mixer.music.queue("twher_one.mp3")            
    if track == "To trust her":
        pygame.mixer.music.queue("ttrher_one.mp3")            
    if track == "Leave her 1":
        pygame.mixer.music.queue("lher_one.mp3")
    if track == "Watch her 1":
        pygame.mixer.music.queue("wher_one.mp3")
    if track == "Trust her 1":
        pygame.mixer.music.queue("trher_one.mp3")            
    if track == "Johnny 1":
        pygame.mixer.music.queue("johnny_one.mp3")            
    if track == "Timmy 1":
        pygame.mixer.music.queue("timmy_one.mp3")            
    if track == "Frodo 1":
        pygame.mixer.music.queue("frodo_one.mp3")            
    if track == "Leave her 2":
        pygame.mixer.music.queue("lher_two.mp3")            
    if track == "Watch her 2":
        pygame.mixer.music.queue("wher_two.mp3")            
    if track == "Trust her 2":
        pygame.mixer.music.queue("trher_two.mp3")            
    if track == "Oh, leave her":
        pygame.mixer.music.queue("olher_one.mp3")            
    if track == "Oh, watch her":
        pygame.mixer.music.queue("olher_one.mp3")            
    if track == "Oh, trust her":
        pygame.mixer.music.queue("olher_one.mp3")            
    if track == "Johnny 2":
        pygame.mixer.music.queue("johnny_two.mp3")            
    if track == "Timmy 2":
        pygame.mixer.music.queue("timmy_two.mp3")            
    if track == "Frodo 2":
        pygame.mixer.music.queue("frodo_two.mp3")            
    if track == "Leave her 3":
        pygame.mixer.music.queue("lher_three.mp3")            
    if track == "Watch her 3":
        pygame.mixer.music.queue("wher_three.mp3")            
    if track == "Trust her 3":
        pygame.mixer.music.queue("trher_three.mp3")            
    if track == "For the voyage is long":
        pygame.mixer.music.queue("ftvil.mp3")            
    if track == "For the voyage is short":
        pygame.mixer.music.queue("ftvis.mp3")            
    if track == "For the voyage is wild":
        pygame.mixer.music.queue("ftviw.mp3")            
    if track == "And he winds don't blow":
        pygame.mixer.music.queue("atwdb.mp3")            
    if track == "And it's time for us":
        pygame.mixer.music.queue("aitfu.mp3")            
    if track == "To leave her":
        pygame.mixer.music.queue("tlher_one.mp3 ")            
    if track == "To watch her":
        pygame.mixer.music.queue("twher_one.mp3")            
    if track == "To trust her":
        pygame.mixer.music.queue("ttrher_one.mp3")            
    if track == "Oh, the wind was foul, and the sea ran high":
        pygame.mixer.music.queue("otwwfatsrh.mp3")            
    if track == "Oh, the wind was wild, and the sea ran high":
        pygame.mixer.music.queue("otwwcatsrh.mp3")            
    if track == "Oh, the wind was weird, and the sea ran high":
        pygame.mixer.music.queue("otwwwatsrh.mp3")            
    if track == "Leave her 1":
        pygame.mixer.music.queue("lher_one.mp3")            
    if track == "Watch her 1":
        pygame.mixer.music.queue("wher_one.mp3")            
    if track == "Trust her 1":
        pygame.mixer.music.queue("trher_one.mp3")            
    if track == "Johnny 1":
        pygame.mixer.music.queue("johnny_one.mp3")            
    if track == "Timmy 1":
        pygame.mixer.music.queue("timmy_one.mp3")            
    if track == "Frodo 1":
        pygame.mixer.music.queue("frodo_one.mp3")            
    if track == "Leave her 2":
        pygame.mixer.music.queue("lher_two.mp3")            
    if track == "Watch her 2":
        pygame.mixer.music.queue("wher_two.mp3")            
    if track == "Trust her 2":
        pygame.mixer.music.queue("trher_two.mp3")            
    if track == "She shipped it green, and none went by":
        pygame.mixer.music.queue("ssiganwb.mp3")            
    if track == "And it's time for us":
        pygame.mixer.music.queue("aitfu.mp3")            
    if track == "To leave her":
        pygame.mixer.music.queue("tlher_one.mp3")            
    if track == "To watch her":
        pygame.mixer.music.queue("twher_one.mp3")            
    if track == "To trust her":
        pygame.mixer.music.queue("ttrher_one.mp3")            
    if track == "Leave her 1":
        pygame.mixer.music.queue("lher_one.mp3")            
    if track == "Watch her 1":
        pygame.mixer.music.queue("wher_one.mp3")            
    if track == "Trust her 1":
        pygame.mixer.music.queue("trher_one.mp3")            
    if track == "Johnny 1":
        pygame.mixer.music.queue("johnny_one.mp3")            
    if track == "Timmy 1":
        pygame.mixer.music.queue("timmy_one.mp3")            
    if track == "Frodo 1":
        pygame.mixer.music.queue("frodo_one.mp3")            
    if track == "Leave her 2":
        pygame.mixer.music.queue("lher_two.mp3")            
    if track == "Watch her 2":
        pygame.mixer.music.queue("wher_two.mp3")            
    if track == "Trust her 2":
        pygame.mixer.music.queue("trher_two.mp3")            
    if track == "Oh, leave her":
        pygame.mixer.music.queue("olher_one.mp3")            
    if track == "Oh, watch her":
        pygame.mixer.music.queue("owher_one.mp3")            
    if track == "Oh, trust her":
        pygame.mixer.music.queue("otrher_one.mp3")            
    if track == "Johnny 2":
        pygame.mixer.music.queue("johnny_two.mp3")            
    if track == "Timmy 2":
        pygame.mixer.music.queue("timmy_two.mp3")            
    if track == "Frodo 2":
        pygame.mixer.music.queue("frodo_two.mp3")            
    if track == "Leave her 3":
        pygame.mixer.music.queue("lher_three.mp3")            
    if track == "Watch her 3":
        pygame.mixer.music.queue("wher_three.mp3")            
    if track == "Trust her 3":
        pygame.mixer.music.queue("trher_three.mp3")            
    if track == "For the voyage is long":
        pygame.mixer.music.queue("ftvil.mp3")            
    if track == "For the voyage is short":
        pygame.mixer.music.queue("ftvis.mp3")            
    if track == "For the voyage is wild":
        pygame.mixer.music.queue("ftviw.mp3")            
    if track == "And the winds don't blow":
        pygame.mixer.music.queue("atwdb.mp3")            
    if track == "And it's time for us":
        pygame.mixer.music.queue("aitfu.mp3")            
    if track == "To leave her":
        pygame.mixer.music.queue("tlher_one.mp3 ")            
    if track == "To watch her":
        pygame.mixer.music.queue("twher_one.mp3")            
    if track == "To trust her":
        pygame.mixer.music.queue("ttrher_one.mp3")            
    if track == "Leave her 1":
        pygame.mixer.music.queue("lher_one.mp3")            
    if track == "Watch her 1":
        pygame.mixer.music.queue("wher_one.mp3")            
    if track == "Trust her 1":
        pygame.mixer.music.queue("trher_one.mp3")            
    if track == "Johnny 1":
        pygame.mixer.music.queue("johnny_one.mp3")            
    if track == "Timmy 1":
        pygame.mixer.music.queue("timmy_one.mp3")            
    if track == "Frodo 1":
        pygame.mixer.music.queue("frodo_one.mp3")            
    if track == "Leave her 2":
        pygame.mixer.music.queue("lher_two.mp3")            
    if track == "Watch her 2":
        pygame.mixer.music.queue("wher_two.mp3")            
    if track == "Trust her 2":
        pygame.mixer.music.queue("trher_two.mp3")            
    if track == "Oh, leave her":
        pygame.mixer.music.queue("olher_one.mp3")            
    if track == "Oh, watch her":
        pygame.mixer.music.queue("owher_one.mp3")            
    if track == "Oh, trust her":
        pygame.mixer.music.queue("otrher_one.mp3")            
    if track == "Johnny 2":
        pygame.mixer.music.queue("johnny_two.mp3")            
    if track == "Timmy 2":
        pygame.mixer.music.queue("timmy_two.mp3")            
    if track == "Frodo 2":
        pygame.mixer.music.queue("frodo_two.mp3")            
    if track == "Leave her 3":
        pygame.mixer.music.queue("lher_three.mp3")            
    if track == "Watch her 3":
        pygame.mixer.music.queue("wher_three.mp3")            
    if track == "Trust her 3":
        pygame.mixer.music.queue("trher_three.mp3")            
    if track == "For the voyage is long":
        pygame.mixer.music.queue("ftvil.mp3")            
    if track == "For the voyage is short":
        pygame.mixer.music.queue("ftvis.mp3")            
    if track == "For he voyage is wild":
        pygame.mixer.music.queue("ftviw.mp3")            
    if track == "And the winds don't blow":
        pygame.mixer.music.queue("atwdb.mp3")            
    if track == "And it's time for us":
        pygame.mixer.music.queue("aitfu.mp3")            
    if track == "To leave her":
        pygame.mixer.music.queue("tlher_one.mp3")            
    if track == "To watch her":
        pygame.mixer.music.queue("twher_one.mp3")
    if track == "To trust her":
        pygame.mixer.music.queue("ttrher_one.mp3")


def cue1(choice):
    if choice == "I":
        playlist1("1")
    if choice == "They":
        playlist1("2")
    if choice == "We":
        playlist1("3")


def cue2(choice):
    if choice == "Old":
        playlist2("4")
    if choice == "Tall":
        playlist2("5")
    if choice == "Sad":
        playlist2("6")


def cue3(choice):
    if choice == "Leave":
        playlist3("7")
    if choice == "Watch":
        playlist3("8")
    if choice == "Trust":
        playlist3("9")


def cue4(choice):
    if choice == "Johnny":
        playlist4("10")
    if choice == "Timmy":
        playlist4("11")
    if choice == "Frodo":
        playlist4("12")


def cue5(choice):
    if choice == "Tomorrow":
        playlist5("13")
    if choice == "Next Tuesday":
        playlist5("13")
    if choice == "On Friday":
        playlist5("14")


def cue6(choice):
    if choice == "Pay":
        playlist6("15")
    if choice == "Bell":
        playlist6("16")
    if choice == "Fish":
        playlist6("17")


def cue7(choice):
    if choice == "Long":
        playlist7("18")
    if choice == "Short":
        playlist7("19")
    if choice == "Wild":
        playlist7("20")


def cue8(choice):
    if choice == "Foul":
        playlist8("21")
    if choice == "Cold":
        playlist8("22")
    if choice == "Wild":
        playlist8("23")


def heresyourlist():
    button_boom("thegrid")
    button_heresyoursong.destroy()
    button_continueonemore.grid(row=1, column=1, padx=10, pady=10, sticky=W)
# When you click Continue after the video
    lex_image.grid(row=1, column=0)
    guido_image.grid(row=1, column=1)


def cuethevideo():
    button_continueonemore.destroy()
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.unload()
    interview()
# Makes you watch the video


button_itw_i = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoose_itw_i)
button_itw_t = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoose_itw_t)
button_itw_w = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschoose_itw_w)
button_ots_o = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoose_ots_o)
button_ots_t = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoose_ots_t)
button_ots_s = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschoose_ots_s)
button_lwt_l = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoose_lwt_l)
button_lwt_w = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoose_lwt_w)
button_lwt_t = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3",  command=letschoose_lwt_t)
button_jtf_j = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoose_jtf_j)
button_jtf_t = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoose_jtf_t)
button_jtf_f = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschoose_jtf_f)
button_tntof_t = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1",
                        command=letschoosetntof_t)
button_tntof_nt = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2",
                         command=letschoosetntof_nt)
button_tntof_of = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3",
                         command=letschoosetntof_of)
button_pbf_p = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoosepbf_p)
button_pbf_b = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoosepbf_b)
button_pbf_f = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschoosepbf_f)
button_lsw_l = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschooselsw_l)
button_lsw_s = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschooselsw_s)
button_lsw_w = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschooselsw_w)
button_fcw_f = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="1", command=letschoosefcw_f)
button_fcw_c = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="2", command=letschoosefcw_c)
button_fcw_w = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="3", command=letschoosefcw_w)
button_heresyoursong = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                              command=heresyourlist)
button_continueonemore = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                                command=cuethevideo)
button_gimme_my_song = Button(win, bg="forest green", fg="black", font=digitalbard_font,
                              text="Listen to your customized song", command=gimme_my_song)
# print("Photo by Kostiantyn Klymovets: https://www.pexels.com/photo/man-playing-lute-on-urban-steps-12831481/")
digitalbard_messages = Label(win, bg="black", text="", font=digitalbard_font, fg="gold")
pygame.mixer.music.load("scarborough_fair.mp3")
pygame.mixer.music.play(-1)
digitalbard_messages.config(text="Welcome to your free trial of Digital Bard.")
digitalbard_messagesline2 = Label(win,
                                  bg="black", text="Please enjoy this sample from our sea shanty collection.",
                                  font=digitalbard_font, fg="gold")
digitalbard_messages.grid(row=2, column=1, padx=10, pady=10, sticky=W)
digitalbard_messagesline2.grid(row=3, column=1, padx=10, pady=10, sticky=W)
proceed = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                 command=letschoose_itw)
start = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Start", width=5, command=instructions)
start.grid(row=1, column=1, padx=10, pady=10, sticky=W)
win.mainloop()
