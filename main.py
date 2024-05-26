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
    pygame.mixer.music.play()


#   I thought I heard
def dj1(tracknumber):
    pygame.mixer.music.unload()
    if tracknumber == "1":
        pygame.mixer.music.load("itih.mp3")
    if tracknumber == "2":
        pygame.mixer.music.load("ttth.mp3")
    if tracknumber == "3":
        pygame.mixer.music.load("wtwh.mp3")


#   The Old Man say
def dj2(tracknumber):
    if tracknumber == "4":
        pygame.mixer.music.queue("to.mp3")
    if tracknumber == "5":
        pygame.mixer.music.queue("tt.mp3")
    if tracknumber == "6":
        pygame.mixer.music.queue("ts.mp3")


def dj3(tracknumber):
    if tracknumber == "7":
        pygame.mixer.music.queue("ms.mp3")


#   Leave her, Johnny, leave her
def dj4(tracknumber):
    if tracknumber == "8":
        pygame.mixer.music.queue("lher_one.mp3")
    if tracknumber == "9":
        pygame.mixer.music.queue("wher_one.mp3")
    if tracknumber == "10":
        pygame.mixer.music.queue("trher_one.mp3")


def dj5(tracknumber):
    if tracknumber == "11":
        pygame.mixer.music.queue("johnny_one.mp3")
    if tracknumber == "12":
        pygame.mixer.music.queue("timmy_one.mp3")
    if tracknumber == "13":
        pygame.mixer.music.queue("frodo_one.mp3")


def dj6(tracknumber):
    if tracknumber == "14":
        pygame.mixer.music.queue("lher_two.mp3")
    if tracknumber == "15":
        pygame.mixer.music.queue("wher_two.mp3")
    if tracknumber == "16":
        pygame.mixer.music.queue("trher_two.mp3")


#   Tomorrow, ye will get your pay
def dj7(tracknumber):
    if tracknumber == "17":
        pygame.mixer.music.queue("tyw.mp3")
    if tracknumber == "18":
        pygame.mixer.music.queue("ntyw.mp3")
    if tracknumber == "19":
        pygame.mixer.music.queue("ofyw.mp3")


def dj8(tracknumber):
    if tracknumber == "20":
        pygame.mixer.music.queue("getyp.mp3")
    if tracknumber == "21":
        pygame.mixer.music.queue("getyb.mp3")
    if tracknumber == "22":
        pygame.mixer.music.queue("getyf.mp3")


#   And it's time for us to leave her
def dj9(tracknumber):
    if tracknumber == "23":
        pygame.mixer.music.queue("aitfu.mp3")


def dj10(tracknumber):
    if tracknumber == "24":
        pygame.mixer.music.queue("tlher_one.mp3")
    if tracknumber == "25":
        pygame.mixer.music.queue("twher_one.mp3")
    if tracknumber == "26":
        pygame.mixer.music.queue("ttrher_one.mp3")


#   Leave her, Johnny, leave her
def dj11(tracknumber):
    if tracknumber == "27":
        pygame.mixer.music.queue("lher_one.mp3")
    if tracknumber == "28":
        pygame.mixer.music.queue("wher_one.mp3")
    if tracknumber == "29":
        pygame.mixer.music.queue("trher_one.mp3")


def dj12(tracknumber):
    if tracknumber == "30":
        pygame.mixer.music.queue("johnny_one.mp3")
    if tracknumber == "31":
        pygame.mixer.music.queue("timmy_one.mp3")
    if tracknumber == "32":
        pygame.mixer.music.queue("frodo_one.mp3")


def dj13(tracknumber):
    if tracknumber == "33":
        pygame.mixer.music.queue("lher_two.mp3")
    if tracknumber == "34":
        pygame.mixer.music.queue("wher_two.mp3")
    if tracknumber == "35":
        pygame.mixer.music.queue("trher_two.mp3")


#   Oh, leave her, Johnny, leave her
def dj14(tracknumber):
    if tracknumber == "36":
        pygame.mixer.music.queue("olher_one.mp3")
    if tracknumber == "37":
        pygame.mixer.music.queue("olher_one.mp3")
    if tracknumber == "38":
        pygame.mixer.music.queue("olher_one.mp3")


def dj15(tracknumber):
    if tracknumber == "39":
        pygame.mixer.music.queue("johnny_two.mp3")
    if tracknumber == "40":
        pygame.mixer.music.queue("timmy_two.mp3")
    if tracknumber == "41":
        pygame.mixer.music.queue("frodo_two.mp3")


def dj16(tracknumber):
    if tracknumber == "42":
        pygame.mixer.music.queue("lher_three.mp3")
    if tracknumber == "43":
        pygame.mixer.music.queue("wher_three.mp3")
    if tracknumber == "44":
        pygame.mixer.music.queue("trher_three.mp3")


#   For the voyage is long, and the winds don't blow
def dj17(tracknumber):
    if tracknumber == "45":
        pygame.mixer.music.queue("ftvil.mp3")
    if tracknumber == "46":
        pygame.mixer.music.queue("ftvis.mp3")
    if tracknumber == "47":
        pygame.mixer.music.queue("ftviw.mp3")


def dj18(tracknumber):
    if tracknumber == "48":
        pygame.mixer.music.queue("atwdb.mp3")


#   And it's time for us to leave her
def dj19(tracknumber):
    if tracknumber == "49":
        pygame.mixer.music.queue("aitfu.mp3")


def dj20(tracknumber):
    if tracknumber == "50":
        pygame.mixer.music.queue("tlher_one.mp3 ")
    if tracknumber == "51":
        pygame.mixer.music.queue("twher_one.mp3")
    if tracknumber == "52":
        pygame.mixer.music.queue("ttrher_one.mp3")


#   Oh, the wind was foul, and the sea ran high
def dj21(tracknumber):
    if tracknumber == "53":
        pygame.mixer.music.queue("otwwfatsrh.mp3")
    if tracknumber == "54":
        pygame.mixer.music.queue("otwwcatsrh.mp3")
    if tracknumber == "55":
        pygame.mixer.music.queue("otwwwatsrh.mp3")


#   Leave her, Johnny, leave her
def dj22(tracknumber):
    if tracknumber == "56":
        pygame.mixer.music.queue("lher_one.mp3")
    if tracknumber == "57":
        pygame.mixer.music.queue("wher_one.mp3")
    if tracknumber == "58":
        pygame.mixer.music.queue("trher_one.mp3")


def dj23(tracknumber):
    if tracknumber == "59":
        pygame.mixer.music.queue("johnny_one.mp3")
    if tracknumber == "60":
        pygame.mixer.music.queue("timmy_one.mp3")
    if tracknumber == "61":
        pygame.mixer.music.queue("frodo_one.mp3")


def dj24(tracknumber):
    if tracknumber == "62":
        pygame.mixer.music.queue("lher_two.mp3")
    if tracknumber == "63":
        pygame.mixer.music.queue("wher_two.mp3")
    if tracknumber == "64":
        pygame.mixer.music.queue("trher_two.mp3")


#   She shipped it green, and none went by
def dj25(tracknumber):
    if tracknumber == "65":
        pygame.mixer.music.queue("ssiganwb.mp3")
#   And it's time for us to leave her


def dj26(tracknumber):
    if tracknumber == "66":
        pygame.mixer.music.queue("aitfu.mp3")


def dj27(tracknumber):
    if tracknumber == "67":
        pygame.mixer.music.queue("tlher_one.mp3")
    if tracknumber == "68":
        pygame.mixer.music.queue("twher_one.mp3")
    if tracknumber == "69":
        pygame.mixer.music.queue("ttrher_one.mp3")


#   Leave her, Johnny, leave her
def dj28(tracknumber):
    if tracknumber == "70":
        pygame.mixer.music.queue("lher_one.mp3")
    if tracknumber == "71":
        pygame.mixer.music.queue("wher_one.mp3")
    if tracknumber == "72":
        pygame.mixer.music.queue("trher_one.mp3")


def dj29(tracknumber):
    if tracknumber == "73":
        pygame.mixer.music.queue("johnny_one.mp3")
    if tracknumber == "74":
        pygame.mixer.music.queue("timmy_one.mp3")
    if tracknumber == "75":
        pygame.mixer.music.queue("frodo_one.mp3")


def dj30(tracknumber):
    if tracknumber == "76":
        pygame.mixer.music.queue("lher_two.mp3")
    if tracknumber == "77":
        pygame.mixer.music.queue("wher_two.mp3")
    if tracknumber == "78":
        pygame.mixer.music.queue("trher_two.mp3")


#   Oh, leave her, Johnny, leave her
def dj31(tracknumber):
    if tracknumber == "79":
        pygame.mixer.music.queue("olher_one.mp3")
    if tracknumber == "80":
        pygame.mixer.music.queue("owher_one.mp3")
    if tracknumber == "81":
        pygame.mixer.music.queue("otrher_one.mp3")


def dj32(tracknumber):
    if tracknumber == "82":
        pygame.mixer.music.queue("johnny_two.mp3")
    if tracknumber == "83":
        pygame.mixer.music.queue("timmy_two.mp3")
    if tracknumber == "84":
        pygame.mixer.music.queue("frodo_two.mp3")


def dj33(tracknumber):
    if tracknumber == "85":
        pygame.mixer.music.queue("lher_three.mp3")
    if tracknumber == "86":
        pygame.mixer.music.queue("wher_three.mp3")
    if tracknumber == "87":
        pygame.mixer.music.queue("trher_three.mp3")


#   For the voyage is long, and the winds don't blow
def dj34(tracknumber):
    if tracknumber == "88":
        pygame.mixer.music.queue("ftvil.mp3")
    if tracknumber == "89":
        pygame.mixer.music.queue("ftvis.mp3")
    if tracknumber == "90":
        pygame.mixer.music.queue("ftviw.mp3")


def dj35(tracknumber):
    if tracknumber == "91":
        pygame.mixer.music.queue("atwdb.mp3")


#   And it's time for us to leave her
def dj36(tracknumber):
    if tracknumber == "92":
        pygame.mixer.music.queue("aitfu.mp3")


def dj37(tracknumber):
    if tracknumber == "93":
        pygame.mixer.music.queue("tlher_one.mp3 ")
    if tracknumber == "94":
        pygame.mixer.music.queue("twher_one.mp3")
    if tracknumber == "95":
        pygame.mixer.music.queue("ttrher_one.mp3")


#   Leave her, Johnny, leave her
def dj38(tracknumber):
    if tracknumber == "96":
        pygame.mixer.music.queue("lher_one.mp3")
    if tracknumber == "97":
        pygame.mixer.music.queue("wher_one.mp3")
    if tracknumber == "98":
        pygame.mixer.music.queue("trher_one.mp3")


def dj39(tracknumber):
    if tracknumber == "99":
        pygame.mixer.music.queue("johnny_one.mp3")
    if tracknumber == "100":
        pygame.mixer.music.queue("timmy_one.mp3")
    if tracknumber == "101":
        pygame.mixer.music.queue("frodo_one.mp3")


def dj40(tracknumber):
    if tracknumber == "102":
        pygame.mixer.music.queue("lher_two.mp3")
    if tracknumber == "103":
        pygame.mixer.music.queue("wher_two.mp3")
    if tracknumber == "104":
        pygame.mixer.music.queue("trher_two.mp3")


#   Oh, leave her, Johnny, leave her
def dj41(tracknumber):
    if tracknumber == "105":
        pygame.mixer.music.queue("olher_one.mp3")
    if tracknumber == "106":
        pygame.mixer.music.queue("owher_one.mp3")
    if tracknumber == "107":
        pygame.mixer.music.queue("otrher_one.mp3")


def dj42(tracknumber):
    if tracknumber == "108":
        pygame.mixer.music.queue("johnny_two.mp3")
    if tracknumber == "109":
        pygame.mixer.music.queue("timmy_two.mp3")
    if tracknumber == "110":
        pygame.mixer.music.queue("frodo_two.mp3")


def dj43(tracknumber):
    if tracknumber == "111":
        pygame.mixer.music.queue("lher_three.mp3")
    if tracknumber == "112":
        pygame.mixer.music.queue("wher_three.mp3")
    if tracknumber == "113":
        pygame.mixer.music.queue("trher_three.mp3")


#   For the voyage is long, and the winds don't blow
def dj44(tracknumber):
    if tracknumber == "114":
        pygame.mixer.music.queue("ftvil.mp3")
    if tracknumber == "115":
        pygame.mixer.music.queue("ftvis.mp3")
    if tracknumber == "116":
        pygame.mixer.music.queue("ftviw.mp3")


def dj45(tracknumber):
    if tracknumber == "117":
        pygame.mixer.music.queue("atwdb.mp3")


#   And it's time for us to leave her
def dj46(tracknumber):
    if tracknumber == "118":
        pygame.mixer.music.queue("aitfu.mp3")


def dj47(tracknumber):
    if tracknumber == "119":
        pygame.mixer.music.queue("tlher_one.mp3")
    if tracknumber == "120":
        pygame.mixer.music.queue("twher_one.mp3")
    if tracknumber == "121":
        pygame.mixer.music.queue("ttrher_one.mp3")


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
        dj12("31")
    if pl == "Frodo":
        dj12("32")
    if pl == "Leave her":
        dj13("33")
    if pl == "Watch her":
        dj13("34")
    if pl == "Trust her":
        dj13("35")
    if pl == "Oh, leave her":
        dj14("36")
    if pl == "Oh, watch her":
        dj14("37")
    if pl == "Oh, trust her":
        dj14("38")
    if pl == "Johnny":
        dj15("39")
    if pl == "Timmy":
        dj15("40")
    if pl == "Frodo":
        dj15("41")
    if pl == "Leave her":
        dj16("42")
    if pl == "Watch her":
        dj16("43")
    if pl == "Trust her":
        dj16("44")
    if pl == "For the voyage is long":
        dj17("45")
    if pl == "For the voyage is short":
        dj17("46")
    if pl == "For the voyage is wild":
        dj17("47")
    if pl == "And the winds don't blow":
        dj18("48")
    if pl == "And it's time for us":
        dj19("49")
    if pl == "To leave her":
        dj20("50")
    if pl == "To watch her":
        dj20("51")
    if pl == "To trust her":
        dj20("52")
    if pl == "Oh, the wind was foul, and the sea ran high":
        dj21("53")
    if pl == "Oh, the wind was cold, and the sea ran high":
        dj21("54")
    if pl == "Oh, the wind was weird, and the sea ran high":
        dj21("55")
    if pl == "Leave her":
        dj22("56")
    if pl == "Watch her":
        dj22("57")
    if pl == "Trust her":
        dj22("58")
    if pl == "Johnny":
        dj23("59")
    if pl == "Timmy":
        dj23("60")
    if pl == "Frodo":
        dj23("61")
    if pl == "Leave her":
        dj24("62")
    if pl == "Watch her":
        dj24("63")
    if pl == "Trust her":
        dj24("64")
    if pl == "She shipped it green, and none went by":
        dj25("65")
    if pl == "And it's time for us":
        dj26("66")
    if pl == "To leave her":
        dj27("67")
    if pl == "To watch her":
        dj27("68")
    if pl == "To trust her":
        dj27("69")
    if pl == "Leave her":
        dj28("70")
    if pl == "Watch her":
        dj28("71")
    if pl == "Trust her":
        dj28("72")
    if pl == "Johnny":
        dj29("73")
    if pl == "Timmy":
        dj29("74")
    if pl == "Frodo":
        dj29("75")
    if pl == "Leave her":
        dj30("76")
    if pl == "Watch her":
        dj30("77")
    if pl == "Trust her":
        dj30("78")
    if pl == "Oh, leave her":
        dj31("79")
    if pl == "Oh, watch her":
        dj31("80")
    if pl == "Oh, trust her":
        dj31("81")
    if pl == "Johnny":
        dj32("82")
    if pl == "Timmy":
        dj32("83")
    if pl == "Frodo":
        dj32("84")
    if pl == "Leave her":
        dj33("85")
    if pl == "Watch her":
        dj33("86")
    if pl == "Trust her":
        dj33("87")
    if pl == "For the voyage is long":
        dj34("88")
    if pl == "For the voyage is short":
        dj34("89")
    if pl == "For the voyage is wild":
        dj34("90")
    if pl == "And the winds don't blow":
        dj35("91")
    if pl == "And it's time for us":
        dj36("92")
    if pl == "To leave her":
        dj37("93")
    if pl == "To watch her":
        dj37("94")
    if pl == "To trust her":
        dj37("95")
    if pl == "Leave her":
        dj38("96")
    if pl == "Watch her":
        dj38("97")
    if pl == "Trust her":
        dj38("98")
    if pl == "Johnny":
        dj39("99")
    if pl == "Timmy":
        dj39("100")
    if pl == "Frodo":
        dj39("101")
    if pl == "Leave her":
        dj40("102")
    if pl == "Watch her":
        dj40("103")
    if pl == "Trust her":
        dj40("104")
    if pl == "Oh, leave her":
        dj41("105")
    if pl == "Oh, watch her":
        dj41("106")
    if pl == "Oh, trust her":
        dj41("107")
    if pl == "Johnny":
        dj42("108")
    if pl == "Timmy":
        dj42("109")
    if pl == "Frodo":
        dj42("110")
    if pl == "Leave her":
        dj43("111")
    if pl == "Watch her":
        dj43("112")
    if pl == "Trust her":
        dj43("113")
    if pl == "For the voyage is long":
        dj44("114")
    if pl == "For the voyage is short":
        dj44("115")
    if pl == "For the voyage is wild":
        dj44("116")
    if pl == "And the winds don't blow":
        dj45("117")
    if pl == "And it's time for us":
        dj46("118")
    if pl == "To leave her":
        dj47("119")
    if pl == "To watch her":
        dj47("120")
    if pl == "To trust her":
        dj47("121")


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
