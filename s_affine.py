from constructors_and_validators import alphabet_constructor, input_validator
import math

def affine_encrypt(chaining,ptext,keys):
    global slope
    global intercept
    ctext = str()

    if chaining == 0:
        affine_choice = int(input("Enter choice. 1 for affine, 2 for atbash, 3 for caesar, 4 for ROT13: "))
        alpha_capital = alphabet_constructor()
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
    else:
        affine_choice = int(keys[0])
        alpha_capital = keys[1]
        match affine_choice:
            case 1:
                slope = int(keys[2])
                if math.gcd(slope,26) != 1:
                    raise Exception('Invalid slope')
                intercept = int(keys[3])
            case 2:
                slope = 25
                intercept = 25
            case 3:
                slope = 1
                intercept = int(keys[2])
            case 4:
                slope = 1
                intercept = 13

    ptext = input_validator(ptext)

    for i in ptext:
        if i in alpha_capital:
            cletter = alpha_capital[(alpha_capital.index(i)*slope + intercept) %26]
            ctext += cletter
        else:
            pass

    return ctext

def affine_decrypt(chaining,ctext,keys):
    slope_inverse = {1:1,3:9,5:21,7:15,9:3,11:19,15:7,17:23,19:11,21:5,23:17}
    global slope
    global intercept
    ptext = str()

    if chaining == 0:
        affine_choice = int(input("Enter choice. 1 for affine, 2 for atbash, 3 for caesar, 4 for ROT13: "))
        alpha_capital = alphabet_constructor()
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
    else:
        affine_choice = int(keys[0])
        alpha_capital = keys[1]
        match affine_choice:
            case 1:
                slope = int(keys[2])
                if math.gcd(slope,26) != 1:
                    raise Exception('Invalid slope')
                intercept = int(keys[3])
            case 2:
                slope = 25
                intercept = 25
            case 3:
                slope = 1
                intercept = int(keys[2])
            case 4:
                slope = 1
                intercept = 13

    ctext = input_validator(ctext)

    for i in ctext:
        if i in alpha_capital:
            pletter = alpha_capital[int((alpha_capital.index(i) -intercept)*(slope_inverse[slope%26])) %26]
            ptext += pletter
        else:
            pass

    return ptext

def affine_driver(mode,chaining,itext,keys):
    if mode == 1:
        return affine_encrypt(chaining,itext,keys)
    else:
        return affine_decrypt(chaining,itext,keys)