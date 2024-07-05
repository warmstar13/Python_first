# x = 0
# try:
#     x = 1
#     print(5/0)
# except FileNotFoundError:
#     print(x)
# except ZeroDivisionError:
#     print(x+1)


# try:
#     try:
#         print(5/0)
#     except:
#         print("1")
# except:
#     print("0")

# string = "hello, my name is john\nI want to work"
# list = string.split(" ")
# print(list)
# print(len(list))
# print(list[4])

num = input("Write a number")
num2 = input("Write a second number")
try:
    cur = int(num) + int(num2)
except ValueError:
    print("WRITE NUMBERS")
else:
    print(cur)
