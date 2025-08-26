import random
import time

print('Welcome to the Vacum Cleaner Program')
time.sleep(2)

def recharge(charge):
    print('Battery is full!',"\u2605","\n")
    cleaning(charge=100)
    
def cleaning (charge):
    
    while charge>10 :
    

        text='Wait please for analysing...' 
        #typing mode
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1) 
        print("\u2665") #heart charachter

        room_A= random.choice([True, False])
        room_B= random.choice([True, False])
        time.sleep(5)

        if room_A==False:
            print('Room A is dirty! :(')
            a='Cleaning Room A...'
            for char in a:
                print(char, end='', flush=True)
                time.sleep(0.1) 
            time.sleep(5)
            print("\n",'Room A is clean! :D')
            time.sleep(2)
        else:
            print('Room A is clean! :D')
            time.sleep(2)
        if room_B==False:
            print('Room B is dirty! :(')

            b='Cleaning Room B...'
            for char in b:
                print(char, end='', flush=True)
                time.sleep(0.1) 
            time.sleep(5)
            print("\n",'Room B is clean! :D')
            time.sleep(2)

        else:
            print('Room B is clean! :D')
            time.sleep(2)
        charge-=25

        if charge<25:
            c='Battery is low! wait for charging...'
            for char in c:
                print(char, end='', flush=True)
                time.sleep(0.1)
            print("\n")
            time.sleep(3)
            recharge(charge=0)
            return charge
        


        
cleaning(charge=100)
