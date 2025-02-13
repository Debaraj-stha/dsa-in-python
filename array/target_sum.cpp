#include <iostream>
#include <vector>
using namespace std;

void display(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Backtracking function to find subset elements
void backtrack(int i, int j, int arr[], vector<int> &subset, vector<vector<bool>> &dp,vector<vector<int>> &allSubsets) {
    if (j == 0) {
        allSubsets.push_back(subset);
        return;
    }
    if (i == 0) {
        return;
    }
    
    // If excluding the current element results in the same sum, move up
    if (dp[i - 1][j]) {
        backtrack(i - 1, j, arr, subset, dp,allSubsets);
    }
    // If including the current element is valid, add it to the subset
    if (j >= arr[i - 1] && dp[i - 1][j - arr[i - 1]]) {
       subset.push_back(arr[i - 1]);
        backtrack(i - 1, j - arr[i - 1], arr, subset, dp, allSubsets);
        subset.pop_back();  // Backtrack to remove the last elem
    }
}

void subarrayWithTargetSum(int arr[], int n, int target) {
    vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

    // Initialize DP table
    for (int i = 0; i <= n; i++) {
        dp[i][0] = true;  // Sum of 0 is always possible with an empty subset
    }

    // DP logic
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= target; j++) {
            if (arr[i - 1] <= j) {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - arr[i - 1]];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << (dp[n][target] ? "Yes" : "No") << endl;
    
          if (dp[n][target]) {
        vector<int> subset;
        vector<vector<int>> allSubsets;
        backtrack(n, target, arr, subset, dp, allSubsets);
        
        cout << "Subsets forming sum " << target << ":\n";
        for (const auto &sub : allSubsets) {
            for (int num : sub) {
                cout << num << " ";
            }
            cout << endl;
        }
    }


    
}

int main() {
    int arr[] = {1, 2, 5, -1, 8, 3, 11, 7, 4, 6, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    display(arr, n);
    subarrayWithTargetSum(arr, n, 11);
    return 0;
}
