#include <iostream>
#include <vector>
using namespace std;

vector<int> findEquilibriumIndices(vector<int>& arr) {
    vector<int> result;
    int totalSum = 0, leftSum = 0;
    for (int num : arr) {
        totalSum += num;
    }
    for (int i = 0; i < arr.size(); i++) {
        // If leftSum == rightSum, store index
        if (leftSum == totalSum - leftSum - arr[i]) {
            result.push_back(i);
        }
        leftSum += arr[i];
    }

    return result;
}

int main() {
    vector<int> arr = {-7, 1, 5, 2, -4, 3, 0};
    vector<int> equilibriumIndices = findEquilibriumIndices(arr);

    cout << "Equilibrium indices: ";
    for (int index : equilibriumIndices) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}
