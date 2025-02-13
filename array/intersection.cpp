#include<iostream>
#include<set>
using namespace std;
void display(int arr[],int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void findUnion(int arr1[],int arr2[],int arr3[],int n1,int n2,int n3){
    set<int> s;
    for(int i=0; i<n1; i++){
        s.insert(arr1[i]);
    }
    for(int i=0; i<n2; i++){
        s.insert(arr2[i]);
    }
    for(int i=0; i<n3; i++){
        s.insert(arr3[i]);
    }
    int arr[s.size()];
    int i=0;
    for(auto x: s){
        arr[i]=x;
        i++;
    }
    display(arr, i);
}
void findIntersection(int arr1[],int arr2[],int arr3[],int n1,int n2,int n3){
    set<int> s;
    for(int i=0; i<n1; i++){
        s.insert(arr1[i]);
    }
    for(int i=0; i<n2; i++){
        if(s.find(arr2[i])!=s.end()){
            cout<<arr2[i]<<" ";
        }
    }
    cout<<endl;
    for(int i=0; i<n3; i++){
        if(s.find(arr3[i])!=s.end()){
            cout<<arr3[i]<<" ";
        }
    }
    cout<<endl;
}
int main(){
    int arr[]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n=sizeof(arr)/sizeof(arr[0]);
    int arr2[]={9,3,8,15,19};
    int m=sizeof(arr2)/sizeof(arr2[0]); 
    int arr3[]={10,17,12,8};
    int k=sizeof(arr2)/sizeof(arr2[0]);
   cout<<"array 1"<<endl;
    display(arr, n);
    cout<<"array 2"<<endl;
    display(arr2, m);
    cout<<"array 3"<<endl;
    display(arr3, k);
    cout<<"union of arrays"<<endl;
    findUnion(arr, arr2, arr3, n, m, k);  // time complexity: O(n+m+k)
    cout<<"Interscetion"<<endl;
    findIntersection(arr, arr2, arr3, n, m, k); // time complexity: O(n+m+k)
    
    return 0;  
}