def check_parity(binary_pattern):
    i = 0
    x = 0
    q = len(binary_pattern)
    while (i < q):
        if (binary_pattern[i]=="1"):
            x = x + 1
        i = i + 1
    if (x%2==0):
        if(binary_pattern[0]=="1"):
            i = 1
            print("correct one is 0", end = "")
            while (i < q):
                print(binary_pattern[i], end = "")
                i = i+1
        else:
            i = 1
            print("correct one is 1", end = "")
            while (i < q):
                print(binary_pattern[i], end = "")
                i = i+1
    else:
        print("No Problem with parity (odd)")
    

binary_pattern = input("Enter binary pattern: ")
check_parity(binary_pattern)

##Enter binary pattern: 10010011
##correct one is 00010011
##>>> ================================ RESTART ================================
##>>> 
##Enter binary pattern: 10000101
##No Problem with parity (odd)
##>>> ================================ RESTART ================================
##>>> 
##Enter binary pattern: 00000001
##No Problem with parity (odd)
