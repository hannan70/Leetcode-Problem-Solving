
def romanToInt(s):
        dist = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        last_value = 0

        for i in range(len(s) - 1, -1, -1):
            current_value = dist[s[i]]

            if current_value < last_value:
                sum -= current_value
            else:
                sum += current_value

            last_value = current_value

        return sum


s = 'MCMXCIV'
print(romanToInt(s))
