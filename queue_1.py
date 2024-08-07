class Queue:
    def __init__(self):
        self.data=[]
        
    def enqueue(self,item):
        if self.is_empty():
            self.data=[item]
        else:
            self.data+=[item]
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            print("dequeueing item...")
            dequeued_item=self.data[0]
            self.data=self.data[1:]
            return dequeued_item
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.data[0]
    def is_empty(self):
        return self.length() == 0
    def length(self):
        count=0
        for item in self.data:
            count+=1
        return count
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are:")  # Output: Queue elements are:
        for item in self.data:
            print(item)
    def to_dict(self):
        return {"queue":self.data}
    def to_list(self):
        return self.data.copy()
        
if __name__ == '__main__':
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())  
    print(queue.length())  
    queue.display()  
    queue.dequeue()
    print(queue.peek()) 
    print(queue.length()) 
    queue.display()
    queue_dict=queue.to_dict()
    print(queue_dict)
    
    