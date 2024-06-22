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
        
        
#   Main Branch Decision Loop:  Choosing a narrator for your poem.
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
    # Nested Decision Loop: Confirming the narrator you've selected, or repeating your options to help you decide.
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
#   Main Branch Decision Loop:  Choose a genre path for your finished poem.
while True:
    print("Let's now go to the choice of genre paths.  Here are your three options:")
    print("1    sea shanties and work songs")
    print("2    folk songs")
    print("3    total chaos")
    choice = input(print("Type the number of your choice and press Enter:  "))
    #   Nested Decision Loop:  Confirming which of the three paths you've chosen.
    while True: 
        if choice == "1":
            print("You have selected option one, sea shanties and work songs.")
            print("Choice One")
            print("1    I")
            print("2    They")
            print("3    We")
            print("4    Once")
            print("5    Twice")
            print("6    Thrice")
            print("7    Drunken")
            print("8    Farting")
            print("9    Stupid")
            print("10   Young")
            print("11   Old")
            print("12   Fat")
            print("13   Pirate")
            print("14   Teacher")
            print("15   Lawyer")
            choice = input(print("Type the number of your choice and press Enter:  "))
            while True:
                #   Leave Her, Johnny
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice One
                        if choice == "1":
                            print("You have selected option one, I.")
                            break
                        if choice == "2":
                            print("You have selected option two, They.")
                            break
                        if choice == "3":
                            print("You have selected option three, We.")
                            break
                    print("Choice Two")
                    print("1    Old")
                    print("2    Tall")
                    print("3    Sad")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Two
                        if choice == "1":
                            print("You have selected option one, Old.")
                            break
                        elif choice == "2":
                            print("You have selected option two, Tall.")
                            break
                        elif choice == "3":
                            print("You have selected option three, Sad.")
                            break
                        else:
                            print("Please choose from the provided options.")
                            continue
                    print("Choice Three")
                    print("1    Say")
                    print("2    Yell")
                    print("3    Wish")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Three
                        if choice == "1":
                            print("You have selected option one, Say.")
                            break
                        elif choice == "2":
                            print("You have selected option two, Yell.")
                            break
                        elif choice == "3":
                            print("You have selected option three, Wish.")
                            break
                        else:
                            print("Please choose from the provided options.")
                            continue
                    print("Choice Four")
                    print("1    Leave")
                    print("2    Watch")
                    print("3    Trust")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Four
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
                    print("Choice Five")
                    print("1    Johnny")
                    print("2    Timmy")
                    print("3    Frodo")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Five
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
                    print("Choice Six")
                    print("1    Tomorrow")
                    print("2    Tuesday")
                    print("3    Friday")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Six
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
                    print("Choice Seven")
                    print("1    Pay")
                    print("2    Bell")
                    print("3    Fish")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Seven
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
                    print("Choice Eight")
                    print("1    Long")
                    print("2    Short")
                    print("3    Wild")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Eight
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
                    print("Choice Nine")
                    print("1    Wind")
                    print("2    Food")
                    print("3    Smell")
                    break
                choice = input(print("Type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Nine
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
                    print("Choice Ten")
                    print("1    Foul")
                    print("2    Cold")
                    print("3    Weird")
                    break
                choice = input(print("type the number of your choice and press Enter:  "))
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Ten
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
                    print("Choice Eleven")
                    print("1    None")
                    print("2    All")
                    print("3    Some")
                    break
                while True:
                    #   Leave Her, Johnny
                    while True:
                        #   Choice Ten
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
                    break
                break
            while True:
                #   Wellerman
                while True:
                    #   Wellerman
                    while True:
                    #   Choice One
                        if choice == "4":
                            print("You have selected option four, Once.")
                            break
                        if choice == "5":
                            print("You have selected option five, Twice.")
                            break
                        if choice == "6":
                            print("You have selected option six, Thrice.")
                            break
                    print("Choice Two")
                    print("1    Billy")
                    print("2    Enterprise")
                    print("3    Carpenter")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Two
                        if choice == "1":
                            print("You have selected option one, Billy.")
                            break
                        if choice == "2":
                            print("You have selected option two, Enterprise.")
                            break
                        if choice == "3":
                            print("You have selected option three, Carpenter.")
                            break
                    print("Choice Three")
                    print("1    Up")
                    print("2    Down")
                    print("3    In")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Three
                        if choice == "1":
                            print("You have selected option one, Up.")
                            break
                        if choice == "2":
                            print("You have selected option two, Down.")
                            break
                        if choice == "3":
                            print("You have selected option three, In.")  
                            break
                    print("Choice Four")
                    print("1    Blow")
                    print("2    Sing")
                    print("3    Dance")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Four
                        if choice == "1":
                            print("You have selected option one, Blow.")
                            break
                        if choice == "2":
                            print("You have selected option two, Sing.")
                            break
                        if choice == "3":
                            print("You have selected option three, Dance.")
                            break
                    print("Choice Five")
                    print("1    Soon")
                    print("2    When")
                    print("3    Why")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Five
                        if choice == "1":
                            print("You have selected option one, Soon.")
                            break
                        if choice == "2":
                            print("You have selected option two, When.")
                            break
                        if choice == "3":
                            print("You have selected option three, Why.")
                            break
                    print("Choice Six")
                    print("1    Wellerman")
                    print("2    Butterfly")
                    print("3    Limousine")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Six
                        if choice == "1":
                            print("You have selected option one, Wellerman.")
                            break
                        if choice == "2":
                            print("You have selected option two, Butterfly.")
                            break
                        if choice == "3":
                            print("You have seelcted option three, Limousine.")
                            break
                    print("Choice Seven")
                    print("1    Come")
                    print("2    Go")
                    print("3    Leave")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Seven
                        if choice == "1":
                            print("You have selected option one, Come.")
                            break
                        if choice == "2":
                            print("You have selected option two, Go.")
                            break
                        if choice == "3":
                            print("You have selected option three, Leave.")
                            break
                    print("Choice Eight")
                    print("1    Sugar")
                    print("2    Twizzlers")
                    print("3    Pizza")
                    break
                while True:
                    #   Wellerman
                    while True:
                    #   Choice Eight
                        if choice == "1":
                            print("You have selected option one, Sugar.")
                            break
                        if choice == "2":
                            print("You have selected option two, Twizzlers.")
                            break
                        if choice == "3":
                            print("You have selected option three, Pizza.")
                            break
                    print("Choice Nine")
                    print("1    Tea")
                    print("2    T-shirts")
                    print("3    Shoes")
                    break
                while True:
                    #   Wellerman
                    while True:
                    #   Choice Nine
                        if choice == "1":
                            print("You have selected option one, Tea.")  
                            break
                        if choice == "2":
                            print("You have selected option two, T-shirts.")
                            break
                        if choice == "3":
                            print("You have selected option three, Shoes.")
                            break
                    print("Choice Ten")
                    print("1    Rum")
                    print("2    Coke")
                    print("3    Prune Juice")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Ten
                        if choice == "1":
                            print("You have selected option one, Rum.")
                            break
                        if choice == "2":
                            print("You have selected option two, Coke.")
                            break
                        if choice == "3":
                            print("You have selected option three, Prune Juice.")
                            break
                    print("Choice Eleven")
                    print("1    Tongue")
                    print("2    Sing")
                    print("3    Mop")
                    break
                while True:
                    #   Wellerman
                    while True:
                        #   Choice Eleven
                        if choice == "1":
                            print("You have selected option one, Tongue.")
                            break
                        if choice == "2":
                            print("You have selected option two, Sing.")
                            break
                        if choice == "3":
                            print("You have selected option three, Mop.")
                            break
                    break
                break
            while True:
                #   Drunken Sailor
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice One
                        if choice == "7":
                            print("You have selected option seven, Drunken.")
                            break
                        if choice == "8":
                            print("You have selected option eight, Farting.")
                            break
                        if choice == "9":
                            print("You have selected option nine, Stupid.")
                            break
                    print("Choice Two")
                    print("1    Sailor")
                    print("2    Bouncer")
                    print("3    Painter")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Two
                        if choice == "1":
                            print("You have selected option one, Sailor.")
                            break
                        if choice == "2":
                            print("You have selected option two, Bouncer.")
                            break
                        if choice == "3":
                            print("You have selected option three, Painter.")
                            break
                    print("Choice Three")
                    print("1    Early")
                    print("2    Lately")
                    print("3    Never")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Three
                        if choice == "1":
                            print("You have selected option one, Early.")
                            break
                        if choice == "2":
                            print("You have selected option two, Lately.")
                            break
                        if choice == "3":
                            print("You have selected option three, Never.")
                            break
                    print("Choice Four")
                    print("1    Morning")
                    print("2    Party")
                    print("3    Evening")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Four
                        if choice == "1":
                            print("You have selected option one, Morning.")
                            break
                        if choice == "2":
                            print("You have selected option two, Party.")
                            break
                        if choice == "3":
                            print("You have selected option three, Evening.")
                            break
                    print("Choice Five")
                    print("1    Brig")
                    print("2    Toilets")
                    print("3    Farts")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Five
                        if choice == "1":
                            print("You have selected option one, Brig.")
                            break
                        if choice == "2":
                            print("You have selected option two, Toilets.")
                            break
                        if choice == "3":
                            print("You have selected option three, Farts.")
                            break
                    print("Choice Six")
                    print("1    Rises")
                    print("2    Wiggles")
                    print("3    Bubbles")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Six
                        if choice == "1":
                            print("You have selectd option one, Rises.")
                            break
                        if choice == "2":
                            print("You have selected option two, Wiggles.")
                            break
                        if choice == "3":
                            print("You have selected option three, Bubbles.")
                            break
                    print("Choice Seven")
                    print("1    Clown")
                    print("2    Dunce")
                    print("3    Crackers")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Seven
                        if choice == "1":
                            print("You have selected option one, Clown.")
                            break
                        if choice == "2":
                            print("You have selected option two, Dunce.")
                            break
                        if choice == "3":
                            print("You have selected option three, Crackers.")
                            break
                    print("Choice Eight")
                    print("1    Wash")
                    print("2    Drink")
                    print("3    Smell")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Eight
                        if choice == "1":
                            print("You have selected option one, Wash.")
                            break
                        if choice == "2":
                            print("You have selected option two, Drink.")
                            break
                        if choice == "3":
                            print("You have selected option three, Smell.")
                            break
                    print("Choice Nine")
                    print("1    Polish")
                    print("2    Wipe")
                    print("3    Clean")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Nine
                        if choice == "1":
                            print("You have selected option one, Polish.")
                            break
                        if choice == "2":
                            print("You have selected option two, Wipe.")
                            break
                        if choice == "3":
                            print("You have selected option three, Clean.")
                            break
                    print("Choice Ten")
                    print("1    Standing")
                    print("2    Vomit")
                    print("3    Laundry")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Ten
                        if choice == "1":
                            print("You have selected option one, Standing.")
                            break
                        if choice == "2":
                            print("You have selected option two, Vomit.")
                            break
                        if choice == "3":
                            print("You have selected option three, Laundry.")
                            break
                    print("Choice Eleven")
                    print("1    Leave")
                    print("2    Breakfast")
                    print("3    Pots")
                    break
                while True:
                    #   Drunken Sailor
                    while True:
                        #   Choice Eleven
                        if choice == "1":
                            print("You have selected option one, Leave.")
                            break
                        if choice == "2":
                            print("You have selected option two, Breakfast.")
                            break
                        if choice == "3":
                            print("You have selected option three, Pots.")
                            break
                    break
                break
            while True:
                while True:
                    while True:
                        #   Choice One
                        while True:
                            if choice == "10":
                                print("You have selected option ten, Young.")
                                break
                            if choice == "11":
                                print("You have selected option eleven, Old.")
                                break
                            if choice == "12":
                                print("You have selected option twelve, Fat.")
                                break
                        print("Choice Two")
                        print("1    Fellows")
                        print("2    Chickens")
                        print("3    Farters")
                        break
                    while True:
                        #   Choice Two
                        while True:
                            if choice == "1":
                                print("You have selected option one, Fellows.")
                                break
                            if choice == "2":
                                print("You have selected option two, Chickens.")
                                break
                            if choice == "3":
                                print("You have selected option three, Farters.")
                                break   
                        print("Choice Three")
                        print("1    Sea")
                        print("2    News")
                        print("3    Game")
                        break
                    while True:
                        #   Choice Three
                        while True:
                            if choice == "1":
                                print("You have selected option one, Sea.")
                                break
                            if choice == "2":
                                print("You have selected option two, News.")
                                break
                            if choice == "3":
                                print("You have selected option three, Game.")
                                break
                        print("Choice Four")
                        print("1    Me")
                        print("2    You")
                        print("3    Down")
                        break
                    while True:
                        #   Choice Four
                        while True:
                            if choice == "1":
                                print("You have selected option one, Me.")
                                break
                            if choice == "2":
                                print("You have selected option two, You.")
                                break
                            if choice == "3":
                                print("You have selected option three, Down.")
                                break
                        print("Choice Five")
                        print("1    Blow")
                        print("2    Slap")
                        print("3    Chase")
                        break
                    while True:
                        #   Choice Five
                        while True:
                            if choice == "1":
                                print("You have selected option one, Blow.")
                                break
                            if choice == "2":
                                print("You have selected option two, Slap.")
                                break
                            if choice == "3":
                                print("You have selected option three, Chase.")
                                break
                        print("Choice Six")
                        print("1    Attention")
                        print("2    Taxes")
                        print("3    Biscuit")
                        break
                    while True:
                        #   Choice Seven
                        while True:
                            if choice == "1":
                                print("You have selected option one, Attention.")
                                break
                            if choice == "2":
                                print("You have selected option two, Taxes.")
                                break
                            if choice == "3":
                                print("You have selected option three, Biscuit.")
                                break
                        print("Choice Seven")
                        print("1    Blow")
                        print("2    Finish")
                        print("3    Take")
                        break
                    while True:
                        #   Choice Eight
                        while True:
                            if choice == "1":
                                print("You have selected option one, Blow.")
                                break
                            if choice == "2":
                                print("You have selected option two, Finish.")
                                break
                            if choice == "3":
                                print("You have selected option three, Take.")
                                break
                        print("Choice Eight")
                        print("1    Deep")
                        print("2    Business")
                        print("3    Lazy")
                        break
                    while True:
                        #   Choice Nine
                        while True:
                            if choice == "1":
                                print("You have selected option one, Deep.")
                                break
                            if choice == "2":
                                print("You have selected option two, Business.")
                                break
                            if choice == "3":
                                print("You have selected option three, Lazy.")
                                break
                        print("Choice Nine")
                        print("1    Sailor")
                        print("2    Pickle")
                        print("3    Fart")
                        break
                    while True:
                        #   Choice Ten
                        while True:
                            if choice == "1":
                                print("You have selected option one, Sailor.")
                                break
                            if choice == "2":
                                print("You have selected option two, Pickle.")
                                break
                            if choice == "3":
                                print("You have selected option three, Fart.")
                                break
                        print("Choice Ten")
                        print("1    Hong Kong")
                        print("2    The Bronx")
                        print("3    L.A.")
                        break
                    while True:
                        #   Choice Eleven   
                        while True:
                            if choice == "1":
                                print("You have selected option one, Hong Kong")
                                break
                            if choice == "2":
                                print("You have selected option two, The Bronx.")
                                break
                            if choice == "3":
                                print("You have selected option three, L.A.")
                                break
                        print("Choice Eleven")
                        print("1    Drink")
                        print("2    Cow")
                        print("3    Boot")
                        break         
                    break
                break
            while True:
                while True:
                    while True:
                        #   Choice One
                        if choice == "13":
                            print("You have selected option thirteen, Pirate.")
                            break
                        if choice == "14":
                            print("You have selected option fourteen, Teacher.")
                            break
                        if choice == "15":
                            print("You have selected option fifteen, Lawyer.")
                            break
                    print("Choice Two")
                    print("1    Me")
                    print("2    Her")
                    print("3    Them")
                    break
                while True:
                    while True:
                        #   Choice Two
                        if choice == "1":
                            print("You have selected option one, Me.")
                            break
                        if choice == "2":
                            print("You have selected option two, Her.")
                            break
                        if choice == "3":
                            print("You have selected option three, Them.")
                            break
                    print("Choice Three")
                    print("1    Pillage")
                    print("2    Sweep")
                    print("3    Bake")
                    break
                while True:
                    while True:
                        #   Choice Three
                        if choice == "1":
                            print("You have selected option one, Pillage.")
                            break
                        if choice == "2":
                            print("You have selected option two, Sweep.")
                            break
                        if choice == "3":
                            print("You have selected option three, Bake.")
                            break
                    print("Choice Four")
                    print("1    Plunder")
                    print("2    Fart")
                    print("3    Faint")
                    break
                while True:
                    while True:
                        #   Choice Four
                        if choice == "1":
                            print("You have selected option one, Plunder.")
                            break
                        if choice == "2":
                            print("You have selected option two, Fart.")
                            break
                        if choice == "3":
                            print("You have selected option three, Faint.")
                            break
                    print("Choice Five")
                    print("1    Rifle")
                    print("2    Vomit")
                    print("3    Books")
                    break
                while True:
                    while True:
                        #   Choice Five
                        if choice == "1":
                            print("You have selected option one, Rifle.")
                            break
                        if choice == "2":
                            print("You have selected option two, Vomit.")
                            break
                        if choice == "3":
                            print("You have selected option three, Books.")
                            break
                    print("Choice Six")
                    print("1    Loot")
                    print("2    Hoot")
                    print("3    Toot")
                    break
                while True:
                    while True:
                        #   Choice Six
                        if choice == "1":
                            print("You have selected option one, Loot.")
                            break
                        if choice == "2":
                            print("You have selected option two, Hoot.")
                            break
                        if choice == "3":
                            print("You have selected option three, Toot.")
                            break
                    print("Choice Seven")
                    print("1    Drink")
                    print("2    Eat")
                    print("3    Shop")
                    break
                while True:
                    while True:
                        #   Choice Seven
                        if choice == "1":
                            print("You have selected option one, Drink.")
                            break
                        if choice == "2":
                            print("You have selected option two, Eat.")
                            break
                        if choice == "3":
                            print("You have selected option three, Shop.")
                            break
                    print("Choice Eight")
                    print("1    Hearties")
                    print("2    Homies")
                    print("3    Peeps")
                    break
                while True:
                    while True:
                        #   Choice Eight
                        if choice == "1":
                            print("You have selected option one, Hearties.")
                            break
                        if choice == "2":
                            print("You have selected option two, Homies.")
                            break
                        if choice == "3":
                            print("You have selected option three, Peeps.")
                            break
                    print("Choice Nine")
                    print("1    Yo")
                    print("2    Go")
                    print("3    No")
                    break
                while True:
                    while True:
                        #   Choice Nine
                        if choice == "1":
                            print("You have selected option one, Yo.")
                            break
                        if choice == "2":
                            print("You have selected option two, Go.")
                            break
                        if choice == "3":
                            print("You have selected option three, No.")
                            break
                    print("Choice Ten")
                    print("1    Kidnap")
                    print("2    Play")
                    print("3    Buy")
                    break
                while True:
                    while True:
                        #   Choice Ten
                        if choice == "1":
                            print("You have selected option one, Kidnap.")
                            break
                        if choice == "2":
                            print("You have selected option two, Play.")
                            break
                        if choice == "3":
                            print("You have selected option three, Buy.")
                            break
                    print("Choice Eleven")
                    print("1    Hoot")
                    print("2    Crap")
                    print("3    Boot")
                    break
                while True:
                    while True:
                        #   Choice Eleven
                        if choice == "1":
                            print("You have selected option one, Hoot.")
                            break
                        if choice == "2":
                            print("You have selected option two, Crap.")
                            break
                        if choice == "3":
                            print("You have selecte doption three, Boot.")
                            break
                    break 
        elif choice == "2":
            print("You have selected option two, folk songs.")
            print("Choice One")
            print("1    Bags")
            print("2    Drugs")
            print("3    Snacks")
            print("4    Give")
            print("5    Sell")
            print("6    Rent")
            print("7    Are")
            print("8    Why")
            print("9    Were")
            print("10   Dublin")
            print("11   Mexico")
            print("12   Houston")
            print("13   Wide")
            print("14   Cold")
            print("15   Fine")
            choice = input(print("Type the number of your choice and press Enter:  "))
            while True:
                while True:
                    #   Choice Two
                    if choice == "1":
                        print("You have selected option one, Bags.")
                        break
                    if choice == "2":
                        print("You have selecte doption two, Drugs.")
                        break
                    if choice == "3":
                        print("You have selected option three, Snacks.")
                        break
                print("Choice Two")
                print("1    Go")
                print("2    Stay")
                print("3    Fight")
                break
            while True:
                while True:
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Go.")
                        break
                    if choice == "2":
                        print("You have selected option two, Stay.")
                        break
                    if choice == "3":
                        print("You have selected option three, Fight.")
                        break
                print("Choice Three")
                print("1    Door")
                print("2    Store")
                print("3    Car")
                break
            while True:
                while True:
                    #   Choice Four
                    if choice == "1":
                        print("You have selected option one, Door.")
                        break
                    if choice == "2":
                        print("You have selected option two, Store.")
                        break
                    if choice == "3":
                        print("You have selected option three, Car.")
                        break
                print("Choice Four")
                print("1    Hate")
                print("2    Love")
                print("3    Want")
                break
            while True:
                while True:
                    #   Choice Five
                    if choice == "1":
                        print("You have selected option one, Hate.")
                        break
                    if choice == "2":
                        print("You have selected option two, Love.")
                        break
                    if choice == "3":
                        print("You have selected option three, Want.")
                        break
                print("Choice Five")
                print("1    Goodbye")
                print("2    Hello")
                print("3    Fart")
                break
            while True:
                while True:
                    #   Choice Six
                    if choice == "1":
                        print("You have selected option one, Goodbye.")
                        break
                    if choice == "2":
                        print("You have selected option two, Hello.")
                        break
                    if choice == "3":
                        print("You have selected option three, Fart.")
                        break
                print("Choice Six")
                print("1    Break")
                print("2    Leave")
                print("3    Dance")
                break
            while True:
                while True:
                    #   Choice Seven
                    if choice == "1":
                        print("You have selected option one, Break.")
                        break
                    if choice == "2":
                        print("You have selected option two, Leave.")
                        break
                    if choice == "3":
                        print("You have selected option three, Dance.")
                        break
                print("Choice Seven")
                print("1    Morning")
                print("2    Warm")
                print("3    Storm")
                break
            while True:
                while True:
                    #   Choice Eight
                    if choice == "1":
                        print("You have selected option one, Morning.")
                        break
                    if choice == "2":
                        print("You have selected option two, Warm.")
                        break
                    if choice == "3":
                        print("You have selected option three, Storm.")
                        break
                print("Choice Eight")
                print("1    Wait")
                print("2    Leave")
                print("3    Burn")
                break
            while True:
                while True:
                    #   Choice Nine
                    if choice == "1":
                        print("You have selected option one, Wait.")
                        break
                    if choice == "2":
                        print("You have selected option two, Leave.")
                        break
                    if choice == "3":
                        print("You have selected option three, Burn.")
                        break
                print("Choice Nine")
                print("1    Lonesome")
                print("2    Sleepy")
                print("3    Angry")
                break
            while True:
                while True:
                    #   Choice Ten
                    if choice == "1":
                        print("You have selected option one, Lonesome.")
                        break
                    if choice == "2":
                        print("You have selected option two, Sleepy.")
                        break
                    if choice == "3":
                        print("You have selected option three, Angry.")
                        break
                print("Choice Ten")
                print("1    Die")
                print("2    Fly")
                print("3    Sue")
                break
            while True:
                while True:
                    #   Choice Eleven
                    if choice == "1":
                        print("You have selected option one, Die.")
                        break
                    if choice == "2":
                        print("You have selected option two, Fly.")
                        break
                    if choice == "3":
                        print("You have selected option three, Sue.")
                        break
                print("Choice Eleven")
                print("1    Go")
                print("2    Belch")
                print("3    Fart")
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "4":
                        print("You have selected option four, Give.")
                        break
                    if choice == "5":
                        print("You have selected option five, Sell.")
                        break
                    if choice == "6":
                        print("You have selected option six, Rent.")
                        break
                print("Choice Two")
                print("1    Me")
                print("2    Her")
                print("3    Them")
                break
            while True:
                while True:
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Me.")
                        break
                    if choice == "2":
                        print("You have selected option two, Her.")
                        break
                    if choice == "3":
                        print("You have selected option three, Them.")
                        break
                print("Choice Three")
                print("1    Home")
                print("2    Job")
                print("3    Zone")
                break
            while True:
                while True:
                    #   Choice Four
                    if choice == "1":
                        print("You have selected option one, Home.")
                        break
                    if choice == "2":
                        print("You have selected option two, Job.")
                        break
                    if choice == "3":
                        print("You have selected option three, Zone.")
                        break
                print("Choice Four")
                print("1    Buffalo")
                print("2    Carrot")
                print("3    Stanley")
                break
            while True:
                while True:
                    #   Choice Five
                    if choice == "1":
                        print("You have selected option one, Buffalo.")
                        break
                    if choice == "2":
                        print("You have selected option two, Carrot.")
                        break
                    if choice == "3":
                        print("You have selected option three, Stanley.")
                        break
                print("Choice Five")
                print("1    Roam")
                print("2    Sing")
                print("3    Jump")
                break
            while True:
                while True:
                    #   Choice Six
                    if choice == "1":
                        print("You have selected option one, Roam.")
                        break
                    if choice == "2":
                        print("You have selected option two, Sing.")
                        break
                    if choice == "3":
                        print("You have selected option three, Jump.")
                        break
                print("Choice Six")
                print("1    Deer")
                print("2    Skunk")
                print("3    Mouse")
                break
            while True:
                while True:
                    #   Choice Seven
                    if choice == "1":
                        print("You have selected option one, Deer.")
                        break
                    if choice == "2":
                        print("You have selected option two, Skunk.")
                        break
                    if choice == "3":
                        print("You have selected option three, Mouse.")
                        break
                print("Choice Seven")
                print("1    Antelope")
                print("2    Ant")
                print("3    Bear")
                break
            while True:
                while True:
                    #   Choice Eight
                    if choice == "1":
                        print("You have selected option one, Antelope.")
                        break
                    if choice == "2":
                        print("You have selected option two, Ant.")
                        break
                    if choice == "3":
                        print("You have selected option three, Bear.")
                        break
                print("Choice Eight")
                print("1    Seldom")
                print("2    Sometimes")
                print("3    Daily")
                break
            while True:
                while True:
                    #   Choice Nine
                    if choice == "1":
                        print("You have selected option one, Seldom.")
                        break
                    if choice == "2":
                        print("You have selected option two, Sometimes.")
                        break
                    if choice == "3":
                        print("You have selected option three, Daily.")
                        break
                print("Choice Nine")
                print("1    Discourage")
                print("2    Encourage")
                print("3    Ridiculous")
                break
            while True:
                while True:
                    #   Choice Ten
                    if choice == "1":
                        print("You have selected option one, Discourage.")
                        break
                    if choice == "2":
                        print("You have selected option two, Encourage.")
                        break
                    if choice == "3":
                        print("You have selected option three, Ridiculous.")
                        break
                print("Choice Ten")
                print("1    Sky")
                print("2    Beer")
                print("3    Eye")
                break
            while True:
                while True:
                    #   Choice Eleven
                    if choice == "1":
                        print("You have selected option one, Sky.")
                        break
                    if choice == "2":
                        print("You have selected option two, Beer.")
                        break
                    if choice == "3":
                        print("You have selected option three, Eye.")
                        break
                print("Choice Eleven")
                print("1    Cloud")
                print("2    Storm")
                print("3    Rain")
                break
            while True:
                while True:
                    #   Choice One
                    if choice == "7":
                        print("You have selected option one, Cloud.")
                        break
                    if choice == "8":
                        print("You have selected option two, Storm.")
                        break
                    if choice == "9":
                        print("You have selected option three, Rain.")
                        break
                print("Choice One")
                print("1    Are")
                print("2    Were")
                print("3    Why")
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "1":
                        print("You have selected option one, Are.")
                        break
                    if choice == "2":
                        print("You have selected option two, Were.")
                        break
                    if choice == "3":
                        print("You have selected option three, Why.")
                        break
                print("Choice Two")
                print("1    Go")
                print("2    Dance")
                print("3    Fly")
                break
            while True:
                while True:
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Go.")
                        break
                    if choice == "2":
                        print("You have selected option two, Dance.")
                        break
                    if choice == "3":
                        print("You have selected option three, Fly.")
                        break
                print("Choice Three")
                print("1    Scarborough")
                print("2    Grocery")
                print("3    Comic")
                break
            while True:
                while True:
                    #   Choice Four
                    if choice == "1":
                        print("You have selected option one, Scarborough.")
                        break
                    if choice == "2":
                        print("You have selected option two, Grocery.")
                        break
                    if choice == "3":
                        print("You have selected option three, Comic.")
                        break
                print("Choice Four")
                print("1    Parsley")
                print("2    Basil")
                print("3    Chicken")
                break
            while True:
                while True:
                    #   Choice Five
                    if choice == "1":
                        print("You have selected option one, Parsley.")
                        break
                    if choice == "2":
                        print("You have selected option two, Basil.")
                        break
                    if choice == "3":
                        print("You have selected option three, Chicken.")
                        break
                print("Choice Five")
                print("1    Sage")
                print("2    Cheese")
                print("3    Salt")
                break
            while True:
                while True:
                    #   Choice Six
                    if choice == "1":
                        print("You have selected option one, Sage.")
                        break
                    if choice == "2":
                        print("You have selected option two, Cheese.")
                        break
                    if choice == "3":
                        print("You have selected option three, Salt.")
                        break
                print("Choice Six")
                print("1    Rosemary")
                print("2    Snickers")
                print("3    Mojitos")
                break
            while True:
                while True:
                    #   Choice Seven
                    if choice == "1":
                        print("You have selected option one, Rosemary.")
                        break
                    if choice == "2":
                        print("You have selected option two, Snickers.")
                        break
                    if choice == "3":
                        print("You have selected option three, Mojitos.")
                        break
                print("Choice Seven")
                print("1    Thyme")
                print("2    Crime")
                print("3    Milk")
                break
            while True:
                while True:
                    #   Choice Eight
                    if choice == "1":
                        print("You have selected option one, Thyme.")
                        break
                    if choice == "2":
                        print("You have selected option two, Crime.")
                        break
                    if choice == "3":
                        print("You have selected option three, Milk.")
                        break
                print("Choice Eight")
                print("1    Remember")
                print("2    Forget")
                print("3    Trash Talk")
                break
            while True:
                while True:
                    #   Choice Nine
                    if choice == "1":
                        print("You have selected option one, Remember.")
                        break
                    if choice == "2":
                        print("You have selected option two, Forget.")
                        break
                    if choice == "3":
                        print("You have selected option three, Trash Talk.")
                        break
                print("Choice Nine")
                print("1    Me")
                print("2    Him")
                print("3    Her")
                break
            while True:
                while True:
                    #   Choice Ten
                    if choice == "1":
                        print("You have selected option one, Me.")
                        break
                    if choice == "2":
                        print("You have selected option two, Him.")
                        break
                    if choice == "3":
                        print("You have selected option three, Her.")
                        break
                print("Choice Ten")
                print("1    There")
                print("2    Here")
                print("3    Near")
                break
            while True:
                while True:
                    #   Choice Eleven
                    if choice == "1":
                        print("You have selected option one, There.")
                        break
                    if choice == "2":
                        print("You have selected option two, Here.")
                        break
                    if choice == "3":
                        print("You have selected option three, Near.")
                        break
                print("Choice Eleven")
                print("1    Love")
                print("2    Llama")
                print("3    Hate")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Love.")
                        break
                    if choice == "2":
                        print("You have selected option two, Llama.")
                        break
                    if choice == "3":
                        print("You have selected option three, Hate.")
                        break
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "10":
                        print("You have selected option ten, Dublin.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Mexico.")
                        break
                    if choice == "13":
                        print("You have selected option twelve, Houston.")
                        break
                print("Choice Two")
                print("1    Sweet")
                print("2    Weird")
                print("3    Old")
                break
            while True:
                while True:
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Sweet.")
                        break
                    if choice == "2":
                        print("You have selected option two, Weird.")
                        break
                    if choice == "3":
                        print("You have selected option three, Old.")
                        break
                print("Choice Three")
                print("1    Push")
                print("2    Sue")
                print("3    Shake")
                break
            while True:
                while True:
                    #   Choice Four
                    if choice == "1":
                        print("You have selected option one, Push.")
                        break
                    if choice == "2":
                        print("You have selected option two, Sue.")
                        break
                    if choice == "3":
                        print("You have selected option three, Shake.")
                        break
                print("Choice Four")
                print("1    Her")
                print("2    His")
                print("3    My")
                break
            while True:
                while True:
                    #   Choice Five
                    if choice == "1":
                        print("You have selected option one, Her.")
                        break
                    if choice == "2":
                        print("You have selected option two, His.")
                        break
                    if choice == "3":
                        print("You have selected option three, My.")
                        break
                print("Choice Five")
                print("1    Wheelbarrow")
                print("2    Knapsack")
                print("3    Camaro")
                break
            while True:
                while True:
                    #   Choice Six
                    if choice == "1":
                        print("You have selected option one, Wheelbarrow.")
                        break
                    if choice == "2":
                        print("You have selected option two, Knapsack.")
                        break
                    if choice == "3":
                        print("You have selected option three, Camaro.")
                        break
                print("Choice Six")
                print("1    Street")
                print("2    Car")
                print("3    Store")
                break
            while True:
                while True:
                    #   Choice Seven
                    if choice == "1":
                        print("You have selected option one, Street.")
                        break
                    if choice == "2":
                        print("You have selected option two, Car.")
                        break
                    if choice == "3":
                        print("You have selected option three, Store.")
                        break
                print("Choice Seven")
                print("1    Broad")
                print("2    Closed")
                print("3    Old")
                break
            while True:
                while True:
                    #   Choice Eight
                    if choice == "1":
                        print("You have selected option one, Broad.")
                        break
                    if choice == "2":
                        print("You have selected option two, Closed.")
                        break
                    if choice == "3":
                        print("You have selected option three, Old.")
                        break
                print("Choice Eight")
                print("1    Narrow")
                print("2    Nasty")
                print("3    Slippery")
                break
            while True:
                while True:
                    #   Choice Nine
                    if choice == "1":
                        print("You have selected option one, Narrow.")
                        break
                    if choice == "2":
                        print("You have selected option two, Nasty.")
                        break
                    if choice == "3":
                        print("You have selected option three, Slippery.")
                        break
                print("Choice Nine")
                print("1    Cockles")
                print("2    Cookies")
                print("3    Pencils")
                break
            while True:
                while True:
                    #   Choice Ten
                    if choice == "1":
                        print("You have selected option one, Cockles.")
                        break
                    if choice == "2":
                        print("You have selected option two, Cookies.")
                        break
                    if choice == "3":
                        print("You have selected option three, Pencils.")
                        break
                print("Choice Ten")
                print("1    Mussels")
                print("2    Taters")
                print("3    French")
                break
            while True:
                while True:
                    #   Choice Eleven
                    if choice == "1":
                        print("You have selected option one, Mussels.")
                        break
                    if choice == "2":
                        print("You have selected option two, Taters.")
                        break
                    if choice == "3":
                        print("You have selected option three, French.")
                        break
                print("Choice Eleven")
                print("1    Alive")
                print("2    Best")
                print("3    Pay")
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "13":
                        print("You have selected option thirteen, Wide.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Cold")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Fine.")
                        break
                print("Choice Two")
                print("1    Swim")
                print("2    Buy")
                print("3    Want")
                break
            while True:
                while True:        
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Swim.")
                        break
                    if choice == "2":
                        print("You have selected option two, Buy.")
                        break
                    if choice == "3":
                        print("You have selected option three, Want.")
                        break
                print("Choice Three")
                print("1    Wing")
                print("2    Ticket")
                print("3    Bird")
                break
            while True:
                #   The Water is Wide
                while True:
                    #   Choice Four
                    if choice == "1":
                        print("You have selected option one, Wing.")
                        break
                    if choice == "2":
                        print("You have selected option two, Ticket.")
                        break
                    if choice == "3":
                        print("You have selected option three, Bird.")
                print("Choice Four")
                print("1    Build")
                print("2    Buy")
                print("3    Sell")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Five
                    if choice == "1":
                        print("You have selected option one, Build.")
                        break
                    if choice == "2":
                        print("You have selected option two, Buy.")
                        break
                    if choice == "3":
                        print("You have selected option three, Sell.")
                        break
                print("Choice Five")
                print("1    Me")
                print("2    Her")
                print("3    Him")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Six
                    if choice == "1":
                        print("You have selected option one, Me.")
                        break
                    if choice == "2":
                        print("You have selected option two, Her.")
                        break
                    if choice == "3":
                        print("You have selected option three, Him.")
                        break
                print("Choice Six")
                print("1    Boat")
                print("2    Mouse")
                print("3    Car")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Seven
                    if choice == "1":
                        print("You have selected option one, Boat.")
                        break
                    if choice == "2":
                        print("You have selected option two, Mouse.")
                        break
                    if choice == "3":
                        print("You have selected option three, Car.")
                        break
                print("Choice Seven")
                print("1    Carry")
                print("2    Ferry")
                print("3    Can't")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Eight
                    if choice == "1":
                        print("You have selected option one, Carry.")
                        break
                    if choice == "2":
                        print("You have selected option two, Ferry.")
                        break
                    if choice == "3":
                        print("You have selected option three, Can't.")
                        break
                print("Choice Eight")
                print("1    Two")
                print("2    Three")
                print("3    Four")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Nine
                    if choice == "1":
                        print("You have selected option one, Two.")
                        break
                    if choice == "2":
                        print("You have selected option two, Three.")
                        break
                    if choice == "3":
                        print("You have selected option three, Four.")
                        break
                print("Choice Nine")
                print("1    Row")
                print("2    Tow")
                print("3    Leave")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Ten
                    if choice == "1":
                        print("You have selected option one, Row.")
                        break
                    if choice == "2":
                        print("You have selected option two, Tow.")
                        break
                    if choice == "3":
                        print("You have selected option three, Leave.")
                        break
                print("Choice Ten")
                print("1    Love")
                print("2    Bro")
                print("3    Cat")
                break
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Eleven
                    if choice == "1":
                        print("You have selected option one, Love.")
                        break
                    if choice == "2":
                        print("You have selected option two, Bro.")
                        break
                    if choice == "3":
                        print("You have selected option three, Cat.")
                        break
                print("Choice Eleven")
                print("1    I")
                print("2    You")
                print("3    Her")
                break
            while True:
                #   The Water is Wide
                while True:
                    if choice == "1":
                        print("You have selected option one, I.")
                        break
                    if choice == "2":
                        print("You have selected option two, You.")
                        break
                    if choice == "3":
                        print("You have selected option three, Her.")
                        break
        elif choice == "3":
            print("You have selected option three, total chaos.")
            while True:
                print("Choice One")
                print("1    I           16  Bags")
                print("2    They        17  Drugs")
                print("3    We          18  Snacks")
                print("4    Once        19  Give")
                print("5    Twice       20  Sell")
                print("6    Thrice      21  Rent")
                print("7    Drunken     21  Rent")
                print("8    Farting     23  Why")
                print("9    Stupid      24  Were")
                print("10   Young       25  Dublin")
                print("11   Old         26  Mexico")
                print("12   Fat         27  Houston")
                print("13   Pirate      28  Wide")
                print("14   Teacher     29  Cold")
                print("15   Lawyer      30  Fine")
                while True:        
                    #   Choice Two
                    if choice == "1":
                        print("You have selected option one, I.")
                        break
                    if choice == "2":
                        print("You have selected option two, They.")
                        break
                    if choice == "3":
                        print("You have selected option three, We.")
                        break
                    if choice == "4":
                        print("You have selected option four, Once.")
                        break
                    if choice == "5":
                        print("You have selected option five, Twice.")
                        break
                    if choice == "6":
                        print("You have selected option six, Thrice.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Drunken.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Farting.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Stupid.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Young.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Old.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Fat.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Pirate.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Teacher.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Lawyer.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Bags.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Drugs.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Snacks.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Give.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Sell.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Rent.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Are.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Why.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Were.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Dublin.")
                        break   
                    if choice == "26":
                        print("You have selected option twenty-six, Mexico.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Houston.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Wide.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Cold.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Fine.")
                        break
                print("Choice Two")
                print("1    Old         16  Go")
                print("2    Tall        17  Stay")
                print("3    Sad         18  Fight")
                print("4    Billy       19  Me")
                print("5    Enterprise  20  Her")
                print("6    Carpenter   21  Them")
                print("7    Sailor      22  Going")
                print("8    Bouncer     23  Dance")
                print("9    Painter     24  Fly")
                print("10   Fellows     25  Sweet")
                print("11   Chickens    26  Weird")
                print("12   Farters     27  Old")
                print("13   Me          28  Swim")
                print("14   Her         29  Buy")
                print("15   Them        30  Want")
                break
            while True:
                while True:        
                    #   Choice Three
                    if choice == "1":
                        print("You have selected option one, Old.")
                        break
                    if choice == "2":
                        print("You have selected option two, Tall.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Sad.")
                        break
                    if choice == "4":
                        print("You have selected option four, Billy.")
                        break
                    if choice == "5":
                        print("You have selected option five, Enterprise.")
                        break
                    if choice == "6":
                        print("You have selected option six, Carpenter.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Sailor.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Bouncer.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Painter.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Fellows.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Chickens.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Farters.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Me.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Her.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Them.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Go.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Stay.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Fight.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Me.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Her.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Them.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Going.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Dance.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Fly.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Sweet.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Weird.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Old.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Swim.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Buy.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Want.")
                        break
                print("Choice Three")
                print("1    Say         16  Door")
                print("2    Yell        17  Store")
                print("3    Wish        18  Car")
                print("4    Up          19  Home")
                print("5    Down        20  Job")
                print("6    In          21  Zone")
                print("7    Early       22  Scarborough")
                print("8    Lately      23  Grocery")
                print("9    Never       24  Comic")
                print("10   Sea         25  Push")
                print("11   News        26  Sue")
                print("12   Game        27  Shake")
                print("13   Pillage     28  Wing")
                print("14   Sweep       29  Ticket")
                print("15   Bake        30  Bird")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Say.")
                        break
                    if choice == "2":
                        print("You have selected option two, Yell.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Wish.")
                        break
                    if choice == "4":
                        print("You have selected option four, Up.")
                        break
                    if choice == "5":
                        print("You have selected option five, Down.")
                        break
                    if choice == "6":
                        print("You have selected option six, In.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Early.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Lately.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Never.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Sea.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, News.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Game.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Pillage.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Sweep.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Bake.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Door.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Store.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Car.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Home.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Job.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Zone.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Scarborough.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Grocery.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Comic.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Push.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Sue.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Shake.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Wing.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Ticket.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Bird.")
                        break
                print("Choice Four")
                print("1    Leave       16  Hate")
                print("2    Watch       17  Love")
                print("3    Trust       18  Want")
                print("4    Blow        19  Buffalo")
                print("5    Sing        20  Carrot")
                print("6    Dance       21  Stanley")
                print("7    Morning     22  Parsley")
                print("8    Party       23  Basil")
                print("9    Evening     24  Chicken")
                print("10   Me          25  Her")
                print("11   You         26  His")
                print("12   Down        27  My")
                print("13   Plunder     28  Build")
                print("14   Fart        29  Buy")
                print("15   Faint       30  Sell")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Leave.")
                        break
                    if choice == "2":
                        print("You have selected option two, Watch.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Trust.")
                        break
                    if choice == "4":
                        print("You have selected option four, Blow.")
                        break
                    if choice == "5":
                        print("You have selected option five, Sing.")
                        break
                    if choice == "6":
                        print("You have selected option six, Dance.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Morning.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Party.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Evening.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Me.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, You.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Down.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Plunder.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Fart.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Faint.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Hate.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Love.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Want.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Buffalo.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Carrot.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Stanley.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Parsley.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Basil.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Chicken.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Her.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, His.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, My.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Build.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Buy.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Sell.")
                        break        
                print("Choice Five")
                print("1    Johnny      16  Goodbye")
                print("2    Timmy       17  Hello")
                print("3    Frodo       18  Fart")
                print("4    Soon        19  Roam")
                print("5    When        20  Sing")
                print("6    Why         21  Jump")
                print("7    Brig        22  Sage")
                print("8    Toilets     23  Cheese")
                print("9    Farts       24  Salt")
                print("10   Blow        25  Wheelbarrow")
                print("11   Slap        26  Knapsack")
                print("12   Chase       27  Camaro")
                print("13   Rifle       28  Me")
                print("14   Vomit       29  Her")
                print("15   Books       30  Him")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Johnny.")
                        break
                    if choice == "2":
                        print("You have selected option two, Timmy.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Frodo.")
                        break
                    if choice == "4":
                        print("You have selected option four, Soon.")
                        break
                    if choice == "5":
                        print("You have selected option five, When.")
                        break
                    if choice == "6":
                        print("You have selected option six, Why.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Brig.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Toilets.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Farts.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Blow.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Slap.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Chase.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Rifle.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Vomit.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Books.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Goodbye.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Hello.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Fart.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Roam.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Sing.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Jump.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Sage.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Cheese.")                       
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Salt.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Wheelbarrow.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Knapsack.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Camaro.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Me.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Her.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Him.")
                        break        
                print("Choice Six")
                print("1    Tomorrow    16  Break")
                print("2    Tuesday     17  Leave")
                print("3    Friday      18  Dance")
                print("4    Wellerman   19  Deer")
                print("5    Butterfly   20  Skunk")
                print("6    Limousine   21  Mouse")
                print("7    Rises       22  Rosemary")
                print("8    Wiggles     23  Snickers")
                print("9    Bubbles     24  Mojitos")
                print("10   Attention   25  Street")
                print("11   Taxes       26  Car")
                print("12   Biscuit     27  Store")
                print("13   Loot        28  Boat")
                print("14   Hoot        29  Mouse")
                print("15   Toot        30  Car")
                break
            while True:
                while True:        
                    if choice == "1":
                        print("You have selected option one, Tomorrow.")
                        break
                    if choice == "2":
                        print("You have selected option two, Tuesday.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Friday.")
                        break
                    if choice == "4":
                        print("You have selected option four, Wellerman.")
                        break
                    if choice == "5":
                        print("You have selected option five, Butterfly.")
                        break
                    if choice == "6":
                        print("You have selected option six, Limousine.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Rises.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Wiggles.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Bubbles.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Attention.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Taxes.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Biscuit.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Loot.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Hoot.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Toot.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Break.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Leave.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Dance.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Deer.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Skunk.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Mouse.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Rosemary.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Snickers.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Mojitos.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Street.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Car.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Store.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Boat.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Mouse.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Car.")
                        break        
                print("Choice Seven")
                print("1    Pay         16  Morning")
                print("2    Bell        17  Warm")
                print("3    Fish        18  Storm")
                print("4    Come        19  Antelope")
                print("5    Go          20  Ant")
                print("6    Leave       21  Bear")
                print("7    Clown       22  Thyme")
                print("8    Dunce       23  Crime")
                print("9    Crackers    24  Milk")
                print("10   Blow        25  Broad")
                print("11   Finish      26  Closed")
                print("12   Take        27  Old")
                print("13   Drink       28  Carry")
                print("14   Eat         29  Ferry")
                print("15   Shop        30  Can't")
                break
            while True:
                while True:        
                    if choice == "1":
                        print("You have selected option one, Pay.")
                        break
                    if choice == "2":
                        print("You have selected option two, Bell.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Fish.")
                        break
                    if choice == "4":
                        print("You have selected option four, Come.")
                        break
                    if choice == "5":
                        print("You have selected option five, Go.")
                        break
                    if choice == "6":
                        print("You have selected option six, Leave.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Clown.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Dunce.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Crackers.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Blow.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Finish.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Take.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Drink.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Eat.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Shop.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Morning.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Warm.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Storm.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Antelope.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Ant.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Bear.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Thyme.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Crime.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Milk.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Broad.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Closed.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Old.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Carry.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Ferry.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Can't.")
                        break       
                print("Choice Eight")
                print("1    Long        16  Wait")
                print("2    Short       17  Leave")
                print("3    Wild        18  Burn")
                print("4    Sugar       19  Seldom")
                print("5    Twizzlers   20  Sometimes")
                print("6    Pizza       21  Daily")
                print("7    Wash        22  Remember")
                print("8    Drink       23  Forget")
                print("9    Smell       24  Trash Talk")
                print("10   Deep        25  Narrow")
                print("11   Business    26  Nasty")
                print("12   Lazy        27  Slippery")
                print("13   Hearties    28  Two")
                print("14   Homies      29  Three")
                print("15   Peeps       30  Four")
                break
            while True:
                while True:        
                    if choice == "1":
                        print("You have selected option one, Long.")
                        break
                    if choice == "2":
                        print("You have selected option two, Short.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Wild.")
                        break
                    if choice == "4":
                        print("You have selected option four, Sugar.")
                        break
                    if choice == "5":
                        print("You have selected option five, Twizzlers.")
                        break
                    if choice == "6":
                        print("You have selected option six, Pizza.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Wash.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Drink.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Smell.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Deep.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Business.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Lazy.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Hearties.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Homies.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Peeps.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Wait.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Leave.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Burn.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Seldom.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Sometimes.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Daily.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Remember.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Forget.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Trash Talk.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Narrow.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Nasty.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Slippery.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Two.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Three.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Four.")
                        break               
                print("Choice Nine")
                print("1    Wind        16  Lonesome")
                print("2    Food        17  Sleepy")
                print("3    Smell       18  Angry")
                print("4    Tea         19  Discourage")
                print("5    T-shirts    20  Encourage")
                print("6    Shoes       21  Ridiculous")
                print("7    Polish      22  Me")
                print("8    Wipe        23  Him")
                print("9    Clean       24  Her")
                print("10   Sailor      25  Cockles")
                print("11   Pickle      26  Cookies")
                print("12   Fart        27  Pencils")
                print("13   Yo          28  Row")
                print("14   Go          29  Tow")
                print("15   No          30  Leave")
                break
            while True:
                while True:        
                    if choice == "1":
                        print("You have selected option one, Wind.")
                        break
                    if choice == "2":
                        print("You have selected option two, Food.")
                        break
                    if choice == "3":
                        print("You have selected option three, Smell.")
                        break
                    if choice == "4":
                        print("You have selectedoption four, Tea.")
                        break
                    if choice == "5":
                        print("You have selected option five, T-shirts.")
                        break
                    if choice == "6":
                        print("You have selected option six, Shoes.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Polish.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Wipe.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Clean.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Sailor.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Pickle.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Fart.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Yo.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Go.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, No.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Lonesome.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Sleepy.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Angry.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Discourage.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Encourage.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Ridiculous.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Me.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Him.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Her.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Cockles.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Cookies.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Pencils.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Row.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Tow.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Leave.")
                        break
                print("Choice Ten")
                print("1    Foul        16  Die")
                print("2    Cold        17  Fly")
                print("3    Weird       18  Sue")
                print("4    Rum         19  Sky")
                print("5    Coke        20  Beer")
                print("6    Prune Juice 21  Eye")
                print("7    Standing    22  There")
                print("8    Vomit       23  Here")
                print("9    Laundry     24  Near")
                print("10   Hong Kong   25  Mussels")
                print("11   The Bronx   26  Taters")
                print("12   L.A.        27  French")
                print("13   Kidnap      28  Love")
                print("14   Play        29  Bro")
                print("15   Buy         30  Cat")
                break
            while True:        
                while True:    
                    if choice == "1":
                        print("You have selected option one, Foul.")
                        break
                    if choice == "2":
                        print("You have selected option two, Cold.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Weird.")
                        break
                    if choice == "4":
                        print("You have selected option four, Rum.")
                        break
                    if choice == "5":
                        print("You have selected option five, Coke.")
                        break
                    if choice == "6":
                        print("You have selected option six, Prune Juice.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Standing.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Vomit.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Laundry.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Hong Kong.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, The Bronx.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, L.A.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Kidnap.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Play.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Buy.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Die.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Fly.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Sue.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Sky.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Beer.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Eye.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, There.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Here.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Near.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Mussels.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Taters.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, French.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Love.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Bro.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Cat.")
                        break       
                print("Choice Eleven")
                print("1    None        16  Go")
                print("2    All         17  Belch")
                print("3    Some        18  Fart")
                print("4    Tongue      19  Cloud")
                print("5    Sing        20  Storm")
                print("6    Mop         21  Rain")
                print("7    Leave       22  Love")
                print("8    Breakfast   23  Llama")
                print("9    Pots        24  Hate")
                print("10   Drink       25  Alive")
                print("11   Cow         26  Best")
                print("12   Toilet      27  Pay")
                print("13   Hoot        28  I")
                print("14   Crap        29  You")
                print("15   Boot        30  Her")
                break
            while True:
                while True:        
                    if choice == "1":
                        print("You have selected option one, None.")
                        break
                    if choice == "2":
                        print("You have selected option two, All.")
                        break    
                    if choice == "3":
                        print("You have selected option three, Some.")
                        break
                    if choice == "4":
                        print("You have selected option four, Tongue.")
                        break
                    if choice == "5":
                        print("You have selected option five, Sing.")
                        break
                    if choice == "6":
                        print("You have selected option six, Mop.")
                        break
                    if choice == "7":
                        print("You have selected option seven, Leave.")
                        break
                    if choice == "8":
                        print("You have selected option eight, Breakfast.")
                        break
                    if choice == "9":
                        print("You have selected option nine, Pots.")
                        break
                    if choice == "10":
                        print("You have selected option ten, Drink.")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Cow.")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Toilet.")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Hoot.")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Crap.")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Boot.")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Go.")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Belch.")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Fart.")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Cloud.")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Storm.")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Rain.")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Love.")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Llama.")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Hate.")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Alive.")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Best.")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Pay.")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, I.")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, You.")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Her.")
                        break       
                break        
        else:
            print("Please select from the provided options.")
            continue
#   Main Branch Decision Loop:  Seeing if you want to listen to your finished poem.
while True:
    print("Are you ready to listen to your poem?")
    choice = input(print("Type Y or N and press Enter:  "))
    if choice == "Y":
        print("All right, here we go!")
        break
    elif choice == "N":
        print("Just let me know when you're ready, then.")
        continue
    else:
        print("Please choose from the provided options.")
        break
#   Main Branch Loop:  Listening to your finished poem.
while True:
    #   Leave Her, Johnny
        #   I/They/We thought I/They/We heard
            #   I thought I heard the Old Man say, "Leave her, Johnny."
            #   They thought they heard the Old Man say, "Leave her, Johnny."
            #   We thought we heard the Old Man say, "Leave her, Johnny."
        #   The Old/Tall/Sad Man say/yell/wish
            #   I thought I heard the Old Man say, "Leave her, Johnny."
            #   I thought I heard the Tall Man say, "Leave her, Johnny."
            #   I thought I heard the Sad Man say, "Leave her, Johnny."
            #   I thought I heard the Old Man yell, "Leave her, Johnny."
            #   I thought I heard the Old Man wish, "Leave her, Johnny."
        #   Leave/Watch/Trust her, Johnny/Timmy/Frodo, Leave/Watch/Trust her
            #   Leave her.
            #   Watch her.
            #   Trust her.
            #   Leave her, Johnny.
            #   Leave her, Timmy.
            #   Leave her, Frodo.
        #   Tomorrow/Next Tuesday/On Friday, ye will get your pay/bell/fish
            #   Tomorrow, ye will get your pay.
            #   Next Tuesday, ye will get your pay.
            #   On Friday, ye will get your pay.
            #   Tomorrow, ye will get your bell.
            #   Tomorrow, ye will get your fish.
        #   And it's time for us to leave/watch/trust her
            #   And it's time for us to leave her.
            #   And it's time for us to watch her.
            #   And it's time for us to trust her.
        #   Oh, the wind/food/smell was foul/cold/weird, and the sea ran high
            #   Oh, the wind was foul.
            #   Oh, the food was foul.
            #   Oh, the smell was foul.
            #   Oh, the wind was cold, and the sea ran high.
            #   Oh, the wind was weird, and the sea ran high.
        #   She shipped it green, and none/all/some went by
            #   She shipped it green, and none went by.
            #   She shipped it green, and all went by.
            #   She shipped it green, and some went by.
        #   Oh, leave/watch/trust her, Johnny/Timmy/Frodo, leave/watch/trust her
            #   Oh, leave her, Johnny, leave her.
            #   Oh, watch her, Johnny, watch her.
            #   Oh, trust her, Johnny, trust her.
            #   Oh, leave her, Timmy.
            #   Oh, leave her, Frodo.
        #   For the voyage is long/short/wild, and the winds don't blow
            #   For the voyage is long, and the winds don't blow.
            #   For the voyage is short, adn the winds don't blow.
            #   For the voyage is wild, adn the winds don't blow.
    #   Wellerman
        #   There once/twice/thrice was a ship that put to sea
            #   There once was a ship that put to sea.
            #   There twice was a ship that put to sea.
            #   There thrice was a ship that put to sea.
        #   The name of the ship was the Billy of Tea/Enterprise D/Carpenter Bee
            #   The name of the ship was the Billy of Tea.
            #   The name of the ship was the Enterprise D.
            #   The name of the ship was the Carpenter Bee.
        #   The winds blew up/down/in, her bow dipped down
            #   The winds blew up.
            #   The winds blew down.
            #   The winds blew in.
            #   Her bow dipped down.
        #   Oh, blow/sing/dance, my bully boys, blow/sing/dance
            #   Oh, blow, my bully boys, blow.
            #   Oh, sing, my bully boys, sing.
            #   Oh, dance, my bully boys, dance.
        #   Soon/When/Why may the Wellerman/Butterfly/Limousine come/go/leave
            #   Soon may the Wellerman come to bring us sugar and tea and rum.
            #   When may the Wellerman come to bring us sugar and tea and rum?
            #   Why may the Wellerman come to bring us sugar and tea and rum?
            #   Soon may the Wellerman go.
            #   Soon may the Wellerman leave.
            #   Soon may the Butterfly come.
            #   Soon may the Limousine come.
        #   To bring us sugar/Twizzlers/pizza and tea/T-shirts/shoes and rum/Coke/prune juice
            #   Soon may the Wellerman come to bring us sugar and tea and rum.
            #   Soon may the Wellerman come to bring us Twizzlers and tea and rum.
            #   Soon may the Wellerman come to bring us pizza and tea and rum.
            #   Soon may the Wellerman come to bring us sugar and T-shirts and Coke.
            #   Soon may the Wellerman come to bring us sugar and shoes and prune juice.
        #   One day when the tonguing/singing/mopping is done
            #   One day when the tonguing is done, we'll take our leave and go.
            #   One day when the singing is done, we'll take our leave and go.
            #   One day when the mopping is done, we'll take our leave and go.
    #   Drunken Sailor
        #   What do you do with a drunken/farting/stupid sailor/bouncer/painter
            #   What do you do with a drunken sailor early in the morning?
            #   What do you do with a drunken bouncer early in the morning?
            #   What do you do with a drunken painter early in the morning?
            #   What do you do with a farting sailor early in the morning?
            #   What do you do with a farting bouncer early in the morning?
            #   What do you do with a farting painter early in the morning?
            #   What do you do with a stupid sailor early in the morning?
            #   What do you do with a stupid bouncer early in the morning?
            #   What do you do with a stupid painter early in the morning?
        #   Early/Lately/Never in the morning/at the party/in the evening
            #   What do you do with a drunken sailor lately in the morning?
            #   What do you do with a drunken sailor lately at the party?
            #   What do you do with a drunken sailor lately in the evening?
            #   What do you do with a drunken sailor never in the morning?            
        #   Put him in the brig/Make him clean the toilets/Make him smell your farts until he's sober
            #   Put him in the brig until he's sober.
            #   Make him clean the toilets until he's sober.
            #   Make him smell your farts until he's sober.
            #   Make him wear a clown suit until he's sober.
            #   Make him wear a dunce cap until he's sober.
            #   Make him just eat crackers until he's sober.
        #   Wey, hey, and up she rises/wiggles/bubbles.
            #   Wey, hey, and up she rises.
            #   Wey, hey, and up she wiggles.
            #   Wey, hey, and up she bubbles.
        #   Make him wash your clothes/drink just prune juice/smell your farts until he's sober
            #   Make him wash your clothes until he's sober.
            #   Make him drink just prune juice until he's sober.
            #   Make him smell your farts until he's sober.
        #   Make him polish silver/Make him wipe your boogers/Make him clean the toilets until he's standing/until he vomits/and do the laundry
            #   Make him polish silver until he's sober.
            #   Make him wipe your boogers until he's sober.
            #   Make him clean the toilets until he's sober.
            #   Make him clean the toilets until he's standing.
            #   Make him clean the toilets until he vomits.
            #   Make him clean the toilets and do the laundry.
        #   Make him leave a message/cook your breakfast once he is sober/scrub the pots until he's sober
            #   Make him leave a message until he's sober.
            #   Make him cook your breakfast once he is sober.
            #   Make him scrub the pots until he's sober.
    #   Blow the Man Down
        #   Come all you young/old/fat fellows/chickens/farters who follow the sea/news/game
            #   Come all you young fellows who follow the sea.
            #   Come all you old fellows who follow the sea.
            #   Come all you fat fellows who follow the sea.
            #   Come all you young farters who follow the sea.
            #   Come all you young chickens who follow the news.
            #   Come all you young fellows who follow the game.
        #   To me/you/them way, hey, blow/slap/chase the man down
            #   To me, way, hey, blow the man down.
            #   To you, way, hey, blow the man down.
            #   To them way, hey, blow the man down.
            #   Slap the man down.
            #   Chase the man down.
        #   And pray pay attention/pay your taxes/have a biscuit and listen to me
            #   And pray pay attention and listen to me.
            #   And pray pay your taxes and listen to me.
            #   And pray have a biscuit and listen to me.
        #   Gimme some time to blow the man down/finish this round/take the mail down
            #   Give me some time to blow the man down.
            #   Give me some time to finish this round.
            #   Give me some time to take the mail down.
        #   I'm a deep water/business class/lazy old sailor/pickle/fart just in from Hong Kong/the Bronx/L.A.
            #   I'm a deep water sailor just in from Hong Kong.
            #   I'm a business class sailor just in from Hong Kong.
            #   I'm a lazy old sailor just in from Hong Kong.
            #   I'm a deep water sailor just in from the Bronx.
            #   I'm a deep water silor just in from L.A.
            #   I'm a deep water pickle just in from Hong Kong.
            #   I'm a deep water fart just in from Hong Kong.
        #   If you buy me a drink/cow/toilet, then I'll sing you a song
            #   If you buy me a drink, then I'll sing you a song.
            #   If you buy me a cow, then I'll sing you a song.
            #   If you buy me a toilet, then I'll sing you a song.
    #   Yo Ho (A Pirate's Life for Me)
        #   Yo ho, yo ho, a pirate's/teacher's/lawyer's life for me/her/them
            #   Yo ho, yo ho, a pirate's life for me.
            #   Yo ho, yo ho, a teacher's life for me.
            #   Yo ho, yo ho, a lawyer's life for me.
            #   Yo ho, yo ho, a pirate's life for her.
            #   Yo ho, yo ho, a pirate's life for them.
        #   We pillage/sweep/bake, we plunder/fart/faint, we rifle/vomit/read books and loot/hoot/toot
            #   We pillage, we plunder, we rifle and loot.
            #   We sweep.
            #   We bake.
            #   We plunder.
            #   We fart.
            #   We faint.
            #   We rifle and loot.
            #   We vomit and loot.
            #   We read books and loot.
            #   We rifle and hoot.
            #   We rifle and toot.
        #   Drink up/Eat up/Shop more, me hearties/me homies/me peeps, yo ho/and go/oh no
            #   Drink up, me hearties, yo ho.
            #   Eat up, me hearties, yo ho.
            #   Shop more, me hearties, yo ho.
            #   Drink up, me homies, yo ho.
            #   Drink up, me peeps, yo ho.
            #   Drink up, me hearties, and go.
            #   Drink up, me hearties, oh no.
        #   We kidnap/play games/buy stuff and ravage and don't give a hoot/crap/boot
            #   We kidnap and ravage and don't give a hoot.
            #   We play games and ravage and don't give a hoot.
            #   We buy stuff and ravage and don't give a hoot.
            #   We kidnap and ravage and don't give a crap.
            #   We kidnap and ravage and don't give a boot.
    #   Leaving on a Jet Plane
        #   All my bags/drugs/snacks are packed
            #   All my bags are packed.
            #   All my drugs are packed.
            #   All my snacks are packed.
        #   I'm ready to go/stay/fight
            #   I'm ready to go.
            #   I'm ready to stay.
            #   I'm ready to fight.
        #   I'm standing here outside your door/store/car
            #   I'm standing here outside your door.
            #   I'm standing here outside your store.
            #   I'm standing here outside your car.
        #   I hate/love/want to wake you up to say goodbye/hello/I farted
            #   I hate to wake you up to say goodbye.
            #   I love to wake you up to say goodbye.
            #   I want to wake you up to say goodbye.
            #   I hate to wake you up to say hello.
            #   I hate to wake you up to say I farted.
        #   But the dawn is breaking/leaving/dancing
            #   But the dawn is breaking.
            #   But the dawn is leaving.
            #   But the dawn is dancing.
        #   It's early morn/early warm/gonna storm
            #   It's early morn.
            #   It's early warm.
            #   It's gonna storm.
        #   The taxi's waiting/leaving/burning
            #   The taxi's waiting.
            #   The taxi's leaving.
            #   The taxi's burning.
        #   He's blowing his horn
            #   He's blowing his horn.
        #   Already, I'm so lonesome/sleepy/angry I could die/fly/sue
            #   Already, I'm so lonesome I could die.
            #   Already, I'm so sleepy I could die.
            #   Already, I'm so angry I could die.
            #   Already, I'm so lonesome I could fly.
            #   Already, I'm so lonesome I could sue.
        #   So kiss me and smile for me
            #   So kiss me and smile for me.
        #   Tell me that you'll wait for me
            #   Tell me that you'll wait for me.
        #   Hold me like you'll never let me go/belch/fart
            #   Hold me like you'll never let me go.
            #   Hold me like you'll never let me belch.
            #   Hold me like you'll never let me fart.
        #   'Cause I'm leaving on a jet plane
            #   'Cause I'm leaving on a jet plane.
        #   Don't know when I'll be back again
            #   Don't know when I'll be back again.
        #   Oh, babe, I hate to go
            #   Oh, babe, I hate to go.
    #   Home on the Range
        #   Oh, give/sell/rent me/her/them a home/job/zone where the buffalo/carrot cakes/Stanley cups roam/sing/jump
            #   Oh, give me a home where the buffalo roam.
            #   Oh, sell me a home where the buffalo roam.
            #   Oh, rent me a home where the buffalo roam.
            #   Oh, give me a job where the buffalo roam.
            #   Oh, give me a zone where the buffalo roam.
            #   Oh, give me a home where the carrot cakes roam.
            #   Oh, give me a home where the Stanley cups roam.
            #   Oh, give me a home where the buffalo sing.
            #   Oh, give mea  home where the buffalo jump.
        #   Where the deer/skunk/mouse and the antelope/ant sometimes/bear sometimes play
            #   Oh, give me a home where the deer and the antelope play.
            #   Oh, give me a home where the skunk and the antelope play.
            #   Oh, give me a home where the mouse and teh antelope play.
            #   Oh, give me a home where the deer and the ant sometimes play.
            #   Oh, give me a home where the deer and teh bear sometimes play.
        #   Where seldom/sometimes/daily is heard a discouraging word/an encouraging word/a ridiculous word
            #   Oh, give me a home where seldom is heard a discouraging word.
            #   Oh, give me a home where sometimes is heard a discouraging word.
            #   Oh, give me a home where daily is heard a discouraging word.
            #   Oh, give me a home where seldom is heard an encouraging word.
            #   Oh, give me a home where seldom is heard a ridiculous word.
        #   And the skies/beers/eyes are not cloudy all day
            #   And the skies are not cloudy all day.
            #   And the beers are not cloudy all day.
            #   And the eyes are not cloudy all day.
        #   Home, home on the range
            # Home, home on the range where the deer and the antelope play.
        #   And the skies are not cloudy/stormy/rainy all day
            #   And the skies are not cloudy all day.
            #   And the skies are not stormy all day.
            #   And the skies aer not rainy all day.
    #   Scarborough Fair
        #   Are/Why/Were you going/dancing/flying to Scarborough Fair/the grocery store/the comic book store
            #   Are you going to Scarborough Fair?
            #   Why are you going to Scarborough Fair?
            #   Were you going to Scarborough Fair?
            #   Are you flying to Scarborough Fair?
            #   Are you dancing to Scarborough Fair?
            #   Are you going to the grocery store?
            #   Are you going to the comic book store? 
        #   Parsley/Basil/Chicken, sage/cheese/salt, rosemary/a Snickers/mojitos, and thyme/crime/milk
            #   Parsley, sage, rosemary, and thyme.
            #   Basil, sage, rosemary, and thyme.
            #   Chicken, sage, rosemary, and thyme.
            #   Parsley, sage, rosemary, and thyme.
            #   Parsley, cheese, a Snickers, and crime.
            #   Basil, salt, mojitos, and crime.
            #   Parsley, sage, rosemary, and milk.
        #   Remember me/him/her/forget me/him/her/trash talk me/him/her to one who lives there/here/near
            #   Remember me to one who lives there.
            #   Remember him to one who lives there.
            #   Remember her to one who lives there.
            #   Forget me to one who lives there.
            #   Trash talk me to one who lives there.
            #   Remember me to one who lives there.
            #   Remember me to one who lives here.
            #   Remember me to one who lives near.
        #   For she once was a true love/a llama/a hater of mine
            #   For she once was a true love of mine.
            #   For she once was a hater of mine.
            #   For she once was a llama of mine.
    #   Cockles and Mussels
        #   In Dublin's fair city/Mexico City/Houston's fair city
            #   In Dublin's fair city, where the girls are so pretty.
            #   In Mexico city, where the girls are so pretty.
            #   In Houston's fair city, where the girls are so pretty.
        #   I once met a girl named sweet/weird/old Molly Malone
            #   I once met a girl named Sweet Molly Malone.
            #   I once met a girl named Weird Molly Malone.
            #   I once met a girl named Old Molly Malone.
        #   As she pushed/sued/shook her/his/my wheelbarrow/old knapsack/Camaro
            #   As she pushed her wheelbarrow.
            #   As she sued her wheelbarrow.
            #   As she shook her wheelbarrow.
            #   As she pushed her old knapsack.
            #   As she pushed her Camaro.
        #   Through streets/cars/stores broad/closed/old and narrow/nasty/slippery
            #   As she pushed her wheelbarrow through streets broad and narrow.
            #   As she pushed her wheelbarrow through streets broad and nasty.
            #   As she pushed her wheelbarrow through streets broad and slippery.
            #   As she pushed her wheelbarrow through cars broad and narrow.
            #   As she pushed her wheelbarrow through stores broad and narrow.
            #   As she pushed her wheelbarrow through streets closed and slippery.
            #   As she pushed her wheelbarrow through streets old and nasty.
        #   Crying, "Cockles/Cookies/Pencils and mussels/taters/French fries, alive, alive, oh!"/I've got the best, oh!"/Just pay what you owe!"
            #   Crying, "Cockles and mussels, alive, alive, oh!"
            #   Crying, "Cookies and taters, I've got the best, oh!"
            #   Crying, "Pencils and French fries, just pay what you owe!"  
    #   The Water Is Wide
        #   Oh, the water is wide/cold/fine
            #   Oh, the water is wide.
            #   Oh, the water is cold.
            #   Oh, the water is fine.
        #   I can't swim o'er/buy more/want more
            #   I can't swim o'er.
            #   I can't buy more.
            #   I can't want more.
        #   And neither have I wings/a ticket/birds to fly
            #   And neither have I wings to fly.
            #   And neither have I a ticket to fly.
            #   And neither have I some birds to fly.
        #   Give/Buy/Sell me/her/him a boat/mouse/car that will carry two/three/four/ferry two/three/four/can't carry two/three/four
            #   Give me a boat that will carry two.
            #   Buy her a mouse that will ferry three.
            #   Sell him a car that will carry four.
            #   Give me a mouse that will carry two.
            #   Give me a car that can't carry two.
        #   A boat shall row/tow/leave my love/bro/cat and I/You/Her
            #   A boat shall row my love and I.
            #   A boat shall tow my bro and you.
            #   A boat shall leave my cat and her.
            