#cryptography main

path_choice = int(input("Enter choice. 1 for encryption, 2 for decryption, 3 for tools, 4 for chaining: "))

if path_choice == 1 or path_choice == 2:
    chaining = 0
    type_choice = int(input("Enter choice. 1 for substitution, 2 for transposition, 3 for mixed, 4 for other: "))
    if type_choice == 1:
        cipher_choice = int(input("Enter choice. 1 for morse, 2 for affine, 3 for tapcode, 4 for playfair, 5 for book, 6 for nihilist: "))
        if path_choice == 1:
            itext = input("Enter plaintext: ")
        else: itext = input("Enter ciphertext: ")
        keys = list()
        match cipher_choice:
            case 1:
                from s_morse import morse_driver
                result = morse_driver
            case 2:
                from s_affine import affine_driver
                result = affine_driver
            case 3:
                from s_tapcode import tapcode_driver
                result = tapcode_driver
            case 4:
                from s_playfair import playfair_driver
                result = playfair_driver
            case 5:
                from s_book import book_driver
                result = book_driver
            case 6:
                from s_nihilist import nihilist_driver
                result = nihilist_driver
            case _:
                print("Invalid cipher choice")
    elif type_choice == 2:
        cipher_choice = int(input("Enter choice. 1 for columnar: "))
        match cipher_choice:
            case 1:
                from t_columnar import columnar_driver
                result = columnar_driver
            case _:
                print("Invalid cipher choice")
    elif type_choice == 3:
        cipher_choice = int(input("Enter choice. 1 for bifid: "))
        match cipher_choice:
            case 1:
                from m_bifid import bifid_driver
                result = bifid_driver
            case _:
                print("Invalid cipher choice")
    elif type_choice == 4:
        cipher_choice = int(input("Enter choice. 1 for pseudomorse: "))
        match cipher_choice:
            case 1:
                from o_pseudomorse import pseudomorse_driver
                result = pseudomorse_driver
            case _: print("Invalid cipher choice")
    else: print("Invalid type choice")
    try:
        print(result(path_choice,chaining,itext,keys))
    except:
        pass
elif path_choice == 3:
    import l_frequency
    tool_choice = int(input("Enter choice. 1 for freq analysis, 2 for freq matching: "))
    match tool_choice:
        case 1:
            l_frequency.frequency_analyzer()
        case 2:
            l_frequency.frequency_matcher()
        case _:
            print("Invalid tool choice")
elif path_choice == 4:
    import chainer
    print(chainer.chainer())
else: print("Invalid choice") 