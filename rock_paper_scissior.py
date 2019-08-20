import random

actions  = ["r" , "p" , "s"]
chances = 3
comp_score = 0
player_score = 0

player_name = input("Enter your name")

print("\nRock Paper Scissor\n")
print("*** Game Begins ***\n")

print("Enter R for rock\nP for paper \nS for Scissor\n")


# print(computers_choice)

while chances > 0:
    computers_choice = random.choice(actions)
    player_choice = input("Enter your choice from R , P , S\n")
    print("Computer's Choice is ",computers_choice)

    if player_choice is computers_choice:
        print("---Draw---")

    elif player_choice == "r" and computers_choice == "p" :
        print("---Computer wins---")
        comp_score = comp_score+1

    elif player_choice == "p" and computers_choice == "r":
        print("---player wins---")
        player_score = player_score+1

    elif player_choice == "p" and computers_choice == "s":
        print("---Computer wins---")
        comp_score = comp_score + 1 # r p s

    elif player_choice == "s" and computers_choice == "p":
        print("---player wins---")
        player_score = player_score + 1

    elif player_choice == "s" and computers_choice == "r":
        print("---Computer wins---")
        comp_score = comp_score + 1

    elif player_choice == "r" and computers_choice == "s":
        print("---player wins---")
        player_score = player_score + 1

    chances = chances-1

    continue

if player_score > comp_score:
    print(f"\n***---{player_name} Wins---***\n")

elif player_score < comp_score:
    print("\n***---Computer Wins---***\n")

else:
    print("\n***---It's a Draw---***\n")


