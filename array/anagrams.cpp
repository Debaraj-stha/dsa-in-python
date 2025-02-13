#include<iostream>
#include<unordered_map>
using namespace std;
void display(int arr[]){
    for(int i=0; i<5; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
bool isAnagrams(int arr1[],int arr2[],int size1,int size2){
    if(size1!=size2) return false;
    unordered_map<int,int> freq;
    for(int i=0; i<size1; i++){
        freq[arr1[i]]++;
    }
    for(int i=0; i<size2; i++){
        freq[arr2[i]]--;
        if(freq[arr2[i]]<0) return false;
    }
    return true;
    

}
int main(){
    int arr1[]={1, 2, 3, 4,8};
    int size1=sizeof(arr1)/sizeof(arr1[0]);
    cout<<"array 1"<<endl;
    display(arr1);
    int arr2[]={1,2,3,4,5};
    int size2=sizeof(arr2)/sizeof(arr2[0]);
    cout<<"array 2"<<endl;
    display(arr2);
    cout<<"Are arrays anagrams? "<<isAnagrams(arr1,arr2,size1,size2)<<endl;
    return 0;
}
// time complexity: O(n), where n is the size of the arrays
// space complexity: O(n), where n is the size of the arrays
   