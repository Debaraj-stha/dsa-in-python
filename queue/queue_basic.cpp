#include <iostream>
using namespace std;

class Queue {
private:
    int front, rear, capacity;
    int* arr;

public:
    Queue(int size) {
        front = rear = -1;
        capacity = size;
        arr = new int[size];
    }

    Queue() {
        front = rear = -1;
        capacity = 1;
        arr = new int[1];
    }

    ~Queue() {
        delete[] arr;
    }

    bool isEmpty() {
        return front == -1 || front > rear;
    }

    bool isFull() {
        return rear == capacity - 1;
    }

    void enqueue(int val) {
        if (isFull()) {
            cout << "Queue is full" << endl;
            return;
        }
        if (front == -1) {
            front = 0; // First element
        }
        rear++;
        arr[rear] = val;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }
        cout << "Dequeued element is " << arr[front] << endl;
        front++;

        // Reset queue when it becomes empty
        if (front > rear) {
            front = rear = -1;
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }
        cout << "Queue:" << endl;
        for (int i = front; i <= rear; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
    int peak(){
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return -1;
        }
        return arr[front];
    }
    int size(){
        return rear-front+1;
    }
    bool isFullWithLimit(int limit){
        return size()>=limit;
    }
    void clear(){
        rear=front=-1;
        cout<<"Queue cleared"<<endl;
    
    }
    void resize(int newSize){
        int *newArr=new int[newSize];
        int size=this->size();
        for (int i = 0; i < size; i++)
        {
            newArr[i]=arr[i];
        }
        delete[] arr;
        arr=newArr;
        capacity=newSize;
        cout<<"Queue resized to "<<newSize<<endl;
    }
    void reverse(){
        if(isEmpty()) return;
        int start=front;
        int end=rear;
        while(start<end){
            swap(arr[start],arr[end]);
            start++;
            end--;
    
        
    }
}
    void sort(){
        if(isEmpty()) return;
        for(int i=front;i<=rear-1;i++){
            for(int j=front;j<=rear-i-1;j++){
                if(arr[j]>arr[j+1]){
                    swap(arr[j],arr[j+1]);
                }
            }
    
    }
}

void swap(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}
};

int main() {
    Queue q(5);
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    q.enqueue(10); // This will print "Queue is full"
    
    q.display();
    
    q.dequeue();
    q.dequeue();
    q.display();

    cout << "Peak element: " << q.peak() << endl;
    
    cout << "Size of queue: " << q.size() << endl;
    q.reverse();
    q.display();
    
    return 0;
}
