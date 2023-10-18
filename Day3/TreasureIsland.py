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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

lr = input("You\'re at a crossroad...Do you want to go left(L) or right(R)? 'L' or 'R' \n").upper()
if lr == "L":
    sw = input("You\'ve come to Do you want to swim(S) or wait(W)? 'S' or'W'\n").upper()
    if sw == "W":
        door = input("You have arrived at the island unharmed. There is a house with 3 doors.Which door will you choose? Yellow(Y), Red(R) or Blue(B)\n").upper()
        if door == "R":
            print("Didn't see that coming! You got burned by fire. GAME OVER!!")
        elif door =="B":
            print("Didn't see that coming! You got eaten by beasts. GAME OVER!!") 
        elif door == "Y":
            print("Congratulation!!! YOU WIN!")
        else:
            print("*sigh* Don't try to  be smart... GAME OVER!!!")
    else:
        print("That was unexpected! You are attached by trout. GAME OVER!!")
else:
    print("Ooops! You fell into a hole. GAME OVER!!")
