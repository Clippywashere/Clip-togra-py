import random

def book_encrypt(chaining,ptext,keys):
    #TODO: Make the selector truly random for marginally better security
    words_list = list()

    if chaining == 0:
        key = input("Enter key text: ")
    else: key = keys[0]
    key = key.upper() +" "

    temp = str()
    for i in key:
        if i == " ":
            if len(temp) != 0:
                words_list.append(temp)
                temp = str()
        elif i.isalpha(): temp += i

    constrained_alphabet = str()
    letter_list = list()

    for i in words_list:
        if i[0] not in letter_list:
            constrained_alphabet += i[0]
            letter_list.append(i[0])

    print("Available letters:", constrained_alphabet)

    ptext = ptext.upper()
    ctext = str()

    for i in ptext:
        filtered_list = list()
        if i == " ":
            ctext += "/ "
        else:
            for j in words_list:
                if j[0] == i:
                    filtered_list.append(j)
            ctext += str(words_list.index(random.choice(filtered_list)) +1) + " "

    return ctext

def book_decrypt(chaining,ctext,keys):
    words_list = list()
    ctext_list = list()
    ptext = str()

    if chaining == 0:
        key = input("Enter key text: ")
    else: key = keys[0]
    key = key.upper()

    temp = str()
    for i in key:
        if i == " ":
            if len(temp) != 0:
                words_list.append(temp)
                temp = str()
        elif i.isalpha(): temp += i

    temp = str()
    for i in ctext:
        if i == " ":
            try:
                temp = int(temp)
            except:
                pass
            ctext_list.append(temp)
            temp = str()
        else:
            temp += i

    for i in ctext_list:
        if i == "/":
            ptext += " "
        else:
            ptext += words_list[i -1][0]

    return ptext

def book_driver(mode,chaining,itext,keys):
    if mode == 1:
        return book_encrypt(chaining,itext,keys)
    else:
        return book_decrypt(chaining,itext,keys)