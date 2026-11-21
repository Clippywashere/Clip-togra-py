def morse_encrypt(chaining,ptext,keys):
    ctext = str()
    alpha_morse = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}

    ptext = ptext.upper()

    for i in ptext:
        if i in alpha_morse:
            ctext += alpha_morse[i]
            ctext += " "
        elif i == " ":
            ctext += "  "

    return ctext

def morse_decrypt(chaining,ctext,keys):
    #TODO: refactor to make it cleaner
    ptext = str()
    morse_alpha = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","":""}

    ctext = ctext.upper()

    temp = str()
    count = 0
    for i in ctext:
        if i == "." or i == "-":
            temp += i
            count = 0
        elif i == " ":
            ptext += morse_alpha[temp]
            temp = str()
            count += 1

        if count == 3:
            ptext += " "
            count = 0
    ptext += morse_alpha[temp]

    return ptext

def morse_driver(mode,chaining,itext,keys):
    if mode == 1:
        return morse_encrypt(chaining,itext,keys)
    else:
        return morse_decrypt(chaining,itext,keys)