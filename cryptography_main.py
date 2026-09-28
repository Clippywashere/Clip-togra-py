#cryptography main

ab_capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
import math

import s_morse
import s_affine
import s_tapcode
import s_playfair
import s_book
import s_nihilist
import m_bifid
import o_pseudomorse
import t_columnar
import l_frequency

path_choice = int(input("Enter choice. 1 for encryption, 2 for decryption, 3 for tools: "))

if path_choice == 1:
    type_choice = int(input("Enter choice. 1 for substitution, 2 for transposition, 3 for mixed, 4 for other: "))
    if type_choice == 1:
        cipher_choice = int(input("Enter choice. 1 for morse, 2 for affine, 3 for tapcode, 4 for playfair, 5 for book, 6 for nihilist: "))
        match cipher_choice:
            case 1:
                s_morse.morse_encrypt()
            case 2:
                s_affine.affine_encrypt()
            case 3:
                s_tapcode.tapcode_encrypt()
            case 4:
                s_playfair.playfair_encrypt()
            case 5:
                s_book.book_encrypt()
            case 6:
                s_nihilist.nihilist_encrypt()
            case _:
                print("Invalid cipher choice")
    elif type_choice == 2:
        cipher_choice = int(input("Enter choice. 1 for columnar: "))
        match cipher_choice:
            case 1:
                t_columnar.columnar_encrypt()
            case _:
                print("Invalid cipher choice")
    elif type_choice == 3:
        cipher_choice = int(input("Enter choice. 1 for bifid: "))
        match cipher_choice:
            case 1:
                m_bifid.bifid_encrypt()
            case _:
                print("Invalid cipher choice")
    elif type_choice == 4:
        cipher_choice = int(input("Enter choice. 1 for pseudomorse: "))
        match cipher_choice:
            case 1:
                o_pseudomorse.pseudomorse_encrypt()
            case _: print("Invalid cipher choice")
    else: print("Invalid type choice")
elif path_choice == 2:
    type_choice = int(input("Enter choice. 1 for substitution, 2 for transposition, 3 for mixed, 4 for other: "))
    if type_choice == 1:
        cipher_choice = int(input("Enter choice. 1 for morse, 2 for affine, 3 for tapcode, 4 for playfair, 5 for book, 6 for nihilist: "))
        match cipher_choice:
            case 1:
                s_morse.morse_decrypt()
            case 2:
                pass
            case 3:
                s_tapcode.tapcode_decrypt()
            case 4:
                s_playfair.playfair_decrypt()
            case 5:
                s_book.book_decrypt()
            case 6:
                s_nihilist.nihilist_decrypt()
            case _: print("Invalid cipher choice")
    elif type_choice == 2:
        pass
    elif type_choice == 3:
        cipher_choice = int(input("Enter choice. 1 for bifid: "))
        match cipher_choice:
            case 1:
                m_bifid.bifid_decrypt()
            case _:
                print("Invalid cipher choice")
    elif type_choice == 4:
        cipher_choice = int(input("Enter choice. 1 for pseudomorse: "))
        match cipher_choice:
            case 1:
                o_pseudomorse.pseudomorse_decrypt()
            case _: print("Invalid cipher choice")
    else: print("Invalid type choice")
elif path_choice == 3:
    tool_choice = int(input("Enter choice. 1 for freq analysis, 2 for freq matching: "))
    match tool_choice:
        case 1:
            l_frequency.frequency_analyzer()
        case 2:
            l_frequency.frequency_matcher()
        case _:
            print("Invalid tool choice")
else: print("Invalid choice") 