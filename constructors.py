ab_capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def alphabet_constructor():
    alpha_choice = int(input("Enter choice. 1 for std alpha, 2 for keyed alpha, 3 for custom alpha: "))
    match alpha_choice:
        case 1:
            alpha_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        case 2:
            key = (input("Enter key: ")).upper()
            key_letter_list = []
            alpha_capital = str()

            for i in key:
                if i.isalpha():
                    if i not in key_letter_list:
                        alpha_capital += i
                        key_letter_list.append(i)
            for j in ab_capital:
                if j not in key_letter_list:
                    alpha_capital += j
        case 3:
            alpha_capital = (input("Enter custom alphabet: ")).upper()
    
    return alpha_capital

def polybiussquare_constructor():
    alpha_choice = int(input("Enter choice. 1 for std alpha (J->I), 2 for std alpha (K->C), 3 for keyed alpha, 4 for custom alpha: "))
    match alpha_choice:
        case 1:
            alpha_25 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
            excluded_letter = "J"
            replacement_letter = "I"
        case 2:
            alpha_25 = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
            excluded_letter = "K"
            replacement_letter = "C"
        case 3:
            key = (input("Enter key: ")).upper()
            excluded_letter = (input("Enter letter to be excluded: ")).upper()
            replacement_letter = (input("Enter letter to replace excluded letter: ")).upper()
            key_letter_list = [excluded_letter]
            alpha_25 = str()

            for i in key:
                if i.isalpha():
                    if i not in key_letter_list and i == excluded_letter:
                        alpha_25 += replacement_letter
                        key_letter_list.append(replacement_letter)
                        key_letter_list.append(i)
                    elif i not in key_letter_list:
                        alpha_25 += i
                        key_letter_list.append(i)
            for j in ab_capital:
                if j not in key_letter_list:
                    alpha_25 += j
        case 4:
            alpha_25 = (input("Enter custom alphabet: ")).upper()
            excluded_letter = (input("Enter letter to be excluded: ")).upper()
            replacement_letter = (input("Enter letter to replace excluded letter: ")).upper()
    
    polybiussquare = [[],[],[],[],[]]
    for i in range(5):
        for j in range(5):
            polybiussquare[i].append(alpha_25[j + 5*i])
    
    return polybiussquare, excluded_letter, replacement_letter