UC=0
LC=0
SC=0
input_string=input("Enter the string:")
for char in input_string:
    if char.isupper():
        UC+=1
    elif char.islower():
        LC+=1
    elif char.isspace():
        SC+=1
print("UC:",UC)
print("LC:",LC)
print("SC:",SC)
print(input_string.swapcase())