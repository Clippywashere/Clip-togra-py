from random import randint
from math import ceil
ab_capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def columnar_encrypt():
    type_choice = int(input("Enter choice. 1 for regular, 2 for irregular: "))
    ptext = input("Enter plaintext: ").upper()
    key = input("Enter key: ").upper()
    keylength = int()
    grid = list()
    transposed_grid = list()
    ctext = str()

    for i in key:
        if i.isalpha():
            grid.append(i)
            keylength += 1

    count = 0
    if type_choice == 1:
        ptextlength = 0
        for i in ptext:
            if i.isalpha():
                grid[count %keylength] += i
                count += 1
                ptextlength += 1
        for j in range(keylength -(ptextlength %keylength) +1):
            if j != 0:
                grid[count %keylength] += ab_capital[randint(0,25)]
                count += 1
    elif type_choice == 2:
        for i in ptext:
            if i.isalpha():
                grid[count %keylength] += i
                count += 1
    else: print("Invalid type choice")

    for i in ab_capital:
        for j in grid:
            if j[0] == i:
                transposed_grid.append(j)

    for i in transposed_grid:
        ctext += i[1:]

    print(ctext)

def columnar_decrypt():
    #TODO: Write decryption function
    ctext = input("Enter ciphertext: ").upper()
    ptext = str()
    p1text = str()
    key = input("Enter key: ").upper()
    transposed_grid = list()
    keylength = int()
    ptextlength = int()
    max_col_length = int()

    for i in ab_capital:
        for j in key:
            if i == j:
                transposed_grid.append(i)
                keylength += 1

    for i in ptext:
        if i.isalpha():
            p1text += i
            ptextlength += 1

    max_col_length = ceil(ptextlength/keylength)

    count = 0
    while count < ptextlength:
        break
