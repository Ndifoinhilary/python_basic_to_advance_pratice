import string
test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

str_data = {
    "length": len(test_str),
    "Digits": len([t for t in test_str if t.isdigit()]),
    "Punctuations":len([p for p in test_str if p in string.punctuation]),
    "Unique": set{[t for t in test_str]}
}



print(str_data)