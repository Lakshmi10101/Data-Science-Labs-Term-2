# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:20:59 2023

@author: LAKSHMIPRIYA Anil
"""

# =============================================================================
# Helper file
# =============================================================================



# Node class for for individual nodees in expression tree
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None



# Implementing Stacks using Linked List

# Node class for the individual nodes
class StackNode:

    # constructor for StackNode class
    def __init__(self, data):
        # your code here
        self.data = data
        self.next = None
        

# Manager class to link the nodes and manage the overall list
class LinkedListStack:

    # constructor for LinkedListStack class
    def __init__(self):
        # your code here
        self.head = None


    # Push: Adds a new element at the back of the list
    def push(self, data):
        # your code here
        exp_node = Node(data)
        node = StackNode(exp_node)
        
        node.next = self.head
        self.head = node

    # Push: Adds a new element at the back of the list
    def push_node(self, exp_node):
        # your code here
        node = StackNode(exp_node)
        
        node.next = self.head
        self.head = node
            


    # Pop: Deletes the element at the last and returns the value of it
    def pop(self):
        # your code here
        if not self.isEmpty():
            top_node = self.head.data
            self.head = self.head.next
            return top_node
        return None
            


    # Returns the size of the stack
    def size(self):
        # your code here
        temp = self.head        # Initialise temp
        len_cnt = 0               # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            len_cnt += 1
            temp = temp.next
        return len_cnt


    # Return the element at the top of the stack without removing it
    def top(self):
        # your code here
        if not self.isEmpty():
            top_value = self.head.data.val
            return top_value
        return None

    def top_node(self):
        # your code here
        if not self.isEmpty():
            top_node = self.head.data
            return top_node
        return None


    # Return true is stack is empty, False if not
    def isEmpty(self):
        # your code here
        if self.size() == 0:
            return True
        return False


    def printIsEmpty(self):
        print("Stack is Empty\n") if self.isEmpty() else print("Stack is not Empty\n")


    # Reverses the stack
    def reverseList(self):
        # your code here
        temp = self.head
        rev_stck_LL = LinkedListStack()
        
        while(temp):
            rev_stck_LL.push(temp.data)
            temp = temp.next
        
        rev_stck_LL.printStack()


    def printStack(self):
        temp = self.head
        print("The Stack created is as follows (top to bottom):")
        while(temp):
            print (temp.data.val, end=" ")
            temp = temp.next
    
    def main(self):
        # Confirm the creation of an empty stack using isEmpty() method 
        print('Checking to see if the stack created is empty - ')
        self.printIsEmpty()
        
        # Inserting elements in the stack using push()
        self.push(3)
        self.push(5)
        self.push(6)
        self.push(2)
        self.push(18)
        self.push(15)
        self.push(4)
        
        # Checking the size of the stack after all the push operations
        print('The size of the stack after the all the push operations: ', self.size())
        
        # Checking the stack after all the push operations
        print('\nThe stack after the all the push operations: ')
        self.printStack()
        
        # Checking the value of the topmost element in the stack after all the push operations
        print('\n\nThe topmost element in the stack is: ', self.top())
    
        # Deleting the topmost element using pop()
        print('\nThe element removed from stack using pop() is: ', self.pop())
        
        # Checking the sixe of the stack after the pop operation
        print('\nThe size of the stack after the pop operation is: ', self.size())
    
        # Checking the value of the topmost element in the stack after the push operation
        print('The topmost element in the stack after the pop operation is: ', self.top())
        
        print('\nReversing the stack:')
        self.reverseList()
    
