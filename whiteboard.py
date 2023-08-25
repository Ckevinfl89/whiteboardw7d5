# Write a Python program to add the digits of a positive integer 
# repeatedly until the result has a single digit.


# EX
# Input:
# n1=48
# # 4+8=12
# # 1+2=3
# # Output:
# # 3

# # Input
# n2=59
# Output
# 5

def solution(num):
    # while num >= 10:
    #     new_num = 0
    #     while num > 0:
    #         new_num += num % 10
    #         num //= 10
    #     num = new_num
    # return num
    while num >= 10:
        new_num = 0
        for digit in str(num):
            new_num += int(digit)
        num = new_num
    return num