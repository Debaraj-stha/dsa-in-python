#include <iostream>
using namespace std;

#define MAX 100  // Maximum number of elements in each bucket

// Corrected Insertion Sort function
void insertionSort(float arr[], int size) {
    for (int i = 1; i < size; i++) {
        float key = arr[i];  // Corrected float type
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void bucketSort(float arr[], int n) {
    int bucketCount = 10;  // Number of buckets
    int bucketSize[bucketCount] = {0};  // Track bucket sizes
    float buckets[bucketCount][MAX];  // 2D Array for buckets

    // Step 1: Distribute elements into buckets
    for (int i = 0; i < n; i++) {
        int bucketIndex = (int)(arr[i] * bucketCount);  // Corrected type casting
        if (bucketIndex >= bucketCount) bucketIndex = bucketCount - 1;  // Prevent overflow
        buckets[bucketIndex][bucketSize[bucketIndex]++] = arr[i];  // Store element
    }

    // Step 2: Sort each bucket using Insertion Sort
    for (int i = 0; i < bucketCount; i++) {
        if (bucketSize[i] > 1) {
            insertionSort(buckets[i], bucketSize[i]);
        }
    }

    // Step 3: Merge sorted buckets into original array
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        for (int j = 0; j < bucketSize[i]; j++) {
            arr[index++] = buckets[i][j];
        }
    }
}

void displayArray(float arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    float arr[] = {0.42, 0.32, 0.52, 0.25, 0.47, 0.51, 0.90, 0.12, 0.73, 0.68};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original Array: ";
    displayArray(arr, n);

    bucketSort(arr, n);

    cout << "Sorted Array: ";
    displayArray(arr, n);

    return 0;
}
