# Per Sandgren, Sweden, 17-11-2017
# Small program converting decimals to fractions

#import functions to check for decimal and gcd
from decimal import Decimal
from fractions import gcd
import sys

#Read in input from user into variable dec, set to float
dec = float(sys.argv[1])
#If input number is a decimal number, convert decimal into fraction, mod 1 on a decimal number will not return 0
if(Decimal(dec) % 1 != 0): 
	dec = int(dec*10000)
	saved_gcd = gcd(dec,10000)
	dec = int(dec*0.001)
	print(dec, "/", (saved_gcd))
#If a non-decimal number has been set, just add /1 to make a fraction of it
else:
	print(int(dec),"/",1)
