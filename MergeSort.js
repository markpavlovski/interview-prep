function merge (arr1, arr2) {
  let result = [];
  let i = 0
  let j = 0
  while (i < arr1.length && j < arr2.length){
    if (arr1[i] <= arr2[j]){
      result.push(arr1[i])
      i++
    } else {
      result.push(arr2[j])
      j++
    }
  }

  if (i < arr1.length) return result.concat(arr1.slice(i))
  if (j < arr2.length) return result.concat(arr2.slice(j))

  return result
}


merge([1,2,8,9,100],[3,4,7])
merge([],[3,4,7])

// Now to sort:

merge(merge([1],[3]),merge([10],[2]))

function mergeSort(arr){

  if (arr.length <= 1) return arr

  const mid = Math.floor(arr.length/2)
  const left = arr.slice(0,mid)
  const right = arr.slice(mid)

  return merge(mergeSort(left), mergeSort(right))

}

mergeSort([1,2,10,4,5,6,7])
mergeSort([7,17,23,16])
