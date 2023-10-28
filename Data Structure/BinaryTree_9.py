class BinarySearchTreeNode:
    def __init__(self, data): #constructor in Python
        self.data = data #just like this.data=data
        self.left = None
        self.right = None


#Inserting in the binary tree
    def add_child(self, data):
        if data == self.data: #Value already exist, it cannot have duplication
            return # node already exist
        
        if data < self.data: #Mean value that we will enter is data and self.data is just like this.data
            if self.left:#if our entered value is less than existed then we will enter that to left
#When it calls itself recursively, it is essentially navigating down the tree to 
#find the appropriate location to insert a new node. 
#This recursive approach continues until it finds an appropriate spot to insert the new data.                
                self.left.add_child(data)#just calling recursively the left if its already there
            else:
                self.left = BinarySearchTreeNode(data)#adding if no left element
        else:
            if self.right: #if entered value is greater than enter that to right
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                

#searching through the binary tree
    def search(self, val): #we are searching val
        if self.data == val: #Lucky if value searching for exactly match the found value
            return True

        if val < self.data:#val is the entered value by us and it will comapre it to existed data
            if self.left:
                return self.left.search(val) #Recursively search value on the left
            else:
                return False #value doesn't exist in my left sub-tree

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

#in-order traversal mean root node to the midddle
    def in_order_traversal(self):
        elements = []
#self.left.in_order_traversal(): This part is a recursive call to the in_order_traversal() 
# method on the left subtree (the left child of the current node). 
# This call effectively traverses the left subtree in an in-order fashion, which means 
# it explores the left child, then the left child of the left child, and so on, until it 
# reaches the leftmost node.
# The result of this recursive call is a list of elements from the left subtree, 
# which represents the values of nodes in the left subtree in ascending order.
# elements += ...: The elements list is extended by concatenating the list of 
# elements obtained from the left subtree using the += operator. This means that 
# the elements from the left subtree are added to the end of the elements list.
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0]) #Making root node

    for i in range(1,len(elements)): #Now, after root add other elements
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    #print("UK is in the list? ", country_tree.search("UK"))
    #print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    #print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Searching for the value-> ", numbers_tree.search(1))