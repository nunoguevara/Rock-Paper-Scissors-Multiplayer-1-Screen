import time
import os
import getpass

rps = {'1' : 'Rock', '2' : 'Paper', '3' : 'Scissors'}

x = 0
y = 0

def rpsc():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

while True:
    print("Rock Paper Scissors 2 Players 1 Screen")
    input("Press Enter to Play the game ")
    while True:
        rpsc()
        player1 = getpass.getpass("Please input your choice as player 1 (use the number): ")
        time.sleep(0.3)
        player2 = getpass.getpass("Please input your choice as player 2 (use the number): ")
        if player1 and player2 in rps:
            print("Please wait...")
            time.sleep(1)
            print("Player 1 input: ", rps[player1])
            print("Player 2 input: ", rps[player2])
            if player1 == "1" and player2 == "3":
                print("Player 1 Win")
                x += 1
            elif player1 == "3" and player2 == "2":
                print("Player 1 Win")
                x += 1
            elif player1 == "2" and player2 == "1":
                print("Player 1 Win")
                x += 1
            elif player1 == player2:
                print("Draw")
            else:
                print("Player 2 Win")
                y += 1
            print("Score: ", x, ":", y)
            if x >= 4:
                print("Player 1 is the Winner!")
                x = 0
                y = 0
                break
            elif y >= 4:
                print("Player 2 is the Winner!")
                x = 0
                y = 0
                break
        else:
            print("Please input valid choice")