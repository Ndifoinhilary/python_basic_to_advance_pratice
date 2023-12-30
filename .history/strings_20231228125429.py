test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"


str_data = {
    "length": len(test_str),
    "Digits": list((t for t in test_str if t.isnumeric))
}


print(str_data)