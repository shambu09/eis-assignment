#include  "factorial.h"

long long findFactorial(int i)
{
	if (i <= 1)
		return 1;
	else
		return i * findFactorial(i - 1);
}