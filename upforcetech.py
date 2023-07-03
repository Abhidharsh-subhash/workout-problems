# arr = [1, 1, 1, 3, 5, 5, 7, 7, 2, 0, 0, 0, 8]
# output = [1, 2, 5, 7, 2, 0, 8]

def remove_consecutive_repeating(arr):
    if len(arr) == 0:
        return []
    else:
        result = [arr[0]]  # Initialize the result list with the first element

        for i in range(1, len(arr)):
            if arr[i] != result[-1]:
                result.append(arr[i])

        return result
arr=[1, 1, 1, 2, 5, 5, 7, 7, 2, 0, 0, 0, 8]
print(remove_consecutive_repeating(arr))