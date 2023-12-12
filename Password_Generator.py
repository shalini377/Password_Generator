#password generator#

'''input: 8
output:
your password: FB3250Lx'''

import random
opinion=str(input("Do you want to customize your password(y/n):"))
password_length=int(input("Enter your password length:"))
if opinion=='n':
  upper_case="QWERTYUIOPLKJHGFDSAZXCVBNM"
  lower_case="qwertyuioplkjhgfdsazxcvbnm"
  symbols="!@#$%^&*/\?"
  numbers="0123456789"
  mix_password=upper_case+lower_case+symbols+numbers
  password="".join(random.sample(mix_password,password_length))
else:
  name=str(input("your_name:"))
  dob=input("DOB:")
  print(type(dob))
  content=str(input("Anything else to be added:"))
  mix_password=name+dob+content
  password="".join(random.sample(mix_password,password_length))
print("your password:", password)

