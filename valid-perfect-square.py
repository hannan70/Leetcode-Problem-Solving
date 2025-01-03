
def isPerfectSquare(num):

    low = 1
    high = num

    while low <= high:
        mid = (low + high) // 2
        if mid*mid == num:
            return True
        elif mid*mid < num:
           low = mid + 1
        else:
            high = mid - 1

    return False


number = 14
print(isPerfectSquare(number))