def sum(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
my_numbers=[12,11,10,5]
result = sum(my_numbers)
print(f"The sum of all elements is: {result}")