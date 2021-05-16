"""
  Make a program that receive a number "n" of spreadsheets. For each one, the program have to: 
  
    Receive the link of the spreadsheet from the user.
    Read the spreadsheet.
    Average the column "C".
    Print the value to two decimal places.
  
  Some spreadsheets to test: 
    https://www.dropbox.com/s/qm0c0r00oupv92t/Lista7P1.csv?dl=1
    https://www.dropbox.com/s/7nru5hihxssf5ry/Lista7P2.csv?dl=1
    
"""

import pandas as pd

n = int(input())

for link in range(n):
  link = input()

  df = pd.read_csv(link)
  mean = df["C"].mean()
  
  print(round(mean, 2))
