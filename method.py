# METHODS OF LISTS
# 1. l.append(val)      [add one element at the end]
fruits = ["apple", "banana", "orange"]
fruits.append("kiwi")
print(fruits)

# 2. l.insert(idx, val) [insert element at index]
fruits = ["apple", "banana", "orange", "kiwi", "mango"]
fruits.insert(1, "guava")
print(fruits)


# 3. l.sort()             [arranges in incerasing order]
fruits.sort()
print(fruits)
# for decreasing order
fruits.sort(reverse = True)
print(fruits)

# 4. l.reverse ()         [reverses order]
marks= [89, 90, 78, 67, 90]
marks.reverse()
print(marks)
