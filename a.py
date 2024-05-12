#phần 1
# color = ["blue","red","green"]
# print(color)
# a = input("nhập thêm màu: ")
# color.append(a)
# print(color)

#phần 2
# a =int(input("nhập vị trí: "))
# print(color[a])
# a =int(input("xóa màu: "))
# color.remove("red")
# print(color)

#phần 3
#bài 1
# list = [5,54,121,334]
# a =int( input("tìm số: "))
# if a in list:
#   print("Yes")
#Bài 2
# nums = [1, 2, 3, 4, 5, 6]
# def totalNums(x):
#     sum = 0
#     for i in x:
#         sum += i
#     return sum
# print(totalNums(nums))
#bài 3
# list = []
# n = input("Nhập số: ")
# while not n == "0" :
#     n = input("Nhập tiếp: ")
#     list.append(n)
# print(list) 
    
#phần 4
#bài 1
# list = [5, 1, 8, 92, 7, 30]
# for i in list:
#     if i % 2 == 0:
#         print(i)
#phần 7
#bài 1
# high_scores = [70,80,90]
# new_scores = input("nhập điểm mới: ")
#bài 2
# high_scores.append(new_scores)
# print(high_scores)
#phần 8
#bài 1
thislist = [100, 50, 65, 82, 23, 11]
# thislist.reverse()
thislist.sort(reverse = True)
print(thislist)
