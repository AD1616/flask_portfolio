# Challenge 1:

var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1, ": integer")
print(var2, ": string")
print(var3, ": character")
print(var4, ": float")

# Challenge 2:

list1 = [5,3,4,1,2, 8, 10, 2]
list2 = list1
def orderList(list):

    list3 = []
    while len(list) > 0:
        smallest = min(list)
        list3.append(smallest)
        list.remove(smallest)
    print(list3)


orderList(list2)

# Challenge 3:

averageList = [23, 41, 90, 55, 71, 83, 69]

def avg(list):

    list3 = []
    while len(list) > 0:
        smallest = min(list)
        smallest = smallest + 3
        list3.append(smallest)
        list.remove(smallest)
    print(list3)

avg(list2)