from time import sleep

from DiffHell import Diffie, genPrime

print("""
________________  _______  ________  __________________________________________
___    |_  ___/ \/ /__   |/  /__   |/  /__  ____/__  __/__  __ \___  _/_  ____/
__  /| |____ \__  /__  /|_/ /__  /|_/ /__  __/  __  /  __  /_/ /__  / _  /     
_  ___ |___/ /_  / _  /  / / _  /  / / _  /___  _  /   _  _, _/__/ /  / /___   
/_/  |_/____/ /_/  /_/  /_/  /_/  /_/  /_____/  /_/    /_/ |_| /___/  \____/   
                                                                               
______________   ___________________  ___________________________________   __ 
___  ____/__  | / /_  ____/__  __ \ \/ /__  __ \__  __/___  _/_  __ \__  | / / 
__  __/  __   |/ /_  /    __  /_/ /_  /__  /_/ /_  /   __  / _  / / /_   |/ /  
_  /___  _  /|  / / /___  _  _, _/_  / _  ____/_  /   __/ /  / /_/ /_  /|  /   
/_____/  /_/ |_/  \____/  /_/ |_| /_/  /_/     /_/    /___/  \____/ /_/ |_/    
                                                                               
_____________ ___________________________________________  _______  __________ 
___    |__  / __  ____/_  __ \__  __ \___  _/__  __/__  / / /__   |/  /_  ___/ 
__  /| |_  /  _  / __ _  / / /_  /_/ /__  / __  /  __  /_/ /__  /|_/ /_____ \  
_  ___ |  /___/ /_/ / / /_/ /_  _, _/__/ /  _  /   _  __  / _  /  / / ____/ /  
/_/  |_/_____/\____/  \____/ /_/ |_| /___/  /_/    /_/ /_/  /_/  /_/  /____/   
""")
while True:
    ch = input("""
    Enter Your Choice:
    1. Diffie-Hellman Key Exchange
    2. RSA Data Encryption and Decryption
    3. ECC Public Key-Private Key Pair Generation
    4. DSA Data Signing Verification
    5. Prime Number Generation
    Q. Quit
    """)
    if ch == '1':
        import DiffHell
        Diffie()
        c = input("Menu/Exit(M/Q): ")
        if c == 'M' or ch == 'm':
            continue
        if c == "Q" or ch == 'q':
            break
        else:
            print("Wrong Input.....")
            break
    
    if ch == '2':
        import RSA
        c = input("Menu/Exit(M/Q): ")
        if c == 'M' or ch == 'm':
            continue
        if c == "Q" or ch == 'q':
            break
        else:
            print("Wrong Input.....")
            break
    
    if ch == '3':
        import ECC
        c = input("Menu/Exit(M/Q): ")
        if c == 'M' or ch == 'm':
            continue
        if c == "Q" or ch == 'q':
            break
        else:
            print("Wrong Input.....")
            break
    
    if ch == '4':
        import DSA
        c = input("Menu/Exit(M/Q): ")
        if c == 'M' or ch == 'm':
            continue
        if c == "Q" or ch == 'q':
            break
        else:
            print("Wrong Input.....")
            break
    
    if ch == '5':
        import DiffHell as d
        num = int(input("Digits: "))
        print(d.genPrime(num))
        c = input("Menu/Exit(M/Q): ")
        if c == 'M' or ch == 'm':
            continue
        if c == "Q" or ch == 'q':
            break
        else:
            print("Wrong Input.....")
            break