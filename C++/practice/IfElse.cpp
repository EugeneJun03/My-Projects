#include <iostream>
using namespace std;
/*if-else statement structure
if ("Conditional statement") {
    "Command statement"
} else if ("Conditional statement") {
    "Command statement"
} else ("Conditional statement") {
    "Command statement"
*/

int main() {
    int score; // Define Vriable
    cout << "Enter yout score: ";
    cin >> score; // getting input

    // The if-else statement has very similar structure
    if (score >= 90) {
        cout << "Grade: A" << endl;
    } else if (score >= 80) {
        cout << "Grade: B" << endl;
    } else if (score >= 70) {
        cout << "Grade: C" << endl;
    } else {
        cout << "Grade: F" << endl;
    }

    return 0;
}