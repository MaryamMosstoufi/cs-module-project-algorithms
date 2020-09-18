'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):

    # with zero solution:
    product = 1
    if arr.count(0) == 0:
        for i in arr:
            product *= i
        for i in range(0, len(arr)):
            temp = arr[i]
            arr[i] = product // temp
        return arr
    elif arr.count(0) == 1:
        for i in range(0, len(arr)):
            if arr[i] == 0:
                arr[i] = 1
                zero = i
            product *= arr[i]
        for i in range(0, len(arr)):
            if i == zero:
                arr[i] = product
            else:
                arr[i] = 0
        return arr
    elif arr.count(0) > 1:
        return[0]*len(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
