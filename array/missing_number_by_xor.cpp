#include <iostream>
using namespace std;

int findMissingNumber(int arr[], int n) {
    int X1 = 0, X2 = 0;

    // XOR of all numbers from 1 to n
    for (int i = 1; i <= n; i++) {
        X1 ^= i;
    }

    // XOR of all elements in the array
    for (int i = 0; i < n - 1; i++) {
        X2 ^= arr[i];
    }

    return X1 ^ X2; // Missing number
}

int main() {
    int arr[] = {1, 2, 4, 5}; // Missing number is 3
    int n = 5;
    
    cout << "Missing Number: " << findMissingNumber(arr, n) << endl;

    return 0;
}
