
function selectionSort(array){
  if (!array.length) return []
  const minIdx = array.reduce((acc, val, idx) => val < acc.val ? {val, idx} : acc, {idx:0, val: array[0]}).idx
  const minVal = array.splice(minIdx,1)[0]
  return [minVal, ...selectionSort(array)]
}

selectionSort([6,2,11,3,4,5])
