#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>
using namespace std;

void display(const vector<int>& arr) {
    for (int a : arr) {
        cout << a << " ";
    }
    cout << endl;
}

// Function to find all subarrays with sum zero
void subArrayWithZeroSum(vector<int>& arr) {
    unordered_map<int, vector<int>> sumMap;
    vector<vector<int>> subArrays;
    int currentSum = 0;

    // Insert a base case to handle full subarrays summing to zero
    sumMap[0].push_back(-1); 

    for (int i = 0; i < arr.size(); i++) {
        currentSum += arr[i];

        // If the sum has been seen before, it means the subarray in between has sum zero
        if (sumMap.find(currentSum) != sumMap.end()) {
            for (int startIdx : sumMap[currentSum]) {
                vector<int> temp(arr.begin() + startIdx + 1, arr.begin() + i + 1);
                subArrays.push_back(temp);
            }
        }
        // Store index for this sum
        sumMap[currentSum].push_back(i);
    }

    // Display results
    for (const auto& sub : subArrays) {
        display(sub);
        cout << "Sum: " << accumulate(sub.begin(), sub.end(), 0) << endl;
        cout << "---------\n";
    }
}

int main() {
    vector<int> arr = {1, 2, -3, 3, -3, 12, 17, -17, 18, 90, 9, -9};
    display(arr);
    subArrayWithZeroSum(arr);
    return 0;
}
