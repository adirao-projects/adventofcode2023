from __future__ import annotations
from typing import Any, Dict, Tuple, List, Set, Optional, TextIO

class Stack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.stack = [None]*size
        
    def push(self, value: Any) -> None:
        i=0
        while self.stack[i]==None:
            if i == self.size-1:
                return False
            else:
                i=i+1    
        self.stack[i] = value
        return True
        
    def pop(self) -> Any:
        i = self.size-1
        while self.stack[i]==None:
            if i == 0:
                return False
            else:
                i=i-1
        value = self.stack[i]
        self.stack[i]=None
        
        return value


class Queue:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [None]*size
        
    def enqueue(self, value: Any) -> None:
        i=self.size-1
        while self.queue[i]==None:
            if i<0:
                return False
            else:
                i=i-1
        self.queue[i] = value
        
        return True
    
    def dequeue(self) -> Any:
        i=self.size-1
        value = self.queue[-1]
        while self.queue[i]!=None:
            if i!=0:
                self.queue[i] = self.queue[i-1]
            else:
                self.queue[i]=None
                
        return value

class Node:
    def __init__(self, next_node=None: Node, label: str, data: Any) -> None:
        self.next = next_node
        self.label = label
        self.data = data

    def __str__(self) -> str:
        return f"{self.label}: {self.data} at {id(self)}"


    def compareData(self, value: Any) -> bool:
        if self.data == value:
            return True

        else:
            return False


class SingleLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def addItem(self, node: Node) -> None:
        if self.head==None:
            self.head=node
        else:
            self.tail.next = node #next item of tail object
        self.tail = node
    
    def getItem(self, item: Any) -> Any:
        current = self.head

        while current.data != None:
            x=current.compareData(item)
            if x:
                break
            else:
                current = current.next
            
        return current.label
    
    def removeItem(self, query):
        prevNode = self.head()
        current = prevNode.next
        
        while current.label != query:
            prevNode = current
            current = current.next
    
        prevNode.next = current.next


class HashMap:
    def __init__(self, size: int) -> None:
        self.size = size
        self.table = [SingleLinkedList()]*size
    
    def addElement(self, idx: Any, data: Any) -> None:
        if type(idx)==str or type(idx)==chr:
            num_idx = self.stringHash(idx)
            
        index = num_idx%self.size
        
        self.table[index].addItem(cNode(idx, data))
        

    def searchElement(self, idx: Any) -> Any:
        if type(idx)==str or type(idx)==chr:
            num_idx = self.stringHash(idx)
        
        index = num_idx%self.size
        
        data = self.table[index].getItem(num_idx)
        
        return data
        
        
    def stringHash(self, string: str) -> int:
        characters = [ord(x) for x in list(string)]
        val = sum(characters)
        return val


class Tree:
    def __init__(self, root, subtrees = None) -> None:
        self.left = root
        self.subtrees = []

    def is_empty(self) -> bool:
        return subtrees is None

    def __len__(self) -> int:

        if self.is_empty():
            return 0
        else:
            size = 1  # count the root
            for subtree in self.subtrees:
                size += subtree.__len__()  # could also do len(subtree) here
            return size

    def __contains__(self, item: Any) -> bool:

        if self.is_empty():
            return False
        elif self._subtrees == []:
            if self._root == item:
                return True
        else:
            if self._root == item:
                return True
            for subtree in self._subtrees:
                output = subtree.__contains__(item)
                if output:
                    return True
        return False


    def height(self: Tree) -> int:
        if self.is_empty():
            return 0
        elif self.subtrees == []:
            return 1
        else:
            height = 1
            for subtree in self._subtrees:
                if subtree.height() > height:
                    height = max(subtree.height(), height)

            return height + 1

class BinaryTreeNode:
    def __init__(self, data: Any, left: BinaryTreeNode, right: BinaryTreeNode) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.data}\nL:{self.left.data}\nR:{self.right.data}"

class BinaryTree:
    def __init__(self, root: BinNode) -> None:
        self.root = None
        self.left = None
        self.right = None

    def preOrder(self):
        raise NotImplementedError

    def inOrder(self):
        raise NotImplementedError

    def postOrder(self):
        raise NotImplementedError

    def addLeaf(self):
        raise NotImplementedError

    def removeLeaf(self):
        raise NotImplementedError