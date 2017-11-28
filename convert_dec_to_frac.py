# Per Sandgren, Sweden, 28-11-2017
# Small program converting decimals to fractions

#import functions to check for decimal and sys to gain arguments set after executing script
from decimal import Decimal
import sys

#implementation of gcd
def gcd(a,b) :
	return_gcd = a
	rest = a % b
	if(rest != 0):
		return_gcd = gcd(a,rest)
	return return_gcd

#Read in input from user into variable dec, short for decimal, set to float
dec = float(sys.argv[1])
to_mul_with = int(len(sys.argv[1])-1)
#If input number is a decimal number, convert decimal into fraction, mod 1 on a decimal number will not return 0
if(Decimal(dec) % 1 != 0): 
	#get initial values multiplied with as many decimals there are
	top = dec*10**to_mul_with
	bottom = 10**to_mul_with
	#get gcd between top and bottom
	saved_gcd = gcd(top, bottom)
	#Divide top and bottom with gcd
	bottom = int(bottom/saved_gcd)
	top = int(top/saved_gcd)
	#print output fraction
	print(top,"/",bottom)

#If a non-decimal number has been set, just add /1 to make a fraction of it
else:
	print(int(dec),"/",1)
