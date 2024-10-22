#include <iostream>

int main() {
    // Declare and initialize the array
    int arr[5] = {1, 2, 3, 4, 5}; 

    // Print the initial array elements
    std::cout << "Initial array elements: " << std::endl;
    for (int i = 0; i < 5; i++) {
        std::cout << "Element: " << arr[i] << std::endl;  // index starts from 0
    }

    // Get 5 numbers from the user
    std::cout << "Give 5 numbers: " << std::endl;
    for (int j = 0; j < 5; j++) {
        std::cin >> arr[j];
    }

    // Find the maximum number
    int Max_num = arr[0];  // Initialize the max value with the first element
    for (int k = 1; k < 5; k++) {
        if (arr[k] > Max_num) {  // If current element is greater than max, update max
            Max_num = arr[k];
        }
    }

    // Print the maximum number
    std::cout << "The maximum number is: " << Max_num << std::endl;

    return 0;  // Return 0 to indicate successful execution
}
