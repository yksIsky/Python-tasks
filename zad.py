import random

def warm_cold():
    ran_int = random.randint(1,51)
    print(ran_int)
    counter = 0
    ip = 0
    while ran_int != ip:
        ip = int(input("Provide number from 1 -50 \n"))
        counter += 1
        if ip > ran_int:
            print( "too much")
            continue
        elif ip < ran_int:
            print( "too low")
            continue


    return print(f"You won  {counter}")

warm_cold()