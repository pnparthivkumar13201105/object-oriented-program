import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90)) 

password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4
password = shuffle(password)

print(password)