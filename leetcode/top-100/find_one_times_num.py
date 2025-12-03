import os

def find_one_times_num(nums):
    res = 0
    for i in range(32):
        count = 0
        for num in nums:
            tag = 1 & (num >> i)
            if tag:
                count += 1
        if count % 3:
            if i == 31:
                res -= (1 << i)
            else:
                res |= (1 << i)
    return res

if __name__ == "__main__":
    nums = [1,1,1,2,3,3,3]
    num = find_one_times_num(nums)
    print(num)