print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tickle Island.")
print("Make it through to the end or be tickled to your death.") 

tickle_1 = input('You have entered the valley of tickles. You can go two directions, what will you choose? "Left" or "Right" \n').lower()
if tickle_1 == 'right':
    tickle_2 = input('You have reached the lake of laughs. You must get to the other side. Will you build a bridge and get over it or fly across on a tickle-billed duck? Choose "Bridge" or "Duck"\n').lower()
    if tickle_2 ==  "duck":
        tickle_3 = input('You come to a crossroad where you can either enter a spunky cave, go down a boring path, or open the door to a colorful mansion. Do you choose "path", "cave" or "Mansion"\n').lower()
        if tickle_3 == "path":
            print('You made it through the valley of tickles with virgin armpits! YOU WIN')
        elif tickle_3 == "cave":
            print('The cave opened up to an underwater dungeon filled with octopie that gave you ten-tickles and you died. GAME OVER')
        elif tickle_3 == "mansion":
            print('The mansion turned out to not be that exciting minus the billion ticking guinea pigs that live there that tickle all of you crevasses. GAME OVER')
        else: print('You lost and did not even get to be tickled. THE END')
    else: print('a bunch of jolly trolls made a home under your bridge invited you for dinner and tickled you senseless. THE END')
else: print('You have been lickled to death by a pack of silly dogs. THE END')




