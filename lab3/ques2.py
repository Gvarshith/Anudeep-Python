a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("before : ",a,",",b)
a,b = b,a
print("after : ",a,",",b)