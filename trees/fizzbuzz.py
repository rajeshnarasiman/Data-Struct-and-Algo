def fizzbuzz(n):
    a = []
    fizz_buzz_dict = {3:"Buzz",5:"Fizz",7:"Tuzz"}
    for i in range(len(n)):
        empty = ""
        for key in fizz_buzz_dict.keys():
            if n[i] % key == 0:
                empty += fizz_buzz_dict[key]
        if not empty:
            empty = str(n[i])
        a.append(empty)
    return a
# Driver function
n = [1,3,5,20,60,35]
fizzbuzz(n)
