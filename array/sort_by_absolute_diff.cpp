#include<iostream>
#include<math.h>
using namespace std;
void display(int arr[],int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
int * calculateDiff(int arr[],int n,int X){
    int * diff=new int[n];
    for(int i=0; i<n; i++){
        diff[i]=abs(arr[i]-X);
    }
    return diff;
}
void sortByDiff(int arr [],int n,int X){
    int * diff=calculateDiff(arr, n, X);
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (diff[j] > diff[j + 1]) {
                swap(diff[j], diff[j + 1]);
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    display(arr,n);
    delete[] diff;
}
int  main(){
    int arr[]={10,6,9,3,7,2,19};
    int n=sizeof(arr)/sizeof(arr[0]);
    int X=6;
    display(arr,n);
    sortByDiff(arr,n,X);
  


}