#include<iostream>
using namespace std;
void display(int *array){
    for(int i=0; i<5; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
}
bool isPowerOfTwo(int num){
    return (num >0) && (num&(num-1)==0);
}
bool isAllPowerOfTwo(int array [],int n){
    if (n==0){
        return false;
    }
    if(!isPowerOfTwo(array[n-1])){
        return false;
    }
    return isAllPowerOfTwo(array,n-1);
    
}


int main(){
    int array[]={1,2,4,8,1};
    int n=sizeof(array)/sizeof(array[0]);
    display(array);
    cout<<isAllPowerOfTwo(array,n)<<endl;
}

//Time Complexity: O(n) where n is the size of the array.
//Space Complexity: O(1) because we are not using any extra space.