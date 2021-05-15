"""
  Make a program that receive 11 int numbers. Print each number received followed by one of these lines:
    
    "is a multiple of three" if the number is a multiple of three.
    "is a multiple of five" if the number is a multiple of five.
    "is a multiple of three and five" if the number is multiple of three and five.
    
  If the number is not a multiple of three neither five, the program output should be only the number as itself.
    
 """

for i in range(11):
  i = int(input())
  
  if i % 3 == 0 and i % 5 == 0:
    print(f"{i} is a multiple of three")
  
  elif i % 3 == 0:
    print(f"{i} é múltiplo de três")
  
  elif i % 5 == 0:
    print(f"{i} is a multiple of five")
  
  else:
    print(i)
