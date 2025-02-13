#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
void display(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

template <typename... Args>
void merge(const Args&... args) {
    vector<int> mergedArr;
    
    // Expand each array and insert its elements into mergedArr
    (mergedArr.insert(mergedArr.end(), args.begin(), args.end()), ...);

    cout << "Before Sorting: ";
    display(mergedArr);

    sort(mergedArr.begin(), mergedArr.end());

    cout << "After Sorting: ";
    display(mergedArr);
}

int main() {
    vector<int> arr1 = {1, 2, 3, 4, 5};
    vector<int> arr2 = {10, 15, 20, 25};
    vector<int> arr3 = {5, 19, 23, 332, 93};
    vector<int> arr4 = {-5, -2, -10, -15};

    merge(arr1, arr2, arr3, arr4); 

    return 0;
}
