from constructors import polybiussquare_constructor

def playfair_encrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ptext = (input("Enter plaintext: ")).upper()
    ptext_25 = str()
    c1text = str()
    c1text_list = list()
    cftext = str()

    for i in ptext:
        if i == excluded_letter:
            ptext_25 += replacement_letter
        elif i == " ":
            pass
        else:
            ptext_25 += i

    for i in range(len(ptext_25) -1):
        if ptext_25[i] == ptext_25[i +1]:
            c1text += ptext_25[i] + "X"
        else: c1text += ptext_25[i]
    c1text += ptext_25[len(ptext_25) -1]

    if len(c1text) %2 == 1:
        c1text += "X"

    count = 0
    for i in c1text:
        if count %2 == 0:
            c1text_list.append(c1text[count] + c1text[count +1])
        count += 1

    for i in c1text_list:
        first_letter_row_index = int(5)
        first_letter_col_index = int(5)
        second_letter_row_index = int(5)
        second_letter_col_index = int(5)
        for j in polybiussquare:
            if i[0] in j:
                first_letter_row_index = polybiussquare.index(j)
                first_letter_col_index = j.index(i[0])
            if i[1] in j:
                second_letter_row_index = polybiussquare.index(j)
                second_letter_col_index = j.index(i[1])
            if first_letter_row_index != 5 and second_letter_row_index != 5:
                if first_letter_row_index == second_letter_row_index:
                    cftext += polybiussquare[first_letter_row_index][(first_letter_col_index +1) %5] +polybiussquare[second_letter_row_index][(second_letter_col_index +1) %5]
                    first_letter_row_index = int(5)
                elif first_letter_col_index == second_letter_col_index:
                    cftext += polybiussquare[(first_letter_row_index +1) %5][first_letter_col_index] +polybiussquare[(second_letter_row_index +1) %5][second_letter_col_index]
                    first_letter_row_index = int(5)
                else:
                    cftext += polybiussquare[first_letter_row_index][second_letter_col_index] +polybiussquare[second_letter_row_index][first_letter_col_index]
                    first_letter_row_index = int(5)

    print(cftext)

def playfair_decrypt():
    polybiussquare, excluded_letter, replacement_letter = polybiussquare_constructor()
    ctext = input("Enter ciphertext: ").upper()
    p1text_list = list()
    pftext = str()

    count = 0
    for i in ctext:
        if count %2 == 0:
            p1text_list.append(ctext[count] + ctext[count +1])
        count += 1

    for i in p1text_list:
        first_letter_row_index = int(5)
        first_letter_col_index = int(5)
        second_letter_row_index = int(5)
        second_letter_col_index = int(5)
        for j in polybiussquare:
            if i[0] in j:
                first_letter_row_index = polybiussquare.index(j)
                first_letter_col_index = j.index(i[0])
            if i[1] in j:
                second_letter_row_index = polybiussquare.index(j)
                second_letter_col_index = j.index(i[1])
            if first_letter_row_index != 5 and second_letter_row_index != 5:
                if first_letter_row_index == second_letter_row_index:
                    pftext += polybiussquare[first_letter_row_index][(first_letter_col_index -1) %5] +polybiussquare[second_letter_row_index][(second_letter_col_index -1) %5]
                    first_letter_row_index = int(5)
                elif first_letter_col_index == second_letter_col_index:
                    pftext += polybiussquare[(first_letter_row_index -1) %5][first_letter_col_index] +polybiussquare[(second_letter_row_index -1) %5][second_letter_col_index]
                    first_letter_row_index = int(5)
                else:
                    pftext += polybiussquare[first_letter_row_index][second_letter_col_index] +polybiussquare[second_letter_row_index][first_letter_col_index]
                    first_letter_row_index = int(5)
        
    print(pftext)