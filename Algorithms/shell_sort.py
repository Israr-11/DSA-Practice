def shell_sort(arr):
    size = len(arr)
    gap = size//2 #total elements divide by 2 is the gap
    print("The gap is as:", gap)
    while gap > 0: 
        for i in range(gap,size):
    #anchor mean currently focused element
            anchor = arr[i]
            print("Anchor value:", anchor)

#For first iteration of array=>[89,78,61,53,23,21,17,12,9,7,6,2,1] 
# gap=6          
#Anchor value: 17
#The value of arr[j]: 17
#The value of arr[j-gap]: 89

#NOW, REMEMBER AFTER SORTING WE ARE DOING J AS GAP-1 
#ALSO WE ARE DOING GAP//2

            j = i#ASSIGNING i to j
    #j here shows the element previous element wrt to anchor
            while j>=gap and arr[j-gap]>anchor:
    #arr[j] is the anchor element
                print("The value of arr[j]:", arr[j])
                print("The value of arr[j-gap]:", arr[j-gap])

                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        # [],
        # [1,5,8,9],
        # [234,3,1,56,34,12,9,12,1300],
        # [5]
    ]
    elements = [89,78,61,53,23,21,17,12,9,7,6,2,1]
    for elements in tests:
        shell_sort(elements)
        print(elements)