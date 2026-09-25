from constructors import polybiussquare_constructor

def bifid_encrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ptext = (input("Enter plaintext: ")).upper()
    ptext_25 = str()
    c1text = str()
    c2text = str()
    cftext = str()

    for i in ptext:
        if i == excluded_letter:
            ptext_25 += replacement_letter
        elif i == " ":
            pass
        else:
            ptext_25 += i

    for i in ptext_25:
        for j in polybiussquare:
            if i in j:
                c1text += str(polybiussquare.index(j) +1) + str(j.index(i) +1)
    
    for i in c1text[::2]:
        c2text += i
    for i in c1text[1::2]:
        c2text += i

    for j in range(0,len(c2text),2):
        cftext += polybiussquare[int(c2text[j]) -1][int(c2text[j +1]) -1]
    print(cftext)

def bifid_decrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ctext = input("Enter ciphertext: ").upper()
    p1text = str()
    pftext = str()

    for i in ctext:
        for j in polybiussquare:
            if i in j:
                p1text += str(polybiussquare.index(j) +1) + str(j.index(i) +1)

    for j in range(int(len(p1text)/2)):
        pftext += polybiussquare[int(p1text[j]) -1][int(p1text[j +int(len(p1text)/2)]) -1]
    print(pftext)