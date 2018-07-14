'''
    Brian Lee
    3620101
    CMPSC 177
    Dictionary Brute-force attack
'''

import sys
import crypt

if len(sys.argv) != 3:
    print "Usage: {} hash salt".format(sys.argv[0])
else:
    with open("words.txt", "r") as dictionary:
        passwords = dictionary.read().splitlines()
    output = open("hash.txt", "wb")
    
    hash1 = sys.argv[1]
    salt = sys.argv[2]
    found = False
    
    for password in passwords:
        e_pass = crypt.crypt(password, salt)
	toPrint = e_pass + '\n'
        output.write(toPrint)
        if(e_pass == hash1):
            print "Password: {}".format(password)
            found = True
            break
    output.close();
    
    if(found == False):
        print "Password not found.\n"
