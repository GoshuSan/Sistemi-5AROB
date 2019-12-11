'''Rsa code, Gabriele Parola'''

import math

def mcd(a,b):  #trova il massimo comune divisore tra i due numeri
    while b:
        a,b = b,a%b
    return a

def mcm(a,b):  #Trova il minimo comune multiplo tra i due numeri
    return a // mcd(a,b)*b

def isPrime(n):  #controlla se il numero è primo 
    for p in range(2,int(np.sqrt(n))+1): #non è necessario ciclare oltre la radice del numero stesso per trovarne un divisore
        if (n%p==0):
            return False
    return True

def setC(m):  #Determina c
    c=2
    while c<m:
        if (mcd(c,m) != 1):
            c=c+1
        else:
            return c


def setD(c, m):  #Determina d
    d = 0
    while d<m:
        if ((c*d)%m)!=1:
            d = d+1
        else:
            return d


while True:
    p=int(input("Butta qui p: "))

    q=int(input("Butta qui q: "))

    if(isPrime(p) and isPrime(q)):
        break
    else:
        print("Ehi boomer, sti numeri non sono mica primi")


n=p*q #Viene calcolato n
print(f"N: {n}")


m=mcm(p-1, q-1) #Viene calcolato il minimo comune multiplo
print(f"M: {m}")

c=setC(m) #1<c<m tale che mcd(c,m) = 1
print(f"C: {c}")

#0<=d<m tale che (cd) mod m = 1
d=setD(c, m)
print(f"D: {d}")

while True:
    a=int(input("Butta qui un numero: "))

    if (a < n):
        encryptedA = pow(a, c) % n
        print(f"Encrypted number [{a}]: {encryptedA}")

        #Decriptazione dato
        unencryptedA = pow(encryptedA, d)%n
        print(f"Unencrypted number[{encryptedA}]: {unencryptedA}")
        break
    else:
        print(f"Num maggiore di: {n}")