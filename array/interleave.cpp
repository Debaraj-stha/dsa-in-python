#include<iostream>
using namespace std;
void display(int array [],int n){
    for(int i=0; i<n; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
}
void interleave(int arr1[],int arr2[],int n){
    int* interleaved =new int[n*2];
    for(int i=0;i<n;i++){
        interleaved[i*2] = arr1[i];
        interleaved[i*2+1] = arr2[i];
    }
    display(interleaved, n*2);
    delete[] interleaved;
}
int main(){
    int arr[] = {0,2,4,6,8};
    int arr2[]={1,3,5,7,9};

    int n = sizeof(arr) / sizeof(arr[0]);
   
    display(arr, n);
    interleave(arr, arr2,n);
    return 0;
}