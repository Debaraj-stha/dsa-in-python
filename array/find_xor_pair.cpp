#include <iostream>
#include <unordered_set>
using namespace std;

void findPairWithXOR(int arr[], int n, int X) {
    unordered_set<int> seen;
    for (int i = 0; i < n; i++) {
        int b = arr[i] ^ X; // Find required pair
        if (seen.find(b) != seen.end()) {
            cout << "Pair found: (" << arr[i] << ", " << b << ")\n";
            return;
        }
        seen.insert(arr[i]); // Store in hash set
    }
    cout << "No pair found\n";
}

int main() {
    int arr[] = {3, 10, 5, 6, 2, 8};
    int X = 5;
    int n = sizeof(arr) / sizeof(arr[0]);
    
    findPairWithXOR(arr, n, X);

    return 0;
}
