class Item:
    
    def __init__(self,name,weight,value):
        self.name = name
        self.weight = weight
        self.value = value
        self.ratio = value / weight if weight != 0 else 0
        
    def __lt__(self, other):
        return self.ratio > other.ratio
    
    def  display(self):
        print(f"{self.name}\t\t{self.weight}\t\t{self.value}\t\t{self.ratio}")
        
        
        
        
if __name__=='__main__':
    items = [Item("A", 8, 60), Item("B", 5, 100), Item("C", 4, 120), Item("D", 5,50)]
    print("Items before sorting")
    print("Name\tWeight\tValue\tRatio")
    for item in items:
        item.display()
    items.sort()
    print("Items after sorting")
    print("Name\tWeight\tValue\tRatio")
    for item in items:
        item.display()
        
    capacity=8
    w=0
    total=0
    n=len(items)
    x=[0]*n
    for i in range(n):
        if items[i].weight+w<capacity:
            x[i]=1
            w+=items[i].weight
            total+=items[i].value
        else:
            needed_weight=capacity-w
            x[i]=needed_weight/items[i].weight
            w+=needed_weight
            total+=x[i]*items[i].value
            break
print(x)
print(f"Profit:{total}")
    
        
        
    
    
 