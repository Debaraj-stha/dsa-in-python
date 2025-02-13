#include<iostream>
using namespace std;
void display(int **arr){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            std::cout<<arr[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
}
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void transpose(int **arr,int rows,int cols){
    for(int i=0; i<rows; i++){
        for(int j=i; j<cols; j++){
            swap(&arr[i][j],&arr[j][i]);
        }
    }
}
int main(){
int** arr=new int*[3];
arr[0]=new int[3]{1,2,3};
arr[1]=new int[3]{4,5,6};
arr[2]=new int[3]{7,8,9};
cout<<"Original Array:"<<endl;
display(arr);
transpose(arr,3,3);
cout<<"Transposed Array:"<<endl;
display(arr);

delete[] arr;

}