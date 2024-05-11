def binary_search_original_index(arr, target):
    #create a list of tuples (value, original index) for each element in the array
    indexed_arr = [(value, index) for index, value in enumerate(arr)]
    #sort the indexed array based on the values
    indexed_arr.sort()
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        print(f'low = {low}, mid = {mid}, high = {high}')
        print(indexed_arr[low:high+1])
        if indexed_arr[mid][0] == target: #Check [0], the first part of the tuple which is the number
            return indexed_arr[mid][1]  #return the original index
        elif indexed_arr[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#test array
arr = [1, 3, 2, 10, 5, 7, 9, 4, 8, 6]
target = 7

#function call
result = binary_search_original_index(arr, target)

if result != -1:
    print(f"{target} can be found at index {result} of the array")
else:
    print(f"{target} is not present in the array")
