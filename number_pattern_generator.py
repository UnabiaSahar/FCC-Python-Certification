def number_pattern(n):
    numbers = ' '
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n<1:
        return 'Argument must be an integer greater than 0.'

    for num in list(range(1,n+1)):
        numbers += str(num) + " "
    return numbers.strip()

print(number_pattern(4))