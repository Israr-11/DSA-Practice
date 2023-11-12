#When we have a unsorted array and want to apply the merge sort algos on it to convert into
#sorted array
def merge_sort(arr):
    if len(arr) <= 1: #if arrays size is one return the exact same array
        return arr
    
#mid = len(arr) // 2: Calculates the midpoint of the array by integer division. 
# This gives you the index where the array will be split into two halves.

#left = arr[:mid]: Creates a new list (left) containing elements from the beginning 
# of the original array (arr) up to, but not including, the midpoint.

#right = arr[mid:]: Creates another new list (right) containing elements from the 
# midpoint to the end of the original array.

    mid = len(arr)//2 #if not 1 element it will divide it into two

    left = arr[:mid] #starting index
    right = arr[mid:] #ending index

#Recursively call the merge sort to get the sorted arrays, like divide, divide and divide
#to get single element array that by defalt was sorted
    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    sorted_list = [] #Empty at the beginning

    len_a = len(a) #length of array a
    len_b = len(b) #length of array b

    i = j = 0 #initialization of i and j pointers to zero

    while i < len_a and j < len_b: #pass over the arrays untill they are finished
        if a[i] <= b[j]: #element in the second list is higher than the element in the first list
            sorted_list.append(a[i])#put the current element of first list in sorted list
            i+=1 #increment the pointer of first list
        else:
            sorted_list.append(b[j]) #else append the element of second array in sorted
            #array
            j+=1
#Now, what if array a finish before the array b then pointer will not go on the other unfinished
#array, so for that case we will have to handle the scenario indiviually after exiting above loop
    while i < len_a:#move on the single array and place the sorted in the list
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

if __name__ == '__main__':
    arr = [10,3,15,7,8,23,98,29]

    #print(merge_sort(arr))
