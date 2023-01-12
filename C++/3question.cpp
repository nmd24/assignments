#include <iostream>
using namespace std;

int main() {
int t1 = 1, t2 = 2, nextTerm = 0, n = 4000000;
cout << "Fibonacci Series: " << t1 << ", " << t2 << ", ";
nextTerm = t1 + t2;
while(nextTerm <= n) {
cout << nextTerm << ", ";
t1 = t2;
t2 = nextTerm;
nextTerm = t1 + t2;
}
}