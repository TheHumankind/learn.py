
def add(*nums):
    sum = 0
    # nums = list(nums)
    # nums.append(1)
    for i in nums:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8,9))
