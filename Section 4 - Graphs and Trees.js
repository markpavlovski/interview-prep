
class GraphNode {
  constructor(val, adj = []){
    this.val = val
    this.adj = adj
    this.visited = false
  }
}

class TreeNode {
  constructor(val, children = []){
    this.val = val
    this.children = children
  }
}

class BinaryTreeNode {
  constructor(val, left = null, right = null){
    this.val = val
    this.left = left
    this.right = right
  }
}

class ListNode{
  constructor(val, next=null){
    this.val=val
    this.next = next
  }
}


class Queue {
  constructor(val){
    this.head = null
    this.tail = null

    if (val) this.enqueue(val)
  }

  enqueue(val){
    const newTail = new ListNode(val)
    if (this.isEmpty()) {
      this.head = newTail
      this.tail = newTail
    } else {
      this.tail.next = newTail
      this.tail = newTail
    }
  }

  dequeue(){
    if (this.isEmpty()) return null
    const currHead = this.head
    this.head = currHead.next
    if (!this.head) this.tail = null
    return currHead.val
  }

  isEmpty(){
    return this.head ? false : true
  }
}


const q = new Queue()
// console.log(q)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
q.dequeue()
// console.log(q)

/* Test Binary Tree

        14

    10      17

8         15    21

  9

*/

const testTree = new BinaryTreeNode(14,
  new BinaryTreeNode(10,
    new BinaryTreeNode(8,
      null,
      new BinaryTreeNode(9)
    ),
    null
  ),
  new BinaryTreeNode(17,
    new BinaryTreeNode(15),
    new BinaryTreeNode(21)
  )
)

// console.log(testTree)


//


const dfsPreOrder = node => {
  if (!node) return null
  console.log(node.val)
  dfsPreorder(node.left)
  dfsPreorder(node.right)
}

// dfsPreOrder(testTree)


const dfsInOrder = node => {
  if (!node) return null
  dfsInOrder(node.left)
  console.log(node.val)
  dfsInOrder(node.right)
}

// dfsInOrder(testTree)



const dfsPostOrder = node => {
  if (!node) return null
  dfsPostOrder(node.left)
  dfsPostOrder(node.right)
  console.log(node.val)
}
//
// dfsPostOrder(testTree)
//




const bfs = node => {
  const queue = new Queue(node)
  while (!queue.isEmpty()){
    const curr = queue.dequeue()
    console.log(curr.val)
    if (curr.left) queue.enqueue(curr.left)
    if (curr.right) queue.enqueue(curr.right)
  }
}

bfs(testTree)







//
