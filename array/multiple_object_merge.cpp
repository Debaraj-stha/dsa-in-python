#include <iostream>
using namespace std;

class Array {
    int size;
    int* array;

public:
    // Constructor
    Array(int size, int* arr) {
        this->size = size;
        this->array = new int[size];
        for (int i = 0; i < size; i++) {
            this->array[i] = arr[i];
        }
    }

    // Copy Constructor
    Array(const Array& other) {
        size = other.size;
        array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = other.array[i];
        }
    }

    // Destructor
    ~Array() {
        delete[] array;
    }

    // Function to merge two arrays
    Array mergeArrays(const Array& other) {
        int newSize = size + other.size;
        int* mergedArray = new int[newSize];

        // Copy elements from the first array
        for (int i = 0; i < size; i++) {
            mergedArray[i] = array[i];
        }

        // Copy elements from the second array
        for (int i = 0; i < other.size; i++) {
            mergedArray[size + i] = other.array[i];
        }

        return Array(newSize, mergedArray);
    }

    // Variadic template function to merge multiple arrays
    template <typename... Args>
    Array mergeArrays(const Array& first, const Args&... rest) {
        Array merged = this->mergeArrays(first);
        return merged.mergeArrays(rest...);
    }
    

    // Base case for recursion (if only one array is passed)
    Array mergeArrays() {
        return *this;
    }

    // Display function
    void display() {
        for (int i = 0; i < size; i++) {
            cout << array[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    int arr1[] = {1, 2};
    int arr2[] = {3, 4};
    int arr3[] = {5, 6};
    int arr4[] = {7, 8, 9};

    Array array1(2, arr1);
    Array array2(2, arr2);
    Array array3(2, arr3);
    Array array4(3, arr4);

    cout << "Array 1: ";
    array1.display();
    cout << "Array 2: ";
    array2.display();
    cout << "Array 3: ";
    array3.display();
    cout << "Array 4: ";
    array4.display();

    // Merging multiple arrays dynamically
    Array mergedArray = array1.mergeArrays(array2, array3, array4);

    cout << "Merged Array: ";
    mergedArray.display();

    return 0;
}
