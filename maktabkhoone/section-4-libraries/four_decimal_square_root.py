"""
Calculates square roots with exactly 4 decimal places.
Input:
  - tedad: Number of inputs
  - x: Series of numbers
Output:
  - Square roots formatted to 4 decimal places
"""
# ریشه دوم با دقیقا چهاررقم اعشار
import math
tedad= int(input())
outlist=list()
for i in range(0,tedad):
    x=float(input())
    outlist.append(math.sqrt(x))
for i in range(0,tedad):
    print("{:0.4f}".format(outlist[i]))

