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


def printTree(tree):
    if tree != None:
        printTree(tree.getLeft())
        print(tree.getNode())
        printTree(tree.getRight())

def depthSearch(tree,visited):
    #This algorithm can be look at as an issue where you always want to start going on the right
    #If there's nothing else on the right then you can try with the left but only the brother of the node

    visited.append(tree.getNode())
    #Stopping until the bottom of the tree for both Right and Left childs
    if tree.getRight() != None:
        depthSearch(tree.getRight(),visited)

    if tree.getLeft() != None:
        depthSearch(tree.getLeft(),visited)

    return visited


def breadthSearch(queue, visisted):
    #We can try taking a look at the algorithm as a stack and queue problem
    #Using a queue it's easy to solve, the sons of a Node are sent to the end of the queue
    #When a node is visisted the value is saved to know the order it was visited
    if len(queue) != 0:#Stopping only when the array is completly empty

        visisted.append(queue[0].getNode())

        if queue[0].getLeft() != None:#In this way we only add the node if it exists at all
            queue.append(queue[0].getLeft())
        if queue[0].getRight() != None:
            queue.append(queue[0].getRight())

        queue.popleft()
        breadthSearch(queue,visisted)

    return visisted

#Creating our binary tree for testing
test = Node(0)
childLeft = Node(1)
childLeft.addRight(Node(3))
childLeft.addLeft(Node(5))
test.addLeft(childLeft)

childRight = Node(2)
childRight.addRight(Node(4))
childRight.addLeft(Node(6))
test.addRight(childRight)

print("Depth First search order:" + str(depthSearch(test,[])))
print("Breadth First search order:" + str(breadthSearch(deque([test]),[])))