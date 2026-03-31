direction = input("Which direction would you like to take? ").lower()
if direction == 'left':
    modeOfTransport = input("You want to swin or want to go by boat")
    if modeOfTransport == 'boat':
        door = input("Which door would you like to take? ")
        if door == 'yellow':
            print("You got the Treasure")
        elif door == 'red':
            print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")