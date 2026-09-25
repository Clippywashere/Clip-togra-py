def numtolet_encrypt():
    ptext = str(input("Enter Plaintext: "))
    numtolet_dict = {"0":"ZERO","1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
    ctext = str()

    for i in ptext:
        if i in numtolet_dict:
            ctext += numtolet_dict[i]
        else: ctext += i

    print(ctext)

numtolet_encrypt()