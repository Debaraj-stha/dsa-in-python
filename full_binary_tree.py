class Node:
    def __init__(self,root=None):
        self.root = root
        self.left=None
        self.right=None
class FullBinaryTree:
    def __init__(self,root):
        self.root=Node(root)
    def insert(self,value):
        queue=[]
        queue.append(self.root)
        while queue:
            temp=queue.pop(0)
            if temp.left is None and temp.right is None:
                temp.left=Node(value)
                return
            if temp.left and temp.right is None:
                temp.right=Node(value)
                return
            else:
                queue.append(temp.left)
                queue.append(temp.right)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.root,end=" ")
            self.inorder(node.right)
    def preorder(self,node):
        if node:
            print(node.root,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.root,end=" ")


    def delete(self,value):
        if self.root is None:
            return
        queue=[]
        queue.append(self.root)
        key_node=None
        while queue:
            temp=queue.pop(0)
            if temp.root==value:
                key_node=temp
                break
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        if key_node:
            deepest_node=self.get_deepest_and_rightmost()
            key_node.root=deepest_node.root
            self.delete_deepest_and_rightmost(deepest_node)

    def get_deepest_and_rightmost(self):
        temp=None
        queue=[]
        queue.append(self.root)
        while queue:
            temp=queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return temp
    
    def delete_deepest_and_rightmost(self, node):
        queue=[]
        queue.append(self.root)
        while queue:
            temp=queue.pop(0)
            if temp is node:
                temp=None
                return
            if temp.right:
                if temp.right is node:
                    temp.right=None
                    return
                else:
                    queue.append(temp.right)
            if temp.left:
                if temp.left is node:
                    temp.left=None
                    return
                else:
                    queue.append(temp.left)



fbt=FullBinaryTree(10)
fbt.insert(20)
fbt.insert(30)
fbt.insert(2)
fbt.insert(3)
fbt.insert(1)
fbt.inorder(fbt.root)
fbt.delete(20)
print("after deleting")
fbt.inorder(fbt.root)