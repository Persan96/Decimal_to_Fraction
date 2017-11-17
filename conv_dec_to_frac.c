#include <stdin.h>
#include <stdio>

int gcd(int a, int b){
	if(a < b)
		gcd(a, b-a);
	else if(b < a)
		gcd(a-b, b)
	else
		return a;
}

int main(int argc, char *argv[])
{
	float dec = float(argv[1]);
	if(dec % 1 != 0)
	{
		int(dec) = int(dec*100);
		int saved_gcd = gcd(dec,100);
		printf("%d/%d\n",(dec/saved_gcd),(100/saved_gcd));
	}
	else
		printf("%d/1\n", dec);

	return 0;
}