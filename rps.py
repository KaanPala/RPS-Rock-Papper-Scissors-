import random

List1 = ["Rock", "Papper", "Scissors"]

total_round = int(input("How many tour do you wanna play:"))
gamer1_point = int(0)
gamer2_point = int(0)
round_counter = 0


while True:
    round_counter +=1
    print("Round number:", round_counter)

    gamer1 = random.choice(List1)
    gamer2 = random.choice(List1)
    print("gamer1 : {}".format(gamer1))
    print("gamer2 : {}".format(gamer2))

    if(gamer1 == "Rock" and gamer2 == "Papper"):
        winner = "gamer2"
        print("Winner is gamer2")
    elif(gamer1 == "Rock" and gamer2 == "Scissors"):
        winner = "gamer1"
        print("Winner is gamer1")
    elif(gamer1 == "Papper" and gamer2 == "Scissors"):
        winner = "gamer2"
        print("Winner is gamer2")
    elif(gamer1 == "Papper" and gamer2 == "Rock"):
        winner = "gamer1"
        print("Winner is gamer1")
    elif(gamer1 == "Scissors" and gamer2 == "Rock"):
        winner = "gamer2"
        print("Winner is gamer2")
    elif(gamer1 == "Scissors" and gamer2 == "Papper"):
        winner = "gamer1"
        print("Winner is gamer1")

    elif(gamer1 == "Rock" and gamer2 == "Rock"):
        draw = ("gamer1=gamer2")
        winner = draw
        print("Game is scoreless")

    elif(gamer1 == "Papper" and gamer2 == "Papper"):
        draw = ("gamer1=gamer2")
        winner = draw
        print("Game is scoreless")

    elif(gamer1 == "Scissors" and gamer2 == "Scissors"):
        draw = ("gamer1=gamer2")
        winner = draw
        print("Game is scoreless")

    if(winner == "gamer1"):
        gamer1_point += 1
        gamer2_point += 0
        print("Gamer1 point = {}".format(gamer1_point))
        print("Gamer2 point = {}".format(gamer2_point))

    elif(winner == "gamer2"):
        gamer1_point += 0
        gamer2_point += 1
        print("Gamer1 point = {}".format(gamer1_point))
        print("Gamer2 point = {}".format(gamer2_point))

    elif(winner == draw):
        gamer1_point += 0
        gamer2_point += 0
        print("Gamer1 point = {}".format(gamer1_point))
        print("Gamer2 point = {}".format(gamer2_point))
    if round_counter == int(total_round):
     break
if gamer1_point == gamer2_point:
    print("There is no winner, tie.")
elif gamer1_point > gamer2_point:
    print("Player 1 won with score", gamer1_point, ":", gamer2_point)
elif gamer1_point < gamer2_point:
    print("Player 2 won with score", gamer1_point, ":", gamer2_point)
