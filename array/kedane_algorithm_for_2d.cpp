#include <iostream>
#include <vector>
#include <climits> // For INT_MIN

using namespace std;

// Kadane's algorithm to find maximum subarray sum
int kadane(vector<int>& arr, int& start, int& end, int n) {
    int maxSum = INT_MIN, sum = 0;
    int tempStart = 0;
    start = 0;
    end = -1;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
        if (sum > maxSum) {
            maxSum = sum;
            start = tempStart;
            end = i;
        }
        if (sum < 0) {
            sum = 0;
            tempStart = i + 1;
        }
    }
    return maxSum;
}


// Function to find the maximum sum submatrix
void maxSumSubmatrix(int** arr, int rows, int cols) {
    int maxSum = INT_MIN;
    int finalLeft, finalRight, finalTop, finalBottom;

    // Iterate over all possible pairs of rows
    for (int top = 0; top < rows; top++) {
        vector<int> temp(cols, 0);

        for (int bottom = top; bottom < rows; bottom++) {
            // Sum up the elements column-wise
            for (int col = 0; col < cols; col++) {
                temp[col] += arr[bottom][col];
            }

            // Apply Kadane's algorithm on this 1D array
            int start, end;
            int sum = kadane(temp, start, end, cols);

            if (sum > maxSum) {
                maxSum = sum;
                finalTop = top;
                finalBottom = bottom;
                finalLeft = start;
                finalRight = end;
            }
        }
    }

    // Print result
    cout << "Maximum Sum: " << maxSum << endl;
    cout << "Top Left: (" << finalTop << ", " << finalLeft << ")" << endl;
    cout << "Bottom Right: (" << finalBottom << ", " << finalRight << ")" << endl;
}

int main() {
    int rows = 3, cols = 3;
    int** arr = new int*[rows];
    arr[0] = new int[cols]{1, 3, -4};
    arr[1] = new int[cols]{2, 5, 6};
    arr[2] = new int[cols]{7, 8, 9};

    maxSumSubmatrix(arr, rows, cols);

    // Free memory
    for (int i = 0; i < rows; i++) {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}
