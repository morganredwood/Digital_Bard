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
    pygame.mixer.music.fadeout(1000)
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
    button_gimme_my_song.grid(row=9, column=1, padx=10, pady=10, sticky=W)


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


def clip(soundfile):
    while True:
        while True:
            if soundfile == "01":
                play = pygame.mixer.Sound("interview01.mp3").play()
                break
            if soundfile == "02":
                play = pygame.mixer.Sound("interview02.mp3").play()
                break
            if soundfile == "03":
                play = pygame.mixer.Sound("interview03.mp3").play()
                break
            if soundfile == "04":
                play = pygame.mixer.Sound("interview04.mp3").play()
                break
            if soundfile == "05":
                play = pygame.mixer.Sound("interview05.mp3").play()
                break
        while True:
            if not play.get_busy():
                break
            else:
                continue


def cue1(choice):
    while True:
        if choice == "I":
            line1 = "I thought I heard"
            break
        if choice == "They":
            line1 = "They thought they heard"
            break
        if choice == "We":
            line1 = "We thought we heard"
            break
    print(line1)
    playlist(track1=line1, track2="", track3="", track4="", track5="", track6="", track7="",
             track8="", track9="", track10="", track11="", track12="", track13="", track14="",
             track15="", track16="", track17="", track18="", track19="", track20="", track21="",
             track22="", track23="", track24="", track25="", track26="", track27="", track28="",
             track29="", track30="", track31="", track32="", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="", track40="", track41="", track42="",
             track43="", track44="", track45="", track46="", track47="")


def cue2(choice):
    while True:
        if choice == "Old":
            line2 = "The Old"
            break
        if choice == "Tall":
            line2 = "The Tall"
            break
        if choice == "Sad":
            line2 = "The Sad"
            break
    line3 = "Man say"
    print(line2)
    print(line3)
    playlist(track1="", track2="line2", track3="line3", track4="", track5="", track6="", track7="",
             track8="", track9="", track10="", track11="", track12="", track13="", track14="",
             track15="", track16="", track17="", track18="", track19="", track20="", track21="",
             track22="", track23="", track24="", track25="", track26="", track27="", track28="",
             track29="", track30="", track31="", track32="", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="", track40="", track41="", track42="",
             track43="", track44="", track45="", track46="", track47="")


def cue3(choice):
    while True:
        if choice == "Leave":
            line4 = "Leave her 1"
            line6 = "Leave her 2"
            line10 = "To leave her"
            line11 = "Leave her 1"
            line13 = "Leave her 2"
            line14 = "Oh, leave her"
            line16 = "Leave her 3"
            line20 = "To leave her"
            line22 = "Leave her 1"
            line24 = "Leave her 2"
            line27 = "To leave her"
            line28 = "Leave her 1"
            line30 = "Leave her 2"
            line31 = "Oh, leave her"
            line33 = "Leave her 3"
            line37 = "To leave her"
            line38 = "Leave her 1"
            line40 = "Leave her 2"
            line41 = "Oh, leave her"
            line43 = "Leave her 3"
            line47 = "To leave her"
            break
        if choice == "Watch":
            line4 = "Watch her 1"
            line6 = "Watch her 2"
            line10 = "To watch her"
            line11 = "Watch her 1"
            line13 = "Watch her 2"
            line14 = "Oh, watch her"
            line16 = "Watch her 3"
            line20 = "To watch her"
            line22 = "Watch her 1"
            line24 = "Watch her 2"
            line27 = "To watch her"
            line28 = "Watch her 1"
            line30 = "Watch her 2"
            line31 = "Oh, watch her"
            line33 = "Watch her 3"
            line37 = "To watch her"
            line38 = "Watch her 1"
            line40 = "Watch her 2"
            line41 = "Oh, watch her"
            line43 = "Watch her 3"
            line47 = "To watch her"
            break
        if choice == "Trust":
            line4 = "Trust her 1"
            line6 = "Trust her 2"
            line10 = "To trust her"
            line11 = "Trust her 1"
            line13 = "Trust her 2"
            line14 = "Oh, trust her"
            line16 = "Trust her 3"
            line20 = "To trust her"
            line22 = "Trust her 1"
            line24 = "Trust her 2"
            line27 = "To trust her"
            line28 = "Trust her 1"
            line30 = "Trust her 2"
            line31 = "Oh, trust her"
            line33 = "Trust her 3"
            line37 = "To trust her"
            line38 = "Trust her 1"
            line40 = "Trust her 2"
            line41 = "Oh, trust her"
            line43 = "Trust her 3"
            line47 = "To trust her"
            break
    line9 = "And it's time for us"
    line18 = "And the winds don't blow"
    line19 = "And it's time for us"
    line25 = "She shipped it green, and none went by"
    line26 = "And it's time for us"
    line36 = "And it's time for us"
    line46 = "And it's time for us"
    print(line4)
    print(line6)
    print(line9)
    print(line10)
    print(line11)
    print(line13)
    print(line14)
    print(line16)
    print(line18)
    print(line19)
    print(line20)
    print(line22)
    print(line24)
    print(line25)
    print(line26)
    print(line27)
    print(line28)
    print(line30)
    print(line31)
    print(line33)
    print(line36)
    print(line37)
    print(line38)
    print(line40)
    print(line41)
    print(line43)
    print(line46)
    print(line47)
    playlist(track1="", track2="", track3="", track4="line4", track5="",
             track6="line6", track7="", track8="", track9="line9", track10="line10",
             track11="line11", track12="", track13="line13", track14="line14", track15="",
             track16="line16", track17="line17", track18="", track19="line19", track20="line20",
             track21="", track22="line22", track23="", track24="line24", track25="line25",
             track26="line26", track27="line27", track28="line28", track29="", track30="line30",
             track31="line31", track32="", track33="line33", track34="", track35="",
             track36="line36", track37="line37", track38="line38", track39="", track40="line40",
             track41="line41", track42="", track43="line43", track44="", track45="",
             track46="line46", track47="line47")


def cue4(choice):
    while True:
        if choice == "Johnny":
            line5 = "Johnny 1"
            line12 = "Johnny 1"
            line15 = "Johnny 2"
            line23 = "Johnny 1"
            line29 = "Johnny 1"
            line32 = "Johnny 1"
            line39 = "Johnny 2"
            line42 = "Johnny 1"
            break
        if choice == "Timmy":
            line5 = "Timmy 1"
            line12 = "Timmy 1"
            line15 = "Timmy 2"
            line23 = "Timmy 1"
            line29 = "Timmy 1"
            line32 = "Timmy 1"
            line39 = "Timmy 2"
            line42 = "Timmy 1"
            break
        if choice == "Frodo":
            line5 = "Frodo 1"
            line12 = "Frodo 1"
            line15 = "Frodo 2"
            line23 = "Frodo 1"
            line29 = "Frodo 1"
            line32 = "Frodo 1"
            line39 = "Frodo 2"
            line42 = "Frodo 1"
            break
    print(line5)
    print(line12)
    print(line15)
    print(line23)
    print(line29)
    print(line32)
    print(line39)
    print(line42)
    playlist(track1="", track2="", track3="", track4="", track5="line5",
             track6="", track7="", track8="", track9="", track10="",
             track11="", track12="line12", track13="", track14="", track15="line15",
             track16="", track17="", track18="", track19="", track20="",
             track21="", track22="", track23="line23", track24="", track25="",
             track26="", track27="", track28="", track29="line29", track30="",
             track31="", track32="line32", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="line39", track40="",
             track41="", track42="line42", track43="", track44="", track45="",
             track46="", track47="")


def cue5(choice):
    while True:
        if choice == "Tomorrow":
            line7 = "Tomorrow, ye will"
            break
        if choice == "Next Tuesday":
            line7 = "Next Tuesday, ye will"
            break
        if choice == "On Friday":
            line7 = "On Friday, ye will"
            break
    print(line7)
    playlist(track1="", track2="", track3="", track4="", track5="",
             track6="", track7="line7", track8="", track9="", track10="",
             track11="", track12="", track13="", track14="", track15="",
             track16="", track17="", track18="", track19="", track20="",
             track21="", track22="", track23="", track24="", track25="",
             track26="", track27="", track28="", track29="", track30="",
             track31="", track32="", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="", track40="",
             track41="", track42="", track43="", track44="", track45="",
             track46="", track47="")


def cue6(choice):
    while True:
        if choice == "Pay":
            line8 = "Get your pay"
            break
        if choice == "Bell":
            line8 = "Get your bell"
            break
        if choice == "Fish":
            line8 = "Get your fish"
            break
    print(line8)
    playlist(track1="", track2="", track3="", track4="", track5="",
             track6="", track7="", track8="line8", track9="", track10="",
             track11="", track12="", track13="", track14="", track15="",
             track16="", track17="", track18="", track19="", track20="",
             track21="", track22="", track23="", track24="", track25="",
             track26="", track27="", track28="", track29="", track30="",
             track31="", track32="", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="", track40="",
             track41="", track42="", track43="", track44="", track45="",
             track46="", track47="")


def cue7(choice):
    while True:
        if choice == "Long":
            line17 = "For the voyage is long"
            line18 = "And the winds don't blow"
            line34 = "For the voyage is long"
            line35 = "And the winds don't blow"
            line44 = "For the voyage is long"
            line45 = "And the winds don't blow"
            break
        if choice == "Short":
            line17 = "For the voyage is short"
            line18 = "And the winds don't blow"
            line34 = "For the voyage is short"
            line35 = "And the winds don't blow"
            line44 = "For the voyage is short"
            line45 = "And the winds don't blow"
            break
        if choice == "Wild":
            line17 = "For the voyage is wild"
            line18 = "And the winds don't blow"
            line34 = "For the voyage is wild"
            line35 = "And the winds don't blow"
            line44 = "For the voyage is wild"
            line45 = "And the winds dont' blow"
            break
    print(line17)
    print(line18)
    print(line34)
    print(line35)
    print(line44)
    print(line45)
    playlist(track1="", track2="", track3="", track4="", track5="",
             track6="", track7="", track8="", track9="", track10="",
             track11="", track12="", track13="", track14="", track15="",
             track16="", track17="line17", track18="line18", track19="", track20="",
             track21="", track22="", track23="", track24="", track25="",
             track26="", track27="", track28="", track29="", track30="",
             track31="", track32="", track33="", track34="line34", track35="line35",
             track36="", track37="", track38="", track39="", track40="",
             track41="", track42="", track43="", track44="line44", track45="line45",
             track46="", track47="")


def cue8(choice):
    while True:
        if choice == "Foul":
            line21 = "Oh, the wind was foul, and the sea ran high"
            break
        if choice == "Cold":
            line21 = "Oh, the wind was cold, and the sea ran high"
            break
        if choice == "Wild":
            line21 = "Oh, the wind was weird, and the sea ran high"
            break
    print(line21)
    playlist(track1="", track2="", track3="", track4="", track5="",
             track6="", track7="", track8="", track9="", track10="",
             track11="", track12="", track13="", track14="", track15="",
             track16="", track17="", track18="", track19="", track20="",
             track21="line21", track22="", track23="", track24="", track25="",
             track26="", track27="", track28="", track29="", track30="",
             track31="", track32="", track33="", track34="", track35="",
             track36="", track37="", track38="", track39="", track40="",
             track41="", track42="", track43="", track44="", track45="",
             track46="", track47="")


def heresyourlist():
    button_boom("thegrid")
    button_heresyoursong.destroy()
    button_continueonemore.grid(row=1, column=1, padx=10, pady=10, sticky=W)
# When you click Continue after the video
    lex_image.grid(row=1, column=0)
    guido_image.grid(row=1, column=1)


def cuethevideo():
    button_continueonemore.destroy()
    interview()
# Makes you watch the video


def gimme_my_song():
    # This actually plays the song
    part("1", track="")
    part("2", track="")
    part("3", track="")
    part("4", track="")
    part("5", track="")
    part("6", track="")
    part("7", track="")
    part("8", track="")
    part("9", track="")
    part("10", track="")
    part("11", track="")
    part("12", track="")
    part("13", track="")
    part("14", track="")
    part("15", track="")
    part("16", track="")
    part("17", track="")
    part("18", track="")
    part("29", track="")
    part("20", track="")
    part("21", track="")
    part("22", track="")
    part("23", track="")
    part("24", track="")
    part("25", track="")
    part("26", track="")
    part("27", track="")
    part("28", track="")
    part("29", track="")
    part("30", track="")
    part("31", track="")
    part("32", track="")
    part("33", track="")
    part("34", track="")
    part("35", track="")
    part("36", track="")
    part("37", track="")
    part("38", track="")
    part("39", track="")
    part("40", track="")
    part("41", track="")
    part("42", track="")
    part("43", track="")
    part("44", track="")
    part("45", track="")
    part("46", track="")
    part("47", track="")


def track(number):


def part(number, track):
    while True:
        if number == "1":
            break
        if number == "2":
        if number == "3":
        if number == "4":
        if number == "5":
        if number == "6":
        if number == "7":
        if number == "8":
        if number == "9":
        if number == "10":
        if number == "11":
        if number == "12":
        if number == "13":
        if number == "14":
        if number == "15":
        if number == "16":
        if number == "17":
        if number == "18":
        if number == "19":
        if number == "20":
        if number == "21":
        if number == "22":
        if number == "23":
        if number == "24":
        if number == "25":
        if number == "26":
        if number == "27":
        if number == "28":
        if number == "29":
        if number == "30":
        if number == "31":
        if number == "32":
        if number == "33":
        if number == "34":
        if number == "35":
        if number == "36":
        if number == "37":
        if number == "38":
        if number == "39":
        if number == "40":
        if number == "41":
        if number == "42":
        if number == "43":
        if number == "44":
        if number == "45":
        if number == "46":
        if number == "47":
    while True:
        if track == "1":
            play = pygame.mixer.Sound("itih.mp3").play()
        if track == "2":
            play = pygame.mixer.Sound("ttth.mp3").play()
        if track == "3":
            play = pygame.mixer.Sound("wtwh.mp3").play()
        if track == "4":
            play = pygame.mixer.Sound("to.mp3").play()
        if track == "5":
            play = pygame.mixer.Sound("tt.mp3").play()
        if track == "6":
            play = pygame.mixer.Sound("ts.mp3").play()
        if track == "7":
            play = pygame.mixer.Sound("ms.mp3").play()
        if track == "8":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "9":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "10":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        if track == "11":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "12":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "13":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "14":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "15":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "16":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        if track == "17":
            play = pygame.mixer.Sound("tyw.mp3").play()
        if track == "18":
            play = pygame.mixer.Sound("ntyw.mp3").play()
        if track == "19":
            play = pygame.mixer.Sound("ofyw.mp3").play()
        if track == "20":
            play = pygame.mixer.Sound("getyp.mp3").play()
        if track == "21":
            play = pygame.mixer.Sound("getyb.mp3").play()
        if track == "22":
            play = pygame.mixer.Sound("getyf.mp3").play()
        if track == "23":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        if track == "24":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "25":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "26":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        if track == "27":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "28":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "29":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        if track == "30":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "31":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "32":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "33":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "34":
            play = pygame.mixer.Sound("wher_two.mp3.").play()
        if track == "35":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        if track == "36":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "37":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "38":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        if track == "39":
            play = pygame.mixer.Sound("johnny_two.mp3").play()
        if track == "40":
            play = pygame.mixer.Sound("timmy_two.mp3").play()
        if track == "41":
            play = pygame.mixer.Sound("frodo_two.mp3").play()
        if track == "42":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "43":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "44":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        if track == "45":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "46":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "47":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        if track == "48":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        if track == "49":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        if track == "50":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "51":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "52":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        if track == "53":
            play = pygame.mixer.Sound("otwwfatsrh.mp3").play()
        if track == "54":
            play = pygame.mixer.Sound("otwwcatsrh.mp3").play()
        if track == "55":
            play = pygame.mixer.Sound("otwwwatsrh.mp3").play()
        if track == "56":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "57":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "58":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        if track == "59":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "60":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "61":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "62":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "63":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "64":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        if track == "65":
            play = pygame.mixer.Sound("ssiganwb.mp3").play()
        if track == "66":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        if track == "67":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "68":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "69":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        if track == "70":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "71":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "72":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        if track == "73":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "74":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "75":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "76":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "77":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "78":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        if track == "79":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "80":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "81":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        if track == "82":
            play = pygame.mixer.Sound("johnny_two.mp3").play()
        if track == "83":
            play = pygame.mixer.Sound("timmy_two.mp3").play()
        if track == "84":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "85":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "86":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "87":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        if track == "88":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "89":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "90":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        if track == "91":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        if track == "92":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        if track == "93":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "94":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "95":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()
        if track == "96":
            play = pygame.mixer.Sound("lher_one.mp3").play()
        if track == "97":
            play = pygame.mixer.Sound("wher_one.mp3").play()
        if track == "98":
            play = pygame.mixer.Sound("trher_one.mp3").play()
        if track == "99":
            play = pygame.mixer.Sound("johnny_one.mp3").play()
        if track == "100":
            play = pygame.mixer.Sound("timmy_one.mp3").play()
        if track == "101":
            play = pygame.mixer.Sound("frodo_one.mp3").play()
        if track == "102":
            play = pygame.mixer.Sound("lher_two.mp3").play()
        if track == "103":
            play = pygame.mixer.Sound("wher_two.mp3").play()
        if track == "104":
            play = pygame.mixer.Sound("trher_two.mp3").play()
        if track == "105":
            play = pygame.mixer.Sound("olher_one.mp3").play()
        if track == "106":
            play = pygame.mixer.Sound("owher_one.mp3").play()
        if track == "107":
            play = pygame.mixer.Sound("otrher_one.mp3").play()
        if track == "108":
            play = pygame.mixer.Sound("johnny_two.mp3").play()
        if track == "109":
            play = pygame.mixer.Sound("timmy_two.mp3").play()
        if track == "110":
            play = pygame.mixer.Sound("frodo_two.mp3").play()
        if track == "111":
            play = pygame.mixer.Sound("lher_three.mp3").play()
        if track == "112":
            play = pygame.mixer.Sound("wher_three.mp3").play()
        if track == "113":
            play = pygame.mixer.Sound("trher_three.mp3").play()
        if track == "114":
            play = pygame.mixer.Sound("ftvil.mp3").play()
        if track == "115":
            play = pygame.mixer.Sound("ftvis.mp3").play()
        if track == "116":
            play = pygame.mixer.Sound("ftviw.mp3").play()
        if track == "117":
            play = pygame.mixer.Sound("atwdb.mp3").play()
        if track == "118":
            play = pygame.mixer.Sound("aitfu.mp3").play()
        if track == "119":
            play = pygame.mixer.Sound("tlher_one.mp3").play()
        if track == "120":
            play = pygame.mixer.Sound("twher_one.mp3").play()
        if track == "121":
            play = pygame.mixer.Sound("ttrher_one.mp3").play()


def playlist(track1, track2, track3, track4, track5, track6, track7, track8, track9, track10,
             track11, track12, track13, track14, track15, track16, track17, track18, track19, track20,
             track21, track22, track23, track24, track25, track26, track27, track28, track29, track30,
             track31, track32, track33, track34, track35, track36, track37, track38, track39, track40,
             track41, track42, track43, track44, track45, track46, track47):
    pygame.mixer.music.unload()
    while True:
        if track1 == "I thought I heard":
            part(number="", track="1")
            break
        if track1 == "They thought they heard":
            part(number="", track="2")
            break
        if track1 == "We thought we heard":
            part(number="", track="3")
            break
    while True:
        if track2 == "The Old":
            part(number="", track="4")
            break
        if track2 == "The Tall":
            part(number="", track="5")
            break
        if track2 == "The Sad":
            part(number="", track="6")
            break
    while True:
        if track3 == "Man say":
            part(number="", track="7")
            break
    while True:
        if track4 == "Leave her":
            part(number="", track="8")
            break
        if track4 == "Watch her":
            part(number="", track="9")
            break
        if track4 == "Trust her":
            part(number="", track="10")
            break
    while True:
        if track5 == "Johnny":
            part(number="", track="11")
            break
        if track5 == "Timmy":
            part(number="", track="12")
            break
        if track5 == "Frodo":
            part(number="", track="13")
            break
    while True:
        if track6 == "Leave her":
            part(number="", track="14")
            break
        if track6 == "Watch her":
            part(number="", track="15")
            break
        if track6 == "Trust her":
            part(number="", track="16")
            break
    while True:
        if track7 == "Tomorrow, ye will":
            part(number="", track="17")
            break
        if track7 == "Next Tuesday, ye will":
            part(number="", track="18")
            break
        if track7 == "On Friday, ye will":
            part(number="", track="19")
            break
    while True:
        if track8 == "Get your pay":
            part(number="", track="20")
            break
        if track8 == "Get your bell":
            part(number="", track="21")
            break
        if track8 == "Get your fish":
            part(number="", track="22")
            break
    while True:
        if track9 == "And it's time for us":
            part(number="", track="23")
            break
    while True:
        if track10 == "To leave her":
            part(number="", track="24")
            break
        if track10 == "To watch her":
            part(number="", track="25")
            break
        if track10 == "To trust her":
            part(number="", track="26")
            break
    while True:
        if track11 == "Leave her":
            part(number="", track="27")
            break
        if track11 == "Watch her":
            part(number="", track="28")
            break
        if track11 == "Trust her":
            part(number="", track="29")
            break
    while True:
        if track12 == "Johnny":
            part(number="", track="30")
            break
        if track12 == "Timmy":
            part(number="", track="31")
            break
        if track12 == "Frodo":
            part(number="", track="32")
            break
    while True:
        if track13 == "Leave her":
            part(number="", track="33")
            break
        if track13 == "Watch her":
            part(number="", track="34")
            break
        if track13 == "Trust her":
            part(number="", track="35")
            break
    while True:
        if track14 == "Oh, leave her":
            part(number="", track="36")
            break
        if track14 == "Oh, watch her":
            part(number="", track="37")
            break
        if track14 == "Oh, trust her":
            part(number="", track="38")
            break
    while True:
        if track15 == "Johnny":
            part(number="", track="39")
            break
        if track15 == "Timmy":
            part(number="", track="40")
            break
        if track15 == "Frodo":
            part(number="", track="41")
            break
    while True:
        if track16 == "Leave her":
            part(number="", track="42")
            break
        if track16 == "Watch her":
            part(number="", track="43")
            break
        if track16 == "Trust her":
            part(number="", track="44")
            break
    while True:
        if track17 == "For the voyage is long":
            part(number="", track="45")
            break
        if track17 == "For the voyage is short":
            part(number="", track="46")
            break
        if track18 == "For the voyage is wild":
            part(number="", track="47")
            break
    while True:
        if track18 == "And the winds don't blow":
            part(number="", track="48")
            break
    while True:
        if track19 == "And it's time for us":
            part(number="", track="49")
            break
    while True:
        if track20 == "To leave her":
            part(number="", track="50")
            break
        if track20 == "To watch her":
            part(number="", track="51")
            break
        if track20 == "To trust her":
            part(number="", track="52")
            break
    while True:
        if track21 == "Oh, the wind was foul, and the sea ran high":
            part(number="", track="53")
            break
        if track21 == "Oh, the wind was cold, and the sea ran high":
            part(number="", track="54")
            break
        if track21 == "Oh, the wind was weird, and the sea ran high":
            part(number="", track="55")
            break
    while True:
        if track22 == "Leave her":
            part(number="", track="56")
            break
        if track22 == "Watch her":
            part(number="", track="57")
            break
        if track22 == "Trust her":
            part(number="", track="58")
            break
    while True:
        if track23 == "Johnny":
            part(number="", track="59")
            break
        if track23 == "Timmy":
            part(number="", track="60")
            break
        if track23 == "Frodo":
            part(number="", track="61")
            break
    while True:
        if track24 == "Leave her":
            part(number="", track="62")
            break
        if track24 == "Watch her":
            part(number="", track="63")
            break
        if track24 == "Trust her":
            part(number="", track="64")
            break
    while True:
        if track25 == "She shipped it green, and none went by":
            part(number="", track="65")
            break
    while True:
        if track26 == "And it's time for us":
            part(number="", track="66")
            break
    while True:
        if track27 == "To leave her":
            part(number="", track="67")
            break
        if track27 == "To watch her":
            part(number="", track="68")
            break
        if track27 == "To trust her":
            part(number="", track="69")
            break
    while True:
        if track28 == "Leave her":
            part(number="", track="70")
            break
        if track28 == "Watch her":
            part(number="", track="71")
            break
        if track28 == "Trust her":
            part(number="", track="72")
            break
    while True:
        if track29 == "Johnny":
            part(number="", track="73")
            break
        if track29 == "Timmy":
            part(number="", track="74")
            break
        if track29 == "Frodo":
            part(number="", track="75")
            break
    while True:
        if track30 == "Leave her":
            part(number="", track="76")
            break
        if track30 == "Watch her":
            part(number="", track="77")
            break
        if track30 == "Trust her":
            part(number="", track="78")
            break
    while True:
        if track31 == "Oh, leave her":
            part(number="", track="79")
            break
        if track31 == "Oh, watch her":
            part(number="", track="80")
            break
        if track31 == "Oh, trust her":
            part(number="", track="81")
            break
    while True:
        if track32 == "Johnny":
            part(number="", track="82")
            break
        if track32 == "Timmy":
            part(number="", track="83")
            break
        if track32 == "Frodo":
            part(number="", track="84")
            break
    while True:
        if track33 == "Leave her":
            part(number="", track="85")
            break
        if track33 == "Watch her":
            part(number="", track="86")
            break
        if track33 == "Trust her":
            part(number="", track="87")
            break
    while True:
        if track34 == "For the voyage is long":
            part(number="", track="88")
            break
        if track34 == "For the voyage is short":
            part(number="", track="89")
            break
        if track34 == "For the voyage is wild":
            part(number="", track="90")
            break
    while True:
        if track35 == "And the winds don't blow":
            part(number="", track="91")
            break
    while True:
        if track36 == "And it's time for us":
            part(number="", track="92")
            break
    while True:
        if track37 == "To leave her":
            part(number="", track="93")
            break
        if track37 == "To watch her":
            part(number="", track="94")
            break
        if track37 == "To trust her":
            part(number="", track="95")
            break
    while True:
        if track38 == "Leave her":
            part(number="", track="96")
            break
        if track38 == "Watch her":
            part(number="", track="97")
            break
        if track38 == "Trust her":
            part(number="", track="98")
            break
    while True:
        if track39 == "Johnny":
            part(number="", track="99")
            break
        if track39 == "Timmy":
            part(number="", track="100")
            break
        if track39 == "Frodo":
            part(number="", track="101")
            break
    while True:
        if track40 == "Leave her":
            part(number="", track="102")
            break
        if track40 == "Watch her":
            part(number="", track="103")
            break
        if track40 == "Trust her":
            part(number="", track="104")
            break
    while True:
        if track41 == "Oh, leave her":
            part(number="", track="105")
            break
        if track41 == "Oh, watch her":
            part(number="", track="106")
            break
        if track41 == "Oh, trust her":
            part(number="", track="107")
            break
    while True:
        if track42 == "Johnny":
            part(number="", track="108")
            break
        if track42 == "Timmy":
            part(number="", track="109")
            break
        if track42 == "Frodo":
            part(number="", track="110")
            break
    while True:
        if track43 == "Leave her":
            part(number="", track="111")
            break
        if track43 == "Watch her":
            part(number="", track="112")
            break
        if track43 == "Trust her":
            part(number="", track="113")
            break
    while True:
        if track44 == "For the voyage is long":
            part(number="", track="114")
            break
        if track44 == "For the voyage is short":
            part(number="", track="115")
            break
        if track44 == "For the voyage is wild":
            part(number="", track="116")
            break
    while True:
        if track45 == "And the winds don't blow":
            part(number="", track="117")
            break
    while True:
        if track46 == "And it's time for us":
            part(number="", track="118")
            break
    while True:
        if track47 == "To leave her":
            part(number="", track="119")
            break
        if track47 == "To watch her":
            part(number="", track="120")
            break
        if track47 == "To trust her":
            part(number="", track="121")
            break
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
button_gimme_my_song = Button(win, bg="forest green", fg="black", font=digitalbard_font,
                              text="Click to hear your customized song", command=gimme_my_song)
button_heresyoursong = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                              command=heresyourlist)
button_continueonemore = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                                command=cuethevideo)
# print("Photo by Kostiantyn Klymovets: https://www.pexels.com/photo/man-playing-lute-on-urban-steps-12831481/")
pygame.mixer.music.load("scarborough_fair.mp3")
pygame.mixer.music.play(-1)
digitalbard_messages = Label(win, bg="black", text="", font=digitalbard_font, fg="gold")
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
# print("Photo by Kostiantyn Klymovets: https://www.pexels.com/photo/man-playing-lute-on-urban-steps-12831481/")
win.mainloop()
