#include <iostream>

int main() {
    int row= 10;

    // Double for statement
    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl; // change line
    }
    return 0;

}