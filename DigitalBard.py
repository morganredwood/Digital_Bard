import pygame
from time import sleep
from time import *
pygame.init()
print("Welcome to your free trial of Digital Bard.")
sleep(3)
print("I will present you with a series of choices that will ultimately result "
      "in a customized poem for you to hear at the end of your adventure.")
sleep(3)
print("This trial includes selections from three of our premium genre paths, "
      "including our latest path, Total Chaos.")
sleep(3)
print("First, let's choose a performer for your poem.  I'll let each one of our nine sample narrators "
      "introduce himself and give a little demonstration.  All you need to do is type the number "
      "that corresponds with the performer of your choice and then press Enter.")
sleep(3)
print("Let's hear from Aloysius first.")
sleep(3)


def aloysius():
    print("Hi, I'm Aloysius, otherwise known as Narrator One.")
    sleep(3)
    print("If you must cross a course cross cow across a crowded cow crossing, "
        "cross the cross coarse cow across the crowded cow crossing carefully.")
    sleep(3)
    print("How much wood would a woodchuck chuck if a woodchuck could chuck wood?  "
        "He would chuck, he would, as much as he could, and chuck as much wood "
        "as a woodchuck would if a woodchuck could chuck wood.")
    sleep(3)


def raistlin():
    print("Narrator Two here.  My name is Raistlin.")
    sleep(3)
    print("You know New York.  You need New York.  You know you need unique New York.")
    sleep(3)
    print("A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.")
    sleep(3)


def reginald():
    print("This is Reginald, Narrator Three.")
    sleep(3)
    print("The great Greek grape growers grow great Greek grapes.")
    sleep(3)
    print("Rubber baby buggy bumpers.")
    sleep(3)


def yaxamie():
    print("My name is Yaxamie, and I'm Narrator Four.")
    sleep(3)
    print("I slit the sheet.  The sheet I slit, and on the slitted sheet I sit.")
    sleep(3)
    print("Six sick hicks nick six slick bricks with picks and sticks.")
    sleep(3)


def tasslehoff():
    print("I'm Narrator Five, Tasslehoff.")
    sleep(3)
    print("The sixth sick sheikh's sixth sheep's sick.")
    sleep(3)
    print("Linda Lou Lambert loves lemon lollipop lip gloss.")
    sleep(3)


def thadian():
    print("Thadian here, your Narrator Six.")
    sleep(3)
    print("Which wrist watches are Swiss wrist watches?")
    sleep(3)
    print("Rory the warrior and Roger the worrier were reared wrongly in a rural brewery.")
    sleep(3)


def morgan():
    print("This is Morgan, Narrator Seven.")
    sleep(3)
    print("One One was a race horse.  Two Two was one too.  One One won one race.  Two Two won one too.")
    sleep(3)
    print("A synonym for cinnamon is a cinnamon synonym.")
    sleep(3)
    print("Betty bought butter, but the butter was bitter, so Betty bought better butter "
          "to make the bitter butter better.")
    sleep(3)


def patrick():
    print("I'm Patrick, Narrator Eight.")
    sleep(3)
    print("I thought a thought, but the thought I thought wasn't the thought I thought I thought.  "
                          "If the thought I thought had been the thought I thought, I wouldn't have thought I thought.")
    sleep(3)
    print("Susie works in a shoeshine shop.  where she shines, she sits, and where she sits, she shines.")
    sleep(3)
    
    
def vincent():
        print("Last but not least, I'm Narrator Nine, Vincent.  Nice to meet you, adventurer.")
        sleep(3)
        print("Brisk, brave brigadiers brandished broad, bright blades, blunderbusses, and bludgeons, "
              "balancing them badly.")
        sleep(3)
        print("Lesser leather never weathered wetter weather better.")
        sleep(3)
        print("Fresh French fried fly fritters.")
        sleep(3)
        
        
#   Main Branch Decision Loop 1:  Choose a narrator for your finished poem.
while True:
    aloysius()
    raistlin()
    reginald()
    yaxamie()
    tasslehoff()
    thadian()
    morgan()
    patrick()
    vincent()
    print("1    Aloysius") 
    print("2    Raistlin")
    print("3    Reginald")
    print("4    Yaxamie")
    print("5    Tasslehoff")    
    print("6    Thadian")
    print("7    Morgan")
    print("8    Patrick")
    print("9    Vincent")
    print("10   Repeat All")
    print("11   Repeat Aloysius")
    print("12   Repeat Raistlin")
    print("13   Repeat Reginald")
    print("14   Repeat Yaxamie")
    print("15   Repeat Tasslehoff")
    print("16   Repeat Thadian")
    print("17   Repeat Morgan")
    print("18   Repeat Patrick")
    print("19   Repeat Vincent")
    while True:
        choice = input(print("Type the number of your choice and press Enter:"))
        if choice == "1":
            print("You have selected Narrator One, Aloysius.")
            print("Hip, hip, hooray!")
            break
        elif choice == "2":
            print("You have selected Narrator Two, Raistlin.")
            print("This is truly the highlight of my day, and for the record, "
                  "I am not one of the mages of Holin'dorf.")
            break
        elif choice == "3":
            print("You have selected Narrator Three, Reginald.")
            print("Hooray, you picked me!")
            break
        elif choice == "4":
            print("You have selected Narrator Four, Yaxamie.")
            print("I have translated the note!")
            break
        elif choice == "5":
            print("You have selected Narrator Five, Tasslehoff.")
            print("Wow, I've never been a narrator before.  This is awesome!")
            break
        elif choice == "6":
            print("You have selected Narrator Six, Thadian.")
            print("I'm glad this is a poetry recital because my lute got ruined in a shipwreck.")
            break
        elif choice == "7":
            print("You have selected Narrator Seven, Morgan.")
            print("Are you on Discord yet?")
            break
        elif choice == "8":
            print("You have selected Narrator Eight, Patrick.")
            print("One ring to rule them all, my dudes.")
            break
        elif choice == "9":
            print("You have selected Narrator Nine, Vincent.")
            print("I am not the greatest painter in the world, Vincent van Gogh.  I am just a tribute.")
            break    
        elif choice == "10":
            aloysius()
            raistlin()
            reginald()
            yaxamie()
            tasslehoff()
            thadian()
            morgan()
            patrick()
            vincent()
            continue
        elif choice == "11":
            aloysius()
            continue
        elif choice == "12":
            raistlin()
            continue
        elif choice == "13":
            reginald()
            continue
        elif choice == "14":
            yaxamie()
            continue
        elif choice == "15":
            tasslehoff()
            continue
        elif choice == "16":
            thadian()
            continue
        elif choice == "17":
            morgan()
            continue
        elif choice == "18":
            patrick()
            continue
        elif choice == "19":
            vincent()
            continue                                                                                    
        else:
            print("Please select from the provided options.")   
            continue
    break
#   Main Branch Decision Loop 2:  Choose a genre path for your finished poem.
while True:
    print("Let's now go to the choice of genre paths.  Here are your three options:")
    print("1    sea shanties and work songs")
    print("2    folk songs")
    print("3    total chaos")
    choice = input(print("Type the number of your choice and press Enter:  "))
    while True:
        if choice == "1":
            print("You have selected option one, sea shanties and work songs.")
            break
        elif choice == "2":
            print("You have selected option two, folk songs.")
            break
        elif choice == "3":
            print("You have selected option three, total chaos.")
            break
        else:
            print("Please selected from the provided options.")
            continue
    #   Nested Decision Loop 2.1:  If you choose sea shanties and work songs.
    while True:
        if choice == "1":
            print("Choice One")
            print("1     I")
            print("2     They")
            print("3     We")
            print("4     Once")
            print("5     Twice")
            print("6     Thrice")
            print("7     Drunken")
            print("8     Farting")
            print("9     Stupid")
            print("10    Young")
            print("11    Old")
            print("12    Fat")
            print("13    Pirate")
            print("14    Teacher")
            print("15    Lawyer")
            while True:
                choice = input(print("Type the number of your choice and press Enter:  "))
                if choice == "1":
                    print("You have selected option one, I.")
                    break
                elif choice == "2":
                    print("You have selected option two, They.")
                    break
                elif choice == "3":
                    print("You have selected option three, We.")
                    break
                elif choice == "4":
                    print("You have selected option four, Once.")
                    break
                elif choice == "5":
                    print("You have selected option five, Twice.")
                    break
                elif choice == "6":
                    print("You have selected option six, Thrice.")
                    break
                elif choice == "7":
                    print("You have selected option seven, Drunken.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Farting.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Stupid.")
                    break
                elif choice == "10":
                    print("You have selected option ten, Young.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Old.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Fat.")
                    break
                elif choice == "13":
                    print("You have selected option thirteen, Pirate.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Teacher.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Lawyer.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
        while True:
            if choice == "1":
                print("Choice Two")
                print("1     Old")
                print("2     Tall")
                print("3     Sad")
            if choice == "2":
                print("Choice Two")
                print("1     Old")
                print("2     Tall")
                print("3     Sad")
            if choice == "3":
                print("Choice Two")
                print("1     Old")
                print("2     Tall")
                print("3     Sad")
            while True:
                choice = input(print("Type the number of your choice and press Enter:  "))
                if choice == "1":
                    print("You have selected option one, Old.")
                    break
                elif choice == "2":
                    print("You have selected option two, Tall.")
                    break
                elif choice == "3":
                    print("You have selected option three, Sad.")
                    break
            if choice == "4":
                print("Choice Two")
                print("4     Billy")
                print("5     Enterprise")
                print("6     Carpenter")
            if choice == "5":
                print("Choice Two")
                print("4     Billy")
                print("5     Enterprise")
                print("6     Carpenter")
            if choice == "6":
                print("Choice Two")
                print("4     Billy")
                print("5     Enterprise")
                print("6     Carpenter")
            while True:
                if choice == "4":
                    print("You have selected option four, Billy.")
                    break
                elif choice == "5":
                    print("You have selected option five, Enterprise.")
                    break
                elif choice == "6":
                    print("You have selected option six, Carpenter.")
                    break
            if choice == "7":
                print("Choice Two")
                print("7     Sailor")
                print("8     Bouncer")
                print("9     Painter")
            if choice == "8":
                print("Choice Two")
                print("7     Sailor")
                print("8     Bouncer")
                print("9     Painter")
            if choice == "9":
                print("Choice Two")
                print("7     Sailor")
                print("8     Bouncer")
                print("9     Painter")
            while True:
                if choice == "7":
                    print("You have selected option seven, Sailor.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Bouncer.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Painter.")
                    break
            if choice == "10":
                print("Choice Two")
                print("10    Fellows")
                print("11    Chickens")
                print("12    Farters")
            if choice == "11":
                print("Choice Two")
                print("10    Fellows")
                print("11    Chickens")
                print("12    Farters")
            if choice == "12":
                print("Choice Two")
                print("10    Fellows")
                print("11    Chickens")
                print("12    Farters")
            while True:
                if choice == "10":
                    print("You have selected option ten, Fellows.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Chickens.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Farters.")
                    break
            if choice == "13":
                print("Choice Two")
                print("13    Me")
                print("14    Her")
                print("15    Them")
            if choice == "14":
                print("Choice Two")
                print("13    Me")
                print("14    Her")
                print("15    Them")
            if choice == "15":
                print("Choice Two")
                print("13    Me")
                print("14    Her")
                print("15    Them")
                while True:
                    if choice == "13":
                        print("You have selected option thirteen, Me.")
                        break
                    elif choice == "14":
                        print("You have selected option fourteen, Her.")
                        break
                    elif choice == "15":
                        print("You have selected option fifteen, Them.")
                        break
            if choice == "1":
                print("Choice Three")
                print("1     Say")
                print("2     Yell")
                print("3     Wish")
            if choice == "2":
                print("Choice Three")
                print("1     Say")
                print("2     Yell")
                print("3     Wish")
            if choice == "3":
                print("Choice Three")
                print("1    Say")
                print("2    Yell")
                print("3    Wish")
                while True:
                    if choice == "1":
                        print("You have selected option one, Say.")
                        break
                    elif choice == "2":
                        print("You have selected option two, Yell.")
                        break
                    elif choice == "3":
                        print("You have selected option three, Wish.")
                        break
            if choice == "4":
                print("Choice Three")
                print("4     Up")
                print("5     Down")
                print("6     In")
            if choice == "5":
                print("Choice Three")
                print("4     Up")
                print("5     Down")
                print("6     In")
            if choice == "6":
                print("4    Up")
                print("5    Down")
                print("6    In")
                while True:
                    if choice == "4":
                        print("You have selected option four, Up.")
                        break
                    elif choice == "5":
                        print("You have selected option five, Down.")
                        break
                    elif choice == "6":
                        print("You have selected option six, In.")
                        break
            if choice == "7":
                print("Choice Three")
                print("7     Early")
                print("8     Lately")
                print("9     Never")
            if choice == "8":
                print("Choice Three")
                print("7     Early")
                print("8     Lately")
                print("9     Never")
            if choice == "9":
                print("Choice Three")
                print("7    Early")
                print("8    Lately")
                print("9    Never")
            while True:
                if choice == "7":
                    print("You have selected option seven, Early.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Lately.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Never.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Three")
                print("10    Sea")
                print("11    News")
                print("12    Game")
            if choice == "11":
                print("Choice Three")
                print("10    Sea")
                print("11    News")
                print("12    Game")
            if choice == "12":
                print("Choice Three")
                print("10    Sea")
                print("11    News")
                print("12    Game")
            while True:
                if choice == "10":
                    print("You have selected option ten, Sea.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, News.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Game.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Three")
                print("13    Pillage")
                print("14    Sweep")
                print("15    Bake")
            if choice == "14":
                print("Choice Three")
                print("13    Pillage")
                print("14    Sweep")
                print("15    Bake")
            if choice == "15":
                print("13    Pillage")
                print("14    Sweep")
                print("15    Bake")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Pillage.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Sweep.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Bake.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Four")
                print("1     Leave")
                print("2     Watch")
                print("3     Trust")
            if choice == "2":
                print("Choice Four")
                print("1     Leave")
                print("2     Watch")
                print("3     Trust")
            if choice == "3":
                print("Choice Four")
                print("1     Leave")
                print("2     Watch")
                print("3    Trust")
            while True:
                if choice == "1":
                    print("You have selected option one, Leave.")
                    break
                elif choice == "2":
                    print("You have selected option two, Watch.")
                    break
                elif choice == "3":
                    print("You have selected option three, Trust.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Four")
                print("4     Blow")
                print("5     Sing")
                print("6     Dance")
            if choice == "5":
                print("Choice Four")
                print("4     Blow")
                print("5     Sing")
                print("6     Dance")
            if choice == "6":
                print("Choice Four")
                print("4    Blow")
                print("5    Sing")
                print("6    Dance")
            while True:
                if choice == "4":
                    print("You have selected option four, Blow.")
                elif choice == "5":
                    print("You have selected option five, Sing.")
                elif choice == "6":
                    print("You have selected option six, Dance.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Four")
                print("7     Morning")
                print("8     Party")
                print("9     Evening")
            if choice == "8":
                print("Choice Four")
                print("7     Morning")
                print("8     Party")
                print("9     Evening")
            if choice == "9":
                print("Choice Four")
                print("7    Morning")
                print("8    Party")
                print("9    Evening")
            while True:
                if choice == "7":
                    print("You have selected option seven, Morning.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Party.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Evening.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Four")
                print("10    Me")
                print("11    You")
                print("12    Down")
            if choice == "11":
                print("Choice Four")
                print("10    Me")
                print("11    You")
                print("12    Down")
            if choice == "12":
                print("Choice Four")
                print("10    Me")
                print("11    You")
                print("12    Down")
            while True:
                if choice == "10":
                    print("You have selected option ten, Me.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, You.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Down.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Four")
                print("13    Plunder")
                print("14    Fart")
                print("15    Paint")
            if choice == "14":
                print("Choice Four")
                print("13    Plunder")
                print("14    Fart")
                print("15    Paint")
            if choice == "15":
                print("Choice Four")
                print("13    Plunder")
                print("14    Fart")
                print("15    Paint")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Plunder.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Fart.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Paint.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Five")
                print("1     Johnny")
                print("2     Timmy")
                print("3     Frodo")
            if choice == "2":
                print("Choice Five")
                print("1     Johnny")
                print("2     Timmy")
                print("3     Frodo")
            if choice == "3":
                print("Choice Five")
                print("1    Johnny")
                print("2    Timmy")
                print("3    Frodo")
            while True:
                if choice == "1":
                    print("You have selected option one, Johnny.")
                    break
                elif choice == "2":
                    print("You have selected option two, Timmy.")
                    break
                elif choice == "3":
                    print("You have selected option three, Frodo.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Five")
                print("4     Soon")
                print("5     When")
                print("6     Why")
            if choice == "5":
                print("Choice Five")
                print("4     Soon")
                print("5     When")
                print("6     Why")
            if choice == "6":
                print("Choice Five")
                print("4     Soon")
                print("5     When")
                print("6     Why")
            while True:
                if choice == "4":
                    print("You have selected option four, Soon.")
                    break
                elif choice == "5":
                    print("You have selected option five, When.")
                    break
                elif choice == "6":
                    print("You have selected option six, Why.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Five")
                print("7     Brig")
                print("8     Toilets")
                print("9     Farts")
            if choice == "8":
                print("Choice Five")
                print("7     Brig")
                print("8     Toilets")
                print("9     Farts")
            if choice == "9":
                print("7     Brig")
                print("8     Toilets")
                print("9     Farts")
            while True:
                if choice == "7":
                    print("You have selected option seven, Brig.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Toilets.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Farts.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Five")
                print("10    Blow")
                print("11    Slap")
                print("12    Chase")
            if choice == "11":
                print("Choice Five")
                print("10    Blow")
                print("11    Slap")
                print("12    Chase")
            if choice == "12":
                print("Choice Five")
                print("10    Blow")
                print("11    Slap")
                print("12    Chase")
            while True:
                if choice == "10":
                    print("You have selected option ten, Blow.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Slap.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Chase.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Five")
                print("13    Rifle")
                print("14    Vomit")
                print("15    Books")
            if choice == "14":
                print("Choice Five")
                print("13    Rifle")
                print("14    Vomit")
                print("15    Books")
            if choice == "15":
                print("Choice Five")
                print("13    Rifle")
                print("14    Vomit")
                print("15    Books")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Riflt.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Vomit.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Books.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Six")
                print("1    Tomorrow")
                print("2    Next Tuesday")
                print("3    On Friday")
            if choice == "2":
                print("Choice Six")
                print("1    Tomorrow")
                print("2    Next Tuesday")
                print("3    On Friday")
            if choice == "3":
                print("Choice Six")
                print("1    Tomorrow")
                print("2    Tuesday")
                print("3    Friday")
            while True:
                if choice == "1":
                    print("You have selected option one, Tomorrow.")
                    break
                elif choice == "2":
                    print("You have selected option two, Tuesday.")
                    break
                elif choice == "3":
                    print("You have selected option three, Friday.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Six")
                print("4     Wellerman")
                print("5     Butterfly")
                print("6     Limousine")
            if choice == "5":
                print("Choice Six")
                print("4     Wellerman")
                print("5     Butterfly")
                print("6     Limousine")
            if choice == "6":
                print("Choice Six")
                print("4    Wellerman")
                print("5    Butterfly")
                print("6    Limousine")
            while True:
                if choice == "4":
                    print("You have selected option four, Wellerman.")
                    break
                elif choice == "5":
                    print("You have selected option five, Butterfly.")
                    break
                elif choice == "6":
                    print("You have selected option six, Limousine.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Six")
                print("7     Rises")
                print("8     Wiggles")
                print("9     Bubbles")
            if choice == "8":
                print("Choice Six")
                print("7     Rises")
                print("8     Wiggles")
                print("9     Bubbles")
            if choice == "9":
                print("Choice Six")
                print("7    Rises")
                print("    Wiggles")
                print("9    Bubbles")
            while True:
                if choice == "7":
                    print("You have selected option seven, Rises.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Wiggles.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Bubbles.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Six")
                print("10    Attention")
                print("11    Taxes")
                print("12    Biscuit")
            if choice == "11":
                print("Choice Six")
                print("10    Attention")
                print("11    Taxes")
                print("12    Biscuit")
            if choice == "12":
                print("Choice Six")
                print("10    Attention")
                print("11    Taxes")
                print("12    Biscuit")
            while True:
                if choice == "10":
                    print("You have selected option ten, Attention.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Taxes.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Biscuit.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Six")
                print("13    Loot")
                print("14    Hoot")
                print("15    Toot")
            if choice == "14":
                print("Choice Six")
                print("13    Loot")
                print("14    Hoot")
                print("15    Toot")
            if choice == "15":
                print("Choice Six")
                print("13    Loot")
                print("14    Hoot")
                print("15    Toot")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Loot.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Hoot.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Toot.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Seven")
                print("1     Pay")
                print("2     Bell")
                print("3    Fish")
            if choice == "2":
                print("Choice Seven")
                print("1     Pay")
                print("2     Bell")
                print("3     Fish")
            if choice == "3":
                print("Choice Seven")
                print("1    Pay")
                print("2    Bell")
                print("3    Fish")
            while True:
                if choice == "1":
                    print("You have selected option one, Pay.")
                    break
                elif choice == "2":
                    print("You have selected option two, Bell.")
                    break
                elif choice == "3":
                    print("You have selected option three, Fish.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Seven")
                print("4     Come")
                print("5     Go")
                print("6     Leave")
            if choice == "5":
                print("Choice Seven")
                print("4     Come")
                print("5     Go")
                print("6     Leave")
            if choice == "6":
                print("Choice Seven")
                print("4     Come")
                print("5     Go")
                print("6     Leave")
            while True:
                if choice == "4":
                    print("You have selected option four, Come.")
                    break
                elif choice == "5":
                    print("You have selected option five, Go.")
                    break
                elif choice == "6":
                    print("You have selected option six, Leave.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Seven")
                print("7     Clown")
                print("8     Dunce")
                print("9     Crackers")
            if choice == "8":
                print("Choice Seven")
                print("7     Clown")
                print("8     Dunce")
                print("     Crackers")
            if choice == "9":
                print("Choice Seven")
                print("7    Clown")
                print("8    Dunce")
                print("9    Crackers")
            while True:
                if choice == "7":
                    print("You have selected option seven, Clown.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Dunce.")
                    break
                elif choice == "9":
                    print("You ahve selecte option nine, Crackers.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Seven")
                print("10    Blow")
                print("11    Finish")
                print("12    Take")
            if choice == "11":
                print("Choice Seven")
                print("10    Blow")
                print("11    Finish")
                print("12    Take")
            if choice == "12":
                print("Choice Seven")
                print("10    Blow")
                print("11    Finish")
                print("12    Take")
            while True:
                if choice == "10":
                    print("You have selected option ten, Blow.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Finish.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Take.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Seven")
                print("13    Drink")
                print("14    Eat")
                print("15    Shop")
            if choice == "14":
                print("Choice Seven")
                print("13    Drink")
                print("14    Eat")
                print("15    Shop")
            if choice == "15":
                print("Choice Seven")
                print("13    Drink")
                print("14    Eat")
                print("15    Shop")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Drink.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Eat.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Shop.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Eight")
                print("1     Long")
                print("2     Short")
                print("3     Wild")
            if choice == "2":
                print("Choice Eight")
                print("1     Long")
                print("2     Short")
                print("3     Wild")
            if choice == "3":
                print("Choice Eight")
                print("1    Long")
                print("2    Short")
                print("3    Wild")
            while True:
                if choice == "1":
                    print("You have selected option one, Long.")
                    break
                elif choice == "2":
                    print("You have selected option two, Short.")
                    break
                elif choice == "3":
                    print("You have selected option three, Wild.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Eight")
                print("4     Sugar")
                print("5     Twizzlers")
                print("6     Pizza")
            if choice == "5":
                print("Choice Eight")
                print("4     Sugar")
                print("5     Twizzlers")
                print("6     Pizza")
            if choice == "6":
                print("Choice Eight")
                print("4    Sugar")
                print("5    Twizzlers")
                print("6    Pizza")
            while True:
                if choice == "4":
                    print("You have selected option four, Sugar.")
                    break
                elif choice == "5":
                    print("You have selected option five, Twizzlers.")
                    break
                elif choice == "6":
                    print("You have selected option six, Pizza.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Eight")
                print("7     Wash")
                print("8     Drink")
                print("9     Smell")
            if choice == "8":
                print("Choice Eight")
                print("7     Wash")
                print("8     Drink")
                print("9     Smell")
            if choice == "9":
                print("Choice Eight")
                print("7     Wash")
                print("8     Drink")
                print("9     Smell")
            while True:
                if choice == "7":
                    print("You have selected option seven, Wash.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Drink.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Smell.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Eight")
                print("10    Deep")
                print("11    Business")
                print("12    Lazy")
            if choice == "11":
                print("Choice Eight")
                print("10    Deep")
                print("11    Business")
                print("12    Lazy")
            if choice == "12":
                print("Choice Eight")
                print("10    Deep")
                print("11    Business")
                print("12    Lazy")
            while True:
                if choice == "10":
                    print("You have selected option ten, Deep.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Business.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Lazy.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Eight")
                print("13    Hearties")
                print("14    Homies")
                print("15    Peeps")
            if choice == "14":
                print("Choice Eight")
                print("13    Hearties")
                print("14    Homies")
                print("15    Peeps")
            if choice == "15":
                print("Choice Eight")
                print("13    Hearties")
                print("14    Homies")
                print("15    Peeps")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Hearties.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Homies.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Peeps.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Nine")
                print("1     Wind")
                print("2     Food")
                print("3     Smell")
            if choice == "2":
                print("Choice Nine")
                print("1     Wind")
                print("2     Food")
                print("3     Smell")
            if choice == "3":
                print("Choice Nine")
                print("1    Wind")
                print("2    Food")
                print("3    Smell")
            while True:
                if choice == "1":
                    print("You have selected option one, Wind.")
                    break
                elif choice == "2":
                    print("You have selected option two, Food.")
                    break
                elif choice == "3":
                    print("You have selected option three, Smell.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Nine")
                print("4     Tea")
                print("5     T-shirts")
                print("6     Shoes")
            if choice == "5":
                print("Choice Nine")
                print("4     Tea")
                print("5     T-shirts")
                print("6     Shoes")
            if choice == "6":
                print("Choice Nine")
                print("4    Tea")
                print("5    T-shirts")
                print("6    Shoes")
            while True:
                if choice == "4":
                    print("You have selected option four, Tea.")
                    break
                elif choice == "5":
                    print("You have selected option five, T-shirts.")
                    break
                elif choice == "6":
                    print("You have selected option six, Shoes.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Nine")
                print("7     Polish")
                print("8     Wipe")
                print("9     Clean")
            if choice == "8":
                print("Choice Nine")
                print("7     Polish")
                print("8     Wipe")
                print("9     Clean")
            if choice == "9":
                print("Choice Nine")
                print("7    Polish")
                print("8    Wipe")
                print("9    Clean")
            while True:
                if choice == "7":
                    print("You have selected option seven, Polish.")
                    break
                elif choice == "8":
                    print("you have selected option eight, Wipe.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Clean.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Nine")
                print("10    Sailor")
                print("11    Pickle")
                print("12    Fart")
            if choice == "11":
                print("Choice Nine")
                print("10    Sailor")
                print("11    Pickle")
                print("12    Fart")
            if choice == "12":
                print("Choice Nine")
                print("10    Sailor")
                print("11    Pickle")
                print("12    Fart")
            while True:
                if choice == "10":
                    print("You have selected option ten, Sailor.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Pickle.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Fart.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Nine")
                print("13    Yo")
                print("14    Go")
                print("15    No")
            if choice == "14":
                print("Choice Nine")
                print("13    Yo")
                print("14    Go")
                print("15    No")
            if choice == "15":
                print("Choice Nine")
                print("13    Yo")
                print("14    Go")
                print("15    No")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Yo.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Go.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, No.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Ten")
                print("1     Foul")
                print("2     Cold")  
            if choice == "2":
                print("Choice Ten")
                print("1     Foul")
                print("2     Cold")
                print("3     Weird")
            if choice == "3":
                print("Choice Ten")
                print("1    Foul")
                print("2    Cold")
                print("3    Weird")
            while True:
                if choice == "1":
                    print("You have selected option one, Foul.")
                    break
                elif choice == "2":
                    print("You have selected option two, Cold.")
                    break
                elif choice == "3":
                    print("You have selected option three, Weird.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Ten")
                print("4     Rum")
                print("5     Coke")
                print("6     Prune Juice")
            if choice == "5":
                print("Choice Ten")
                print("4     Rum")
                print("5     Coke")
                print("6     Prune Juice")
            if choice == "6":
                print("Choice Ten")
                print("4     Rum")
                print("5     Coke")
                print("6     Prune Juice")
            while True:
                if choice == "4":
                    print("You have selected option four, Rum.")
                    break
                elif choice == "5":
                    print("You have selected option five, Coke.")
                    break
                elif choice == "6":
                    print("You have selected option six, Prune Juice.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Ten")
                print("7     Standing")
                print("8     Vomit")
                print("9     Laundry")
            if choice == "8":
                print("Choice Ten")
                print("7     Standing")
                print("8     Vomit")
                print("9     Laundry")
            if choice == "9":
                print("Choice Ten")
                print("7    Standing")
                print("8    Vomit")
                print("9    Laundry")
                while True:
                    if choice == "7":
                        print("You have selected option seven, Standing.")
                        break
                    elif choice == "8":
                        print("You have selected option eight, Vomit.")
                        break
                    elif choice == "9":
                        print("You have selected option nine, Laundry.")
                        break
                    else:
                        print("Please choose from the provided options.")
                        continue
            if choice == "10":
                print("Choice Ten")
                print("10    Hong Kong")
                print("11    The Bronx")
                print("12    L.A.")
            if choice == "11":
                print("Choice Ten")
                print("10    Hong Kong")
                print("11    The Bronx")
                print("12    L.A.")
            if choice == "12":
                print("Choice Ten")
                print("10    Hong Kong")
                print("11    The Bronx")
                print("12    L.A.")
            while True:
                if choice == "10":
                    print("You have selected option ten, Hong Kong.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, The Bronx.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, L.A.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13": 
                print("Choice Ten")
                print("13    Kidnap")
                print("14    Play")
                print("15    Buy")
            if choice == "14":
                print("Choice Ten")
                print("13    Kidnap")
                print("14    Play")
                print("15    Buy")
            if choice == "15":
                print("Choice Ten")
                print("13    Kidnap")
                print("14    Play")
                print("15    Buy")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Kidnap.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Play.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Buy.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "1":
                print("Choice Eleven")
                print("1     None")
                print("2     All")
                print("3     Some")
            if choice == "2":
                print("Choice Eleven")
                print("1     None")
                print("2     All")
                print("3     Some")
            if choice == "3":
                print("Choice Eleven")
                print("1    None")
                print("2    All")
                print("3    Some")
            while True:
                if choice == "1":
                    print("You have selected option one, None.")
                    break
                elif choice == "2":
                    print("You have selected option two, All.")
                    break
                elif choice == "3":
                    print("You have selected option three, Some.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "4":
                print("Choice Eleven")
                print("4     Tonguing")
                print("5     Singing")
                print("6     Mopping")
            if choice == "5":
                print("Choice Eleven")
                print("4     Tonguing")
                print("5     Singing")
                print("6     Mopping")
            if choice == "6":
                print("Choice Eleven")
                print("4    Tonguing")
                print("5    Singing")
                print("6    Mopping")
            while True:
                if choice == "4":
                    print("You have selected option four, Tonguing.")
                    break
                elif choice == "5":
                    print("You have selected option five, Singing.")
                    break
                elif choice == "6":
                    print("You have selected option six, Mopping.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "7":
                print("Choice Eleven")
                print("7     Leave")
                print("8     Breakfast")
                print("9     Pots")
            if choice == "8":
                print("Choice Eleven")
                print("7     Leave")
                print("8     Breakfast")
                print("9     Pots")
            if choice == "9":
                print("Choice Eleven")
                print("7    Leave")
                print("8    Breakfast")
                print("9    Pots")
            while True:
                if choice == "7":
                    print("You have selected option seven, Leave.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Breakfast.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Pots.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "10":
                print("Choice Eleven")
                print("10    Drink")
                print("11    Cow")
                print("12    Toilet")
            if choice == "11":
                print("Choice Eleven")
                print("10    Drink")
                print("11    Cow")
                print("12    Toilet")
            if choice == "12":
                print("Choice Eleven")
                print("10    Drink")
                print("11    Cow")
                print("12    Toilet")
            while True:
                if choice == "10":
                    print("you have selected option ten, Drink.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Cow.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Toilet.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            if choice == "13":
                print("Choice Eleven")
                print("13    Hoot")
                print("14    Crap")
                print("15    Boot")
            if choice == "14":
                print("Choice Eleven")
                print("13    Hoot")
                print("14    Crap")
                print("15    Boot")
            if choice == "15":
                print("Choice Eleven")
                print("13    Hoot")
                print("14    Crap")
                print("15    Boot")
            while True:
                if choice == "13":
                    print("You have selected option thirteen, Hoot.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Crap.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Boot.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue

#   Nested Decision Loop 2.2:  If you choose folk songs.
# Path Two:  folk songs
    while True:
        print("Choice One")
        print("1     Bags")
        print("2     Drugs")
        print("3     Snacks")
        print("4     Give")
        print("5     Sell")
        print("6     Rent")
        print("7     Are")
        print("8     Why")
        print("9     Were")
        print("10    Dublin")
        print("11    Mexico")
        print("12    Houston")
        print("13    Wide")
        print("14    Cold")
        print("15    Fine")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Bags.")
            break
        elif choice == "2":
            print("You have selected option two, Drugs.")
            break
        elif choice == "3":
            print("You have selected option three, Snacks.")
            break
        elif choice == "4":
            print("You have selected option four, Give.")
            break
        elif choice == "5":
            print("You have selected option five, Sell.")
            break
        elif choice == "6":
            print("You have selected option six, Rent.")
            break
        elif choice == "7":
            print("You have selected option seven, Are.")
            break
        elif choice == "8":
            print("You have selected option eight, Why.")
            break
        elif choice == "9":
            print("You have selected option nine, Were.")
            break
        elif choice == "10":
            print("You have selected option ten, Dublin.")
            break
        elif choice == "11":
            print("You have selected option eleven, Mexico.")
            break
        elif choice == "12":
            print("You have selected option twelve, Houston.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Wide.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Cold.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Fine.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Two")
    print("1     Go")
    print("2     Stay")
    print("3     Fight")
    print("4     Me")
    print("5     Her")
    print("6     Them")
    print("7     Going")
    print("8     Dance")
    print("9     Fly")
    print("10    Sweet")
    print("11    Weird")
    print("12    Old")
    print("13    Swim") 
    print("14    Buy")
    print("15    Want")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Go.")
            break
        elif choice == "2":
            print("You have selected option two, Stay.")
            break
        elif choice == "3":
            print("You have selected option three, Fight.")
            break
        elif choice == "4":
            print("You have selected option four, Me.")
            break
        elif choice == "5":
            print("You have selected option five, Her.")
            break
        elif choice == "6":
            print("You have selected option six, Them.")
            break
        elif choice == "7":
            print("You have selected option seven, Going.")
            break
        elif choice == "8":
            print("You have selected option eight, Dance.")
            break
        elif choice == "9":
            print("You have selected option nine, Fly.")
            break
        elif choice == "10":
            print("You have selected otpion ten, Sweet.")
            break
        elif choice == "11":
            print("You have selected option eleven, Weird.")
            break
        elif choice == "12":
            print("You have selected option twelve, Old.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Swim.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Buy.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Want.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Three")
    print("1     Door")
    print("2     Store")
    print("3     Car")
    print("4     Home")
    print("5     Job")
    print("6     Zone")
    print("7     Scarborough")
    print("8     Grocery")
    print("9     Comic")
    print("10    Push")
    print("11    Knapsack")
    print("12    Camaro")
    print("13    Wing")
    print("14    Ticket")
    print("15    Bird")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Door.")
            break
        elif choice == "2":
            print("You have selected option two, Store.")
            break   
        elif choice == "3":
            print("You have selected option three, Car.")
            break
        elif choice == "4":
            print("You have selected option four, Home.")
            break
        elif choice == "5":
            print("You have selected option five, Job.")
            break
        elif choice == "6":
            print("You have selected option six, Zone.")
            break
        elif choice == "7":
            print("You have selected option seven, Scarborough.")
            break
        elif choice == "8":
            print("You have selected option eight, Grocery.")
            break
        elif choice == "9":
            print("You have selected option nine, Comic.")
            break
        elif choice == "10":
            print("You have selected option ten, Push.")
            break
        elif choice == "11":
            print("You have selected option eleven, Knapsack.")
            break
        elif choice == "12":
            print("You have selected option twelve, Camaro.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Wing.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Ticket.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Bird.")
            break
        else:
            print("Please choose from the available options.")
            continue
    break
while True:
    print("Choice Four")
    print("1     Hate")
    print("2     Love")
    print("3     Want")
    print("4     Buffalo")
    print("5     Carrot")
    print("6     Stanley")
    print("7     Parsley")
    print("8     Basil")
    print("9     Chicken")
    print("10    Push")
    print("11    Sue")
    print("12    Shake")
    print("13    Build")
    print("14    Buy")
    print("15    Sell")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Hate.")
            break
        elif choice == "2":
            print("You have selected option two, Love.")
            break
        elif choice == "3":
            print("You have selected option three, Want.")
            break
        elif choice == "4":
            print("You have selected option four, Buffalo.")
            break
        elif choice == "5":
            print("You have selected option five, Carrot.")
            break
        elif choice == "6":
            print("You have selected option six, Stanley.")
            break
        elif choice == "7":
            print("You have selected option seven, Parsley.")
            break
        elif choice == "8":
            print("You have selected option eight, Basil.")
            break
        elif choice == "9":
            print("You have selected option nine, Chicken.")
            break
        elif choice == "10":
            print("You have selected option ten, Push.")
            break
        elif choice == "11":
            print("You have selected option eleven, Sue.")
            break
        elif choice == "12":
            print("You have selected option twelve, Shake.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Build.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Buy.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Sell.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Five")
    print("1     Goodbye")
    print("2     Hello")
    print("3     Fart")
    print("4     Roam")
    print("5     Sing")
    print("6     Jump")
    print("7     Sage")
    print("8     Cheese")
    print("9     Salt")
    print("10    Wheelbarrow")
    print("11    Knapsack")
    print("12    Camaro")
    print("13    Me")
    print("14    Her")
    print("15    Him")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Goodbye.")
            break
        elif choice == "2":
            print("You have selected option two, Hello.")
            break
        elif choice == "3":
            print("You have selected option three, Fart.")
            break
        elif choice == "4":
            print("You have selected option four, Roam.")
            break
        elif choice == "5":
            print("You have selected option five, Sing.")
            break
        elif choice == "6":
            print("You have selected option six, Jump.")
            break
        elif choice == "7":
            print("You have selected option seven, Sage.")
            break
        elif choice == "8":
            print("You have selected option eight, Cheese.")
            break
        elif choice == "9":
            print("You have selected option nine, Salt.")
            break
        elif choice == "10":
            print("You have selected option ten, Wheelbarrow.")
            break
        elif choice == "11":
            print("You have selected option eleven, Knapsack.")
            break
        elif choice == "12":
            print("You have selected option twelve, Camaro.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Me.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Her.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Him.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Six")
    print("1     Break")
    print("2     Leave")
    print("3     Dance")
    print("4     Deer")
    print("5     Skunk")
    print("6     Mouse")
    print("7     Rosemary")
    print("8     Snickers")
    print("9     Mojitos")
    print("10    Street")
    print("11    Car")
    print("12    Store")
    print("13    Boat")
    print("14    Mouse")
    print("15    Car")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Break.")
            break
        elif choice == "2":
            print("You have selected option two, Leave.")
            break
        elif choice == "3":
            print("You have selected option three, Dance.")
            break
        elif choice == "4":
            print("You have selected option four, Deer.")
            break
        elif choice == "5":
            print("You have selected option five, Skunk.")
            break
        elif choice == "6":
            print("You have selected option six, Mouse.")
            break
        elif choice == "7":
            print("You have selected option seven, Rosemary.")
            break
        elif choice == "8":
            print("You have selected option eight, Snickers.")
            break
        elif choice == "9":
            print("You have selected option nine, Mojitos.")
            break
        elif choice == "10":
            print("You have selected option ten, Street.")
            break
        elif choice == "11":
            print("You have selected option eleven, Car.")
            break
        elif choice == "12":
            print("You have selected option twelve, Store.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Boat.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Mouse.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Car.")
            break
    break
while True:
    print("Choice Seven")
    print("1     Morning")
    print("2     Warm")
    print("3     Storm")
    print("4     Antelope")
    print("5     Ant")
    print("6     Bear")
    print("7     Thyme")
    print("8     Crime")
    print("9     Milk")
    print("10    Broad")
    print("11    Closed")
    print("12    Old")
    print("13    Carry")
    print("14    Ferry")
    print("15    Can't")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Morning.")
            break
        elif choice == "2":
            print("You have selected option two, Warm.")
            break
        elif choice == "3":
            print("You have selected option three, Storm.")
            break
        elif choice == "4":
            print("You have selected option four, Antelope.")
            break
        elif choice == "5":
            print("You have selected option five, Ant.")
            break
        elif choice == "6":
            print("You have selected option six, Bear.")
            break
        elif choice == "7":
            print("You have selected option seven, Thyme.")
            break
        elif choice == "8":
            print("You have selected option eight, Crime.")
            break
        elif choice == "9":
            print("You have selected option nine, Milk.")
            break
        elif choice == "10":
            print("You have selected option ten, Broad.")
            break
        elif choice == "11":
            print("You have selected option eleven, Closed.")
            break
        elif choice == "12":
            print("You have selected option twelve, Old.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Carry.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Ferry.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Can't.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Eight")
    print("1     Wait")
    print("2     Leave")
    print("3     Burn")
    print("4     Seldom")
    print("5     Sometimes")
    print("6     Daily")
    print("7     Thyme")
    print("8     Crime")
    print("9     Milk")
    print("10    Narrow")
    print("11    Nasty")
    print("12    Slippery")
    print("13    Two")
    print("14    Three")
    print("15    Four")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Wait.")
            break
        elif choice == "2":
            print("You have selected option two, Leave.")
            break
        elif choice == "3":
            print("You have selected option three, Burn.")
            break
        elif choice == "4":
            print("You have selected option four, Seldom.")
            break
        elif choice == "5":
            print("You have selected option five, Sometimes.")
            break
        elif choice == "6":
            print("You have selected option six, Daily.")
            break
        elif choice == "7":
            print("You have selected option seven, Thyme.")
            break
        elif choice == "8":
            print("You have selected option eight, Crime.")
            break
        elif choice == "9":
            print("You have selected option nine, Milk.")
            break
        elif choice == "10":
            print("You have selected option ten, Narrow.")
            break
        elif choice == "11":
            print("You have selected option eleven, Nasty.")
            break
        elif choice == "12":
            print("You have selected option twelve, Slippery.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Two.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Three.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Four.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Nine")
    print("1     Lonesome")
    print("2     Sleepy")
    print("3     Angry")
    print("4     Discourage")
    print("5     Encourage")
    print("6     Ridiculous")
    print("7     Me")
    print("8     Him")
    print("9     Her")
    print("10    Cockles")
    print("11    Cookies")
    print("12    Pencils")
    print("13    Row")
    print("14    Tow")
    print("15    Leave")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Lonesome.")
            break
        elif choice == "2":
            print("You have selected option two, Sleepy.")
        elif choice == "3":
            print("You have selected option three, Angry.")
            break
        elif choice == "4":
            print("You have selected option four, Discourage.")
            break
        elif choice == "5":
            print("You have selected option five, Encourage.")
            break
        elif choice == "6":
            print("You have selected option six, Ridiculous.")
            break
        elif choice == "7":
            print("You have selected option seven, Me.")
            break
        elif choice == "8":
            print("You have selected option eight, Him.")
            break
        elif choice == "9":
            print("You have selected option nine, Her.")
            break
        elif choice == "10":
            print("You have selected option ten, Cockles.")
            break
        elif choice == "11":
            print("You have selected option eleven, Cookies.")
            break
        elif choice == "12":
            print("You have selected option twelve, Pencils.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Row.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Tow.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Leave.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Ten")
    print("1     Die")
    print("2     Fly")
    print("3     Sue")
    print("4     Sky")
    print("5     Beer")
    print("6     Eye")
    print("7     There")
    print("8     Here")
    print("9     Near")
    print("10    Mussels")
    print("11    Taters")
    print("12    French")
    print("13    Love")
    print("14    Bro")
    print("15    Cat")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Die.")
            break
        elif choice == "2":
            print("You have selected option two, Fly.")
            break
        elif choice == "3":
            print("You have selected option three, Sue.")
            break
        elif choice == "4":
            print("You have selected option four, Sky.")
            break
        elif choice == "5":
            print("You have selected option five, Beer.")
            break
        elif choice == "6":
            print("You have selected option six, Eye.")
            break
        elif choice == "7":
            print("You have selected option seven, There.")
            break
        elif choice == "8":
            print("You have selected option eight, Here.")
            break
        elif choice == "9":
            print("You have selected option nine, Near.")
            break
        elif choice == "10":
            print("You have selected option ten, Mussels.")
            break
        elif choice == "11":
            print("You have selected option eleven, Taters.")
            break
        elif choice == "12":
            print("You have selected option twelve, French.")
            break
        elif choice == "13":
            print("You have selected option thirteen, Love.")
            break
        elif choice == "14":
            print("You have selected option fourteen, Bro.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Cat.")
            break
        else:
            print("Please choose from the provided options.")
            continue
    break
while True:
    print("Choice Eleven")
    print("1     Go")
    print("2     Belch")
    print("3     Fart")
    print("4     Cloud")
    print("5     Storm")
    print("6     Rain")
    print("7     Love")
    print("8     Llama")
    print("9     Hate")
    print("10    Alive")
    print("11    Best")
    print("12    Pay")
    print("13    I")
    print("14    You")
    print("15    Her")
    while True:
        choice = input(print("Type the number of your choice and press Enter:  "))
        if choice == "1":
            print("You have selected option one, Go.")
            break
        elif choice == "2":
            print("You have selected option two, Belch.")
            break
        elif choice == "3":
            print("You have selected option three, Fart.")
            break
        elif choice == "4":
            print("You have selected option four, Cloud.")
            break
        elif choice == "5":
            print("You have selected option five, Storm.")
            break
        elif choice == "6":
            print("You have selected option six, Rain.")
            break
        elif choice == "7":
            print("You have selected option seven, Love.")
            break
        elif choice == "8":
            print("You have selected option eight, Llama.")
            break
        elif choice == "9":
            print("You have selected option nine, Hate.")
            break
        elif choice == "10":
            print("You have selected option ten, Alive.")
            break
        elif choice == "11":
            print("You have selected option eleven, Best.")
            break
        elif choice == "12":
            print("You have selected option twelve, Pay.")
            break
        elif choice == "13":
            print("You have selected option thirteen, I.")
            break
        elif choice == "14":
            print("You have selected option fourteen, You.")
            break
        elif choice == "15":
            print("You have selected option fifteen, Her.")
            break
        else:
            print("Please choose from the provided options.")
            continue
#   Nested Decision loop 2.3:  If you choose total chaos.
# Part 3:  total chaos
    while True:
        print("Choice One")
        print("1    I          16    Bags")
        print("2    They       17    Drugs")
        print("3    We         18    Snacks")
        print("4    Once       19    Give")
        print("5    Twice      20    Sell")
        print("6    Thrice     21    Rent")
        print("7    Drunken    22    Are")
        print("8    Farting    23    Why")
        print("9    Stupid     24    Were")
        print("10   Young      25    Dublin")
        print("11   Old        26    Mexico")
        print("12   Fat        27    Houston")
        print("13   Pirate     28    Wide")
        print("14   Teacher    29    Cold")
        print("15   Lawyer     30    Fine")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, I.")
                break
            elif choice == "2":
                print("You have selected option two, They.")
                break
            elif choice == "3":
                print("You ahve selected option three, We.")
                break
            elif choice == "4":
                print("You have selected option four, Once.")
                break
            elif choice == "5":
                print("You ahve selected option five, Twice.")
                break
            elif choice == "6":
                print("You have selected option six, Thrice.")
                break
            elif choice == "7":
                print("You have selected option seven, Drunken.")
                break
            elif choice == "8":
                print("You have selected option eight, Farting.")
                break
            elif choice == "9":
                print("You have selected option nine, Stupid.")
                break
            elif choice == "10":
                print("You have selected option ten, Young.")
                break
            elif choice == "11":
                print("You have selected option eleven, Old.")
                break
            elif choice == "12":
                print("You have selected option twelve, Fat.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Pirate.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Teacher.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Lawyer.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Bags.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Drugs.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Snacks.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Give.")
                break
            elif choice == "20":
                print("You have selected option twenty, Sell.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Rent.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Are.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Why.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Were.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Dublin.")
                break
            elif choice == "26":
                print("You have selected option twnety-six, Mexico.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Houston.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Wide.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Cold.")
                break
            elif choice == "30":
                print("You have selected option thirty, Fine.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        while True:
            print("Choice Two")
            print("1    Old           16    Go")
            print("2    Tall          17    Stay")
            print("3    Sad           18    Fight")
            print("4    Billy         19    Me")
            print("5    Enterprise    20    Her")
            print("6    Carpenter     21    Them")
            print("7    Sailor        22    Going")
            print("8    Bouncer       23    Dance")
            print("9    Painter       24    Fly")
            print("10   Fellows       25    Sweet")
            print("11   Chickens      26    Weird")
            print("12   Farters       27    Old")
            print("13   Me            28    Swim")
            print("14   Her           29    Buy")
            print("15   Them          30    Want")
            while True:
                choice = input(print("Type the number of your choice and press Enter:  "))
                if choice == "1":
                    print("You have selected option one, Old.")
                    break
                elif choice == "2":
                    print("You have selected option two, Tall.")
                    break
                elif choice == "3":
                    print("You have selected option three, Sad.")
                    break
                elif choice == "4":
                    print("You have selected option four, Billy.")
                    break
                elif choice == "5":
                    print("You have selected option five, Enterprise.")
                    break
                elif choice == "6":
                    print("You have selected option six, Carpenter.")
                    break
                elif choice == "7":
                    print("You have selected option seven, Sailor.")
                    break
                elif choice == "8":
                    print("You have selected option eight, Bouncer.")
                    break
                elif choice == "9":
                    print("You have selected option nine, Painter.")
                    break
                elif choice == "10":
                    print("You have selected option ten, Fellows.")
                    break
                elif choice == "11":
                    print("You have selected option eleven, Me.")
                    break
                elif choice == "12":
                    print("You have selected option twelve, Farters.")
                    break
                elif choice == "13":
                    print("You have selected option thirteen, Me.")
                    break
                elif choice == "14":
                    print("You have selected option fourteen, Her.")
                    break
                elif choice == "15":
                    print("You have selected option fifteen, Them.")
                    break
                elif choice == "16":
                    print("You have selected option sixteen, Go.")
                    break
                elif choice == "17":
                    print("You have selected option seventeen, Stay.")
                    break
                elif choice == "18":
                    print("You have selected option eighteen, Fight.")
                    break
                elif choice == "19":
                    print("You have selected option nineteen, Me.")
                    break
                elif choice == "20":
                    print("You have selected option twenty, Her.")
                    break
                elif choice == "21":
                    print("You have selected option twenty-one, Them.")
                    break
                elif choice == "22":
                    print("You have selected option twenty-two, Going.")
                    break
                elif choice == "23":
                    print("You have selected option twenty-three, Dance.")
                    break
                elif choice == "24":
                    print("You have selected option twenty-four, Fly.")
                    break
                elif choice == "25":
                    print("You have selected option twenty-five, Sweet.")
                    break
                elif choice == "26":
                    print("You have selected option twenty-six, Weird.")
                    break
                elif choice == "27":
                    print("You have selected option twenty-seven, Old.")
                    break
                elif choice == "28":
                    print("You have selected option twenty-eight, Swim.")
                    break
                elif choice == "29":
                    print("You have selected option twenty-nine, Buy.")
                    break
                elif choice == "30":
                    print("You have selected option thirty, Want.")
                    break
                else:
                    print("Please choose from the provided options.")
                    continue
            break
        break
    while True:
        print("Choice Three")
        print("1    Say        16    Door")
        print("2    Yell       17    Store")
        print("3    Wish       18    Car")
        print("4    Up         19    Home")
        print("5    Down       20    Job")
        print("6    In         21    Zone")
        print("7    Early      22    Scarborough")
        print("8    Lately     23    Grocery")
        print("9    Never      24    Comic")
        print("10   Sea        25    Push")
        print("11   News       26    Knapsack")
        print("12   Game       27    Camaro")
        print("13   Pillage    28    Wing")
        print("14   Sweep      29    Ticket")
        print("15   Bake       30    Bird")
        while True: 
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Say.")
                break
            elif choice == "2":
                print("You have selected option two, Yell.")
                break
            elif choice == "3":
                print("You have selected option three, Wish.")
                break
            elif choice == "4":
                print("You have selected option four, Up.")
                break
            elif choice == "5":
                print("You have selected option five, Down.")
                break
            elif choice == "6":
                print("You have selected option six, In.")
                break
            elif choice == "7":
                print("You have selected option seven, Early.")
                break
            elif choice == "8":
                print("You have selected option eight, Lately.")
                break
            elif choice == "9":
                print("You have selected option nine, Never.")
                break
            elif choice == "10":
                print("You have selected option ten, Sea.")
                break
            elif choice == "11":
                print("You have selected option eleven, News.")
                break
            elif choice == "12":
                print("You have selected option twelve, Game.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Pillage.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Sweep.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Bake.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Door.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Store.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Car.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Home.")
                break
            elif choice == "20":
                print("You have selected option twenty, Job.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Zone.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Scarborough.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Grocery.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Comic.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Push.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Knapsack.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Camaro.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Wing.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Ticket.")
                break
            elif choice == "30":
                print("You have selected option thirty, Bird.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
    while True:
        print("Choice Four")
        print("1    Leave      16    Hate")
        print("2    Watch      17    Love")
        print("3    Trust      18    Want")
        print("4    Blow       19    Buffalo")
        print("5    Sing       20    Carrot")
        print("6    Dance      21    Stanley")
        print("7    Morning    22    Parsley")
        print("8    Party      23    Basil")
        print("9    Evening    24    Chicken")
        print("10   Me         25    Push")
        print("11   You        26    Sue")
        print("12   Down       27    Shake")
        print("13   Plunder    28    Build")
        print("14   Fart       29    Buy")
        print("15   Paint      30    Sell")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Leave.")
                break
            elif choice == "2":
                print("You have selected option two, Watch.")
                break
            elif choice == "3":
                print("You have selected option three, Trust.")
                break
            elif choice == "4":
                print("You have selected option four, Blow.")
                break
            elif choice == "5":
                print("You have selected option five, Sing.")
                break
            elif choice == "6":
                print("You have selected option six, Dance.")
                break
            elif choice == "7":
                print("You have selected option seven, Morning.")
                break
            elif choice == "8":
                print("You have selected option eight, Party.")
                break
            elif choice == "9":
                print("You have selected option nine, Evening.")
                break
            elif choice == "10":
                print("You have selected option ten, Me.")
                break
            elif choice == "11":
                print("You have selected option eleven, You.")
                break
            elif choice == "12":
                print("You have selected option twelve, Down.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Plunder.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Fart.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Paint.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Hate.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Love.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Want.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Buffalo.")
                break
            elif choice == "20":
                print("You have selected option twenty, Carrot.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Stanley.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Parsley.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Basil.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Chicken.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Push.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Sue.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Shake.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Build.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Buy.")
                break
            elif choice == "30":
                print("You have selected option thirty, Sell.")
                break
            else:
                print("Please choose from the provided options.")
                continue
    while True:
        print("Choice Five")
        print("1    Johnny     16    Goodbye")
        print("2    Timmy      17    Hello")
        print("3    Frodo      18    Fart")
        print("4    Soon       19    Roam")
        print("5    When       20    Sing")
        print("6    Why        21    Jump")
        print("7    Brig       22    Sage")
        print("8    Toilets    23    Cheese")
        print("9    Farts      24    Salt")
        print("10   Blow       25    Wheelbarrow")
        print("11   Slap       26    Knapsack")
        print("12   Chase      27    Camaro")
        print("13   Rifle      28    Me")
        print("14   Vomit      29    Her")
        print("15   Books      30    Him")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Johnny.")
                break
            elif choice == "2":
                print("You have selected option two, Timmy.")
                break
            elif choice == "3":
                print("You have selected option three, Frodo.")
                break
            elif choice == "4":
                print("You have selected option four, Soon.")
                break
            elif choice == "5":
                print("You have selected option five, When.")
                break
            elif choice == "6":
                print("You have selected option six, Why.")
                break
            elif choice == "7":
                print("You have selected option seven, Brig.")
                break
            elif choice == "8":
                print("You have selected option eight, Toilets.")
                break
            elif choice == "9":
                print("You have selected option nine, Farts.")
                break
            elif choice == "10":
                print("You have selected option ten, Blow.")
                break
            elif choice == "11":
                print("You have selected option eleven, Slap.")
                break
            elif choice == "12":
                print("You have selected option twelve, Chase.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Rifle.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Vomit.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Books.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Goodbye.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Hello.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Fart.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Roam.")
                break
            elif choice == "20":
                print("You have selected option twenty, Sing.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Jump.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Sage.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Cheese.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Salt.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Wheelbarrow.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Knapsack.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Camaro.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Me.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Her.")
                break
            elif choice == "30":
                print("You have selected option thirty, Him.")
                break
            else:
                print("Please choose from the provided options.")
                continue
    while True:
        print("Choice Six")
        print("1    Tomorrow        16    Break")
        print("2    Tuesday         17    Leave")
        print("3    Friday          18    Dance")
        print("4    Wellerman       19    Deer")
        print("5    Butterfly       20    Skunk")
        print("6    Limousine       21    Mouse")
        print("7    Rises           22    Rosemary")
        print("8    Wiggles         23    Snickers")
        print("9    Bubbles         24    Mojitos")
        print("10   Attention       25    Street")
        print("11   Taxes           26    Car")
        print("12   Biscuit         27    Store")
        print("13   Loot            28    Boat")
        print("14   Hoot            29    Mouse")
        print("15   Toot            30    Car")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Tomorrow.")
                break
            elif choice == "2":
                print("You have selected option two, Tuesday.")
                break
            elif choice == "3":
                print("You have selected option three, Friday.")
                break
            elif choice == "4":
                print("You have selected option four, Wellerman.")
                break
            elif choice == "5":
                print("You have selected option five, Butterfly.")
                break
            elif choice == "6":
                print("You have selected option six, Limousine.")
                break
            elif choice == "7":
                print("You have selected option seven, Rises.")
                break
            elif choice == "8":
                print("You have selected option eight, Wiggles.")
                break
            elif choice == "9":
                print("You have selected option nine, Bubbles.")
                break
            elif choice == "10":
                print("You have selected option ten, Attention.")
                break
            elif choice == "11":
                print("You have selected option eleven, Taxes.")
                break
            elif choice == "12":
                print("You have selected option twelve, Biscuit.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Loot.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Hoot.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Toot.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Break.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Leave.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Dance.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Deer.")
                break
            elif choice == "20":
                print("You have selected option twenty, Skunk.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Mouse.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Rosemary.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Snickers.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Mojitos.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Street.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Car.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Store.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Boat.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Mouse.")
                break
            elif choice == "30":
                print("You have selected option thirty, Car.")
                break
            else:
                print("Please choose from the provided options.")
                continue
    while True:
        print("Choice Seven")
        print("1    Pay         16    Morning")
        print("2    Bell        17    Warm")
        print("3    Fish        18    Storm")
        print("4    Come        19    Antelope")
        print("5    Go          20    Ant")
        print("6    Leave       21    Bear")
        print("7    Clown       22    Thyme")
        print("8    Dunce       23    Crime")
        print("9    Crackers    24    Milk")
        print("10   Blow        25    Broad")
        print("11   Finish      26    Closed")
        print("12   Take        27    Old")
        print("13   Drink       28    Carry")
        print("14   Eat         29    Ferry")
        print("15   Shop        30    Can't")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Pay.")
                break
            elif choice == "2":
                print("You have selected option two, Bell.")
                break
            elif choice == "3":
                print("You ahve selected option three, Fish.")
                break
            elif choice == "4":
                print("You have selected option four, Come.")
                break
            elif choice == "5":
                print("You have selected option five, Go.")
                break
            elif choice == "6":
                print("You have selected option six, Leave.")
                break
            elif choice == "7":
                print("You have selected option seven, Clown.")
                break
            elif choice == "8":
                print("You have selected option eight, Dunce.")
                break
            elif choice == "9":
                print("You have selected option nine, Crackers.")
                break
            elif choice == "10":
                print("You have selected option ten, Blow.")
                break
            elif choice == "11":
                print("You have selected option eleven, Finish.")
                break
            elif choice == "12":
                print("You have selected option twelve, Take.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Drink.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Eat.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Shop.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Morning.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Warm.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Storm.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Antelope.")
                break
            elif choice == "20":
                print("You have selected option twenty, Ant.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Bear.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Thyme.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Crime.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Milk.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Broad.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Closed.")
                break
            elif choice == "27":
                print("You have selected option twenty-seven, Old.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Carry.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Ferry.")
                break
            elif choice == "30":
                print("You have selected option thirty, Can't.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
    while True:
        print("Choice Eight")
        print("1    Long         16    Wait")
        print("2    Short        17    Leave")
        print("3    Wild         18    Burn")
        print("4    Sugar        19    Seldom")
        print("5    Twizzlers    20    Sometimes")
        print("6    Pizza        21    Daily")
        print("7    Wash         22    Thyme")
        print("8    Drink        23    Crime")
        print("9    Smell        24    Milk")
        print("10   Deep         25    Narrow")
        print("11   Business     26    Nasty")
        print("12   Lazy         27    Slippery")
        print("13   Hearties     28    Two")
        print("14   Homies       29    Three")
        print("15   Peeps        30    Four")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Long.")
                break
            elif choice == "2":
                print("You have selected option two, Short.")
                break
            elif choice == "3":
                print("You have selected option three, Wild.")
                break
            elif choice == "4":
                print("You have selected option four, Sugar.")
                break
            elif choice == "5":
                print("You have selected option five, Twizzlers.")
                break
            elif choice == "6":
                print("You have selected option six, Pizza.")
                break
            elif choice == "7":
                print("You have selected option seven, Wash.")
                break
            elif choice == "8":
                print("You have selected option eight, Drink.")
                break
            elif choice == "9":
                print("You have selected option nine, Smell.")
                break
            elif choice == "10":
                print("You have selected option ten, Deep.")
                break
            elif choice == "11":
                print("You have selected option eleven, Business.")
                break
            elif choice == "12":
                print("You have selected option twelve, Lazy.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Hearties.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Homies.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Peeps.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Wait.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Leave.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Burn.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Seldom.")
                break
            elif choice == "20":
                print("You have selected option twenty, Sometimes.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Daily.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Thyme.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Crime.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Milk.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Narrow.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Nasty.")
                break
            elif choice == "27":
                print("You have selected optin twenty-seven, Slippery.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Two.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Three.")
                break
            elif choice == "30":
                print("You have selected option thirty, Four.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
    while True:
        print("Choice Nine")
        print("1    Wind        16    Lonesome")
        print("2    Food        17    Sleepy")
        print("3    Smell       18    Angry")
        print("4    Tea         19    Discourage")
        print("5    T-shirts    20    Encourage")
        print("6    Shoes       21    Ridiculous")
        print("7    Polish      22    Me")
        print("8    Wipe        23    Him")
        print("9    Clean       24    Her")
        print("10   Sailor      25    Cockles")
        print("11   Pickle      26    Cookies")
        print("12   Fart        27    Pencils")
        print("13   Yo          28    Row")
        print("14   Go          29    Tow")
        print("15   No          30    Leave")
        while True:
            choice = input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Wind.")
                break
            elif choice == "2":
                print("You have selected option two, Food.")
                break
            elif choice == "3":
                print("You have selected option three, Smell.")
                break
            elif choice == "4":
                print("You have selected option four, Tea.")
                break
            elif choice == "5":
                print("You have selected option five, T-shirts.")
                break
            elif choice == "6":
                print("You have selected option six, Shoes.")
                break
            elif choice == "7":
                print("You have selected option seven, Polish.")
                break
            elif choice == "8":
                print("You have selected option eight, Wipe.")
                break
            elif choice == "9":
                print("You have selected option nine, Clean.")
                break
            elif choice == "10":
                print("You have selected option ten, Sailor.")
                break
            elif choice == "11":
                print("You have selected option eleven, Pickle.")
                break
            elif choice == "12":
                print("You have selected option twelve, Fart.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Yo.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Go.")
                break
            elif choice == "15":
                print("You have selected option fifteen, No.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Lonesome.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Sleepy.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Angry.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Discourage.")
                break
            elif choice == "20":
                print("You have selected option twenty, Encourage.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Ridiculous.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Me.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Him.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Her.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Cockles.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Cookies.")
                break
            elif choice == "27":
                print("You have selected optin twenty-seven, Pencils.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Row.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Tow.")
                break
            elif choice == "30":
                print("You have selected option thirty, Leave.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
    while True:
        print("Choice Ten")
        print("1    Foul           16    Die")
        print("2    Cold           17    Fly")
        print("3    Weird          18    Sue")
        print("4    Rum            19    Sky")
        print("5    Coke           20    Beer")
        print("6    Prune Juice    21    Eye")
        print("7    Standing       22    There")
        print("8    Vomit          23    Here")
        print("9    Laundry        24    Near")
        print("10   Hong Kong      25    Mussels")
        print("11   The Bronx      26    Taters")
        print("12   L.A.           27    French")
        print("13   Kidnap         28    Love")
        print("14   Play           29    Bro")
        print("15   Buy            30    Cat")
        while True:
            choice == input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, Foul.")
                break
            elif choice == "2":
                print("You have selected option two, Cold.")
                break
            elif choice == "3":
                print("You have selected option three, Weird.")
                break
            elif choice == "4":
                print("You have selected option four, Rum.")
                break
            elif choice == "5":
                print("You have selected option five, Coke.")
                break
            elif choice == "6":
                print("You have selected option six, Prune Juice.")
                break
            elif choice == "7":
                print("You have selected option seven, Standing.")
                break
            elif choice == "8":
                print("You have selected option eight, Vomit.")
                break
            elif choice == "9":
                print("You have selected option nine, Laundry.")
                break
            elif choice == "10":
                print("You have selected option ten, Hong Kong.")
                break
            elif choice == "11":
                print("You have selected option eleven, The Bronx.")
                break
            elif choice == "12":
                print("You have selected option twelve, L.A..")
                break
            elif choice == "13":
                print("You have selected option thirteen, Kidnap.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Play.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Buy.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Die.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Fly.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Sue.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Sky.")
                break
            elif choice == "20":
                print("You have selected option twenty, Beer.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Eye.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, There.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Here.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Near.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Mussels.")
                break
            elif choice == "26":
                print("You have selected option twenty-six, Taters.")
                break
            elif choice == "27":
                print("You have selected optin twenty-seven, French.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, Love.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, Bro.")
                break
            elif choice == "30":
                print("You have selected option thirty, Cat.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
    while True:
        print("Choice Eleven")
        print("1    None         16    Go")
        print("2    All          17    Belch")
        print("3    Some         18    Fart")
        print("4    Tonguing     19    Cloud")
        print("5    Singing      20    Storm")
        print("6    Mopping      21    Rain")
        print("7    Leave        22    Love")
        print("8    Breakfast    23    Llama")
        print("9    Pots         24    Hate")
        print("10   Drink        25    Alive")
        print("11   Cow          26    Best")
        print("12   Toilet       27    Pay")
        print("13   Hoot         28    I")
        print("14   Crap         29    You")
        print("15   Boot         30    Her")
        while True:
            choice == input(print("Type the number of your choice and press Enter:  "))
            if choice == "1":
                print("You have selected option one, None.")
                break
            elif choice == "2":
                print("You have selected option two, All.")
                break
            elif choice == "3":
                print("You have selected option three, Some.")
                break
            elif choice == "4":
                print("You have selected option four, Tonguing.")
                break
            elif choice == "5":
                print("You have selected option five, Singing.")
                break
            elif choice == "6":
                print("You have selected option six, Mopping.")
                break
            elif choice == "7":
                print("You have selected option seven, Leave.")
                break
            elif choice == "8":
                print("You have selected option eight, Breakfast.")
                break
            elif choice == "9":
                print("You have selected option nine, Pots.")
                break
            elif choice == "10":
                print("You have selected option ten, Drink.")
                break
            elif choice == "11":
                print("You have selected option eleven, Cow.")
                break
            elif choice == "12":
                print("You have selected option twelve, Toilet.")
                break
            elif choice == "13":
                print("You have selected option thirteen, Hoot.")
                break
            elif choice == "14":
                print("You have selected option fourteen, Crap.")
                break
            elif choice == "15":
                print("You have selected option fifteen, Boot.")
                break
            elif choice == "16":
                print("You have selected option sixteen, Go.")
                break
            elif choice == "17":
                print("You have selected option seventeen, Belch.")
                break
            elif choice == "18":
                print("You have selected option eighteen, Fart.")
                break
            elif choice == "19":
                print("You have selected option nineteen, Cloud.")
                break
            elif choice == "20":
                print("You have selected option twenty, Storm.")
                break
            elif choice == "21":
                print("You have selected option twenty-one, Rain.")
                break
            elif choice == "22":
                print("You have selected option twenty-two, Love.")
                break
            elif choice == "23":
                print("You have selected option twenty-three, Llama.")
                break
            elif choice == "24":
                print("You have selected option twenty-four, Hate.")
                break
            elif choice == "25":
                print("You have selected option twenty-five, Alive.")
                break
            elif choice == "26":    
                print("You have selected option twenty-six, Best.")
                break
            elif choice == "27":
                print("You have selected optin twenty-seven, Pay.")
                break
            elif choice == "28":
                print("You have selected option twenty-eight, I.")
                break
            elif choice == "29":
                print("You have selected option twenty-nine, You.")
                break
            elif choice == "30":
                print("You have selected option thirty, Her.")
                break
            else:
                print("Please choose from the provided options.")
                continue
        break
#   Main Branch Decision Loop 3: See/Hear your poem.