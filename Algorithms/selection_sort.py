
def selection_sort(arr):
    size = len(arr)
    #array=[89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
    print("The size of the array is:", size)
    for i in range(size-1):

    #The size of the array is: 13
    # The i value: 0
    # The value of j is as: 1
    # The value of j is as: 2
    # The value of j is as: 3
    #j is the value in the array on which pointer is pointing to and min_index is the 
    #minimum index
        print("The i value:", i)
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                print("The value of j is as:", j)
                min_index = j
        if i != min_index:
#Its like arr[i]=arr[min_index] & arr[min_index]=arr[i]
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        # [],
        # [1,5,8,9],
        # [234,3,1,56,34,12,9,12,1300],
        # [78, 12, 15, 8, 61, 53, 23, 27],
        # [5]
    ]
    for elements in tests:
        selection_sort(elements)
        # print(elements)