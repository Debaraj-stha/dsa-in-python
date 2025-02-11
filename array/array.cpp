#include <iostream>
#include <math.h>
#include <climits>
#include<set>
struct Partition
{
    int *firstPart;
    int firstSize;
    int *secondPart;
    int secondSize;
};

using namespace std;

class Array
{
    int size;
    int *array; // Pointer to store dynamically allocated array

public:
    // Constructor with size parameter
    Array(int size, int *values)
    {
        this->size = size;
        array = new int[size]; // Allocate an array
        assignValues(values);
        cout << "Array of size " << size << " is initialized" << endl;
    }
    Array(int size)
    {
        this->size = size;
        array = new int[size]; // Allocate an array

        cout << "Array of size " << size << " is initialized" << endl;
    }
    // Copy constructor
    Array(const Array &other)
    {
        size = other.size;
        array = new int[size]; // Allocate memory for new array
        assignValues(other.array);
        cout << "Array copied from another array" << endl;
    }
Array(int* inputArr, int n) : size(n) {
        array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = inputArr[i];
        }
    }
    Array(int *values)
    {
        this->size = 10;
        array = new int[10]; // Allocate an array
        assignValues(values);
        cout << "Array of size " << size << " is initialized" << endl;
    }

    // Default constructor
    Array()
    {
        this->size = 10;
        array = new int[size]; // Allocate array with default size
        cout << "Default array of size " << size << " is initialized" << endl;
    }

    // Destructor
    ~Array()
    {
        delete[] array; // Deallocate memory
        cout << "Array memory freed" << endl;
    }

    // return size of the array
    int getSize()
    {
        return size;
    }

    // return array
    int *getArray()
    {
        return array;
    }
    // print array items
    void display()
    {
        for (int i = 0; i < size; i++)
        {
            cout << array[i] << " ";
        }
        cout << endl;
    }
    void assignValues(int *values)
    {
        for (int i = 0; i < size; i++)
        {
            array[i] = values[i];
        }
    }
    // Set array item
    int setValue(int index, int value)
    {
        if (index >= 0 && index < size)
        {
            array[index] = value;
            return 1;
        }
        else
        {
            cout << "Invalid index" << endl;
            return 0;
        }
    }

    // returns index of next empty index
    static int nextEmptyIndex(int *array, int size)
    {
        for (int i = 0; i < size; i++)
        {
            if (array[i] == 0)
            {
                return i;
            }
        }
        return -1; // No unfilled location found
    }
    int getItem(int index)
    {
        if (index >= 0 && index < size)
        {
            return array[index];
        }
        else
        {
            cout << "Invalid index" << endl;
            return -1; // Invalid index
        }
    }
    // Add an item to the array
    int add(int value)
    {
        try
        {
            int index = nextEmptyIndex(array, size);
            if (index != -1)
            {
                array[index] = value;
                return 1;
            }
            else
            {
                cout << "Array is full" << endl;
                return 0;
            }
        }
        catch (exception &e)
        {
            cerr << "Exception: " << e.what() << endl;
            return 0; // Exception occurred during array operation
        }
    }
    // Remove an item from the array
    int remove(int value)
    {
        int isArrayEmpty = nextEmptyIndex(array, size);
        // 0 means first empty index which is empty
        if (isArrayEmpty == 0)
        {
            cout << "Array is empty" << endl;
            return 0;
        }
        for (int i = 0; i < size; i++)
        {
            if (array[i] == value)
            {
                array[i] = 0;
                return 1;
            }
        }
        cout << "Item not found in array" << endl;
        return 0;
    }
    int removeAt(int index)
    {
        try
        {
            if (index >= 0 && index < size)
            {
                array[index] = 0;
                return 1;
            }
            return 0;
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << '\n';
            return 0;
        }
    }
    int insertAt(int index, int value)
    {
        if (index < 0)
        {
            cout << "Invalid index!" << endl;
            return 0;
        }
        if (index >= size)
        {
            resize(index + 1, size, array);
        }

        int nextFreeIndex = nextEmptyIndex(array, size);
        if (nextFreeIndex == -1)
        {
            cout << "Array is full!" << endl;
            return 0;
        }

        if (array[index] == 0)
        {
            array[index] = value;
            return 1;
        }

        // Shift elements to the right
        for (int i = nextFreeIndex; i > index; i--)
        {
            array[i] = array[i - 1];
        }
        array[index] = value;
        return 1;
    }
    int index(int value)
    {
        for (int i = 0; i < size; i++)
        {
            if (array[i] == value)
            {
                return i;
            }
        }
        return -1; // Item not found in array
    }
    int deleteValues(int *values, int noOfItem)
    {
        int count = 0;

        for (int i = 0; i < noOfItem; i++)
        {
            int indexOfItem = index(values[i]);
            if (indexOfItem != -1)
            {
                removeAt(indexOfItem);
                count++;
            }
        }
        return count;
    }

    int findMax()
    {
        int max = array[0];
        for (int i = 1; i < size; i++)
        {
            if (array[i] > max)
            {
                max = array[i];
            }
        }
        return max;
    }
    int findMin()
    {
        int min = array[0];
        for (int i = 1; i < size; i++)
        {
            if (array[i] < min)
            {
                min = array[i];
            }
        }
        return min;
    }
    int sum()
    {
        int sum = 0;
        for (int i = 0; i < size; i++)
        {
            sum += array[i];
        }
        return sum;
    }
    double average()
    {
        int s = sum();
        return static_cast<double>(s) / size;
    }

    int isSorted(int *values, int n, string order = "")
    {
        if (n == 1)
        {
            return 1;
        }
        if (order == "")
        {
            if (values[0] < values[1])
            {
                order = "asc";
            }
            else if (values[0] > values[1])
            {
                order = "desc";
            }
        }

        if (order == "asc")
        {
            if (values[n - 2] > values[n - 1])
            {
                return 0;
            }
        }
        else if (order == "desc")
        {
            if (values[n - 2] < values[n - 1])
            {
                return 0;
            }
        }

        return isSorted(values, n - 1, order);
    }

    // Partition function
    int partition(int p, int r)
    {
        int x = array[r];
        int i = p - 1;
        for (int j = p; j <= r - 1; j++)
        {
            if (array[j] <= x)
            {
                i++;
                swap(&array[i], &array[j]);
            }
        }
        swap(&array[i + 1], &array[r]);
        return (i + 1);
    }

    // QuickSort function
    void quickSort(int p, int r)
    {
        int sorted = isSorted(array, size);
        ;
        if (p < r)
        {
            int q = partition(p, r);
            quickSort(p, q - 1);
            quickSort(q + 1, r);
        }
    }

    // Swap function
    void swap(int *a, int *b)
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }

    // clear array
    void clearArray()
    {
        for (int i = 0; i < size; i++)
        {
            setValue(i, 0);
        }
    }

    static int *resize(int newSize, int oldSize, int *array)
    {
        int *newArray = new int[newSize];
        for (int i = 0; i < (newSize < oldSize ? newSize : oldSize); i++)
        {
            newArray[i] = array[i];
        }
        delete[] array;
        array = newArray;
        oldSize = newSize;
        cout << "Array resized to " << newSize << endl;
        return newArray;
    }

    int itemAt(int index)
    {
        if (index >= 0 && index < size)
        {
            return array[index];
        }
        return -1;
    }

    double findMedian()
    {

        if (!isSorted(array, size))
        {
            quickSort(0, size - 1);
        }

        int mid = size / 2;
        if (size % 2 == 0)
        {
            return (array[mid - 1] + array[mid]) / 2;
        }
        return array[mid];
    }
    // check if array contains any duplicates
    int isDuplicates()
    {
        for (int i = 0; i < size - 1; i++)
        {
            if (array[i] == array[i + 1])
            {
                return 1;
            }
        }
        return 0;
    }

    // count occurrences of the specified element
    int countOccurrences(int value)
    {
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == value)
            {
                count++;
            }
        }
        return count;
    }

    // find the mode
    int findMode()
    {
        if (!isSorted(array, size))
        {
            quickSort(0, size - 1);
        }
        int maxCount = 0;
        int mode = array[0];
        for (int i = 0; i < size - 1; i++)
        {
            if (array[i] == array[i + 1])
            {
                int count = countOccurrences(array[i]);
                if (count > maxCount)
                {
                    maxCount = count;
                    mode = array[i];
                }
            }
        }
        return mode;
    }
    // fill the array with   value
    int fill(int value)
    {

        for (int i = 0; i < size; i++)
        {
            setValue(i, value);
        }
        return 1;
    }
    int *getDuplicate()
    {
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == array[i + 1])
            {
                count++;
            }
        }
        int *duplicates = new int[count];
        int index = 0;
        for (int i = 0; i < size - 1; i++)
        {
            if (array[i] == array[i + 1])
            {
                duplicates[index] = i;
                count++;
            }
        }
        return duplicates;
    }
    // count duplicates
    int countDuplicates()
    {
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == array[i + 1])
            {
                count++;
            }
        }
        return count;
    }

    // remove duplicates
    int removeDuplicates()
    {
        if (size == 0 || size == 1)
        {
            return 1;
        }
        if (!isSorted(array, size))
        {
            quickSort(0, size - 1); // sort array before removing duplicates
        }
        if (!isDuplicates())
        {
            return 1;
        }
        int count = 0;
        for (int i = 0; i < size - 1; i++)
        {
            if (array[i] != array[i + 1])
            {
                array[count] = array[i];
                count++;
            }
        }
        return count;
    }

    // find the second largest element
    int findSecondLargest()
    {
        if (!isSorted(array, size))
        {
            quickSort(0, size - 1);
        }
        if (size < 2)
        {
            return -1;
        }
        return array[size - 2];
    }

    int *copy()
    {
        int *newArray = new int[size];
        for (int i = 0; i < size; i++)
        {
            newArray[i] = array[i];
        }
        return newArray;
    }

    int *getSubarray(int start = 0, int end = 0)
    {
        if (start < 0 or end > size)
        {
            cout << "Invalid start or end index" << endl;
            return nullptr;
        }
        int newSize = end - start + 1;
        int *newArray = new int[newSize];
        for (int i = start; i < end; i++)
        {
            newArray[i] = array[i];
        }

        return newArray;
    }
    bool isEmpty()
    {
        return size == 0;
    }
    void suffle()
    {
        srand(time(0));
        for (int i = 0; i < size; i++)
        {
            int j = rand() % size;
            swap(&array[i], &array[j]);
        }
    }
    // merge array and return new Array instance
    Array merge(Array &other)
    {
        int newSize = size + other.getSize();
        int *newArray = new int[newSize];
        for (int i = 0; i < size; i++)
        {
            newArray[i] = array[i];
        }
        for (int i = 0; i < other.getSize(); i++)
        {
            int emptyIndex = nextEmptyIndex(newArray, newSize);
            newArray[emptyIndex] = other.array[i];
        }

        return Array(newSize, newArray);
    }
    // count the number of null value
    int countNull()
    {
        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == 0)
            {
                count++;
            }
        }
        return count;
    }
    // return aray of null indices
    int *getNull()
    {
        if (nextEmptyIndex(array, size) == -1)
        {
            return nullptr;
        }

        int count = 0;
        for (int i = 0; i < size; i++)
        {
            if (array[i] == 0)
            {
                count++;
            }
        }

        if (count == 0)
        {
            return nullptr;
        }
        cout << "count = " << count << endl;

        int *newArray = new int[count]; // Allocate only necessary memory
        int index = 0;

        for (int i = 0; i < size; i++)
        {
            if (array[i] == 0)
            {
                newArray[index++] = i;
            }
        }
        cout << "index=" << index;

        return newArray;
    }

    void fillNull(string fillby = "", int value = 1)
    {
        int *nullIndices = getNull();
        if (!nullIndices)
        {
            cout << "No null values found" << endl;
            return;
        }
        int count = countNull();
        for (int i = 0; i < count; i++)
        {
            if (fillby == "mode")
            {
                int mode = findMode();
                setValue(nullIndices[i], mode);
            }
            else if (fillby == "median")
            {
                int median = findMedian();
                setValue(nullIndices[i], median);
            }
            else
            {
                setValue(nullIndices[i], value);
            }
        }
        delete[] nullIndices;
    }
    // return reference of item at given index
    int *getReferenceOfItemAt(int index)
    {
        if (index >= 0 && index < size)
        {
            return &array[index]; // Returning a reference
        }
        else
        {
            throw out_of_range("Invalid index"); // Throw an exception for invalid indices
        }
    }

    // reverse element
    void reverse(int reverseUntil)
    {
        try
        {
            for (int i = 0; i < reverseUntil / 2; i++)
            {
                swap(&array[i], &array[reverseUntil - i - 1]);
            }
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << '\n';
        }
    }
    void rotate(int k)
    {
        try
        {
            int lastInsertPos = nextEmptyIndex(array, size); // Find actual size of array
            k = k % lastInsertPos;                           // Avoid unnecessary rotations
            if (k < 0)
                k += lastInsertPos; // Handle negative rotations

            // Step 1: Reverse the entire array
            reverse(lastInsertPos);
            // Step 2: Reverse the first k elements
            reverse(k);
            // Step 3: Reverse the remaining elements
            reverse(lastInsertPos - k);
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << '\n';
        }
    }

    // calculate cumulative sum
    int cumulativeSum();
    int cumulativeProduct();
    int binarySearch(int target, int low, int high);
    int gcdOfAllelements();
    int lcmOfAllElements();
    int missingNumber(int low, int high);
    bool isPalindrome();
    double variance();
    double standardDeviation();
    bool isArithmetic();
    bool isGeometric();
    int *getPeaks();
    int *valleys();
    int peakCount();
    int valleyCount();
    int *maxmin_within(int start, int end);
    Partition partitionAt(int index);
     Array getUnion(Array& other) {
        std::set<int> unionSet;
        for (int i = 0; i < size; i++) {
            unionSet.insert(array[i]);
        }
        for (int i = 0; i < other.getSize(); i++) {
            unionSet.insert(other.getArray()[i]);
        }

        int* resultArr = new int[unionSet.size()];
        int index = 0;
        for (int num : unionSet) {
            resultArr[index++] = num;
        }

        return Array(resultArr, unionSet.size());
    }
    Array getIntersetion(Array&other){
        std::set<int> setA(array,array+size);
        set<int> intersectionSet;
        for(int i=0;i<other.getSize();i++) {
            if(setA.find(other.array[i])!= setA.end()) {
                intersectionSet.insert(other.array[i]);
            }
        }
        int* resultArr = new int[intersectionSet.size()];
        int index = 0;
        for(int arr:intersectionSet){
            resultArr[index++]=arr;
        }
        return Array(resultArr, intersectionSet.size());
    }
};
// Implementation of member functions
 
inline Partition Array::partitionAt(int index)
{
     if (index < 0 || index >= size) {
        Partition p=Partition();
        p.firstPart=nullptr;
        p.secondPart=nullptr;
        p.firstSize=0;
        p.secondSize=0;
        return p; // Handle invalid index
        }
    int* firstpart=new int[index];
    int* secondpart=new int[size-index];
    for(int i=0; i<index; i++){
        firstpart[i]=array[i];
    }
    for(int i=index; i<size; i++){
        secondpart[i-index]=array[i];
    }
    Partition p=Partition();
    p.firstPart=firstpart;
    p.secondPart=secondpart;
    p.firstSize=index;
    p.secondSize=size-index;
    return p;
}

inline int *Array::maxmin_within(int start, int end)
{

    if (start > end || start < 0 || end >= nextEmptyIndex(array, size))
    {
        return nullptr;
    }

    int *maxmin = new int[2];
    maxmin[0] = INT_MIN; // Store max
    maxmin[1] = INT_MAX; // Store min

    for (int i = start; i <= end; i++)
    {
        if (array[i] > maxmin[0])
        {
            maxmin[0] = array[i]; // Maximum value
        }
        if (array[i] < maxmin[1])
        {
            maxmin[1] = array[i]; // Minimum value
        }
    }

    return maxmin;
}

inline int Array::peakCount()
{
    int peakCount = 0;
    int lastValidIndex = nextEmptyIndex(array, size);

    for (int i = 1; i < lastValidIndex - 1; i++)
    {
        if (array[i] > array[i - 1] && array[i] > array[i + 1])
        {
            peakCount++;
        }
    }

    return peakCount;
}

inline int Array::valleyCount()
{
    int valleyCount = 0;
    int lastValidIndex = nextEmptyIndex(array, size);
    for (int i = 1; i < lastValidIndex - 1; i++)
    {
        if (array[i] < array[i - 1] && array[i] < array[i + 1])
        {
            valleyCount++;
        }
    }
    return valleyCount;
}
inline int *Array::getPeaks()
{
    int index = 0;
    int *peaks = new int[peakCount()];

    int lastValidIndex = nextEmptyIndex(array, size);
    for (int i = 1; i < lastValidIndex - 1; i++)
    {
        if (array[i] > array[i - 1] && array[i] > array[i + 1])
        {
            peaks[index] = array[i];
            index++;
        }
    }
    return peaks;
}
inline int *Array::valleys()
{
    int *array = new int[valleyCount()];
    int index = 0;
    int lastValidIndex = nextEmptyIndex(array, size);
    for (int i = 1; i < lastValidIndex - 1; i++)
    {
        if (array[i] < array[i - 1] && array[i] < array[i + 1])
        {
            array[index] = array[i];
            index++;
        }
    }
    return array;
}
inline bool Array::isGeometric()
{
    int lastValidIndex = nextEmptyIndex(array, size);
    double ratio = array[1] / array[0];
    for (int i = 1; i < lastValidIndex; i++)
    {
        if (array[i] / array[i - 1] != ratio)
        {
            return false;
        }
    }
    return true;
}
inline bool Array::isArithmetic()
{
    int lastValidIndex = nextEmptyIndex(array, size);
    int diff = array[1] - array[0];
    for (int i = 1; i < lastValidIndex; i++)
    {
        if (array[i] - array[i - 1] != diff)
        {
            return false;
        }
    }
    return true;
}
inline double Array::variance()
{
    double mean = average();
    double varianceSum = 0;
    int arraySize = nextEmptyIndex(array, size);
    for (int i = 0; i < arraySize; i++)
    {
        double diff = array[i] - mean;
        varianceSum += diff * diff;
    }
    return varianceSum / (arraySize - 1);
}
inline double Array::standardDeviation()
{
    return sqrt(variance());
}
inline bool Array::isPalindrome()
{
    int lastValidIndex = nextEmptyIndex(array, size);
    int mid = lastValidIndex / 2;
    for (int i = 0; i < mid; i++)
    {
        if (array[i] != array[lastValidIndex - i - 1])
        {
            return false;
        }
    }
    return true;
}

inline int Array::cumulativeSum()
{
    int sum = 0;
    int arraySize = nextEmptyIndex(array, size);
    for (int i = 0; i < arraySize; i++)
    {
        sum += array[i];
    }
    return sum;
}
inline int Array::cumulativeProduct()
{
    int product = 1;
    int arraySize = nextEmptyIndex(array, size);
    for (int i = 0; i < arraySize; i++)
    {
        product *= array[i];
    }
    return product;
}
inline int Array::binarySearch(int target, int low, int high)
{
    while (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (array[mid] == target)
        {
            return mid;
        }
        else if (array[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return -1;
}

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

inline int Array::gcdOfAllelements()
{
    int res = array[0];
    for (int i = 1; i < nextEmptyIndex(array, size); i++)
    {
        res = gcd(res, array[i]);
        if (res == 1)
        {
            return 1;
        }
    }
    return res;
}
int lcm(int a, int b)
{
    return (1LL * a * b) / gcd(a, b); // Prevent overflow
}

inline int Array::lcmOfAllElements()
{
    int res = array[0];
    for (int i = 1; i < nextEmptyIndex(array, size); i++)
    {
        res = lcm(res, array[i]);
    }
    return res;
}

inline int Array::missingNumber(int low, int high)
{

    // Apply binary search
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (array[mid] == mid + 1)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return low + 1;
}
void printPartition(Partition p) {
        std::cout << "First Partition: ";
        for (int i = 0; i < p.firstSize; i++) {
            std::cout << p.firstPart[i] << " ";
        }
        std::cout << "\nSecond Partition: ";
        for (int i = 0; i < p.secondSize; i++) {
            std::cout << p.secondPart[i] << " ";
        }
        std::cout << std::endl;
    }
int main()
{
    cout << "Array in C++" << endl;
    Array a1;
    a1.add(3);
    a1.add(4);
    a1.add(9);
    a1.add(5);
    a1.add(15);
    a1.add(7);
    a1.add(10);
    Partition p = a1.partitionAt(3);
    printPartition(p);

    // Clean up memory
    delete[] p.firstPart;
    delete[] p.secondPart;
    Array a2(5);
    a2.add(1);
    a2.add(2);
    a2.add(3);
    a2.add(4);
    Array z=a1.getUnion(a2);
    z.display();
    Array a3=a1.getIntersetion(a2);
    a3.display();

    return 0;
}
