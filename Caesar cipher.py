#Caesar cipher
#Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). 
#The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). 
#So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC".
#This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency
# analysis to guess the key, or just try all 25 keys

#bring in alphabet and put numbers to letters

import string
alphabet = list(string.ascii_lowercase)


'''
alphadict = {}
for index, ele in enumerate(alphabet):
    alphadict[index] = ele

print(alphadict)
'''


#encode:



def encode(strin,ciph):
    strlst = list(strin)
    for i in range(len(strlst)):
        try: 
            strlst[i] = alphabet[(alphabet.index(strlst[i])+ciph)%len(alphabet)]
        except:
            pass
    print(''.join(strlst))


#decode:
def decode(strin,ciph):
    strlst = list(strin)
    for i in range(len(strlst)):
        try: 
            strlst[i] = alphabet[(alphabet.index(strlst[i])-ciph)%len(alphabet)]
        except:
            pass
    print(''.join(strlst))

#run
def caesar_cipher():
    actiontype = input('Would you like to encode or decode a string? (type encode or decode): ').lower()
    if actiontype == 'encode':
        stringtoenc = input("Please enter the string you'd like to encode: ")
        cipher = int(input("Please enter the key you'd like to encode it with (an integer from 1-25): "))
        encode(stringtoenc,cipher)
    elif actiontype == 'deccode':
        stringtoenc = input("Please enter the string you'd like to decode: ")
        cipher = int(input("Please enter the key you'd like to decode it with (an integer from 1-25): "))
        encode(stringtoenc,cipher)


caesar_cipher()
