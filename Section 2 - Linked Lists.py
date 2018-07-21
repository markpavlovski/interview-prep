class Node:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.nxt = nxt


# For Testing
sll = Node(2,Node(3,Node(2,Node(7,Node(3,Node(2,None))))))
ll = Node(1, sll)
z = ll
while z:
  print(z.val)
  z = z.nxt

"""
2.1 Remove Duplicates
"""

def removeDups(head):
  d= {head.val:1}
  prev = head
  curr = head.nxt
  while curr:
    if curr.val in d:
      curr = curr.nxt
    else:
      d[curr.val] = 1
      prev.nxt = curr
      prev = curr
      curr = curr.nxt
  prev.nxt = None # this is important



# removeDups(ll)
# print('\n')

# x = ll
# while x:
#   print(x.val)
#   x = x.nxt

"""
2.2 Return K'th to last, assuming k > 0
"""

def kToLast(head, k):
  counter = 0
  slow = None
  fast = head
  while fast.nxt:
    fast = fast.nxt
    if slow:
      slow = slow.nxt
    counter += 1
    if counter == k :
      slow = head

  return slow

# print('!!',kToLast(ll,3).val)
# print('!!',kToLast(ll,2).val)


# Nice recursive solution suggested by the book, if we only want to print the value.
def kToLastRec(head, k):
  if not head.nxt:
    return 0

  index = kToLastRec(head.nxt,k) + 1
  if index == k :
    print(head.val)

  return index



kToLastRec(ll,20)

"""
2.3 Delete a node in the middle
"""

def delMiddleNode(head, node):
  curr = head
  while curr:
    if curr.nxt == node:
      curr.nxt = node.nxt
      break
    curr = curr.nxt


def delMiddleNodeClean(node):
  node.val = node.nxt.val
  node.nxt = node.nxt.nxt


# delMiddleNode(ll, sll)
# delMiddleNodeClean(sll)

# x = ll
# while x:
#   print(x.val)
#   x = x.nxt



"""
2.4 Partition so that all nodes with values smaller than the target are on the left side, and teh rest are on teh right
"""

def partition(head, val):
  pHead = head
  pTail = head
  curr = head.nxt

  while curr:
    if curr.val < val:
      pHead = Node(curr.val, pHead)
    else:
      newNode = Node(curr.val)
      pTail.nxt = newNode
      pTail = pTail.nxt
    curr = curr.nxt

  return pHead

print('\n')
lll = Node(2,Node(3,Node(2,Node(7,Node(3,Node(5,None))))))

# x = partition(lll,5)
# while x:
#   print(x.val)
#   x = x.nxt

"""
2.5 Sum Lists
"""

def sumList(headA,headB, carry=0):
  if not headA and not headB:
    if carry:
      return Node(carry, None)
    else:
      return None
  if not headA:
    curr = Node((headB.val + carry) % 10)
    if headB.val + carry > 9:
      carry = 1
    else:
      carry = 0
    nextNode = headB.nxt
    curr.nxt = nextNode
    return curr
  if not headB:
    curr = Node((headA.val + carry) % 10)
    if headA.val + carry > 9:
      carry = 1
    else:
      carry = 0
    nextNode = headA.nxt
    curr.nxt = nextNode
    return curr
  else:
    curr = Node((headA.val + headB.val + carry) % 10)
    if headA.val + headB.val + carry > 9:
      carry = 1
    else:
      carry = 0
    nextNode = sumList(headA.nxt, headB.nxt, carry)
    curr.nxt = nextNode
    return curr

lA = Node(3,Node(2,Node(6,None)))
lB = Node(7,Node(5,Node(4,None)))


# x = sumList(lA, lB)
# while x:
#   print(x.val)
#   x = x.nxt

# print(x.val)
# print(x.nxt.val)


"""
2.5 isPalindrome
"""

def reverseInPlace(head):
  if not head.nxt:
    return head

  nextNode = head.nxt
  nextHead = reverseInPlace(nextNode)
  head.nxt = None
  nextNode.nxt = head

  return nextHead

def reverseNew(head):
  newHead = None
  curr = head
  while curr:
    newHead =Node(curr.val, newHead)
    curr = curr.nxt
  return newHead


x = reverseNew(ll)
while x:
  print(x.val)
  x = x.nxt

def isPalindrome(head):
  currHead = head
  revHead = reverseNew(head)
  print(currHead.val, revHead.val)
  print(currHead.nxt, revHead.nxt)


  while head:
    print(head.val, revHead.val)
    if head.val != revHead.val:
      return False
    head = head.nxt
    revHead = revHead.nxt
  return True


pll = Node(1,Node(2,Node(3,Node(2,Node(1,None)))))
print(isPalindrome(pll))
