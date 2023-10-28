class Node:

    #Node class represents the indivisual element in the node and it contains
    # 1) next's address and 2) value of the specific node

    #Equivalent of constructor somehow in js and see here self is like this, init is a 
    #built in method of a class
    #We use __init__ method or function to assign the values to the class

    #In Linked list we usually have a node that contain value and address to the next node that is
    #being defined below in __init__ method

    def __init__(self, data=None, next=None) :
        self.data=data  #value at the node
        self.next=next    #pointer to the next element of the node

    #This is the class that has method pointing to itself
class LinkedList:
    def __init__(self):
        self.head=None   #head is pointing to next node's address

    def inserting_at_the_beginning(self, data):
        node= Node(data, self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        llstr=""

        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)
    
    def insert_at_the_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
    # if there are next values in the head then it will iterate over them 
    # and will iterate untill itr.next is none and that will end and we have to 
    #put node out there
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
    
    def insert_lot_of_values(self, data_list):
        self.head=None
        for data in data_list:
            self.insert_at_the_end(data)
            #print(values_at_end)
    
    
    def get_length_of_linkedlist(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next   #iterate unitll itr.next is none mean the last node
        return count

    def remove_specific_element(self, index):
        
        if index<0 or index>=self.get_length_of_linkedlist():
             raise Exception("Invalid index")
        
        if index==0: #If index==0 then its last 
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count +=1


    def insert_specific_element(self, index,data):
        
        if index<0 or index>=self.get_length_of_linkedlist():
             raise Exception("Invalid index")
        
        if index==0: #If index==0 then its last 
            self.inserting_at_the_beginning(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data, itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1

    

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_lot_of_values(["Ali", "Israr", "Pakistan"])
    #ll.remove_specific_element(1)
    ll.insert_specific_element(1, "hello")
    ll.print()
    print("Length of linked list is as:", ll.get_length_of_linkedlist())



