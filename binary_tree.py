class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
       queue=[]
       queue.append(self)
       while queue:
           temp=queue.pop(0)
           if not temp.left:
               temp.left=Node(key)
               break
           else:
               queue.append(temp.left)
           if not temp.right:
               temp.right=Node(key)
               break
           else:
               queue.append(temp.right)
       
            

    def delete(self, key):
        queue=[]
        key_node=None
        queue.append(self)
        while queue:
            temp=queue.pop(0)
            if temp.key==key:
                key_node=temp
                break
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        if key_node:
            deepest_node=self.get_deepest_and_rightmost()
            key_node.key=deepest_node.key
            self.delete_deepest_and_rightmost(deepest_node)

    def get_deepest_and_rightmost(self):
        # Use a queue to perform level order traversal to find the deepest and rightmost node
        queue = []
        queue.append(self)
        temp = None
        while queue:
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return temp

    def delete_deepest_and_rightmost(self, node_to_delete):
        # Use a queue to perform level order traversal to delete the deepest and rightmost node
        queue = []
        queue.append(self)
        while queue:
            temp = queue.pop(0)
            if temp is node_to_delete:
                temp = None
                return
            if temp.right:
                if temp.right is node_to_delete:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left is node_to_delete:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=",")
        if self.right:
            self.right.inorder()

    def preorder(self):
        print(self.key, end=",")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key, end=",")


if __name__ == "__main__":
    root = Node(11)
    root.insert(7)
    root.insert(13)
    root.insert(4)
    root.insert(9)
    root.insert(12)
    root.insert(15)

    print("Inorder traversal before deletion:")
    root.inorder()
    print("\nDeleting node with key 9")
    root.delete(9)
    print("Inorder traversal after deletion:")
    root.inorder()
