class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, value):
        """check is value to be insert is less than  root value and if yes it goes to left child otherwise it goes to right child"""
        if value < self.value:
            print(f"if {value}")
            if self.left is None:
                self.left = Node(value) 
            else:
                self.left.insert(value)
        else:
          
            print(f"else {value}")
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def inorder(self):
        #print left child first and right child
        if self.left:
            self.left.inorder()
        print(self.value, end=' ')
        if self.right:
            self.right.inorder()

    def preorder(self):
        #print root first and left child
        print(self.value, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        #print left child first and right child
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=' ')

    
    
    def delete(self, value):
        if not self:
            return self

        # Find the node to be deleted
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Node with two children
            temp = self._minValueNode(self.right) #find minimum child of right side children
            self.value = temp.value
            self.right = self.right.delete(temp.value)

        return self

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    root = Node(60)
    root.insert(50)
    root.insert(30)
    root.insert(40)
    root.insert(70)
    root.insert(80)
    root.insert(65)
    root.inorder()
    print()
    root.preorder()
    print()
    root.postorder()
