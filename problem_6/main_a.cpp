#include <iostream>
#include "./source/factorial/factorial.h"
#include "./source/prime/ifprime.h"


using namespace std;
int main()
{
	string res;
	res = isPrime(17) ? "True" : "False";
	cout << "Factorial(10) = " << findFactorial(10) << endl;
	cout << "isPrime(17) = " << res << endl;
}