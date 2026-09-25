def phonetic_encrypt():
    ptext = input("Enter plaintext: ").upper()
    phonetic_dict = {"A":"ALPHA","B":"BRAVO","C":"CHARLIE","D":"DELTA","E":"ECHO","F":"FOXTROT","G":"GOLF","H":"HOTEL","I":"INDIA","J":"JULIETT","K":"KILO","L":"LIMA","M":"MIKE","N":"NOVEMBER","O":"OSCAR","P":"PAPA","Q":"QUEBEC","R":"ROMEO","S":"SIERRA","T":"TANGO","U":"UNIFORM","V":"VICTOR","W":"WHISKEY","X":"XRAY","Y":"YANKEE","Z":"ZULU"}
    ctext = str()

    for i in ptext:
        if i in phonetic_dict:
            ctext += phonetic_dict[i]
        else: ctext += i

    print(ctext)

phonetic_encrypt()