from s_morse import morse_driver
from s_affine import affine_driver
from s_tapcode import tapcode_driver
from s_playfair import playfair_driver
from s_book import book_driver
from s_nihilist import nihilist_driver
from m_bifid import bifid_driver
from o_pseudomorse import pseudomorse_driver
from t_columnar import columnar_driver

def chainer():
    func_dict = {"SM":morse_driver,
                "SA":affine_driver,
                "ST":tapcode_driver,
                "SP":playfair_driver,
                "SB":book_driver,
                "SN":nihilist_driver,
                "MB":bifid_driver,
                "OP":pseudomorse_driver,
                "TC":columnar_driver}
    chaining = 1 
    print("Chain cryptosystem format: ")
    print("[1 for encrypt, 2 for decrypt][input text](<cipher1> ckey1,key1,...,keyn)(<cipher2> ckey2,key1,...,keyn)...")
    print()
    print("ckeys: ")
    print("NORMAL CIPHERS: SA - Affine, SP - Playfair, MB - Bifid, TC - Columnar")
    print("TERMINATING ONLY: SM - Morse, OP - Pseudomorse, ST - Tapcode, SB - Book, SN - Nihilist")
    print()

    chain = input("Enter chain cryptosystem here: ")

    temp = str()
    split_list = list()
    for i in chain:
        if i in "[]()":
            split_list.append(temp)
            temp = str()
        else:
            temp += i
    split_list = split_list[1::2]

    mode = int(split_list[0])
    result = split_list[1]

    for i in split_list[2:]:
        inner_list = i.split(",")
        ckey = inner_list[0]
        keys = inner_list[1:]

        result = func_dict[ckey](mode,chaining,result,keys)

    return result