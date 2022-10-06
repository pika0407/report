#백준 10818
'''
n = int(input())
nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]
for i in range(0, n):
    if int(nums[i]) > max_num:
        max_num = nums[i]
    if int(nums[i]) < min_num:
        min_num = nums[i]
print(min_num, max_num)
'''

'''
#백준 1978
n = int(input())
nums = list(map(int,input().split()))
rescnt = 0
for i in nums:
    cnt = 0
    if i == 1:
        continue
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        rescnt += 1
print(rescnt)
'''



