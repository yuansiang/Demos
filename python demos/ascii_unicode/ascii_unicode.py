#ASCII and Unicode
#American Standard Code for Information Interchange

# ASCII decimal to character
for i in range(65,123): # uppercase A to lowercase z
    print(chr(i), end = " ") # chr() returns ASCII character

print("\n")
# ASCII character to decimal
print(ord('A'), end ="\n")

# Unicode hexadecimal to character
print(chr(0x5fb7), end ="\n")

print(hex(ord('德')), end ="\n")

print(chr(0x5fb7) + chr(0x660e) + chr(0x653f) + chr(0x5e9c) + chr(0x4e2d) + chr(0x5b66))

