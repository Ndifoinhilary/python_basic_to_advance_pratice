even = [2,4,6,8,10,12,14,16,18,20]
old = [1,3,5,7,9,11,13,15,17,19]



even_squaares = list(e**2 for e in even if e > 4 and e < 16)

print(even_squaares)