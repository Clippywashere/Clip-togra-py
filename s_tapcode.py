from constructors_and_validators import polybiussquare_constructor, polybius_input_validator

def tapcode_encrypt(chaining,ptext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    ptext_25 = str()
    ctext = str()

    ptext_25 = polybius_input_validator(ptext,excluded_letter,replacement_letter)

    for i in ptext_25:
        for j in polybiussquare:
            if i in j:
                ctext += "."*(polybiussquare.index(j) +1) + " " + "."*(j.index(i) +1) + " "

    return ctext

def tapcode_decrypt(chaining,ctext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    ptext = str()
    temp = str()
    tap_list = list()

    ctext = ctext.strip() + " "

    for i in ctext:
        if i == " ":
            tap_list.append(temp.count("."))
            temp = str()
        else:
            temp += i

    for j in range(0,len(tap_list),2):
        ptext += polybiussquare[tap_list[j] -1][tap_list[j +1] -1]

    return ptext

def tapcode_driver(mode,chaining,itext,keys):
    if mode == 1:
        return tapcode_encrypt(chaining,itext,keys)
    else:
        return tapcode_decrypt(chaining,itext,keys)