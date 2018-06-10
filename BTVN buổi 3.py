# alphabet = [ "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v"
#             , "w", "x", "y", "z", "a" ]
# User_word= input("Enter your data to count letters ")
# for i in range (len(alphabet)):
#     print(alphabet[i-1], " {0}".format((User_word.lower()).count(alphabet[i-1])))



# inventory = {
#     'gold' : 500,
#     'pouch' : ['flint', 'twine', 'gemstone'],
#     'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
# }
#
# inventory["pocket"] = []
# print(inventory)
#
# inventory["pocket"]=[ 'seashell', 'strange berry', 'lint']
# print(inventory)
#
#
# del inventory["backpack"][1]
# print(inventory)
#
# inventory["gold"] = [500,50]
# print(inventory)


# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
#
# }
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 3
#     "pear": 15
#
# }
#
# for fruit in prices:
#     for number in stock:
#         print("{0} \n"
#               "price: ".format(fruit),prices[fruit])
#         print("stock: ",stock[number])
#
# Total = 0
# for fruit in prices:
#     for number in stock:
#         Total = prices[fruit] * stock[number]
# print("Money earn ", Total)



# number = []
# for i in range(6):
#     A = int(input("Nhập số cho vào danh sách "))
#     number.insert(i-1, A)
# print(*number, sep = ", ")
# Number = int(input("Enter a number "))
# with count
# B = number.count(Number)
# if B>1:
#     print(Number, "appears", B, "times in my list")
# else:
#     print(Number,"appears", B, "time in my list")



# without count
# B = 0
# for i in range (len(number)):
#     if number[i-1] == Number:
#         B += 1
# if B>1:
#     print(Number, "appears", B, "times in my list")
# else:
#     print(Number,"appears", B, "time in my list")