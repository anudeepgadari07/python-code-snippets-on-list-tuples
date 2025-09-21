# 1. Add all elements of a list
nums = [1, 2, 3, 4, 5]
print("1:", sum(nums))

# 2. Find max and min in a list
nums = [10, 20, 5, 30]
print("2: Max =", max(nums), "Min =", min(nums))

# 3. Count even and odd numbers in a list
nums = [1, 2, 3, 4, 5, 6]
even = len([x for x in nums if x % 2 == 0])
odd = len(nums) - even
print("3: Even =", even, "Odd =", odd)

# 4. Reverse a list without using reverse()
nums = [1, 2, 3, 4, 5]
print("4:", nums[::-1])

# 5. Remove duplicates from list
nums = [1, 2, 2, 3, 4, 4, 5]
print("5:", list(set(nums)))

# 6. Sort a list of strings by length
words = ["python", "is", "awesome"]
print("6:", sorted(words, key=len))

# 7. Find the second largest number in the list
nums = [10, 20, 4, 45, 99]
unique = list(set(nums))
unique.sort()
print("7:", unique[-2])

# 8. Find sum of all nested list elements
nested = [[1, 2], [3, 4], [5]]
print("8:", sum(sum(x) for x in nested))

# 9. Check if two lists are equal
a = [1, 2, 3]
b = [1, 2, 3]
print("9:", a == b)

# 10. Merge two lists and sort them
a = [3, 1, 4]
b = [6, 2, 5]
merged = sorted(a + b)
print("10:", merged)

# 11. Convert tuple to list and back
t = (1, 2, 3)
lst = list(t)
t2 = tuple(lst)
print("11:", lst, t2)

# 12. Check if the tuple contains a value
t = (1, 2, 3, 4)
print("12:", 3 in t)

# 13. Unpack a tuple into variables
t = (10, 20, 30)
a, b, c = t
print("13:", a, b, c)

# 14. Create a list of squares using comprehension
squares = [x*x for x in range(1, 6)]
print("14:", squares)

# 15. Count how many times a number appears in a list
nums = [1, 2, 2, 3, 2, 4]
print("15:", nums.count(2))

# 16. Find index of element in tuple
t = (10, 20, 30, 40)
print("16:", t.index(30))

# 17. Slice a tuple from index 1 to 3
t = (10, 20, 30, 40, 50)
print("17:", t[1:4])

# 18. Replace element in list with another
nums = [1, 2, 3, 4]
nums[2] = 99
print("18:", nums)

# 19. Filter only strings from mixed lists
mixed = [1, "hello", 3.5, "world", True]
strings = [x for x in mixed if isinstance(x, str)]
print("19:", strings)

# 20. Take input of the list from the user and print sum
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("20: Sum =", sum(nums))
