from sys import exit
from textwrap import dedent
from random import randint
import winsound
import random

from scene import Scene


class Start(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Welcome to \"The legend of Zelda\" Game " + asterics)
        print("\n")
        print(dedent("""\tWelcome to hove groove, your city's being terrorised by the evil Zelda
            \tYou have to fight to stay alive, where do you wanna start ? 
            \tMurded FIONA's house, Evil ZELDA's childhood home, Hove groove's high school?"""))
        choice = input("> ")
        if choice == "FIONA" or choice == "fiona":
            return 'fionaHouse'
        elif choice == "ZELDA" or choice == "Zelda":
            return 'zeldaHome'
        elif choice == "high school" or choice == "High School":
            print("No!!!... Not yet anyways...")
            input("Press Enter ")
            return "start"
        else:
            print("????? And what's that? ?????\b")
            return 'start'


class FionaHouse(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Fiona's House " + asterics)
        print("\n")
        print(dedent("""There's a nasty hole on the roof in Fiona's house
            that's leads to hove groove's underground world
            There's a blanket on top of the couch
            What do you want to do?"""))
        print("\t* \"Climb over\" Something to get higher")
        print("\t* \"Jump\" up and down to reach the hole in the roof!")
        print("\t* \"Swing\" the end of a blanket into a hole")
        decide = input("> ")
        if decide == "climb over" or decide == "Climb over":
            print("""Well considering that you're tall to just grab the hole in the roof,
                  That won't work, Try again\n""")
                
            ##start again at the beginnning
            input("Press Enter ")
            return 'fionaHouse'
        elif decide == "Jump" or decide == "jump":
            print("""Jump?? Really? The roof is really high, unless you have got a trampoline...but you don't,
              so Try again!\n""")
            input("Press Enter ")
            return 'fionaHouse'
        elif decide == "Swing" or decide == "swing":
            print("""\nThe other half goes through the hole and the other half remains on your side
             and becomes perfectly balanced in the middle.
            The gravitational pull from both worlds holds the blanket perfectly in the middle
            Amazed by this, you grab hold of the blanket, climb up, go through and jump into the scary unknown! \n""")
            input("Press Enter ")
            return 'underFiona'
        else:
            print("\n????? Try again! ?????\n")
            return 'fionaHouse'


class ZeldaHome(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Zelda's Home " + asterics)
        print("\n")
        print(dedent("""\tThis is the childhood home of the monster himself,
            the walls are covered in dark tree branches,
            very creepy! There's a door to your \"left\" and the \"stairs\" 
            infront of you that leads upstairs, which way?"""))
        choose = input("> ")
        if choose == "left":
            print("The door is locked!\n")
            input("Press Enter ")
            return "zeldaHome"
        elif choose == "stairs":
            print(dedent("""The stairs lead to Zelda's room, you get inside and immediately
            zelda can feel your presence from the underworld. The lights start to illuminate
            from infront of you. He's in the rooom with you!
            Zelda wants to bring you to the underworld with him forever,
            What do you do? run, freeze or scream??"""))
            
            choice = input("> ")
            if choice == "freeze":
                print("""Being an easy target you are, Zelda just fryes your brains off with his finger """)
                input("Press Enter ")
                return "dead"
            elif choice == "scream":
                print("""That won't help but annoy Zelda, He lifts you up with his power
                    He then draws the air from insode of you along with your scream
                    He then lets go of you and you fall dead on the floor.""")
                return "dead"
            elif choice == "run":
                print("\tLeg it as fast as you can downstairs, but one of the tree brenches grabs you by the leg!")
                input("Press Enter ")
                return "fight"
            else:
                print("\n ????? And what's that?? ?????\n")
                return "zeldaHome"
           
                  
class ZeldaWorld(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Zelda's World " + asterics)
        
        print("""\n \tWelcome to Zelda's World, Zelda's world is the same as Hove Groove,
              but every else is dark, no sun , just some reddish glimmer of death and misery, 
              even the trees are red and it's full of ugly flying bats. You need to find Zelda
              and eliminate him, he may be at his own house, Fiona's house or at the high school.""")
        print("You need to make a choice, \"Fiona\",Zelda's \"House\" or \"High School\" ")
        chosed = input("> ")
        if chosed == "Fiona":
            return "underFiona"
        elif chosed == "House":
            return "underZelda"
        elif chosed == "High School":
            return "underSchool"
        else:
            print("\n??? Nah... You need to choose properly!\n ?????\n")
            return "ZeldaWorld"
            

class Fight(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Fight " + asterics)
        print("\n")
        print("""\tThe tree branch has got a tight grip on you and you have to get out,
            or else!!, do you fight like crazy? or use your head?""")
        choosing = input("> ")
        if choosing == "fight like crazy":
            print("""You punch the branch like crazy, but frankly it's pointless and before you know it,
                the whole house has got a hold on you, you're being killed slowly!""")
            return "dead"
        elif choosing == "use your head":
            print("""\nTools like cutlery and scissors are lying around...
            so you grab one of those and stab or cut the tree branches off you
            and leg it for your life.""")
            print("But... You ran into the underworld.......Somehow....")
            input("Press Enter ")
            return "underFight"
        else:
            print("\n???? You only had two distinct options!, Do it properly!")
            return "fight"
            

class Dead(Scene):
    
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " ☠You're Dead☠ " + asterics)
        print("\n")
        print("GoOd Job! GAme Over!! YoU Lost!!!")
        exit(0)
        

class UnderFiona(Scene):
    
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Underworld Fiona's House " + asterics)
        print("\n")
        print(dedent("""In Fiona's underworld house there's the same hole that leads to the normal world,
            the blanket is still left hanging.
            Fiona is the first victim that had her life taken by the evil Zelda, anyhow the hole
            in the roof is the only proof that links to the monster himself. """))
        print("Zelda is not here, go look for him!")
        print("choose: Zelda's house or high school")
        
        choosen = input("> ")
        if choosen == "Zelda's house" or choosen == "Zelda's House":
            return "underZelda"
        elif choosen == "High School" or choosen == "high school":
            return "underSchool"
        else:
            print("\n???? Comon! You need to make a precise choice! ????\n")
            return "underFiona"


class UnderZelda(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Underworld Zelda's House " + asterics)
        print("\n")
        print(dedent("""This is the underground location of zelda's own house, 
              like the topside there's only two options, the door to your left
              and the stairs ahead of you."""))
        print("Which way do you want to go? \"left\" door or the \"stairs\"? ")
        chosen = input("> ")
        if chosen == "left":
            print(dedent("""This time the door on the left is open,
                You walk into the room and immediately the dooor behind you closes shut! 
                 This is Zelda's own childhood room, he killed his family when he was young!
                Zelda rises from under the floor into the rooom, he's a human being 
                but he has tentacles connected to him accross the room.
                He stands right there infront of you, his skin looks like the branches
                he's connected to, you can see him because somehow Zelda's room has candles
                That's his weakness, he's half human and half plant.
                You're both looking at each other, he gets annoyed and translocates you
                out of his room."""))
            input("Press Enter ")
            return "underFight"
        elif chosen == "stairs":
            print(dedent("""The room contains a window that looks directly to Zelda's room
            in the normal world and it acts as his passage to cross to the other side to kill us
            You need to destroy this window!!!.....
            The room is filled with different objects that you can use, Machete, Spade, and a brick
            Zelda is unpredictable!!!"""))
            
            weapon = input("> ")
            if weapon == "Machete":
                print(dedent("""Great choice! You can use the machete to vut Zelda's window,
                this is possible in Zelda's world!
                You cut the window into pieces, You have made Zelda very angry!!
                He comes from behind with a smack"""))
                input("Press Enter ")
                return "underFight"
            elif weapon == "spade" or weapon == "Spade":
                print(dedent("""So you take the spade and jam it at the window, it's not an 
                             excellent choice but the spade does leave some damage on his window
                             You left some scratches at level 2, with some deeper grooves at level 3
                             Zelda is annoyed at the execution of shoddy job you have done
                             He comes from behind you and gives you a smack it knocks you out."""))
                input("Press Enter ")
                return "underFight"
            elif weapon == "brick" or weapon == "Brick":
                print(dedent("""You throw the brick at the window but the window carves in a little
                             then bounces back and chucks the brick back at the floor
                             You keep smacking that window, that you end up attracting Zelda's attention to yourself
                             He grabs you by the neck and lifts you off the ground until you next to ugly ceiling
                             He then throws you at the wall, you're out cold!"""))
            else:
                print("\n??? There's only two distinctive options! Try again!! ????\n")
                return "underZelda"
                

class UnderFight(Scene):
 
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Underworld Fight Scene " + asterics)
        print("\n")
        
        print(dedent("""\tYou wake up in Zelda's land, everything is dark brown, no sun, no moon
            but there's is some kind of light albeit everything is brown.
            There's some questionable objects on the floor like a chainsaw, Gasoline and a Hammer
            Zelda rises from under the land into the open world, he's a human being 
            but he has tentacles connected to him across the floor.
            He stands right there in-front of you, his skin looks like the branches
            he's connected to, you can see him because Zelda is big Guy... but not muscular.  
            You're both looking at each other....again! He gets really annoyed and the battle begins
            You have a few weapons at your disposal,
             \n1. Gasoline\n2. Brick\n3. Chainsaw\n4. Bleach and \n5. Hose pipe"""))
        weapon = int(input("Pick your number: "))
        
        if weapon == 1:
            
            print("""So you pick the gas bottle and throw it it at Zelda, he's covered in gasoline but now what?
                Gas on its own won't ignite, you need one of his candles, Quick! go this room and get one, 
                Type :\"Candle\" """)
            decided = input("> ")
            while decided != "candle" or decided != "Candle":
                decided = input("You need to type \"candle\" ")
                    
            if decided == "candle" or decided == "Candle":
                print("Great! You need to burn him down, now type the magic word!")
                magic = input("> ")
                if magic == "burn!!!" or magic == "throw!!!" or magic == "BURN!!!" or magic == "Burn!!!":
                    print(dedent("""You chuck the candle at him and viola! he catches on fire and he screams in pain
                    Bwaaaaaaahhhhhhhhhaaaahaaaaaaaa!!!!!...... He burns in pain!!!"""))
                    input("Press Enter ")
                    return "complete"
                else:
                    print("\nYou need to type the word that'll the mission! ?????\n")
                    input("Press enter ")
                    return "dead"
                        
            else:
                print("You're Worse than a Drunkard's jokes!!")
            
        elif weapon == 2:
            print("""You chuck a brick at ihim and Zelda catches it in the air and chucks it stright at your head
                at speed, ouch! You're dead!""")
            return "dead"
        elif weapon == 3:
            print("Excellent choice, you can use the chainsaw to grind him to pieces, ready! go! type \"start\" ")
            fight = input("> ")
            while fight != "start":
                fight = input("type \"start\" > ")
            life = 0

            kitt = "chophim"
            print("Press :")
            while life < 7:
                print(kitt[life])
                grind = input("> ")
                if grind != kitt[life]:
                    #tells the player what they should have typed
                    print(f"You should have typed \" {kitt[life]}\"")
                    print("Watch properly!")
                    input("Press Enter ")
                    return "dead"
                life = life + 1
            print(kitt)
            print("Congratulations! You chopped him to pieces!!")
            input("Press Enter ")
            return "complete"
        elif weapon == 4:
            print(dedent("""Unexpected choice, but i'm sure you would have known, bleach kills plants
                    and since Zelda is part-plant, we can use bleach to eliminate him
                    You'll need to get close to him to bleach him, the fight begins, Ready! """))
            print("You run toward him, he sees you but his gonna wack your head head off, duck")
            defense = input("> ")
            if defense == "d":
                print(dedent("""Nice move, you duck and his hand goes over your lucky head,
                and you push forward, he comes for your legs, duck!"""))
                move = input("> ")
                if move == "u":
                    print(dedent("""Nice , you jump up and his glorious smack missed you buy an inch,
                     you're getting close,
                        but he's about to split you in half , duck!"""))
                    strike = input("> ")
                    if strike == "l":
                        print("You duck left and he stikes the ground and cracks the stones on it")
                        print("You need to pour it at him")
                        #list initialisation

                        poison = "pour pour pour"
                        print("Press: ")
                        life = 0
                        while life < 14:
                            ##display the contents of the list
                            print(poison[life])
                            grind = input("> ")
                            if grind != poison[life]:
                                print(f"You should have typed \"{poison[life]}\"")
                                input("Press Enter ")
                                return "dead"
                            life = life + 1
                        print(poison)
                        print("You pour the bleach on him and Zelda cries in pain and dies slowly, ")
                        return "complete"
                    elif strike == "r":
                        print("You duck right and  he strikes the ground and cracks the stones on it")
                        print("You need to pour it at him")

                        poison1 = "pour pour pour"
                        print("Press: ")
                        life = 0
                        while life < 14:
                            print(poison1[life])
                            grind = input("> ")
                            if grind != poison1[life]:
                                print("ahh, dead!")
                                print(f"You should have typed \"{poison1[life]}\" ")
                                input("Press Enter ")
                                return "dead"
                            life = life + 1
                        print(poison1)
                        print("You poired bleach on him and Zelda cries in pain and slowly dies,")
                        return "complete"
                    else:
                        print("\n ???? bad input! ????\n")
                        print("You get split in half!")
                        input("Press Enter ")
                        return "dead"
                else:
                    print("\n???? bad inout! ????\n")
                    print("Zelda swipes you off your lazy feet, You're toast!!")
            else:
                print("\n????? bad input! ?????\n")
                print("He smacks your head off!!")
                input("Press Enter ")
                return "dead"

        elif weapon == 5:
            mawaza = ["What are you going to with it choke him down?"
                      " Zelda will tear the hose in half!! and then you're next!",
                "Oh so maybe you wanna whip him with the hose??? "
                "Will that kill him, No!! It won't!!! You have a death☠ wish!!!",
                "Maybe you wanna water him down? but that'll make him only stronger.... "
                "because plants need water!!!",
                "Maybe you wanna tie him down, from the leg or something,"
                " that could work...provided you have enough strength to hold him,"
                " you're taking chances, A - for Effort"]
            print(random.choice(mawaza))
            input("Press Enter ")
            return "dead"
        else:
            print("\n????? Bad input! ?????\n")
            return "underFight"


class UnderSchool(Scene):
    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " Hove Groove High School " + asterics)
        print("\n")
        print(dedent(""" \tWelcome to the underworld of Hove Groove's High school
            You enter through the door and go past the Principal's office 
            until you reach a door that opens up to the basket ball's court
            You enter inside and it looks like no one has been here for a while
            and there's some spider webs here and there, you clear your throat
            and there's some echo throughout the room.
            Suddenly you hear foot steps of a four legged animal and it's headed your way!
            The only way out is through lab's door, you run towards it and it's locked
            with a keypad.
                """))
        print("\t You have to guess the PIN to get out!!!,"
              " The PIN has 4 digits \"You can use the clue\" \"Integer Only!!!\" ")
        
        code = f"{randint(1,3)}{randint(2,5)}{randint(3,7)}{randint(5,9)}"

        guess = int(input("[keypad]> : "))

        guesses = 0
        maxed = 7
        coded = int(code)
        while guess != coded and guesses < 7:
            if guesses == 6:
                print(f"You have {maxed - guesses} try left.")
            if guesses < 6:
                print(f"You have {maxed - guesses} tries left.") 
            print("Beep!!")
            winsound.Beep(2000, 1000)
            guesses += 1
            guess = int(input("[keypad]> : "))
            if guess == 0000:
                print("The 1st digit is between 1 & 3, The 2nd is between 2 & 5,"
                      " The 3rd is between 3 & 7, The 4th is between 5 & 9")
                guesses -= 1
                winsound.Beep(1000, 500)
            elif guess == 746:
                print(code)
                guesses -= 1
                winsound.Beep(500, 500)
            elif len(str(guess)) > 4:
                print("PIN can't be more than four digits!")
                winsound.Beep(250, 500)
            elif len(str(guess)) < 4 and guess != 746:
                print("PIN can't be less than four digits")
                winsound.Beep(250, 500)
            else:
                print("")

        if guess == coded:
            winsound.Beep(1000, 500)
            print("\nYou manage to open the door and lock yourself in before the creeps come an eat you!")
            print(dedent("""The creature runs after you and smashes in the door,
             it then throws the flames at the door from it's mouth,
             in a few minutes the creature will burn the dooor out and eat you!
            There's secret doors in the lab labelled 1 and 2, which one do you pick?"""))
        
            keyed = int(input("> "))
            if keyed == 1:
                print("You go through the first and then everything goes blank, you're unconcious")
                input("Press Enter ")
                return "underFight"
            elif keyed == 2:
                print("You go through the second door and then everything goes blank, you're unconcious")
                input("Press Enter ")
                return "underFight"
            else:
                print("Oh Noo!!!!!")
                return "underSchool"
        else:
            winsound.Beep(4000, 2000)
            print("""\nThat's the sound of death!!
            \nThe creature fries the door open and fries you with flames from it's mouth
                before it finally eats the crunchy you for lunch""")
            input("Press Enter ")
            return "dead"
            

class Complete(Scene):

    def enter(self):
        asterics = "*" * 30
        print("\n")
        print(asterics + " ○( ＾皿＾)っ Hehehe…(￣y▽￣)╭ Ohohoho....." + asterics)
        print("\n")
        print("Congratulations!!, You have defeated Zelda , You have won the game.")
    