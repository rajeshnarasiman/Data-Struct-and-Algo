def kadanes(a):
    max_cur = max_glob = a[0]
    u= []
    for i in range (1, len(a)):
        max_cur = max(a[i], max_cur + a[i])

        if max_cur > max_glob:
            max_glob = max_cur

    return max_glob, u


a = [1,3,4,4,-9,6,7,-8,9]

print(kadanes(a))

