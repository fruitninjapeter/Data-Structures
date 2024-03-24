def listsum(numList):
   theSum = 0
   for i in numList:
      theSum = theSum + i
   return theSum


def max_list_iter(int_list):  # must use iteration not recursion
   max = None
   for i in int_list:
      if (max is None or i > max):
         max = i
   return max


print(max_list_iter([2,5,-2]))


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if len(int_list) == 1:
      return int_list
   else:
      return reverse_rec(int_list[1:]) + [int_list[0]]


print(reverse_rec([1,2,3]))


def binarySearch(alist,item):
   first = 0
   last = len(alist) - 1
   found = False

   while first <= last and not found:
      midpoint = (first + last) // 2
      if alist[midpoint] == item:
         found = True
      else:
         if item < alist[midpoint]:
            last = midpoint - 1
         else:
            first = midpoint - 1
   return found


def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if high >= low:
      mid = (high + low) // 2
      if int_list[mid] == target: # element is present in middle
         return mid

      elif arr[mid] > target: # element present left of mid within subarray
         return bin_search(target, low, mid - 1, int_list)

      else: # else element can be present right of mid within subarray
         return bin_search(target, mid + 1, high, int_list)

   else: # element not present in array
      return None


arr = []
x = 10

# Function call
result = bin_search(x, 0, len(arr) - 1, arr)


if result != None:
   print("Element is present at index", str(result))

else:
   print("Element is not present in array")