from tkinter import Tk, Label, Text, Button, Entry, END
from tkinter.messagebox import showinfo
import math

#linked list
class Node():
    def __init__(self, index):
        self.index = index
        self.next = None

#My code for the implmentation of the counting out game from the previous hw
# def task1_game(n, k):
#     head = Node(0)
#     current = head
#     for i in range(1,n):
#         new_node = Node(i)
#         current.next = new_node
#         current = new_node
#     current.next = head

#     while current.next != current:
#         for j in range( k-1): 
#             current = current.next
#         current.next = current.next.next
#     return current.index

# Main function that runs the game in sequence
def compute():
    global n_entry
    global k_entry
    global k
    global current
    global label_list
    n = int(n_entry.get())
    k = int(k_entry.get())

    #if it meets the given criteria, then continue with the game, or else showinfo to the user
    if n > 1 and n < 12 and k >= 1:
        txt.insert(END, f'Game Started. N ={n} K ={k}\n')

        label_list = [] #stores the labels of the players in a list so we can access all by index and delete them later in game sequence

        #creates the head node and corresponding label
        head = Node(0)
        head_label = Label(master=root, text=f' {head.index} ', borderwidth=2, font = 'custom_font' , relief='groove')
        head_label.grid(row=4, column = 4)
        label_list.append(head_label)

        #create the other nodes and their labels
        current = head
        for i in range(1,n):
            new_node = Node(i)
            current.next = new_node
            current = new_node
            current_label = Label(master=root, text=f' {current.index} ', borderwidth=2, font = 'custom_font', relief = 'groove')
            current_label.grid (row=4, column=4+i)
            label_list.append(current_label)
        current.next = head

        #appear the eliminate button once all the node labels are created
        eliminate_button = Button(root, text='Eliminate', command = eliminate)
        eliminate_button.grid(row=3,column=2)

        #count the number of rounds so we can display it on the display text
        global counter
        counter = 1 

    else:
        showinfo(message='Allowed values: \n 1<n<12 \n k>=1')

#implementation of the eliminate button
def eliminate():
    global label_list
    global counter
    global current

    #uses the counting out method for linked list, then deletes the last node and its label
    txt.insert(END, f'Round {counter}: ')
    for j in range(k-1):
        current=current.next
    txt.insert(END, f'Player {current.next.index} has been eliminated!\n')
    label_list[current.next.index].destroy()
    current.next = current.next.next
    counter += 1

    #if there is only one node left, end the game and print the messages
    if current.next == current:

        showinfo(message =f'WINNER: Player {current.index}')
        txt.insert(END, f'WINNER of this round is Player {current.index}\n')
        label_list[current.index].destroy()
        txt.delete('1.0', 'end')

#main tkinter implementation
root = Tk()
root.geometry('900x750')
root.title('Counting-out Game')
custom_font = ('Arial, 22')

#n and k labels and entries
n_label = Label(master=root, text= 'N: ', font = custom_font)
n_label.grid(row=1, column = 0)
k_label = Label(master=root, text= 'K: ', font = custom_font)
k_label.grid(row = 2, column = 0)
n_entry = Entry(root)
n_entry.grid(row = 1, column = 1)
k_entry = Entry(root)
k_entry.grid(row = 2, column = 1)

#create the start button
start_button = Button(root, text='Start', command = compute)
start_button.grid(row = 3, column = 1)

buffer_label = Label(root, text = '                   ', ) #extra invisible label just so stuff is stable and doesnt shift around
buffer_label.grid(row=4, column = 2)



txt = Text(master=root, width = 70, height = 50)
txt.grid(row = 10, column = 4, columnspan = 11)

root.mainloop()

