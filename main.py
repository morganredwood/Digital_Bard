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
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.unload()
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
    spinitnow1(track)
    spinitnow2(track)
    spinitnow3(track)
    spinitnow4(track)
    spinitnow5(track)
    spinitnow6(track)
    spinitnow7(track)
    spinitnow8(track)
    spinitnow9(track)
    spinitnow10(track)
    spinitnow11(track)
    spinitnow12(track)
    spinitnow13(track)
    spinitnow14(track)
    spinitnow15(track)
    spinitnow16(track)
    spinitnow17(track)
    spinitnow18(track)
    spinitnow19(track)
    spinitnow20(track)
    spinitnow21(track)
    spinitnow22(track)
    spinitnow23(track)
    spinitnow24(track)
    spinitnow25(track)
    spinitnow26(track)
    spinitnow27(track)
    spinitnow28(track)
    spinitnow29(track)
    spinitnow30(track)
    spinitnow31(track)
    spinitnow32(track)
    spinitnow33(track)
    spinitnow34(track)
    spinitnow35(track)
    spinitnow36(track)
    spinitnow37(track)
    spinitnow38(track)
    spinitnow39(track)
    spinitnow40(track)
    spinitnow41(track)
    spinitnow42(track)
    spinitnow43(track)
    spinitnow44(track)
    spinitnow45(track)
    spinitnow46(track)
    spinitnow47(track)


def letschoosefcw_w():
    button_boom("fcw")
    selection8.config(text="Weird")
    cue8(choice="Weird")
    herewego()


def spinitnow1(track):
    while True:
        if track == "1":
            pygame.mixer.music.load("itih.mp3")
            break
        if track == "2":
            pygame.mixer.music.load("ttth.mp3")
            break
        if track == "3":
            pygame.mixer.music.load("wtwh.mp3")
            break


def spinitnow2(track):
    while True:
        if track == "4":
           pygame.mixer.music.queue("to.mp3")
           break
        if track == "5":
            pygame.mixer.music.queue("tt.mp3")
            break
        if track == "6":
            pygame.mixer.music.load("ts.mp3")
            break


def spinitnow3(track):
    if track == "7":
        pygame.mixer.music.queue("ms.mp3")


def spinitnow4(track):
    while True:
        if track == "8":
            pygame.mixer.music.queue("lher_one.mp3")
            break
        if track == "9":
            pygame.mixer.music.queue("wher_one.mp3")
            break
        if track == "10":
            pygame.mixer.music.queue("trher_one.mp3")
            break

def spinitnow5(track):
    while True:
        if track == "11":
            pygame.mixer.music.queue("johnny_one.mp3")
            break
        if track == "12":
            pygame.mixer.music.queue("timmy_one.mp3")
            break
        if track == "13":
            pygame.mixer.music.queue("frodo_one.mp3")
            break


def spinitnow6(track):
    while True:
        if track == "14":
            pygame.mixer.music.queue("lher_two.mp3")
        if track == "15":
            pygame.mixer.music.queue("wher_two.mp3")
            break
        if track == "16":
            pygame.mixer.music.queue("trher_two.mp3")
            break


def spinitnow7(track):
    while True:
        if track == "17":
            pygame.mixer.music.queue("tyw.mp3")
            break
        if track == "18":
            pygame.mixer.music.queue("ntyw.mp3")
            break
        if track == "19":
            pygame.mixer.music.queue("ofyw.mp3")
            break


def spinitnow8(track):
    while True:
        if track == "20":
            pygame.mixer.music.queue("getyp.mp3")
            break
        if track == "21":
            pygame.mixer.music.queue("getyb.mp3")
            break
        if track == "22":
            pygame.mixer.music.queue("getyf.mp3")
            break


def spinitnow9(track):
    while True:
        if track == "23":
            pygame.mixer.music.queue("aitfu.mp3")
            break


def spinitnow10(track):
    while True:
        if track == "24":
            pygame.mixer.music.queue("tlher_one.mp3")
            break
        if track == "25":
            pygame.mixer.music.queue("twher_one.mp3")
            break
        if track == "26":
            pygame.mixer.music.queue("ttrher_one.mp3")
def spinitnow11(track):
    while True:
        if track == "27":
            pygame.mixer.music.queue("lher_one.mp3")
            break
        if track == "28": 
            pygame.mixer.music.queue("wher_one.mp3")
            break
        if track == "29":   
            pygame.mixer.music.queue("trher_one.mp3")
            break


def spinitnow12(track):
    while True:  
        if track == "30":
            pygame.mixer.music.queue("johnny_one.mp3")
            break 
        if track == "31":  
            pygame.mixer.music.queue("timmy_one.mp3")
            break
        if track == "32":  
            pygame.mixer.music.queue("frodo_one.mp3")
            break


def spinitnow13(track):
    while True: 
        if track == "33":
            pygame.mixer.music.queue("lher_two.mp3")
            break
        if track == "34":
            pygame.mixer.music.queue("wher_two.mp3")
            break
        if track == "35":
            pygame.mixer.music.queue("trher_two.mp3")
            break


def spinitnow14(track):
    while True:
        if track == "36":
            pygame.mixer.music.queue("olher_one.mp3")
            break
        if track == "37":
            pygame.mixer.music.queue("olher_one.mp3")
            break
        if track == "38":
            pygame.mixer.music.queue("olher_one.mp3")
            break


def spinitnow15(track):
    while True:
        if track == "39":
            pygame.mixer.music.queue("johnny_two.mp3")
            break
        if track == "40":
            pygame.mixer.music.queue("timmy_two.mp3")
            break
        if track == "41":
            pygame.mixer.music.queue("frodo_two.mp3")
            break 


def spinitnow16(track):
    while True:
        if track == "42":
            pygame.mixer.music.queue("lher_three.mp3")
            break
        if track == "43":
            pygame.mixer.music.queue("wher_three.mp3")
            break
        if track == "44":
            pygame.mixer.music.queue("trher_three.mp3")
            break


def spinitnow17(track):
    while True:
        if track == "45":
            pygame.mixer.music.queue("ftvil.mp3")
            break 
        if track == "46":
            pygame.mixer.music.queue("ftvis.mp3")
            break
        if track == "47":
            pygame.mixer.music.queue("ftviw.mp3")
            break


def spinitnow18(track):
    while True:
        if track == "48":
            pygame.mixer.music.queue("atwdb.mp3")
            break


def spinitnow19(track):
    while True:
        if track == "49":
            pygame.mixer.music.queue("aitfu.mp3")
            break


def spinitnow20(track):
    while True:
        if track == "50":
            pygame.mixer.music.queue("tlher_one.mp3 ")
            break
        if track == "51":  
            pygame.mixer.music.queue("twher_one.mp3")
            break
        if track == "52":
            pygame.mixer.music.queue("ttrher_one.mp3")
            break


def spinitnow21(track):
    while True:
        if track == "53":
            pygame.mixer.music.queue("otwwfatsrh.mp3")
            break
        if track == "54":   
            pygame.mixer.music.queue("otwwcatsrh.mp3")
            break
        if track == "55":   
            pygame.mixer.music.queue("otwwwatsrh.mp3")
            break


def spinitnow22(track):
    while True:
        if track == "56":
            pygame.mixer.music.queue("lher_one.mp3")
            break
        if track == "57":
            pygame.mixer.music.queue("wher_one.mp3")
            break
        if track == "58":  
            pygame.mixer.music.queue("trher_one.mp3")
            break


def spinitnow23(track):
      59      pygame.mixer.music.queue("johnny_one.mp3")
       60     pygame.mixer.music.queue("timmy_one.mp3")
      61      pygame.mixer.music.queue("frodo_one.mp3")
def spinitnow24(track):
      62      pygame.mixer.music.queue("lher_two.mp3")
       63     pygame.mixer.music.queue("wher_two.mp3")
      64      pygame.mixer.music.queue("trher_two.mp3")
def spinitnow25(track):
       65     pygame.mixer.music.queue("ssiganwb.mp3")
def spinitnow26(track):
       66     pygame.mixer.music.queue("aitfu.mp3")
def spinitnow27(track):
      67      pygame.mixer.music.queue("tlher_one.mp3")
       68     pygame.mixer.music.queue("twher_one.mp3")
       69     pygame.mixer.music.queue("ttrher_one.mp3")
def spinitnow28(track):
      70      pygame.mixer.music.queue("lher_one.mp3")
        71    pygame.mixer.music.queue("wher_one.mp3")
        72    pygame.mixer.music.queue("trher_one.mp3")
def spinitnow29(track):
      73      pygame.mixer.music.queue("johnny_one.mp3")
       74     pygame.mixer.music.queue("timmy_one.mp3")
        75    pygame.mixer.music.queue("frodo_one.mp3")
def spinitnow30(track):
      76      pygame.mixer.music.queue("lher_two.mp3")
       77     pygame.mixer.music.queue("wher_two.mp3")
       78     pygame.mixer.music.queue("trher_two.mp3")
def spinitnow31(track):
      79      pygame.mixer.music.queue("olher_one.mp3")
       80     pygame.mixer.music.queue("owher_one.mp3")
       81     pygame.mixer.music.queue("otrher_one.mp3")
def spinitnow32(track):
      82      pygame.mixer.music.queue("johnny_two.mp3")
      83      pygame.mixer.music.queue("timmy_two.mp3")
      84      pygame.mixer.music.queue("frodo_two.mp3")
def spinitnow33(track):
      85      pygame.mixer.music.queue("lher_three.mp3")
      86      pygame.mixer.music.queue("wher_three.mp3")
      87      pygame.mixer.music.queue("trher_three.mp3")
def spinitnow34(track):
      88      pygame.mixer.music.queue("ftvil.mp3")
      89      pygame.mixer.music.queue("ftvis.mp3")
      90      pygame.mixer.music.queue("ftviw.mp3")
def spinitnow35(track):
       91     pygame.mixer.music.queue("atwdb.mp3")
def spinitnow36(track):
        92    pygame.mixer.music.queue("aitfu.mp3")
def spinitnow37(track):
       93     pygame.mixer.music.queue("tlher_one.mp3 ")
        94    pygame.mixer.music.queue("twher_one.mp3")
       95     pygame.mixer.music.queue("ttrher_one.mp3")
def spinitnow38(track):
      96      pygame.mixer.music.queue("lher_one.mp3")
      97      pygame.mixer.music.queue("wher_one.mp3")
       98     pygame.mixer.music.queue("trher_one.mp3")
def spinitnow39(track):
     99       pygame.mixer.music.queue("johnny_one.mp3")
      100      pygame.mixer.music.queue("timmy_one.mp3")
     101       pygame.mixer.music.queue("frodo_one.mp3")
def spinitnow40(track):
     102       pygame.mixer.music.queue("lher_two.mp3")
      103      pygame.mixer.music.queue("wher_two.mp3")
      104      pygame.mixer.music.queue("trher_two.mp3")
def spinitnow41(track):
    105        pygame.mixer.music.queue("olher_one.mp3")
      106      pygame.mixer.music.queue("owher_one.mp3")
     107       pygame.mixer.music.queue("otrher_one.mp3")
def spinitnow42(track):
   108         pygame.mixer.music.queue("johnny_two.mp3")
     109       pygame.mixer.music.queue("timmy_two.mp3")
    110        pygame.mixer.music.queue("frodo_two.mp3")
def spinitnow43(track):
    111        pygame.mixer.music.queue("lher_three.mp3")
   112         pygame.mixer.music.queue("wher_three.mp3")
  113        pygame.mixer.music.queue("trher_three.mp3")
def spinitnow44(track):
 114           pygame.mixer.music.queue("ftvil.mp3")
 115           pygame.mixer.music.queue("ftvis.mp3")
 116           pygame.mixer.music.queue("ftviw.mp3")
def spinitnow45(track):
117            pygame.mixer.music.queue("atwdb.mp3")
def spinitnow46(track):
    while True:
 118           pygame.mixer.music.queue("aitfu.mp3")
def spinitnow47(track):
    while True:
119            if pygame.mixer.music.queue("tlher_one.mp3")
                pygame.mixer.music.queue("twher_one.mp3")
                pygame.mixer.music.queue("ttrher_one.mp3")


def cue1(choice):
    while True:
        if choice == "I":
            break
        if choice == "They":
            break
        if choice == "We":
            break
    print(choice)


def cue2(choice):
    while True:
        if choice == "Old":
            break
        if choice == "Tall":
            break
        if choice == "Sad":
            break
    print(choice)


def cue3(choice):
    while True:
        if choice == "Leave":
            break
        if choice == "Watch":
            break
        if choice == "Trust":
            break
    print(choice)


def cue4(choice):
    while True:
        if choice == "Johnny":
            break
        if choice == "Timmy":
            break
        if choice == "Frodo":
            break
    print(choice)


def cue5(choice):
    while True:
        if choice == "Tomorrow":
            break
        if choice == "Next Tuesday":
            break
        if choice == "On Friday":
            break
    print(choice)


def cue6(choice):
    while True:
        if choice == "Pay":
            break
        if choice == "Bell":
            break
        if choice == "Fish":
            break
    print(choice)


def cue7(choice):
    while True:
        if choice == "Long":
            break
        if choice == "Short":
            break
        if choice == "Wild":
            break
    print(choice)


def cue8(choice):
    while True:
        if choice == "Foul":
            break
        if choice == "Cold":
            break
        if choice == "Wild":
            break
    print(choice)


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


#   I thought I heard
def dj1(tracknumber):
    while True:
        if tracknumber == "1":
            break
        if tracknumber == "2":
            break
        if tracknumber == "3":
            break
    spinitnow1(print(tracknumber))


#   The Old Man say
def dj2(tracknumber):
    while True:
        if tracknumber == "4":
            break
        if tracknumber == "5":
            break
        if tracknumber == "6":
            break
    spinitnow2(print(tracknumber))


def dj3(tracknumber):
    if tracknumber == "7":
    spinitnow3(print(tracknumber))


#   Leave her, Johnny, leave her
def dj4(tracknumber):
    while True:
        if tracknumber == "8":
            break
        if tracknumber == "9":
            break
        if tracknumber == "10":
            break
    spinitnow1(print(tracknumber))


def dj5(tracknumber):
    while True:
        if tracknumber == "11":
            break
        if tracknumber == "12":
            break
        if tracknumber == "13":
            break
    spinitnow5(print(tracknumber))


def dj6(tracknumber):
    while True:
        if tracknumber == "14":
            break
        if tracknumber == "15":
            break
        if tracknumber == "16":
            break
    spinitnow6(print(tracknumber))


#   Tomorrow, ye will get your pay
def dj7(tracknumber):
    while True:
        if tracknumber == "17":
            break
        if tracknumber == "18":
            break
        if tracknumber == "19":
            break
    spinitnow7(print(tracknumber))


def dj8(tracknumber):
    while True:
        if tracknumber == "20":
            break
        if tracknumber == "21":
            break
        if tracknumber == "22":
            break
    spinitnow8(print(tracknumber))


def dj9(tracknumber):
    while True:
        if tracknumber == "23":
            break
    spinitnow9(print(tracknumber))


def dj10(tracknumber):
    while True:
        if tracknumber == "24":
            break
        if tracknumber == "25":
            break
        if tracknumber == "26":
            break
    spinitnow10(print(tracknumber))


def dj11(tracknumber):
    while True:
        if tracknumber == "27":
            break
        if tracknumber == "28":
            break
        if tracknumber == "29":
            break
    spinitnow11(print(tracknumber))


def dj12(tracknumber):
    while True:
        if tracknumber == "30":
            break
        if tracknumber == "31":
            break
        if tracknumber == "32":
            break
    spinitnow12(print(tracknumber))


def dj13(tracknumber):
    while True:
        if tracknumber == "33":
            break
        if tracknumber == "34":
            break
        if tracknumber == "35":
            break
    spinitnow13(print(tracknumber))


def dj14(tracknumber):
    while True:
        if tracknumber == "36":
            break
        if tracknumber == "37":
            break
        if tracknumber == "38":
            break
    spinitnow14(print(tracknumber))


def dj15(tracknumber):
    while True:
        if tracknumber == "39":
            break
        if tracknumber == "40":
            break
        if tracknumber == "41":
            break
    spinitnow15(print(tracknumber))


def dj16(tracknumber):
    while True:
        if tracknumber == "42":
            break
        if tracknumber == "43":
            break
        if tracknumber == "44":
            break
    spinitnow16(print(tracknumber))


#   For the voyage is long, and the winds don't blow
def dj17(tracknumber):
    while True:
        if tracknumber == "45":
            break
        if tracknumber == "46":
            break
        if tracknumber == "47":
            break
    spinitnow17(print(tracknumber))


def dj18(tracknumber):
    while True:
        if tracknumber == "48":
            break
    spinitnow18(print(tracknumber))

#   And it's time for us to leave her
def dj19(tracknumber):
    while True:
        if tracknumber == "49":
            break
    spinitnow19(print(tracknumber))


def dj20(tracknumber):
    while True:
        if tracknumber == "50":
        if tracknumber == "51":
            break
        if tracknumber == "52":
            break
    spinitnow20(print(tracknumber))
#   Oh, the wind was foul, and the sea ran high


def dj21(tracknumber):
    while True:
        if tracknumber == "53":
            break
        if tracknumber == "54":
            break
        if tracknumber == "55":
            break
    spinitnow21(print(tracknumber))


#   Leave her, Johnny, leave her
def dj22(tracknumber):
    while True:
        if tracknumber == "56":
            break
        if tracknumber == "57":
            break
        if tracknumber == "58":
            break
    spinitnow22(print(tracknumber))


def dj23(tracknumber):
    while True:
        if tracknumber == "59":
            break
        if tracknumber == "60":
            break
        if tracknumber == "61":
            break
    spinitnow23(print(tracknumber))


def dj24(tracknumber):
    while True:
        if tracknumber == "62":
            break
        if tracknumber == "63":
            break
        if tracknumber == "64":
            break
    spinitnow24(print(tracknumber))
#   She shipped it green, and none went by


def dj25(tracknumber):
    while True:
        if tracknumber == "65":
            break
#   And it's time for us to leave her
    spinitnow25(print(tracknumber))


def dj26(tracknumber):
    while True:
        if tracknumber == "66":
            break
    spinitnow26(print(tracknumber))

def dj27(tracknumber):
    while True:
        if tracknumber == "67":
            break
        if tracknumber == "68":
            break
        if tracknumber == "69":
            break
    spinitnow27(print(tracknumber))


#   Leave her, Johnny, leave her
def dj28(tracknumber):
    while True:
        if tracknumber == "70":
            break
        if tracknumber == "71":
            break
        if tracknumber == "72":
            break
    spinitnow28(print(tracknumber))


def dj29(tracknumber):
    while True:
        if tracknumber == "73":
            break
        if tracknumber == "74":
            break
        if tracknumber == "75":
            break
    spinitnow29(print(tracknumber))


def dj30(tracknumber):
    while True:
        if tracknumber == "76":
            break
        if tracknumber == "77":
            break
        if tracknumber == "78":
            break
    spinitnow30(print(tracknumber))


#   Oh, leave her, Johnny, leave her
def dj31(tracknumber):
    while True:
        if tracknumber == "79":
            break
        if tracknumber == "80":
            break
        if tracknumber == "81":
            break
    spinitnow31(print(tracknumber))


def dj32(tracknumber):
    while True:
        if tracknumber == "82":
            break
        if tracknumber == "83":
            break
        if tracknumber == "84":
            break
    spinitnow32(print(tracknumber))


def dj33(tracknumber):
    while True:
        if tracknumber == "85":
            break
        if tracknumber == "86":
            break
        if tracknumber == "87":
            break
    spinitnow33(print(tracknumber))


#   For the voyage is long, and the winds don't blow
def dj34(tracknumber):
    while True:
        if tracknumber == "88":
            break
        if tracknumber == "89":
            break
        if tracknumber == "90":
            break
    spinitnow34(print(tracknumber))


def dj35(tracknumber):
    while True:
        if tracknumber == "91":
            break
    spinitnow35(print(tracknumber))


#   And it's time for us to leave her
def dj36(tracknumber):
    while True:
        if tracknumber == "92":
            break
    spinitnow36(print(tracknumber))

def dj37(tracknumber):
    while True:
        if tracknumber == "93":
        if tracknumber == "94":
            break
        if tracknumber == "95":
            break
    spinitnow37(print(tracknumber))


#   Leave her, Johnny, leave her
def dj38(tracknumber):
    while True:
        if tracknumber == "96":
            break
        if tracknumber == "97":
            break
        if tracknumber == "98":
            break
    spinitnow38(print(tracknumber))


def dj39(tracknumber):
    while True:
        if tracknumber == "99":
            break
        if tracknumber == "100":
            break
        if tracknumber == "101":
            break
    spinitnow39(print(tracknumber))


def dj40(tracknumber):
    while True:
        if tracknumber == "102":
            break
        if tracknumber == "103":
            break
        if tracknumber == "104":
            break
    spinitnow40(print(tracknumber))


#   Oh, leave her, Johnny, leave her
def dj41(tracknumber):
    while True:
        if tracknumber == "105":
            break
        if tracknumber == "106":
            break
        if tracknumber == "107":
            break
    spinitnow41(print(tracknumber))


def dj42(tracknumber):
    while True:
        if tracknumber == "108":
            break
        if tracknumber == "109":
            break
        if tracknumber == "110":
            break
    spinitnow42(print(tracknumber))


def dj43(tracknumber):
    while True:
        if tracknumber == "111":
            break
        if tracknumber == "112":
            break
        if tracknumber == "113":
            break
    spinitnow43(print(tracknumber))


#   For the voyage is long, and the winds don't blow
def dj44(tracknumber):
    while True:
        if tracknumber == "114":
            break
        if tracknumber == "115":
            break
        if tracknumber == "116":
            break
    spinitnow44(print(tracknumber))


def dj45(tracknumber):
    while True:
        if tracknumber == "117":
            break
    spinitnow45(print(tracknumber))


#   And it's time for us to leave her
def dj46(tracknumber):
    while True:
        if tracknumber == "118":
            break
    spinitnow46(print(tracknumber))


def dj47(tracknumber):
    while True:
        if tracknumber == "119":
            break
        if tracknumber == "120":
            break
        if tracknumber == "121":
            break
    spinitnow47(print(tracknumber))


def playlist(pl):
    while True:
        if pl == "I thought I heard":
            dj1("1")
            break
        if pl == "They thought they heard":
            dj1("2")
            break
        if pl == "We thought we heard":
            dj1("3")
            break
    while True:
        if pl == "The Old":
            dj2("4")
            break
        if pl == "The Tall":
            dj2("5")
            break
        if pl == "The Sad":
            dj2("6")
            break
    while True:
        if pl == "Man say":
            dj3("7")
            break
    while True:
        if pl == "Leave her":
            dj4("8")
            break
        if pl == "Watch her":
            dj4("9")
            break
        if pl == "Trust her":
            dj4("10")
            break
    while True:
        if pl == "Johnny":
            dj5("11")
            break
        if pl == "Timmy":
            dj5("12")
            break
        if pl == "Frodo":
            dj5("13")
            break
    while True:
        if pl == "Leave her":
            dj6("14")
            break
        if pl == "Watch her":
            dj6("15")
            break
        if pl == "Trust her":
            dj6("16")
            break
    while True:
        if pl == "Tomorrow, ye will":
            dj7("17")
            break
        if pl == "Next Tuesday, ye will":
            dj7("18")
            break
        if pl == "On Friday, ye will":
            dj7("19")
            break
    while True:
        if pl == "Get your pay":
            dj8("20")
            break
        if pl == "Get your bell":
            dj8("21")
            break
        if pl == "Get your fish":
            dj8("22")
            break
    while True:
        if pl == "And it's time for us":
            dj9("23")
            break
    while True:
        if pl == "To leave her":
            dj10("24")
            break
        if pl == "To watch her":
            dj10("25")
            break
        if pl == "To trust her":
            dj10("26")
            break
    while True:
        if pl == "Leave her":
            dj11("27")
            break
        if pl == "Watch her":
            dj11("28")
            break
        if pl == "Trust her":
            dj11("29")
            break
    while True:
        if pl == "Johnny":
            dj12("30")
            break
        if pl == "Timmy":
            dj12("31")
            break
        if pl == "Frodo":
            dj12("32")
            break
    while True:
        if pl == "Leave her":
            dj13("33")
            break
        if pl == "Watch her":
            dj13("34")
            break
        if pl == "Trust her":
            dj13("35")
            break
    while True:
        if pl == "Oh, leave her":
            dj14("36")
            break
        if pl == "Oh, watch her":
            dj14("37")
            break
        if pl == "Oh, trust her":
            dj14("38")
            break
    while True:
        if pl == "Johnny":
            dj15("39")
            break
        if pl == "Timmy":
            dj15("40")
            break
        if pl == "Frodo":
            dj15("41")
            break
    while True:
        if pl == "Leave her":
            dj16("42")
            break
        if pl == "Watch her":
            dj16("43")
            break
        if pl == "Trust her":
            dj16("44")
            break
    while True:
        if pl == "For the voyage is long":
            dj17("45")
            break
        if pl == "For the voyage is short":
            dj17("46")
            break
        if pl == "For the voyage is wild":
            dj17("47")
            break
    while True:
        if pl == "And the winds don't blow":
            dj18("48")
            break
    while True:
        if pl == "And it's time for us":
            dj19("49")
            break
    while True:
        if pl == "To leave her":
            dj20("50")
            break
        if pl == "To watch her":
            dj20("51")
            break
        if pl == "To trust her":
            dj20("52")
            break
    while True:
        if pl == "Oh, the wind was foul, and the sea ran high":
            dj21("53")
            break
        if pl == "Oh, the wind was cold, and the sea ran high":
            dj21("54")
            break
        if pl == "Oh, the wind was weird, and the sea ran high":
            dj21("55")
            break
    while True:
        if pl == "Leave her":
            dj22("56")
            break
        if pl == "Watch her":
            dj22("57")
            break
        if pl == "Trust her":
            dj22("58")
            break
    while True:
        if pl == "Johnny":
            dj23("59")
            break
        if pl == "Timmy":
            dj23("60")
            break
        if pl == "Frodo":
            dj23("61")
            break
    while True:
        if pl == "Leave her":
            dj24("62")
            break
        if pl == "Watch her":
            dj24("63")
            break
        if pl == "Trust her":
            dj24("64")
            break
    while True:
        if pl == "She shipped it green, and none went by":
            dj25("65")
            break
    while True:
        if pl == "And it's time for us":
            dj26("66")
            break
    while True:
        if pl == "To leave her":
            dj27("67")
            break
        if pl == "To watch her":
            dj27("68")
            break
        if pl == "To trust her":
            dj27("69")
            break
    while True:
        if pl == "Leave her":
            dj28("70")
            break
        if pl == "Watch her":
            dj28("71")
            break
        if pl == "Trust her":
            dj28("72")
            break
    while True:
        if pl == "Johnny":
            dj29("73")
            break
        if pl == "Timmy":
            dj29("74")
            break
        if pl == "Frodo":
            dj29("75")
            break
    while True:
        if pl == "Leave her":
            dj30("76")
            break
        if pl == "Watch her":
            dj30("77")
            break
        if pl == "Trust her":
            dj30("78")
            break
    while True:
        if pl == "Oh, leave her":
            dj31("79")
            break
        if pl == "Oh, watch her":
            dj31("80")
            break
        if pl == "Oh, trust her":
            dj31("81")
            break
    while True:
        if pl == "Johnny":
            dj32("82")
            break
        if pl == "Timmy":
            dj32("83")
            break
        if pl == "Frodo":
            dj32("84")
            break
    while True:
        if pl == "Leave her":
            dj33("85")
            break
        if pl == "Watch her":
            dj33("86")
            break
        if pl == "Trust her":
            dj33("87")
            break
    while True:
        if pl == "For the voyage is long":
            dj34("88")
            break
        if pl == "For the voyage is short":
            dj34("89")
            break
        if pl == "For the voyage is wild":
            dj34("90")
            break
    while True:
        if pl == "And the winds don't blow":
            dj35("91")
            break
    while True:
        if pl == "And it's time for us":
            dj36("92")
            break
    while True:
        if pl == "To leave her":
            dj37("93")
            break
        if pl == "To watch her":
            dj37("94")
            break
        if pl == "To trust her":
            dj37("95")
            break
    while True:
        if pl == "Leave her":
            dj38("96")
            break
        if pl == "Watch her":
            dj38("97")
            break
        if pl == "Trust her":
            dj38("98")
            break
    while True:
        if pl == "Johnny":
            dj39("99")
            break
        if pl == "Timmy":
            dj39("100")
            break
        if pl == "Frodo":
            dj39("101")
            break
    while True:
        if pl == "Leave her":
            dj40("102")
            break
        if pl == "Watch her":
            dj40("103")
            break
        if pl == "Trust her":
            dj40("104")
            break
    while True:
        if pl == "Oh, leave her":
            dj41("105")
            break
        if pl == "Oh, watch her":
            dj41("106")
            break
        if pl == "Oh, trust her":
            dj41("107")
            break
    while True:
        if pl == "Johnny":
            dj42("108")
            break
        if pl == "Timmy":
            dj42("109")
            break
        if pl == "Frodo":
            dj42("110")
            break
    while True:
        if pl == "Leave her":
            dj43("111")
            break
        if pl == "Watch her":
            dj43("112")
            break
        if pl == "Trust her":
            dj43("113")
            break
    while True:
        if pl == "For the voyage is long":
            dj44("114")
            break
        if pl == "For the voyage is short":
            dj44("115")
            break
        if pl == "For the voyage is wild":
            dj44("116")
            break
    while True:
        if pl == "And the winds don't blow":
            dj45("117")
            break
    while True:
        if pl == "And it's time for us":
            dj46("118")
            break
    while True:
        if pl == "To leave her":
            dj47("119")
            break
        if pl == "To watch her":
            dj47("120")
            break
        if pl == "To trust her":
            dj47("121")
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
