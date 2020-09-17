'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    start = 0
    end = len(arr)-1
    while end - start > 1:
        if arr[start] == 0:
            while arr[end] == 0 and end-start > 1:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]
        start += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
