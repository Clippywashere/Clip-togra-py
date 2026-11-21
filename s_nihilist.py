from constructors_and_validators import polybiussquare_constructor, polybius_input_validator

def nihilist_encrypt(chaining,ptext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    ptext_25 = str()
    key_25 = str()
    key_numbers = list()
    ctext = str()

    if chaining == 0:
        key = (input("Enter key: "))
    else:
        key = keys[3]
    
    ptext_25 = polybius_input_validator(ptext,excluded_letter,replacement_letter)
    key_25 = polybius_input_validator(key,excluded_letter,replacement_letter)

    for i in key_25:
        for j in polybiussquare:
            if i in j:
                key_numbers.append((polybiussquare.index(j) +1)*10 + j.index(i) +1)

    count = 0
    for i in ptext_25:
        for j in polybiussquare:
            if i in j:
                ctext += str((polybiussquare.index(j) +1)*10 + j.index(i) +1 +key_numbers[count%len(key_25)]) +" "
                count += 1
    return ctext

def nihilist_decrypt(chaining,ctext,keys):
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor(chaining,keys)
    key_25 = str()
    nihi_list = list()
    unkeyed_nihi_list = list()
    key_numbers = list()
    ptext = str()
    temp = str()

    if chaining == 0:
        key = input("Enter key: ")
    else:
        key = keys[3]
    ctext = ctext.strip() + " "

    key_25 = polybius_input_validator(key,excluded_letter,replacement_letter)

    for i in key_25:
        for j in polybiussquare:
            if i in j:
                key_numbers.append((polybiussquare.index(j) +1)*10 + j.index(i) +1)

    for i in ctext:
        if i == " ":
            nihi_list.append(int(temp))
            temp = str()
        else:
            temp += i

    count = 0
    for i in nihi_list:
        unkeyed_nihi_list.append(int(i -(key_numbers[count %len(key_25)])))
        count += 1

    for i in unkeyed_nihi_list:
        ptext += polybiussquare[(i //10) -1][(i %10) -1]

    return ptext

def nihilist_driver(mode,chaining,itext,keys):
    if mode == 1:
        return nihilist_encrypt(chaining,itext,keys)
    else:
        return nihilist_decrypt(chaining,itext,keys)