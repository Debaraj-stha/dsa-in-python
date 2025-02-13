#include<iostream>
#include<climits>
using namespace std;
void display(int arr[],int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void maximum_product_subarray(int arr[],int n){
    int start=0,end=0,tempStart=0;
    int currProduct=arr[0]>0 ? arr[0]:1;
    int maxProduct=INT_MIN;
    for(int i=1; i<n; i++){
        currProduct*=arr[i];
        if(currProduct>maxProduct){
            maxProduct=currProduct;
            start=tempStart;
            end=i;
        }
        if(arr[i]<=0){
            currProduct=1;
            tempStart=i+1;
        }

    }
    int subSize=end-start+1;
    for(int i=0;i<subSize;i++){
        cout<<arr[start+i]<<" ";
    }
    cout<<endl;
    cout<<"Maximum product subarray: "<<maxProduct<<endl;

}
int main(){
    int arr[]={1,-2,3,4,-9,4,7,9};
    int n=sizeof(arr)/sizeof(arr[0]);
    display(arr,n);
    maximum_product_subarray(arr,n);
    
}