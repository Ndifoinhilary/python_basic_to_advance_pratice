test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

digit = [t for t in test_str if t.isdigit()]
str_data = {
    "length": len(test_str),
    "Digits": len(digit)
}

digits_only = [char for char in test_str if char.isdigit()]
length_of_digits = len(digits_only)
print(length_of_digits)
print(str_data)