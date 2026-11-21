from constructors_and_validators import polybiussquare_constructor, polybius_input_validator

def bifid_encrypt(chaining,ptext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    ptext_25 = str()
    c1text = str()
    c2text = str()
    cftext = str()

    ptext_25 = polybius_input_validator(ptext,excluded_letter,replacement_letter)

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
    
    return cftext

def bifid_decrypt(chaining,ctext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    p1text = str()
    pftext = str()

    ctext = ctext.upper()

    for i in ctext:
        for j in polybiussquare:
            if i in j:
                p1text += str(polybiussquare.index(j) +1) + str(j.index(i) +1)

    for j in range(int(len(p1text)/2)):
        pftext += polybiussquare[int(p1text[j]) -1][int(p1text[j +int(len(p1text)/2)]) -1]
    
    return pftext

def bifid_driver(mode,chaining,itext,keys):
    if mode == 1:
        return bifid_encrypt(chaining,itext,keys)
    else:
        return bifid_decrypt(chaining,itext,keys)