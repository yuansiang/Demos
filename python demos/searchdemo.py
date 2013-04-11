######LINEAR SEARCH######
##def linear_search(elements, target):
##    for i in range (len(elements)):
##        if elements[i] == target:
##            return "yes"
##    return -1
##
##items = [3,1,4,2,5]
##x = int(input("Search for what "))
##print(linear_search(items, x))

########BINARY SEARCH########
####def binary_search(elements, target, low, high):
####    mid = (low + high) // 2
####    if low > high: #case for not found
####        return -1
####    elif elements[mid] ==  target: #case for found
####        return mid
####    elif target < elements[mid]: #case for recursion 1
####        return binary_search(elements, target, low, mid-1)
####    else: #cause for target > elements , case for recursion 2
####        return binary_search(elements,target, mid+1, high)
####
####items = [1,2,3,4,5]
####x = int(input(" enter x "))
####print(binary_search(items,x,0,len(items)-1))

######Bubble Sort######
##def bubble_sort(A):
##  swapped = True # assume not sorted
##  while swapped:
##    swapped = False
##    for i in range(1,len(A)):
##      if A[i-1] > A[i]:
##        A[i-1], A[i] = A[i], A[i-1]
##        swapped = True
##  return A
##
### main
##A = [4, 5, 2, 1, 3]
##print(bubble_sort(A))
####good for small input size or when array/list is sorted 
####bad when large input size or when array/list is reversely sorted 
####worst case: O(n2)
####  (n - 1) + (n - 2)...(2) + (1) = n(n - 1)/2
####early termination efficiently built into algorithm

##########Insertion Sort######
######def insertion_sort(a):
######    for j in range(1, len(a)):
######        num = a[j]
######        i = j - 1
######        while (i >= 0 and a[i] > num):
######            a[i + 1] = a[i]
######            i = i - 1
######        a[i + 1] = num
######    return a
######
######x = insertion_sort([12,13,8])
######print(x)

###Quick Sort Efficiency###
def quicksort(elements):
  if elements == []:
    return []
  else:
    pivot = elements[0]

    less = []
    great = []

    for item in elements[1:]:
      if item < pivot:
        less.append(item)
      else:
        great.append(item)
        
    less = quicksort(less)
    great = quicksort(great)
    return less + [pivot] + great

print(quicksort([10, 23, 1, 17, 93, 10]))
        
