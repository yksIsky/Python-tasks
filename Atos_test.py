import random


def warm_cold():
    ran_int = random.randint(1,51)
    
    ip = 0
    while ran_int != ip:
        ip = int(input("Provide number from 1 -50 "))
        if ran_int == -1:
            print("End Game")
            break
        elif ip > ran_int:
            print("cold")
        elif ip < ran_int:
            print("warm")
            
    return print("You Won")

warm_cold()
