#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Array {
public:
    int* array;
    int size;

    Array(int size, int arr[]) {
        this->size = size;
        this->array = new int[size];
        for (int i = 0; i < size; i++) {
            this->array[i] = arr[i];
        }
    }

    void display() {
        for (int i = 0; i < size; i++) {
            cout << array[i] << " ";
        }
        cout << endl;
    }

    void sortOnFrequency() {
        unordered_map<int, int> count;
        for (int i = 0; i < size; i++) {
            count[array[i]]++;
        }
        vector<pair<int, int>> freqVector;
        for (const auto& pair : count) {
            freqVector.push_back(pair);
        }
        sort(freqVector.begin(),freqVector.end(),[](pair<int,int>&a,pair<int,int>&b){
            return a.second > b.second; // Compare by frequency in descending order
        });
        int index = 0;
    for (auto& entry : freqVector) {
        int value = entry.first;
        int frequency = entry.second;
        while (frequency--) {
            array[index++] = value;
        }

        }
    }
 
};

int main() {
    int val[] = {10, 22, 9, 33, 44, 20, 22, 10, 11, 33, 9, 9, 9, 9};
    int size = sizeof(val) / sizeof(val[0]);

    Array arr2(size, val);

    cout << "Original Array: ";
    arr2.display();

    arr2.sortOnFrequency();
    cout << "Array sorted based on frequency: ";
    arr2.display();

    return 0;
}

/*
    void sortByFrequency() {
        // Use unordered_map to count frequencies of each element
        unordered_map<int, int> freqMap;

        for (int i = 0; i < size; i++) {
            freqMap[array[i]]++;
        }

        // Create a vector of pairs (value, frequency) for sorting
        vector<pair<int, int>> freqVec;
        for (const auto& pair : freqMap) {
            freqVec.push_back(pair);
        }

        // Sort the vector by frequency in descending order
        sort(freqVec.begin(), freqVec.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second; // Compare by frequency
        });

        // Rebuild the array based on the sorted frequency
        int index = 0;
        for (const auto& pair : freqVec) {
            for (int i = 0; i < pair.second; i++) {
                array[index++] = pair.first;
            }
        }
    }*/