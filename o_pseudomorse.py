from random import randint

def pseudomorse_encrypt(chaining,ptext,keys):
    prob_morse = [1,1,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4]
    one_lettered_morse = [".","-"]
    two_lettered_morse = [".-","-.","..","--"]
    three_lettered_morse = ["...","..-",".-.",".--","-..","-.-","--.","---"]
    four_lettered_morse = ["-...","-.-.","..-.","....",".---",".-..",".--.","--.-","...-","-..-","-.--","--.."]
    c1text = str()
    cftext = str()
    temp = list()

    for i in ptext:
        if i != " ":
            j = "0" + bin(ord(i))[2:]
            for k in j:
                c1text += {"1":"-","0":"."}[k]
    
    while len(c1text) > 0:
        n = prob_morse[randint(0,25)]
        match n:
            case 1:
                temp = one_lettered_morse
            case 2:
                temp = two_lettered_morse
            case 3:
                temp = three_lettered_morse
            case 4:
                temp = four_lettered_morse
        if c1text[0:n] in temp:
            cftext += c1text[0:n] 
            cftext += " "
            c1text = c1text[n:]

    return cftext

def pseudomorse_decrypt(chaining,ctext,keys):
    p1text = str()
    pftext = str()

    for i in ctext:
        if i != " ":
            p1text += {"-":"1",".":"0"}[i]
    
    for j in range(0,int(len(p1text)/8)):
        pftext += chr(int(p1text[8*j:8*(j +1)],2))
    
    return pftext

def pseudomorse_driver(mode,chaining,itext,keys):
    if mode == 1:
        return pseudomorse_encrypt(chaining,itext,keys)
    else:
        return pseudomorse_decrypt(chaining,itext,keys)