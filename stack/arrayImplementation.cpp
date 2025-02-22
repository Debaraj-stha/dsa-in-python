#include<iostream>
using namespace std;
class Stack{
    int top;
    int capacity;
    int *arr;
    public:
    Stack(int size){
        top = -1;
        capacity = size;
        arr = new int[size];
    }
    Stack(){
        top = -1;
        capacity = 1;
        arr = new int[1];
    }
    int getCapacity(){
        return capacity;
    }
    int getTop(){
        return top;
    }

    void display(){
        cout<<"Stack:"<<endl;
        int i=top;
        while(i!=-1){
            cout<<arr[i]<<endl;
            i--;
        }
    }
    void push(int val){
        if (top==capacity-1){
            cout<<"Stack is full"<<endl;
        }
        else{
            top++;
            arr[top]=val;
        }
    }
    void pop(){
        if (top==-1){
            cout<<"Stack is empty"<<endl;
        }
        else{
            cout<<"Popped element is "<<arr[top]<<endl;
            top--;
        }
    }
    ~Stack(){
        delete[] arr;
    }

};


int main(){
    Stack s(5);
    Stack s1;
    cout<<s.getCapacity()<<endl;
    cout<<s1.getCapacity()<<endl;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    s.push(6);
    s.push(22);
    s.display();
}