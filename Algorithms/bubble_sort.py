# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements) #Calculating the size of elements

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j] #storing element in temporary variable
                elements[j] = elements[j+1] #Swapping the numbers
                elements[j+1] = tmp 
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    #elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print("Sorted strings array is as:",elements)



    