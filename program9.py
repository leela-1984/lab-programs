digits=0
letters=0
input_string = input("Enter the string:")
for char in input_string:
    if char.isdigit():
        digits+=1
    elif char.isalpha():
        letters+=1
print("No. of letters:",letters)
print("No. of digits:",digits)