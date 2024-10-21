#include <iostream>
using namespace std;
// Same as in python

int add(int a, int b) {
    return a + b;
}

int duble(int a) {
    return a*2;
}

int main() {
    int a,b;

    cout << "Double the sum of the two: " << endl;
    cin >> a >> b;

    cout << "It is " << duble(add(a,b));
    return 0;
}
