numbers=(7,32,43,42,55,86,97,48,39)
count_odd=0
count_even=0
for x in numbers:
    if not x%2:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)