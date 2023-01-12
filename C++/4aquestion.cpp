#include <iostream>
using namespace std;

bool isprime(int number){
if(number < 2) return false;
if(number == 2) return true;
if(number % 2 == 0) return false;
for(int i=3; (i*i)<=number; i+=2){
if(number % i == 0 ) return false;
}
return true;
}

void test_isprime() {
cout << "isprime(2) = " << isprime(2) << '\n';
cout << "isprime(10) = " << isprime(10) << '\n';
cout << "isprime(17) = " << isprime(17) << '\n';
}

int main() {
test_isprime();
}