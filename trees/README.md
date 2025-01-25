# Binary trees properties.
1. Maxium 2 nodes. 
2. Left.data < Rt.data, Right.data >= Rt.data

# Traversals
## Inorder
L Rt R - Left gets printed first, then root followed by right. Appropriate for sorting binary search trees. 
## Pre-order
Rt L R - Root gets printed first, then left followed by right.
## Post-order
L R Rt - Left gets printed first then right followed by right.

# Complete Binary Tree
A balanced binary tree has roughly the same number of nodes in the left and right subtrees of the root. The exception to this is the bottom level of the tree, which we fill in from left to right. Another interesting property of a complete tree is that we can represent it using a single list. We do not need to use nodes and references or even lists of lists. Because the tree is complete, the left child of a parent (at position *p*) is the node that is found in position *(2p+1)* in the list. Similarly, the right child of the parent is at position *(2p+2)* in the list. To find the parent of any node in the tree, we can simply use Python’s integer division. Given that a node is at position in the list, the parent is at position *((n-1))//2*




# Priority Queue
A priority queue acts like a queue in that you dequeue an item by removing it from the front. The highest priority items are at the front of the queue and the lowest priority items are at the back. The classic way to implement a priority queue is using a data structure called a **binary heap**. A binary heap will allow us both to enqueue and dequeue items in Olog(n).  A heap is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the heap property: in a max heap, for any given node C, if P is a parent node of C, then the key (the value) of P is greater than or equal to the key of C. In a min heap, the key of P is less than or equal to the key of C. The node at the "top" of the heap (with no parents) is called the root node

## 2 Variations of binary heap:
1. min heap - smallest key value is always at the front/root
2. max heap - largest key value is always at the front/root

