number = int(input("Enter the number to print the multiplication table:"))
upto = int(input("Enter upto which you want to print the multiplication table:"))
print ("The multiplication table of:",number)
for count in range (1, upto +1):
    print (number,'x',count,'=',number*count)