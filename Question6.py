""" 
  Write a software/program that is able to read from the keyboard (with a input command)
- a integer representing a city's population (we're going to denote/set this number as P);
- a real number (float), greater than 1, representing the flu infection rate in that city (we're going to denote/set this number as txInfection). 
Assume that the user will always type a value greater than 1 for TxInfection, i.e., it will not be necessary to check it again.
Now let's denote/set the number of infected people in a day i as Cti. Also consider that today is the day 0 of study, i.e., i=0, 
and this city has exactly Ct0=1040 infected people. Also consider that:
  I) Only the people that were infected in the day i-1 is able to infect people in the day i (i.e, Cti=Cti-1 * TxInfection), 
for 0 < i ≤ NumDiasImunidade where NumDiasImunidade is the number of days to obtain collective immunity.
  II) Any person that is already infected will survive and acquire immunity for the rest of the running time of this model
  III) The calculus/calculation of the number of immunized people in the city is cumulative. For instance, the number of immunized people in day 5 
is equal to Ct0 + Ct1 + Ct2 + Ct3 + Ct4 + Ct5.
  IV) The collective immunity in that population will occur when the number of infected people is greater or equal to 71% of the total population. 
In other words, the infectations will keep occurring as long as the number of immunized people is less than 0.71*P Given the population of the city
and the infection rate (both read through input commands), your software/program must print how many days the city will reach collective immunity.

"""

P = int(input())
txInfection = float(input())

Ct0 = 1040    
imun = 0
imunColetiva = 0.71 * P
numDiasImunidade = 0

for numDiasImunidade in range(0, numDiasImunidade + 1):
  while imun < imunColetiva:
    Ct0 = Ct0 * txInfection
    imun = imun + Ct0
    numDiasImunidade = numDiasImunidade + 1
   
  print(f"A cidade conseguiu imunidade coletiva em {numDiasImunidade} dias")
