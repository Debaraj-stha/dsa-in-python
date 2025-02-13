#include<iostream>
#include<vector>
#include<climits>  // For INT_MAX

using namespace std;

void display(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sort(vector<vector<int>>& PerSum) {
    for (int i = 0; i < PerSum.size(); i++) {
        for (int j = 0; j < PerSum.size() - i - 1; j++) {
            if (PerSum[j][0] > PerSum[j + 1][0]) {
                swap(PerSum[j], PerSum[j + 1]);
            }
        }
    }
}

int findIndex(vector<vector<int>>& PerSum, int val) {
    int l = 0;
    int r = PerSum.size() - 1;
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (PerSum[mid][0] >= val) {
            r = mid;
        } else {
            l = mid + 1; 
        }
    }
    return PerSum[l][0] == val ? l : -1;
}

int findMinimumSubArray(int* arr, int n, int X) {
    int result = INT_MAX;
    int sum = 0;
    vector<vector<int>> PerSum;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
        PerSum.push_back({sum, i});
    }
    sort(PerSum);

    vector<int> minIndex(n);
    minIndex[0] = PerSum[0][1]; 

    // Populate minIndex array
    for (int i = 1; i < n; i++) {
        minIndex[i] = min(minIndex[i - 1], PerSum[i][1]);
    }

    sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
        if (sum < X) {
            result = min(result, i + 1); 
        } else {
            int ind = findIndex(PerSum, sum - X - 1);
            if (ind != -1 && minIndex[ind] < i) {
                result = min(result, i - minIndex[ind]);
            }
        }
    }

    return result == INT_MAX ? -1 : result;  // Return -1 if no subarray is found
}

int main() {
    int arr[] = {2, -3, 3, 2, 0, -1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    display(arr, n);
    cout << "Smallest subarray having sum less than " << k << " = " << findMinimumSubArray(arr, n, k) << endl;

    return 0;
}
