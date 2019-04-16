# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len = 8
p =  "".join(random.sample(s,passlen ))
print (p)
