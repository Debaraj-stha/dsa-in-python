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
    int pop(){
        if (top==-1){
            cout<<"Stack is empty"<<endl;
        }
        else{
            int ele=arr[top];
            // cout<<"Popped element is "<<arr[top]<<endl;
            top--;
            return ele;
        }
        return -1;
    }
    void search(int val){
        int i=top;
        while (i!=-1)
        {
            if(arr[i]==val){
                cout<<"Element found at position "<<i+1<<endl;
                return;
            }
            i--;
        }
        cout<<"Element not found"<<endl;
        
    }

    int peek(){
        if (top==-1){
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        else{
            return arr[top];
        }
    }
    bool isEmpty(){
        return top==-1;
    }
    bool isFull(){
        return top==capacity-1;
    }
    int size(){
        return top+1;
    }
    void clear(){
        top=-1;
    }
    void resize(int newsize){
        int *newArr=new int[newsize];
        for (int i = 0; i <= top; i++)
        {
            newArr[i]=arr[i];
        }
        delete[] arr;
        arr=newArr;
        capacity=newsize;
    }
    int getMin(){
        if(top==-1){
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        int min=arr[top];
        for (int i = top-1; i >= 0; i--)
        {
            if(arr[i]<min){
                min=arr[i];
            }
        }
        return min;
    }
    int getMax(){
        if(isEmpty()){
            cout<<"Stack is empty"<<endl;
            return -1;
        }
        int max=arr[top];
        for (int i = top-1; i >= 0; i--)
        {
            if(arr[i]>max){
                max=arr[i];
            }
        }
        return max;
    }
    void reverse() {
        if (isEmpty()) {
            return;
        }
        int temp = pop(); // Corrected: use pop() instead of arr[top]
        reverse();
        insertAtBottom(temp); // Call the corrected function
    }
    
    void insertAtBottom(int value) {
        if (isEmpty()) {
            push(value);
        } else {
            int temp = pop();
            insertAtBottom(value);
            push(temp);
        }
    }
    void removeDuplicates(){
        if(isEmpty()){
            return;
        }
        int temp=pop();
        removeDuplicates();
        if(temp!=peek()){
            push(temp);
        }
    }
    void sortedInsert(int value){
        if (isEmpty() || value>peek()){
            push(value);
            return;
        }
        int temp=pop();
        sortedInsert(value);
        push(temp);
    }
    void sort(){
        if(isEmpty()){
            return;
        }
        int temp=pop();
        sort();
        sortedInsert(temp);
    }
    

    ~Stack(){
        delete[] arr;
    }

};


int main(){
    Stack s(10);
    Stack s1;
    cout<<s.getCapacity()<<endl;
    cout<<s1.getCapacity()<<endl;
    s.push(1);
    s.push(2);
    s.push(30);
    s.push(4);
    s.push(9);
    s.push(6);
    s.push(22);
    s.display();
    s.search(22);
    cout<<"Reversing stack..."<<endl;
    s.reverse();
    s.display();
    cout<<"Removing duplicates..."<<endl;
    s.removeDuplicates();
    s.display();
    cout<<"Sorting stack..."<<endl;
    s.sort();
    s.display();
    cout<<"Min element is "<<s.getMin()<<endl;
    cout<<"Max element is "<<s.getMax()<<endl;
    return 0;
}