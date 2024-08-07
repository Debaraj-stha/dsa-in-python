class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        print("pushing...")
        if self.is_empty():
            self.stack = [item]
        else:
            self.stack+=[item]
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            print("popping stack element")
            popped_item=self.stack[-1]
            self.stack=self.stack[:-1]
            return popped_item
    
    
    def length(self):
        count=0
        for item in self.stack:
            count += 1
        return count
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack elements are:")  # Output: Stack elements are:
        for i in range(self.length() - 1, -1, -1):
            print(self.stack[i])
    
    def is_empty(self):
        return  self.length()==0
    
    
    def get_stack_top(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            elem=self.stack[-1]
            index=self.indexOf(elem)
            return index,elem
        
        
    def indexOf(self,value):
        if self.is_empty():
            print("Stack is empty")
            return -1
        for i in range(self.length()):
            if self.stack[i]==value:
                return i
        return -1
    
    
    def get_stack_bottom(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[0]
        
    def peek(self):
        index,elem=self.get_stack_top()
        return elem
    def clear(self):
        self.stack=[]
        print("Stack cleared")
    def reverse(self):
        self.stack=self.stack[::-1]
        print("Stack reversed")
    def to_list(self):
        return self.stack.copy()
    
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    item_popped=stack.pop()
    print("Item popped:", item_popped)
    stack.display()
    index,elem=stack.get_stack_top()
    print("Top element:",index,elem)
    r=stack.reverse()
    print("Stack reversed")
    stack.display()
    x=stack.to_list()
    print("Stack to list:",x)