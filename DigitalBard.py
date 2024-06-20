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
                #   Blow the Man Down
                while True:
                    #   Blow the Man Down
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
                #   Yo Ho (A Pirate's Life for Me)
                while True:
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                    #   Yo Ho (A Pirate's Life for Me)
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Leaving on a Jet Plane
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
                #   Home on the Range
                while True:
                    #   Choice One
                print("Choice One")
                print("1    Give")
                print("2    Sell")
                print("3    Rent")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Two
                print("Choice Two")
                print("1    Me")
                print("2    Her")
                print("3    Them")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Three
                print("Choice Three")
                print("1    Home")
                print("2    Job")
                print("3    Zone")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Four
                print("Choice Four")
                print("1    Buffalo")
                print("2    Carrot")
                print("3    Stanley")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Five
                print("Choice Five")
                print("1    Roam")
                print("2    Sing")
                print("3    Jump")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Six
                print("Choice Six")
                print("1    Deer")
                print("2    Skunk")
                print("3    Mouse")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Seven
                print("Choice Seven")
                print("1    Antelope")
                print("2    Ant")
                print("3    Bear")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Eight
                print("Choice Eight")
                print("1    Seldom")
                print("2    Sometimes")
                print("3    Daily")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Nine
                print("Choice Nine")
                print("1    Discourage")
                print("2    Encourage")
                print("3    Ridiculous")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Ten
                print("Choice Ten")
                print("1    Sky")
                print("2    Beer")
                print("3    Eye")
                break
            while True:
                #   Home on the Range
                while True:
                    #   Choice Eleven
                print("Choice Eleven")
                print("1    Cloud")
                print("2    Storm")
                print("3    Rain")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice One
                print("Choice One")
                print("1    Are")
                print("2    Were")
                print("3    Why")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Two
                print("Choice Two")
                print("1    Go")
                print("2    Dance")
                print("3    Fly")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Three
                print("Choice Three")
                print("1    Scarborough")
                print("2    Grocery")
                print("3    Comic")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Four
                print("Choice Four")
                print("1    Parsley")
                print("2    Basil")
                print("3    Chicken")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Five
                print("Choice Five")
                print("1    Sage")
                print("2    Cheese")
                print("3    Salt")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Six
                print("Choice Six")
                print("1    Rosemary")
                print("2    Snickers")
                print("3    Mojitos")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Seven
                print("Choice Seven")
                print("1    Thyme")
                print("2    Crime")
                print("3    Milk")
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Eight
                print("Choice Eight")
                print("1    Me")
                print("2    Him")
                print("3    Her")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Nine
                print("Choice Nine")
                print("1    There")
                print("2    Here")
                print("3    Near")
                break
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Ten
                print("Choice Ten")
            while True:
                #   Scarborough Fair
                while True:
                    #   Choice Eleven
                print("Choice Eleven")
            while True:
                #   Molly Malone
                while True:
                    #   Choice One
                print("Choice One")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Two
                print("Choice Two")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Three
                print("Choice Three")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Four
                print("Choice Four")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Five
                print("Choice Five")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Six
                print("Choice Six")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Seven
                print("Choice Seven")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Eight
                print("Choice Eight")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Nine
                print("Choice Nine")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Ten
                print("Choice Ten")
            while True:
                #   Molly Malone
                while True:
                    #   Choice Eleven
                print("Choice Eleven")
            while True:
                #   The Water is Wide
                while True:
                    #   Choice One
                print("Choice One")
            while True:
                #   The Water is Wide
                while True:
                    #   Choice Two
                print("Choice Two")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Three
                print("Choice Three")
            while True:
                #   The Water is Wide
                while True:
                    #   Choice Four
                print("Choice Four")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Five
                print("Choice Five")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Six
                print("Choice Six")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Seven
                print("Choice Seven")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Eight
                print("Choice Eight")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Nine
                print("Choice Nine")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Ten
                print("Choice Ten")
            while True:
                #   The Water is Wide
                while True:        
                    #   Choice Eleven
                print("Choice Eleven")
        elif choice == "3":
            print("You have selected option three, total chaos.")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:
                    #   Choice One
                print("Choice One")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Two
                print("Choice Two")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Three
                print("Choice Three")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Four
                print("Choice Four")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Five
                print("Choice Five")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Six
                print("Choice Six")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Seven
                print("Choice Seven")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Eight
                print("Choice Eight")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Nine
                print("Choice Nine")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Ten
                print("Choice Ten")
            while True:
                #   Leave Her, Johnny
                #   Wellerman
                #   Drunken Sailor
                #   Blow the Man Down
                #   Yo Ho (A Pirate's Life for Me)
                #   Leaving on a Jet Plane
                #   Home on the Range
                #   Scarborough Fair
                #   Molly Malone
                #   The Water is Wide
                while True:        
                    #   Choice Eleven
                print("Choice Eleven")
        else:
            print("Please select from the provided options.")
            continue

            
