def permutation(str1, str2):
    n1= len(str1)
    n2 = len(str2)
    if n1 != n2:
        return print("Not a permutation")
    a = sorted(str1)
    #str_1 = "".join(a)
    b = sorted(str2)
    #str_2 = "".join(b)
    if a == b:
        return (print("Yes string2: {} is a permutation of string 1: {}".format(str2,str1)))
    else:
        return print("Not a permutation")

#driver code
ele_1 = "rajesh"
ele_2 = "hejars"

permutation(ele_1,ele_2)
