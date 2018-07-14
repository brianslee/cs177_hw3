'''
    Brian Lee
    3620101
    CMPSC 177
    Brute-force attack
'''

import sys
import crypt
import itertools

tyrionHash = "ZaK5ixQERPPlk"
tyrionSalt = "Za"

alphaNumAll = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print "Finding Tyrion's password..."

for possible in itertools.product(alphaNumAll, repeat=6):
    password = ''.join(possible)
    e_pass = crypt.crypt(password, tyrionSalt)

    print "Pass: {} Hash: {}".format(password, e_pass)

    if(e_pass == tyrionHash):
        print "Password: {} Salt: {} Hash: {}".format(password, tyrionSalt, e_pass)
        break
    

print "Done\n"
