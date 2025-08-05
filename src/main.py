from Player import Player
from random import randrange

def init_game():
    Players = [Player(input("Player 1 Name: ")), Player(input("Player 2 Name: "))]
    Players[0].link(Players[1])
    apostrophe = []
    for player in Players:
        if player.name[-1].lower() == 's':
            apostrophe.append("'")
        else:
            apostrophe.append("'s")
    turn = 0
    return Players, apostrophe, turn


def main():
    Players, apostrophe, turn = init_game()
    print("\nThis is Knucklebones!\n")

    while True:

        print(Players[0])
        
        if turn % 2 == 0:
            turn = 0
        print(f"It Is {Players[turn].name}{apostrophe[turn]} Turn: (press ENTER to roll) ", end="")
        
        input()
        dice = randrange(1, 7)
        print(f"You rolled a {dice}!\n")

        col = int(input("Select a Column to Place: "))
        while True:
            try:
                Players[turn].place(dice, col - 1)
                print()
                break
            except Exception as e:
                print(e)
                col = int(input("Choose an Available Column: "))
        


        if Players[turn].isfull():
            max_points = Players[0].total_points
            winner_idx = 0
            for i in range(1, len(Players)):
                if Players[i].total_points > max_points:
                    max_points = Players[i].total_points
                    winner_idx = i
            print(Players[0])
            print(f"{Players[winner_idx].name} Is The Winner!\n")
            
            play_again = input("Want to Play Again? (yes/no) ")
            print()
            if play_again == "yes" or play_again == 'y':
                Players, apostrophe, turn = init_game()
                continue
            break

        turn += 1




main()
