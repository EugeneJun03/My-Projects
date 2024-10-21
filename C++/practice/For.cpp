#include <iostream>

int main() {
    // Increase
    for (int i = 1; i <= 5; i++) {
        std::cout << "Count: " << i << std::endl;
    }

    std::cout << "---------"<< std::endl;
    
    // Decrease
    for (int i = 5; i >= 1; i--) {  // 조건을 i >= 1로 수정
        std::cout << "Count: " << i << std::endl;
    }

    return 0;
}
