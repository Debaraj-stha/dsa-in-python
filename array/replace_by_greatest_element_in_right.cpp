#include<iostream>
using namespace std;
void display(int array[],int n){
    for(int i=0; i<n; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;

}

void replaceByGreatestElement(int array[], int n) {
    int maxSoFar = -1;  // Last element should always be replaced by -1
    for (int i = n - 1; i >= 0; i--) {
        int current = array[i];  
        array[i] = maxSoFar;     
        if (current > maxSoFar) {
            maxSoFar = current; 
        }
    }
}
int main(){
    int arr[]={17, 18, 5, 4, 6, 1};
    int n=sizeof(arr)/sizeof(arr[0]);
    display(arr,n);
    replaceByGreatestElement(arr,n);
    display(arr,n);
    
}