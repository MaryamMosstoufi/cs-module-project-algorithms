'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n, ways={0: 1, 1: 1, 2: 2}):

#     if n in ways:
#         return ways[n]

#     ways[n] = eating_cookies(
#         n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

#     return ways[n]


def eating_cookies(n, a={}):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    # Our base cases are 0:1, 1:1, 2:2
    base = [1, 1, 2]
    # Notice that adding these gives 4, i.e. eating_cookies(3)
    # Notice sum(1, 2, 4) = 7, i.e. eating_cookies(4)
    # Notice sum(2, 4, 7) = 13, i.e. eating_cookies(5)
    # Instead of recursively calling the funciton, let's just store the
    # values in a list, base, and sum the last three elements
    # To get to this point, n > 2, so we iterate n-2 times
    for _ in range(2, n):
        cookies = base[-3] + base[-2] + base[-1]
        # Then append the new value to the end of the list to continue iteration
        base.append(cookies)
    # Return the last element of the list
    # return base[-1]
    # Easier to just return the variable cookies!
    return cookies


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
