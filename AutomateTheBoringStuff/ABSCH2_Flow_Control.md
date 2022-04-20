## Automate The Boring Things! CH2 Flow Control


#### Break and Continue
```python
while True:  # loop indefinitely when conditions fail
    print("Who are you?")
    name = input("> ")
    if name != "Victor":
        continue  # Not Victor? Back to the top of the loop
    print("Hello, Victor. What is your password?")

    password = input("> ")
    if password == 'ye':
        print("Access Granted")
        break  # Access is Granted so Break the loop
    print("Wrong Password")  # This is print statement is part of the while loop and will loop back to the top
```
*Break* statements when executed will break out of the while loop early. <br>
*Continue* statements when executed will jump back to the top of the loop and re-evalute the loop's condition.

#### Using Flow Control create a Rock Paper Scissors Game

```python
import random


def cpu():
    num = random.randint(0, 2)
    cpu_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return cpu_dict[num]


def rps_game():
    wins = 0
    losses = 0
    ties = 0
    while True:
        print(f"Your current results are:\nWins: {wins}\nTies: {ties}\nLoses: {losses}")
        print("Would you like to play Rock Paper Scissors?")
        ans = input("press any key to play or \"e\" to exit:  ")

        if ans == "e":
            break
        player_move = input("Rock \nPaper \nScissors\nEnter your choice: ")
        print("Okay! lets start! Rock Paper Scissors SHOOT!")
        cpu_move = cpu()
        print(f"You Picked {player_move}")
        print(f"CPU Picked {cpu_move}")

        if player_move == cpu_move:
            ties += 1
            print("You Tied!")
            continue
        elif player_move == "Scissors" and cpu_move == "Paper":
            wins += 1
            print("You Win!")
            continue
        elif player_move == "Rock" and cpu_move == "Scissors":
            wins += 1
            print("You Win!")
            continue
        else:
            losses += 1
            print("You Lost!")
            continue
    print(f"Your end results are:\nWins: {wins}\nTies: {ties}\nLoses: {losses}")


rps_game()

```
