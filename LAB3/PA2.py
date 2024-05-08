# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:37:49 2023

@author: LAKSHMIPRIYA Anil
"""

# Node class for individual nodes in doubly linked list
class Node:
    # Constructor for Node class
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class HashTableChain:
    # Constructor for Hash Table with chaining implementation
    def __init__(self, size, file):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        self.filename = file

    # hash function to determine the index for a given key
    def hash_function(self, key):        
        hash_index = 0
        for char in key:
            hash_index = (hash_index * self.g + ord(char)) % self.size
        return hash_index
        

    # insert a key-value pair to the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        
        if self.table[index] is None:
            # Create an instance of a node with the given key and insert it to table
            new_node = Node(key, value)
            self.table[index] = new_node
            
        else:
            head = self.table[index]            
            
            while head:
                existing_key = head.key
                if existing_key != key: 
                    if head.next:
                        head = head.next
                    else:
                        # Create an instance of a node with the given key and insert it in linked list
                        new_node = Node(key, value)
                        head.next =  new_node
                        new_node.prev = head
                        break
                else:
                    # Update the existing key with the new value
                    if head.prev == None:
                        # The current node is the beginning node in the linked list
                        if head.next:
                            # Remove the previous instance of the key
                            head.next.prev = None
                            self.table[index] = head.next
                            head = None
                            
                            # Create a new instance of the key with updated value
                            new_node = Node(key, value)
                            new_head = self.table[index]
                            
                            # Insert the new instance of the key in the linked list of the hash table
                            new_node.next = new_head
                            new_head.prev = new_node
                            self.table[index] = new_node
                            
                            '''
                            # Equivalent to
                            new_node = Node(key, current_val + 1)
                            new_node.next = head.next
                            head.next.prev = new_node
                            head = None
                            self.table[index] = new_node '''
                            
                        else:    # The current node is the only node in the linked list
                            # Remove the previous instance of the key
                            head = None
                            self.table[index] = None
                            
                            # Create a new instance of the key with updated value and insert it
                            new_node = Node(key, value)
                            self.table[index] = new_node
                            
                    else:    # The current node is not at the beginning of the linked list 
                       # Remove the previous instance of the key
                       if head.next:
                           head.prev.next = head.next
                           head.next.prev = head.prev 
                       else:
                           head.prev.next = None  
                       head = None
                       
                       # Create a new instance of the key with updated value
                       new_node = Node(key, value)
                       head_list = self.table[index]
                       
                       # Insert the new instance of the key at the beginning of the linked list
                       new_node.next = head_list
                       head_list.prev = new_node     
                       self.table[index] = new_node
                       
        

    # retrieve the value for a given key
    def search(self, key):
        index = self.hash_function(key)
        
        if self.table[index] is None:
            # Search unsuccessful - No entries for given index
            return None
        
        head = self.table[index]        
        while head:
            existing_key = head.key
            if existing_key != key: 
                if head.next:
                    head = head.next
                else:
                    # Search unsuccessful - End of linked list
                    return None
            else:
                # Search successful
                return head.value
        
        
    

    def delete(self, key):
        index = self.hash_function(key)
        
        if self.table[index] is None:
            # Index corresponding to key doesn't exist
            return
        
        head = self.table[index]        
        while head:
            existing_key = head.key
            if existing_key != key: 
                if head.next:
                    head = head.next
                else:
                    # Key doesn't exist in linked list of corresponding index
                    break
            else:
                # Key found in linked list
                
                # The current node is the beginning node in the linked list
                if head.prev == None:
                    # If there are more than one nodes in the linked list
                    if head.next:
                        head.next.prev = None
                        self.table[index] = head.next
                      
                    # The current node is the only node in the linked list
                    else:                           
                        self.table[index] = None
                
                # The current node is not at the beginning of the linked list       
                else: 
                    # The current node is not at the end of the linked list
                    if head.next:
                        head.prev.next = head.next
                        head.next.prev = head.prev  
                        
                    # The current node is at the end of the linked list
                    else:
                        head.prev.next = None                        
                head = None
        
     

# =============================================================================                  

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTableLinProb:
    def __init__(self, size, file):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        self.deleted = HashNode(-1, -1)
        self.filename = file
        

    # hash function to determine the index for a given key
    def hash_function(self, key):       
        hash_index = 0
        for char in key:
            hash_index = (hash_index * self.g + ord(char)) % self.size
        return hash_index


    # insert a key-value pair to the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        probe_count = 0
        
        '''
        While the index position is occupied 
            and the value at that position has not been deleted before, 
            update the index to the next consecutive value'''
        while self.table[index] and self.table[index].key != -1:
            current_key = self.table[index].key
            if current_key == key:
                self.table[index] = HashNode(key, value)
                break
            
            index = (index + 1) % self.size  # Linear probing
            probe_count += 1
            
            if probe_count == self.size:
                try:
                    raise Exception('Hash table overflow!')
                except Exception as e:
                    print(e)
                    self.size *= 2
                    print(f'Mitigation - Hash table capacity doubled to {self.size}.')                    
                    temp_table = [None] * self.size
                    temp_table[:self.size//2]
                    self.table = temp_table
                    index = (probe_count) % self.size
                    break
          
        '''
        If the index position is not occupied 
            or the value at that position has been deleted before, 
            insert the value at this index'''
        if not self.table[index] or self.table[index].key == -1:
            self.table[index] = HashNode(key, value)
        



    # retrieve the value for a given key
    def search(self, key):        
        index = self.hash_function(key)
        probe_count = 0
        
        while self.table[index]:
            if probe_count == self.size:    # Unsuccessful search - to avoid infinite loop
                return None                  
            
            item_node = self.table[index]
            current_key = item_node.key
            if current_key == key:          # Successful search
                return item_node.value
            index = (index + 1) % self.size
            probe_count += 1
        


    def delete(self, key):
        index = self.hash_function(key)
        probe_count = 0
        
        while self.table[index]:
            if probe_count == self.size:    # Unsuccessful search - to avoid infinite loop
                break                   
            
            item_node = self.table[index]
            current_key = item_node.key
            if current_key == key:          # Successful search
                self.table[index] = self.deleted
                break
            index = (index + 1) % self.size
            probe_count += 1
            

        

# =============================================================================


class HashTableDoubleHash:
    def __init__(self, size, file):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        self.filename = file
        

    # hash function to determine the index for a given key
    def hash_function(self, key):       
        hash_index = 0
        for char in key:
            hash_index = (hash_index * self.g + ord(char)) % self.size
        return hash_index
    
    
    # hash function to determine the offset for a given key
    def hash_function2(self, key):    
        '''
        Parameters
        ----------
        key : A string
            Represents a word from dictionary.

        Returns
        -------
        int
            The offset from the initial probe position.
            
        Strategy
        -------
        Auxillary function h2(k) = 1 + ASCII_sum(key) % m'
            where m' is slightly smaller than hash table size m
                  m is prime
                  h2(k) and m are relatively prime so that the entire hash table is probed.

        '''
        hash_offset = 0
        for char in key:
            hash_offset += (ord(char)) % (self.size - 1)
        return 1 + hash_offset % (self.size - 1)


    # insert a key-value pair to the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        probe_count = 0
        
        '''
        While the index position is occupied, 
            update the index with the hash offset'''
        while self.table[index]:
            current_key = self.table[index].key
            if current_key == key:
                self.table[index] = HashNode(key, value)
                break
            
            index = (index + (probe_count + 1) * self.hash_function2(key)) % self.size  # Double hashing
            probe_count += 1
            
            if probe_count == self.size:
                try:
                    raise Exception('Hash table overflow!')
                except Exception as e:
                    print(e)
                    self.size *= 2
                    print(f'Mitigation - Hash table capacity doubled to {self.size}.')                    
                    temp_table = [None] * self.size
                    temp_table[:self.size//2]
                    self.table = temp_table
                    index = (probe_count) % self.size
                    break
          
        '''
        If the index position is not occupied,
            insert the value at this index'''
        if not self.table[index]:
            self.table[index] = HashNode(key, value)
        



    # retrieve the value for a given key
    def search(self, key):        
        index = self.hash_function(key)
        probe_count = 0
        
        while self.table[index]:
            if probe_count == self.size:    # Unsuccessful search - to avoid infinite loop
                return None                  
            
            item_node = self.table[index]
            current_key = item_node.key
            if current_key == key:          # Successful search
                return item_node.value
            index = (index + (probe_count + 1) * self.hash_function2(key)) % self.size
            probe_count += 1
        


    def delete(self, key):
        index = self.hash_function(key)
        probe_count = 0
        
        while self.table[index]:
            if probe_count == self.size:    # Unsuccessful search - to avoid infinite loop
                break                   
            
            item_node = self.table[index]
            current_key = item_node.key
            if current_key == key:          # Successful search
                self.table[index] = None
                break
            index = (index + (probe_count + 1) * self.hash_function2(key)) % self.size
            probe_count += 1
            
        
# Create a hash table from the given file
def create_hash_table(obj): 
    with open(obj.filename, 'r') as my_dictionary:
        for line in my_dictionary:
            word = line.strip()
            search_result = obj.search(word)
            if search_result:
                new_count = search_result + 1
                obj.insert(word, new_count)
            else:
                obj.insert(word, 1)
                    
                
# Create a txt file to display the hash table
def export_hash_table(obj, filename):  
        with open(filename, 'w') as file:
            
            for head in obj.table:                
                # If there's a linked list at this index
                if head:
                    if type(head) == Node:
                        while head.next:                        
                            file.write(f'{head.key} {head.value}\n')
                            head = head.next
                        else:
                            file.write(f'{head.key} {head.value}\n')
                            
                    if type(head) == HashNode:
                        file.write(f'{head.key} {head.value}\n')
        
                   
# =============================================================================


if __name__ == '__main__':
    htc = HashTableChain(581, 'dictionary.txt')
    create_hash_table(htc)
    filename = 'Chaining.txt'  
    export_hash_table(htc, filename)

    word_count =  0
    with open(filename, 'r') as my_word_freq_file:
                for line in my_word_freq_file:
                  word_count += 1
    print(word_count)
    
    htlp = HashTableLinProb(14533, 'dictionary.txt')
    create_hash_table(htlp)
    filename = 'Probing.txt'  
    export_hash_table(filename)

    htdh = HashTableDoubleHash(14533, 'dictionary.txt')
    create_hash_table(htdh)
    filename = 'DoubleHashing.txt'  
    export_hash_table(htdh, filename)