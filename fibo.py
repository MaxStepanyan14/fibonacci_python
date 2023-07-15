f1, f2 = 0,1

n = int(input("Enter a number: "))

print(f1)
print(f2)

while n > 2:
    f1, f2 = f2, f1 + f2
    print(f2, end="\n")
    n -=1

input("\nEnter")
