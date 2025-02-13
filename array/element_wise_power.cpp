#include<iostream>
using namespace std;
int myPower(int x,int n){
    if(n==0){
        return 1;
    }
    if(x<0){
        x=1/x;
        n=-n;
    }
    int res=1;
    while (n!=0)
    {
        if (n % 2 != 0){
            res *= x;
        }
        x*=x;
        n /= 2;
    }
    return res;   

}
void elemetWisePower(int arr1[],int arr2[]){
    for(int i=0; i<5; i++){
        cout<<myPower(arr1[i],arr2[i])<<" ";
    }
}
int main(){
    int arr1[]={2,3,4,5,6};

    int arr2[]={1,2,3,4,5};
    cout<<"Element-wise Power of arr1 and arr2:"<<endl;
    elemetWisePower(arr1,arr2);
   delete[] arr1;
   delete [] arr2;
    return 0;
}