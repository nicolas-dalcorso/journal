#   Node
from typing import Any
from NaiveDataClasses import Data;
import hashlib;


class Node:
    __slots__ = 'data', 'next'
    
    #   Node constructor
    def __init__(self, data, next=None) -> None:
        self.data = data;
        self.next = next;

class BinaryTreeNode(Node):
    __slots__ = 'data', 'left', 'right';
    
    def __init__(self, data) -> None:
        self.data = data;
        self.left = None;
        self.right = None;
        
    def __iter__(self) -> None:
        return self;
    
    def __next__(self):
        if(self.left != None):
            yield self.left;
        elif(self.right != None):
            yield self.right;
        else:
            raise StopIteration;    
    
    def __repr__(self) -> str:
        return str(self.data);
        
class BinaryTree:
    def __init__(self) -> None:
        self.size   = 0;
        self._index = 0;
        self.root   = None;
        self.stack  = [];
        
    def _stack(self, data):
        self.stack.append(data);
        
    def insert(self, data) -> None:
        newNode = BinaryTreeNode(data);
        self.stack.append(newNode)
        
        if(self.root == None):
            self.root = newNode;
        else:
            if(newNode.data.id < self.root.data.id):
                self.root.left = newNode;
            else:
                self.root.right = newNode;
                
        self.size += 1;
        
    def __iter__(self) -> None:
        return self;
    
    def __next__(self):
        curr =  self.stack[self._index];
        while(curr):
            yield curr;
            self._index += 1;
        raise StopIteration
        

class HashTable:
    def defineTable(self, func):
        return self._buildTable(LinkedList);
    
    def _checkSize(self) -> bool:
        return self.size / self.capacity <= 0.5;
    
    def _buildTable(self, func):
        if(func == None):
            func = LinkedList();
        return [func() for i in range(self.capacity)];
       
    def __resize(self):
        self._index     = 0;
        self.capacity  *= 2;
        self.table      = self._buildTable(LinkedList);
        
        for bucket in self.table:
            for element in bucket:
                if(element == None):
                    continue;
                else:
                    self.insert(element.data.id, element.data)

        
    
    def hash(self, key) -> int:
        h = hashlib.new('sha224');
        h.update(str(key).encode('utf-8'));
        return int(h.hexdigest(), base=16) % self.capacity;
        
        
    def insert(self, pair:tuple) -> bool:
        key, data = pair;
        
        #   Get hashkey from object
        hashkey = self.hash(key);
        
        #   Get bucket
        bucket = self.table[hashkey];
        
        #   Insert object into bucket
        bucket.insert(data);
        self.size += 1;
        
        #   Resize the hashtable?
        if(self._checkSize()):
            return;
        else:
            self.__resize();

    
    def __init__(self, capacity:int) -> None:
        self.capacity   = capacity;
        self.table      = self._buildTable(LinkedList);
        self.size       = 0;
        self._index     = 0;
        
    def __len__(self) -> int:
        return self.capacity;
    
    def __iter__(self):
        return self

    def __next__(self):
        if(self._index < self.capacity):
            currList = self.table[self._index];
            self._index += 1;
            return currList;
        else:
            raise StopIteration;
            
#   Singly Linked List
class LinkedList:
    __slots__ = 'head', 'size';
    
    def __init__(self) -> None:
        self.head = None;
        self.size = 0;
        
    def insert(self, data):
        self.size += 1;
        
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return str(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.__init__();
    
    def isEmpty(self) -> bool:
        return self.size == 0;
    
    def __len__(self) -> int:
        return self.size;
    


if __name__ == '__main__':
    ht = BinaryTree();
    for i in range((5)):
        ht.insert(Data(i));
    
    for l in ht:
        print(l)