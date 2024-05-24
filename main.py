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
background_image.place(x=0, y=0)
digitalbard_font = ("Lucida Calligraphy", 14)
selection1 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection2 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection3 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection4 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection5 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection6 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection7 = Label(win, bg="gray14", fg="gold", text="", width=5)
selection8 = Label(win, bg="gray14", fg="gold", text="", width=5)
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
    digitalbard_messages.config(text="You will be shown various song options in groups of three items.", padx=10,
                                pady=10)
    digitalbard_messagesline2.config(text="You may choose one item from each group.", wraplength=500, padx=10, pady=10)
    proceed.place(x=50, y=100)


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
    interview()
    selection8.config(text="Foul")
    cue8(choice="Foul")


def interview():
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load("interview01.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.queue("interview02.mp3")
    pygame.mixer.music.queue("interview03.mp3")
    pygame.mixer.music.queue("interview04.mp3")
    pygame.mixer.music.queue("interview05.mp3")
    herewego()


def letschoosefcw_c():
    button_boom("fcw")
    interview()
    selection8.config(text="Cold")
    cue8(choice="Cold")


def herewego():
    selection1.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    selection2.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    selection3.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    selection4.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    selection5.grid(row=5, column=1, padx=10, pady=10, sticky=W)
    selection6.grid(row=6, column=1, padx=10, pady=10, sticky=W)
    selection7.grid(row=7, column=1, padx=10, pady=10, sticky=W)
    selection8.grid(row=8, column=1, padx=10, pady=10, sticky=W)
    button_heresyoursong.grid(row=9, column=1, padx=10, pady=10, sticky=W)

def letschoosefcw_w():
    button_boom("fcw")
    interview()
    selection8.config(text="Weird")
    cue8(choice="Weird")


def isiton():
    while True:
        if not play.get_busy():
            break
        else:
            continue


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
        isiton()


def cue1(choice):
    if choice == "I":
        track01 = "I"
    if choice == "They":
        track02 = "They"
    if choice == "We":
        track03 = "We"


def cue2(choice):
    if choice == "Old":
        track04 = "Old"
    if choice == "Tall":
        track05 = pygame.mixer.Sound("tt.mp3")
    if choice == "Sad":
        track06 = pygame.mixer.Sound("ts.mp3")


def cue3(choice):
    if choice == "Leave":
        track07 = pygame.mixer.Sound("lher_one.mp3")
        track06 = pygame.mixer.Sound("lher_two.mp3")
        track10 = pygame.mixer.Sound("tlher_one.mp3")
        track11 = pygame.mixer.Sound("lher_one.mp3")
        track13 = pygame.mixer.Sound("lher_two.mp3")
        track14 = pygame.mixer.Sound("olher_one.mp3")
        track16 = pygame.mixer.Sound("lher_three.mp3")
        track20 = pygame.mixer.Sound("tlher_one.mp3")
        track22 = pygame.mixer.Sound("lher_one.mp3")
        track24 = pygame.mixer.Sound("lher_two.mp3")
        track27 = pygame.mixer.Sound("tlher_one.mp3")
        track28 = pygame.mixer.Sound("lher_one.mp3")
        track30 = pygame.mixer.Sound("lher_two.mp3")
        track31 = pygame.mixer.Sound("olher_one.mp3")
        track33 = pygame.mixer.Sound("lher_three.mp3")
        track37 = pygame.mixer.Sound("tlher_one.mp3")
        track38 = pygame.mixer.Sound("lher_one.mp3")
        track40 = pygame.mixer.Sound("lher_two.mp3")
        track41 = pygame.mixer.Sound("olher_one.mp3")
        track43 = pygame.mixer.Sound("lher_three.mp3")
        track47 = pygame.mixer.Sound("tlher_one.mp3")
        track06 = pygame.mixer.Sound("lher_two.mp3")
        track10 = pygame.mixer.Sound("tlher_one.mp3")
        track11 = pygame.mixer.Sound("lher_one.mp3")
        track13 = pygame.mixer.Sound("lher_two.mp3")
        track14 = pygame.mixer.Sound("olher_one.mp3")
        track16 = pygame.mixer.Sound("lher_three.mp3")
        track20 = pygame.mixer.Sound("tlher_one.mp3")
        track22 = pygame.mixer.Sound("lher_one.mp3")
        track24 = pygame.mixer.Sound("lher_two.mp3")
        track27 = pygame.mixer.Sound("tlher_one.mp3")
        track28 = pygame.mixer.Sound("lher_one.mp3")
        track30 = pygame.mixer.Sound("lher_two.mp3")
        track31 = pygame.mixer.Sound("olher_one.mp3")
        track33 = pygame.mixer.Sound("lher_three.mp3")
        track37 = pygame.mixer.Sound("tlher_one.mp3")
        track38 = pygame.mixer.Sound("lher_one.mp3")
        track40 = pygame.mixer.Sound("lher_two.mp3")
        track41 = pygame.mixer.Sound("olher_one.mp3")
        track43 = pygame.mixer.Sound("lher_three.mp3")
        track47 = pygame.mixer.Sound("tlher_one.mp3")
    if choice == "Watch":
        track04 = pygame.mixer.Sound("wher_one.mp3")
        track06 = pygame.mixer.Sound("wher_two.mp3")
        track10 = pygame.mixer.Sound("twher_one.mp3")
        track11 = pygame.mixer.Sound("wher_one.mp3")
        track13 = pygame.mixer.Sound("wher_two.mp3")
        track14 = pygame.mixer.Sound("owher_one.mp3")
        track16 = pygame.mixer.Sound("wher_three.mp3")
        track20 = pygame.mixer.Sound("twher_one.mp3")
        track22 = pygame.mixer.Sound("wher_one.mp3")
        track24 = pygame.mixer.Sound("wher_two.mp3")
        track27 = pygame.mixer.Sound("twher_one.mp3")
        track28 = pygame.mixer.Sound("wher_one.mp3")
        track30 = pygame.mixer.Sound("wher_two.mp3")
        track31 = pygame.mixer.Sound("owher_one.mp3")
        track33 = pygame.mixer.Sound("wher_three.mp3")
        track37 = pygame.mixer.Sound("twher_one.mp3")
        track38 = pygame.mixer.Sound("wher_one.mp3")
        track40 = pygame.mixer.Sound("wher_two.mp3")
        track41 = pygame.mixer.Sound("owher_one.mp3")
        track43 = pygame.mixer.Sound("wher_three.mp3")
        track47 = pygame.mixer.Sound("twher_one.mp3")
    if choice == "Trust":
        track04 = pygame.mixer.Sound("trher_one.mp3")
        track06 = pygame.mixer.Sound("trher_two.mp3")
        track10 = pygame.mixer.Sound("ttrher_one.mp3")
        track11 = pygame.mixer.Sound("trher_one.mp3")
        track13 = pygame.mixer.Sound("trher_two.mp3")
        track14 = pygame.mixer.Sound("otrher_one.mp3")
        track16 = pygame.mixer.Sound("trher_three.mp3")
        track20 = pygame.mixer.Sound("ttrher_one.mp3")
        track22 = pygame.mixer.Sound("trher_one.mp3")
        track24 = pygame.mixer.Sound("trher_two.mp3")
        track27 = pygame.mixer.Sound("ttrher_one.mp3")
        track28 = pygame.mixer.Sound("trher_one.mp3")
        track30 = pygame.mixer.Sound("trher_two.mp3")
        track31 = pygame.mixer.Sound("otrher_one.mp3")
        track33 = pygame.mixer.Sound("trher_three.mp3")
        track37 = pygame.mixer.Sound("ttrher_one.mp3")
        track38 = pygame.mixer.Sound("trher_one.mp3")
        track40 = pygame.mixer.Sound("trher_two.mp3")
        track41 = pygame.mixer.Sound("otrher_one.mp3")
        track43 = pygame.mixer.Sound("trher_three.mp3")
        track47 = pygame.mixer.Sound("ttrher_one.mp3")
def cue4(choice):
    if choice == "Johnny":
        track05 = pygame.mixer.Sound("johnny_one.mp3")
        track12 = pygame.mixer.Sound("johnny_one.mp3")
        track15 = pygame.mixer.Sound("johnny_two.mp3")
        track23 = pygame.mixer.Sound("johnny_one.mp3")
        track29 = pygame.mixer.Sound("johnny_one.mp3")
        track32 = pygame.mixer.Sound("johnny_two.mp3")
        track39 = pygame.mixer.Sound("johnny_one.mp3")
        track42 = pygame.mixer.Sound("johnny_one.mp3")
    if choice == "Timmy":
        track05 = pygame.mixer.Sound("timmy_one.mp3")
        track12 = pygame.mixer.Sound("timmy_one.mp3")
        track15 = pygame.mixer.Sound("timmy_two.mp3")
        track23 = pygame.mixer.Sound("timmy_one.mp3")
        track29 = pygame.mixer.Sound("timmy_one.mp3")
        track32 = pygame.mixer.Sound("timmy_two.mp3")
        track39 = pygame.mixer.Sound("timmy_one.mp3")
        track42 = pygame.mixer.Sound("timmy_one.mp3")
    if choice == "Frodo":
        track05 = pygame.mixer.Sound("frodo_one.mp3")
        track12 = pygame.mixer.Sound("frodo_one.mp3")
        track15 = pygame.mixer.Sound("frodo_two.mp3")
        track23 = pygame.mixer.Sound("frodo_one.mp3")
        track29 = pygame.mixer.Sound("frodo_one.mp3")
        track32 = pygame.mixer.Sound("frodo_two.mp3")
        track39 = pygame.mixer.Sound("frodo_one.mp3")
        track42 = pygame.mixer.Sound("frodo_one.mp3")
def cue5(choice):
    if choice == "Tomorrow":
        track07 = pygame.mixer.Sound("tyw.mp3")
    if choice == "Next Tuesday":
        track07 = pygame.mixer.Sound("ntyw.mp3")
    if choice == "On Friday":
        track07 = pygame.mixer.Sound("ofyw.mp3")


def cue6(choice):
    if choice == "Pay":
        track08 = pygame.mixer.Sound("getyp.mp3")
    if choice == "Bell":
        track08 = pygame.mixer.Sound("getyb.mp3")
    if choice == "Fish":
        track08 = pygame.mixer.Sound("getyf.mp3")


def cue7(choice):
    if choice == "Long":
        track17 = pygame.mixer.Sound("ftvil.mp3")
        track34 = pygame.mixer.Sound("ftvil.mp3")
        track44 = pygame.mixer.Sound("ftvil.mp3")
    if choice == "Short":
        track17 = pygame.mixer.Sound("ftvis.mp3")
        track34 = pygame.mixer.Sound("ftvis.mp3")
        track44 = pygame.mixer.Sound("ftvis.mp3")
    if choice == "Wild":
        track17 = pygame.mixer.Sound("ftviw.mp3")
        track34 = pygame.mixer.Sound("ftviw.mp3")
        track44 = pygame.mixer.Sound("ftviw.mp3")

def cue8(choice):
    if choice == "Foul":
        track21 = pygame.mixer.Sound("otwwfatsrh.mp3")
    if choice == "Cold":
        track21 = pygame.mixer.Sound("otwwcatsrh.mp3")
    if choice == "Weird":
        track21 = pygame.mixer.Sound("otwwwatsrh.mp3")


def heresyoursong():
    line1 = track01.play


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
button_heresyoursong = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Click to hear your customized song", command=heresyoursong)
# print("Photo by Kostiantyn Klymovets: https://www.pexels.com/photo/man-playing-lute-on-urban-steps-12831481/")
pygame.mixer.music.load("scarborough_fair.mp3")
pygame.mixer.music.play(-1)
digitalbard_messages = Label(image_spot, bg="black", text="", wraplength=500, font=digitalbard_font, fg="gold", padx=24,
                             pady=10, justify="left")
digitalbard_messages.config(text="Welcome to your free trial of Digital Bard.")
digitalbard_messagesline2 = Label(image_spot,
                                  bg="black", text="Please enjoy this sample from our sea shanty collection.",
                                  wraplength=500, font=digitalbard_font, fg="gold", padx=10, pady=10, justify="left")
digitalbard_messages.place(x=50, y=200)
digitalbard_messagesline2.place(x=50, y=350)
proceed = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Continue",
                 command=letschoose_itw)
start = Button(win, bg="forest green", fg="black", font=digitalbard_font, text="Start", width=5, command=instructions)
start.place(x=50, y=100)
win.mainloop()
