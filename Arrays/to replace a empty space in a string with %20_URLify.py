def replace(s):
    str = ""
    for i in s:
        if i == " ":
            str += "%20"
        else:
            str += i
    return str

#driver function

url = "I am very at coding"

print(replace(url))