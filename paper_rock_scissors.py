import random

moves = ["paper", "rock", "scissors"]
gamer = input("Choose: paper, rock, scissors ")
keep_playing = True
while keep_playing:
    npc = random.choice(moves)
    print("Computer choose "+ npc)

    if gamer == npc: print("Draw")
    if gamer =="paper" and npc == "rock":
        print("You're win")
    if gamer =="paper" and npc =="scissors":
        print("Computer wins")
    if gamer =="rock" and npc =="paper":
        print("Computer wins")
    if gamer =="rock" and npc =="scissors":
        print("You'are win")
    if gamer =="scissors" and npc =="paper":
        print("You'are win")
    if gamer =="scissors" and npc =="rock":
        print("Computer wins")

    new_choice = input("Do you wanna play one more time? Yes/No ")
    if new_choice == "Yes":
        keep_playing = True
    if new_choice =="No":
        keep_playing = False
