#include <iostream>
#include <vector>
using namespace std;

void display(vector<int> arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

void backtrack(int i, int j, int arr[], vector<int>& subset, bool** dp, vector<vector<int>>& allSubsets) {
    if (j == 0) {
        allSubsets.push_back(subset);
        return;
    }
    if (i == 0) {
        return;
    }
    if (dp[i - 1][j]) {
        backtrack(i - 1, j, arr, subset, dp, allSubsets);
    }
    if (j >= arr[i - 1] && dp[i - 1][j - arr[i - 1]]) {
        subset.push_back(arr[i - 1]);
        backtrack(i - 1, j - arr[i - 1], arr, subset, dp, allSubsets);
        subset.pop_back();
    }
}

bool** subsetSumToTarget(int n, int target, int arr[]) {
    bool** dp = new bool*[n + 1];
    for (int i = 0; i <= n; i++) {
        dp[i] = new bool[target + 1]{false};
    }
    
    for (int i = 0; i <= n; i++) {
        dp[i][0] = true;  // Base case: sum of 0 is always possible
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= target; j++) {
            if (arr[i - 1] <= j) {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp;
}

int sum(int arr[], int n) {
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}

void partition(int n, int arr[]) {
    int s = sum(arr, n);
    if (s % 2 != 0) {
        cout << "Cannot be partitioned into two subsets with equal sum." << endl;
        return;
    }
    
    int target = s / 2;
    bool** dp = subsetSumToTarget(n, target, arr);

    if (dp[n][target]) {
        vector<vector<int>> allSubset1,allSubset2;
        vector<int> subset1,subset2;
        backtrack(n, target, arr, subset1, dp, allSubset1);
        backtrack(n, s - target, arr, subset2, dp, allSubset2);

        for(size_t i = 0; i < allSubset1.size();i++){
            cout << "Subset 1: ";
            display(allSubset1[i]);
            cout << "Subset 2: ";
            display(allSubset2[i]);
            cout << endl;
        }
        
    } else {
        cout << "No valid partition found." << endl;
    }

    // Free allocated memory
    for (int i = 0; i <= n; i++) {
        delete[] dp[i];
    }
    delete[] dp;
}

int main() {
    int arr[] = {1, 5, 5, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    partition(n, arr);
    
    return 0;
}
