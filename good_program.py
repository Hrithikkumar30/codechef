count = int (input())

for i in range(count):
    a = float(input())

    b = a/4
    c = a//4

    if b==c:
        print("Good")
    else:
        print("Not Good")
