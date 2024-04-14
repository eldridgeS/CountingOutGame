
#Create the node class that we will use to create the linked list
class Node():
    def __init__(self, index):
        self.index = index
        self.next = None

#Create the function that will simulate our game "One potato, Two Potato"
#Our function takes in two arguments, n (number of people) and K (number of steps)
def task1_game(n, k):

    #firstly we need to create the circular linked list

    head = Node(0) #we need the linked list to exist outside the for loop
    current = head #use current as a pointer
    for i in range(1,n):
        new_node = Node(i) #create a new node
        current.next = new_node #let the current's next node be the new node created
        current = new_node #move the pointer to the next node for next iteration

    current.next = head #Created the linked list, point the tail to head (circular)

    #Next, we need to run the counting algorithm
    
    #base case: when there is only one node left -> next pointer points to current
    #use a while loop so can run the steps as long as we need
    while current.next != current:

        #step k-1 times, and we skip over the node at the kth step
        for j in range( k-1): 

            current = current.next
             
        current.next = current.next.next

    #At this point, we only have 1 Node left, so return that Node's index
    return current.index
