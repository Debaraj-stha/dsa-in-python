#include <iostream>

using namespace std;
void swap(int *a,int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void sort(int arr[] ,int n){
    for(int i=0; i<n; i++){
        for(int j=0; j<n-i-1; j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }

}
void wiggleSort(int arr[], int n) {
    sort(arr,n); 
    for (int i = 1; i < n - 1; i += 2) {
        swap(arr[i], arr[i + 1]);
    }
}

void displayArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {3, 5, 2, 1, 6, 4};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original Array: ";
    displayArray(arr, n);

    wiggleSort(arr, n);

    cout << "Wiggle Sorted Array: ";
    displayArray(arr, n);

    return 0;
}
