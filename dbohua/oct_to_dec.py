import math
def oct_to_dec(oct_num):
    length = len(oct_num)
    dec_num = 0
    for i in range(length):
        dec_num += (float(oct_num[i]) * float(math.pow(8, length-i-1)))
    return dec_num

print(oct_to_dec("00010011"))
    
