# 1. Print number from 1 to 5.

"""i = 1
while i <= 5:
    print(i)
    i += 1"""

# 2. Take value from user and output the sum of it.

"""n = int(input("Enter a number: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i += 1

print("Sum =", sum)"""

# 3. Print odd numbers from 1 to 20.

"""i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1"""

# 4. Print table of 4.

"""i = 1
while i <= 10:
    print("4 x", i, "=", 4 * i)
    i += 1"""

# 5. Print reverse number.

"""i = 10
while i >= 1:
    print(i)
    i -= 1"""

# 6. Find largest number in list.

"""lst = [10, 25, 5, 40, 30]
i = 0
largest = lst[0]

while i < len(lst):
    if lst[i] > largest:
        largest = lst[i]
    i += 1

print("Largest number =", largest)"""

# 7. Print even numbers between 1 to 20.

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1