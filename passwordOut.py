'''
    Brian Lee
    3620101
    CMPSC 177
    Brute-force attack
'''

import sys
import crypt

tyrionHash = "ZaK5ixQERPPlk"
tyrionSalt = "Za"

alphaNumAll = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
numeric = "0123456789"
lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

password = 'aaaaaaaa'

output = open("password.txt", "wb")

for a in upperAlpha:
    password[0] = a
    
    for b in alpha:
        password[1] = b
        
        for c in alpha:
            password[2] = c
            
            for d in alpha:
                password[3] = d
                
                for e in alpha:
                    password[4] = e
                    
                    for f in alphaNumAll:
                        password[5] = f
                        out = password[0:5] 
                        output.write(out)
                        output.write("\n")
                        
                        for g in alphaNumAll:
                            password[6] = g
                            out = password[0:6]
                            output.write(out)
                            output.write("\n")
                            
                            for h in alphaNumAll:
                                password[7] = h
                                out = password[0:7]
                                output.write(out)
                                output.write("\n")
                                
output.close()