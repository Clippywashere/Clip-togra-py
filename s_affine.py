from constructors import alphabet_constructor
import math

def affine_encrypt():

    affine_choice = int(input("Enter choice. 1 for affine, 2 for atbash, 3 for caesar, 4 for ROT13: "))
    global slope
    global intercept
    alpha_capital = alphabet_constructor()
    ctext = str()
    ptext = input("Enter plaintext: ").upper()

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

    for i in ptext:
        if i in alpha_capital:
            cletter = alpha_capital[(alpha_capital.index(i)*slope + intercept) %26]
            ctext += cletter
        else:
            pass

    print(ctext)

def affine_decrypt():

    affine_choice = int(input("Enter choice. 1 for affine, 2 for atbash, 3 for caesar, 4 for ROT13: "))
    global slope
    global intercept
    alpha_capital = alphabet_constructor()
    ptext = str()
    slope_inverse = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17}

    ctext = input("Enter ciphertext: ").upper()

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

    for i in ctext:
        if i in alpha_capital:
            pletter = alpha_capital[int((alpha_capital.index(i) -intercept)*(slope_inverse[slope%26])) %26]
            ptext += pletter
        else:
            pass

    print(ptext)