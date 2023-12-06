#include <iostream>
#include <string>
using namespace std;

int main() {
int number; char *output;

cout << "Enter the number: ";
cin >> number;

if (number == -1) {
output = "negative one";
} else if (number == 0) {
output = "zero";
} else if (number == 1) {
output = "positive one";
} else {
output = "other value";
}

// Print the results
cout << "Entered value is: " << output << endl;
return 0;
}