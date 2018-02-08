class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
    
    def addLeft(self,node):
        self.l=node

    def getLeft(self):
        return self.l

    def addRight(self,node):
        self.r=node

    def getRight(self):
        return self.r

    def getNode(self):
        return self.v