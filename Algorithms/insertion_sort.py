
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        print("The anchor is as:", anchor) #The first element of the array here it is 11
        print("The i's value is as:", i) #i mean the index of current element with pointer on it
        j = i - 1 #j mean the index of left element like if pointer is on 9 then j will be 11
        print("The value of j is as:", j)
        while j>=0 and anchor < elements[j]:
        #for first iteration j index value is 0, anchor value is 9 and i index is 1
        # So, 1st iteration -> 0=0 and 9<11
            elements[j+1] = elements[j] # So, as 9 is less than 11 so, they are swapped
            j = j - 1 
        print("j value again after swap:", j) 
        elements[j+1] = anchor #pointer transerferred to next value

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
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
        insertion_sort(elements)
        #print(f'sorted array: {elements}')