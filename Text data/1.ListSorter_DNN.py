list1 = input("Enter a list of numbers separated by commas: ")
# за да разделим списъка със запетая
number_strings = list1.split(',')
# създаваме нов списък numbers; прави итерации минавайки през всеки елемент от списъка;
# и ги превръща в числа;  Превръща текстовия низ в числов
numbers = [int(i) for i in number_strings]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)