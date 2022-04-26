def count_bits(n):
    counter = 0
    bytes = bin(n)
    for char in bytes:
        if char == '1':
            counter = counter + 1
    return counter