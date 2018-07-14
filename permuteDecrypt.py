'''
    Brian Lee
    3620101
    CMPSC 177
    Self-generated dictionary attack
'''

import sys
import crypt

if len(sys.argv) != 3:
    print "Usage: {} hash salt".format(sys.argv[0])
else:
    with open("permute.txt", "r") as dictionary:
        passwords = dictionary.read().splitlines()
    output = open("permPass.txt", "w")
    
    hash1 = sys.argv[1]
    salt = sys.argv[2]
    found = False
    
    for password in passwords:
        e_pass = crypt.crypt(password, salt)
        output.write(password)
        output.write(": ")
	toPrint = e_pass + '\n'
        output.write(toPrint)
        #output.write("\n")
        if(e_pass == hash1):
            print "Password: {}".format(password)
            found = True
            break
    output.close();
    
    if(found == False):
        print "Password not found.\n"
