dict1 = {"aiyc": 123, "lilei": 520}
print(dict1.get("aiyc22","aiyc00"))

Set1 = {1, 3, 5, 7, 8}
Set2 = {2, 3, 5, 9,10}

#方法一
print((Set1 - Set2) | (Set2 - Set1))

#方法二
print((Set1 | Set2) - (Set1 & Set2))



