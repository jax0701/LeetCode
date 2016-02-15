import sys

class binaryTree:
    def BinaryTree(self,r):
        return [r,[],[]]

    def insertLeft(self,root,newBranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1,[newBranch,t,[]])
        else:
            root.insert(1,[newBranch,[],[]])
        return root

    def insertRight(self,root,newBranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2,[newBranch,[],t])
        else:
            root.insert(2,[newBranch,[],[]])
        return root
    
    def getRootVal(self, root):
        return root[0]

    def setRootVal(self,root,newVal):
        root[0] = newVal

    def getLeftChild(self, root):
        return root[1]

    def getRightChild(self, root):
        return root[2]

class Solution:
    def __init__(self):
        self.depth = 1
        self.temp = 0

    def maxDepth(self, root):
        print("Dividing")
        print root
        print self.depth

        if len(root)>1 and (root[1]!=None or root[2]!=None):
            self.depth = self.depth+1

            leftChild = root[1]
            rightChild = root[2]
            
            self.maxDepth(leftChild)
            self.maxDepth(rightChild)

            if self.depth > self.temp:
                self.temp = self.depth
        
        return self.temp

A = binaryTree()
r = A.BinaryTree(7)
A.insertLeft(r,17)
A.insertLeft(r,27)
A.insertLeft(r,22)
A.insertLeft(r,81)
A.insertLeft(r,3)
A.insertLeft(r,10)
B = Solution()
print B.maxDepth(r)





