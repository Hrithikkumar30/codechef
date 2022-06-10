count = int (input())
for i in range(count):
    
    a , b,c  = map(int , input().split(" "))

    if a*c < b:
        print("yes")
    else:
            print("no")


# while True:
#     try:
#         for i in range (int(input())):
#             a = 5
#             b=10
#             c = int(input())
#             if a*c < b:
#                 print("yes")
#             else:
#                 print("no")
#     except:
#         break
