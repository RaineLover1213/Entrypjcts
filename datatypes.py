#print(type('hello wrld'))
firstnum=input ('What is the first number? ')
secondnum=input('What is your second number? ')
if firstnum > secondnum:
 print(f"{firstnum} is greater than {secondnum}")
elif firstnum < secondnum:
 print(f"{firstnum} is less than {secondnum}")  
elif firstnum == secondnum:
 print(f"{firstnum} and {secondnum} are equal.") 
else:
 print('Invalid submission')