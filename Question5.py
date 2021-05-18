"""
  Make a program that read from keyboard two positive and int numbers "x" and "y". The program
  should be able to print on the screen a sequence of consecutives int numbers, from "x" to "y",
  one number per line. However, if a number of the sequence is a multiple of 6, then print
  "Multiple of 6" instead the number. Furthermore, the program should show at the final line how
  many multiples of 6 are in the sequence.

"""

x = int(input())
y = int(input())

count = 0

for i in range(x, y+1):
  if x % 6 == 0:
    print("Múltiplo de 6")
    x = x+1
    count = count + 1
  else:
    print(x)
    x = x+1

print(f"Total de múltiplos de 6: {count}")
