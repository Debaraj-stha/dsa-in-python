#include <iostream>
#include <math.h>
#include <climits>
#include<set>
using namespace std;
struct Partition
{
    int *firstPart;
    int firstSize;
    int *secondPart;
    int secondSize;
};
class Array{
    int size;
    int *array; // Pointer to store dynamically allocated array
    public:
    // Constructor
    Array(int size, int *array){
        this->size=size;
        this->array=new int[size];
        for(int i=0; i<size; i++){
            this->array[i]=array[i];
        }
    }
    //copy constructor
    Array(Array &other){
        int size=other.getSize();
        array=new int[size];
        for(int i=0; i<size; i++){
            array[i]=other.array[i];
        }
        this->size=other.getSize();
    }


    //for 2d array
     Array(int rows, int cols, int **arr) {
        size = rows * cols;
        array = new int[size];

        int index = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                array[index++] = arr[i][j]; 
            }
        }
    }
    Array(){
        size=0;
        array=nullptr;
    }
    // Destructor
    ~Array(){
        delete[] array;
    }
    // Function to swap elements at two given indices
    void swap(int i, int j){
        int temp=array[i];
        array[i]=array[j];
        array[j]=temp;
    }
    void display(){
        for(int i=0; i<size; i++){
            cout<<array[i]<<" ";
        }
        cout<<endl;
    }
    int getSize(){
        return size;
    }
    int *getArray(){
        return array;
    }
    
    //merging array
    Array mergeArrays(Array &other){
        int *newArray=new int[size+other.getSize()];
        for(int i=0; i<size; i++){
            newArray[i]=array[i];
        }
        for(int i=0; i<other.getSize(); i++){
            newArray[size+i]=other.array[i];
        }
        return Array(size+other.getSize(),newArray);
    }
static int resize(int newsize,int oldSize,int *array){
    int *newArray=new int[newsize];
    for(int i=0; i<min(newsize,oldSize); i++){
        newArray[i]=array[i];
    }
    delete[] array;
    array=newArray;
    return newsize;

}
    
int* findAllOccurances(int value){
    int count=0;
    for(int i=0; i<size; i++){
        if(array[i]==value){
            count++;
    }
    }
    int* indices=new int[count];
    int index=0;
    for(int i=0; i<size; i++){
        if(array[i]==value){
            indices[index++]=i;
        }
    }
    
    
return indices;
}
int findFirstIndex(int value){
    
    for(int i=0;i<size;i++){
        if(array[i]==value){
            return i;
            break;
        }

    }
    return -1;
}
int findLastIndex(int value){
    
    for(int i=size-1;i>0;i--){
        if(array[i]==value){
            return i;
            break;
        }

    }
    return -1;
}
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
int foundMode(){
    int maxcount=0;
    int mode=array[0];
    for(int i=1;i<size;i++){
        int count=countOccurrences(array[i]);
        if(count>maxcount){
            maxcount=count;
            mode=array[i];
        }
    }
    return mode;
}
int getZeroPosition(){
    for(int i=0; i<size; i++){
        if(array[i]==0){
            return i;
        }
    }
    return -1;
}
void moveAllZeroToEnd(){
    int writePos=0;
    for (int i=0; i<size; i++){
        if(array[i]!=0){
            swap(i, writePos);
            writePos++;
        }
    }
}
int nextOf(int value){
    for(int i=0; i<size; i++){
        if(array[i]==value){
            return i+1;
        }
    }
    return -1;
}


int* subarrayWithMaximumSum(int&subSize) {
    int currentSum = 0, maxSum = INT_MIN;
    int start = 0, end = 0, tempStart = 0;
    
    for (int i = 1; i < size; i++) {
        currentSum += array[i];

        if (currentSum > maxSum) {
            maxSum = currentSum;
            start = tempStart;  // Update start index
            end = i;            // Update end index
        }

        if (currentSum < 0) {
            currentSum = 0;
            tempStart = i + 1;  // Start a new subarray
        }
    }

    // Size of the maximum sum subarray
    subSize = end - start + 1;
    int* subarray = new int[subSize];

    // Copy elements of the maximum subarray
    for (int i = 0; i < subSize; i++) {
        subarray[i] = array[start + i];
    }

    return subarray;
}
int longestIncreasingSubsequences(){
    int *dp=new int[size];
    for (int i = 0; i < size; i++){
        dp[i]=1;
    }
    for(int i=1; i < size; i++){
        for (int j =0;j<i;j++){
            if(array[i]>array[j]){
                dp[i]=max(dp[i],dp[j]+1);
            }
        }
    }
    int maxLIS=0;
    for (int i=0;i<size;i++){
        cout<<dp[i]<<endl;
        maxLIS=max(maxLIS,dp[i]);
    }
    delete [] dp;
    return maxLIS;
    
}
void sortEvenOddSeparately(){
    int start=0, end=size-1;
    while(start<end){
        while(start<end && array[start]%2==0){
            start++;
        }
        while(start<end && array[end]%2!=0){
            end--;
        }
        swap(start,end);
    }
}




};

int main(){

    int val[]={10,22,9,33,44,20,22,10,11,33,9,9,9,9};
    int size=sizeof(val)/sizeof(val[0]);
    Array arr2(size,val);
;
   
    cout<<"Array after sorting by frequency: ";
    arr2.display();
   
    return 0;



}