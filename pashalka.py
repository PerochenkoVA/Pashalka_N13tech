import random
import sys
import time

def main():
    playGame = (input(`Would you like to play a game? (Y/N) `))
    
    if playGame == (`Y`) or playGame == (`y`):
        print (`You answered Y for Yes`)
        print()
        time.sleep(1.5) # pause for a second and a half
        print(`Welcom to the Number Guessing game`)
        time.sleep(1.5) # pause for a second and a half
        print()
        print(`Lets see how smart you are ... ready`)
        time.sleep(1.5) # pause for three second
        print()
        print()
        
        # The game begins
        print (`I`m thinking of a munber between 1 fyd 200`)
        randomNumber = random.randint(1,201)
        found = False
        
        while not found:
            userGuess = int(input(`What`s your first guess? `))
            
            if userGuess == randomNumber:
                print(`Woo Hoo! You got it buddy!`)
                found = True
            elif userGuess > randomNumber:
                print(`Nope, you have to guss lower!`)
            else: 
                print(`Nope, you have to guess higher!`)
        print()
        print(`@@@$$$!!!*** GAME OVER ***!!!$$$@@@`)
        sys.exit()
    elif playGame == (`N`) or playGame == (`n`):
            print(`Since you said no, have a nice a day, GOODbye`)
    else:
            print(`Not a valid empty, try again Y or N `)
            main()
            
if __name__==`__main__`: main()
        
        
            