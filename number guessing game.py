# written by Mohammad.Amin.Kiani

####################################

from random import randint
import os

####################################
''' --------------------------------------------------------------------------- '''
kill = 0
my_number = randint(1,100)

while(True) :
    
    num = eval(input("please Enter my number [1 to 100] : "))
    
    if(num == my_number):
        print(f"YOU WON! that is...{num}")
        break
        
    else:
        if(kill == 8):
            print("GAME OVER! by...")
            break
        
        if(num < my_number):
            print("YOU LOSE! bigger than...")
            kill += 1
            input("q for quit :")
            os.system('cls')
            continue
        
        if(num > my_number):
            print("YOU LOSE! smaller than...")
            kill += 1
            input("q for quit :")
            os.system('cls')
            continue

''' --------------------------------------------------------------------------- '''
