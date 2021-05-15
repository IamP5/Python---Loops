"""Make a program that receive 10 int numbers (one by one) and tell how much are positives, negatives and equal to zero. Print them in that order """


pos = 0
zero = 0
neg = 0

for i in range (10):
  i = int(input())
  if i > 0:
    pos = pos + 1 
  elif i < 0:
    neg = neg + 1
  else:
    zero = zero + 1
    
    

print(pos, '\n', neg, '\n', zero)
