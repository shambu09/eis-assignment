#include <dlfcn.h>
#include <iostream>

using namespace std;
int main()
{
	string res;
	cout << "Opening A.so..." << endl;
	cout << "Opening B.so..." << endl;
	cout << "libraries loaded into memory." << endl << endl;

	void* handle_fact  = dlopen("./source/factorial/libs/A.so", RTLD_LAZY);
	void* handle_prime = dlopen("./source/prime/libs/B.so", RTLD_LAZY);

	typedef long long (*factFunc_type)(int);
	typedef bool (*primeFunc_type)(long);

	cout << "function pointers are assigned with addresses of functions loaded "
			"in memory." << endl << endl;

	factFunc_type findFactorial = (factFunc_type)dlsym(handle_fact, "findFactorial");
	primeFunc_type isPrime = (primeFunc_type)dlsym(handle_prime, "isPrime");

	res = isPrime(17) ? "True" : "False";
	cout << "Factorial(10) = " << findFactorial(10) << endl;
	cout << "isPrime(17) = " << res << endl << endl;

	dlclose(handle_fact);
	dlclose(handle_prime);

	cout << "function pointers are equal to nullptrs now, as the libraries are "
			"offloaded from the memory." << endl;
	cout << "Fact(10) = " << findFactorial(10) << endl;
	cout << "isPrime(17) = " << isPrime(17) << endl;
}