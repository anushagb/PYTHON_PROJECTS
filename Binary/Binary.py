import random
import time


def binary_search(l , target, low = None, high = None):
    if low is None:
        low = 0 
    if high is None:
        high = len(l)-1
    if high < low:
        return -1
    mid = (low + high) //2 
    if l[mid] == target:
        return mid
    elif target < l[mid]:
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l , target, mid+1, high)

if __name__ == '__main__':
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_list = list(map(int, user_input.split()))

    target = int(input("Enter the number to search for: "))

    print("User's list:", user_list)
    print("Target:", target)

   

    start = time.perf_counter()
    binary_result = binary_search(user_list, target)
    end = time.perf_counter()
    binary_time = end - start

    print("Binary search result:", binary_result)

    
    if binary_result != -1:
        print("Binary search found the target at index:", binary_result)
    else:
        print("Binary search did not find the target.")

    print("Binary search time:", binary_time, "seconds.")
