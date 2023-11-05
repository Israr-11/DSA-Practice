# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr): #swapping elements values
    #a and b are indexes and arr is the actual array
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def quick_sort(elements, start, end):#elements array, start and end pointer
    if start < end:
        pi = partition(elements, start, end) #calling partition function
        quick_sort(elements, start, pi-1) #calling quick sort for left array of sorted pivot
        quick_sort(elements, pi+1, end)#calling quick sort for right array of sorted pivot


def partition(elements, start, end):
    pivot_index = start #start will contain the 0th index in this case or 0
    pivot = elements[pivot_index] #pivot will be first index or 11 here
    # print("The last index:", end)
    while start < end: #1st iteration-> 0 < 6
        while start < len(elements) and elements[start] <= pivot:
            start+=1
    
        while elements[end] > pivot:
            end-=1

        if start < end: #Mean do it till list or array end
            swap(start, end, elements)#swap end and start
    swap(pivot_index, end, elements) #swap the pivot

    return end



if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    #print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        # [3, 7, 9, 11],
        # [25, 22, 21, 10],
        # [29, 15, 28],
        # [],
        # [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')


