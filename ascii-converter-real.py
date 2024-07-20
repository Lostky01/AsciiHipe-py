import random 
# random ass shit
print("enter the string : ")
text = input()
print("enter the number of cipher : ")
ciph_num = int(input())

def shift_cipher(text, ciph_num):
    result = ''
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + ciph_num) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + ciph_num) % 26 + 97)
        else:
            result += char
    
    return result

decoded_love = shift_cipher(text, ciph_num)
ascii_char = []
for i in decoded_love:
    ascii_char.append(ord(i))
print(ascii_char)    



for i in ascii_char:
    deprecated_ascii = ascii_char[0]
    if i == deprecated_ascii:
        print("wo ai ni " + chr(i), end='')
    else:
        print(chr(i), end='')    