ab_capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def frequency_matcher():
    ctext = input("Enter ciphertext: ").upper()
    ptext = str()
    letter_freq = list()
    sorted_freq = list()
    freq_list = "ETAONRISHDLFCMUGYPWBVKJXZQ"

    for i in ab_capital:
        letter_freq.append([i,ctext.count(i)])
        
    for i in ab_capital:
        maximum = 0
        index = 0
        for j in letter_freq:
            if j[1] > maximum:
                maximum = j[1]
        for j in letter_freq:
            if j[1] == maximum:
                sorted_freq.append(letter_freq[index][0])
                letter_freq[index][1] = -1
                break
            else: index += 1

    for i in ctext:
        for j in sorted_freq:
            if i == j:
                ptext += freq_list[sorted_freq.index(j)]

    print(ptext)

def frequency_analyzer():
    ctext = input("Enter ciphertext: ").upper()
    letter_freq = list()
    for i in ab_capital:
        if ctext.count(i) != 0:
            letter_freq.append([i,ctext.count(i)])

    print(letter_freq)