#include <iostream>
using namespace std;

int main() {
    int age;
    double height;
    
    cout << "Enter your age and height: ";
    cin >> age >> height;  // 공백으로 구분된 두 값을 입력받음
    
    cout << "You are " << age << " years old and " << height << " meters tall." << std::endl;
    return 0;
}