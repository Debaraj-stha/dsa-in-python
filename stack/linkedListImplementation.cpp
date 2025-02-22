#include <iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
    ~Node(){
        cout<<"Node deleted"<<endl;
        delete next;  // delete the dynamically allocated memory for next pointer
    }
};
class Stack{
    Node* top;
    public:
    Stack(){
        top = NULL;
    }
    void push(int val){
        Node* newNode = new Node();
        newNode->data = val;
        newNode->next = top;
        top = newNode;
    }
    void display(){
        Node*temp=top;
        while (temp!=NULL){
            cout<<temp->data<<endl;
            temp = temp->next;
        }
        
        
    }
    void pop(){
        if(top==NULL){
            cout<<"Stack is EMPTY"<<endl;
        }
        else{
            cout<<"Popped element is "<<top->data<<endl;
            top = top->next;
        }
    }
    void peek(){
        if(top==NULL){
            cout<<"Stack is EMPTY"<<endl;
        }
        else{
            cout<<"Top element is "<<top->data<<endl;
        }
    }
    ~Stack(){
        cout<<"Stack deleted"<<endl;
        delete top;  // delete the dynamically allocated memory for top pointer
    }
};
int main(){
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.display();
    s.pop();
    s.display();
    return 0;
}
