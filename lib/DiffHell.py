from time import sleep
import random
def genPrime(num):
    prime_list = [] #initializing empty list to store prime numbers
    while True: #etting range according to digit input
        if num == 1:
            x = 0
            y = 9
            break        

        elif num == 2:
            x = 10
            y = 99
            break        

        elif num == 3:
            x = 100
            y = 999
            break

        elif num == 4:
            x == 1000
            y == 9999
            break        

        elif num == 5:
            x = 10000
            y = 99999
            break
        
        else: #default case, re-enter
            print("Can Upto 5 Digit Limit.......\n")
            continue
        
    for n in range(x, y):
        isPrime = True 

        for j in range(2, n): 
            if n % j == 0: #condition for non-prime number
                isPrime = False

        if isPrime: #stores prime numbers
            prime_list.append(n)    

    n = random.choice([i for i in prime_list if x<i<y]) #chooses random number among the list

    return n


def Diffie():
    while True: #getting value for private key
        a = input("Enter value for your private key: ")
        try:
            a = int(a)
        except:
            print("Enter a numerical value:")
            sleep(2)      
            continue
        break

    while True: #calculating p and g
        ch = input("Do you want to generate public numbers(p,g) automatically? (Y/N):")
        if ch == 'y' or ch == 'Y':
            while True:
                digit = int(input("Digits: "))
                n1 = int(genPrime(digit))
                n2 = int(genPrime(digit))
                if n2 < n1:
                    p = n1
                    g = n2            
                else:
                    p = n2
                    g = n1
                print("P: ", p)
                print("G: ", g)
                break

        elif ch == "N" or ch =='n':
            p = int(input("P:"))
            g = int(input("G: "))
            break
        
        elif ch == 'e' or ch == 'e':
            break
        else:
            break

    while True: #calculating create and generate exchanged key then generate shared key
        A = int(pow(g,a,p))
        print("Your publically generated Key: ",A)

        while True: #getting value for private key
            B = input("Enter Other publically obtained number: ")
            try:
                B = int(B)
            except:
                print("Enter a numerical value:")
                sleep(2)
                continue
            break

        key = int(pow(B,a,p))

        print("Shared Key is: ",key)

        break