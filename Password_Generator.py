#password generator#

'''input: 8
output:
your password: FB3250Lx'''

import random
password_length=int(input())
upper_case="QWERTYUIOPLKJHGFDSAZXCVBNM"
lower_case="qwertyuioplkjhgfdsazxcvbnm"
symbols="!@#$%^&*/\?"
numbers="0123456789"
mix_password=upper_case+lower_case+symbols+numbers
password="".join(random.sample(mix_password,password_length))
print("your password:", password)

