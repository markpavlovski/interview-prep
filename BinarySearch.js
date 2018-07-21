
function binarySearch (array, num) {
   low = 0
   high = array.length
   while (low <= high){
     mid = low + Math.floor((high-low)/2)
     if (array[mid] === num) return mid
     if (num < array[mid]) {
       high = mid
     } else {
       low = mid + 1
     }
   }
   return -1
}


binarySearch([2,3,4,5],5)
