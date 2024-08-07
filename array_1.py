class Array:
    def __init__(self):
        self.data = []
        
    def length(self):
        """retur length of the array"""
        count = 0
        for _ in self.data:
            count += 1
        return count
    
    def printArr(self):
        print(f'[{",".join(map(str,self.data))}]')
        
    def insertAt(self, index:int, value):
        """insert element at index"""
        if index < 0 or index > len(self.data):
            raise IndexError("Invalid index")
        self.append(value)
        self.printArr()
        for i in range(len(self.data) - 2, index - 1, -1):
            print("i=",i)
            self.data[i + 1] = self.data[i]
        self.data[index] = value
                    
                    
    def append(self, *args):
        """"append list elements to the end of the list'"""
        self.data+=[value  for value in args]
        
            
        
    def remove(self,value):
        """remove given value from the list"""
        try:
            index = self.data.index(value)
            if index == -1:
                raise ValueError(f"{value} not found in the array")
            for i in range(self.length()):
                if self.data[i]==value:
                    self.data[i]=self.data[i+1]
                    break
        except ValueError as ve:
               raise ValueError(f"{value} not found in the array")
        
    def removeAt(self,index:int):
        """"remove given element from the list"""
        if index < 0 or index >= len(self.data):
            raise IndexError("Invalid index")
        new_arr=Array()
        for i in range(len(self.data)):
            if i!= index:
                new_arr.data.append(self.data[i])
        self.data = new_arr.data
        return 1
    
    def insertAtFirst(self,value):
        self.append(None)
        for  i in range(self.length()-1,0,-1):
            self.data[i] = self.data[i - 1]
        self.data[0] = value
        
    def sort(self,reverse=False):
        """sort the array """
        length=self.length()
        for i in range(length):
            for j in range(length):
                if reverse:
                 if self.data[i] < self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                else:
                    if self.data[i] > self.data[j]:
                        self.data[i], self.data[j] = self.data[j], self.data[i]
                        
    def reverse(self):
        """ reverse order of list element"""
        self.data=self.data[::-1]
            
    def isEmpty(self):
        """check if list is empty"""
        return self.length()==0
        
    def indexOf(self,item):
        """find index of item in list"""
        if self.isEmpty():
            return -1
        for value in self.data:
            if value==item:
                return self.data.index(value)
        return -1
    def merge(self,other):
        self.data+=other.data
    def isinstance(self,other):
        return type(self)==type(other)
    
    def isEqual(self,other):
        if self.length()!=other.length():
            return False
        for i in range(self.length()):
            if self.data[i]!=other.data[i]:
                return False
        return True
    
    def get_sum(self)->int:
        temp=0
        for data in self.data:
            temp+=data
        return temp
    
    def get_min_max(self, start:int, end:int):
        if not self.data:
            raise ValueError("The list is empty.")
        
        if start < 0 or end >= len(self.data) or start > end:
            raise IndexError("Invalid start or end index.")
        
        if start == end:
            min0 = max0 = self.data[start]
        elif start == end - 1:
            if self.data[start] < self.data[end]:
                min0 = self.data[start]
                max0 = self.data[end]
            else:
                min0 = self.data[end]
                max0 = self.data[start]
        else:
            mid = (start + end) // 2
            min0_left, max0_left = self.get_min_max(start, mid)
            min0_right, max0_right = self.get_min_max(mid + 1, end)
            
            min0 = min(min0_left, min0_right)
            max0 = max(max0_left, max0_right)
        
        return min0, max0
    def binary_search(self,value,data=None,start=0):
        if data is None:
            data = self.data
        
        length = len(data)
        if length == 0:
            return -1
        
        mid = length // 2

        if value == data[mid]:
            return start + mid
        elif value < data[mid]:
            return self.binary_search(value, data[:mid], start)
        else:
            return self.binary_search(value, data[mid + 1:], start + mid + 1)
        
    def count(self,value):
        count = 0
        for item in self.data:
            if item == value:
                count += 1
        return count
    
    def clear(self):
        self.data = []
        
    def join(self,seperator:str):
        return seperator.join(map(str, self.data))
    def split(self,value):
        left=Array()
        right=Array()
        if not self.data:
            return left,right
        for item in self.data:
            if item == value:
                left.data=self.data[:self.indexOf(item)]
                right.data=self.data[self.indexOf(item) + 1:]
                return left, right
        return left,right
    
        
        

    def copy(self):
        return self.data
    
    def __str__(self):
        return f'[{",".join(map(str, self.data))}]'
    
    
    
        
if __name__ == "__main__":
    a = Array()
    a.data = [1, 2, 3]
    print(a.length())  
    a.printArr()      
    print(type(a))
    a.insertAt(1, 78)
    a.printArr()  
    # a.remove(3)
    a.printArr()
    a.append(3)
    a.append(1)
    a.printArr()
    # a.removeAt(2)
    a.remove(78)
    a.data=[3,8,0,8]
    a.append(33,9,93,2)
    a.printArr()
    a.insertAtFirst(122)
    a.printArr()
    a.reverse()
    a.printArr()
    a.sort(reverse=True)
    a.reverse()
    a.printArr()
    i=a.indexOf(122)
    b=Array()
    b.data=[12,13,14]
    a.merge(b)
    a.printArr()
    print(i)

    x,y=a.get_min_max(0,a.length()-1)
    print("min max",x,y)
    s=a.get_sum()
    print("sum",s)
    l=Array()
    l.data=[1,2,3,4,5,6,7,8,9,10,11]
    x=l.binary_search(7)
    print("binary search",x)
    b=a.join(",")
    print("join",b)
    g=Array()
    g.data=[1,2,3,4,5,6,7,8,9,9,10,11]
    b,c=g.split(6)
    
    x=c.__str__()
    print(x)
    b.printArr()
    c.printArr()
    