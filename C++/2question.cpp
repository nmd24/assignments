#include <iostream>
#include <vector>
using namespace std;

void print(vector<int> const &input)
{
for (auto it = input.cbegin(); it != input.cend(); it++) {
cout << *it << ' ';
}
}

int main()
{
vector<int> input = { 1, 2, 3, 4, 5 };
print(input);
}