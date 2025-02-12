#include <iostream>
using namespace std;

void display1D(int array[], int n) {
    for (int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;
}


void display2D(int** array, int row, int col) {
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cout << array[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to reshape a 1D array into a 2D array
void reshape(int row, int col, int arr[], int n) {
    if (row * col != n) { // Ensure valid reshaping
        cout << "Reshape not possible with given dimensions!" << endl;
        return;
    }

    int** newArr = new int*[row];
    for (int i = 0; i < row; i++) {
        newArr[i] = new int[col];
    }

    // Fill the new 2D array with elements from the 1D array
    for (int i = 0; i < n; i++) {
        newArr[i / col][i % col] = arr[i];
    }


    display2D(newArr, row, col);

    
    delete[] newArr;
}
void reshape(int row,int col,int** arr){
    if(row==0 || col==0){
        cout<<"Invalid reshaping dimensions"<<endl;
        return;
    }
    int *neArr=new int[row*col];
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++){
            neArr[i*col+j]=arr[i][j];
        }
    }
    display1D(neArr,row*col);

}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6,7,8,9}; // Example array
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Original 1D array:\n";
    display1D(arr, n);

    cout << "\nReshaped 2D array (2x3):\n";
    reshape(3, 3, arr, n);

    cout << "\nOriginal 2D array:\n";
    int** arr2D = new int*[2];
    arr2D[0] = new int[3]{1, 2, 3};
    arr2D[1] = new int[3]{4, 5, 6};
    display2D(arr2D, 2, 3);
    reshape(2,3,arr2D);
    

    return 0;
}
