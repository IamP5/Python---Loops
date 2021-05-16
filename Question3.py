""" Make a program that receive a float number "n". If the number is greater than 157, print "Goal Achieved" and break the loop. 
    Else, print "Insufficient" and read a new number "n". You should read at most 5 numbers """

for i in range(5):
  i = float(input())

  if i > 157:
    print("Goal Achieved")
    break
  else: 
    print("Insufficient")
