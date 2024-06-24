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
                            track1("I thought I heard") 
                            break
                        if choice == "2":
                            print("You have selected option two, They.")
                            track1("They thought they heard")
                            break
                        if choice == "3":
                            print("You have selected option three, We.")
                            track1("We thought we heard")
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
                            track2("the Old")
                            break
                        elif choice == "2":
                            print("You have selected option two, Tall.")
                            track2("the Tall")
                            break
                        elif choice == "3":
                            print("You have selected option three, Sad.")
                            track2("the Sad")
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
                            track3("Man say")
                            break
                        elif choice == "2":
                            print("You have selected option two, Yell.")
                            track3("Man yell")
                            break
                        elif choice == "3":
                            print("You have selected option three, Wish.")
                            track3("Man wish")
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
                            track4("Leave her,")
                            track6("leave her")
                            track9("And it's time for us to leave her.")
                            track12("Leave her,")
                            track14("leave her")
                            track16("And it's time for us to leave her")
                            track17("Leave her,")
                            track19("leave her")
                            track20("Oh, leave her,")
                            track22("leave her")
                            track24("And it's time for us to leave her")
                            break
                        elif choice == "2":
                            print("You have selected option two, Watch.")
                            track4("Watch her,")
                            track6("watch her")
                            track9("And it's time for us to watch her")
                            track12("Watch her,")
                            track14("leave her")
                            track16("And it's time for us to watch her")
                            track17("Watch her,")
                            track19("watch her")
                            track20("Oh, watch her,")
                            track22("watch her")
                            track24("And it's time for us to watch her")
                            break
                        elif choice == "3":
                            print("You have selected option three, Trust.")
                            track4("Trust her,")
                            track6("trust her")
                            track9("And it's time for us to trust her")      
                            track12("Trust her,")     
                            track14("trust her")        
                            track16("And it's time for us to trust her")  
                            track17("Trust her,")
                            track19("trust her")
                            track20("Oh, trust her,")
                            track22("trust her")
                            track24("And it's time for us to trust her")
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
                            track5("Johnny,")
                            track13("Johnny,")
                            track18("Johnny,")
                            track21("Johnny,")
                            break
                        elif choice == "2":
                            print("You have selected option two, Timmy.")
                            track5("Timmy,")
                            track13("Timmy,")
                            track18("Timmy,")
                            track21("Timmy,")
                            break
                        elif choice == "3":
                            print("You have selected option three, Frodo.")
                            track5("Frodo,")
                            track13("Frodo,")
                            track18("Frodo,")
                            track21("Frodo,")
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
                            track7("Tomorrow, ye will")
                            break
                        elif choice == "2":
                            print("You have selected option two, Tuesday.")
                            track7("Next Tuesday, ye will")
                            break
                        elif choice == "3":
                            print("You have selected option three, Friday.")
                            track7("On Friday, ye will")
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
                            track8("get your pay")
                            break
                        elif choice == "2":
                            print("You have selected option two, Bell.")
                            track8("get your bell")
                            break
                        elif choice == "3":
                            print("You have selected option three, Fish.")
                            track8("get your fish")
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
                            track23("For the voyage is long, and the winds don't blow")
                            break
                        elif choice == "2":
                            print("You have selected option two, Short.")
                            track23("For the voyage is short, and the winds don't blow")
                            break
                        elif choice == "3":
                            print("You have selected option three, Wild.")
                            track23("For the voyage is wild, and the winds don't blow")
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
                            track10("Oh, the wind")
                            break   
                        elif choice == "2":
                            print("You have selected option two, Food.")
                            track10("Oh, the food")
                            break
                        elif choice == "3":
                            print("You have selected option three, Smell.")
                            track10("Oh, the smell")
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
                            track11("was foul, and the sea ran high")
                            break
                        elif choice == "2":
                            print("You have selected option two, Cold.")
                            track11("was cold, and the sea ran high")
                            break
                        elif choice == "3":
                            print("You have selected option three, Weird.")
                            track11("was weird, and the sea ran high")
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
                            track15("She shipped it green, and none went by")
                            break
                        elif choice == "2":
                            print("You have selected option two, All.")
                            track15("She shipped it green, and all went by")
                            break
                        elif choice == "3":
                            print("You have selected option three, Some.")
                            track15("She shipped it green, and some went by")
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
                            track1("There once was a ship that put to sea")
                            break
                        if choice == "5":
                            print("You have selected option five, Twice.")
                            track1("There twice was a ship that put to sea")
                            break
                        if choice == "6":
                            print("You have selected option six, Thrice.")
                            track1("There thrice was a ship that put to sea")
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
                            track2("The name of the ship was the Billy of Tea")
                            break
                        if choice == "2":
                            print("You have selected option two, Enterprise.")
                            track2("The name of the ship was the Enterprise D")
                            break
                        if choice == "3":
                            print("You have selected option three, Carpenter.")
                            track2("The name of the ship was the Carpenter Bee")
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
                            track3("The winds blew up, her bow dipped down")
                            break
                        if choice == "2":
                            print("You have selected option two, Down.")
                            track3("The winds blew down, her bow dipped down")
                            break
                        if choice == "3":
                            print("You have selected option three, In.")  
                            track3("The winds blew in,  her bow dipped down")
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
                            track4("Oh, blow, my bully boys, blow")
                            break
                        if choice == "2":
                            print("You have selected option two, Sing.")
                            track4("Oh, sing, my bully boys, sing")
                            break
                        if choice == "3":
                            print("You have selected option three, Dance.")
                            track4("Oh, dance, my bully boys, dance")
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
                            track5("Soon may")
                            break
                        if choice == "2":
                            print("You have selected option two, When.")
                            track5("When may")
                            break
                        if choice == "3":
                            print("You have selected option three, Why.")
                            track5("Why may")
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
                            track6("the Wellerman")
                            break
                        if choice == "2":
                            print("You have selected option two, Butterfly.")
                            track6("the Butterfly")
                            break
                        if choice == "3":
                            print("You have seelcted option three, Limousine.")
                            track6("the Limousine")
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
                            track7("come")
                            break
                        if choice == "2":
                            print("You have selected option two, Go.")
                            track7("go")
                            break
                        if choice == "3":
                            print("You have selected option three, Leave.")
                            track7("leave")
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
                            track8("To bring us sugar")
                            break
                        if choice == "2":
                            print("You have selected option two, Twizzlers.")
                            track8("To bring us Twizzlers")
                            break
                        if choice == "3":
                            print("You have selected option three, Pizza.")
                            track8("To bring us pizza")
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
                            track9("and tea")
                            break
                        if choice == "2":
                            print("You have selected option two, T-shirts.")
                            track9("and T-shirts")
                            break
                        if choice == "3":
                            print("You have selected option three, Shoes.")
                            track9("and shoes")
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
                            track10("and rum")
                            break
                        if choice == "2":
                            print("You have selected option two, Coke.")
                            track10("and Coke")
                            break
                        if choice == "3":
                            print("You have selected option three, Prune Juice.")
                            track10("and prune juice")
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
                            track11("One day, when the tonguing is done, we'll take our leave and go")
                            break
                        if choice == "2":
                            print("You have selected option two, Sing.")
                            track11("One day, when the singing is done, we'll take our leave and go")
                            break
                        if choice == "3":
                            print("You have selected option three, Mop.")
                            track11("One day, when the mopping is done, we'll take our leave and go")
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
                            track1("What do you do with a drunken")
                            track3("What do you do with a drunken")
                            track5("What do you do with a drunken")
                            break
                        if choice == "8":
                            print("You have selected option eight, Farting.")
                            track1("What do you do with a farting")
                            track3("What do you do with a farting")
                            track5("What do you do with a farting")
                            break
                        if choice == "9":
                            print("You have selected option nine, Stupid.")
                            track1("What do you do with a stupid")
                            track3("What do you do with a stupid")
                            track5("What do you do with a stupid")
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
                            track2("sailor")
                            track4("sailor")
                            track6("sailor")
                            break
                        if choice == "2":
                            print("You have selected option two, Bouncer.")
                            track2("bouncer")
                            track4("bouncer")
                            track6("bouncer")
                            break
                        if choice == "3":
                            print("You have selected option three, Painter.")
                            track2("painter")
                            track4("painter")
                            track6("painter")
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
                            track7("Early")
                            track12("Early")
                            track17("Early")
                            track22("Early")
                            break
                        if choice == "2":
                            print("You have selected option two, Lately.")
                            track7("Lately")
                            track12("Lately")
                            track17("Lately")
                            track22("Lately")
                            break
                        if choice == "3":
                            print("You have selected option three, Never.")
                            track7("Never")
                            track12("Never")
                            track17("Never")
                            track22("Never")
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
                            track8("in the morning")
                            track13("in the morning")
                            track18("in the morning")
                            track23("in the morning")
                            break
                        if choice == "2":
                            print("You have selected option two, Party.")
                            track8("at the party")
                            track13("at the party")
                            track18("at the party")
                            track23("at the party")
                            break
                        if choice == "3":
                            print("You have selected option three, Evening.")
                            track8("in the evening")
                            track13("in the evening")
                            track18("in the evening")
                            track23("in the evening")
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
                            track9("Throw him in the brig until he's sober")
                            break
                        if choice == "2":
                            print("You have selected option two, Toilets.")
                            track9("Make him clean the toilets until he's sober")
                            break
                        if choice == "3":
                            print("You have selected option three, Farts.")
                            track9("Make him smell your farts until he's sober")
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
                            track19("Way, hey, and up she rises")
                            track20("Way, hey, and up she rises")
                            track21("Way, hey, and up she rises")
                            break
                        if choice == "2":
                            print("You have selected option two, Wiggles.")
                            track19("Way, hey, and up she wiggles")
                            track20("Way, hey, and up she wiggles")
                            track21("Way, hey, and up she wiggles")
                            break
                        if choice == "3":
                            print("You have selected option three, Bubbles.")
                            track19("Way, hey, and up she bubbles")
                            track20("Way, hey, and up she bubbles")
                            track21("Way, hey, and up she bubbles")
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
                            track10("Make him wear a clown suit until he's sober")
                            break
                        if choice == "2":
                            print("You have selected option two, Dunce.")
                            track10("Make him wear a dunce cap until he's sober")
                            break
                        if choice == "3":
                            print("You have selected option three, Crackers.")
                            track10("Make him just eat crackers until he's sober")
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
                            track11("Make him wash your clothes once he is sober")
                            break
                        if choice == "2":
                            print("You have selected option two, Drink.")
                            track11("Make him drink just prune juice until he's sober")
                            break
                        if choice == "3":
                            print("You have selected option three, Smell.")
                            track11("Make him smell your armpits until he's sober")
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
                            track14("Make him polish silver")
                            break
                        if choice == "2":
                            print("You have selected option two, Wipe.")
                            track14("Make him wipe your boogers")
                            break
                        if choice == "3":
                            print("You have selected option three, Clean.")
                            track14("Make him clean your boots")
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
                            track15("while he is standing")
                            break
                        if choice == "2":
                            print("You have selected option two, Vomit.")
                            track15("until he vomits")
                            break
                        if choice == "3":
                            print("You have selected option three, Laundry.")
                            track15("and do the laundry")
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
                            track16("Make him leave the party until he's sober")
                            break
                        if choice == "2":
                            print("You have selected option two, Breakfast.")
                            track16("Make him fix your breakfast once he is sober")
                            break
                        if choice == "3":
                            print("You have selected option three, Pots.")
                            track16("Make him scour the pots until he's sober")
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
                                track1("Come all you young")
                                break
                            if choice == "11":
                                print("You have selected option eleven, Old.")
                                track1("Come all you old")
                                break
                            if choice == "12":
                                print("You have selected option twelve, Fat.")
                                track1("Come all you fat")
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
                                track2("fellows")
                                break
                            if choice == "2":
                                print("You have selected option two, Chickens.")
                                track2("chickens")
                                break
                            if choice == "3":
                                print("You have selected option three, Farters.")
                                track2("farters")
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
                                track3("who follow the sea")
                                break
                            if choice == "2":
                                print("You have selected option two, News.")
                                track3("who follow the news")
                                break
                            if choice == "3":
                                print("You have selected option three, Game.")
                                track3("who follow the game")
                                break
                        print("Choice Four")
                        print("1    Me")
                        print("2    You")
                        print("3    Them")
                        break
                    while True:
                        #   Choice Four
                        while True:
                            if choice == "1":
                                print("You have selected option one, Me.")
                                track4("To me, way, hey,")
                                track11("To me, way, hey,")
                                break
                            if choice == "2":
                                print("You have selected option two, You.")
                                track4("To you, way, hey,")
                                track11("To you, way, hey,")
                                break
                            if choice == "3":
                                print("You have selected option three, Them.")
                                track4("To them, way, hey,")
                                track11("To them, way, hey,")
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
                                track5("blow the man down")
                                track12("blow the man down")
                                break
                            if choice == "2":
                                print("You have selected option two, Slap.")
                                track5("slap the man down")
                                track12("slap the man down")
                                break
                            if choice == "3":
                                print("You have selected option three, Chase.")
                                track5("chase the man down")
                                track12("chase the man down")
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
                                track6("And pray pay attention and listen to me")
                                break
                            if choice == "2":
                                print("You have selected option two, Taxes.")
                                track6("And pray pay your taxes and listen to me")
                                break
                            if choice == "3":
                                print("You have selected option three, Biscuit.")
                                track6("And pray eat a biscuit and listen to me")
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
                                track7("Give me some time to blow the man down")
                                track14("Give me some time to blow the man down")
                                break
                            if choice == "2":
                                print("You have selected option two, Finish.")
                                track7("Give me some time to finish this round")
                                track14("Give me some time to finish this round")
                                break
                            if choice == "3":
                                print("You have selected option three, Take.")
                                track7("Give me some time to take the mail down")
                                track14("Give me some time to take the mail down")
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
                                track8("I'm a deep water")
                                break
                            if choice == "2":
                                print("You have selected option two, Business.")
                                track8("I'm a business class")
                                break
                            if choice == "3":
                                print("You have selected option three, Lazy.")
                                track8("I'm a lazy old")
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
                                track9("sailor")
                                break
                            if choice == "2":
                                print("You have selected option two, Pickle.")
                                track9("pickle")
                                break
                            if choice == "3":
                                print("You have selected option three, Fart.")
                                track9("fart")
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
                                track10("just in from Hong Kong")
                                break
                            if choice == "2":
                                print("You have selected option two, The Bronx.")
                                track10("just in from the Bronx")
                                break
                            if choice == "3":
                                print("You have selected option three, L.A.")
                                track10("just in from L.A.")
                                break
                        print("Choice Eleven")
                        print("1    Drink")
                        print("2    Cow")
                        print("3    Boot")
                        break
                    while True:
                        while True:
                            if choice == "1":
                                print("You have selected option one, Drink.")
                                track13("If you buy me a drink, then I'll sing you a song")
                                break
                            if choice == "2":
                                print("You have selected option two, Cow.")
                                track13("If you buy me a cow, then I'll sing you a song")
                                break
                            if choice == "3":         
                                print("You have selected option three, Boot.")
                                track13("If you buy me a boot, then I'll sing you a song")
                                break
                    break
                break
            while True:
                while True:
                    while True:
                        #   Choice One
                        if choice == "13":
                            print("You have selected option thirteen, Pirate.")
                            track1("Yo ho, yo ho, a pirate's life")
                            track15("Yo ho, yo ho, a pirate's life")
                            break
                        if choice == "14":
                            print("You have selected option fourteen, Teacher.")
                            track1("Yo ho, yo ho, a teacher's life")
                            track15("Yo ho, yo ho, a teacher's life")
                            break
                        if choice == "15":
                            print("You have selected option fifteen, Lawyer.")
                            track1("Yo ho, yo ho, a lawyer's life")
                            track15("Yo ho, yo ho, a lawyer's life")
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
                            track2("for me")
                            track16("for me")
                            break
                        if choice == "2":
                            print("You have selected option two, Her.")
                            track2("for her")
                            track16("for me")
                            break
                        if choice == "3":
                            print("You have selected option three, Them.")
                            track2("for them")
                            track16("for them")
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
                            track3("We pillage,")
                            break
                        if choice == "2":
                            print("You have selected option two, Sweep.")
                            track3("We sweep up,")
                            break
                        if choice == "3":
                            print("You have selected option three, Bake.")
                            track3("We bake things,")
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
                            track4("we plunder,")
                            break
                        if choice == "2":
                            print("You have selected option two, Fart.")
                            track4("we fart,")
                            break
                        if choice == "3":
                            print("You have selected option three, Faint.")
                            track4("we faint,")
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
                            track5("we rifle")
                            break
                        if choice == "2":
                            print("You have selected option two, Vomit.")
                            track5("we vomit")
                            break
                        if choice == "3":
                            print("You have selected option three, Books.")
                            track5("we read books")
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
                            track6("and loot")
                            break
                        if choice == "2":
                            print("You have selected option two, Hoot.")
                            track6("and hoot")
                            break
                        if choice == "3":
                            print("You have selected option three, Toot.")
                            track6("and toot")
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
                            track7("Drink up,")
                            track12("Drink up,")
                            break
                        if choice == "2":
                            print("You have selected option two, Eat.")
                            track7("Eat up,")
                            track12("Eat up,")
                            break
                        if choice == "3":
                            print("You have selected option three, Shop.")
                            track7("Shop more,")
                            track12("Eat up,")
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
                            track8("me hearties,")
                            track13("me hearties,")
                            break
                        if choice == "2":
                            print("You have selected option two, Homies.")
                            track8("me homies,")
                            track13("me homies,")
                            break
                        if choice == "3":
                            print("You have selected option three, Peeps.")
                            track8("me peeps,")
                            track13("me homies,")
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
                            track9("yo ho")
                            track14("yo ho")
                            break
                        if choice == "2":
                            print("You have selected option two, Go.")
                            track9("and go")
                            track14("and go")
                            break
                        if choice == "3":
                            print("You have selected option three, No.")
                            track9("oh no")
                            track14("oh no")
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
                            track10("We kidnap and ravage")
                            break
                        if choice == "2":
                            print("You have selected option two, Play.")
                            track10("We play games and ravage")
                            break
                        if choice == "3":
                            print("You have selected option three, Buy.")
                            tarck10("We buy stuff and ravage")
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
                            track11("and don't give a hoot")
                            break
                        if choice == "2":
                            print("You have selected option two, Crap.")
                            track11("and don't give a crap")
                            break
                        if choice == "3":
                            print("You have selecte doption three, Boot.")
                            track11("and don't give a boot")
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
                        track1("All my bags are packed")
                        break
                    if choice == "2":
                        print("You have selecte doption two, Drugs.")
                        track1("All my drugs are packed")
                        break
                    if choice == "3":
                        print("You have selected option three, Snacks.")
                        track1("All my snacks are packed")
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
                        track2("I'm ready to go")
                        break
                    if choice == "2":
                        print("You have selected option two, Stay.")
                        track2("I'm ready to stay")
                        break
                    if choice == "3":
                        print("You have selected option three, Fight.")
                        track2("I'm ready to fight")
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
                        track3("I'm standing here outside your door")
                        break
                    if choice == "2":
                        print("You have selected option two, Store.")
                        track3("I'm standing here outside your store")
                        break
                    if choice == "3":
                        print("You have selected option three, Car.")
                        track3("I'm standign here outside your car")
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
                        track4("I hate to wake you up")
                        break
                    if choice == "2":
                        print("You have selected option two, Love.")
                        track4("I love to wake you up")
                        break
                    if choice == "3":
                        print("You have selected option three, Want.")
                        track4("I want to wake you up")
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
                        track5("to say goodbye")
                        break
                    if choice == "2":
                        print("You have selected option two, Hello.")
                        track5("to say hello")
                        break
                    if choice == "3":
                        print("You have selected option three, Fart.")
                        track5("to say I farted")
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
                        track6("But the dawn is breaking")
                        break
                    if choice == "2":
                        print("You have selected option two, Leave.")
                        track6("But the dawn is leaving")
                        break
                    if choice == "3":
                        print("You have selected option three, Dance.")
                        track6("But the dawn is dancing")
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
                        track7("It's early morn")
                        break
                    if choice == "2":
                        print("You have selected option two, Warm.")
                        track7("It's really warm")
                        break
                    if choice == "3":
                        print("You have selected option three, Storm.")
                        track7("It's gonna storm")
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
                        track8("The taxi's waiting, he's blowing his horn")
                        break
                    if choice == "2":
                        print("You have selected option two, Leave.")
                        track8("The taxi's leaving, he's blowing his horn")
                        break
                    if choice == "3":
                        print("You have selected option three, Burn.")
                        track8("The taxi's burning, he's blowing his horn")
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
                        track9("Already, I'm so lonesome,")
                        break
                    if choice == "2":
                        print("You have selected option two, Sleepy.")
                        track9("Already, I'm so sleepy,")
                        break
                    if choice == "3":
                        print("You have selected option three, Angry.")
                        track9("Already, I'm so angry,")
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
                        track10("I could die")
                        break
                    if choice == "2":
                        print("You have selected option two, Fly.")
                        track10("I could fly")
                        break
                    if choice == "3":
                        print("You have selected option three, Sue.")
                        track10("I could sue")
                        break
                print("Choice Eleven")
                print("1    Go")
                print("2    Belch")
                print("3    Fart")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Go.")
                        track11("So kiss me and smile for me")
                        track12("Tell me that you'll wait for me")
                        track13("Hold me like you'll never let me go")
                        track14("'Cause I'm leaving on a jet plane")
                        track15("Don't know when I'll be back again")
                        track16("Oh, babe, I hate to go")
                        break
                    if choice == "2":
                        print("You have selected option two, Belch.")
                        track11("So kiss me and smile for me")
                        track12("Tell me that you'll wait for me")
                        track13("Hold me like you'll never let me go")
                        track14("'Cause I'm leaving on a jet plane")
                        track15("Don't know when I'll be back again")
                        track16("Oh, babe I hate to belch")
                        break
                    if choice == "3":
                        print("You have selected option three, Fart.")
                        track11("So kiss me and smile for me")
                        track12("Tell me that you'll wait for me")
                        track13("Hold me like you'll never let me go")
                        track15("'Cause I'm leaving on a jet plane")
                        track15("Don't know when I'll be back again")
                        track16("Oh, babe, I hate to fart")
                        break
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "4":
                        print("You have selected option four, Give.")
                        track1("Oh, give")
                        break
                    if choice == "5":
                        print("You have selected option five, Sell.")
                        track1("Oh, sell")
                        break
                    if choice == "6":
                        print("You have selected option six, Rent.")
                        track1("Oh, rent")
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
                        track2("me")
                        break
                    if choice == "2":
                        print("You have selected option two, Her.")
                        track2("her")
                        break
                    if choice == "3":
                        print("You have selected option three, Them.")
                        track2("them")
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
                        track3("a home")
                        track12("Home, home on the range")
                        break
                    if choice == "2":
                        print("You have selected option two, Job.")
                        track3("a job")
                        track12("Job, job on the range")
                        break
                    if choice == "3":
                        print("You have selected option three, Zone.")
                        track3("a zone")
                        track12("Zone, zone on the range")
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
                        track4("where the buffalo")
                        break
                    if choice == "2":
                        print("You have selected option two, Carrot.")
                        track4("where the carrot cakes")
                        break
                    if choice == "3":
                        print("You have selected option three, Stanley.")
                        track4("where the Stanley cups")
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
                        track5("roam")
                        break
                    if choice == "2":
                        print("You have selected option two, Sing.")
                        track5("sing")
                        break
                    if choice == "3":
                        print("You have selected option three, Jump.")
                        track5("jump")
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
                        track6("Where the deer")
                        track13("Where the deer")
                        break
                    if choice == "2":
                        print("You have selected option two, Skunk.")
                        track6("Where the skunks")
                        track13("Where the skunks")
                        break
                    if choice == "3":
                        print("You have selected option three, Mouse.")
                        track6("Where the mice")
                        track13("Where the mice")
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
                        track7("and the antelope play")
                        track14("and the antelope play")
                        break
                    if choice == "2":
                        print("You have selected option two, Ant.")
                        track7("and the ants sometimes play")
                        track14("and the ants sometimes play")
                        break
                    if choice == "3":
                        print("You have selected option three, Bear.")
                        track7("and the bears sometimes play")
                        track14("and the bears sometimes play")
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
                        track8("Where seldom is heard")
                        track15("Where seldom is heard")
                        break
                    if choice == "2":
                        print("You have selected option two, Sometimes.")
                        track8("Where sometimes is heard")
                        track15("Where sometimes is heard")
                        break
                    if choice == "3":
                        print("You have selected option three, Daily.")
                        track8("Where daily is heard")
                        track15("Where daily is heard")
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
                        track9("a discouraging word")
                        track16("a discouraging word")
                        break
                    if choice == "2":
                        print("You have selected option two, Encourage.")
                        track9("an encouraging word")
                        track16("an encouraging word")
                        break
                    if choice == "3":
                        print("You have selected option three, Ridiculous.")
                        track9("a ridiculous word")
                        track16("a ridiculous word")
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
                        track10("And the skies are not")
                        track17("And the skies are not")
                        break
                    if choice == "2":
                        print("You have selected option two, Beer.")
                        track10("And the beers are not")
                        track17("And the beers are not")
                        break
                    if choice == "3":
                        print("You have selected option three, Eye.")
                        track10("And my eyes are not")
                        track17("And my eyes are not")
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
                        track11("cloudy all day")
                        track18("cloudy all day")
                        break
                    if choice == "8":
                        print("You have selected option two, Storm.")
                        track11("stormy all day")
                        track18("stormy all day")
                        break
                    if choice == "9":
                        print("You have selected option three, Rain.")
                        track11("rainy all day")
                        track18("rainy all day")
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
                        track1("Are you")
                        break
                    if choice == "2":
                        print("You have selected option two, Were.")
                        track1("Were you")
                        break
                    if choice == "3":
                        print("You have selected option three, Why.")
                        track1("Why are you")
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
                        track2("going to")
                        break
                    if choice == "2":
                        print("You have selected option two, Dance.")
                        track2("dancing to")
                        break
                    if choice == "3":
                        print("You have selected option three, Fly.")
                        track2("flying to")
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
                        track3("Scarborough Fair")
                        break
                    if choice == "2":
                        print("You have selected option two, Grocery.")
                        track3("the grocery store")
                        break
                    if choice == "3":
                        print("You have selected option three, Comic.")
                        track3("the comic book store")
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
                        track4("Parsley,")
                        break
                    if choice == "2":
                        print("You have selected option two, Basil.")
                        track4("Basil,")
                        break
                    if choice == "3":
                        print("You have selected option three, Chicken.")
                        track4("Chicken,")
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
                        track5("sage,")
                        break
                    if choice == "2":
                        print("You have selected option two, Cheese.")
                        track5("cheese,")
                        break
                    if choice == "3":
                        print("You have selected option three, Salt.")
                        track5("salt,")
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
                        track6("rosemary,")
                        break
                    if choice == "2":
                        print("You have selected option two, Snickers.")
                        track6("a Snickers,")
                        break
                    if choice == "3":
                        print("You have selected option three, Mojitos.")
                        track6("mojitos,")
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
                        track7("and thyme")
                        break
                    if choice == "2":
                        print("You have selected option two, Crime.")
                        track7("and crime")
                        break
                    if choice == "3":
                        print("You have selected option three, Milk.")
                        track7("and milk")
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
                        track8("Remember")
                        break
                    if choice == "2":
                        print("You have selected option two, Forget.")
                        track8("Forget")
                        break
                    if choice == "3":
                        print("You have selected option three, Trash Talk.")
                        track8("Trash talk")
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
                        track9("me")
                        break
                    if choice == "2":
                        print("You have selected option two, Him.")
                        track9("him")
                        break
                    if choice == "3":
                        print("You have selected option three, Her.")
                        track9("her")
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
                        track10("to one who lives there")
                        break
                    if choice == "2":
                        print("You have selected option two, Here.")
                        track10("to one who lives here")
                        break
                    if choice == "3":
                        print("You have selected option three, Near.")
                        track10("to one who lives near")
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
                        track11("For she once was a true love of mine")
                        break
                    if choice == "2":
                        print("You have selected option two, Llama.")
                        track11("For she once was a llama of mine")
                        break
                    if choice == "3":
                        print("You have selected option three, Hate.")
                        track11("For she once was a hater of mine")
                        break
                break
            while True:
                while True:
                    #   Choice Two
                    if choice == "10":
                        print("You have selected option ten, Dublin.")
                        track1("In Dublin's fair city, where the girls are so pretty")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Mexico.")
                        track1("In Mexico City, where the girls are so pretty")
                        break
                    if choice == "13":
                        print("You have selected option twelve, Houston.")
                        track1("In Houston's fair city, where the girls are so pretty")
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
                        track2("I once met a girl named Sweet Molly Malone")
                        break
                    if choice == "2":
                        print("You have selected option two, Weird.")
                        track2("I once met a girl named Weird Molly Malone")
                        break
                    if choice == "3":
                        print("You have selected option three, Old.")
                        track2("I once met a girl named Old Molly Malone")
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
                        track3("As she pushed")
                        break
                    if choice == "2":
                        print("You have selected option two, Sue.")
                        track3("As she sued")
                        break
                    if choice == "3":
                        print("You have selected option three, Shake.")
                        track3("As she shook")
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
                        track4("her")
                        break
                    if choice == "2":
                        print("You have selected option two, His.")
                        track4("his")
                        break
                    if choice == "3":
                        print("You have selected option three, My.")
                        track5("my")
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
                        track6("wheelbarrow")
                        break
                    if choice == "2":
                        print("You have selected option two, Knapsack.")
                        track6("old knapsack")
                        break
                    if choice == "3":
                        print("You have selected option three, Camaro.")
                        track6("Camaro")
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
                        track7("through streets")
                        break
                    if choice == "2":
                        print("You have selected option two, Car.")
                        track7("through cars")
                        break
                    if choice == "3":
                        print("You have selected option three, Store.")
                        track7("through stores")
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
                        track8("broad")
                        break
                    if choice == "2":
                        print("You have selected option two, Closed.")
                        track8("closed")
                        break
                    if choice == "3":
                        print("You have selected option three, Old.")
                        track8("old")
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
                        track9("and narrow")
                        break
                    if choice == "2":
                        print("You have selected option two, Nasty.")
                        track9("and nasty")
                        break
                    if choice == "3":
                        print("You have selected option three, Slippery.")
                        track9("and slippery")
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
                        track10("Crying, Cockles)
                        track15("Crying, Cockles")
                        break
                    if choice == "2":
                        print("You have selected option two, Cookies.")
                        track10("Crying, Cookies")
                        track15("Crying, Cookies")
                        break
                    if choice == "3":
                        print("You have selected option three, Pencils.")
                        track10("Crying, Pencils")
                        track15("Crying, Pencils")
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
                        track11("and mussels,")
                        track15("and mussels,")
                        break
                    if choice == "2":
                        print("You have selected option two, Taters.")
                        track11("and taters,")
                        track15("and taters,")
                        break
                    if choice == "3":
                        print("You have selected option three, French.")
                        track11("and French fries,")
                        track15("and French fries,")
                        break
                print("Choice Eleven")
                print("1    Alive")
                print("2    Best")
                print("3    Pay")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Alive.")
                        track12("alive, alive, oh")
                        track13("Alive, alive, oh")
                        track14("Alive, alive, oh")
                        track16("Alive, alive, oh")
                        break
                    if choice == "2":
                        print("You have selected option two, Best.")
                        track12("I've got the best, oh")
                        track13("I've got the best, oh")
                        track14("I've got the best, oh")
                        track16("I've got the best, oh")
                        break
                    if choice == "3":
                        print("You have selected option three, Pay.")
                        track12("just pay what you owe")
                        track13("Just pay what you owe")
                        track14("Just pay what you owe")
                        track16("Just pay what you owe")
                        break
                break                    
            while True:
                while True:
                    #   Choice Two
                    if choice == "13":
                        print("You have selected option thirteen, Wide.")
                        track1("Oh, the water is wide")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Cold")
                        track1("Oh, the water is cold")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Fine.")
                        track1("Oh, the water is fine")
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
                        track2("I can't swim o'er")
                        break
                    if choice == "2":
                        print("You have selected option two, Buy.")
                        track2("I can't buy more")
                        break
                    if choice == "3":
                        print("You have selected option three, Want.")
                        track2("I don't want more")
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
                        track3("And neither have I wings to fly")
                        break
                    if choice == "2":
                        print("You have selected option two, Ticket.")
                        track3("And neither have I tickets to fly")
                        break
                    if choice == "3":
                        print("You have selected option three, Bird.")
                        track3("And neither have I birds to fly")
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
                        track4("Build")
                        break
                    if choice == "2":
                        print("You have selected option two, Buy.")
                        track5("Buy")
                        break
                    if choice == "3":
                        print("You have selected option three, Sell.")
                        track5("Sell")
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
                        track6("me a")
                        break
                    if choice == "2":
                        print("You have selected option two, Her.")
                        track6("her a")
                        break
                    if choice == "3":
                        print("You have selected option three, Him.")
                        track6("him a")
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
                        track7("boat")
                        track11("A boat")
                        break
                    if choice == "2":
                        print("You have selected option two, Mouse.")
                        track7("mouse")
                        track11("A mouse")
                        break
                    if choice == "3":
                        print("You have selected option three, Car.")
                        track7("car")
                        track11("A car")
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
                        track8("that will carry")
                        break
                    if choice == "2":
                        print("You have selected option two, Ferry.")
                        track8("that will ferry")
                        break
                    if choice == "3":
                        print("You have selected option three, Can't.")
                        track9("that can't carry")
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
                        track10("two")
                        break
                    if choice == "2":
                        print("You have selected option two, Three.")
                        track10("three")
                        break
                    if choice == "3":
                        print("You have selected option three, Four.")
                        track10(four)
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
                        track12("shall row")
                        break
                    if choice == "2":
                        print("You have selected option two, Tow.")
                        track12("shall tow")
                        break
                    if choice == "3":
                        print("You have selected option three, Leave.")
                        track12("shall leave")
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
                        track13("my love")
                        break
                    if choice == "2":
                        print("You have selected option two, Bro.")
                        track13("my bro")
                        break
                    if choice == "3":
                        print("You have selected option three, Cat.")
                        track13("my cat")
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
                        track14("and I")
                        break
                    if choice == "2":
                        print("You have selected option two, You.")
                        track14("and you")
                        break
                    if choice == "3":
                        print("You have selected option three, Her.")
                        track14("and her")
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
                print("7    Drunken     21  Are")
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
                        track1("I thought I heard the Old Man say, Leave her, Johnny, leave her")
                        break
                    if choice == "2":
                        print("You have selected option two, They.")
                        track1("They thought they heard the Old Man say, Leave her, Johnny, leave her")
                        break
                    if choice == "3":
                        print("You have selected option three, We.")
                        track1("We thought we heard the Old Man say, Leave her, Johnny, leave her")
                        break
                    if choice == "4":
                        print("You have selected option four, Once.")
                        track1("There once was a ship that put to sea")
                        break
                    if choice == "5":
                        print("You have selected option five, Twice.")
                        track1("There twice was a ship that put to sea")
                        break
                    if choice == "6":
                        print("You have selected option six, Thrice.")
                        track1("There thrice was a ship that put to sea")
                        break
                    if choice == "7":
                        print("You have selected option seven, Drunken.")
                        track1("What do you do with a drunken sailor")
                        break
                    if choice == "8":
                        print("You have selected option eight, Farting.")
                        track1("What do you do with a farting sailor")
                        break
                    if choice == "9":
                        print("You have selected option nine, Stupid.")
                        track1("What do you do with a stupid sailor")
                        break
                    if choice == "10":
                        print("You have selected option ten, Young.")
                        track1("Come all you young fellows who follow the sea")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Old.")
                        track1("Come all you old fellows who follow the sea")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Fat.")
                        track1("Come all you fat fellows who follow the sea")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Pirate.")
                        track1("Yo ho, yo ho, a pirate's life for me")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Teacher.")
                        track1("Yo ho, yo ho, a teacher's life for me")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Lawyer.")
                        track1("Yo ho, yo ho, a lawyer's life for me")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Bags.")
                        track1("All my bags are packed")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Drugs.")
                        track1("All my drugs are packed")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Snacks.")
                        track1("All my snacks are packed")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Give.")
                        track1("Oh, give me a home where the buffalo roam")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Sell.")
                        track1("Oh, sell me a home where the buffalo roam")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Rent.")
                        track1("Oh, rent me a home where the buffalo roam")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Are.")
                        track1("Are you going to Scarborough Fair")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Why.")
                        track1("Why are you going to Scarborough Fair")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Were.")
                        track1("Were you going to Scarborough Fair")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Dublin.")
                        track1("In Dublin's fair city")
                        break   
                    if choice == "26":
                        print("You have selected option twenty-six, Mexico.")
                        track1("In Mexico City")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Houston.")
                        track1("In Houston's fair city")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Wide.")
                        track1("Oh, the water is wide")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Cold.")
                        track1("Oh, the water is cold")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Fine.")
                        track1("Oh, the water is fine")
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
                        track2("I thought I heard the Old Man say, Leave her, Johnny, leave her")
                        break
                    if choice == "2":
                        print("You have selected option two, Tall.")
                        track2("I thought I heard the Tall Man say, Leave her, Johnny, leave her")
                        break    
                    if choice == "3":
                        print("You have selected option three, Sad.")
                        track2("I thought I heard the Sad Man say, Leave her Johnny, leave her")
                        break
                    if choice == "4":
                        print("You have selected option four, Billy.")
                        track2("The name of the ship was the Billy of Tea")
                        break
                    if choice == "5":
                        print("You have selected option five, Enterprise.")
                        track2("The name of the ship was the Enterprise D")
                        break
                    if choice == "6":
                        print("You have selected option six, Carpenter.")
                        track2("The name of the ship was the Carpenter Bee")
                        break
                    if choice == "7":
                        print("You have selected option seven, Sailor.")
                        track2("What do you do with a drunken sailor")
                        break
                    if choice == "8":
                        print("You have selected option eight, Bouncer.")
                        track2("What do you do with a drunken bouncer")
                        break
                    if choice == "9":
                        print("You have selected option nine, Painter.")
                        track2("What do you do with a drunken painter")
                        break
                    if choice == "10":
                        print("You have selected option ten, Fellows.")
                        track2("Come all you young fellows who follow the sea")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Chickens.")
                        track2("Come all you young chickens who follow the sea")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Farters.")
                        track2("Come all you young farters who follow the sea")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Me.")
                        track2("To me, way, hey, blow the man down")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Her.")
                        track2("To her, way, hey, blow the man down")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Them.")
                        track2("To them, way, hey, blow the man down")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Go.")
                        track2("I'm ready to go")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Stay.")
                        track2("I'm ready to stay")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Fight.")
                        track2("I'm ready to fight")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Me.")
                        track2("Oh, give me a home where the buffalo roam")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Her.")
                        track2("Oh, give her a home where the buffalo roam")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Them.")
                        track2("Oh, give them a home where the buffalo roam")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Going.")
                        track2("Are you going to Scarborough Fair")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Dance.")
                        track2("Are you dancing to Scarborough Fair")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Fly.")
                        track2("Are you flying to Scarborough Fair")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Sweet.")
                        track2("I once met a girl named Sweet Molly Malone")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Weird.")
                        track2("I once met a girl named Weird Molly Malone")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Old.")
                        track2("I once met a girl named Old Molly Malone")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Swim.")
                        track2("I can't swim o'er")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Buy.")
                        track2("I can't buy more")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Want.")
                        track2("I don't want more")
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
                        track3("I thought I heard the Old Man say, Leave her, Johnny, leave her")
                        break
                    if choice == "2":
                        print("You have selected option two, Yell.")
                        track3("I thought I heard the Old Man yell, Leave her, Johnny, leave her")
                        break    
                    if choice == "3":
                        print("You have selected option three, Wish.")
                        track3("I thought I heard the Old Man wish, Leave her, Johnny, leave her")
                        break
                    if choice == "4":
                        print("You have selected option four, Up.")
                        track3("The winds blew up, her bow dipped down")
                        break
                    if choice == "5":
                        print("You have selected option five, Down.")
                        track3("The winds blew down, her bow dipped down")
                        break
                    if choice == "6":
                        print("You have selected option six, In.")
                        track3("The winds blew in, her bow dipped down")
                        break
                    if choice == "7":
                        print("You have selected option seven, Early.")
                        track3("What do you do with a drunken sailor early in the morning")
                        break
                    if choice == "8":
                        print("You have selected option eight, Lately.")
                        track3("What do you do with a drunken sailor lately in the morning")
                        break
                    if choice == "9":
                        print("You have selected option nine, Never.")
                        track3("What do you do with a drunken sailor never in the morning")
                        break
                    if choice == "10":
                        print("You have selected option ten, Sea.")
                        track3("Come all you young fellows who follow the sea")
                        break
                    if choice == "11":
                        print("You have selected option eleven, News.")
                        track3("Come all you young fellows who follow the news")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Game.")
                        track3("Come all you young fellows who follow the game")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Pillage.")
                        track3("We pillage, we plunder, we rifle and loot")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Sweep.")
                        track3("We sweep up, we plunder, we rifle and loot")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Bake.")
                        track3("We bake things, we plunder, we rifle and loot")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Door.")
                        track3("I'm standing here outside your door")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Store.")
                        track3("I'm standing here outside your store")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Car.")
                        track3("I'm standing here outside your car")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Home.")
                        track3("Oh, give me a home where the buffalo roam")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Job.")
                        track3("Oh, give me a job where the buffalo roam")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Zone.")
                        track3("Oh, give me a zone where the buffalo roam")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Scarborough.")
                        track3("Are you going to Scarborough Fair")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Grocery.")
                        track3("Are you going to the grocery store")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Comic.")
                        track3("Are you going to the comic book store")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Push.")
                        track3("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Sue.")
                        track3("I once met a girl named Sweet Molly Malone as she sued her wheelbarrow")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Shake.")
                        track3("I once met a girl named Sweet Molly Malone as she shook her wheelbarrow")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Wing.")
                        track3("And neither have I wings to fly")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Ticket.")
                        track3("And neither have I tickets to fly")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Bird.")
                        track3("And neither have I birds to fly")
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
                print("12   Them        27  My")
                print("13   Plunder     28  Build")
                print("14   Fart        29  Buy")
                print("15   Faint       30  Sell")
                break
            while True:
                while True:
                    if choice == "1":
                        print("You have selected option one, Leave.")
                        track4("Leave her, Johnny, leave her")
                        break
                    if choice == "2":
                        print("You have selected option two, Watch.")
                        track4("Watch her, Johnny, watch her")
                        break    
                    if choice == "3":
                        print("You have selected option three, Trust.")
                        track4("Trust her, Johnny, trust her")
                        break
                    if choice == "4":
                        print("You have selected option four, Blow.")
                        track4("Oh, blow, my bully boys, blow")
                        break
                    if choice == "5":
                        print("You have selected option five, Sing.")
                        track4("Oh, sing, my bully boys, sing")
                        break
                    if choice == "6":
                        print("You have selected option six, Dance.")
                        track4("Oh, dance, my bully boys, dance")
                        break
                    if choice == "7":
                        print("You have selected option seven, Morning.")
                        track4("What do you do with a drunken sailor early in the morning")
                        break
                    if choice == "8":
                        print("You have selected option eight, Party.")
                        track4("What do you do with a drunken sailor early at the party")
                        break
                    if choice == "9":
                        print("You have selected option nine, Evening.")
                        track4("What do you do with a drunken sailor early in the evening")
                        break
                    if choice == "10":
                        print("You have selected option ten, Me.")
                        track4("To me, way, hey, blow the man down")
                        break
                    if choice == "11":
                        print("You have selected option eleven, You.")
                        track4("To you, way, hey, blow the man down")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Them.")
                        track4("To them, way, hey, blow the man down")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Plunder.")
                        track4("We pillage, we plunder, we rifle and loot")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Fart.")
                        track4("We pillage, we fart, we rifle and loot")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Faint.")
                        track4("We pillage, we faint, we rifle and loot")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Hate.")
                        track4("I hate to wake you up to say goodbye")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Love.")
                        track4("I love to wake you up to say goodbye")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Want.")
                        track4("I want to wake you up to say goodbye")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Buffalo.")
                        track4("Oh, give me a home where the buffalo roam")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Carrot.")
                        track4("Oh, give me a home where the carrot cakes roam")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Stanley.")
                        track4("Oh, give me a home where the Stanley cups roam")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Parsley.")
                        track4("Parsley, sage, rosemary, and time")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Basil.")
                        track4("Basil, sage, rosemary, and thyme")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Chicken.")
                        track4("Chicken, sage, rosemary, and thyme")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Her.")
                        track4("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, His.")
                        track4("I once met a girl named Sweet Molly Malone as she pushed his wheelbarrow")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, My.")
                        track4("I once met a girl named Sweet Molly Malone as she pushed my wheelbarrow")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Build.")
                        track4("Build me a boat that will carry two")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Buy.")
                        track4("Buy me a boat that will carry two")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Sell.")
                        track4("Sell me a boat that will carry two")
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
                        track5("Leave her, Johnny, leave her")
                        break
                    if choice == "2":
                        print("You have selected option two, Timmy.")
                        track5("Leave her, Timmy, leave her")
                        break    
                    if choice == "3":
                        print("You have selected option three, Frodo.")
                        track5("Leave her, Frodo, leave her")
                        break
                    if choice == "4":
                        print("You have selected option four, Soon.")
                        track5("Soon may the Wellerman come to bring us sugar and tea and rum")
                        break
                    if choice == "5":
                        print("You have selected option five, When.")
                        track5("When may the Wellerman come to bring us sugar and tea and rum")
                        break
                    if choice == "6":
                        print("You have selected option six, Why.")
                        track5("Why may the Wellerman come to bring us sugar and tea and rum")
                        break
                    if choice == "7":
                        print("You have selected option seven, Brig.")
                        track5("Throw him in the brig until he's sober")
                        break
                    if choice == "8":
                        print("You have selected option eight, Toilets.")
                        track5("Make him scrub the toilets until he's sober")
                        break
                    if choice == "9":
                        print("You have selected option nine, Farts.")
                        track5("Make him smell your farts until he's sober")
                        break
                    if choice == "10":
                        print("You have selected option ten, Blow.")
                        track5("To me, way, hey, blow the man down")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Slap.")
                        track5("To me, way, hey, slap the man down")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Chase.")
                        track5("To me, way, hey, chase the man down")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Rifle.")
                        track5("We pillage, we plunder, we rifle and loot")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Vomit.")
                        track5("We pillage, we plunder, we vomit and loot")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Books.")
                        track5("We pillage, we plunder, we read books and loot")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Goodbye.")
                        track5("I hate to wake you up to say goodbye")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Hello.")
                        track5("I hate to wake you up to say hello")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Fart.")
                        track5("I hate to wake you up to say I farted")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Roam.")
                        track5("Oh, give me a home where the buffalo roam")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Sing.")
                        track5("Oh, give me a home where the buffalo sing")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Jump.")
                        track5("Oh, give me a home where the buffalo jump")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Sage.")
                        track5("Parsley, sage, rosemary, and thyme")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Cheese.")
                        track5("Parsley, cheese, rosemary, and thyme")                       
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Salt.")
                        track5("Parsley, salt, rosemary, and thyme")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Wheelbarrow.")
                        track5("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Knapsack.")
                        track5("I once met a girl named Sweet Molly Malone as she pushed her old knapsack")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Camaro.")
                        track5("I once met a girl named Sweet Molly Malone as she pushed her Camaro")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Me.")
                        track5("Build me a boat that will carry two")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Her.")
                        track5("Build her a boat that will carry two")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Him.")
                        track5("Build him a boat that will carry two")
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
                        track6("Tomorrow, ye will get your pay")
                        break
                    if choice == "2":
                        print("You have selected option two, Tuesday.")
                        track6("Next Tuesday, ye will get your pay")
                        break    
                    if choice == "3":
                        print("You have selected option three, Friday.")
                        track6("On Friday, ye will get your pay")
                        break
                    if choice == "4":
                        print("You have selected option four, Wellerman.")
                        track6("Soon may the Wellerman come to bring us sugar and tea and rum")
                        break
                    if choice == "5":
                        print("You have selected option five, Butterfly.")
                        track6("Soon may the Butterfly come to bring us sugar and tea and rum")
                        break
                    if choice == "6":
                        print("You have selected option six, Limousine.")
                        track6("Soon may the Limousine come to bring us sugar and tea and rum")
                        break
                    if choice == "7":
                        print("You have selected option seven, Rises.")
                        track6("Way, hey, and up she rises")
                        break
                    if choice == "8":
                        print("You have selected option eight, Wiggles.")
                        track6("Way, hey, and up she wiggles")
                        break
                    if choice == "9":
                        print("You have selected option nine, Bubbles.")
                        track6("Way, hey, and up she bubbles")
                        break
                    if choice == "10":
                        print("You have selected option ten, Attention.")
                        track6("And pray pay attention and listen to me")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Taxes.")
                        track6("And pray pay your taxes and listen to me")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Biscuit.")
                        track6("And pray eat some biscuits and listen to me")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Loot.")
                        track6("We pillage, we plunder, we rifle and loot")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Hoot.")
                        track6("We pillage, we plunder, we rifle and hoot")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Toot.")
                        track6("We pillage, we plunder, we rifle and toot")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Break.")
                        track6("But the dawn is breaking, it's early morn")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Leave.")
                        track6("But the dawn is leaving, it's early morn")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Dance.")
                        track6("But the dawn is dancing, it's early morn")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Deer.")
                        track6("Where the deer and the antelope play")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Skunk.")
                        track6("Where the skunks and the antelope play")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Mouse.")
                        track6("Where the mice and the antelop play")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Rosemary.")
                        track6("Parsley, sage, rosemary, and thyme")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Snickers.")
                        track6("Parsley, sage, a Snickers, and thyme")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Mojitos.")
                        track6("Parsley, sage, mojitos, and thyme")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Street.")
                        track6("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through streets broad and narrow")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Car.")
                        track6("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through cars broad and narrow")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Store.")
                        track6("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through stores broad and narrow")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Boat.")
                        track6("Build me a boat that will carry two")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Mouse.")
                        track6("Build me a mouse that will carry two")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Car.")
                        track6("Build me a car that will carry two")
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
                        track7("Tomorrow, ye will get your pay")
                        break
                    if choice == "2":
                        print("You have selected option two, Bell.")
                        track7("Tomorrow, ye will get your bell")
                        break    
                    if choice == "3":
                        print("You have selected option three, Fish.")
                        track7("Tomorrow, ye will get your fish")
                        break
                    if choice == "4":
                        print("You have selected option four, Come.")
                        track7("Soon may the Wellerman come to bring us sugar and tea and rum")
                        break
                    if choice == "5":
                        print("You have selected option five, Go.")
                        track7("Soon may the Wellerman go to bring us sugar and tea and rum")
                        break
                    if choice == "6":
                        print("You have selected option six, Leave.")
                        track7("Soon may the Wellerman leave to bring us sugar and tea and rum")
                        break
                    if choice == "7":
                        print("You have selected option seven, Clown.")
                        track7("Make him wear a clown suit until he's sober")
                        break
                    if choice == "8":
                        print("You have selected option eight, Dunce.")
                        track7("Make him wear a dunce cap until he's sober")
                        break
                    if choice == "9":
                        print("You have selected option nine, Crackers.")
                        track7("Make him just eat crackers until he's sober")
                        break
                    if choice == "10":
                        print("You have selected option ten, Blow.")
                        track7("Give me some time to blow the man down")
                        break
                    if choice == "11":
                        print("You have selected option eleven, Finish.")
                        track7("Give me some time to finish this round")
                        break
                    if choice == "12":
                        print("You have selected option twelve, Take.")
                        track7("Give me some time to take the mail down")
                        break
                    if choice == "13":
                        print("You have selected option thirteen, Drink.")
                        track7("Drink up, me hearties, yo ho")
                        break
                    if choice == "14":
                        print("You have selected option fourteen, Eat.")
                        track7("Eat up, me hearties, yo ho")
                        break
                    if choice == "15":
                        print("You have selected option fifteen, Shop.")
                        track7("Shop more, me hearties, yo ho")
                        break
                    if choice == "16":
                        print("You have selected option sixteen, Morning.")
                        track7("It's early morn")
                        break
                    if choice == "17":
                        print("You have selected option seventeen, Warm.")
                        track7("It's really warm")
                        break
                    if choice == "18":
                        print("You have selected option eighteen, Storm.")
                        track7("It's gonna storm")
                        break
                    if choice == "19":
                        print("You have selected option nineteen, Antelope.")
                        track7("Where the deer and the antelope play")
                        break
                    if choice == "20":
                        print("You have selected option twenty, Ant.")
                        track7("Where the deer and the ant sometimes play")
                        break
                    if choice == "21":
                        print("You have selected option twenty-one, Bear.")
                        track7("Where the deer and the bears sometimes play")
                        break
                    if choice == "22":
                        print("You have selected option twenty-two, Thyme.")
                        track7("Parsley, sage, rosemary, and thyme")
                        break
                    if choice == "23":
                        print("You have selected option twenty-three, Crime.")
                        track7("Parsley, sage, rosemary, and crime")
                        break
                    if choice == "24":
                        print("You have selected option twenty-four, Milk.")
                        track7("Parsley, sage, rosemary, and milk")
                        break
                    if choice == "25":
                        print("You have selected option twenty-five, Broad.")
                        track7("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through streets broad and narrow")
                        break
                    if choice == "26":
                        print("You have selected option twenty-six, Closed.")
                        track7("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through streets closed and narrow")
                        break
                    if choice == "27":
                        print("You have selected option twenty-seven, Old.")
                        track7("I once met a girl named Sweet Molly Malone as she pushed her wheelbarrow through streets old and narrow")
                        break
                    if choice == "28":
                        print("You have selected option twenty-eight, Carry.")
                        track7("Build me a boat that will carry two")
                        break
                    if choice == "29":
                        print("You have selected option twenty-nine, Ferry.")
                        track7("Build me a boat that will ferry two")
                        break
                    if choice == "30":
                        print("You have selected option thirty, Can't.")
                        track7("Build me a boat that can't carry two")
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
    