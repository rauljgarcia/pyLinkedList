class Node:
    '''
    Create and initialize Node class instance.
    '''
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    '''
    Create and initialize LinkedList class instance.
    '''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        '''
        Insert data to the end of the linked list.
        
        Parameters:
        value: data type of node
        
        Returns: True 
        '''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

    def prepend(self, value):
        '''
        Insert data to the beginning of the linked list.

        Parameters:
        value: data type of node
        
        Returns: True 
        '''
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True 
    
    def pop_first(self):
        '''
        Remove the first node and return the node's data.
        '''
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        if self.length == 1:
            self.head = None
            self.tail = None
            temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def pop(self):
        '''
        Remove the last node and return the node's data.
        '''
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index):
        '''
        Gets and returns the value of the node at a given index
        '''
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def print_list(self):
        '''
        This method prints every node's data.
        '''
        temp = self.head
        str = ''
        while temp is not None:
            str += (f'{temp.value}->')
            temp = temp.next
        print(f'\t   {str}'+ 'None')
