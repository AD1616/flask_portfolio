# Challenge 1:

var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))

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

average_List = [23, 41, 90, 55, 71, 83]

def averageList(list):

    # for i in range(len(average_List)):
    #     average_List[i] += 3

    temp = [x+3 for x in list]
    sum = 0

    for i in range(len(temp)):
        sum += temp[i]

    # print(len(temp))
    return (sum/len(temp))

avg = averageList(average_List)
print(avg)