def compute (a,b):
    product = a*b
    if product <=1000:
        return product
    else:
        return a+b 
a = int(input("Enter the 1st value:"))
b = int(input("Enter the 2nd value:"))
result = compute (a,b)
print (f"The result is: {result}")