def linear_search(items, x):
    flag = 0
    for i in range(len(items)):
        if items[i] == x:
            flag = 1
            break
    if flag == 1:
        print("item found at position:", i + 1)
    else:
        print("item not found")
items = [5, 7, 10, 12, 15]
print("list of items is", items)
x = 10  
linear_search(items, x)
