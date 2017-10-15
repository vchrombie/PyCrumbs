import sys

print('password generator')

print ('Enter the type of password : (strong,weak) ')
type = raw_input()
if type == 'strong':
   pwdlen = 8
else:
   pwdlen = 4

import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pwd =  "".join(random.sample(s,pwdlen ))

print('the new password is ' + pwd)
exit()
