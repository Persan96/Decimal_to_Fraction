# Per Sandgren, Sweden, 17-11-2017
# Small program converting decimals to fractions

#import functions to check for decimal and gcd
from decimal import Decimal
from fractions import gcd
import sys

#Read in input from user into variable dec, set to float
dec = float(sys.argv[1])
tomulwith = int(len(sys.argv[1])-1)
print("initial: ",dec, tomulwith)
#If input number is a decimal number, convert decimal into fraction, mod 1 on a decimal number will not return 0
if(Decimal(dec) % 1 != 0): 
	#get initial values multiplied with as many decimals there are
	top = dec*10**tomulwith
	bottom = 10**tomulwith
	print("multiplication: ", top, bottom)
	#get gcd between top and bottom
	saved_gcd = gcd(top, bottom)
	print(saved_gcd)
	#Divide top and bottom with gcd
	bottom = int(bottom/saved_gcd)
	top = int(top/saved_gcd)
	#implement checker to simplify if too long number
	print(top,"/",bottom)
#If a non-decimal number has been set, just add /1 to make a fraction of it
else:
	print(int(dec),"/",1)
