def dec_to_bin(x):
    bin_num = ""
    while x !=0:
        remainder = x%2
        bin_num=str(remainder)+bin_num
        x = x//2
    return bin_num

print(dec_to_bin(10))

def bin_to_dec(x):
        print("")
        
