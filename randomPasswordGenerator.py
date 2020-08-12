#randomPasswordGenerator
#used for choosing random elements from list
from random import choice
import string
digits=['1','2','3','4','5','6','7','8','9','0']
characters=['!','@','#','%','^','&','*','?','/','|',',','.']
x=string.ascii_lowercase
y=string.ascii_uppercase
# 8 digits random password
#choice is used for choosing elements
password=choice(y)+choice(x)+choice(digits)+choice(characters)+choice(y)+choice(x)+choice(digits)+choice(characters)
print(password)
# below method will be used for choosing more random password
for i in password:
    print(choice(password),end='')
