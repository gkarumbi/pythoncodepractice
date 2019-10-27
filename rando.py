#   def generate_password(self):

import random

# from random import Random as Random

   
char="ABCDEFGHIJKLMNOPQRSTUVWXYXabcdefghijklmnopqrstuvwxyx1234567890!@#$#%$^%&^&*&()_+>?:<"
# char="ABCD>?:<"
password =""
ps =[]
# print(len(char))
# while 0 < len(char):

for i in range(8):
        ps.append(random.choice(char))

        password+= random.choice(char)
        # password= random.choice(char)
print(password)
print(ps)