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


def cue1(choice):
    while True:
        if choice == "I":
            pl1 = "I thought I heard"
            break
        if choice == "They":
            pl1 = "They thought they heard"
            break
        if choice == "We":
            pl1 = "We thought we heard"
            break
    playlist(pl=pl1)


def cue2(choice):
    while True:
        if choice == "Old":
            pl2 = "The Old"
            break
        if choice == "Tall":
            pl2 = "The Tall"
            break
        if choice == "Sad":
            pl2 = "The Sad"
            break
    playlist(pl=pl2)


def cue3(choice):
    while True:
        if choice == "Leave":
            pl4 = "Leave her 1"
            pl6 = "Leave her 2"
            pl10 = "To leave her"
            pl11 = "Leave her 1"
            pl13 = "Leave her 2"
            pl14 = "Oh, leave her"
            pl16 = "Leave her 3"
            pl20 = "To leave her"
            pl22 = "Leave her 1"
            pl24 = "Leave her 2"
            pl27 = "To leave her"
            pl28 = "Leave her 1"
            pl30 = "Leave her 2"
            pl31 = "Oh, leave her"
            pl33 = "Leave her 3"
            pl37 = "To leave her"
            pl38 = "Leave her 1"
            pl40 = "Leave her 2"
            pl41 = "Oh, leave her"
            pl43 = "Leave her 3"
            pl47 = "To leave her"
            break
        if choice == "Watch":
            pl4 = "Watch her 1"
            pl6 = "Watch her 2"
            pl10 = "To watch her"
            pl11 = "Watch her 1"
            pl13 = "Watch her 2"
            pl14 = "Oh, watch her"
            pl16 = "Watch her 3"
            pl20 = "To watch her"
            pl22 = "Watch her 1"
            pl24 = "Watch her 2"
            pl27 = "To watch her"
            pl28 = "Watch her 1"
            pl30 = "Watch her 2"
            pl31 = "Oh, watch her"
            pl33 = "Watch her 3"
            pl37 = "To watch her"
            pl38 = "Watch her 1"
            pl40 = "Watch her 2"
            pl41 = "Oh, watch her"
            pl43 = "Watch her 3"
            pl47 = "To watch her"
            break
        if choice == "Trust":
            pl4 = "Trust her 1"
            pl6 = "Trust her 2"
            pl10 = "To trust her"
            pl11 = "Trust her 1"
            pl13 = "Trust her 2"
            pl14 = "Oh, trust her"
            pl16 = "Trust her 3"
            pl20 = "To trust her"
            pl22 = "Trust her 1"
            pl24 = "Trust her 2"
            pl27 = "To trust her"
            pl28 = "Trust her 1"
            pl30 = "Trust her 2"
            pl31 = "Oh, trust her"
            pl33 = "Trust her 3"
            pl37 = "To trust her"
            pl38 = "Trust her 1"
            pl40 = "Trust her 2"
            pl41 = "Oh, trust her"
            pl43 = "Trust her 3"
            pl47 = "To trust her"
            break
    pl9 = "And it's time for us"
    pl18 = "And the winds don't blow"
    pl19 = "And it's time for us"
    pl25 = "She shipped it green, and none went by"
    pl26 = "And it's time for us"
    pl36 = "And it's time for us"
    pl46 = "And it's time for us"
    playlist(pl=pl9)
    playlist(pl=pl18)
    playlist(pl=pl19)
    playlist(pl=pl25)
    playlist(pl=pl26)
    playlist(pl=pl36)
    playlist(pl=pl46)
    playlist(pl=pl4)
    playlist(pl=pl6)
    playlist(pl=pl10)
    playlist(pl=pl11)
    playlist(pl=pl13)
    playlist(pl=pl14)
    playlist(pl=pl16)
    playlist(pl=pl20)
    playlist(pl=pl22)
    playlist(pl=pl24)
    playlist(pl=pl27)
    playlist(pl=pl28)
    playlist(pl=pl30)
    playlist(pl=pl31)
    playlist(pl=pl33)
    playlist(pl=pl37)
    playlist(pl=pl38)
    playlist(pl=pl40)
    playlist(pl=pl41)
    playlist(pl=pl43)
    playlist(pl=pl47)


def cue4(choice):
    while True:
        if choice == "Johnny":
            pl5 = "Johnny 1"
            pl12 = "Johnny 1"
            pl15 = "Johnny 2"
            pl23 = "Johnny 1"
            pl29 = "Johnny 1"
            pl32 = "Johnny 1"
            pl39 = "Johnny 2"
            pl42 = "Johnny 1"
            break
        if choice == "Timmy":
            pl5 = "Timmy 1"
            pl12 = "Timmy 1"
            pl15 = "Timmy 2"
            pl23 = "Timmy 1"
            pl29 = "Timmy 1"
            pl32 = "Timmy 1"
            pl39 = "Timmy 2"
            pl42 = "Timmy 1"
            break
        if choice == "Frodo":
            pl5 = "Frodo 1"
            pl12 = "Frodo 1"
            pl15 = "Frodo 2"
            pl23 = "Frodo 1"
            pl29 = "Frodo 1"
            pl32 = "Frodo 1"
            pl39 = "Frodo 2"
            pl42 = "Frodo 1"
            break
    playlist(pl=pl5)
    playlist(pl=pl12)
    playlist(pl=pl15)
    playlist(pl=pl23)
    playlist(pl=pl29)
    playlist(pl=pl32)
    playlist(pl=pl39)
    playlist(pl=pl42)


def cue5(choice):
    while True:
        if choice == "Tomorrow":
            pl7 = "Tomorrow, ye will"
            break
        if choice == "Next Tuesday":
            pl7 = "Next Tuesday, ye will"
            break
        if choice == "On Friday":
            pl7 = "On Friday, ye will"
            break
    playlist(pl=pl7)


def cue6(choice):
    while True:
        if choice == "Pay":
            pl8 = "Get your pay"
            break
        if choice == "Bell":
            pl8 = "Get your bell"
            break
        if choice == "Fish":
            pl8 = "Get your fish"
            break
    playlist(pl=pl8)


def cue7(choice):
    while True:
        if choice == "Long":
            pl17 = "For the voyage is long"
            pl18 = "And the winds don't blow"
            pl34 = "For the voyage is long"
            pl35 = "And the winds don't blow"
            pl44 = "For the voyage is long"
            pl45 = "And the winds don't blow"
            break
        if choice == "Short":
            pl17 = "For the voyage is short"
            pl18 = "And the winds don't blow"
            pl34 = "For the voyage is short"
            pl35 = "And the winds don't blow"
            pl44 = "For the voyage is short"
            pl45 = "And the winds don't blow"
            break
        if choice == "Wild":
            pl17 = "For the voyage is wild"
            pl18 = "And the winds don't blow"
            pl34 = "For the voyage is wild"
            pl35 = "And the winds don't blow"
            pl44 = "For the voyage is wild"
            pl45 = "And the winds dont' blow"
            break
    playlist(pl=pl17)
    playlist(pl=pl18)
    playlist(pl=pl34)
    playlist(pl=pl35)
    playlist(pl=pl44)
    playlist(pl=pl45)


def cue8(choice):
    while True:
        if choice == "Foul":
            pl21 = "Oh, the wind was foul, and the sea ran high"
            break
        if choice == "Cold":
            pl21 = "Oh, the wind was cold, and the sea ran high"
            break
        if choice == "Wild":
            pl21 = "Oh, the wind was weird, and the sea ran high"
            break
    playlist(pl=pl21)


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
    pass


def dj1(tracknumber):


def dj2(tracknumber):


def dj3(tracknumber):


def dj4(tracknumber):


def dj4(tracknumber):


def dj5(tracknumber):


def dj6(tracknumber):


def dj7(tracknumber):


def dj8(tracknumber):


def dj9(tracknumber):


def dj10(tracknumber):


def dj11(tracknumber):

def dj12(tracknumber):


def dj13(tracknumber):


def dj14(tracknumber):


def dj15(tracknumber):


def dj16(tracknumber):


def dj17(tracknumber):


def dj18(tracknumber):


def dj19(tracknumber):


def dj20(tracknumber):


def dj21(tracknumber):


def dj22(tracknumber):


def dj23(tracknumber):


def dj24(tracknumber):


def dj25(tracknumber):


def dj26(tracknumber):


def dj27(tracknumber):


def dj28(tracknumber):


def dj29(tracknumber):


def dj30(tracknumber):


def dj31(tracknumber):


def dj32(tracknumber):


def dj33(tracknumber):


def dj34(tracknumber):


def dj35(tracknumber):


def dj36(tracknumber):


def dj37(tracknumber):


def dj38(tracknumber):


def dj39(tracknumber):


def dj40(tracknumber):


def dj41(tracknumber):


def dj42(tracknumber):


def dj43(tracknumber):


def dj44(tracknumber):


def dj45(tracknumber):


def dj46(tracknumber):


def dj47(tracknumber):


def playlist(pl):
    if pl == "I thought I heard":
        dj1("1")
    if pl == "They thought they heard":
        dj1("2")
    if pl == "We thought we heard":
        dj1("3")
    if pl == "The Old":
        dj2("4")
    if pl == "The Tall":
        dj2("5")
    if pl == "The Sad":
        dj2("6")
    if pl == "Man say":
        dj3("7")
    if pl == "Leave her":
        dj4("8")
    if pl == "Watch her":
        dj4("9")
    if pl == "Trust her":
        dj4("10")
    if pl == "Johnny":
        dj5("11")
    if pl == "Timmy":
        dj5("12")
    if pl == "Frodo":
        dj5("13")
    if pl == "Leave her":
        dj6("14")
    if pl == "Watch her":
        dj6("15")
    if pl == "Trust her":
        dj6("16")
    if pl == "Tomorrow, ye will":
        dj7("17")
    if pl == "Next Tuesday, ye will":
        dj7("18")
    if pl == "On Friday, ye will":
        dj7("19")
    if pl == "Get your pay":
        dj8("20")
    if pl == "Get your bell":
        dj8("21")
    if pl == "Get your fish":
        dj8("22")
    if pl == "And it's time for us":
        dj9("23")
    if pl == "To leave her":
        dj10("24")
    if pl == "To watch her":
        dj10("25")
    if pl == "To trust her":
        dj10("26")
    if pl == "Leave her":
        dj11("27")
    if pl == "Watch her":
        dj11("28")
    if pl == "Trust her":
        dj11("29")
    if pl == "Johnny":
        dj12("30")
    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Oh, leave her":

    if pl == "Oh, watch her":

    if pl == "Oh, trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "For the voyage is long":

    if pl == "For the voyage is short":

    if pl == "For the voyage is wild":

    if pl == "And the winds don't blow":

    if pl == "And it's time for us":

    if pl == "To leave her":

    if pl == "To watch her":

    if pl == "To trust her":

    if pl == "Oh, the wind was foul, and the sea ran high":

    if pl == "Oh, the wind was cold, and the sea ran high":

    if pl == "Oh, the wind was weird, and the sea ran high":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "She shipped it green, and none went by":

    if pl == "And it's time for us":

    if pl == "To leave her":

    if pl == "To watch her":

    if pl == "To trust her":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Oh, leave her":

    if pl == "Oh, watch her":

    if pl == "Oh, trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "For the voyage is long":

    if pl == "For the voyage is short":

    if pl == "For the voyage is wild":

    if pl == "And the winds don't blow":

    if pl == "And it's time for us":

    if pl == "To leave her":

    if pl == "To watch her":

    if pl == "To trust her":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "Oh, leave her":

    if pl == "Oh, watch her":

    if pl == "Oh, trust her":

    if pl == "Johnny":

    if pl == "Timmy":

    if pl == "Frodo":

    if pl == "Leave her":

    if pl == "Watch her":

    if pl == "Trust her":

    if pl == "For the voyage is long":

    if pl == "For the voyage is short":

    if pl == "For the voyage is wild":

    if pl == "And the winds don't blow":

    if pl == "And it's time for us":

    if pl == "To leave her":

    if pl == "To watch her":

    if pl == "To trust her":




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
