import random 

computer_choices=['rock','paper','scissor']
player_choices=['rock','paper','scissor','scissors']

total_rounds=0
total_player_score=0
total_computer_score=0

print("#***************************#")
print("#    ROCK PAPER SCISSORS    #")
print("#***************************#")
print('\n')

play_again='yes'
play_again_choices=['yes','no','y','n']

while play_again in ['yes','y']:
    n=int(input("Number of rounds to play:"))
    print('\n')
    player_score=0
    computer_score=0
    for i in range(1,n+1):
        total_rounds+=1
        print("ROUND->",i)
        print('\t')
        computer_choice=random.choice(computer_choices)
        player_choice=input("Enter your choice(Rock/Paper/Scissor): ").lower()
        while player_choice not in player_choices:
            player_choice=input("Invalid input, please enter again:")
        print('Computer chose: ',computer_choice)
        
        if player_choice==computer_choice:
            print("Its a draw")
        
        elif player_choice=='rock' and computer_choice=='scissor':
            print("!!! You Won !!!")
            player_score+=1
            total_player_score+=1
        
        elif player_choice=='paper' and computer_choice=='rock':
            print("!!! You Won !!!")
            player_score+=1
            total_player_score+=1
        
        elif player_choice in ['scissors','scissors'] and computer_choice=='paper':
            print("!!! You Won !!!")
            player_score+=1
            total_player_score+=1
        
        else:
            print("!!! Computer Won !!!")
            computer_score+=1
            total_computer_score+=1
        
        print('\n')
    
    print("Rounds played: ",n)
    print("Player score: ",player_score)
    print("Computer score: ",computer_score)
    
    if player_score > computer_score:
        print("Player won by a margin of ",player_score-computer_score," rounds")
    
    elif player_score < computer_score:
        print("Computer won by a margin of ",computer_score-player_score," rounds")
    
    else:
        print("!!! ITS A DRAW !!!")
    
    print("\n")
    play_again=input("Do you wanna play again (Yes/No): ").lower()
    while play_again not in play_again_choices:
        play_again=input("Invalid input, please enter again:")

print("\n"*2)
    
print("Total rounds played: ",total_rounds)
print("Total player score: ",total_player_score)
print("Total computer score: ",total_computer_score)
print('\n')
print("!!! Thank You For Playing !!!!")        
        
        
    