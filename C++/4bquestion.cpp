#include <iostream>
#include <vector>
using namespace std;
void test_case();

int main(){
    test_case();
}

void fact(int n,   int factorCount = 2) {
  cout << "Required factors of " << n <<" : 1, ";
  for (int i = 2; i <= n / 2; ++i) {
    if (n % i == 0) {
      cout << i << ", ";
      ++factorCount;
    }
  }
  cout << n << endl << endl;
}

void test_case(){
    fact(2);
    fact(72);
    fact(196);
}