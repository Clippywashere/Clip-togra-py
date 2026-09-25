def semaphore_encrypt():
    ptext = input("Enter plaintext: ").upper()
    semaphore_dict = {"A":"7:30","B":"5:45","C":"10:30","D":"6:00","E":"1:30","F":"4:30","G":"6:22","H":"6:45","I":"10:35","J":"3:00","K":"8:00","L":"1:37","M":"2:37","N":"7:22","O":"8:52","P":"9:00","Q":"00:45","R":"9:15","S":"4:45","T":"11:00","U":"1:50","V":"4:00","W":"1:15","X":"4:07","Y":"10:15","Z":"4:15"}
    ctext = str()

    for i in ptext:
        if i in semaphore_dict:
            ctext += semaphore_dict[i] + " "
        elif i == " ":
            ctext += "/ "
        else: ctext += i

    print(ctext)

semaphore_encrypt()