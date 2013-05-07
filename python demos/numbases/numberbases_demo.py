def dec_to_bin(x):
    binary = []
    binary.append(1)
    while x!=1:
        y = x%2
        x = x//2
        if y==1:
            binary.append(1)
        else:
            binary.append(0)
    return binary

print(dec_to_bin(2))

def bin_to_dec(x):
    
        
