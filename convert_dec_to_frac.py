# Per Sandgren, Sweden, 17-11-2017
# Small program converting decimals to fractions

#import functions to check for decimal and gcd
from decimal import Decimal
from fractions import gcd

#Read in input from user
dec = float(input("Insert decimal number: "))
#If input number is a decimal number, convert decimal into fraction, mod 1 on a decimal number will not return 0
if(Decimal(dec) % 1 != 0): 
	dec = int(dec*100)
	saved_gcd = gcd(dec,100)
	dec = dec/saved_gcd
	print(dec, "/", (100/saved_gcd))
#If a non-decimal number has been set, just add /1 to make a fraction of it
else:
	print(int(dec),"/",1)
