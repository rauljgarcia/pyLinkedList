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
        curr = self.head
        self.head = self.tail
        self.tail = curr
        pre = None
        next = None
        while curr is not None:
            next = curr.next
            curr.next = pre
            pre = curr
            curr = next
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

    def find_middle_node(self):
        '''
        Find and return a pointer for middle node of the linked list.

        Parameters: none

        Returns:
        temp: pointer to the data
        '''
        fast_ptr = self.head
        slow_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    
    def partition_list(self, k):
        '''
        Partition a linked list at x and maintain its relative order

        Parameters:
        k: the partitioning value

        Returns: None
        '''
        if self.head is None:
            return None
        dummy1 = dummy2 = Node(0) 
        prev1, prev2 = dummy1, dummy2
        cur = self.head
        while cur is not None:
            if cur.value < k:
                prev1.next = cur
                prev1 = cur
            else:
                prev2.next = cur
                prev2 = cur
            cur = cur.next
        prev1.next = dummy2.next
        prev2.next = None
        dummy1 = dummy2 = prev1 = prev2 = None

def has_cycle(ll):
    '''
    Function takes a linked list and checks if it has a cycle

    Parameters:
    ll: linked list

    Returns:
    True: if the linked list has a cycle
    False: if the linked list does not have a cycle
    '''
    fast_ptr = ll.head
    slow_ptr = ll.head
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if fast_ptr == slow_ptr:
            return True
    return False

def find_kth_from_end(ll, k):
    '''
    Function returns the k-th node from the end of the linked list
     without using length method

     Parameters:
     ll: linked list
     k: The k-th node

     Returns:
     Pointer to the k-th node from end of the linked list
    '''
    fast_ptr = ll.head
    slow_ptr = ll.head
    for i in range(k):
        if fast_ptr is None:
            return None
        fast_ptr = fast_ptr.next
    while fast_ptr is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
    return slow_ptr