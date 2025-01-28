def generate(numRows):
    new_list = []
    for row in range(1, numRows+1):
        n = 1
        current_row = []
        for space in range(numRows - row):
            print(" ", end="")
        for col in range(row):
            if row == 1 or col == 0:
               n = 1
            else:
                n = n * (row - col) // col
            current_row.append(n)
            print(f"{n} ", end="")
        new_list.append(current_row)
        print()


    return new_list



numRows = 5
print(generate(numRows))
