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
        value: appropriate data type being added
        
        Returns: 
        True: bool to show data was successfuly added
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
        value: appropriate data type being added
        
        Returns:
        True: bool to show data was successfuly added
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

        Parameters: none

        Returns: 
        temp: pointer to the data that was removed
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

        Parameters: none

        Returns:
        temp: pointer to the data that was removed
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
        Get and return a pointer to the data at a given index.

        Parameters:
        index: integer of the index to get

        Returns:
        temp: pointer to the data
        '''
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        '''
        Set a new value to the data at a given index.

        Parameters:
        index: integer, the index of the data being modified
        value: appropriate value being set to the data at the index

        Returns:
        True: bool to show data was successfuly set
        False: bool to show data was not sucessfully set
        '''
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        '''
        Insert data at a given index in the linked list 

        Parameters:
        index: integer, index in the list where the data is added
        value: appropriate value being set to the data

        Returns:
        True: bool to show data was successfuly added
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        '''
        Delete data at a given index in the linked list.

        index: integer, index in the list where the data is removed

        temp: pointer to the data being removed
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        '''
        Reverse the order of the data in the linked list.

        Parameters: none

        Returns:
        True: Bool to show linked list was sucessfully reversed
        '''
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

    def print_list(self):
        '''
        Print the linked list in order.

        Parameters: none

        Returns: None
        '''
        temp = self.head
        str = ''
        while temp is not None:
            str += (f'{temp.value}->')
            temp = temp.next
        print(f'\t   {str}'+ 'None')