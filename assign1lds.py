#1. Delete the element in linked list:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def getNode(data):
    temp = ListNode(data)
    temp.next = None
    return temp
def printList(head):
    while (head.next):
        print(head.val, end=' -> ')
        head = head.next
    print(head.val, end='')
def removeZeroSum(head, K):
    root = ListNode(0)
    root.next = head
    umap = dict()
    umap[0] = root
    sum = 0
    while (head != None):
        if ((sum - K) in umap):
 
            prev = umap[sum - K]
            start = prev
            aux = sum
            sum = sum - K
            while (prev != head):
                prev = prev.next
                aux += prev.val
                if (prev != head):
                    umap.remove(aux)
            start.next = head.next
        else:
            umap[sum] = head
            head = head.next
    return root.next
head = getNode(1)
head.next = getNode(2)
head.next.next = getNode(-3)
head.next.next.next = getNode(1)
head.next.next.next.next = getNode(5)
head = removeZeroSum(head, 3)
if(head != None):
    printList(head)

#2. Reverse the linked list:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def reverse(self, head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)
        return prev
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
llist = linkedlist()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("\nGiven linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)
  
print ("\nReversed Linked list")
llist.printList()

#3. Merging the Linked list:
class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None
  
  
class LinkedList:
    def __init__(self):
        self.head = None
          
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end = '->')
            temp = temp.next
    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
        while p_curr != None and q_curr != None:
            p_next = p_curr.next
            q_next = q_curr.next
            q_curr.next = p_next  
            p_curr.next = q_curr 
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr
llist1 = LinkedList()
llist2 = LinkedList()
llist1.push(3)
llist1.push(2)
llist1.push(1)
llist2.push(4)
llist2.push(5)
llist2.push(6)
llist2.push(7)
print("\nFirst Linked List:")
llist1.printList()
  
print("\nSecond Linked List:")
llist2.printList()
llist1.merge(p=llist1, q=llist2)
  
print("\nModified first linked list:")
llist1.printList()
  
print("\nModified second linked list:")
llist2.printList()


#4. Count pairs given sum
from array import *
arr = array('i', [5,2,-1,3,4,-5])
sum = 1
def pairs(arr,sum):
    count = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                count =+1
    return count

print("\nCount of pairs:", pairs(arr,sum))

#5. Duplicate array:
from array import *
arr = array('i', [5,2,-1,3,4,5,2,1])
def duplicate(arr):
    org_arr = []
    dup_arr = []
    for i in arr:
        if i not in org_arr:
            org_arr.append(i)
        else:
            dup_arr.append(i)
    return dup_arr
print("Duplicates array:", duplicate(arr))

#6. Kth smallest and largest:
arr =  [12,3,5,7,19,9]
K = 3
def kthsmall(arr,K):
    arr.sort()
    return arr[0]
def kthlarge(arr,K):
    arr.sort()
    return arr[K]
print("Smallest No:", kthsmall(arr,K))
print("Largest No", kthlarge(arr,K))

# #7. Move negative elements one side:
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr.sort()
print("Moved a negative elements array:", arr)

#8. Reverse a string using Stack:

def reverse(string):
    stack = []
    for i in string:
        stack.append(i)
    print(stack)
    rev_str = ""
    for i in string:
        if stack != 0:
            popped = stack.pop()
            rev_str += popped
    return rev_str

print("Reversed string:"+ reverse('Laavanya'))

#9. Postfix expression;
class stack:
    def __init__(self, length):
        self.length = length
        self.array = []
    def push(self, x):
        self.array.append(x)
    def pop(self):
        if self.array != 0:
            return self.array.pop()
    def postfix(self, exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())
exp = "231*+9-"
obj = stack(len(exp))
print("Postfix of given expression:", obj.postfix(exp))

#10. Implement Queue:
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if self.queue == 0:
            return "Queue is empty"
        else:
           
            q = self.queue.pop(0)
            return q
que = Queue()
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que.dequeue())
print(que.dequeue())
print(que.dequeue())