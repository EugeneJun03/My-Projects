#include <iostream>

int main() {
    int arr[5] = {1, 2, 3, 4, 5}; // def array and reset as {1, 2, 3, 4, 5}

    for (int i = 0; i < 5; i++) {
        std::cout << "Element: " << arr[i] << std::endl; // index starts from 0
    }
    return 0;
}