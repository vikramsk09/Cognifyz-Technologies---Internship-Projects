n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

