def morse_encrypt():
    ptext = input("Enter plaintext: ").upper()
    ctext = str()
    alpha_morse = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}

    for i in ptext:
        if i in alpha_morse:
            ctext += alpha_morse[i]
            ctext += " "
        elif i == " ":
            ctext += "  "

    print(ctext)

def morse_decrypt():
    #TODO: refactor to make it cleaner

    ctext = input("Enter ciphertext: ").upper()
    ptext = str()
    morse_alpha = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z","":""}

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

    print(ptext)