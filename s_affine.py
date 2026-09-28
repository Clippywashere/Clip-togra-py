from constructors import alphabet_constructor
import math

def affine_encrypt():

    affine_choice = int(input("Enter choice. 1 for affine, 2 for atbash, 3 for caesar, 4 for ROT13"))

    match affine_choice:
        case 1:
            slope = int(input("Enter slope: "))
            if math.gcd(slope,26) != 1:
                raise Exception('Invalid slope')
            intercept = int(input("Enter intercept: "))
        case 2:
            slope = 25
            intercept = 25
        case 3:
            slope = 1
            intercept = int(input("Enter key: "))
        case 4:
            slope = 1
            intercept = 13

    ctext = str()
    ptext = input("Enter plaintext: ").upper()
    alpha_capital = alphabet_constructor()

    for i in ptext:
        if i in alpha_capital:
            cletter = alpha_capital[(alpha_capital.index(i)*slope + intercept) %26]
            ctext += cletter
        else:
            pass

    print(ctext)

def affine_decrypt(slope,intercept):

#TODO: doesn't work, read up on modulo inverse function and/or euclidean algorithm to finish 

    ptext = str()
    ctext = input("Enter ciphertext: ").upper()
    alpha_capital = alphabet_constructor()

    for i in ctext:
        if i in alpha_capital:
            pletter = alpha_capital[int((alpha_capital.index(i) -intercept) /slope) %26]
            ptext += pletter
        else:
            pass

    print(ptext)