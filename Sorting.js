// Merge Sort

const merge = (a,b) => {
  if (!a.length) return b
  if (!b.length) return a

  const curr = (a[a.length-1] >= b[b.length-1]) ? a.pop() : b.pop()
  const result = merge(a,b)
  result.push(curr)
  return result
}


const x = [1,1,2,3,5,8,13]
const y = [14]

console.log(merge(x,y))

const mergeSort = arr => {
  if (arr.length<=1) return arr
  const middle = arr.length/2
  const left = []
  const right = []
  arr.forEach((el,idx) => idx < middle ? left.push(el) : right.push(el))
  return merge(mergeSort(left),mergeSort(right))
}

console.log(mergeSort([4,2,4,6,8,2,90,23]))
