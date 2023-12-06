#include <iostream>
#include <math.h>
#include <vector>
using namespace std;
void test_case();

int main(){
    test_case();
}

void primefact(int n) {
    cout << "Prime factors of " << n << " : ";
    while (n % 2 == 0)
    {
        cout << 2 << " ";
        n = n/2;
    }
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            cout << i << " ";
            n = n/i;
        }
    }
    if (n > 2)
        cout << n << ", ";
    cout << endl;
}

void test_case(){
    primefact(2);
    primefact(72);
    primefact(196);
}