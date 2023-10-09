import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input("piedra, papel o tijera: ").lower()
    

    if not user_option in options:
        print("That option is not valid.")
        # continue
        return None, None
        
        
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Tie!")
        
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Rock beats scissors.")
            print("User won")
            user_wins += 1
            
        else:
            print("Paper beats rock")
            print("Computer won")
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "piedra":
            print("Paper beats rock")
            print("User won")
            user_wins += 1
        else:
            print("Scissors beats paper")
            print("Computer won")
            computer_wins += 1

    elif user_option == "tijera":
        if computer_option == "papel":
            print("Scissors beats paper")
            print("User won")
            user_wins += 1
        else:
            print("Rock beats scissors")
            print("Computer won")
            computer_wins += 1   
    return user_wins, computer_wins
        
def check_game_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print("The winner is the computer.")
        return True
    elif user_wins == 2:
        print("The winner is the user.")
        return True
    return False     
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    


    while True:
        
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('Computer wins', computer_wins)
        print('User wins', user_wins)
        
        rounds += 1
        
        user_option, computer_option = choose_options()
        
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
   
        if check_game_winner(user_wins, computer_wins):
            break

run_game()                                