#include<iostream>
using namespace std;
void calculateXOR(int arr[],int n){
    int xorResult=0;
    for(int i=0; i<n; i++){
        xorResult^=arr[i];
    }
    cout<<"XOR Result: "<<xorResult<<endl;
}
int main(){
    int arr[]={1,2,3,4,5,7};
    calculateXOR(arr,6);
    //Note: XOR operation has property that a XOR b XOR a = 0 and a XOR b XOR b = a.
    //So, XOR of all elements in the array gives the missing number.
    //In this case, missing number is 6. 

    return 0;

}
