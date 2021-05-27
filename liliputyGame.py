import random

def game():
    print('_______________________________')
    a = int(input('0/1: '))
    return a

"""===================================================="""
flag = True
print('1 to start/continue game, 0 to quit')
while flag == True:
    
    choice = game()

    if choice == 1:
        r = random.randint(1, 10)

        i = random.randint(0, 8)

        if i == 0:
            print(r, 'GIANTS')
        elif i == 1:
            print(r, 'FROG-JUMPS')
        elif i == 2:
            print(r, 'SPINS')
        elif i == 3:
            print(r, 'STEPS')
        elif i == 4:
            print(r, 'LILIPUTS')
        elif i == 5:
            print(r, 'CAMEL SPIT')
        elif i == 6:
            print(r, 'JUMPS')
        elif i == 7:
            print(r, 'GNOME WALK')
        else:
            print('DO NOT MOVE')
            
    elif choice == 0:
        print('-----------nice-game-----------')
        flag = False
        
    else:
        print('not an option')
    
