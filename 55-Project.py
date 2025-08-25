# Rock Paper Scissors Game Using Random Module

'''
Winning Rulse as follow
Rock vs paper -> paper wins
Rock vs scissors -> paper wins
paper vs scissors -> paper wins

'''

import random
l= ["rock", "scissors", "paper"]

while True:
    comp_count = 0
    u_count = 0
    
    uc = int(input('''
     Game Start.......
     1- Yes 
     2- No | Exit                                 
                          '''))
    if uc == 1:
        for a in range(1,6):
            userInput = int(input('''
            1- Rock
            2- Scissior
            3- Paper                     
                                  '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissors"
            elif userInput == 3:
                uchoice = "paper"
            Comp_Choice = random.choice(l)
            
            if Comp_Choice == uchoice:
                print("Computer choice : ", Comp_Choice)
                print("Your choice : ", uchoice)
                print("Game its Tie!")
                u_count = u_count + 1
                comp_count = comp_count + 1
            
            elif (uchoice == "rock" and Comp_Choice == "scissors") or (uchoice == "paper" and Comp_Choice == "rock") or (uchoice == "scissors" and Comp_Choice == "paper"):
                print("Computer choice : ", Comp_Choice)
                print("Your choice : ", uchoice)
                print("You win!")
                u_count = u_count + 1
            else:
                print("Computer choice : ", Comp_Choice)
                print("Your choice : ", uchoice)
                print("Computer win!")
                comp_count = comp_count + 1
                
        if u_count == comp_count:
            print("Final Game Draw....")
            print("Your Score : ", u_count)
            print("Computer  Score : ", comp_count)
            
        elif u_count > comp_count:
            print("Final You Win The Game....!")
            print("Your Score : ", u_count)
            print("Computer  Score : ", comp_count)
        else:
            print("Final Computer Win The Game....!")
            print("Your Score : ", u_count)
            print("Computer  Score : ", comp_count)
        
    else:
        break