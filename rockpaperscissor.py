import random
options=("rock","paper","scissors")
running=True
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter a choice(rock,paper,scissors):")
    print(f"player:{player}")
    print(f"computer:{computer}")
    if player==computer:
        print("it's a tie")
    elif player=="rock" and computer=="scissors":
        print("You won")
    elif player=="paper" and computer=="rock":
        print("You won")
    elif player=="scissors" and computer=="paper":
        prit("You won")
    else:
        print("You lose the game")
    play_again=input("play again?(y/n):")
    if not play_again=="y":
        running=False
print("Thanks for playing!")
