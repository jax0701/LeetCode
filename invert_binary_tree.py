class binaryTree:
    def bTree(self,r):
        self.root= [r,[],[]]

    def insertLeft(self,newBranch):
        t = self.root.pop(1)
        if len(t) > 1:
            self.root.insert(1,[newBranch,t,[]])
        else:
            self.root.insert(1,[newBranch,[],[]])
        return self.root

    def insertRight(self,newBranch):
        t = self.root.pop(2)
        if len(t) > 1:
            self.root.insert(2,[newBranch,[],t])
        else:
            self.root.insert(2,[newBranch,[],[]])
        return self.root
    
    def getRootVal(self):
        return self.root[0]

    def setRootVal(self,newVal):
        self.root[0] = newVal

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]

class Solution(object):
        def invertTree(self, root):

            if len(root)>1:
                temp = root[2]
                root[2] = root[1]
                root[1] = temp

                self.invertTree(root[1])
                self.invertTree(root[2])

            return root

`
