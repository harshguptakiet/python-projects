def find_single(nums):
    single = 0
    for num in nums:
        single ^= num
    return single

# Initialize the list
lst = []

# Read the number of elements
a = int(input())

# Read each element and append to the list
for i in range(a):
    num = int(input())
    lst.append(num)

# Find the single element
result = find_single(lst)
print(result)
