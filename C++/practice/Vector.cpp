#include <vector>
#include <iostream>  // Added for using cout
using namespace std;

/* Functions for vector:
   1. push_back(): Appends a new element at the back of the vector
   2. size(): Returns the current size of the vector
   3. at(index): Finds the element at the given index (or you can also use "vectorname[index]")
*/

int main() {
    vector<int> v = {1, 2, 3, 4, 5};  // Declare vector "v" and initialize it with elements 1 to 5

    int a;
    cout << "Give a number that you want to add in vector(end if -1): " << endl;
    cin >> a;

    while (a != -1) {
        v.push_back(a); //Appends input=a at the back of the vector
        cout << "Give a number that you want to add in vector(end if -1): " << endl;
        cin >> a;
    }

    // Loop through the vector and print each element
    for (int i = 0; i < v.size(); i++) {
        cout << "Element " << i << ": " << v.at(i) << endl;  // Access each element by index and print it
    }
    
    return 0;  // Return 0 to indicate successful execution
}
