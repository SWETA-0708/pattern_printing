def print_diamond(rows):
    # Upper part of the diamond
    for i in range(1, rows, 2):
        print(" " * ((rows - i) // 2) + "*" * i)

    # Lower part of the diamond
    for i in range(rows, 0, -2):
        print(" " * ((rows - i) // 2) + "*" * i)

# Set the number of rows for the diamond (should be an odd number for symmetry)
num_rows = 7
print_diamond(num_rows)
