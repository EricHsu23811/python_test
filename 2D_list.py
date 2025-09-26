# 二維列表&巢狀迴圈 - https://youtu.be/zdMUJJKFdsU?si=DvAItS83hSExZJNL&t=10906

nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
    ]

# print(nums[0][0])
# print(nums[1][2])
# print(nums[3][0])

for row in nums:    # row:行、column:列 #逐一印出所有2D列表的每個值
    for col in row:
        print(col)