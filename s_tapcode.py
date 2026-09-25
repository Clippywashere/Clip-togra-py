from constructors import polybiussquare_constructor

def tapcode_encrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ptext = (input("Enter plaintext: ")).upper()
    ptext_25 = str()
    ctext = str()

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
                ctext += "."*(polybiussquare.index(j) +1) + " " + "."*(j.index(i) +1) + " "
    print(ctext)

def tapcode_decrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ctext = (input("Enter ciphertext: ")).strip() + " "
    ptext = str()
    temp = str()
    tap_list = list()

    for i in ctext:
        if i == " ":
            tap_list.append(temp.count("."))
            temp = str()
        else:
            temp += i

    for j in range(0,len(tap_list),2):
        ptext += polybiussquare[tap_list[j] -1][tap_list[j +1] -1]
    print(ptext)