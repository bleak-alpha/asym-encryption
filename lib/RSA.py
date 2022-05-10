from os import putenv
import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False

def RSA(ch):
    if ch == 'E' or ch == 'e':
        genKey = input("Do you want to generate a key pair? (Y/N): ")
        if genKey == 'y' or 'Y':
            generateKeys()
            publicKey, privateKey = loadKeys()
        elif genKey == 'n' or genKey == 'N':
            publicKey = int(input("Public Key: "))
            privateKey = int(input("Private Key: "))
        message = input('Write your message here:')
        ciphertext = encrypt(message, publicKey)
        signature = sign(message, privateKey)
        print('Cipher text: {ciphertext}')
        print('Signature: {signature}')
    
    elif ch == 'D' or ch == 'd':
        ciphertext = input("Cipher Text: ")
        privateKey = int(input("Private Key: "))
        text = decrypt(ciphertext, privateKey)
        if text:
            print('Message text: {text}')
        else:
            print('Unable to decrypt the message.')
    elif ch == "v" or ch == "V":
        text = input("Text: ")
        signature = input("Signature: ")
        publicKey = input("Public Key")
        if verify(text, signature, publicKey):
            print('Successfully verified signature')
        else:
            print('The message signature could not be verified')
        
ch = input("d/e/v")
RSA(ch)