def isHappy(n):
    def get_next(num):
        total = 0
        while num > 0:
            reminder = num % 10
            total += reminder**2
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


n = 19
print(isHappy(n))