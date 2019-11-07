def rev(num):
    empty = []
    for nums in num:
        rev = 0
        while (nums > 0):
            a = nums % 10
            rev = (rev*10) + a
            nums = nums // 10
        empty.append(rev)
    return max(empty)

# Driver Function 
num = [256]
int_rev(num)
