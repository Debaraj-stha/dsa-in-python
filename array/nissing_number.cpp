#include <iostream>
#include <vector>
using namespace std;

int findMissingNumber(const vector<int>& arr) {
    int low = 0, high = arr.size() - 1;
    
    // Apply binary search
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        // Check if the current element is in the expected position
        if (arr[mid] == mid + 1) {
            low = mid + 1;  // Missing number is to the right
        } else {
            high = mid - 1; // Missing number is to the left
        }
    }

    // The missing number is at the `low` index (1-based)
    return low + 1;
}

int main() {
    vector<int> arr = {1, 2, 7, 8, 9, 10};
    
    cout << "Missing number: " << findMissingNumber(arr) << endl;
    
    return 0;
}
