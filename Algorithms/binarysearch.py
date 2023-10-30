from util import time_it

@time_it 
#Timeit is a module in the Python standard library that provides various functions 
# for measuring the execution times of small portions of code
def linear_search(numbers_list, number_to_find):
    #When we have list of elements and we call them using enumerate then it will return
    #index of list as well as values
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1 #When no result found it will return -1


@time_it
def binary_search(numbers_list, number_to_find):
#Intially, left, mid indexes will be zero and right indexes will be last element's index
    left_index = 0
    right_index = len(numbers_list) - 1 #last element & list start from zero so, that's 
    #why minus-ing
    mid_index = 0

#[4,9,11,17,21,25,29,32,38]
#While executing the binary search we have to look for indexes like in the
#first iteration the left index will be zero for assumed list and right will be 8
#In second iteration as we already discard all the elements to the left of 21 including 21
#So, in third iteration the left index will be 5 and right will be 8 and so, again
#we will divide it by and will get target as 32
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2 #Floor divison as it returns the 
        #integer's value like if 2.5 after divide it will give 2 as answer
        mid_number = numbers_list[mid_index]


        #if midnumber equal to target then return the number's index
        if mid_number == number_to_find:
            return mid_index

        #if number to find is greater than target then increment index or move right
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            #if the number target is less than the number you are currently on then
            #decrement the mid index
            right_index = mid_index - 1

    return -1


#We can also use recursion for the problem too, because we are doing or calling the 
#samething and then performing the recursion based on that.

#Actually, we are doing recursive functionality in the same right and left index's boundary
#again and again and if we don't find any element in there we will set left and 
#right index again

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    #print(f"Number found at index {index} using binary search")
    #print(f"{linear_search([2,5,7,9,10,12], 14)}")