#include <iostream>
// It's same as python

int main() {
    int i = 1;

    while (i <= 10) {
        std::cout << "Count: " << i << std::endl;
        i += 2; // Increase 2 every loop(you can increase 1 by "i++;")
    }
}