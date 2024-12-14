import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Enter a number between 2 and 4")
    else:
        print("Enter a number between 2 and 4") 

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print("\nPlayer", i + 1, "has just started!")
        print("Your total score is: ", player_scores[i], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (Y/n): ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1! Turn done")
                break
            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is: ", current_score)
        player_scores[i] += current_score
        print("Your total score is: ", player_scores[i])

max_score = max(player_scores)
winner = player_scores.index(max_score)
print("Player number", winner + 1, "is the winner with the score: ", max_score)