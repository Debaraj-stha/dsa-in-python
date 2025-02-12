#include <iostream>
using namespace std;

void display(int array[], int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}

// Reverse a portion of the array from start index to end index
void reverse(int array[], int start, int end) {
    while (start < end) {
        swap(array[start], array[end]);
        start++;
        end--;
    }
}

void reverseToKGroup(int arr[], int n, int k) {
    for (int i = 0; i < n; i += k) {
        // Calculate correct end index (last group may have fewer elements)
        int end = min(i + k - 1, n - 1);
        reverse(arr, i, end);
    }
}

int main() {
    int arr[] = {1, 2, 8, 9, 10, 7, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    cout << "Original Array: ";
    display(arr, n);

    reverseToKGroup(arr, n, k);

    cout << "Reversed in K-Groups: ";
    display(arr, n);

    return 0;
}
