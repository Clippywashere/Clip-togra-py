from constructors import alphabet_constructor

def affine_encrypt(slope,intercept):
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